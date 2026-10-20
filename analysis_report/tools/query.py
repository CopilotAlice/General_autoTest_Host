#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""指定函数的上下游调用链: python analysis_report/tools/query.py <函数名子串> [--depth 3] [--legacy]"""
import json, os, sys, argparse, collections
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ap = argparse.ArgumentParser(); ap.add_argument('name'); ap.add_argument('--depth', type=int, default=3); ap.add_argument('--legacy', action='store_true')
a = ap.parse_args()
F = {f['id']: f for f in json.load(open(os.path.join(R, 'function_index.json'), encoding='utf-8'))}
G = json.load(open(os.path.join(R, 'function_call_graph.json'), encoding='utf-8'))['edges']
out, inn = collections.defaultdict(list), collections.defaultdict(list)
for e in G:
    if e['kind'] != 'defines':
        out[e['src']].append(e); inn[e['dst']].append(e)
hits = [i for i, f in F.items() if a.name.lower() in f['qualname'].lower() and (a.legacy or not f['legacy'])]
if not hits:
    sys.exit('未找到: ' + a.name)
def walk(fid, table, key, d, path, ind):
    for e in table.get(fid, []):
        n = e[key]
        f = F.get(n)
        if not f:
            continue
        rec = ' ↻递归/循环' if n in path else ''
        print(f'{ind}[{e["kind"]}/{e["conf"]}@L{e["line"]}] {f["module"]}::{f["qualname"]} ({f["file"]}:{f["line"]}){rec}')
        if d > 1 and not rec:
            walk(n, table, key, d - 1, path | {n}, ind + '    ')
for h in hits:
    f = F[h]
    print(f'\n=== {h}  ({f["file"]}:{f["line"]}) flags={f["flags"]}')
    print('-- 下游(被它调用):'); walk(h, out, 'dst', a.depth, {h}, '  ')
    print('-- 上游(调用它):'); walk(h, inn, 'src', a.depth, {h}, '  ')
