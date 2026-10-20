# 项目架构 / 模块依赖 / 函数调用树 分析报告

> 全部结果由 **纯静态分析 (Python `ast`)** 生成：未导入、未运行任何业务代码（无串口/转台/电源/文件删除等副作用），未修改任何业务文件；所有产物都在本目录 `analysis_report/` 内。
> 重新生成：`python analysis_report/tools/render.py`（会调用 `analyze.py`），自检：`python analysis_report/tools/check.py`，查询某函数上下游：`python analysis_report/tools/query.py begin_test --depth 3`。

## 1. 分析范围与入口
| 项 | 结果 |
|---|---|
| 语言/框架 | Python 3 + PyQt5 + pyqtgraph + pyserial + pandas/numpy |
| 已分析 | 38 个 `.py`（38/38，无语法错误）→ 616 个函数/方法(含每模块 `<module>` 伪函数)、36 个类、957 条调用关系 |
| 已排除 | `.git`、`__pycache__`、`旧文件/`（283 个历史归档文件，仅清点）、`test_fun/`（1457 个样例数据 txt）、规则/配置 txt、二进制包 (`.zip/.7z/.exe`) |
| 测试代码 | 未发现 `test_*.py`/pytest/unittest；`test_fun/` 是数据而非测试 |
| **当前主入口** | `通用自动测试上位机V0.95.py`（`if __name__ == '__main__'`，L4487）→ `MainWindow`，继承 `QMainWindow + Automated_testingV19.Ui_MainWindow` |
| 旧版入口 | `通用自动测试上位机V0.90.py`（遗留，引用 `Automated_testingV17`，与 V0.95 有大量逐字重复函数）|
| 疑似未使用 | `Automated_testingV20.py`(未被导入的新 UI)、`Automated_testing.py`/`sample_testingV13.py`(仅 pyuic 注释的空壳)、`funs/checks.py`、`funs/checks_remove.py`(与 `fun_checks.py` 重复)、`.ui` 文件仅为设计源 |

### 启动流程（已在代码中核对）
`__main__` → 导入期 `_prepare_runtime_workdir()` 切换工作目录 → `MainWindow.__init__`（读 `配置文件/debug_mode.ini`，`setupUi`，`show`）→ `QTimer.singleShot(50, init_after_show)` → `_init_modules_in_batches()` 依据 `module_chain` 列表用 `setattr(self, attr, cls(self))` **动态**实例化 17 个 manager（`init_ini/debug/init_ui/times/settings/constants/events/threads/uilogic/getui/events_devide/events_hidden/tools_*/navs`，各自保存 `self.mw=MainWindow`）→ `init_after_show` 其余 ~600 行完成状态变量初始化和 `signal.connect` → `app.exec_()` 事件循环。

## 2. 架构分层（图1）
入口(主窗口) → UI层(`Automated_testingV19`,`ui.init_ui`,`ui.inits.*`,`ui.get_ui`) → 事件层(`ui.logic` 负责 connect，`ui.event`/`ui.events.*` 为槽) → 业务逻辑层(`ui.times/debug/threads`,`ui.tools.*`,`ui.navs`) → 数据处理层(`ui.structs`,`funs.fun_chy2`,`funs.fun_sate`) → 设备通信层(`funs.fun_serial`,`ui.tools.tools_burn_ymodem`) ；配置层(`ui.settings/load_ini/constants`,`funs.fun_locals`,`inits_funcTest`) 与公共工具层(`funs.fun_checks`)。每个模块的职责见 `project_inventory.json` → `modules[].role`（依据实际类/函数阅读得出）。
> 注意：串口读写并不集中在设备层：`ui.structs`(三轴转台串口)、`ui.event`(`clickEvent_decodeShow_tryReceive`)、主窗口(`power_serials.write`、`threading_receive_data/sate`、`begin_test_bd`)都直接使用 `serial`。

