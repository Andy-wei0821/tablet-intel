# -*- coding: utf-8 -*-
"""生成 WB_2026-11-04_硬件看板.html —— 智能终端硬件情报日报
加载双 Agent 采集 JSON + 主代理复核修补（4 条旧闻/死链替换、6 条换源/校准），
按状态排序渲染合规单 HTML。
"""
import json
import re

TODAY = "2026-11-04"
TODAY_INT = 20261104
BASE = r"E:/AI相关/预研究/202608/03_输出/"
OUT = BASE + "WB_2026-11-04_硬件看板.html"

DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

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
    if base == "已上市" and skey(date_str) > TODAY_INT:
        base = "即将上市"
    return base

def cap_stars(g, s):
    s = int(s)
    return s if g == "A" else min(s, 4)

def clean(s):
    if isinstance(s, str):
        s = s.replace("{", "").replace("}", "")
        s = re.sub(r'^[①-⑩]\s*', '', s.strip())
        return s
    if isinstance(s, list):
        return [clean(x) for x in s]
    return s

CN_NEW = [
{
 "region":"cn","category":"平板","title":"小米平板9 Pro Max 蝉联10月安兔兔平板性能榜第一：玄戒O3断层领先",
 "status":"已上市","date":"2026-11-03","main_dim":"SoC/芯片","dims":"SoC/芯片|显示/OLED|电池/快充",
 "grade":"B","stars":4,"signal_type":"榜单/性能信号","corroboration":2,
 "key_params":"玄戒O3（10核全大核+首发16核G2-Ultra GPU+NPU 200TOPS，240亿晶体管，LPDDR6 113.8GB/s）整机安兔兔V12跑分5206401，领先第二名iQOO Pad Ultra（骁龙8至尊版Gen6，4847214）约36万分；13.3英寸3.4K 144Hz原色屏，12000mAh+120W，5.67mm/645g",
 "tech_features":["玄戒O3为榜单中唯一非骁龙平台，自研SoC平板断层领先","13.3英寸3.4K高刷原色屏，可选纳米柔光版","12000mAh大电池+120W快充，6麦克风+8扬声器","首发澎湃OS 4，支持DP-in秒变拓展屏"],
 "why_important":"小米自研玄戒O3在平板形态完成对高通旗舰SoC的性能反超，验证国产SoC在大屏散热冗余下的真实竞争力，是国产芯片进入生产力终端的标志性信号。",
 "relevance":"自研SoC+大屏平板组合直接对标iPad Pro/MatePad Pro Max高端段；对平板产品线SoC选型（自研vs高通）与散热设计提供参照。",
 "vendor":"小米/平板9 Pro Max","url":"https://finance.sina.cn/tech/2026-11-03/detail-inixkzyf0053409.d.html",
 "source_name":"新浪财经（快科技）","source_detail":"快科技/新浪财经 2026-11-03 安兔兔10月平板性能榜报道；小米官网 mi.com 产品页印证规格",
 "note":"产品已于9月10日开售（4799元起），本条收录其10月性能榜信号；区别于11-01期已覆盖的小米平板9/9 Pro标准版"
},
{
 "region":"cn","category":"AI耳机·耳穿戴","title":"漫步者IR披露：多款AI耳机密集上市，Lolli5 ANC接入豆包+DeepSeek双大模型",
 "status":"已上市","date":"2026-10-28","main_dim":"AI/NPU","dims":"AI/NPU|音频",
 "grade":"B","stars":4,"signal_type":"投资者关系披露/产品矩阵","corroboration":2,
 "key_params":"Lolli5 ANC：充电仓智能触控屏+豆包/DeepSeek双大模型协同（会议录音、实时互译、AI会议速记）；Comfo Clip Ultra：四麦+双骨导通话降噪+AI运动教练；NeoBuds Pro 5：1动圈+2楼氏动铁三分频；W800NB 118小时续航；前三季度营收20.81亿元(+1.21%)、归母净利3.40亿元(+13.37%)",
 "tech_features":["耳机端全面接入豆包与DeepSeek双大模型，漫翻译支持多国语言实时互译","Lolli5 ANC充电仓触控屏可直接操控会议录音","Comfo Clip Q2搭载海思谛听音频芯片并适配开源鸿蒙","OWS耳夹式AI耳机为2026年布局重点"],
 "why_important":"上市公司IR口径系统披露AI耳机产品矩阵与端侧大模型落地路径，反映传统声学厂商正以双大模型+触控屏交互重塑耳机产品定义。",
 "relevance":"端侧音频AI+耳穿戴是8类终端中AI落地最快的品类之一；对AI耳机自研vs外采大模型、录音转写场景定义有直接参考价值。",
 "vendor":"漫步者/Lolli5 ANC、Comfo Clip Ultra、NeoBuds Pro 5","url":"https://www.cnfin.com/announ/detail/index.html?dannoun=lcdetail&id=846540276239",
 "source_name":"新华财经","source_detail":"新华财经 2026-10-28 漫步者(002351.SZ)投资者关系活动记录表（编号PR2026102801）",
 "note":"上市公司官方披露口径；Comfo Clip Q2（海思谛听+鸿蒙）曾于09-15期覆盖，本条聚焦双大模型落地与新品矩阵"
},
{
 "region":"cn","category":"笔记本电脑","title":"华硕灵耀14 2026双11行情：第三代酷睿Ultra 5（Intel 18A）+47 TOPS NPU下探6千元档",
 "status":"已上市","date":"2026-10-26","main_dim":"AI/NPU","dims":"AI/NPU|SoC/芯片|电池/快充",
 "grade":"C","stars":3,"signal_type":"双11行情/选购","corroboration":2,
 "key_params":"第三代英特尔酷睿Ultra 5（Intel 18A制程，睿频4.5GHz，Xe3核显），NPU算力47 TOPS；整机约1.2kg/13.9mm，70Wh电池最高29.6小时续航；双11 Plus国补到手6374.2元起",
 "tech_features":["Intel 18A制程第三代酷睿Ultra正式进入主流轻薄本","47 TOPS NPU支持断网可用端云一体AI功能（小硕知道）","70Wh+1.2kg轻薄长续航组合","陶瓷铝A面工艺下放6千元档"],
 "why_important":"Intel 18A新制程芯片以6千元档价位规模铺货，标志先进制程AI PC从旗舰下探主流市场；内存涨价周期中的逆势定价策略值得关注。",
 "relevance":"为AI PC NPU算力基准（45-50 TOPS）与轻薄本电池/重量配比提供竞品参照；18A供应节奏影响2027年笔记本SoC选型。",
 "vendor":"华硕/灵耀14 2026","url":"https://zhikeji.pconline.com.cn/article/1669913",
 "source_name":"太平洋知科技","source_detail":"太平洋知科技 2026-10-26 双11选购稿；什么值得买社区价格分析稿互相印证（灵耀14 2026骁龙版国补5779元）",
 "note":"选购推广性质稿件，规格与第三方社区稿可交叉印证；同级对比中骁龙X2 Elite版促销价7649元"
},
{
 "region":"cn","category":"无线充","title":"安克 MagGo 2 Pro 美国开售：25W Qi2.2+SnapCool主动散热，首款SGS A+双认证无线充移动电源",
 "status":"已上市","date":"2026-10-23","main_dim":"电池/快充","dims":"电池/快充|散热|认证/合规",
 "grade":"A","stars":4,"signal_type":"开售/认证信号","corroboration":2,
 "key_params":"10,000mAh；Qi2.2 25W磁吸无线充（iPhone 17 Pro 25分钟充至50%，对标20W有线充电曲线）；SnapCool智能风扇+双风道+三层石墨烯，充电全程背面<36°C（低于48°C标准限值12°C）；45W USB-C回充52分钟至80%；$109.99",
 "tech_features":["全球首款获SGS Premium Performance Mark A+评级（超快充+散热双项）的无线移动电源","低阻电芯+实时温度监测保障25W满速不掉档","智能显示屏实时显示功率/温度/电池健康","0-80°折叠支架，自动识别iPhone 17/18系列适配功率"],
 "why_important":"主动散热成为25W Qi2.2无线充的标配竞争维度，SGS A+双认证树立第三方温控标杆，预示磁吸配件进入散热军备竞赛。",
 "relevance":"Qi2.2 25W+温控方案直接影响手机配件生态与整机无线充电规格定义；散热架构（风扇+石墨烯）可平移至平板/桌搭场景。",
 "vendor":"安克/MagGo 2 Pro","url":"https://www.anker.com/blogs/power-banks/best-iphone-18-pro-magnetic-power-bank",
 "source_name":"Anker官网","source_detail":"Anker官方博客（发货周期9/28-10/18）；Forbes 2026-10-23 报道其SGS A+双认证与美国开售",
 "note":"IFA 2026首发获五项Best of IFA；本系列09-23期曾覆盖MagGo 2.0，本条为其正式开售+SGS认证进展"
}
]

