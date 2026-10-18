# -*- coding: utf-8 -*-
"""生成 WB_2026-10-16_硬件看板.html —— 智能终端硬件情报日报
读取两个采集 JSON，应用已验证的替换（死链/错级修正），归一化、裁剪到 15+15，渲染合规单 HTML。
"""
import json

TODAY = "2026-10-18"
TODAY_INT = 20261018
OUT = r"E:/AI相关/预研究/202608/03_输出/WB_2026-10-18_硬件看板.html"
CN_JSON = r"E:/AI相关/预研究/202608/03_输出/_agent_cn_2026-10-18.json"
INTL_JSON = r"E:/AI相关/预研究/202608/03_输出/_agent_intl_2026-10-18.json"

# 16 技术维度（固定顺序）
DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

CATEGORY_ORDER = ["平板","手机","智能手表","AR-VR眼镜","笔记本电脑","无线充","智能音箱","AI耳机·耳穿戴"]

def skey(d):
    d = (d or "").strip()
    try:
        if len(d) == 10:
            return int(d.replace("-",""))
        if len(d) == 7:
            y,m = d.split("-"); return int(y)*10000 + int(m)*100 + 15
        if len(d) == 4:
            return int(d)*10000 + 901
    except Exception:
        pass
    return 0

def to_ymd(s):
    s = (s or "").strip()
    try:
        if len(s) == 10:
            return int(s.replace("-",""))
        if len(s) == 7:
            y,m = s.split("-"); return int(y)*10000 + int(m)*100 + 15
    except Exception:
        pass
    return 0

STATUS_RANK = {"即将上市":0, "进行中":1, "已上市":2}

def norm_status(raw, date_str):
    s = (raw or "").strip()
    if any(k in s for k in ["即将","未上市","预售","曝光","官宣","定档","预热","预约","待发","公布","预告","前瞻"]):
        base = "即将上市"
    elif any(k in s for k in ["已上市","开售","发售","上架","现售","售卖","在售","上市","发布"]):
        base = "已上市"
    elif "进行中" in s:
        base = "进行中"
    else:
        base = "即将上市"
    if base == "已上市" and to_ymd(date_str) > TODAY_INT:
        base = "即将上市"
    return base

def cap_stars(g, s):
    s = int(s)
    return s if g == "A" else min(s, 4)

# ---------- 归一化 ----------
def corr_cn(n):
    try: n = int(n)
    except Exception: n = 1
    return "1（单源）" if n <= 1 else "2（多源印证）"

def corr_intl(detail, grade):
    d = detail or ""
    if ("/" in d) or ("、" in d) or ("印证" in d) or ("，" in d):
        return "多源印证（%s级）" % grade
    return "单源（%s级）" % grade

def norm_cn(it):
    date = it["date"]
    return {
        "region":"cn","title":it["title"],"category":it["category"],
        "main_dim":it["main_dim"],"dims":it.get("dims", it["main_dim"]),
        "status":norm_status(it["status"], date),"stars":cap_stars(it["source_level"], it["stars"]),
        "grade":it["source_level"],
        "signal_type":it["signal_type"],"corroboration":corr_cn(it.get("corroboration",1)),
        "key_params":it["key_params"],"tech_features":it["tech_features"],
        "why":it["why_important"],"relevance":"、".join(it.get("related",[])) if it.get("related") else "",
        "vendor":it["vendor"],"date":date,"url":it["url"],
        "source_name":it["source_name"],"source_detail":it["source_detail"],
        "note":it.get("note","")
    }

def norm_intl(it):
    date = it["date"]
    grade = it["source_grade"]
    domain = it.get("domain","")
    parts = [p.strip() for p in domain.split(",") if p.strip()]
    md = parts[0] if parts else "AI/NPU"
    dims = "|".join(parts) if parts else "AI/NPU"
    return {
        "region":"intl","title":it["title"],"category":it["category"],
        "main_dim":md,"dims":dims,
        "status":norm_status(it["status"], date),"stars":cap_stars(grade, it["stars"]),
        "grade":grade,
        "signal_type":it["signal_type"],"corroboration":corr_intl(it.get("source_detail",""), grade),
        "key_params":it["key_params"],"tech_features":it["tech_features"],
        "why":it["why_important"],"relevance":it.get("terminal_link",""),
        "vendor":it["vendor"],"date":date,"url":it["url"],
        "source_name":it.get("source_name", grade+"级信源"),"source_detail":it.get("source_detail",""),
        "note":it.get("note","")
    }

