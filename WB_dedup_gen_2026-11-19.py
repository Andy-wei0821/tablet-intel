# -*- coding: utf-8 -*-
import re, io, os
BASE = os.path.dirname(os.path.abspath(__file__))
issues = ["2026-11-05","2026-11-06","2026-11-07","2026-11-08","2026-11-09","2026-11-10","2026-11-11","2026-11-12","2026-11-13","2026-11-16","2026-11-17","2026-11-18"]
out = []
for d in issues:
    fp = os.path.join(BASE, f"WB_{d}_硬件看板.html")
    if not os.path.exists(fp):
        print(d, "MISSING")
        continue
    with io.open(fp, encoding="utf-8") as f:
        html = f.read()
    t1 = re.findall(r'class="card-title"[^>]*>(.*?)</div>', html, re.S)
    t2 = re.findall(r'class="td-title"[^>]*><a[^>]*>(.*?)</a>', html, re.S)
    n = 0
    for t in t1 + t2:
        t = re.sub(r'<[^>]+>', '', t).strip()
        if t:
            out.append(f"{d}\t{t}")
            n += 1
    print(d, n)
with io.open(os.path.join(BASE, "_dedup_14d_2026-11-19.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("TOTAL", len(out))