INTL_PATCH = {
 "Suunto Race 3S": {"url":"https://us.suunto.com/blogs/news/suunto-launches-race-3s-next-generation-performance-watch",
   "grade":"A","source_name":"Suunto官网","stars":4,
   "source_detail":"Suunto官方博客 2026-10-15 发布稿；官方产品页印证硅碳电池与64GB规格","date":"2026-10-15"},
 "Acer Iconia": {"url":"https://www.91mobiles.com/hub/acer-iconia-tab-11-tab-12-launched-india/",
   "grade":"B","source_name":"91mobiles","stars":3,
   "source_detail":"91mobiles 2026-10-12 发布报道；pc-tablet/TechVorm 多源印证",
   "key_params":"Iconia Tab 12 5G：12.2英寸IPS 2400×1600 90Hz全贴合，联发科MT8755（2×A76 2.4GHz+6×A55），8GB+128/256GB，10000mAh 18W，16MP主摄+2MP微距；Tab 11 5G：10.95英寸450尼特90Hz，₹23,990/₹26,990起，支持键盘盖+手写笔"},
 "OPPO Enco X4": {"url":"https://www.frandroid.com/marques/3294707_oppo-lance-les-enco-x4-ses-premiers-ecouteurs-en-qualite-sans-perte",
   "grade":"B","source_name":"Frandroid","stars":4,
   "source_detail":"Frandroid 2026-10-27 报道（随Find X10全球发布登陆欧洲，€219）；TechNewsReel 印证6nm NPU规格","date":"2026-10-21"},
 "Pimax Crystal": {"grade":"B","stars":4,
   "key_params":"$1,399；60GHz无线为选配60G AirLink套件（另售$599），标配Wi-Fi 6E；Steam Frame同场对比发布",
   "note":"60G AirLink为选配件，正文需区分标配与选配；Steam Frame（09-15期已覆盖）为同期参照产品"},
 "Pico Space Pro": {"grade":"B","stars":3,
   "source_detail":"UploadVR 2026-10-11 报道日本认证档案曝光；认证信息属爆料口径，规格待官宣印证"},
 "Lenovo Tab Plus Gen 2": {"grade":"C","stars":3,
   "source_detail":"TechBeat PH 2026-10-26 报道菲律宾上市 PHP25,995；区域媒体单一信源"},
 "HP ProBook": {"key_params":"14英寸3K OLED，Intel Wildcat Lake Core 5/7，NPU 17 TOPS，商务本AI PC定位",
   "note":"CNET原文提及Wildcat Lake但未明写18A制程；正文含OmniBook 5内容已备注"}
}