# ---------- 构建 CN / INTL（直接归一化，JSON 已为终稿） ----------
raw_cn = json.load(open(CN_JSON, encoding="utf-8"))
cn_clean = [norm_cn(it) for it in raw_cn]
raw_intl = json.load(open(INTL_JSON, encoding="utf-8"))
intl_clean = [norm_intl(it) for it in raw_intl]
assert len(cn_clean) == 15, "CN count=%d" % len(cn_clean)
assert len(intl_clean) == 15, "INTL count=%d" % len(intl_clean)

DATA = cn_clean + intl_clean

# ---------- 清洗：去除花括号 ----------
def clean(s):
    if isinstance(s, str):
        return s.replace("{", "").replace("}", "")
    if isinstance(s, list):
        return [clean(x) for x in s]
    return s
for d in DATA:
    for k, v in list(d.items()):
        d[k] = clean(v)

# ---------- 维度计数 ----------
dim_count = {dm: 0 for dm in DIMS}
for d in DATA:
    parts = [p.strip() for p in d["dims"].split("|")]
    for p in parts:
        if p in dim_count:
            dim_count[p] += 1
covered = sum(1 for dm in DIMS if dim_count[dm] > 0)
grade_count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for d in DATA:
    grade_count[d["grade"]] += 1
five_star = sum(1 for d in DATA if d["stars"] == 5)

# ---------- 排序（区内按状态→时间倒序） ----------
def sort_key(d):
    return (STATUS_RANK.get(d["status"], 9), -skey(d["date"]))
cn = sorted([d for d in DATA if d["region"]=="cn"], key=sort_key)
intl = sorted([d for d in DATA if d["region"]=="intl"], key=sort_key)
ordered = cn + intl

# ---------- Top5 ----------
def top_sort(d):
    gr = {"A":0,"B":1,"C":2,"D":3,"E":4}[d["grade"]]
    return (-d["stars"], gr, STATUS_RANK.get(d["status"],9), -skey(d["date"]))
top5 = sorted(DATA, key=top_sort)[:5]

# ---------- HTML 渲染 ----------
def stars(n):
    return "★" * n

def status_tag(status):
    if status == "即将上市":
        return '<span class="status-tag status-coming">即将上市</span>'
    if status == "进行中":
        return '<span class="status-tag status-progress">进行中</span>'
    return ""

def region_tag(region):
    if region == "cn":
        return '<span class="td-region region-cn">国内</span>'
    return '<span class="td-region region-intl">国际</span>'

def source_tag(g):
    return '<span class="source-tag source-%s">%s</span>' % (g.lower(), g)

