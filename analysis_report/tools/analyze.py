#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""静态分析器: 仅使用 ast 读取源码, 不导入/不执行业务代码 (无硬件副作用).

用法: python analysis_report/tools/analyze.py [--root <项目根>] [--out <输出目录>]
输出: analysis_report/data/*.json  (供 render.py 生成图表与 HTML)
"""
import ast, os, sys, json, hashlib, argparse, collections, builtins

EXCLUDE_DIRS = {'.git', '__pycache__', 'venv', '.venv', 'env', 'node_modules', 'build', 'dist',
                '.vscode', 'analysis_report', 'test_fun', '旧文件'}
LEGACY_FILES = {'通用自动测试上位机V0.90.py': '被 V0.95 取代的旧版主程序(仍引用 Automated_testingV17)'}
GENERATED_MARK = 'Form implementation generated from reading ui file'
BUILTINS = set(dir(builtins))
DYNAMIC_NAMES = {'getattr', 'setattr', 'hasattr', 'delattr', '__import__', 'import_module', 'eval', 'exec',
                 'globals', 'locals', 'vars', 'importlib'}
IO_METHODS = {'write', 'read', 'read_all', 'readline', 'readlines', 'in_waiting', 'inWaiting', 'flushInput', 'flushOutput',
              'reset_input_buffer', 'reset_output_buffer', 'readall'}
COMMON_METHODS = {'append', 'get', 'items', 'keys', 'values', 'update', 'format', 'join', 'split', 'strip',
                  'read', 'write', 'close', 'open', 'start', 'stop', 'run', 'send', 'clear', 'add', 'remove',
                  'copy', 'index', 'count', 'pop', 'insert', 'extend', 'replace', 'lower', 'upper', 'encode',
                  'decode', 'show', 'hide', 'text', 'setText', 'setEnabled', 'isChecked', 'connect', 'emit'}


def read_text(path):
    raw = open(path, 'rb').read()
    for enc in ('utf-8-sig', 'gbk'):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            pass
    return raw.decode('utf-8', 'replace')


def dotted(node):
    """Name/Attribute 链 -> ['a','b','c']; 否则 None"""
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
        return parts[::-1]
    return None


class Func:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.calls = []      # 原始调用记录
        self.connects = []
        self.dyn = []
        self.local_types = {}
        self.nested = {}     # name -> id (直接嵌套函数)
        self.flags = set()


class Collector(ast.NodeVisitor):
    def __init__(self, mod):
        self.m = mod
        self.cls_stack, self.fn_stack = [], []
        mod.funcs = []
        mod.classes = []
        mod.module_fn = Func(id=f'{mod.name}::<module>', module=mod.name, file=mod.rel, cls=None, name='<module>',
                             qualname='<module>', line=1, end_line=len(mod.text.splitlines()), args=[],
                             decorators=[], parent=None)
        mod.module_fn.flags.add('module_body')
        mod.funcs.append(mod.module_fn)
        self.ids = set()

    def cur(self):
        return self.fn_stack[-1] if self.fn_stack else self.m.module_fn

    def uid(self, base, line):
        i = base
        if i in self.ids:
            i = f'{base}#L{line}'
        self.ids.add(i)
        return i

    def visit_ClassDef(self, node):
        qual = '.'.join([c.name for c in self.cls_stack] + [node.name]) if not self.fn_stack else \
            '.'.join([f.qualname for f in self.fn_stack[-1:]] + ['<locals>', node.name])
        cid = self.uid(f'{self.m.name}::{qual}', node.lineno)
        ci = dict(id=cid, module=self.m.name, file=self.m.rel, name=node.name, qualname=qual, line=node.lineno,
                  end_line=getattr(node, 'end_lineno', node.lineno), bases=[dotted(b) or [ast.unparse(b)] for b in node.bases],
                  decorators=[ast.unparse(d) for d in node.decorator_list], methods={}, attr_types={}, assigns_mw=False,
                  doc=(ast.get_docstring(node) or '')[:200])
        self.m.classes.append(ci)
        self.cls_stack.append(ci)
        saved = self.fn_stack
        self.fn_stack = []   # 类体内语句归属 <module>
        for st in node.body:
            self.visit(st)
        self.fn_stack = saved
        self.cls_stack.pop()

    def visit_FunctionDef(self, node):
        parent = self.fn_stack[-1] if self.fn_stack else None
        cls = self.cls_stack[-1] if (self.cls_stack and not self.fn_stack) else None
        if parent:
            qual = f'{parent.qualname}.<locals>.{node.name}'
        elif cls:
            qual = f'{cls["qualname"]}.{node.name}'
        else:
            qual = node.name
        fid = self.uid(f'{self.m.name}::{qual}', node.lineno)
        a = node.args
        args = [x.arg for x in a.posonlyargs + a.args] + (['*' + a.vararg.arg] if a.vararg else []) + \
               [x.arg for x in a.kwonlyargs] + (['**' + a.kwarg.arg] if a.kwarg else [])
        f = Func(id=fid, module=self.m.name, file=self.m.rel, cls=cls['id'] if cls else None,
                 name=node.name, qualname=qual, line=node.lineno, end_line=getattr(node, 'end_lineno', node.lineno),
                 args=args, decorators=[ast.unparse(d) for d in node.decorator_list],
                 parent=parent.id if parent else None, is_async=isinstance(node, ast.AsyncFunctionDef))
        f.body_hash = hashlib.md5(ast.dump(ast.Module(body=node.body, type_ignores=[])).encode()).hexdigest()
        f.n_stmts = sum(1 for _ in ast.walk(node))
        f.doc = (ast.get_docstring(node) or '')[:200]
        self.m.funcs.append(f)
        if cls:
            cls['methods'].setdefault(node.name, fid)
        if parent:
            parent.nested[node.name] = fid
            parent.calls.append(dict(chain=None, target_id=fid, kind='defines', line=node.lineno, expr='def ' + node.name))
        for d in node.decorator_list:      # 装饰器表达式属于外层作用域
            self.visit(d)
        self.fn_stack.append(f)
        for st in node.body:
            self.visit(st)
        self.fn_stack.pop()

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Assign(self, node):
        val = node.value
        if isinstance(val, ast.Call) and dotted(val.func):
            ch = dotted(val.func)
            for t in node.targets:
                tc = dotted(t)
                if tc and len(tc) == 1:
                    self.cur().local_types[tc[0]] = ch
                elif tc and len(tc) == 2 and tc[0] == 'self' and self.cls_stack:
                    self.cls_stack[-1]['attr_types'].setdefault(tc[1], ch)
        for t in node.targets:
            tc = dotted(t)
            if tc and len(tc) == 2 and tc[0] == 'self' and self.cls_stack:
                self.cls_stack[-1].setdefault('attr_assigns', {}).setdefault(tc[1], (node.lineno, self.cur().id))
            if tc == ['self', 'mw'] and self.cls_stack:
                self.cls_stack[-1]['assigns_mw'] = True
        self.generic_visit(node)

    def visit_Call(self, node):
        fn = self.cur()
        line = node.lineno
        ch = dotted(node.func)
        if isinstance(node.func, ast.Attribute) and node.func.attr == 'connect':
            sender = dotted(node.func.value)
            fn.connects.append(dict(sender=sender, signal=sender[-1] if sender else None, slot=node.args[0] if node.args else None,
                                    line=line, in_loop=False, expr=ast.unparse(node)[:160]))
        elif ch and ch[-1] == 'singleShot' and len(node.args) >= 2:
            fn.connects.append(dict(sender=ch, signal='singleShot', slot=node.args[1], line=line, expr=ast.unparse(node)[:160], timer=True))
        elif ch and ch[-1] in ('Thread', 'Timer') and 'threading' in ch + ['threading']:
            tgt = None
            for kw in node.keywords:
                if kw.arg == 'target':
                    tgt = kw.value
            if tgt is None and ch[-1] == 'Timer' and len(node.args) >= 2:
                tgt = node.args[1]
            if tgt is not None:
                fn.connects.append(dict(sender=ch, signal='thread_target', slot=tgt, line=line, expr=ast.unparse(node)[:160], thread=True))
        if ch:
            if ch[-1] in DYNAMIC_NAMES or ch[0] in ('importlib',):
                fn.dyn.append(dict(kind='reflection', name='.'.join(ch), line=line, expr=ast.unparse(node)[:160]))
            fn.calls.append(dict(chain=ch, kind='call', line=line, expr='.'.join(ch) + '(...)',
                                 argc=len(node.args), kws=[k.arg for k in node.keywords]))
        elif isinstance(node.func, (ast.Subscript, ast.Lambda)) or (isinstance(node.func, ast.Call) and not isinstance(node.func.func, ast.Attribute)):
            fn.dyn.append(dict(kind='indirect_call', name=ast.unparse(node.func)[:80], line=line, expr=ast.unparse(node)[:160]))
        self.generic_visit(node)


class Module:
    pass


def load_project(root):
    mods = {}
    for dp, dns, fns in os.walk(root):
        dns[:] = sorted(d for d in dns if d not in EXCLUDE_DIRS and not d.startswith('.'))
        for fn in sorted(fns):
            if not fn.endswith('.py'):
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root).replace(os.sep, '/')
            m = Module()
            m.rel, m.text = rel, read_text(p)
            parts = rel[:-3].split('/')
            m.is_pkg = parts[-1] == '__init__'
            if m.is_pkg:
                parts = parts[:-1]
            m.name = '.'.join(parts)
            m.pkg = m.name if m.is_pkg else '.'.join(parts[:-1])
            m.generated = GENERATED_MARK in m.text[:600]
            m.legacy = os.path.basename(rel) in LEGACY_FILES and '/' not in rel
            m.syntax_error = None
            try:
                m.tree = ast.parse(m.text, filename=rel)
            except SyntaxError as e:
                m.tree, m.syntax_error = None, str(e)
            mods[m.name] = m
    return mods


def resolve_import_module(mods, base_pkg, level, name):
    if level:
        pk = base_pkg.split('.') if base_pkg else []
        pk = pk[:len(pk) - (level - 1)] if level > 1 else pk
        full = '.'.join(pk + ([name] if name else []))
    else:
        full = name or ''
    return full


def longest_internal(mods, full):
    parts = full.split('.')
    for i in range(len(parts), 0, -1):
        c = '.'.join(parts[:i])
        if c in mods:
            return c, parts[i:]
    return None, parts


def build(root):
    mods = load_project(root)
    # ---- 收集 ----
    for m in mods.values():
        if m.tree is None:
            m.funcs, m.classes = [], []
            continue
        Collector(m).visit(m.tree)
        if m.generated:   # 自动生成的 pyuic 文件: 只索引定义, 不分析几千行界面构造调用
            for f in m.funcs:
                f.calls, f.connects, f.dyn = [], [], []
                f.flags.add('generated')
    # ---- import 事件 ----
    import_edges = []   # (src_mod, dst_mod|None, ext_name, kind, line, names)
    ns_events = {}
    for m in mods.values():
        ev = []
        if m.tree is None:
            ns_events[m.name] = ev
            continue
        for n in ast.walk(m.tree):
            if isinstance(n, ast.Import):
                for a in n.names:
                    im, rest = longest_internal(mods, a.name)
                    if im:
                        bound = a.asname or a.name.split('.')[0]
                        tgt = im if a.asname else longest_internal(mods, a.name.split('.')[0])[0] or im
                        ev.append((n.lineno, 'bind', bound, ('module', tgt if a.asname else (a.name.split('.')[0] if a.name.split('.')[0] in mods else im))))
                        import_edges.append((m.name, im, None, 'import', n.lineno, [a.name]))
                    else:
                        bound = a.asname or a.name.split('.')[0]
                        ev.append((n.lineno, 'bind', bound, ('ext', a.name if a.asname else a.name.split('.')[0])))
                        import_edges.append((m.name, None, a.name, 'import', n.lineno, [a.name]))
            elif isinstance(n, ast.ImportFrom):
                full = resolve_import_module(mods, m.pkg, n.level, n.module)
                im, rest = longest_internal(mods, full)
                if im and not rest:
                    names = [a.name for a in n.names]
                    import_edges.append((m.name, im, None, 'from', n.lineno, names))
                    for a in n.names:
                        if a.name == '*':
                            ev.append((n.lineno, 'star', im, None))
                        else:
                            sub = f'{im}.{a.name}'
                            ev.append((n.lineno, 'from', a.asname or a.name, (im, a.name, sub if sub in mods else None)))
                            if sub in mods:
                                import_edges.append((m.name, sub, None, 'from-submodule', n.lineno, [a.name]))
                else:
                    import_edges.append((m.name, None, full, 'from', n.lineno, [a.name for a in n.names]))
                    for a in n.names:
                        if a.name != '*':
                            ev.append((n.lineno, 'bind', a.asname or a.name, ('ext', f'{full}.{a.name}')))
        # 顶层定义
        for f in m.funcs:
            if f.parent is None and f.cls is None and f.name != '<module>':
                ev.append((f.line, 'bind', f.name, ('func', f.id)))
        for c in m.classes:
            if '.' not in c['qualname']:
                ev.append((c['line'], 'bind', c['name'], ('class', c['id'])))
        ev.sort(key=lambda x: x[0])
        ns_events[m.name] = ev
    # ---- 命名空间 (处理 from x import * 的递归泄漏) ----
    ns_cache = {}

    def ns_of(mn, stack=()):
        if mn in ns_cache:
            return ns_cache[mn]
        if mn in stack:
            return {}
        ns = {}
        for _, kind, a, b in ns_events.get(mn, []):
            if kind == 'bind':
                ns[a] = b
            elif kind == 'star':
                for k, v in ns_of(a, stack + (mn,)).items():
                    if not k.startswith('_'):
                        ns[k] = v
            elif kind == 'from':
                im, nm, sub = b
                if sub:
                    ns[a] = ('module', sub)
                else:
                    t = ns_of(im, stack + (mn,)).get(nm)
                    ns[a] = t if t else ('unresolved_sym', f'{im}.{nm}')
        ns_cache[mn] = ns
        return ns

    for mn in mods:
        ns_of(mn)

    funcs = {f.id: f for m in mods.values() for f in m.funcs}
    classes = {c['id']: c for m in mods.values() for c in m.classes}
    cls_by_name = collections.defaultdict(list)
    for c in classes.values():
        cls_by_name[c['name']].append(c['id'])

    # ---- 类基类解析 / 方法解析 ----
    for c in classes.values():
        c['bases_resolved'] = []
        for b in c['bases']:
            t = resolve_name_chain(mods, ns_cache, c['module'], b)
            if t and t[0] == 'class':
                c['bases_resolved'].append(t[1])
            else:
                c.setdefault('bases_external', []).append('.'.join(b))
    def mro(cid, seen=None):
        seen = seen or set()
        if cid in seen or cid not in classes:
            return []
        seen.add(cid)
        out = [cid]
        for b in classes[cid]['bases_resolved']:
            out += mro(b, seen)
        return out

    def find_method(cid, name):
        for k in mro(cid):
            if name in classes[k]['methods']:
                return classes[k]['methods'][name]
        return None

    # ---- 主窗口 / manager 映射 (来自 module_chain 中的 (attr, 说明, 类) 元组) ----
    main_cid, attr_map, chain_hints = None, {}, []
    for m in mods.values():
        if m.legacy or m.tree is None:
            continue
        for fn in m.funcs:
            pass
        for n in ast.walk(m.tree):
            if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'module_chain' for t in n.targets) \
                    and isinstance(n.value, ast.List):
                for el in n.value.elts:
                    if isinstance(el, ast.Tuple) and len(el.elts) == 3 and isinstance(el.elts[0], ast.Constant):
                        ch = dotted(el.elts[2])
                        t = resolve_name_chain(mods, ns_cache, m.name, ch) if ch else None
                        if t and t[0] == 'class':
                            attr_map[el.elts[0].value] = t[1]
                            chain_hints.append(dict(attr=el.elts[0].value, cls=t[1], line=el.lineno, file=m.rel,
                                                    label=el.elts[1].value if isinstance(el.elts[1], ast.Constant) else ''))
                # 找所属主窗口类
                for c in m.classes:
                    if c['line'] <= n.lineno <= c['end_line']:
                        main_cid = c['id']
    mw_classes = {c['id'] for c in classes.values() if c['assigns_mw']}
    manager_ids = set(attr_map.values())

    # 方法名 -> 定义 (排除 legacy / generated, 用于唯一名推断)
    meth_index = collections.defaultdict(list)
    for c in classes.values():
        mm = mods[c['module']]
        if mm.legacy or mm.generated:
            continue
        for n_, fid in c['methods'].items():
            meth_index[n_].append(fid)

    edges, externals, attr_calls = [], collections.defaultdict(collections.Counter), collections.Counter()
    unresolved = []

    def add(src, dst, kind, conf, line, expr, note=''):
        edges.append(dict(src=src, dst=dst, kind=kind, conf=conf, line=line, expr=expr, note=note))

    def resolve_in_class(cid, name):
        return find_method(cid, name)

    def resolve_call(fn, chain, nsx, cid_ctx, is_ref=False):
        """返回 [(dst_id, kind, conf, note)] 或 ('ext', name) / ('attr',) / ('unres', why)"""
        root = chain[0]
        res = []
        # 嵌套函数 / 外层局部函数
        f = fn
        while f is not None:
            if len(chain) == 1 and chain[0] in f.nested:
                return [(f.nested[chain[0]], 'call', 'high', 'nested')]
            f = funcs.get(f.parent) if f.parent else None
        if root in ('self', 'cls') and cid_ctx:
            if len(chain) == 1:
                return [('attr',)]
            a = chain[1]
            if len(chain) == 2:
                mid = resolve_in_class(cid_ctx, a)
                if mid:
                    note = ''
                    subs = [s for s in classes.values() if cid_ctx in mro(s['id'])[1:] and a in s['methods']]
                    if subs:
                        note = 'polymorphic: 被 ' + ','.join(s['qualname'] for s in subs) + ' 重写'
                    return [(mid, 'call', 'high', note)]
                if cid_ctx in mw_classes or cid_ctx == main_cid:
                    cand = meth_index.get(a, [])
                    if len(cand) == 1 and a not in COMMON_METHODS:
                        return [(cand[0], 'call', 'low', 'mixin: 方法定义在其他 manager 类(运行时挂载)')]
                return [('attr',)]
            # len>=3
            if a == 'mw' and cid_ctx in mw_classes:
                rest = chain[2:]
                if len(rest) == 1:
                    if main_cid:
                        mid = resolve_in_class(main_cid, rest[0])
                        if mid:
                            return [(mid, 'call', 'medium', 'self.mw -> MainWindow (运行时由构造参数注入)')]
                    cand = meth_index.get(rest[0], [])
                    if len(cand) == 1 and rest[0] not in COMMON_METHODS:
                        return [(cand[0], 'call', 'low', 'self.mw.<名称> 在其他 manager 中唯一定义')]
                    return [('attr',)]
                if rest[0] in attr_map:
                    mid = resolve_in_class(attr_map[rest[0]], rest[1])
                    if mid:
                        return [(mid, 'call', 'medium', f'self.mw.{rest[0]} -> {classes[attr_map[rest[0]]]["name"]} (module_chain 挂载)')]
                return [('attr',)]
            if cid_ctx == main_cid and a in attr_map:
                mid = resolve_in_class(attr_map[a], chain[2])
                if mid:
                    return [(mid, 'call', 'medium', f'self.{a} -> {classes[attr_map[a]]["name"]} (module_chain 挂载)')]
            at = classes[cid_ctx]['attr_types'].get(a)
            if at:
                t = resolve_name_chain(mods, ns_cache, fn.module, at)
                if t and t[0] == 'class':
                    mid = resolve_in_class(t[1], chain[2])
                    if mid:
                        return [(mid, 'call', 'medium', f'self.{a} = {".".join(at)}(...)')]
            return [('attr',)]
        lt = fn.local_types.get(root) or mods[fn.module].module_fn.local_types.get(root)
        if lt and len(chain) >= 2:
            t = resolve_name_chain(mods, ns_cache, fn.module, lt)
            if t and t[0] == 'class':
                mid = resolve_in_class(t[1], chain[1])
                if mid:
                    return [(mid, 'call', 'medium', f'局部变量 {root} = {".".join(lt)}(...)')]
        t = nsx.get(root)
        if t:
            return follow(t, chain[1:], 'high')
        if root in BUILTINS and len(chain) == 1:
            return [('builtin',)]
        if len(chain) >= 2:
            a = chain[-1]
            cand = meth_index.get(a, [])
            if len(cand) == 1 and a not in COMMON_METHODS and not a.startswith('__'):
                return [(cand[0], 'call', 'low', f'按方法名唯一匹配推测 ({".".join(chain)})')]
            return [('attr',)]
        return [('unres', f'无法解析名称 {root!r} (参数/动态绑定的可调用对象)')]

    def follow(t, rest, conf):
        k = t[0]
        if k == 'func':
            return [(t[1], 'call', conf, '')]
        if k == 'class':
            if not rest:
                init = find_method(t[1], '__init__')
                return [(init or t[1], 'create', conf, 'ctor')]
            mid = find_method(t[1], rest[0])
            return [(mid, 'call', conf, 'Class.method')] if mid else [('attr',)]
        if k == 'module':
            if not rest:
                return [('attr',)]
            sub = ns_cache.get(t[1], {}).get(rest[0])
            if f'{t[1]}.{rest[0]}' in mods and not (sub and sub[0] in ('func', 'class')):
                sub = ('module', f'{t[1]}.{rest[0]}')
            if sub:
                return follow(sub, rest[1:], conf)
            return [('unres', f'模块 {t[1]} 中无 {rest[0]}')]
        if k == 'ext':
            return [('ext', '.'.join([t[1]] + rest))]
        return [('unres', f'未解析导入符号 {t[1]}')]

    def slot_targets(fn, expr, nsx, cid_ctx):
        """connect / singleShot / Thread(target=) 的回调参数 -> 目标函数列表"""
        out = []
        if expr is None:
            return out
        if isinstance(expr, ast.Lambda):
            for n in ast.walk(expr.body):
                if isinstance(n, ast.Call):
                    ch = dotted(n.func)
                    if ch:
                        for r in resolve_call(fn, ch, nsx, cid_ctx):
                            out.append((r, 'lambda'))
            return out
        if isinstance(expr, ast.Call):
            ch = dotted(expr.func)
            if ch and ch[-1] == 'partial' and expr.args:
                for r in slot_targets(fn, expr.args[0], nsx, cid_ctx):
                    out.append((r[0], 'partial'))
                return out
        ch = dotted(expr)
        if ch:
            for r in resolve_call(fn, ch, nsx, cid_ctx):
                out.append((r, 'direct'))
            return out
        return [(('unres', 'slot 表达式: ' + ast.unparse(expr)[:60]), 'expr')]

    # ---- 解析所有调用 ----
    for m in mods.values():
        nsx = ns_cache.get(m.name, {})
        for fn in m.funcs:
            cid_ctx = fn.cls
            # 嵌套函数继承外层类上下文
            p = fn
            while cid_ctx is None and p is not None and p.parent:
                p = funcs.get(p.parent)
                cid_ctx = p.cls if p else None
            fn.ctx_cls = cid_ctx
            for c in fn.calls:
                if c['kind'] == 'defines':
                    add(fn.id, c['target_id'], 'defines', 'high', c['line'], c['expr'])
                    continue
                ch = c['chain']
                if len(ch) >= 2 and ch[-1] in IO_METHODS and any('serial' in x.lower() or x.lower() in ('ser', 'com', 'port') for x in ch[:-1]):
                    fn.flags.add('serial_io_heuristic')
                    fn.io_sites = getattr(fn, 'io_sites', []) + [dict(line=c['line'], expr='.'.join(ch))]
                res = resolve_call(fn, ch, nsx, cid_ctx)
                for r in res:
                    if r[0] in funcs or r[0] in classes:
                        add(fn.id, r[0], r[1], r[2], c['line'], c['expr'], r[3])
                    elif r[0] == 'ext':
                        externals[fn.id][r[1]] += 1
                    elif r[0] == 'attr':
                        attr_calls[fn.id] += 1
                    elif r[0] == 'unres':
                        unresolved.append(dict(src=fn.id, line=c['line'], expr=c['expr'], why=r[1]))
            for cn in fn.connects:
                sig = cn['signal']
                kind = 'connect'
                if cn.get('timer'):
                    kind = 'timer'
                if cn.get('thread'):
                    kind = 'thread'
                if sig == 'timeout':
                    kind = 'timer'
                tg = slot_targets(fn, cn['slot'], nsx, cid_ctx)
                if not tg:
                    fn.dyn.append(dict(kind='connect_unparsed', name=cn['expr'], line=cn['line'], expr=cn['expr']))
                for r, how in tg:
                    sender = '.'.join(cn['sender']) if cn['sender'] else '?'
                    note = f'{sender}.connect' if sig not in ('singleShot', 'thread_target') else sig
                    if how != 'direct':
                        note += f' via {how}'
                    if r[0] in funcs or r[0] in classes:
                        add(fn.id, r[0], kind, r[2] if how == 'direct' else min_conf(r[2], 'medium'), cn['line'], cn['expr'],
                            note + (' | ' + r[3] if r[3] else ''))
                        funcs[r[0]].flags.add({'connect': 'qt_slot', 'timer': 'timer_callback', 'thread': 'thread_entry'}[kind]) \
                            if r[0] in funcs else None
                    elif r[0] == 'ext':
                        externals[fn.id][r[0 + 1]] += 1
                    elif r[0] in ('unres', 'attr'):
                        fn.dyn.append(dict(kind='connect_slot_unresolved', name=cn['expr'], line=cn['line'], expr=cn['expr'],
                                           why=r[1] if r[0] == 'unres' else '槽为运行期对象属性(控件/结构体成员), 静态无法定位定义'))
            # 反射 / 动态
        # setattr 循环挂载 manager: 补充 chain_hints 边
    # module_chain 动态实例化 (cls(self) 经 setattr 挂载)
    for h in chain_hints:
        host = None
        for f in funcs.values():
            if f.file == h['file'] and f.line <= h['line'] <= f.end_line and f.name != '<module>':
                host = f
        if host:
            init = find_method(h['cls'], '__init__') or h['cls']
            add(host.id, init, 'dynamic', 'medium', h['line'], f"module_chain: ('{h['attr']}', '{h['label']}', {classes[h['cls']]['name']})",
                '经 _init_module(name, cls) -> cls(self) + setattr(self, attr, instance) 动态实例化')
    # QThread.run / Thread.run 入口
    for c in classes.values():
        for b in c.get('bases_external', []):
            if b.endswith('QThread') or b.endswith('Thread'):
                rid = c['methods'].get('run')
                if rid:
                    funcs[rid].flags.add('thread_entry')
                c.setdefault('stereotype', 'QThread')
    # 主入口: if __name__ == '__main__'
    entries = []
    for m in mods.values():
        if m.tree is None:
            continue
        for n in m.tree.body:
            if isinstance(n, ast.If) and 'name' in ast.unparse(n.test) and '__main__' in ast.unparse(n.test):
                entries.append(dict(module=m.name, file=m.rel, line=n.lineno, id=m.module_fn.id))
                m.module_fn.flags.add('entry')
    return dict(mods=mods, funcs=funcs, classes=classes, edges=edges, externals=externals, attr_calls=attr_calls,
                unresolved=unresolved, import_edges=import_edges, ns=ns_cache, main_cid=main_cid, attr_map=attr_map,
                chain_hints=chain_hints, entries=entries, mw_classes=mw_classes, mro=mro)


def min_conf(a, b):
    order = ['high', 'medium', 'low', 'manual']
    return a if order.index(a) > order.index(b) else b


def resolve_name_chain(mods, ns_cache, modname, chain):
    ns = ns_cache.get(modname, {})
    t = ns.get(chain[0])
    rest = chain[1:]
    while t and t[0] == 'module' and rest:
        sub = ns_cache.get(t[1], {}).get(rest[0])
        if (not sub or sub[0] not in ('func', 'class')) and f'{t[1]}.{rest[0]}' in mods:
            sub = ('module', f'{t[1]}.{rest[0]}')
        t = sub
        rest = rest[1:]
    if t and not rest:
        return t
    return None


# ---------------------------------------------------------------------------
def tarjan(nodes, adj):
    idx, low, on, st, res, c = {}, {}, set(), [], [], [0]
    sys.setrecursionlimit(100000)

    def sc(v):
        idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        for w in adj.get(v, ()):
            if w not in idx:
                sc(w); low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = []
            while True:
                w = st.pop(); on.discard(w); comp.append(w)
                if w == v:
                    break
            res.append(comp)
    for v in nodes:
        if v not in idx:
            sc(v)
    return res


def export(P, root, out):
    mods, funcs, classes, edges = P['mods'], P['funcs'], P['classes'], P['edges']
    os.makedirs(out, exist_ok=True)

    def j(name, obj):
        with open(os.path.join(out, name), 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)

    # 调用图 SCC (仅 call/create/connect/timer/thread/dynamic)
    cadj = collections.defaultdict(set)
    for e in edges:
        if e['kind'] != 'defines' and e['dst'] in funcs:
            cadj[e['src']].add(e['dst'])
    sccs = tarjan(list(funcs), cadj)
    cyc = [s for s in sccs if len(s) > 1 or (s[0] in cadj.get(s[0], ()))]
    cyc_ids = {x for s in cyc for x in s}
    for f in funcs.values():
        if f.id in cyc_ids:
            f.flags.add('in_cycle')
    for e in edges:
        if e['src'] == e['dst']:
            e['recursive'] = True
    callers = collections.defaultdict(list)
    for e in edges:
        callers[e['dst']].append(e)

    HW = ('serial',)
    for f in funcs.values():
        for ex in P['externals'].get(f.id, {}):
            if ex.split('.')[0] in HW:
                f.flags.add('hardware_io')
        if 'serial_io_heuristic' in f.flags:
            f.flags.add('hardware_io')
        if f.name in ('__init__',) and f.cls:
            f.flags.add('constructor')
    # 事件回调: 以 event_/clkEvent_/changeEvent_ 命名且被 connect
    func_rows = []
    for f in funcs.values():
        m = mods[f.module]
        inb = [e for e in callers.get(f.id, []) if e['kind'] != 'defines']
        outb = [e for e in edges if e['src'] == f.id and e['kind'] != 'defines']
        func_rows.append(dict(
            id=f.id, module=f.module, file=f.file, class_id=f.cls, class_name=classes[f.cls]['name'] if f.cls else None,
            name=f.name, qualname=f.qualname, line=f.line, end_line=f.end_line, args=f.args, decorators=f.decorators,
            flags=sorted(f.flags), parent=f.parent, generated=m.generated, legacy=m.legacy,
            calls_internal=sorted({e['dst'] for e in outb}), called_by=sorted({e['src'] for e in inb}),
            calls_external=dict(P['externals'].get(f.id, {})), widget_attr_calls=P['attr_calls'].get(f.id, 0),
            dynamic_sites=f.dyn, io_sites=getattr(f, 'io_sites', []), n_stmts=getattr(f, 'n_stmts', 0), has_static_caller=bool(inb)))
    j('function_index.json', func_rows)
    j('function_call_graph.json', dict(
        nodes=[r['id'] for r in func_rows], edges=edges,
        confidence_legend={'high': '已确认: 名称/导入/self 方法静态可解析', 'medium': '静态推断: 经 self.mw / 运行时挂载 / 局部变量类型',
                           'low': '推测: 仅按方法名唯一性匹配', 'manual': '待人工确认'},
        kind_legend={'call': '直接调用', 'create': '对象创建(调用类构造)', 'connect': 'Qt 信号槽连接(间接调用)',
                     'timer': '定时器回调(间接)', 'thread': '线程入口(间接)', 'dynamic': '动态分发(间接)',
                     'defines': '嵌套函数定义(非调用)'},
        cycles=[sorted(s) for s in cyc], unresolved_names=P['unresolved']))
    # 类
    crow = []
    for c in classes.values():
        creators = [dict(src=e['src'], line=e['line']) for e in edges if e['kind'] == 'create' and
                    (e['dst'] == c['id'] or e['dst'] == c['methods'].get('__init__'))]
        crow.append(dict(id=c['id'], module=c['module'], file=c['file'], name=c['name'], qualname=c['qualname'], line=c['line'],
                         end_line=c['end_line'], bases=['.'.join(b) for b in c['bases']], bases_resolved=c['bases_resolved'],
                         bases_external=c.get('bases_external', []), methods=c['methods'], attr_types={k: '.'.join(v) for k, v in c['attr_types'].items()},
                         attaches_mw_bridge=c['assigns_mw'], stereotype=c.get('stereotype'), created_by=creators,
                         mounted_as=[k for k, v in P['attr_map'].items() if v == c['id']]))
    j('class_relationships.json', dict(classes=crow, main_window_class=P['main_cid'], manager_mounts=P['chain_hints']))
    # 模块依赖
    dep, ext = collections.defaultdict(lambda: dict(kinds=set(), lines=[], names=[])), collections.defaultdict(set)
    for s, d, en, k, ln, names in P['import_edges']:
        if d and d != s:
            x = dep[(s, d)]
            x['kinds'].add(k); x['lines'].append(ln); x['names'] += names
        elif not d:
            ext[s].add(en.split('.')[0])
    dedges = [dict(src=s, dst=d, kinds=sorted(v['kinds']), lines=sorted(set(v['lines'])), names=sorted(set(v['names']))[:12])
              for (s, d), v in sorted(dep.items())]
    adj = collections.defaultdict(set)
    for e in dedges:
        adj[e['src']].add(e['dst'])
    msccs = [s for s in tarjan(list(mods), adj) if len(s) > 1]
    fan_in, fan_out = collections.Counter(), collections.Counter()
    for e in dedges:
        fan_out[e['src']] += 1; fan_in[e['dst']] += 1
    # 运行期(调用层)模块耦合
    call_mod = collections.Counter()
    for e in edges:
        if e['kind'] != 'defines' and e['dst'] in funcs:
            a, b = funcs[e['src']].module, funcs[e['dst']].module
            if a != b:
                call_mod[(a, b)] += 1
    cadj2 = collections.defaultdict(set)
    for (a, b) in call_mod:
        cadj2[a].add(b)
    call_sccs = [s for s in tarjan(list(mods), cadj2) if len(s) > 1]
    ext_use = collections.Counter()
    for s, v in ext.items():
        for x in v:
            ext_use[x] += 1
    std = set(getattr(sys, 'stdlib_module_names', set()))
    j('module_dependencies.json', dict(
        modules=sorted(mods), edges=dedges, import_cycles=msccs,
        runtime_call_coupling=[dict(src=a, dst=b, calls=n) for (a, b), n in call_mod.most_common()],
        runtime_call_cycles=call_sccs,
        coupling={m: dict(fan_in=fan_in[m], fan_out=fan_out[m]) for m in sorted(mods)},
        external_by_module={k: sorted(v) for k, v in sorted(ext.items())},
        third_party={k: v for k, v in sorted(ext_use.items()) if k not in std and k != '__future__'},
        stdlib={k: v for k, v in sorted(ext_use.items()) if k in std}))
    # 模块清单
    rows = []
    for m in sorted(mods.values(), key=lambda x: x.rel):
        mf = [f for f in funcs.values() if f.module == m.name and f.name != '<module>']
        mc = [c for c in classes.values() if c['module'] == m.name]
        deps_in = sorted({e['src'] for e in dedges if e['dst'] == m.name})
        deps_out = sorted({e['dst'] for e in dedges if e['src'] == m.name})
        rows.append(dict(name=m.name, file=m.rel, lines=len(m.text.splitlines()), is_package=m.is_pkg, generated=m.generated,
                         legacy=m.legacy, syntax_error=m.syntax_error,
                         classes=[c['name'] for c in mc], n_functions=len(mf),
                         top_level_functions=[f.name for f in mf if not f.parent and not f.cls][:60],
                         imports_internal=deps_out, imported_by=deps_in,
                         imports_external=sorted(ext.get(m.name, [])),
                         has_main_guard=any(en['module'] == m.name for en in P['entries'])))
    j('project_inventory_modules.json', rows)
    # 动态/待确认
    dyn = []
    for f in funcs.values():
        for d in f.dyn:
            dyn.append(dict(func=f.id, file=f.file, **d))
    dyn += [dict(func=u['src'], file=funcs[u['src']].file, kind='unresolved_name', line=u['line'], expr=u['expr'], name=u['why'])
            for u in P['unresolved']]
    # 动态 setattr 挂载
    j('dynamic_and_unresolved.json', dyn)
    # 疑似未调用
    nocall = []
    for f in funcs.values():
        m = mods[f.module]
        if f.name == '<module>' or m.generated or f.name.startswith('__') or f.parent:
            continue
        if not any(e['kind'] != 'defines' for e in callers.get(f.id, [])):
            nocall.append(dict(id=f.id, file=f.file, line=f.line, legacy=m.legacy))
    # 重复实现
    byh = collections.defaultdict(list)
    for f in funcs.values():
        if f.name != '<module>' and getattr(f, 'n_stmts', 0) >= 25 and not mods[f.module].generated:
            byh[f.body_hash].append(f.id)
    dups = [v for v in byh.values() if len(v) > 1]
    byname = collections.defaultdict(list)
    for f in funcs.values():
        if f.name != '<module>' and not f.name.startswith('__') and not mods[f.module].generated and not f.parent:
            byname[f.name].append(f.id)
    same_name = {k: v for k, v in byname.items() if len({funcs[i].file for i in v}) > 1}
    shadows = []
    for c in classes.values():
        for a, (ln, fid) in c.get('attr_assigns', {}).items():
            if a in c['methods'] and not mods[c['module']].generated:
                users = [e for e in edges if e['dst'] == c['methods'][a] and e['kind'] == 'call']
                shadows.append(dict(cls=c['id'], name=a, method_line=funcs[c['methods'][a]].line, assigned_line=ln, assigned_in=fid,
                                    file=c['file'], static_callers=[dict(src=e['src'], line=e['line']) for e in users]))
    j('quality_findings.json', dict(attribute_shadows_method=shadows, no_static_caller=nocall, duplicate_bodies=dups, same_name_across_files=same_name,
                                    in_cycle=[sorted(s) for s in cyc]))
    return dict(cyc=cyc, msccs=msccs, call_sccs=call_sccs)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument('--root', default=os.path.abspath(os.path.join(here, '..', '..')))
    ap.add_argument('--out', default=os.path.abspath(os.path.join(here, '..')))
    a = ap.parse_args()
    P = build(a.root)
    r = export(P, a.root, a.out)
    print('modules', len(P['mods']), 'funcs', len(P['funcs']), 'classes', len(P['classes']), 'edges', len(P['edges']))
    print('import cycles', r['msccs'], 'call-level module cycles', len(r['call_sccs']), 'func cycles', len(r['cyc']))
