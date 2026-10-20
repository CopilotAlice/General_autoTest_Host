#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""基于 analyze.py 的结果生成: 目录树/清单/调用树/Mermaid/HTML. 只读源码, 只写 analysis_report/."""
import os, sys, json, shutil, collections, datetime, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analyze as A

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..'))
ROOT = os.path.abspath(os.path.join(OUT, '..'))

LAYERS = ['入口', 'UI层', '事件层', '业务逻辑层', '数据处理层', '设备通信层', '配置层', '公共工具层']
# 模块 -> (层, 职责). 职责依据阅读各模块的类/函数定义写成, 并在 README 中说明验证方式
ROLES = {
 '通用自动测试上位机V0.95': ('入口', '当前主程序: MainWindow(QMainWindow+Ui_MainWindow); 启动、manager 动态挂载(module_chain)、定时器/串口收发线程、测试流程(begin/bd/plan_test)、绘图、转台指令类 Turntable_class'),
 '通用自动测试上位机V0.90': ('入口', '[旧版/遗留] 被 V0.95 取代的主程序, 引用 Automated_testingV17; 与 V0.95 存在大量逐字重复函数'),
 'Automated_testingV19': ('UI层', 'pyuic5 生成的 Ui_MainWindow (V0.95 使用), 仅 setupUi/retranslateUi'),
 'Automated_testingV20': ('UI层', 'pyuic5 生成的 Ui_MainWindow V2.0, 未被任何模块导入(疑似未启用的新界面)'),
 'Automated_testingV17': ('UI层', 'pyuic5 生成的 Ui_MainWindow V1.7 (仅旧版 V0.90 使用)'),
 'Automated_testing': ('UI层', 'pyuic5 空壳(仅注释), 无定义'),
 'sample_testingV13': ('UI层', 'pyuic5 空壳(仅注释), 无定义'),
 'ui': ('公共工具层', '包标记 ui/__init__.py (仅文档字符串)'),
 'ui.init_ui': ('UI层', 'MainWindowInit: 控件初始化/绘图控件/时间/提示/路径; 另含 struct_paraCal 标定参数处理类与均值函数'),
 'ui.inits': ('UI层', '包: 导出 MainWindowInitDebugMsg/ShowMsg/FuncTest'),
 'ui.inits.inits_debugMsg': ('UI层', 'MainWindowInitDebugMsg: 调试信息占位初始化'),
 'ui.inits.inits_showMsg': ('UI层', 'MainWindowInitShowMsg: 显示信息处理初始化 (init_showMsg_process)'),
 'ui.inits.inits_funcTest': ('配置层', 'MainWindowInitFuncTest: 读取 functest_config.ini, 机器码校验(uuid/hashlib), 按配置隐藏功能分组'),
 'ui.load_ini': ('配置层', 'MainWindowInitIni: 读取 debug_mode / ui 配置 ini'),
 'ui.settings': ('配置层', 'MainWindowSetting: 默认配置、para_com/para_config/root_config 读取'),
 'ui.constants': ('配置层', 'MainWindowConstants: 初始化路径、12 路设置、装订结构、发送结构、三轴结构(持有 ui.structs 对象)'),
 'ui.structs': ('数据处理层', '数据/设备状态结构: struct_general_bind, struct_tab_setting(串口配置控件封装), struct_sate(卫导), struct_turnTable3x(三轴转台串口), clickEventThread_decodeShow(QThread)'),
 'ui.logic': ('事件层', 'MainWindowLogic: 集中完成控件信号 -> ui.event/ui.events 槽函数的 connect 连接'),
 'ui.event': ('事件层', 'MainWindowEvent: 点击/变更事件处理(装订、解算显示、自动发送、规则切换等)'),
 'ui.events': ('事件层', '包: 导出 MainWindowEventDevide/Hidden'),
 'ui.events.events_devide': ('事件层', 'MainWindowEventDevide: 温箱与三轴转台控制事件(串口开关/指令/转动)'),
 'ui.events.events_hidden': ('事件层', 'MainWindowEventHidden: 隐藏控件显示切换事件'),
 'ui.times': ('业务逻辑层', 'MainWindowTimes: 测试计时/下拉框刷新等 QTimer 事件'),
 'ui.threads': ('业务逻辑层', 'MainWindowThread: 仅保存 mainWindow 引用的占位类'),
 'ui.debug': ('业务逻辑层', 'MainWindowDebug/struct_debug: 调试信息定时显示'),
 'ui.get_ui': ('UI层', 'MainWindowGetUI: 获取路径下拉框名称等界面取值辅助'),
 'ui.navs': ('业务逻辑层', '包: 导出 MainWindowNavLoc'),
 'ui.navs.nav_loc': ('业务逻辑层', 'MainWindowNavLoc/IMUColumnConfigDialog: 惯导轨迹/离线地图(瓦片/SVG)加载与绘制'),
 'ui.tools': ('业务逻辑层', '包: 导出 MainWindowToolBdcalib/BurnYmodem'),
 'ui.tools.tools_bdcalib': ('业务逻辑层', 'MainWindowToolBdcalib + class_Worker(QThread): 标定数据预览/平均/参数计算/多项式拟合/生成 bin'),
 'ui.tools.tools_burn_ymodem': ('设备通信层', 'YModemBurnWorker(QThread) + MainWindowToolBurnYmodem: 通过 pyserial 以 YModem 协议烧录固件'),
 'funs.fun_chy2': ('数据处理层', '规则解析与通用函数: class_rule(解算规则文件解析/十六进制解码)、try_* 类型转换、转台/天线/GNSS 指令构造、机器码'),
 'funs.fun_checks': ('公共工具层', 'CRC16/CRC32 等校验函数'),
 'funs.checks': ('公共工具层', 'fun_checks 的重复副本(疑似废弃)'),
 'funs.checks_remove': ('公共工具层', 'fun_checks 的重复副本(文件名带 remove, 疑似废弃)'),
 'funs.fun_sate': ('数据处理层', '卫导 NMEA/KSXT/HEADINGA 报文 -> 位置/速度解析'),
 'funs.fun_serial': ('设备通信层', 'pyserial 封装: tryOpenSerial / tryOpenAndSend (含重试)'),
 'funs.fun_locals': ('配置层', '规则类型/目录名映射常量 locals_model_list'),
}
LAYER_ORDER = {l: i for i, l in enumerate(LAYERS)}
CHAIN_OF_INTEREST_KINDS = ('call', 'create', 'connect', 'timer', 'thread', 'dynamic')