def card_html(d, idx, expanded):
    n = idx
    cls = "intel-card %s%s" % (d["region"], " expanded" if expanded else "")
    tf = "".join('<li data-num="%s">%s</li>' % (chr(0x2460+i), t) for i, t in enumerate(d["tech_features"]))
    status_badge = ('<span class="status-tag status-coming">即将上市</span>' if d["status"]=="即将上市"
                   else '<span class="status-tag status-progress">进行中</span>' if d["status"]=="进行中" else "")
    return '''<!-- Card %(n)d: %(title)s -->
      <div class="%(cls)s" id="card-%(n)d">
        <div class="card-header" onclick="toggleCard('card-%(n)d')">
          <div class="card-num">%(n)d</div>
          <div class="card-title-area">
            <div class="card-title">%(title)s</div>
            <div class="card-badges">
              %(stag)s
              <span class="card-domain">%(domain)s</span>
              <span class="stars">%(stars)s</span>
              %(sbadge)s
            </div>
          </div>
          <span class="card-toggle">▼</span>
        </div>
        <div class="card-body">
          <div class="card-content">
            <div class="field-grid">
              <div class="field"><div class="field-label">信号类型</div><div class="field-value">%(stype)s</div></div>
              <div class="field"><div class="field-label">印证源数</div><div class="field-value">%(corr)s</div></div>
              <div class="field full"><div class="field-label">关键参数</div><div class="field-value">%(kp)s</div></div>
              <div class="field full"><div class="field-label">技术特性</div><div class="field-value"><ul class="tech-list">%(tf)s</ul></div></div>
              <div class="field full"><div class="field-label">为什么重要</div><div class="field-value">%(why)s</div></div>
              <div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">%(rel)s</div></div>
              <div class="field"><div class="field-label">厂商/型号</div><div class="field-value">%(vendor)s</div></div>
              <div class="field"><div class="field-label">时间</div><div class="field-value">%(date)s</div></div>
              <div class="field"><div class="field-label">URL</div><div class="field-value"><a href="%(url)s" target="_blank">%(sname)s</a></div></div>
              <div class="field"><div class="field-label">信源明细</div><div class="field-value">%(sdetail)s</div></div>
              <div class="field full"><div class="field-label">备注待印证</div><div class="field-value">%(note)s</div></div>
            </div>
          </div>
        </div>
      </div>''' % {
        "n": n, "cls": cls, "title": d["title"], "stag": source_tag(d["grade"]),
        "domain": d["dims"].replace("|","/"), "stars": stars(d["stars"]), "sbadge": status_badge,
        "stype": d["signal_type"], "corr": d["corroboration"], "kp": d["key_params"],
        "tf": tf, "why": d["why"], "rel": d["relevance"], "vendor": d["vendor"],
        "date": d["date"], "url": d["url"], "sname": d["source_name"],
        "sdetail": d["source_detail"], "note": d["note"]
    }

def summary_row(n, d):
    return ('<tr><td>%d</td><td class="td-title"><a href="#card-%d">%s</a></td><td>%s</td>'
            '<td>%s</td><td class="td-status">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>') % (
        n, n, d["title"], region_tag(d["region"]), d["dims"].replace("|","/"),
        status_tag(d["status"]), source_tag(d["grade"]), d["date"], stars(d["stars"]))

dim_chips = ""
for dm in DIMS:
    c = dim_count[dm]
    onoff = "on" if c > 0 else "off"
    dim_chips += '<div class="dim-chip %s">%s <span class="dim-count">%d条</span></div>' % (onoff, dm, c)

top_cards = ""
for i, d in enumerate(top5, 1):
    top_cards += '''      <div class="signal-card">
        <div><span class="sig-rank">%d</span><span class="sig-title">%s</span></div>
        <div class="sig-tags"><span class="sig-dim">%s</span><span class="sig-stars">%s</span></div>
        <div class="sig-key">%s</div>
      </div>''' % (i, d["title"], d["main_dim"], stars(d["stars"]), d["key_params"][:60])

NEED = ("title","region","category","main_dim","dims","status","stars","grade",
         "signal_type","corroboration","key_params","tech_features","why","relevance",
         "vendor","date","url","source_name","source_detail","note")
for d in DATA:
    for nk in NEED:
        assert nk in d, ("MISSING", nk, "IN", d.get("title"))

cn_cards = "\n".join(card_html(d, i+1, i==0) for i, d in enumerate(cn))
intl_cards = "\n".join(card_html(d, len(cn)+i+1, False) for i, d in enumerate(intl))
summary_rows = "\n".join(summary_row(i+1, d) for i, d in enumerate(ordered))

stat_a = grade_count["A"]; stat_b = grade_count["B"]