## 3. 核心调用链（详见 `function_trees/`）
1. **启动**：`<module>` →create→ `MainWindow.__init__` →timer→ `init_after_show` → `_init_modules_in_batches` →dynamic→ 17 个 manager `__init__`；`MainWindowLogic.__init__` 建立约 30 个 `控件信号 → MainWindowEvent.*` 的 connect（`ui.logic → ui.event` 26 处，是最强的运行期耦合）。
2. **开始测试**：`pushButton_begin_test.clicked` →connect→ `begin_test` → `read_rules` / `only_test`(→ 线程 `threading_receive_sate/data` → `fun_serial.tryOpenSerial` → `serial.Serial`) / `bd_test`(→ 线程 `begin_test_bd` → `Turntable_class.*` 指令构造 → 串口 write) / `bd3x_test` / `plan_test`(→ 线程 `plan_test_threading` → `only_test`/`bd_test`/`event_power_off` → `power_serials.write`)。时序图见 `diagrams/sequence_flow*_begin_test.mmd`。
3. **电源/温箱/三轴**：`event_power_on/off`、`MainWindowEventDevide.clickEvent_turntable3x_*` →`struct_turnTable3x.sendAndRec` → 串口。
4. **定时器**：`show_message_01s/05s/1s/2s/5s`、`event_send_sate1/2`、`event_td_send1`、`event_fz_send1`、`event_gnss_send1`（`QTimer.timeout.connect`，共 16 条 timer 边）。
5. **线程**：`QThread` 子类 3 个（`clickEventThread_decodeShow`、`class_Worker`、`YModemBurnWorker`）+ `threading.Thread(target=…)` 6 处；共 114 条信号槽 connect（非旧版）。

## 4. 模块关系 / 循环依赖 / 高耦合（图2）
* **import 层面无循环依赖**（Tarjan SCC 结果为空）。
* **运行期存在隐式双向耦合**：每个 manager 通过 `self.mw` 回调 `MainWindow`，主窗口又通过 `module_chain` 持有 manager——这在 import 图中不可见，是最主要的架构耦合（`self.mw.` 引用共约 560 处，绝大多数是控件访问）。
* 高耦合/热点：`通用自动测试上位机V0.95`(fan-out 19；4491 行；`init_after_show` 单函数 619 行)，`funs.fun_chy2`(被 5 模块导入，且被 `from … import *` 泄漏名称)，`funs.fun_locals`(fan-in 6)，`ui.event`(706 行，124 处 `self.mw`)，`ui.structs`(35 个方法无静态调用者，实为通过 `mw.constants.structList_12tab[i].xxx` 动态访问)。
* 函数级递归：`int2hex`(V0.90/V0.95)、`del_empty_folder`(fun_chy2、init_ui)、`MainWindowNavLoc._infer_xyz_tile_layout`，调用树中以 ↻ 标注，不再展开。
* 重复实现：`funs/checks.py`、`checks_remove.py`、`fun_checks.py` 三份 CRC；V0.95 内重复定义 `GPGGA2loc/sate2location/check2serial…`，与 `funs` 重复；`Turntable_class.reset_inside/outside` 在类内重复定义两次（后者覆盖前者，L4442/L4449 覆盖 L4428/L4435）。

## 5. 无法静态确定的关系（`function_trees/06_dynamic_and_unresolved.txt`，均为「待人工确认」）
* `getattr/setattr/hasattr` 反射（V0.95 45 处、`nav_loc` 41 处等）；主窗口通过 `setattr(self, attr, cls(self))` 挂载 manager —— 已根据 `module_chain` 元组人工建模为 `dynamic/medium` 边。
* `connect()` 的槽为运行期对象属性/下标表达式（如 `structList_12tab[i].switch_open`，`ui/logic.py:53`）。
* 参数/局部可调用对象：`try_set_text/try_get_text` 中的 `types(...)`、`tools_bdcalib` 中动态导入的 matplotlib formatter。
* **规则文本 DSL**：`解算规则/标定规则/装订规则/自动规则/…` 的 txt 由 `funs.fun_chy2.class_rule` 与各 `logic_read*` 在运行期解析并驱动测试流程，规则内容与代码之间的关系无法静态推导。
* 属性式 I/O：`obj.serials.write()`、`mw.constants.struct_sate.serials` 等串口对象存放于结构体属性，静态上仅能用启发式(`*serial*.write/read`)标记 `hardware_io`。
* 多态：同名方法按类解析；未使用方法名全局唯一匹配以外的猜测。仅按“方法名唯一”推测的关系标为 `low`。

## 6. 可信度与边类型
| 可信度 | 含义 |
|---|---|
| high | 名称/导入/`self.method` 等静态可确定 |
| medium | 经 `self.mw`、`module_chain` 挂载、局部变量类型、lambda/partial 推断 |
| low | 仅按方法名在项目内唯一匹配推测 |
| manual | 待人工确认（见第 5 节清单） |

边类型：`call` 直接调用；`create` 对象创建；`connect` 信号槽(间接)；`timer` 定时器回调(间接)；`thread` 线程入口(间接)；`dynamic` 动态分发(间接)；`import` 模块导入。**引用（如把函数作为回调传递）只记录为 connect/timer/thread，不当作直接调用。**

