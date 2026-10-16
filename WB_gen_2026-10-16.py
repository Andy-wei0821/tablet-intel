# -*- coding: utf-8 -*-
"""生成 WB_2026-10-16_硬件看板.html —— 智能终端硬件情报日报
读取两个采集 JSON，应用已验证的替换（死链/错级修正），归一化、裁剪到 15+15，渲染合规单 HTML。
"""
import json

TODAY = "2026-10-16"
TODAY_INT = 20261016
OUT = r"E:/AI相关/预研究/202608/03_输出/WB_2026-10-16_硬件看板.html"
CN_JSON = r"E:/AI相关/预研究/202608/03_输出/_agent_cn_2026-10-16.json"
INTL_JSON = r"E:/AI相关/预研究/202608/03_输出/_agent_intl_2026-10-16.json"

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
    if s in ("已上市","开售","发布","发售","上架","现售"):
        base = "已上市"
    elif s in ("未上市","预售","曝光","官宣","定档","预热","即将上市"):
        base = "即将上市"
    elif s == "进行中":
        base = "进行中"
    else:
        base = "即将上市"
    if base == "已上市" and to_ymd(date_str) > TODAY_INT:
        base = "即将上市"
    return base

def cap_stars(g, s):
    s = int(s)
    return s if g == "A" else min(s, 4)

# ---------- 已验证替换条目（覆盖死链/错级） ----------
IQOO16 = {
    "region":"cn","title":"iQOO 16发布：第六代骁龙8超级至尊版+2K 165Hz+8400mAh",
    "category":"手机","main_dim":"SoC/芯片","dims":"SoC/芯片",
    "status":"已上市","stars":4,"grade":"B",
    "signal_type":"发布","corroboration":"1（今日头条/中国报道）",
    "key_params":"第六代骁龙8超级至尊版(2nm)；2K 165Hz 三星珠峰屏(2800nit)；8400mAh蓝海电池+100W有线；5000万三摄；9月29日开售",
    "tech_features":["首批2nm第六代骁龙8超级至尊版+自研Q4电竞芯片，支持全场景光追/超分/超帧并发",
                     "2K LEAD 2.0三星M16发光材料屏，165Hz+2800nit全局峰值，912万子像素逐屏校准",
                     "8400mAh蓝海大电池+100W有线闪充，8.5K VC冰穹散热系统",
                     "5000万三摄+IP68/IP69，运行OriginOS 7，KPL年度总决赛官方比赛用机"],
    "why":"iQOO数字旗舰迭代，2nm骁龙8超级至尊版+三星2K 165Hz屏+8400mAh，把电竞性能与续航推向新高度，与一加/REDMI在性能旗舰价位正面竞争。",
    "relevance":"牵引2nm骁龙旗舰平台、2K高刷屏、百瓦快充与游戏显示芯片供应链。",
    "vendor":"vivo/iQOO","date":"2026-09-29","url":"https://www.toutiao.com/article/7694182827554013705",
    "source_name":"今日头条(中国报道)","source_detail":"今日头条2026-09-29/10-08报道iQOO16正式发布并全渠道开售",
    "note":"起售价以官方为准；部分参数来自发布稿。"
}

LEINIAO_IO = {
    "region":"cn","title":"雷鸟 iO AI眼镜现货开售：34g双目显示+55语种翻译",
    "category":"AR-VR眼镜","main_dim":"显示/OLED","dims":"显示/OLED|AI/NPU",
    "status":"已上市","stars":3,"grade":"C",
    "signal_type":"发售","corroboration":"1（京东/雷鸟官方现货页）",
    "key_params":"双目显示翻译眼镜；34g；入眼亮度1800nit；55种语言实时翻译；240mAh+48h续航；10月15日现货开售；约¥2140起",
    "tech_features":["34g轻量双目显示AI眼镜，入眼亮度1800nit，佩戴接近日常镜架",
                     "支持55种语言实时翻译，骨传导音频，免掏手机沟通",
                     "240mAh电池，综合续航48小时，25分钟充至80%",
                     "雷鸟智能眼镜京东自营现货，国补后约¥2140起"],
    "why":"雷鸟以轻量双目显示+多语种翻译切入消费AI眼镜，延续RayNeo在AR光学的积累，丰富国产AI眼镜价格带。",
    "relevance":"国产AI眼镜在显示/翻译/轻量化方向的量产化代表，对MicroLED与语音供应链有牵引。",
    "vendor":"雷鸟/RayNeo iO","date":"2026-10-15","url":"https://www.rayneo.cn/",
    "source_name":"京东(雷鸟智能眼镜自营)","source_detail":"京东商品页2026-10-15现货开售(雷鸟 iO AI眼镜，34g/1800nit/55语种/48h)",
    "note":"数据来自京东/雷鸟官方现货页；具体参数以商品页为准。"
}