HTML = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>智能终端硬件情报日报 · %(TODAY)s</title>
<style>
  :root {
    --bg: #f5f7fa; --card-bg: #fff; --border: #e4e7ed;
    --text: #303133; --text-secondary: #606266; --text-tertiary: #909399;
    --primary: #409eff; --success: #67c23a; --warning: #e6a23c; --danger: #f56c6c; --info: #909399;
    --tag-a: #67c23a; --tag-b: #409eff; --tag-c: #e6a23c; --tag-d: #f56c6c; --tag-e: #aa55ff;
    --shadow: 0 2px 12px rgba(0,0,0,0.06); --shadow-hover: 0 4px 20px rgba(0,0,0,0.1); --radius: 10px;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--text); line-height:1.6; padding:20px; }
  .container { max-width:1200px; margin:0 auto; }
  .header { background:linear-gradient(135deg,#667eea 0%%,#764ba2 100%%); color:#fff; border-radius:var(--radius); padding:28px 32px; margin-bottom:20px; box-shadow:var(--shadow); }
  .header h1 { font-size:24px; margin-bottom:8px; }
  .header .subtitle { font-size:14px; opacity:0.9; }
  .header .meta { display:flex; gap:12px; margin-top:14px; flex-wrap:wrap; }
  .meta-badge { background:rgba(255,255,255,0.2); border:1px solid rgba(255,255,255,0.3); border-radius:20px; padding:4px 14px; font-size:13px; }
  .stats-bar { display:flex; gap:16px; margin-bottom:24px; flex-wrap:wrap; }
  .stat-item { background:var(--card-bg); border-radius:var(--radius); padding:14px 20px; box-shadow:var(--shadow); flex:1; min-width:140px; text-align:center; }
  .stat-num { font-size:22px; font-weight:700; color:var(--primary); }
  .stat-label { font-size:12px; color:var(--text-tertiary); margin-top:4px; }
  .dim-panel { background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }
  .dim-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }
  .dim-title { font-size:16px; font-weight:700; display:flex; align-items:center; gap:8px; }
  .dim-title::before { content:''; width:4px; height:18px; background:var(--success); border-radius:2px; }
  .dim-counter { font-size:14px; color:var(--text-secondary); }
  .dim-counter .dim-num { font-size:18px; font-weight:600; color:var(--success); }
  .dim-counter .dim-total { color:var(--text-tertiary); }
  .dim-bar { width:100%%; height:8px; background:#f0f2f5; border-radius:4px; margin-bottom:16px; overflow:hidden; }
  .dim-bar-fill { height:100%%; background:linear-gradient(90deg,#67c23a,#95d475); border-radius:4px; transition:width 0.5s; }
  .dim-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
  .dim-chip { padding:8px 12px; border-radius:8px; font-size:13px; font-weight:500; display:flex; justify-content:space-between; align-items:center; }
  .dim-chip.on { background:#f0f9eb; border:1px solid #c2e7b0; color:#67c23a; }
  .dim-chip.off { background:#f5f7fa; border:1px solid #e4e7ed; color:#c0c4cc; }
  .dim-chip .dim-count { font-size:11px; opacity:0.7; font-weight:400; }
  .summary-section { background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }
  .section-title { font-size:16px; font-weight:700; margin-bottom:14px; display:flex; align-items:center; gap:8px; }
  .section-title::before { content:''; width:4px; height:18px; background:var(--primary); border-radius:2px; }
  table { width:100%%; border-collapse:collapse; font-size:13px; }
  thead th { background:#f0f2f5; padding:10px 12px; text-align:left; font-weight:600; color:var(--text-secondary); border-bottom:2px solid var(--border); white-space:nowrap; }
  tbody td { padding:10px 12px; border-bottom:1px solid var(--border); vertical-align:top; }
  tbody tr:hover { background:#f5f7fa; }
  tbody tr:last-child td { border-bottom:none; }
  .td-title { font-weight:600; color:var(--text); }
  .td-region { font-size:12px; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; }
  .region-cn { background:#ecf5ff; color:#409eff; }
  .region-intl { background:#fdf6ec; color:#e6a23c; }
  .source-tag { display:inline-block; font-size:12px; font-weight:700; padding:2px 10px; border-radius:12px; white-space:nowrap; }
  .source-a { background:#f0f9eb; color:var(--tag-a); border:1px solid #c2e7b0; }
  .source-b { background:#ecf5ff; color:var(--tag-b); border:1px solid #b3d8ff; }
  .source-c { background:#fdf6ec; color:var(--tag-c); border:1px solid #f5dab1; }
  .source-d { background:#fef0f0; color:var(--tag-d); border:1px solid #fbc4c4; }
  .source-e { background:#f3f0ff; color:var(--tag-e); border:1px solid #d3c2ff; }
  .status-tag { display:inline-block; font-size:11px; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; margin-left:8px; }
  .td-status .status-tag { margin-left:0; font-size:10px; padding:1px 6px; }
  .status-coming { background:#ecf5ff; color:#409eff; border:1px solid #b3d8ff; }
  .status-released { background:#f0f9eb; color:#67c23a; border:1px solid #c2e7b0; }
  .status-progress { background:#f4f4f5; color:#909399; border:1px solid #e4e7ed; }
  .intel-section { margin-bottom:24px; }
  .intel-cards { display:grid; grid-template-columns:1fr; gap:16px; }
  .intel-card { background:var(--card-bg); border-radius:var(--radius); box-shadow:var(--shadow); overflow:hidden; transition:box-shadow 0.3s; border-left:4px solid var(--primary); }
  .intel-card.cn { border-left-color:var(--tag-b); }
  .intel-card.intl { border-left-color:var(--tag-c); }
  .intel-card:hover { box-shadow:var(--shadow-hover); }
  .card-header { padding:16px 20px; cursor:pointer; display:flex; align-items:flex-start; gap:12px; user-select:none; }
  .card-num { flex-shrink:0; width:28px; height:28px; border-radius:50%%; background:#f0f2f5; color:var(--text-secondary); font-size:13px; font-weight:700; display:flex; align-items:center; justify-content:center; margin-top:2px; }
  .intel-card.cn .card-num { background:#ecf5ff; color:var(--tag-b); }
  .intel-card.intl .card-num { background:#fdf6ec; color:var(--tag-c); }
  .card-title-area { flex:1; }
  .card-title { font-size:15px; font-weight:600; color:var(--text); margin-bottom:6px; }
  .card-badges { display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
  .card-badges .stars { font-size:12px; color:var(--warning); letter-spacing:1px; }
  .card-domain { font-size:12px; color:var(--text-tertiary); background:#f5f7fa; padding:2px 8px; border-radius:4px; }
  .card-toggle { flex-shrink:0; color:var(--text-tertiary); font-size:14px; transition:transform 0.3s; margin-top:4px; }
  .intel-card.expanded .card-toggle { transform:rotate(180deg); }
  .card-body { max-height:0; overflow:hidden; transition:max-height 0.4s ease; }
  .intel-card.expanded .card-body { max-height:3000px; }
  .card-content { padding:0 20px 18px 20px; border-top:1px solid var(--border); padding-top:16px; }
  .field-grid { display:grid; grid-template-columns:1fr 1fr; gap:12px 20px; }
  .field { display:flex; flex-direction:column; gap:4px; }
  .field.full { grid-column:1 / -1; }
  .field-label { font-size:12px; font-weight:600; color:var(--text-tertiary); letter-spacing:0.5px; }
  .field-value { font-size:13px; color:var(--text-secondary); line-height:1.7; }
  .field-value a { color:var(--primary); text-decoration:none; word-break:break-all; }
  .field-value a:hover { text-decoration:underline; }
  .field-value .tech-list { padding-left:0; list-style:none; }
  .field-value .tech-list li { padding:2px 0; padding-left:18px; position:relative; }
  .field-value .tech-list li::before { content:attr(data-num); position:absolute; left:0; font-weight:700; color:var(--primary); }
  @media (max-width:768px) { .field-grid { grid-template-columns:1fr; } .dim-grid { grid-template-columns:repeat(2,1fr); } table { font-size:12px; } thead th,tbody td { padding:8px 6px; } }

  html { scroll-behavior: smooth; }
  .td-title a { color: inherit; text-decoration: none; }
  .td-title a:hover { color: var(--primary); text-decoration: underline; }
  .top-signals-panel { background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }
  .top-signals-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }
  .top-signals-title { font-size:16px; font-weight:700; display:flex; align-items:center; gap:8px; }
  .top-signals-title::before { content:''; width:4px; height:18px; background:var(--warning); border-radius:2px; }
  .top-signals-grid { display:grid; grid-template-columns:repeat(5,1fr); gap:12px; }
  .signal-card { background:linear-gradient(135deg,#f5f7fa,#fafafa); border-radius:8px; padding:12px 14px; border-left:3px solid var(--success); transition:box-shadow 0.3s; }
  .signal-card:hover { box-shadow:var(--shadow-hover); }
  .signal-card .sig-rank { display:inline-block; font-size:11px; font-weight:700; color:#fff; background:var(--success); border-radius:50%%; width:18px; height:18px; text-align:center; line-height:18px; margin-right:6px; }
  .signal-card .sig-title { font-size:13px; font-weight:600; color:var(--text); line-height:1.4; }
  .signal-card .sig-tags { display:flex; gap:4px; flex-wrap:wrap; margin-bottom:4px; margin-top:6px; }
  .signal-card .sig-dim { font-size:11px; background:#f0f9eb; color:#67c23a; border-radius:4px; padding:1px 6px; }
  .signal-card .sig-stars { font-size:12px; color:#e6a23c; }
  .signal-card .sig-key { font-size:11px; color:var(--text-secondary); line-height:1.5; margin-top:4px; }
</style>
</head>
<body>
<div class="container">

  <!-- Header -->
  <div class="header">
    <h1>智能终端硬件情报日报 · %(TODAY)s</h1>
    <div class="subtitle">采集口径：8类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑/AI耳机·耳穿戴） | 搜索窗口60天 | 国内15条 + 国际15条</div>
    <div class="meta">
      <span class="meta-badge">总情报 30条</span>
      <span class="meta-badge">国内 15条</span>
      <span class="meta-badge">国际 15条</span>
      <span class="meta-badge">信源 A-E级</span>
      <span class="meta-badge">搜索窗口 60天</span>
    </div>
  </div>

  <!-- Stats Bar -->
  <div class="stats-bar">
    <div class="stat-item"><div class="stat-num">30</div><div class="stat-label">总情报数</div></div>
    <div class="stat-item"><div class="stat-num">%(A)d</div><div class="stat-label">A级信源</div></div>
    <div class="stat-item"><div class="stat-num">%(B)d</div><div class="stat-label">B级信源</div></div>
    <div class="stat-item"><div class="stat-num">8</div><div class="stat-label">覆盖产品类别</div></div>
    <div class="stat-item"><div class="stat-num">%(FS)d</div><div class="stat-label">五星条数</div></div>
  </div>

  <!-- Dimension Coverage Panel -->
  <div class="dim-panel">
    <div class="dim-header">
      <div class="dim-title">技术维度覆盖面板</div>
      <div class="dim-counter"><span class="dim-num">%(COV)d</span><span class="dim-total"> / 16 维度</span></div>
    </div>
    <div class="dim-bar"><div class="dim-bar-fill" style="width:%(PCT).2f%%"></div></div>
    <div class="dim-grid">
      %(DIMCHIPS)s
    </div>
  </div>

  <!-- Top 5 Key Signals -->
  <div class="top-signals-panel">
    <div class="top-signals-header">
      <div class="top-signals-title">今日重点信号 Top 5</div>
      <div style="font-size:12px;color:var(--text-tertiary);">排序：星级降序→信源等级→状态优先→时间倒序</div>
    </div>
    <div class="top-signals-grid">
      %(TOPCARDS)s
    </div>
  </div>

  <!-- Summary Table -->
  <div class="summary-section">
    <div class="section-title">今日概要表</div>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>领域</th><th>上市状态</th><th>信源</th><th>时间</th><th>重要度</th></tr></thead>
      <tbody>
%(SUMMARY)s
      </tbody>
    </table>
  </div>

  <!-- Domestic Intelligence -->
  <div class="intel-section">
    <div class="section-title">一、国内情报（15条）</div>
      <div class="intel-cards">
%(CN)s
      </div>
  </div>

  <!-- International Intelligence -->
  <div class="intel-section">
    <div class="section-title">二、国际情报（15条）</div>
      <div class="intel-cards">
%(INTL)s
      </div>
  </div>

</div>
<script>
function toggleCard(id) {
  var el = document.getElementById(id);
  if (el.classList.contains('expanded')) { el.classList.remove('expanded'); }
  else { el.classList.add('expanded'); }
}
</script>
</body>
</html>''' % {
    "TODAY": TODAY, "A": stat_a, "B": stat_b, "FS": five_star, "COV": covered,
    "PCT": covered/16.0*100, "DIMCHIPS": dim_chips, "TOPCARDS": top_cards,
    "SUMMARY": summary_rows, "CN": cn_cards, "INTL": intl_cards
}

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print("written:", OUT)
print("covered dims:", covered, "/16")
print("A/B/C/D/E:", grade_count)
print("five_star:", five_star)
print("cn:", len(cn), "intl:", len(intl))
print("top5:", [d["title"][:24] for d in top5])
