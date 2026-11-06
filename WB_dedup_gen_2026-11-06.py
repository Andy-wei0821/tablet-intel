# -*- coding: utf-8 -*-
import re, glob, os
BASE = r"E:/AI相关/预研究/202608/03_输出/"
files = ["WB_2026-10-31_硬件看板.html","WB_2026-11-01_硬件看板.html","WB_2026-11-02_硬件看板.html","WB_2026-11-03_硬件看板.html","WB_2026-11-04_硬件看板.html"]
out=[]
for f in files:
    p = BASE+f
    if not os.path.exists(p):
        print("MISSING", f); continue
    h = open(p, encoding="utf-8").read()
    titles = re.findall(r'class="card-title"[^>]*>(.*?)</div>', h, re.S)
    n=0
    for t in titles:
        t = re.sub(r'<[^>]+>','',t).strip()
        if t:
            out.append((f[3:13], t)); n+=1
    print(f, n)
seen=set(); lines=[]
for d,t in out:
    k=t
    if k in seen: continue
    seen.add(k); lines.append("%s\t%s" % (d,t))
with open(BASE+"_dedup_14d_2026-11-06.txt","w",encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print("total", len(lines))
