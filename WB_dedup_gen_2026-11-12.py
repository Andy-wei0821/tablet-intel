# -*- coding: utf-8 -*-
import re, io, os
BASE = os.path.dirname(os.path.abspath(__file__))
issues = ["2026-10-31","2026-11-01","2026-11-02","2026-11-03","2026-11-04","2026-11-06","2026-11-07","2026-11-08","2026-11-09","2026-11-10","2026-11-11"]
out = []
for d in issues:
    fp = os.path.join(BASE, f"WB_{d}_硬件看板.html")
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
with io.open(os.path.join(BASE, "_dedup_14d_2026-11-12.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("TOTAL", len(out))