def layer_of(m):
    return ROLES.get(m, ('公共工具层', ''))[0]


def short(fid):
    return fid.split('::', 1)[-1]


def label(f):
    return f'{f.module}::{f.qualname}'


def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(text)


def wj(path, obj):
    w(path, json.dumps(obj, ensure_ascii=False, indent=1))


def esc(s):
    return s.replace('"', "'").replace('<', '‹').replace('>', '›')


# ------------------------------------------------------------------ 目录树/清单
def project_tree():
    skip = {'.git', '__pycache__', 'analysis_report'}
    lines = [os.path.basename(ROOT) + '/']

    def rec(d, prefix):
        ents = sorted(os.listdir(d), key=lambda x: (not os.path.isdir(os.path.join(d, x)), x))
        ents = [e for e in ents if e not in skip]
        for i, e in enumerate(ents):
            p = os.path.join(d, e)
            last = i == len(ents) - 1
            br = '└── ' if last else '├── '
            if os.path.isdir(p):
                files = [f for _, _, fs in os.walk(p) for f in fs]
                py = sum(1 for f in files if f.endswith('.py'))
                dense = len(files) > 12 and py == 0 or e in ('test_fun', '旧文件')
                lines.append(f'{prefix}{br}{e}/' + (f'   [{len(files)} 个文件, 其中 {py} 个 .py, 已折叠]' if dense else ''))
                if not dense:
                    rec(p, prefix + ('    ' if last else '│   '))
            else:
                lines.append(f'{prefix}{br}{e}')
    rec(ROOT, '')
    return '\n'.join(lines) + '\n'


def categorize():
    cats = collections.defaultdict(list)
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in ('.git', '__pycache__', 'analysis_report')]
        for f in fns:
            rel = os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, '/')
            ext = os.path.splitext(f)[1].lower()
            top = rel.split('/')[0]
            if top == '旧文件':
                c = 'legacy_archive(旧文件/, 未纳入分析)'
            elif top == 'test_fun':
                c = 'test_data(test_fun/ 样例数据)'
            elif ext == '.py':
                c = 'python_source'
            elif ext == '.ui':
                c = 'qt_ui_designer'
            elif ext == '.ini' or top == '配置文件':
                c = 'config(配置文件/)'
            elif top.endswith('规则'):
                c = 'rule_files(' + top + ', 运行期由 class_rule/MainWindowLogic 读取)'
            elif ext == '.ipynb':
                c = 'notebook'
            elif ext in ('.zip', '.7z', '.exe'):
                c = 'binary_archive'
            elif ext in ('.json', '.md', '.txt'):
                c = 'other_text'
            else:
                c = 'other'
            cats[c].append(rel)
    return cats


# ------------------------------------------------------------------ 树
def children_of(P):
    ch = collections.defaultdict(list)
    for e in P['edges']:
        if e['kind'] in CHAIN_OF_INTEREST_KINDS and e['dst'] in P['funcs']:
            ch[e['src']].append(e)
    for k in ch:
        ch[k].sort(key=lambda e: (e['line'], e['dst']))
    return ch


def tree_text(P, ch, root, maxdepth=60, expanded=None, indent='', depth=0, path=(), out=None, edge=None):
    F = P['funcs']
    out = [] if out is None else out
    expanded = set() if expanded is None else expanded
    f = F[root]
    tag = ''
    if edge:
        tag = f"[{edge['kind']}/{edge['conf']}@L{edge['line']}] "
    mark = ''
    if root in path:
        out.append(f'{indent}{tag}{label(f)}  ↻ 递归/循环调用(不再展开)  ({f.file}:{f.line})')
        return out
    if root in expanded and ch.get(root):
        out.append(f'{indent}{tag}{label(f)}  ↑ 已在上文展开  ({f.file}:{f.line})')
        return out
    flags = ','.join(sorted(f.flags - {'constructor'}))
    out.append(f'{indent}{tag}{label(f)}  ({f.file}:{f.line})' + (f'  <{flags}>' if flags else ''))
    expanded.add(root)
    if depth >= maxdepth:
        return out
    groups = collections.OrderedDict()
    for e in ch.get(root, []):
        groups.setdefault((e['dst'], e['kind']), []).append(e)
    for (dst, kind), es in groups.items():
        e = dict(es[0])
        if len(es) > 1:
            e['line'] = '%s(+%d 处: %s)' % (es[0]['line'], len(es) - 1, ','.join(str(x['line']) for x in es[1:6]))
        tree_text(P, ch, dst, maxdepth, expanded, indent + '    ', depth + 1, path + (root,), out, e)
    return out