## 7. 文件清单与查看方式
| 文件 | 说明 |
|---|---|
| `index.html` | **交互式报告**（本地打开即可，无需联网/依赖）：左侧文件树+搜索，中间 模块依赖图 / 函数调用图 / 调用树（缩放、拖动、过滤、双击展开），右侧详情（定义行号、调用者/被调用者、`vscode://file/…` 定位链接，可在顶部修改源码根路径）|
| `diagrams/index.html` | Mermaid 图集（图1-6，含图例/说明；使用 `vendor/mermaid.min.js` v10.9.1 MIT，离线渲染）|
| `architecture.mmd` `module_dependencies.mmd` `startup_flow.mmd` | 图1/2/5 源文件（`diagrams/` 中另有 `class_relationships.mmd`、`call_tree_entry.mmd`、`sequence_flow*.mmd`、`by_module/*.mmd` 局部调用树）|
| `project_tree.txt` / `project_inventory.json` / `project_inventory_modules.json` | 目录树、文件分类、入口、线程/定时器、第三方依赖、每模块职责/层/导入关系 |
| `module_dependencies.json` | import 边(含行号)、循环、fan-in/out、运行期调用耦合、第三方库 |
| `function_index.json` | 616 个函数：稳定 ID(`模块::限定名`)、文件、行号区间、参数、装饰器、标志(qt_slot/timer_callback/thread_entry/hardware_io/entry…)、直接调用/被调用、外部库调用、动态点 |
| `function_call_graph.json` | 全部调用边：src/dst/kind/conf/行号/表达式/说明 + 函数级循环 |
| `class_relationships.json` | 类、继承、组合、创建位置、manager 挂载 |
| `dynamic_and_unresolved.json` / `quality_findings.json` | 动态/待确认清单；无调用者函数、重复实现、同名函数 |
| `function_trees/` | `01_entry_tree.txt` 入口全量调用树（`01b` 为 4 层精简版）、`by_module/`、`by_class/`、`05_ui_event_to_hardware_chains.txt`、`06_dynamic_and_unresolved.txt` |
| `quality_report.json` | `check.py` 自检结果 |
| `tools/` | `analyze.py`(静态分析)、`render.py`(报告生成)、`check.py`、`query.py`、`viewer_template.html` |

增量更新：节点 ID 为 `相对模块路径点号名::类.方法`（重复定义追加 `#L行号`），可对两次 JSON 做 diff。

## 8. 质量检查结果（`quality_report.json`）
* 应分析的 38 个 `.py` 全部扫描；排除了缓存/旧文件归档/样例数据；无语法错误。
* 每个函数的定义行号均与源码 `def` 对应（0 处不符）；每条调用边的行号均落在调用者函数范围内；无悬空边。
* 外部依赖（均未在仓库内提供，仅静态记录）：PyQt5、pyqtgraph、pyserial、pandas、numpy、debugpy(注释残留)。无无法解析的内部模块导入。
* 业务代码 0 处修改；未执行任何业务程序。
* 已知局限：`self.mw.<控件>.<方法>()` 这类 Qt 控件调用不当作内部调用；`low` 可信度边仅供参考。

## 9. 推荐的后续重构顺序
1. **清理死代码与重复**：移除/归档 `funs/checks*.py`、`Automated_testingV20/V17`、V0.90；把 V0.95 内重复的工具函数(`hex2int/int2hex/reverse/GPGGA2loc…`)统一到 `funs`，消除 `import *`。
2. **拆分 `init_after_show`(619 行) 与 `MainWindow`**：把 connect 全部迁入 `ui.logic`，状态变量迁入 `ui.settings/constants`。
3. **显式依赖注入替换 `self.mw` + `setattr` 动态挂载**：为 manager 声明明确接口，打破 MainWindow↔manager 隐式循环，并使静态分析/IDE 跳转可用。
4. **串口访问集中**：所有 `serial` 读写收敛到 `funs.fun_serial`/设备适配层，上层不直接持有 `serial` 对象，便于加入模拟设备进行无硬件测试。
5. **补充测试**：优先覆盖 `funs.fun_chy2.class_rule`、`fun_checks`、`fun_sate`、`Turntable_class` 指令构造等纯函数。
6. **规则 DSL 文档化/校验**：为规则 txt 增加 schema 校验，补上规则→代码的可追溯性。
