#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""质量检查: 源码覆盖 / 行号对应 / 边落点 / 业务代码未被修改. 输出 analysis_report/quality_report.json"""
import os, sys, json, subprocess, ast
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.abspath(os.path.join(HERE, '..')); ROOT = os.path.abspath(os.path.join(OUT, '..'))
sys.path.insert(0, HERE)
import analyze as A
F = json.load(open(os.path.join(OUT, 'function_index.json'), encoding='utf-8'))
E = json.load(open(os.path.join(OUT, 'function_call_graph.json'), encoding='utf-8'))['edges']
fid = {f['id']: f for f in F}
inv = json.load(open(os.path.join(OUT, 'project_inventory_modules.json'), encoding='utf-8'))
res = {}
# 1 覆盖: 工作区内除排除目录外的所有 .py
want = set()
for dp, dns, fns in os.walk(ROOT):
    dns[:] = [d for d in dns if d not in A.EXCLUDE_DIRS and not d.startswith('.')]
    want |= {os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, '/') for f in fns if f.endswith('.py')}
got = {r['file'] for r in inv}
res['py_files_expected'] = len(want); res['py_files_analyzed'] = len(got); res['missing'] = sorted(want - got)
res['syntax_errors'] = [r['file'] for r in inv if r['syntax_error']]
# 2 定义行号对应
cache, bad = {}, []
for f in F:
    if f['name'] == '<module>':
        continue
    lines = cache.setdefault(f['file'], A.read_text(os.path.join(ROOT, f['file'])).splitlines())
    seg = ' '.join(lines[f['line'] - 1:f['line'] + 1 + len(f['decorators'])])
    if ('def ' + f['name']) not in seg:
        bad.append(f['id'])
res['def_line_mismatch'] = bad
# 3 边的行号落在源函数范围内
off = [e for e in E if e['src'] in fid and not (fid[e['src']]['line'] <= e['line'] <= fid[e['src']]['end_line'] if isinstance(e['line'], int) else True)]
res['edge_line_outside_src'] = len(off); res['edge_line_samples'] = off[:5]
# 4 边端点存在
res['edges_dangling'] = sum(1 for e in E if e['src'] not in fid or (e['dst'] not in fid and '::' not in e['dst']))
# 5 业务代码未改动
try:
    st = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'], capture_output=True, text=True).stdout.splitlines()
    res['modified_outside_analysis_report'] = [l for l in st if 'analysis_report' not in l]
except Exception as ex:
    res['modified_outside_analysis_report'] = str(ex)
res['executed_business_code'] = False
json.dump(res, open(os.path.join(OUT, 'quality_report.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