def write_trees(P, ch):
    F, C, M = P['funcs'], P['classes'], P['mods']
    d = os.path.join(OUT, 'function_trees')
    shutil.rmtree(d, ignore_errors=True)
    entry = next((en for en in P['entries'] if not M[en['module']].legacy), None)
    # 1 入口调用树
    if entry:
        txt = tree_text(P, ch, entry['id'])
        w(os.path.join(d, '01_entry_tree.txt'),
          '# 项目入口 -> 全部可达函数调用树 (静态)\n# 格式: [边类型/可信度@调用行] 模块::函数 (文件:定义行) <标志>\n'
          '# call=直接调用 create=对象创建 connect=信号槽(间接) timer=定时器回调(间接) thread=线程入口(间接) dynamic=动态分发(间接)\n'
          '# 可信度 high=已确认 medium=静态推断 low=推测\n# 已展开的节点在后文以 "↑ 已在上文展开" 引用, 避免重复与无限展开\n\n' + '\n'.join(txt) + '\n')
        # 核心业务: 仅 depth<=4 的精简版
        slim = tree_text(P, ch, entry['id'], maxdepth=4)
        w(os.path.join(d, '01b_entry_tree_depth4.txt'), '\n'.join(slim) + '\n')
    # 2 按模块
    for m in M.values():
        if m.generated:
            continue
        fs = [f for f in m.funcs]
        L = [f'# 模块 {m.name}  ({m.rel})\n']
        for f in sorted(fs, key=lambda x: x.line):
            outs = ch.get(f.id, [])
            ins = [e for e in P['edges'] if e['dst'] == f.id and e['kind'] != 'defines']
            L.append(f'## {f.qualname}  L{f.line}-{f.end_line}  args=({", ".join(f.args)})' + (f'  <{",".join(sorted(f.flags))}>' if f.flags else ''))
            for e in outs:
                L.append(f'  -> [{e["kind"]}/{e["conf"]}@L{e["line"]}] {label(F[e["dst"]])}' + (f'   # {e["note"]}' if e['note'] else ''))
            for k, v in sorted(P['externals'].get(f.id, {}).items()):
                L.append(f'  => (外部库) {k} x{v}')
            for e in ins[:12]:
                L.append(f'  <- [{e["kind"]}/{e["conf"]}@L{e["line"]}] {label(F[e["src"]])}')
            if len(ins) > 12:
                L.append(f'  <- ... 另有 {len(ins) - 12} 个调用者')
            L.append('')
        w(os.path.join(d, 'by_module', m.name.replace('/', '_') + '.txt'), '\n'.join(L))
    # 3 按类
    for c in C.values():
        if M[c['module']].generated:
            continue
        L = [f'# 类 {c["module"]}::{c["qualname"]}  ({c["file"]}:{c["line"]})  bases={[".".join(b) for b in c["bases"]]}\n']
        for n_, fid in c['methods'].items():
            f = F[fid]
            L.append(f'## {c["name"]}.{n_}  L{f.line}')
            for line in tree_text(P, ch, fid, maxdepth=2):
                L.append('   ' + line)
            L.append('')
        w(os.path.join(d, 'by_class', f'{c["module"]}.{c["qualname"]}'.replace('/', '_') + '.txt'), '\n'.join(L))
    # 5 UI 事件 -> 硬件 链
    hw = [f.id for f in F.values() if 'hardware_io' in f.flags and not M[f.module].legacy]
    rev = collections.defaultdict(list)
    for e in P['edges']:
        if e['kind'] in ('call', 'connect', 'timer', 'thread') and e['dst'] in F:
            rev[e['dst']].append(e)
    starts = {f.id for f in F.values() if f.flags & {'qt_slot', 'timer_callback', 'thread_entry'}}
    chains = []
    for h in hw:
        seen = {h: None}
        q = collections.deque([h])
        while q:
            x = q.popleft()
            if x in starts and x != h:
                p = [x]
                while seen[p[-1]] is not None:
                    p.append(seen[p[-1]][0])
                chains.append(p)  # start ... h
                continue
            for e in rev.get(x, []):
                if e['src'] not in seen:
                    seen[e['src']] = (x, e)
                    q.append(e['src'])
    # 回溯 UI 创建: slot 往上找 connect 边的建立者
    L = ['# PyQt5 事件 -> 业务处理 -> 硬件(串口)/数据处理 调用链 (BFS 最短路径, 静态)\n',
         '# 注意: 串口对象多保存在 ui.constants/ui.structs 的结构体属性中, 通过 obj.write()/read() 访问, 静态分析只能用启发式(serial_io_heuristic)识别 I/O 点\n']
    seen_chain = set()
    n = 0
    for p in sorted(chains, key=lambda x: (-len({F[i].module for i in x}), len(x))):
        key = tuple(p)
        if key in seen_chain:
            continue
        seen_chain.add(key)
        n += 1
        L.append(f'## 链 {n}: {label(F[p[0]])}  [{",".join(sorted(F[p[0]].flags))}]')
        for i, fid in enumerate(p):
            f = F[fid]
            L.append(f'   {"  " * i}{"└▶ " if i else ""}{label(f)}  ({f.file}:{f.line})' + ('  ★硬件I/O' if 'hardware_io' in f.flags else ''))
        io = getattr(F[p[-1]], 'io_sites', [])
        for s in io[:3]:
            L.append(f'   {"  " * len(p)}└▶ [{s["line"]}] {s["expr"]}  (串口读写, 启发式)')
        for k in P['externals'].get(p[-1], {}):
            if k.startswith('serial'):
                L.append(f'   {"  " * len(p)}└▶ (外部库) {k}')
        L.append('')
    # 无可达 slot 的硬件函数
    reached = {c[-1] for c in chains}
    L.append('## 未找到静态 UI 事件入口的硬件 I/O 函数 (多由 threading.Thread/反射/运行期属性触发, 需人工确认)')
    for h in hw:
        if h not in reached:
            L.append(f'  - {label(F[h])}  ({F[h].file}:{F[h].line})  被调用者: {[label(F[e["src"]]) for e in rev.get(h, [])][:4]}')
    w(os.path.join(d, '05_ui_event_to_hardware_chains.txt'), '\n'.join(L) + '\n')
    # 6 动态
    dyn = json.load(open(os.path.join(OUT, 'dynamic_and_unresolved.json'), encoding='utf-8'))
    by = collections.defaultdict(list)
    for x in dyn:
        if not any(M[mn].legacy for mn in [x['func'].split('::')[0]]):
            by[x['kind']].append(x)
    L = ['# 无法静态确定的关系专项清单 (均标记为: 待人工确认)\n',
         '- reflection: getattr/setattr/hasattr/eval/exec/importlib 等反射或动态导入, 目标由运行期字符串决定',
         '- connect_slot_unresolved: connect() 的槽为运行期对象属性/下标表达式, 无法定位定义',
         '- unresolved_name: 被调用名称来自参数/局部可调用对象',
         '- indirect_call: f()() / x[i]() 形式',
         '- dynamic(call-graph edge): 通过 module_chain + _init_module(cls) + setattr 动态实例化 manager, 已根据元组列表人工建模为 medium 可信度边\n']
    for k, v in by.items():
        L.append(f'## {k}  ({len(v)})')
        for x in sorted(v, key=lambda z: (z['file'], z['line'])):
            L.append(f'  {x["file"]}:{x["line"]}  {short(x["func"])}  ::  {x["expr"][:110]}' + (f'   -- {x["why"]}' if x.get('why') else ''))
        L.append('')
    w(os.path.join(d, '06_dynamic_and_unresolved.txt'), '\n'.join(L))
    return entry, chains


