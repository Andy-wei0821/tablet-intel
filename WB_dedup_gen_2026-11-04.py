# -*- coding: utf-8 -*-
"""扫描近 14 天看板，生成去重清单（标题清单）"""
import re, os

BASE = r"E:/AI相关/预研究/202608/03_输出/"
FILES = ["WB_2026-10-31_硬件看板.html", "WB_2026-11-01_硬件看板.html",
         "WB_2026-11-02_硬件看板.html", "WB_2026-11-03_硬件看板.html"]
OUT = BASE + "_dedup_14d_2026-11-04.txt"

pat_card = re.compile(r'class="card-title"[^>]*>(.*?)</div>', re.S)
pat_td = re.compile(r'class="td-title"[^>]*><a[^>]*>(.*?)</a>', re.S)

rows = []
for fn in FILES:
    p = BASE + fn
    if not os.path.exists(p):
        print("MISS", fn); continue
    html = open(p, encoding="utf-8").read()
    titles = set()
    for m in pat_card.findall(html) + pat_td.findall(html):
        t = re.sub(r'<[^>]+>', '', m).strip()
        t = re.sub(r'\s+', ' ', t)
        if t:
            titles.add(t)
    d = fn[3:13]
    print(fn, len(titles))
    for t in sorted(titles):
        rows.append(d + "\t" + t)

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(rows))
print("TOTAL", len(rows), "->", OUT)