DATA = []
for fn in ["_agent_cn_2026-11-04.json", "_agent_intl_2026-11-04.json"]:
    with open(BASE + fn, encoding="utf-8") as f:
        DATA.extend(json.load(f))

# ---- 主代理复核修补：CN 剔除 4 条旧闻/死链，替换为新采集 4 条 ----
CN_REMOVE_KEYS = ["MatePad Pro Max", "WATCH GT 7", "MateBook 14", "MagFlow"]
before = len(DATA)
DATA = [d for d in DATA if not any(k in d.get("title","") for k in CN_REMOVE_KEYS)]
removed = before - len(DATA)
assert removed == 4, "removed=%d" % removed
DATA.extend(CN_NEW)

# ---- INTL 修补 ----
def patch(d):
    for k, p in INTL_PATCH.items():
        if k in d.get("title",""):
            for f, v in p.items():
                d[f] = v
    return d
DATA = [patch(d) for d in DATA]

# region 归一化（Agent 可能写「国内/国际」）
def norm_region(r):
    r = (r or "").strip().lower()
    if r in ("国内", "cn", "china"):
        return "cn"
    if r in ("国际", "intl", "international", "global"):
        return "intl"
    return r
for d in DATA:
    d["region"] = norm_region(d.get("region", ""))

assert len(DATA) == 30, "count=%d" % len(DATA)

for d in DATA:
    for k, v in list(d.items()):
        d[k] = clean(v)
    d["status"] = norm_status(d.get("status",""), d.get("date",""))
    d["stars"] = cap_stars(d["grade"], d["stars"])

dim_count = {dm: 0 for dm in DIMS}
for d in DATA:
    for p in [p.strip() for p in d["dims"].split("|")]:
        if p in dim_count:
            dim_count[p] += 1
covered = sum(1 for dm in DIMS if dim_count[dm] > 0)
grade_count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for d in DATA:
    grade_count[d["grade"]] += 1
five_star = sum(1 for d in DATA if d["stars"] == 5)
cn_n = sum(1 for d in DATA if d["region"]=="cn")
intl_n = sum(1 for d in DATA if d["region"]=="intl")

def sort_key(d):
    return (STATUS_RANK.get(d["status"], 9), -skey(d["date"]))
cn = sorted([d for d in DATA if d["region"]=="cn"], key=sort_key)
intl = sorted([d for d in DATA if d["region"]=="intl"], key=sort_key)
ordered = cn + intl

def top_sort(d):
    gr = {"A":0,"B":1,"C":2,"D":3,"E":4}[d["grade"]]
    return (-d["stars"], gr, STATUS_RANK.get(d["status"],9), -skey(d["date"]))
top5 = sorted(DATA, key=top_sort)[:5]

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
        "tf": tf, "why": d["why_important"], "rel": d["relevance"], "vendor": d["vendor"],
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
print("covered dims:", covered, "/16  missing:", [dm for dm in DIMS if dim_count[dm]==0])
print("A/B/C/D/E:", grade_count)
print("five_star:", five_star)
print("cn:", cn_n, "intl:", intl_n)
print("top5:", [d["title"][:24] for d in top5])
from collections import Counter
print("cn cats:", Counter(d["category"] for d in cn))
print("intl cats:", Counter(d["category"] for d in intl))