# ------------------------------------------------------------------ Mermaid
class Ids:
    def __init__(self, pfx='n'):
        self.m, self.pfx = {}, pfx

    def __call__(self, k):
        if k not in self.m:
            self.m[k] = f'{self.pfx}{len(self.m)}'
        return self.m[k]


def mm_modules(P, dep, include_legacy=False):
    M = P['mods']
    ids = Ids('m')
    L = ['%% 图2 模块依赖关系图 (import / 运行期调用耦合)', '%% 实线=import 依赖; 虚线=运行期跨模块函数调用耦合(self.mw 桥接/对象调用, 非 import)',
         '%% 红色=循环依赖(无), 橙色=高耦合(fan_in+fan_out 靠前)', 'flowchart LR']
    fan = {m: dep['coupling'][m]['fan_in'] + dep['coupling'][m]['fan_out'] for m in M}
    top = set(sorted(fan, key=lambda m: -fan[m])[:5])
    nodes = [m for m in M if include_legacy or not (M[m].legacy or m in ('Automated_testingV17', 'Automated_testingV20', 'Automated_testing', 'sample_testingV13'))]
    for la in LAYERS:
        ms = [m for m in nodes if layer_of(m) == la]
        if not ms:
            continue
        L.append(f'  subgraph {ids("L" + la)}["{la}"]')
        for m in ms:
            L.append(f'    {ids(m)}["{esc(m)}<br/><small>{esc(M[m].rel)}</small>"]')
        L.append('  end')
    s = set(nodes)
    for e in dep['edges']:
        if e['src'] in s and e['dst'] in s:
            L.append(f'  {ids(e["src"])} -->|"import L{e["lines"][0]}"| {ids(e["dst"])}')
    for c in dep['runtime_call_coupling']:
        if c['src'] in s and c['dst'] in s and c['calls'] >= 2:
            L.append(f'  {ids(c["src"])} -.->|"call x{c["calls"]}"| {ids(c["dst"])}')
    for m in nodes:
        if m in top:
            L.append(f'  style {ids(m)} fill:#ffe0b3,stroke:#e67e00,stroke-width:2px')
    for cyc in dep['import_cycles']:
        for m in cyc:
            L.append(f'  style {ids(m)} fill:#ffb3b3,stroke:#c00')
    return '\n'.join(L) + '\n'


def mm_arch(P, dep):
    M = P['mods']
    ids = Ids('a')
    L = ['%% 图1 项目总体架构图 (层 -> 模块), 层间箭头 = 层内模块 import 的聚合 (数字=import 条数)', 'flowchart TB']
    active = [m for m in M if not (M[m].legacy or m in ('Automated_testingV17', 'Automated_testingV20', 'Automated_testing', 'sample_testingV13', 'ui', 'ui.inits', 'ui.events', 'ui.tools', 'ui.navs'))]
    for la in LAYERS:
        ms = [m for m in active if layer_of(m) == la]
        if not ms:
            continue
        L.append(f'  subgraph {ids("L" + la)}["{la}"]')
        L.append('    direction LR')
        for m in ms:
            L.append(f'    {ids(m)}["{esc(m.split(".")[-1])}"]')
        L.append('  end')
    agg = collections.Counter()
    for e in dep['edges']:
        a, b = layer_of(e['src']), layer_of(e['dst'])
        if e['src'] in active and e['dst'] in active and a != b:
            agg[(a, b)] += 1
    for (a, b), n in sorted(agg.items(), key=lambda x: (LAYER_ORDER[x[0][0]], LAYER_ORDER[x[0][1]])):
        L.append(f'  {ids("L" + a)} -->|"import x{n}"| {ids("L" + b)}')
    # 运行期挂载
    mc = [m for m in M if m.startswith('ui.') and any(c['id'] in P['attr_map'].values() for c in P['classes'].values() if c['module'] == m)]
    main = '通用自动测试上位机V0.95'
    for m in sorted(mc):
        L.append(f'  {ids(main)} -.->|"module_chain 动态挂载"| {ids(m)}')
    L.append('  PyQt5(["PyQt5 / pyqtgraph"]):::ext\n  SER(["pyserial 串口设备"]):::ext\n  DATA(["规则/配置文本文件"]):::ext')
    L.append(f'  {ids("L设备通信层")} --> SER')
    L.append(f'  {ids("L配置层")} --> DATA')
    L.append(f'  {ids("LUI层")} --> PyQt5')
    L.append('  classDef ext fill:#eee,stroke:#999,stroke-dasharray: 4 2')
    return '\n'.join(L) + '\n'