XREAL_AURA = {
    "region":"intl","title":"XREAL AURA发布：Android XR空间计算眼镜+70° FOV+Gemini",
    "category":"AR-VR眼镜","main_dim":"显示/OLED","dims":"显示/OLED|AI/NPU|摄像头",
    "status":"已上市","stars":5,"grade":"A",
    "signal_type":"发布","corroboration":"1（XREAL官方）",
    "key_params":"70°光学透视显示；Android XR+Gemini；骁龙Reality Elite+X1S双芯；95g；12G/256G $1279、16G/512G $1499",
    "tech_features":["70°光学透视FOV，Sony Micro-OLED 1920×1200/眼，1050nit，PPD 32，最高120Hz",
                     "Android XR+Gemini端侧AI，理解所见所问，可开最多五块虚拟屏",
                     "骁龙Reality Elite+XREAL X1S双芯分体架构，48 TOPS，整机仅95g轻量",
                     "电致变色调光、双摄6DoF追踪、Bose调音空间音频、指纹识别"],
    "why":"XREAL AURA以Android XR+Gemini把空间计算做成眼镜形态，70° FOV与分体双芯平衡性能与佩戴，是消费级AR眼镜与AI助手融合的标杆。",
    "relevance":"牵引Micro-OLED、Android XR生态、端侧Gemini与轻量化AR供应链，对AI眼镜赛道有外溢启示。",
    "vendor":"XREAL / AURA","date":"2026-10","url":"https://www.xreal.com/aura",
    "source_name":"XREAL官方","source_detail":"XREAL官方产品页(aura)，A级信源","note":"2026年10月上市，首发美/加/日/韩；具体国行节奏待确认。"
}

ANKER = {
    "region":"intl","title":"Anker Prime Qi2.2 25W折叠三合一充电器：主动散热+便携",
    "category":"无线充","main_dim":"电池/快充","dims":"电池/快充|散热|BMS/电源",
    "status":"已上市","stars":3,"grade":"B",
    "signal_type":"发售","corroboration":"1（9to5Mac）",
    "key_params":"Qi2.2 25W磁吸；三合一(手机+Apple Watch+AirPods)；折叠便携；主动风冷(AirCool 19dB)；含45W充电头；约$99",
    "tech_features":["Qi2.2认证25W磁吸无线充，三设备同充，折叠后掌心大小",
                     "内置主动散热AirCool(19dB)，控温<98.6°F保25W满速",
                     "随附45W USB-C充电头，支持110-220V国际电压",
                     "对标已停产MagSafe Duo，可立可折，旅行友好"],
    "why":"Anker把Qi2.2 25W三合一做成折叠便携形态并加入主动散热，填补MagSafe Duo退市后的旅行充电空档，推动高功率磁吸配件普及。",
    "relevance":"牵引Qi2.2高功率磁吸、无线充主动散热与BMS温控趋势。",
    "vendor":"Anker / Prime Qi2 25W Foldable 3-in-1","date":"2026-09-27",
    "url":"https://9to5mac.com/2026/09/27/anker-magsafe-travel-sized-3-in-1-charger-qi2",
    "source_name":"9to5Mac","source_detail":"9to5Mac 2026-09-27实测报道(Anker官方在售)",
    "note":"Amazon在售约$99；国行上市时间待确认。"
}

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
        "main_dim":it["main_dim"],"dims":it["main_dim"],
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

# ---------- 构建 CN（18 → 15） ----------
raw_cn = json.load(open(CN_JSON, encoding="utf-8"))
cn_clean = []
for it in raw_cn:
    t = it["title"]
    if "华为MatePad Mini 2" in t: continue          # 裁剪（曝光类，窗口内已饱和）
    if "小米金沙江" in t: continue                   # 裁剪
    if "安克AI会议耳机" in t or ("安克" in t and "会议耳机" in t): continue  # 裁剪
    if "雷鸟彩显" in t: continue                     # 死链（供应链文），以雷鸟 iO 替换
    if "iQOO 16" in t:
        cn_clean.append(IQOO16); continue            # 覆盖（修正 URL 为已验证发布稿）
    cn_clean.append(norm_cn(it))
cn_clean.append(LEINIAO_IO)                          # 雷鸟 iO 补位

# ---------- 构建 INTL（16 → 15） ----------
raw_intl = json.load(open(INTL_JSON, encoding="utf-8"))
intl_clean = []
for it in raw_intl:
    t = it["title"]
    if "Amazon Fire HD 8" in t: continue             # 裁剪（低星入门）
    if "Meta Ray-Ban Display" in t: continue        # 死链（meta.com 抓取失败），以 XREAL AURA 替换
    if "Twelve South" in t: continue                # 死链（Apple 商店泛类目），以 Anker 替换
    if "iPad Pro M5" in t:
        # 修正：TechPulse 媒体而非 Apple 官方；10-22 发售→即将上市
        it["source_grade"] = "B"
        it["source_name"] = "TechPulse"
        it["source_detail"] = "TechPulse科技媒体2026-09-06前瞻/10-22报道(非Apple官方页面)"
        it["note"] = "信源为科技媒体TechPulse，非Apple官方；10-22发售，截至出报日(10-16)未上市，状态记为即将上市。"
        intl_clean.append(norm_intl(it)); continue
    intl_clean.append(norm_intl(it))
intl_clean.append(XREAL_AURA)                        # 补位
intl_clean.append(ANKER)                             # 补位

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
