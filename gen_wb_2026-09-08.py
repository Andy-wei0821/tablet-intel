# -*- coding: utf-8 -*-
"""生成 WB_2026-09-08_硬件看板.html（每日智能终端硬件情报日报）"""
import json, re, html, os

BASE = "E:/AI相关/预研究/202608/03_输出"
DATE = "2026-09-08"
WEEKDAY = "周二"

# ---------- 读取数据 ----------
cn = json.load(open(f"{BASE}/_agent_cn_2026-09-08.json", encoding="utf-8"))
intl_full = json.load(open(f"{BASE}/_agent_intl_2026-09-08.json", encoding="utf-8"))
intl_fill = json.load(open(f"{BASE}/_agent_intl_fill_2026-09-08.json", encoding="utf-8"))

# 丢弃与 CN 区重复的 3 条 + 与 09-07 去重表冲突的 2 条（INTL 区）
DROP = ["MatePad Air", "小米平板9 Pro Max", "Yoga Tab Plus Gen 2", "小米 18 Fold", "Moto Watch Ultra"]
intl_kept = [it for it in intl_full if not any(d in it["title"] for d in DROP)]

all_items = cn + intl_kept + intl_fill
assert len(all_items) == 30, f"期望 30 条，实际 {len(all_items)}"

# ---------- 排序：状态(即将上市→进行中→已上市)，同状态内时间倒序 ----------
STATUS_RANK = {"coming": 0, "progress": 1, "released": 2}
STATUS_LABEL = {"coming": "即将上市", "progress": "进行中", "released": "已上市"}
STATUS_CLASS = {"coming": "status-coming", "progress": "status-progress", "released": "status-released"}
SRC_RANK = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

all_items.sort(key=lambda c: c["time"], reverse=True)           # 时间倒序（稳定）
all_items.sort(key=lambda c: STATUS_RANK[c["status"]], reverse=False)  # 状态升序（稳定，保组内时间倒序）

def stars_str(n): return "★★★★★"[:n] + "☆☆☆☆☆"[:5 - n]

def corr(c):
    if isinstance(c, int): return f"{c} 个印证源"
    s = str(c).replace(" sources", " 个印证源").replace(" source", " 个印证源")
    return s

def s(x):
    if x is None: return ""
    return html.escape(str(x).replace("{", "").replace("}", ""))

# ---------- Top5 重点信号：星级降序→信源升序(A优先)→状态优先→时间倒序 ----------
top_pool = [c for c in all_items if c["stars"] >= 4]
top_pool.sort(key=lambda c: c["time"], reverse=True)
top_pool.sort(key=lambda c: (SRC_RANK[c["source_grade"]], STATUS_RANK[c["status"]]), reverse=False)
top_pool.sort(key=lambda c: -c["stars"], reverse=False)
top5 = top_pool[:5]

# ---------- 16 维覆盖 ----------
DIMS = ["SoC/芯片", "显示/OLED", "折叠屏", "手写笔/触控", "散热/液冷", "电池/续航",
        "快充/无线充", "影像", "AI/NPU", "音频/扬声器", "5G/通信", "Wi-Fi/连接",
        "AR/VR显示", "材质/工艺", "可持续/模块化", "手柄/外设"]
dim_count = {d: 0 for d in DIMS}
for it in all_items:
    for d in it.get("dims", []):
        if d in dim_count: dim_count[d] += 1
covered = sum(1 for d in DIMS if dim_count[d] > 0)

A = sum(1 for it in all_items if it["source_grade"] == "A")
B = sum(1 for it in all_items if it["source_grade"] == "B")
five = sum(1 for it in all_items if it["stars"] == 5)

# ---------- 提取模板 CSS / JS ----------
tmpl = open(f"{BASE}/WB_2026-09-07_硬件看板.html", encoding="utf-8").read()
css = re.search(r"<style>(.*?)</style>", tmpl, re.S).group(1)
script = re.search(r"<script>(.*?)</script>", tmpl, re.S).group(1)

# ---------- 卡片 ----------
def card_html(it, idx):
    region_cls = "cn" if it["region"] == "cn" else "intl"
    expanded = " expanded" if idx == 1 else ""
    stars = stars_str(it["stars"])
    src_cls = "source-" + it["source_grade"].lower()
    st_cls = STATUS_CLASS[it["status"]]
    st_lbl = STATUS_LABEL[it["status"]]
    tech = "".join(f'        <li data-num="{i+1}">{s(t)}</li>\n' for i, t in enumerate(it["tech_features"]))
    return f'''      <div class="intel-card {region_cls}{expanded}" id="card-{idx}">
        <div class="card-header" onclick="toggleCard(this)">
          <div class="card-num">{idx}</div>
          <div class="card-title-area">
            <div class="card-title">{s(it['title'])}</div>
            <div class="card-badges">
              <span class="stars">{stars}</span>
              <span class="source-tag {src_cls}">{it['source_grade']}</span>
              <span class="status-tag {st_cls}">{st_lbl}</span>
              <span class="card-domain">{s(it['category'])}</span>
            </div>
          </div>
          <div class="card-toggle">▼</div>
        </div>
        <div class="card-body">
          <div class="card-content">
            <div class="field-grid">
              <div class="field"><div class="field-label">信号类型</div><div class="field-value">{s(it['signal_type'])}</div></div>
              <div class="field"><div class="field-label">印证源数</div><div class="field-value">{s(corr(it['corroboration']))}</div></div>
              <div class="field full"><div class="field-label">关键参数</div><div class="field-value">{s(it['key_params'])}</div></div>
              <div class="field full"><div class="field-label">技术特性</div><div class="field-value"><ul class="tech-list">
{tech}      </ul></div></div>
              <div class="field full"><div class="field-label">为什么重要</div><div class="field-value">{s(it['why_matters'])}</div></div>
              <div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">{s(it['relevance'])}</div></div>
              <div class="field"><div class="field-label">厂商</div><div class="field-value">{s(it['vendor'])}</div></div>
              <div class="field"><div class="field-label">型号</div><div class="field-value">{s(it['model'])}</div></div>
              <div class="field"><div class="field-label">时间</div><div class="field-value">{s(it['time'])}</div></div>
              <div class="field"><div class="field-label">来源URL</div><div class="field-value"><a href="{html.escape(it['source_url'])}" target="_blank">{s(it['source_name'])}</a></div></div>
              <div class="field full"><div class="field-label">信源明细</div><div class="field-value">{s(it['source_detail'])}</div></div>
              <div class="field full"><div class="field-label">备注/待印证</div><div class="field-value">{s(it['notes'])}</div></div>
            </div>
          </div>
        </div>
      </div>'''