def mm_startup(P, ch):
    F, C, M = P['funcs'], P['classes'], P['mods']
    ids = Ids('s')
    main = '通用自动测试上位机V0.95'
    def fid(q):
        return f'{main}::{q}'
    L = ['%% 图5 程序启动流程图 (节点均可在 function_trees/01_entry_tree.txt 中追溯; 括号为源码位置)', 'flowchart TD']
    def node(f, text=None):
        ff = F[f]
        return f'{ids(f)}["{(text or esc(ff.qualname)).replace("<br/>", "<br/>")}<br/><small>{esc(ff.file)}:{ff.line}</small>"]'
    seq = [fid('<module>'), fid('_prepare_runtime_workdir'), fid('_find_runtime_root')]
    entry = F[fid('<module>')]
    L.append(f'  {node(entry.id, "__main__: QApplication(sys.argv)")}')
    L.append(f'  {node(fid("_prepare_runtime_workdir"), "导入期: RUNTIME_ROOT=_prepare_runtime_workdir() (切换工作目录)")}')
    L.append(f'  {node(fid("_find_runtime_root"))}')
    L.append(f'  {ids(entry.id)} -.->|"模块导入时已执行"| {ids(fid("_prepare_runtime_workdir"))} --> {ids(fid("_find_runtime_root"))}')
    L.append(f'  {node(fid("MainWindow.__init__"), "MainWindow.__init__: 读取 debug_mode.ini, setupUi, show")}')
    L.append(f'  {ids(entry.id)} -->|"create L{[e for e in ch[entry.id] if e["dst"] == fid("MainWindow.__init__")][0]["line"]}"| {ids(fid("MainWindow.__init__"))}')
    L.append(f'  {node(fid("MainWindow.init_after_show"))}')
    L.append(f'  {ids(fid("MainWindow.__init__"))} -->|"QTimer.singleShot(50) timer"| {ids(fid("MainWindow.init_after_show"))}')
    L.append(f'  {node(fid("MainWindow._init_modules_in_batches"), "_init_modules_in_batches: 按 module_chain 顺序实例化")}')
    L.append(f'  {ids(fid("MainWindow.init_after_show"))} -->|call| {ids(fid("MainWindow._init_modules_in_batches"))}')
    prev = fid('MainWindow._init_modules_in_batches')
    for h in P['chain_hints']:
        init = A_find(P, h['cls'])
        tgt = F[init]
        L.append(f'  {node(init, f"{C[h['cls']]['name']}.__init__<br/>({h['label']}, mw.{h['attr']})")}')
        L.append(f'  {ids(prev)} -->|"dynamic L{h["line"]}"| {ids(init)}')
        prev = init
        for e in ch.get(init, [])[:0]:
            pass
    L.append(f'  EL(["app.exec_() 事件循环 -> 信号槽/QTimer/线程 驱动"])')
    L.append(f'  {ids(entry.id)} --> EL')
    L.append('  CFG["配置加载: ui.load_ini / ui.settings / ui.inits.inits_funcTest(读 functest_config.ini)"]')
    L.append(f'  {ids(P["attr_map"]["init_ini"] if False else A_find(P, P["attr_map"]["init_ini"]))} -.-> CFG')
    return '\n'.join(L) + '\n'


def A_find(P, cid):
    c = P['classes'][cid]
    return c['methods'].get('__init__') or cid


def mm_classes(P):
    C, M = P['classes'], P['mods']
    ids = Ids('c')
    L = ['%% 图4 类关系图: 继承(<|--) / 组合(*--, self.x=Cls()) / 对象创建(..>) / 运行期挂载(--> mw.attr)', 'classDiagram']
    act = [c for c in C.values() if not M[c['module']].legacy and c['module'] not in ('Automated_testingV20',)]
    names = {}
    for c in act:
        nm = c['name'] if sum(1 for x in act if x['name'] == c['name']) == 1 else f'{c["name"]}_{c["module"].split(".")[-1]}'
        names[c['id']] = nm.replace('.', '_').replace('-', '_')
    for c in act:
        n = names[c['id']]
        L.append(f'  class {n} {{')
        if c.get('stereotype'):
            L.append(f'    <<{c["stereotype"]}>>')
        for mname in list(c['methods'])[:6]:
            L.append(f'    +{mname}()')
        if len(c['methods']) > 6:
            L.append(f'    +...({len(c["methods"]) - 6} more)')
        L.append('  }')
    exts = set()
    for c in act:
        n = names[c['id']]
        for b in c['bases_resolved']:
            if b in names:
                L.append(f'  {names[b]} <|-- {n} : 继承 {c["file"]}@L{c["line"]}')
        for b in c.get('bases_external', []):
            en = b.replace('.', '_')
            if en not in exts:
                L.append(f'  class {en}')
                exts.add(en)
            L.append(f'  {en} <|-- {n} : 继承(外部)')
        for a, tc in c['attr_types'].items():
            t = A.resolve_name_chain(P['mods'], P['ns'], c['module'], tc)
            if t and t[0] == 'class' and t[1] in names:
                L.append(f'  {n} *-- {names[t[1]]} : self.{a}')
    if P['main_cid']:
        mn = names.get(P['main_cid'])
        for h in P['chain_hints']:
            if h['cls'] in names and mn:
                L.append(f'  {mn} --> {names[h["cls"]]} : 挂载 {h["attr"]} (module_chain L{h["line"]})')
    # 对象创建(跨类)
    seen = set()
    for e in P['edges']:
        if e['kind'] == 'create':
            src = P['funcs'][e['src']]
            tc = None
            dst = P['funcs'].get(e['dst'])
            if dst and dst.cls:
                tc = dst.cls
            elif e['dst'] in C:
                tc = e['dst']
            if src.cls in names and tc in names and src.cls != tc and (src.cls, tc) not in seen:
                seen.add((src.cls, tc))
                L.append(f'  {names[src.cls]} ..> {names[tc]} : 创建 L{e["line"]}')
    return '\n'.join(L) + '\n'


def mm_calltree(P, ch, root, depth=3, maxn=60):
    F = P['funcs']
    ids = Ids('f')
    L = [f'%% 图3 函数调用树(局部): 自 {short(root)} 起 depth={depth}; 边: -->call/create, ==>信号槽/定时器/线程(间接), -.->动态', 'flowchart LR']
    seen, q, n = {root}, [(root, 0)], 0
    while q and n < maxn:
        x, d = q.pop(0)
        L.append(f'  {ids(x)}["{esc(F[x].qualname)}<br/><small>{esc(F[x].module)}:{F[x].line}</small>"]')
        if d >= depth:
            continue
        for e in ch.get(x, []):
            arrow = {'call': '-->', 'create': '-->', 'connect': '==>', 'timer': '==>', 'thread': '==>', 'dynamic': '-.->'}[e['kind']]
            L.append(f'  {ids(x)} {arrow}|"{e["kind"]}/{e["conf"]} L{e["line"]}"| {ids(e["dst"])}')
            if e['dst'] not in seen:
                seen.add(e['dst']); q.append((e['dst'], d + 1)); n += 1
    return '\n'.join(L) + '\n'


def mm_sequence(P, chain):
    F, C = P['funcs'], P['classes']
    L = ['%% 图6 关键业务时序图: UI 事件/定时器/线程 -> 业务函数 -> 串口设备 (由 call graph 最短路径自动生成)', 'sequenceDiagram', '  autonumber', '  actor U as 操作员/Qt事件循环']
    parts = {}
    def pid(fid):
        f = F[fid]
        k = f.cls or f.module
        nm = (C[f.cls]['name'] if f.cls else f.module.split('.')[-1])
        if k not in parts:
            parts[k] = f'P{len(parts)}'
            L.append(f'  participant {parts[k]} as {esc(nm)}')
        return parts[k]
    L.append('  participant HW as 串口设备(pyserial)')
    body = []
    first = chain[0]
    con = next((e for e in P['edges'] if e['dst'] == first and e['kind'] in ('connect', 'timer', 'thread')), None)
    L.append('  participant W as Qt控件/QTimer/线程')
    if con:
        body.append(f'  U->>W: 用户操作 / 定时触发 ({esc(con["note"].split(" | ")[0])})')
        body.append(f'  W-){pid(first)}: {esc(F[first].name)}() 槽 [{con["kind"]} 连接于 {F[con["src"]].file}:{con["line"]}]')
    else:
        body.append(f'  U->>{pid(first)}: {esc(F[first].name)} (回调, {F[first].file}:{F[first].line})')
    for a, b in zip(chain, chain[1:]):
        e = next((e for e in P['edges'] if e['src'] == a and e['dst'] == b and e['kind'] != 'defines'), None)
        kind = e['kind'] if e else 'call'
        line = e['line'] if e else '?'
        arrow = '-)' if kind in ('thread', 'timer', 'connect') else '->>'
        body.append(f'  {pid(a)}{arrow}{pid(b)}: {esc(F[b].name)}() [{kind} L{line}]')
    last = chain[-1]
    io = getattr(F[last], 'io_sites', [])
    ex = [k for k in P['externals'].get(last, {}) if k.startswith('serial')]
    txt = (io[0]['expr'] + f' L{io[0]["line"]}') if io else (ex[0] if ex else 'serial I/O')
    body.append(f'  {pid(last)}->>HW: {esc(txt)}')
    body.append(f'  HW-->>{pid(last)}: 数据/应答')
    return '\n'.join(L + body) + '\n'


DIAG_META = {
 'architecture.mmd': ('图1 项目总体架构图', '实线箭头=层间 import 聚合(数字为 import 条数); 虚线=MainWindow 经 module_chain 动态挂载 manager; 灰色椭圆=外部依赖', '分层依据 ROLES 表(读代码得出); 设备通信并非单一层: 串口读写还分布在 ui.structs/ui.event/主窗口中'),
 'module_dependencies.mmd': ('图2 模块依赖关系图', '实线=import; 虚线=运行期跨模块调用耦合(self.mw 桥接等, 非 import); 橙色=高耦合(fan_in+fan_out 前5)', 'import 图无循环依赖; 但 manager <-> MainWindow 通过 self.mw 形成运行期双向耦合(未在 import 中体现)'),
 'call_tree_entry.mmd': ('图3 函数调用树(入口局部, depth=3)', '实线=直接调用/创建; 粗线=信号槽/定时器/线程(间接); 点线=动态分发', '完整调用树见 function_trees/01_entry_tree.txt; 按模块局部树见 diagrams/by_module/'),
 'class_relationships.mmd': ('图4 类关系图', '<|--继承; *--组合(self.x=Cls()); ..>对象创建; -->运行期挂载', '仅含非旧版类; 外部基类(QMainWindow/QThread 等)以空类表示'),
 'startup_flow.mmd': ('图5 程序启动流程图', '实线=调用/创建, 虚线=导入期或动态实例化', '每个节点标注源码位置, 可在 function_trees/01_entry_tree.txt 中追溯'),
}
SEQ_NOTE = ('图6 关键业务时序图', '实线箭头=同步调用; 开口箭头=信号槽/线程/定时器(异步间接调用)', '由调用图最短路径自动生成; 串口 I/O 点为启发式识别(serial 外部调用或 *serial*.write/read)')