# ---------- 摘要表行 ----------
def summary_row(it, idx):
    region_cls = "region-cn" if it["region"] == "cn" else "region-intl"
    region_lbl = "国内" if it["region"] == "cn" else "国际"
    src_cls = "source-" + it["source_grade"].lower()
    st_cls = STATUS_CLASS[it["status"]]
    st_lbl = STATUS_LABEL[it["status"]]
    return f'''      <tr>
        <td>{idx}</td>
        <td class="td-title"><a href="#card-{idx}">{s(it['title'])}</a></td>
        <td><span class="td-region {region_cls}">{region_lbl}</span></td>
        <td>{s(it['category'])}</td>
        <td><span class="source-tag {src_cls}">{it['source_grade']}</span></td>
        <td class="td-status"><span class="status-tag {st_cls}">{st_lbl}</span></td>
        <td>{s(it['time'])}</td>
      </tr>'''

# ---------- Top5 卡片 ----------
def top_card(it, rank):
    return f'''      <div class="signal-card">
        <div><span class="sig-rank">{rank}</span><span class="sig-title">{s(it['title'])}</span></div>
        <div class="sig-tags"><span class="sig-dim">{s(it['category'])}</span><span class="sig-stars">{stars_str(it['stars'])}</span></div>
        <div class="sig-key">{s(it['source_grade'])}级 / {s(it['key_params'][:110])}</div>
      </div>'''

summary_rows = "\n".join(summary_row(it, i + 1) for i, it in enumerate(all_items))
cards = "\n".join(card_html(it, i + 1) for i, it in enumerate(all_items))
top_cards = "\n".join(top_card(it, i + 1) for i, it in enumerate(top5))
dim_html = "".join(f'      <div class="dim-chip {"on" if dim_count[d] > 0 else "off"}">{d} <span class="dim-count">{dim_count[d]}条</span></div>\n' for d in DIMS)

doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>智能终端硬件情报日报 · {DATE}（{WEEKDAY}）</title>
  <style>{css}</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>智能终端硬件情报日报 · {DATE}（{WEEKDAY}）</h1>
    <div class="subtitle">采集口径：8类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑/AI耳机·耳穿戴） | 搜索窗口60天 | 去重窗口14天</div>
    <div class="meta">
      <span class="meta-badge">总情报 30条</span>
      <span class="meta-badge">国内 15条</span>
      <span class="meta-badge">国际 15条</span>
      <span class="meta-badge">信源 A-E级</span>
      <span class="meta-badge">搜索窗口 60天</span>
    </div>
  </div>
  <div class="stats-bar">
    <div class="stat-item"><div class="stat-num">30</div><div class="stat-label">总情报数</div></div>
    <div class="stat-item"><div class="stat-num">{A}</div><div class="stat-label">A级信源</div></div>
    <div class="stat-item"><div class="stat-num">{B}</div><div class="stat-label">B级信源</div></div>
    <div class="stat-item"><div class="stat-num">8</div><div class="stat-label">覆盖产品类别</div></div>
    <div class="stat-item"><div class="stat-num">{five}</div><div class="stat-label">五星条数</div></div>
  </div>
  <div class="dim-panel">
    <div class="dim-header">
      <div class="dim-title">技术维度覆盖面板</div>
      <div class="dim-counter"><span class="dim-num">{covered}</span><span class="dim-total"> / 16 维度</span></div>
    </div>
    <div class="dim-bar"><div class="dim-bar-fill" style="width:{int(covered/16*100)}%"></div></div>
    <div class="dim-grid">
{dim_html}    </div>
  </div>
  <div class="top-signals-panel">
    <div class="top-signals-header">
      <div class="top-signals-title">今日重点信号 Top 5</div>
      <div style="font-size:12px;color:var(--text-tertiary);">排序：A级优先→星级降序→状态优先→时间倒序</div>
    </div>
    <div class="top-signals-grid">
{top_cards}    </div>
  </div>
  <div class="summary-section">
    <div class="section-title">情报摘要表</div>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>类别</th><th>信源</th><th>状态</th><th>时间</th></tr></thead>
      <tbody>
{summary_rows}
      </tbody>
    </table>
  </div>
  <div class="intel-section">
    <div class="section-title">情报详情卡片</div>
    <div class="intel-cards">
{cards}
    </div>
  </div>
</div>
<script>{script}</script>
</body>
</html>'''

out = f"{BASE}/WB_2026-09-08_硬件看板.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(doc)

print("OK 生成", out)
print("总条数", len(all_items), "| A级", A, "| B级", B, "| 五星", five, "| 覆盖维度", covered)
print("Top5:", [t["title"] for t in top5])
print("丢弃 INTL 重复/冲突条数:", len(intl_full) - len(intl_kept))