def build_html(P, dep, ch):
    F, C, M = P['funcs'], P['classes'], P['mods']
    mnames = sorted(M)
    midx = {m: i for i, m in enumerate(mnames)}
    fids = sorted(F, key=lambda i: (midx[F[i].module], F[i].line, i))
    fidx = {f: i for i, f in enumerate(fids)}
    inv = json.load(open(os.path.join(OUT, 'project_inventory_modules.json'), encoding='utf-8'))
    invd = {r['name']: r for r in inv}
    mods = []
    for m in mnames:
        r = invd[m]
        lay, role = ROLES.get(m, ('公共工具层', ''))
        mods.append(dict(id=m, file=M[m].rel, layer=lay, role=role, lines=r['lines'], legacy=M[m].legacy, generated=M[m].generated,
                         entry=r['has_main_guard'], dead=(not r['imported_by'] and not r['has_main_guard'] and not r['is_package']),
                         empty=(r['n_functions'] == 0 and not r['classes']),
                         classes=r['classes'], imp_out=[midx[x] for x in r['imports_internal']], imp_in=[midx[x] for x in r['imported_by']],
                         ext=r['imports_external'], cyc=any(m in c for c in dep['import_cycles'])))
    funcs = []
    for fid in fids:
        f = F[fid]
        funcs.append([fid, midx[f.module], C[f.cls]['name'] if f.cls else '', f.name, f.qualname if f.cls or f.parent else f.name, f.line, f.end_line,
                      sorted(f.flags), f.args, dict(P['externals'].get(fid, {})), f.dyn and [dict(kind=d['kind'], line=d['line'], expr=d['expr'][:100]) for d in f.dyn if d['kind'] != 'reflection' or True][:20] or []])
    edges = [[fidx[e['src']], fidx[e['dst']], e['kind'], e['conf'], e['line'], e['note']] for e in P['edges']
             if e['kind'] != 'defines' and e['src'] in fidx and e['dst'] in fidx]
    classes = []
    for c in C.values():
        classes.append(dict(i=len(classes), name=c['name'], mod=c['module'], line=c['line'], bases=['.'.join(b) for b in c['bases']],
                            mounted=[k for k, v in P['attr_map'].items() if v == c['id']], methods=[fidx[x] for x in c['methods'].values()]))
    files = []
    data_dirs = {'处理规则', '标定规则', '网口规则', '自动规则', '装订规则', '解算规则', 'test_fun', '旧文件'}
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = sorted(d for d in dns if d not in ('.git', '__pycache__', 'analysis_report'))
        rel_d = os.path.relpath(dp, ROOT).replace(os.sep, '/')
        if rel_d != '.' and rel_d.split('/')[0] in data_dirs:
            if '/' not in rel_d:
                n = sum(len(x[2]) for x in os.walk(dp))
                files.append(dict(p=rel_d, collapsed=True, n=n))
            dns[:] = []
            continue
        for fn in sorted(fns):
            rel = (rel_d + '/' + fn) if rel_d != '.' else fn
            mn = None
            if fn.endswith('.py'):
                mn = next((i for i, m in enumerate(mnames) if M[m].rel == rel), None)
            files.append(dict(p=rel, m=mn))
    entry_fn = next((en['id'] for en in P['entries'] if not M[en['module']].legacy), None)
    return dict(root=ROOT.replace(os.sep, '/'), layers=LAYERS, files=files, mods=mods, funcs=funcs, edges=edges, classes=classes,
                imports=[[midx[e['src']], midx[e['dst']], e['kinds'], e['lines']] for e in dep['edges']],
                coupling=[[midx[e['src']], midx[e['dst']], e['calls']] for e in dep['runtime_call_coupling']],
                entry=fidx[entry_fn])


def write_html(P, dep, ch):
    data = build_html(P, dep, ch)
    tpl = open(os.path.join(HERE, 'viewer_template.html'), encoding='utf-8').read()
    w(os.path.join(OUT, 'index.html'), tpl.replace('/*__DATA__*/', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')))
    # Mermaid 图集
    diag = os.path.join(OUT, 'diagrams')
    sec = []
    order = ['architecture.mmd', 'module_dependencies.mmd', 'call_tree_entry.mmd', 'class_relationships.mmd', 'startup_flow.mmd']
    order += sorted(f for f in os.listdir(diag) if f.startswith('sequence_'))
    for f in order:
        meta = DIAG_META.get(f) or (SEQ_NOTE[0] + ' (' + f + ')', SEQ_NOTE[1], SEQ_NOTE[2])
        txt = open(os.path.join(diag, f), encoding='utf-8').read()
        sec.append(f'<section><h2>{meta[0]}</h2><p><b>图例:</b> {meta[1]}</p><p><b>说明:</b> {meta[2]}</p><p><a href="{f}">源文件 {f}</a></p>'
                   f'<pre class="mermaid">{txt.replace("&", "&amp;").replace("<", "&lt;")}</pre></section>')
    bm = sorted(os.listdir(os.path.join(diag, 'by_module')))
    lazy = ''.join(f'<details data-f="by_module/{f}"><summary>{f[:-4]}</summary><pre class="mermaid-lazy" hidden>{open(os.path.join(diag, "by_module", f), encoding="utf-8").read().replace("&", "&amp;").replace("<", "&lt;")}</pre></details>' for f in bm)
    html = ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>Mermaid 图集</title><style>body{font:14px "Microsoft YaHei",sans-serif;margin:16px 24px}'
            'section{border-top:2px solid #24344d;margin-top:22px}pre.mermaid{background:#fff;overflow:auto}details{margin:4px 0}</style></head><body>'
            '<h1>Mermaid 图集 (本地渲染, 无需联网)</h1><p><a href="../index.html">← 交互式报告</a> · 若图未显示请确认 ../vendor/mermaid.min.js 存在; 也可将 .mmd 粘贴到任意 Mermaid 编辑器。</p>'
            + ''.join(sec) + '<section><h2>按模块的局部函数调用树</h2><p>点击展开渲染(边数上限 80)。</p>' + lazy + '</section>'
            '<script src="../vendor/mermaid.min.js"></script><script>mermaid.initialize({startOnLoad:true,maxTextSize:2000000,maxEdges:5000,securityLevel:"loose",flowchart:{useMaxWidth:false}});'
            'document.querySelectorAll("details").forEach(d=>d.addEventListener("toggle",async()=>{if(!d.open||d.dataset.done)return;d.dataset.done=1;const p=d.querySelector("pre");const {svg}=await mermaid.render("m"+Math.random().toString(36).slice(2),p.textContent);const div=document.createElement("div");div.innerHTML=svg;d.appendChild(div)}));'
            '</script></body></html>')
    w(os.path.join(diag, 'index.html'), html)


def main():
    P = A.build(ROOT)
    A.export(P, ROOT, OUT)
    dep = json.load(open(os.path.join(OUT, 'module_dependencies.json'), encoding='utf-8'))
    ch = children_of(P)
    F, C, M = P['funcs'], P['classes'], P['mods']
    # 基础文件
    w(os.path.join(OUT, 'project_tree.txt'), project_tree())
    cats = categorize()
    mods_inv = json.load(open(os.path.join(OUT, 'project_inventory_modules.json'), encoding='utf-8'))
    for r in mods_inv:
        r['layer'], r['role'] = ROLES.get(r['name'], ('公共工具层', ''))
    entry, chains = write_trees(P, ch)
    inv = dict(
        generated_at=datetime.date.today().isoformat(),
        language='Python 3 (PyQt5 桌面应用)', analysis_scope=dict(
            analyzed='所有 .py (排除 .git/__pycache__/旧文件/test_fun/analysis_report)',
            excluded_legacy_archive='旧文件/ (归档的历史版本, 约 30 个 .py, 仅清点未分析)'),
        entry_points=[dict(e, legacy=M[e['module']].legacy) for e in P['entries']],
        startup=dict(main_window_class=P['main_cid'], manager_mounts=P['chain_hints']),
        file_categories={k: dict(count=len(v), files=v if len(v) <= 60 else v[:15] + [f'... 共 {len(v)} 个'] ) for k, v in sorted(cats.items())},
        modules=mods_inv, layers=LAYERS,
        third_party=dep['third_party'], stdlib=dep['stdlib'],
        tests='未发现 test_*.py/pytest/unittest; test_fun/ 为样例数据而非测试代码',
        notebooks=[x for x in cats.get('notebook', [])],
        threads_timers=dict(
            qthread_classes=[c['qualname'] for c in C.values() if c.get('stereotype') == 'QThread'],
            thread_edges=[dict(src=short(e['src']), dst=short(e['dst']), line=e['line']) for e in P['edges'] if e['kind'] == 'thread' and not M[F[e['src']].module].legacy],
            timer_edges=[dict(src=short(e['src']), dst=short(e['dst']), line=e['line']) for e in P['edges'] if e['kind'] == 'timer' and not M[F[e['src']].module].legacy],
            signal_slot_connections=sum(1 for e in P['edges'] if e['kind'] == 'connect' and not M[F[e['src']].module].legacy)))
    wj(os.path.join(OUT, 'project_inventory.json'), inv)
    # mermaid
    diag = os.path.join(OUT, 'diagrams')
    shutil.rmtree(diag, ignore_errors=True)
    os.makedirs(diag)
    mm = {}
    mm['architecture.mmd'] = mm_arch(P, dep)
    mm['module_dependencies.mmd'] = mm_modules(P, dep)
    mm['startup_flow.mmd'] = mm_startup(P, ch)
    mm['class_relationships.mmd'] = mm_classes(P)
    main_init = f'通用自动测试上位机V0.95::<module>'
    mm['call_tree_entry.mmd'] = mm_calltree(P, ch, main_init, depth=3, maxn=70)
    mainmod = '通用自动测试上位机V0.95'
    start = f'{mainmod}::MainWindow.begin_test'
    hwf = [f.id for f in F.values() if f.module == mainmod and 'hardware_io' in f.flags]
    paths = []
    for g in hwf:
        prev, q = {start: None}, collections.deque([start])
        while q:
            x = q.popleft()
            if x == g:
                break
            for e in ch.get(x, []):
                if e['kind'] in ('call', 'thread', 'timer', 'connect') and e['dst'] not in prev:
                    prev[e['dst']] = x
                    q.append(e['dst'])
        if g in prev:
            p, x = [], g
            while x is not None:
                p.append(x); x = prev[x]
            paths.append(p[::-1])
    for i, c in enumerate(sorted(paths, key=lambda p: (-len(p), p[-1]))[:3]):
        mm[f'sequence_flow{i + 1}_begin_test.mmd'] = mm_sequence(P, c)
    others = [c for c in sorted(chains, key=lambda x: (-len({F[i].module for i in x}), len(x))) if not M[F[c[0]].module].legacy and len(c) <= 4 and F[c[0]].id != start][:1]
    for i, c in enumerate(others):
        mm[f'sequence_flow{len(paths[:3]) + i + 1}_other.mmd'] = mm_sequence(P, c)
    for name, text in mm.items():
        w(os.path.join(OUT, name) if name in ('architecture.mmd', 'module_dependencies.mmd', 'startup_flow.mmd') else os.path.join(diag, name), text)
        if name in ('architecture.mmd', 'module_dependencies.mmd', 'startup_flow.mmd'):
            w(os.path.join(diag, name), text)
    # 按模块局部调用树 / 依赖
    for m in M.values():
        if m.generated or m.name in ('ui', 'ui.events', 'ui.inits', 'ui.tools', 'ui.navs'):
            continue
        fs = [f for f in m.funcs if ch.get(f.id) and f.name != '<module>']
        if not fs:
            continue
        ids = Ids('f')
        L = [f'%% 模块局部调用树: {m.name} ({m.rel}); 仅显示该模块内函数的直接调用(至多 80 条边)', 'flowchart LR']
        cnt = 0
        used = set()
        for f in fs:
            for e in ch[f.id]:
                if cnt >= 80:
                    break
                arrow = {'call': '-->', 'create': '-->', 'connect': '==>', 'timer': '==>', 'thread': '==>', 'dynamic': '-.->'}[e['kind']]
                for x in (f.id, e['dst']):
                    if x not in used:
                        used.add(x)
                        L.append(f'  {ids(x)}["{esc(F[x].qualname)}<br/><small>{esc(F[x].module)}:{F[x].line}</small>"]')
                L.append(f'  {ids(f.id)} {arrow}|"{e["kind"]}/{e["conf"]}"| {ids(e["dst"])}')
                cnt += 1
        w(os.path.join(diag, 'by_module', m.name + '.mmd'), '\n'.join(L) + '\n')
    # 图页 (本地 mermaid)
    write_html(P, dep, ch)
    return P, dep, ch, mm


if __name__ == '__main__':
    main()
