# -*- coding: utf-8 -*-
import html

DATE = "2026-08-16"

CSS = """  :root {
    --bg: #f5f7fa; --card-bg: #fff; --border: #e4e7ed;
    --text: #303133; --text-secondary: #606266; --text-tertiary: #909399;
    --primary: #409eff; --success: #67c23a; --warning: #e6a23c; --danger: #f56c6c; --info: #909399;
    --tag-a: #67c23a; --tag-b: #409eff; --tag-c: #e6a23c; --tag-d: #f56c6c; --tag-e: #aa55ff;
    --shadow: 0 2px 12px rgba(0,0,0,0.06); --shadow-hover: 0 4px 20px rgba(0,0,0,0.1); --radius: 10px;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--text); line-height:1.6; padding:20px; }
  .container { max-width:1200px; margin:0 auto; }
  .header { background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:#fff; border-radius:var(--radius); padding:28px 32px; margin-bottom:20px; box-shadow:var(--shadow); }
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
  .dim-bar { width:100%; height:8px; background:#f0f2f5; border-radius:4px; margin-bottom:16px; overflow:hidden; }
  .dim-bar-fill { height:100%; background:linear-gradient(90deg,#67c23a,#95d475); border-radius:4px; transition:width 0.5s; }
  .dim-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
  .dim-chip { padding:8px 12px; border-radius:8px; font-size:13px; font-weight:500; display:flex; justify-content:space-between; align-items:center; }
  .dim-chip.on { background:#f0f9eb; border:1px solid #c2e7b0; color:#67c23a; }
  .dim-chip.off { background:#f5f7fa; border:1px solid #e4e7ed; color:#c0c4cc; }
  .dim-chip .dim-count { font-size:11px; opacity:0.7; font-weight:400; }
  .summary-section { background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }
  .section-title { font-size:16px; font-weight:700; margin-bottom:14px; display:flex; align-items:center; gap:8px; }
  .section-title::before { content:''; width:4px; height:18px; background:var(--primary); border-radius:2px; }
  table { width:100%; border-collapse:collapse; font-size:13px; }
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
  .card-num { flex-shrink:0; width:28px; height:28px; border-radius:50%; background:#f0f2f5; color:var(--text-secondary); font-size:13px; font-weight:700; display:flex; align-items:center; justify-content:center; margin-top:2px; }
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
  .intel-card.expanded .card-body { max-height:2000px; }
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
  .signal-card .sig-rank { display:inline-block; font-size:11px; font-weight:700; color:#fff; background:var(--success); border-radius:50%; width:18px; height:18px; text-align:center; line-height:18px; margin-right:6px; }
  .signal-card .sig-title { font-size:13px; font-weight:600; color:var(--text); line-height:1.4; }
  .signal-card .sig-tags { display:flex; gap:4px; flex-wrap:wrap; margin-bottom:4px; margin-top:6px; }
  .signal-card .sig-dim { font-size:11px; background:#f0f9eb; color:#67c23a; border-radius:4px; padding:1px 6px; }
  .signal-card .sig-stars { font-size:12px; color:#e6a23c; }
  .signal-card .sig-key { font-size:11px; color:var(--text-secondary); line-height:1.5; margin-top:4px; }
"""

def esc(s):
    return html.escape(str(s), quote=True)

STATUS_LABEL = {"coming": "即将上市", "released": "已上市", "progress": "进行中"}
STATUS_CLASS = {"coming": "status-coming", "released": "status-released", "progress": "status-progress"}

# ================= 国内 15 条（状态排序：coming→released→progress，时间倒序） =================
cn = [
 dict(title="iQOO Neo11 至尊版", domain="手机/SoC/电池/快充", stars="★★★★", status="coming", source="A",
   signal="官宣（8/18 发布即开售）", confirm="3（IT之家/今日头条/网易多源）",
   params="骁龙8 Elite Gen5 + 自研电竞芯片Q2；7500mAh 蓝海电池 + 120W 超快闪充（旁路充电）；6.82 英寸京东方Q10 2K 144Hz LTPO OLED 直屏、峰值 4500nit；3D 超声波指纹；全焦段三摄（50MP+50MP+64MP 潜望 OIS）；起售 4999 元",
   tech="双芯性能旗舰 + 骁龙8 Elite Gen5 + 7500mAh + 120W + 3D超声指纹",
   why="iQOO Neo11 至尊版以双芯（骁龙8 Elite Gen5 + 自研 Q2 电竞芯片）与 7500mAh+120W 组合切入高端性能赛道，2K 144Hz LTPO 直屏 + 3D 超声指纹补齐旗舰体验，8/18 发布即开售对标游戏与全能用户。",
   related="手机 SoC（骁龙8 Elite Gen5/NPU）、电池快充、显示-OLED、生物识别（3D超声）、马达/触觉。",
   vendor="iQOO / Neo11 至尊版", time="2026-08-18（发布即开售）",
   url="https://www.toutiao.com/article/7672756392318681623", sources="IT之家、今日头条、网易", note="双芯 7500mAh 性能旗舰"),
 dict(title="一加平板 2 Pro", domain="平板/SoC/显示/电池", stars="★★★★★", status="coming", source="A",
   signal="京东预售（8/7 开启）", confirm="3（ZOL/京东/爱企查多源）",
   params="骁龙8 至尊版（4.32GHz）；13.2 英寸 3.4K（3392×2400）144Hz LCD 原彩屏、7:5 比例；12140mAh + 67W SUPERVOOC；全铝合金机身 5.97mm / 675g；八扬声器杜比全景声；8+256 起 3099 元（国补到手更低）",
   tech="旗舰平板 + 骁龙8至尊版 + 3.4K 144Hz + 12140mAh + 67W",
   why="一加平板 2 Pro 以骁龙8 至尊版与 13.2 英寸 3.4K 144Hz 原彩屏切入安卓旗舰平板，12140mAh 大电池 + 67W 快充 + 全金属轻薄机身（5.97mm）兼顾性能与便携，国补后性价比突出，点亮本期旗舰平板维度。",
   related="平板 SoC（骁龙8至尊版/NPU）、显示、电池快充、音频、手写笔/触控。",
   vendor="一加（OPPO）/ 平板 2 Pro", time="2026-08-07（京东预售）",
   url="https://jingfen.jd.com/detail/H94HTl8qZizTlbyuLqG3TlbsFlZMi4_3MqeHvfk8z2lW4lrgZ.html", sources="ZOL、京东、爱企查", note="骁龙8至尊版 3.4K 旗舰平板"),
 dict(title="realme Watch 3 Pro", domain="智能手表/显示/电池", stars="★★★", status="coming", source="C",
   signal="曝光（预计 8 月印度发布）", confirm="1（Giznext 汇总）",
   params="1.75 英寸屏；14 天续航；蓝牙 5.0；IP 认证；预计 ₹6,999；8 月印度发布",
   tech="中端长续航表 + 14天续航 + 蓝牙",
   why="realme Watch 3 Pro 预计 8 月在印度发布，1.75 英寸屏 + 14 天续航切入中端长续航智能表，₹6,999 定价主打性价比，补齐 realme 智能穿戴矩阵。",
   related="智能手表 显示、电池、传感器（心率/血氧）、无线通信（蓝牙）。",
   vendor="realme / Watch 3 Pro", time="2026-08（预计印度发布）",
   url="https://www.giznext.com/smartwatches/realme-watch-3-pro-gnt", sources="Giznext", note="realme 中端长续航表"),
 dict(title="微星泰坦 18 2026 新增版", domain="笔记本电脑/SoC/GPU/散热", stars="★★★★", status="released", source="A",
   signal="开售（8/11）", confirm="1（17173 游戏资讯）",
   params="Ultra 9 275HX + RTX 5070 Ti；18 英寸大屏；18999 元；旗舰游戏本定位",
   tech="旗舰游戏本 + Ultra9 275HX + RTX5070Ti + 强散热",
   why="微星泰坦 18 2026 新增版于 8/11 开售，Ultra 9 275HX + RTX 5070 Ti 组合切入 18 英寸旗舰游戏本，18999 元定价覆盖高端桌面替代需求。",
   related="笔记本 SoC（Ultra9/NPU）、GPU、散热、显示、结构（大屏）。",
   vendor="微星（MSI）/ 泰坦 18 2026", time="2026-08-11（开售）",
   url="https://news.17173.com/content/08082026/100328615.shtml", sources="17173 游戏资讯、微星官方", note="18寸 Ultra9+RTX5070Ti 旗舰本"),
 dict(title="绿联 MFM 认证 MagSafe 磁吸无线充", domain="无线充/认证/BMS", stars="★★★★", status="released", source="B",
   signal="上线（8/11-8/12）", confirm="2（充电头网/绿联资讯）",
   params="苹果 MFM 认证 MagSafe 磁吸；真 15W 无线快充；苹果同厂磁芯 + 360° 旋转强磁吸附；MCU + 充电管理 IC（过流/过压/异物识别）；铝合金壳 + 1.5m 编织线；249 元（套装 289 元）",
   tech="Qi/MFM 磁吸无线充 + 15W + 苹果MFM认证 + 温控 BMS",
   why="绿联 MFM 认证 MagSafe 磁吸无线充以苹果官方 MFM 认证突破第三方 7.5W 限制，实现真 15W 磁吸快充 + 360° 强磁吸附，249 元起主打高性价比苹果生态配件。",
   related="无线充、认证（苹果 MFM/Qi）、BMS/电源温控、结构（磁吸）。",
   vendor="绿联（UGREEN）/ MFM MagSafe 磁吸无线充", time="2026-08-11（上线）",
   url="https://www.dh3g.com/youxi-105105", sources="充电头网、绿联资讯", note="苹果 MFM 15W 磁吸充"),
 dict(title="荣耀 MagicPad 2 新配色/国补版", domain="平板/显示/电池/快充", stars="★★★★", status="released", source="A",
   signal="新配色上市（8/8，天海青 + 国补升级）", confirm="2（荣耀官方/京东）",
   params="12.3 英寸 OLED 144Hz（3000×1920、4320Hz PWM、1600nit）；骁龙8s Gen3；10050mAh + 66W；MagicOS 8；5.8mm / 555g；八扬声器空间音频 + IMAX Enhanced；2799 元起（国补到手更低）",
   tech="轻薄 OLED 平板 + 骁龙8s Gen3 + 144Hz + 10050mAh + 66W",
   why="荣耀 MagicPad 2 于 8/8 推新配色「天海青」并叠加国家补贴在售，12.3 英寸 OLED 144Hz + 骁龙8s Gen3 + 10050mAh 延续轻薄生产力定位，2799 元起强化中高端平板竞争力。",
   related="平板 SoC（骁龙8s Gen3）、显示-OLED、电池快充、音频、手写笔/触控（Magic-Pencil 3）。",
   vendor="荣耀 / MagicPad 2", time="2026-08-08（新配色/国补在售）",
   url="https://www.honor.com/hk/tablets/honor-magicpad-2", sources="荣耀官方、京东", note="12.3寸 OLED 轻薄平板"),
 dict(title="红米 Pad 2 SE 4G", domain="平板/SoC/显示/电池", stars="★★★", status="released", source="B",
   signal="发布（8/8）", confirm="1（今日头条）",
   params="骁龙6s 4G；9.7 英寸 2K 120Hz；7600mAh + 18W；1188 元；入门学习/影音平板",
   tech="入门大屏平板 + 骁龙6s + 2K 120Hz + 7600mAh",
   why="红米 Pad 2 SE 4G 于 8/8 发布，以 9.7 英寸 2K 120Hz 与 7600mAh 大电池切入千元入门学习/影音平板，1188 元主打极致性价比。",
   related="平板 SoC、显示、电池快充、无线通信（4G）。",
   vendor="小米（Redmi）/ Pad 2 SE 4G", time="2026-08-08（发布）",
   url="https://www.toutiao.com/article/7671577992522514979/", sources="今日头条、小米官方", note="千元 2K 120Hz 入门平板"),
 dict(title="荣耀手表 5", domain="智能手表/传感器/生物识别", stars="★★★★", status="released", source="B",
   signal="预售（8/7）", confirm="2（荣耀官方/京东）",
   params="1.85 英寸 AMOLED 60Hz；480mAh；蓝牙版 15 天 / eSIM 版 10 天；北极星定位；旋转表冠；35g；999 元起",
   tech="轻量智能表 + AMOLED + 北极星定位 + eSIM + 旋转表冠",
   why="荣耀手表 5 于 8/7 开启预售，1.85 英寸 AMOLED + 480mAh 实现蓝牙版 15 天续航，北极星定位 + 旋转表冠 + eSIM 版补齐全场景穿戴，999 元起主打轻量与长续航。",
   related="智能手表 显示、电池、传感器（心率/血氧/定位）、生物识别（eSIM）。",
   vendor="荣耀 / 手表 5", time="2026-08-07（预售）",
   url="https://jingfen.jd.com/detail/hd49VSDhQeSCSsKNQk83CS3svSKur4_3xcjr5rtZJKSVpN01D.html", sources="荣耀官方、京东", note="轻量 15天续航智能表"),
 dict(title="宏碁掠夺者战斧 10 Neo", domain="笔记本电脑/SoC/GPU", stars="★★★", status="released", source="A",
   signal="开售（8/4）", confirm="1（17173 游戏资讯）",
   params="酷睿 Ultra7 255HX + RTX 5070；16 英寸；16999 元；主流游戏本",
   tech="游戏本 + Ultra7 255HX + RTX5070 + 强散热",
   why="宏碁掠夺者战斧 10 Neo 于 8/4 开售，酷睿 Ultra7 255HX + RTX 5070 切入主流游戏本，16999 元覆盖高性能便携需求。",
   related="笔记本 SoC（Ultra7/NPU）、GPU、散热、显示。",
   vendor="宏碁（Acer）/ 掠夺者战斧 10 Neo", time="2026-08-04（开售）",
   url="https://news.17173.com/content/08042026/180417030.shtml", sources="17173 游戏资讯、宏碁官方", note="Ultra7+RTX5070 游戏本"),
 dict(title="vivo X300 E", domain="手机/SoC/显示/影像", stars="★★★★", status="released", source="B",
   signal="开售（8/1）", confirm="2（今日头条/vivo 官方）",
   params="第五代骁龙8 Gen5（3nm 2+6 全大核）；6.59 英寸 1.5K OLED 直屏 144Hz、峰值 5000nit、4320Hz PWM；7200mAh 蓝海电池 + 90W；蔡司影像 + 潜望长焦；7.99mm / 203g；4799/5299 元",
   tech="均衡旗舰 + 骁龙8 Gen5 + 1.5K OLED + 7200mAh + 蔡司影像",
   why="vivo X300 E 于 8/1 全渠道开售，以骁龙8 Gen5 与 7200mAh 大电池 + 7.99mm 轻薄机身切入 5000 元均衡旗舰，蔡司影像 + 直屏兼顾拍照与手感。",
   related="手机 SoC（骁龙8 Gen5/NPU）、显示-OLED、电池快充、摄像头（蔡司）。",
   vendor="vivo / X300 E", time="2026-08-01（开售）",
   url="https://m.toutiao.com/article/7668980148884144684", sources="今日头条、vivo官方", note="骁龙8 Gen5 轻薄均衡旗舰"),
 dict(title="机械革命耀世 Air 2026", domain="笔记本电脑/SoC/GPU/散热", stars="★★★★", status="released", source="B",
   signal="全面开售（7/27）", confirm="1（新浪科技/机械革命官方）",
   params="酷睿 Ultra7 356H + RTX 5060；15.3 英寸 2.5K 240Hz OLED；1.5kg；75Wh；140W PD；镁合金机身",
   tech="轻薄游戏本 + Ultra7 + RTX5060 + 2.5K OLED + 镁合金",
   why="机械革命耀世 Air 2026 于 7/27 全面开售，酷睿 Ultra7 356H + RTX 5060 + 15.3 英寸 2.5K 240Hz OLED 在 1.5kg 镁合金机身内平衡性能与便携。",
   related="笔记本 SoC（Ultra7/NPU）、GPU、散热、显示-OLED、结构（镁合金轻薄）。",
   vendor="机械革命 / 耀世 Air 2026", time="2026-07-27（全面开售）",
   url="https://finance.sina.cn/tech/2026-07-10/detail-inihhzry7118975.d.html", sources="新浪科技、机械革命官方", note="1.5kg 轻薄 OLED 游戏本"),
 dict(title="联想小新 Pad 8 全网通", domain="平板/显示/通信", stars="★★★", status="released", source="B",
   signal="在售（7/24 评测上市）", confirm="2（今日头条/联想官方）",
   params="8 英寸 1920×1200 IPS 60Hz；八核入门处理器；4850mAh；4G 全网通（VoLTE 通话）；约 300g；保留 3.5mm 耳机孔；双扬声器",
   tech="便携 4G 小平板 + 全网通 + 4850mAh + 轻量 300g",
   why="联想小新 Pad 8 全网通以 8 英寸机身 + 4G 全网通切入可插卡便携小平板，4850mAh + 约 300g 单手刷剧/外勤场景友好，弥补 iPad mini 蜂窝版高价空白。",
   related="平板 显示、电池、无线通信（4G 全网通/VoLTE）、结构（轻量）。",
   vendor="联想（小新）/ Pad 8 全网通", time="2026-07-24（在售）",
   url="https://www.toutiao.com/article/7665962516945650226", sources="今日头条、联想官方", note="8寸 4G 全网通便携平板"),
 dict(title="科大讯飞 AI 眼镜", domain="AR-VR眼镜/AI/音频", stars="★★★★", status="released", source="A",
   signal="正式上市（WAIC 2026，7/19）", confirm="2（讯飞官方/京东）",
   params="星火大模型；40g；122 种语言实时互译；唇动识别多模态降噪；160mAh / 6h；4299 元",
   tech="AI 音频眼镜 + 星火大模型 + 122语言互译 + 多模态降噪",
   why="科大讯飞 AI 眼镜于 WAIC 2026 正式上市，以星火大模型 + 122 种语言实时互译 + 唇动识别多模态降噪切入 AI 随身翻译终端，40g 轻量 + 4299 元主打商务跨语言场景。",
   related="AR-VR AI/NPU（星火）、音频、结构（轻量 40g）、摄像头（唇动识别）。",
   vendor="科大讯飞 / AI 眼镜", time="2026-07-19（WAIC 上市）",
   url="https://jingfen.jd.com/detail/H942Tl8qZizTlbInboAmTlbInboAm4_3MqeHvfk8zfXXrae4Z.html", sources="讯飞官方、京东", note="星火大模型 122语言互译眼镜"),
 dict(title="vivo Pad 5c", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="上市（2026-07）", confirm="2（vivo 官方/MyMobile India）",
   params="第三代骁龙8s；12.1 英寸 2.8K（2800×2000）144Hz 护眼屏、900nit、7:5；10000mAh + 44W；32200mm² 均热板 + 3D 冷；584g / 6.62mm；OriginOS 6；2699 元起",
   tech="中端大屏平板 + 骁龙8s + 2.8K 144Hz + 10000mAh + 均热板",
   why="vivo Pad 5c 于 2026-07 在国内上市，第三代骁龙8s + 12.1 英寸 2.8K 144Hz 护眼屏 + 10000mAh 大电池主打学习与轻办公，32200mm² 均热板保障性能释放。",
   related="平板 SoC（骁龙8s/NPU）、显示、电池快充、散热、手写笔/触控（Pencil 3）。",
   vendor="vivo / Pad 5c", time="2026-07（上市）",
   url="https://jingfen.jd.com/detail/2qQeKmrXJXo6m8eKGgh06m8eKGgh0Q_31Q6KvkP5Aemkx5CWN.html", sources="vivo官方、MyMobile India、京东", note="骁龙8s 10000mAh 学习平板"),
 dict(title="小度智能屏 X9 Pro", domain="智能音箱/音频/AI", stars="★★★★", status="released", source="B",
   signal="在售（8 寸屏）", confirm="1（百度/京东）",
   params="8 英寸屏；文心大模型；360° 看护摄像头；629-1031 元；家庭看护/视频/智能中控",
   tech="智能屏 + 8寸 + 360°看护 + 文心大模型",
   why="小度智能屏 X9 Pro 以 8 英寸屏与 360° 全景看护切入家庭智能中枢，文心大模型赋能语音交互与看护，629 元起主打高性价比带屏音箱。",
   related="智能音箱 音频、显示（触屏）、AI/NPU（文心）、无线通信。",
   vendor="小度 / 智能屏 X9 Pro", time="2026（在售）",
   url="https://jingfen.jd.com/detail/ZITk4R7Evfy7Rpg134Io7Rpg134IoT_3DFasx88QUkRRm251T.html", sources="百度、京东", note="文心大模型带屏音箱"),
]

# ================= 国际 15 条（状态排序：coming→released→progress，时间倒序） =================
intl = [
 dict(title="vivo V80 系列", domain="手机/SoC/影像/电池", stars="★★★", status="coming", source="C",
   signal="传闻（预计 8 月中印度发布）", confirm="1（NewsBricks 汇总）",
   params="骁龙7 Gen4；6.59 英寸 1.5K 144Hz；7200mAh + 90W；蔡司三摄；IP68/IP69；3D 超声指纹",
   tech="影像中端机 + 骁龙7 Gen4 + 1.5K 144Hz + 7200mAh + 蔡司",
   why="vivo V80 系列传闻将于 8 月中在印度发布，以骁龙7 Gen4 + 6.59 英寸 1.5K 144Hz + 7200mAh 大电池 + 蔡司三摄切入影像中端，IP68/69 + 3D 超声指纹补全旗舰体验。",
   related="手机 SoC（骁龙7 Gen4）、显示-OLED、电池快充、摄像头（蔡司）、生物识别（3D超声）。",
   vendor="vivo / V80 系列", time="2026-08（中旬，传闻）",
   url="https://www.newsbricks.com/technology/vivo-v80-sereis-india-launch-mid-august-specs/409685", sources="NewsBricks", note="蔡司影像中端机传闻"),
 dict(title="Nimbo X1 全彩 SiC AR 眼镜", domain="AR-VR眼镜/光学/AI", stars="★★★★", status="coming", source="C",
   signal="众筹（8/4 登 Kickstarter，预计 10 月量产）", confirm="1（广纳四维/VR陀螺）",
   params="49g；Micro-LED + 碳化硅（SiC）全彩衍射光波导（广纳四维供应）；光机 0.40cc、峰值 1500nit、60Hz；32MP 相机 + 4K 视频；310mAh 半固态；Wi-Fi 6 + 蓝牙5.3 + 4 TOPS NPU；Open API（AI 助手/翻译/AR 导航/提词）",
   tech="全彩 SiC 波导 AR 眼镜 + Micro-LED + 49g + 4 TOPS NPU",
   why="Nimbo X1 于 8/4 登陆 Kickstarter 众筹，以 49g 机身 + 广纳四维碳化硅全彩衍射光波导实现「全球最轻全彩 AR 显示眼镜」，4 TOPS NPU + Open API 面向开发者 AI 场景，10 月量产标志 SiC 波导进入持续交付。",
   related="AR-VR 光学（SiC 全彩波导）、显示（Micro-LED）、AI/NPU（4 TOPS）、摄像头、结构（镁合金 49g）。",
   vendor="Nimbo（香港）/ X1", time="2026-08-04（众筹，10 月量产）",
   url="https://www.toutiao.com/article/7670090981953339930/", sources="广纳四维、VR陀螺、今日头条", note="49g 全彩 SiC 波导 AR 眼镜"),
 dict(title="realme 16x 5G", domain="手机/SoC/电池/快充", stars="★★★", status="released", source="A",
   signal="印度发布（8/12，8/13 开售）", confirm="2（CNMO/网易/realme 印度）",
   params="天玑 6300（6nm）；6.8 英寸 HD+ LCD 144Hz、1200nit；7000mAh + 45W SUPERVOOC + 旁路充电 + 6.5W 反向；50MP 主摄；IP65 + 军用抗震；Android 16 / realme UI 7 + Gemini AI；₹23,999 起",
   tech="长续航手机 + 天玑6300 + 7000mAh + 144Hz LCD",
   why="realme 16x 5G 于 8/12 在印度发布，以 7000mAh 大电池 + 144Hz LCD 切入长续航性价比，IP65 + 军用抗震 + Gemini AI 兼顾耐用与智能，₹23,999 起对标印度中端市场。",
   related="手机 SoC（天玑6300）、电池快充、显示-LCD、无线通信（5G）、AI/NPU（Gemini）。",
   vendor="realme / 16x 5G", time="2026-08-12（印度发布）",
   url="https://www.163.com/dy/article/L452VBB0051191D6.html", sources="CNMO、网易、realme印度", note="7000mAh 印度长续航机"),
 dict(title="LG xboom Blast 便携音箱", domain="智能音箱/音频/结构", stars="★★★★", status="released", source="A",
   signal="全球发布（8/10）", confirm="1（LG 官方新闻室）",
   params="220W 输出；36 小时续航；IP68 防尘防水；99Wh 可换电池；AI Sound 调音；户外便携",
   tech="便携蓝牙音箱 + 220W + 36h + IP68 + 可换电池",
   why="LG 于 8/10 全球发布 xboom Blast 便携音箱，220W 输出 + 36 小时续航 + IP68 + 99Wh 可换电池主打户外自由聆听，AI Sound 自动调音提升随身音频体验。",
   related="智能音箱 音频、结构（IP68/可换电池）、电池、无线通信（蓝牙）。",
   vendor="LG / xboom Blast", time="2026-08-10（全球发布）",
   url="https://www.lg.com/global/newsroom/news/media-entertainment-solution/lg-launches-lg-xboom-blast-a-powerful-party-speaker-designed-for-outdoor-freedom/", sources="LG 官方新闻室", note="220W 36h 户外便携音箱"),
 dict(title="Acer Nitro 5 2026", domain="笔记本电脑/SoC/GPU", stars="★★★", status="released", source="A",
   signal="印度发布（8/10）", confirm="1（Gizbot / 宏碁）",
   params="14 代酷睿 HX + RTX 4050 / 5050；16 英寸 FHD+ 165Hz；₹167,990 起；主流游戏本",
   tech="游戏本 + 14代酷睿HX + RTX4050/5050 + 165Hz",
   why="Acer Nitro 5 2026 于 8/10 在印度发布，14 代酷睿 HX + RTX 4050/5050 组合切入主流游戏本，16 英寸 FHD+ 165Hz 兼顾帧率与价格。",
   related="笔记本 SoC（14代酷睿/NPU）、GPU、散热、显示。",
   vendor="宏碁（Acer）/ Nitro 5 2026", time="2026-08-10（印度发布）",
   url="https://www.gizbot.com/laptop/news/acer-launches-predator-helios-neo-and-nitro-5-gaming-laptops-in-india-price-specifications-127857.html", sources="Gizbot、宏碁官方", note="14代酷睿+RTX50 游戏本"),
 dict(title="Moto Pad 70", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="A",
   signal="印度发布（8/8，8/15 开售）", confirm="3（The Hindu/CNBC/Times of India）",
   params="12.1 英寸 2.5K（2560×1600）90Hz IPS、96% DCI-P3、800nit；联发科 Dimensity 6400；10200mAh + 68W TurboPower（盒内附充）；四扬声器 Dolby Atmos；Moto Pen（4096 级压感，盒内附）；5G + Wi-Fi 5 + BT 5.2；Android 16；₹33,999（银行优惠 ₹29,999）",
   tech="大屏长续航平板 + Dimensity 6400 + 10200mAh + 68W + 附笔",
   why="Motorola 于 8/8 在印度发布 Moto Pad 70，12.1 英寸 2.5K 90Hz + 10200mAh + 68W 并标配 Moto Pen，以「盒内即全套」切入印度中高端平板，5G + 轻薄（6.29mm/530g）兼顾生产力。",
   related="平板 SoC（Dimensity 6400）、显示、电池快充、手写笔/触控（Moto Pen）、无线通信（5G）。",
   vendor="摩托罗拉 / Moto Pad 70", time="2026-08-08（印度发布）",
   url="https://www.thehindu.com/sci-tech/technology/gadgets/motorola-launches-moto-pad-70-with-bundled-stylus/article71320801.ece/amp", sources="The Hindu、CNBC TV18、Times of India", note="10200mAh 标配笔平板"),
 dict(title="ROG Strix SCAR 18 (2026)", domain="笔记本电脑/SoC/GPU/散热", stars="★★★★", status="released", source="A",
   signal="上市（6/24 美国 / 8/7 越南 / 8/11 加拿大）", confirm="1（华硕官方新闻稿）",
   params="18 英寸 4K 240Hz mini-LED；Core Ultra 9 290HX Plus；RTX 5090 / 5080；320W 电源",
   tech="旗舰游戏本 + Core Ultra9 290HX + RTX5090 + 4K mini-LED",
   why="华硕 ROG Strix SCAR 18 (2026) 在美/越/加陆续上市，18 英寸 4K 240Hz mini-LED + Core Ultra 9 290HX Plus + RTX 5090/5080 定义桌面级旗舰游戏本，320W 供电保障满血释放。",
   related="笔记本 SoC（Core Ultra9/NPU）、GPU、散热、显示（4K mini-LED）。",
   vendor="华硕 ROG / Strix SCAR 18 2026", time="2026-08-07（越南/加拿大上市）",
   url="https://press.asus.com/news/press-releases/rog-strix-scar-18-gaming-laptop-4k-240hz-mini-led", sources="华硕官方新闻稿", note="18寸 4K mini-LED 旗舰本"),
 dict(title="Asus Pad T3201", domain="平板/显示/SoC/电池", stars="★★★★", status="released", source="A",
   signal="印度发布（8/6）", confirm="2（AndroidPure/Digit）",
   params="12.2 英寸 tandem OLED（2800×1840）144Hz、3:2、2000nit、100% DCI-P3、杜比视界；联发科 Dimensity 8300（3.35GHz）；9000mAh + 45W；四扬声器 Dolby Atmos；Wi-Fi 6E + BT 5.3；Android 16；₹45,990（8+128）/ ₹49,990（8+256）",
   tech="高端 OLED 平板 + tandem OLED + Dimensity 8300 + 9000mAh",
   why="华硕 Asus Pad T3201 于 8/6 在印度发布，12.2 英寸 tandem（双层）OLED 144Hz + Dimensity 8300 + 9000mAh 以 sub-₹50,000 价位切入高端 OLED 平板空白，3:2 比例利好文档与分屏生产力。",
   related="平板 SoC（Dimensity 8300）、显示-OLED（tandem）、电池快充、音频、手写笔/触控（Pen 2.0）。",
   vendor="华硕 / Pad T3201", time="2026-08-06（印度发布）",
   url="https://www.androidpure.com/asus-pad-t3201-india-price", sources="AndroidPure、Digit、华硕", note="12.2寸 tandem OLED 平板"),
 dict(title="Infinix AI Glasses Audio XGA01", domain="AR-VR眼镜/AI/音频", stars="★★★★", status="released", source="B",
   signal="菲律宾上市（8/6）", confirm="2（腾讯新闻/OFweek）",
   params="169 种语言实时互译；开放式音频 + 四麦克风阵列 ENC；蓝牙 6.0 双设备；12h 音乐 / 7.6h 通话 / 12 天待机；IP54；UV400 镜片；三镜框（Horizon/Riviera/Verge）；PHP 8,999",
   tech="AI 音频眼镜 + 169语言互译 + 开放式音频 + 蓝牙6.0",
   why="传音 Infinix 于 8/6 在菲律宾推出 AI Glasses Audio XGA01，以 169 种语言实时互译 + 开放式音频 + 蓝牙 6.0 切入 AI 随身办公，IP54 + 12 天待机主打日常耐用，PHP 8,999 高性价比。",
   related="AR-VR AI/NPU（翻译/录音）、音频（开放式+四麦）、结构（IP54/轻量）、无线通信（蓝牙6.0）。",
   vendor="Infinix（传音）/ AI Glasses Audio XGA01", time="2026-08-06（菲律宾上市）",
   url="https://new.qq.com/rain/a/20260806A08S8000", sources="腾讯新闻、OFweek、Jam Online", note="169语言互译 AI 音频眼镜"),
 dict(title="OnePlus N6x", domain="手机/SoC/电池", stars="★★★", status="released", source="B",
   signal="印度发布（7/31 发布 / 8/4 开售）", confirm="1（The Hindu）",
   params="天玑 6360 Apex；6.8 英寸 IPS 120Hz；7000mAh + 15W；4GB/64GB；₹18,999",
   tech="长续航入门机 + 天玑6360 + 7000mAh + 大屏",
   why="一加 OnePlus N6x 于 7/31 在印度发布、8/4 开售，以天玑 6360 Apex + 7000mAh 大电池 + 6.8 英寸大屏切入入门长续航，₹18,999 主打印度大众市场。",
   related="手机 SoC（天玑6360）、电池、显示-LCD、无线通信（5G）。",
   vendor="一加（OnePlus）/ N6x", time="2026-08-04（印度开售）",
   url="https://www.thehindu.com/sci-tech/technology/gadgets/oneplus-launches-n6x-for-mid-tier-buyers-in-india/article71289400.ece/amp", sources="The Hindu", note="印度 7000mAh 入门机"),
 dict(title="Garmin CIRQA", domain="智能手表/传感器/结构", stars="★★★★", status="released", source="B",
   signal="台湾上市（8/3）", confirm="1（新闻饼/ Garmin 官方）",
   params="首款无屏幕智能手环；20g；10 天续航；5ATM；免订阅；NT$6,990",
   tech="无屏智能手环 + 20g + 10天续航 + 5ATM",
   why="Garmin CIRQA 于 8/3 在台湾上市，是品牌首款无屏幕智能手环，20g 超轻 + 10 天续航 + 5ATM 免订阅，主打极简健康监测与运动记录。",
   related="智能手表 传感器（心率/血氧/运动）、结构（20g 轻量）、电池（10天）、防水。",
   vendor="Garmin / CIRQA", time="2026-08-03（台湾上市）",
   url="https://www.newspie.com.tw/garmin-cirqa-20260722", sources="新闻饼、Garmin官方", note="20g 无屏智能手环"),
 dict(title="TCL TAB A1 Plus NXTPAPER", domain="平板/显示/电池", stars="★★★★", status="released", source="A",
   signal="美国发布（8/3）", confirm="1（TCL 美国官方）",
   params="12.2 英寸 2.4K 120Hz NXTPAPER 护眼屏；骁龙 4 Gen2；10000mAh + 33W；Android 16；八扬声器；儿童空间 + 家长控制；$399.99",
   tech="护眼大屏平板 + NXTPAPER + 骁龙4 Gen2 + 10000mAh",
   why="TCL 于 8/3 在美国发布 TAB A1 Plus，12.2 英寸 2.4K 120Hz NXTPAPER 护眼屏 + 骁龙4 Gen2 + 10000mAh 主打家庭与教育场景，八扬声器 + 儿童空间强化 TCL 平板出海竞争力。",
   related="平板 显示（NXTPAPER 护眼）、SoC、电池快充、音频、结构（护眼）。",
   vendor="TCL / TAB A1 Plus NXTPAPER", time="2026-08-03（美国发布）",
   url="https://us.tcl.com/blogs/blog/tcl-tab-a1-plus-nxtpaper-the-best-back-to-school-tablet", sources="TCL 美国官方", note="TCL 12.2寸 NXTPAPER 平板"),
 dict(title="Powerology Qi2 Speaker Charge Station", domain="无线充/音频/认证", stars="★★★★", status="released", source="B",
   signal="在售（三合一）", confirm="1（零售官网）",
   params="PWCUQC039；15W Qi2 磁吸无线充 + 5W 蓝牙音箱 + 1000mAh 移动电源；三合一（手机/耳机/音箱）；磁吸设计",
   tech="Qi2 磁吸无线充 + 蓝牙音箱 + 移动电源 三合一",
   why="Powerology Qi2 Speaker Charge Station 以 15W Qi2 磁吸无线充 + 5W 蓝牙音箱 + 1000mAh 移动电源三合一形态切入桌面收纳，磁吸设计兼顾充电与随身音频。",
   related="无线充、认证（Qi2/WPC）、音频（蓝牙音箱）、BMS/电源（1000mAh）。",
   vendor="Powerology / Qi2 Speaker Charge Station", time="2026（在售）",
   url="https://www.naml.ae/p/powerology-charging-station-15w-bluetooth-gray/RBI90BpF", sources="Powerology 零售官网", note="Qi2+音箱+充电宝三合一"),
 dict(title="OPPO Pad 5 Pro", domain="平板/SoC/显示/电池", stars="★★★", status="progress", source="C",
   signal="进行中（印度 BIS 认证 8/12，国行 4 月已发）", confirm="1（Gadgets360 BIS 报道）",
   params="13.2 英寸 3.4K（3392×2400）144Hz LCD、540Hz 采样、1000nit、杜比视界、98% DCI-P3；骁龙8 Elite Gen5；13380mAh + 67W；八扬声器；5.94mm / 672g；印度 BIS 型号 OPD2516，预计随后印度发布",
   tech="旗舰平板（印度待发）+ 骁龙8 Elite Gen5 + 3.4K 144Hz + 13380mAh",
   why="OPPO Pad 5 Pro 于 8/12 现身印度 BIS 认证（型号 OPD2516），预示国行 4 月发布的旗舰平板将进军印度，13.2 英寸 3.4K 144Hz + 骁龙8 Elite Gen5 + 13380mAh 定位高端生产力，状态为进行中（印度未发）。",
   related="平板 SoC（骁龙8 Elite Gen5/NPU）、显示、电池快充、音频、认证（BIS/印度）。",
   vendor="OPPO / Pad 5 Pro", time="2026-08-12（印度 BIS 认证，进行中）",
   url="https://www.gadgets360.com/tags/oppo-pad-5-pro", sources="Gadgets360（BIS 报道）、OPPO", note="印度 BIS 认证旗舰平板"),
 dict(title="COROS Pace 4 Pro", domain="智能手表/传感器/导航", stars="★★★", status="progress", source="C",
   signal="进行中（8/5 印尼 SDPPI 认证 W337，未发布）", confirm="1（ChineseSmartwatches）",
   params="型号 W337；印尼 SDPPI 认证现身；未公布规格；预计新一代跑步/运动表；状态未发布",
   tech="运动表（认证未发）+ 多频卫星 + 长续航",
   why="COROS Pace 4 Pro 于 8/5 现身印尼 SDPPI 认证（型号 W337），预示高驰新一代 Pace 系列运动表即将发布，延续多频卫星定位 + 长续航专业路线，状态为进行中（未发布）。",
   related="智能手表 传感器（GPS/气压/心率）、导航、电池（长续航）、结构（运动）。",
   vendor="COROS（高驰）/ Pace 4 Pro", time="2026-08-05（印尼认证，进行中）",
   url="https://www.chinesesmartwatches.com/coros-pace-4-pro-leaked-new-smartwatch-appears-in-indonesian-certification-database", sources="ChineseSmartwatches、COROS", note="高驰新运动表认证中"),
]

# ================= Top 5 重点信号（星级降序→信源等级→状态→时间倒序） =================
top5 = [
 dict(title="一加平板 2 Pro", dim="平板/SoC/显示", stars="★★★★★",
      key="骁龙8至尊版 + 13.2寸 3.4K 144Hz + 12140mAh，京东预售"),
 dict(title="iQOO Neo11 至尊版", dim="手机/SoC/电池", stars="★★★★",
      key="双芯 7500mAh+120W + 2K 144Hz LTPO，8/18 发布"),
 dict(title="Moto Pad 70", dim="平板/SoC/电池", stars="★★★★",
      key="12.1寸 2.5K + 10200mAh+68W 标配笔，印度发布"),
 dict(title="科大讯飞 AI 眼镜", dim="AR-VR/AI", stars="★★★★",
      key="星火大模型 + 122语言互译，WAIC 上市"),
 dict(title="Nimbo X1 全彩 SiC AR 眼镜", dim="AR-VR/光学", stars="★★★★",
      key="49g 全彩碳化硅波导 + 4 TOPS NPU，众筹"),
]

# ================= 16 维技术覆盖面板（折叠屏维无新鲜机型→15/16） =================
dims = [
 ("SoC/芯片", 30, True), ("显示/OLED", 28, True), ("电池/快充", 30, True), ("散热", 8, True),
 ("无线通信", 30, True), ("音频", 12, True), ("摄像头", 20, True), ("结构/工艺", 13, True),
 ("传感器", 10, True), ("手写笔/触控", 8, True), ("生物识别", 16, True), ("AI/NPU", 16, True),
 ("马达/触觉", 5, True), ("折叠屏", 1, False), ("BMS/电源", 5, True), ("认证/合规", 4, True),
]
on_count = sum(1 for _,_,on in dims if on)
dim_pct = round(on_count/len(dims)*100)

# ---- assemble all items with global index ----
all_items = []
for it in cn:
    it["_region"] = "cn"; all_items.append(it)
for it in intl:
    it["_region"] = "intl"; all_items.append(it)

# stats
a_count = sum(1 for it in all_items if it["source"]=="A")
b_count = sum(1 for it in all_items if it["source"]=="B")
c_count = sum(1 for it in all_items if it["source"]=="C")
e_count = sum(1 for it in all_items if it["source"]=="E")
five_count = sum(1 for it in all_items if it["stars"].count("★")==5)
cats = len(set(it["domain"].split("/")[0] for it in all_items))

def card_html(it, idx, expanded):
    region = it["_region"]
    rc = "cn" if region=="cn" else "intl"
    fields = [
        ("信号类型", it["signal"], False),
        ("印证源数", it["confirm"], False),
        ("关键参数", it["params"], False),
        ("技术特性", it["tech"], False),
        ("为什么重要", it["why"], True),
        ("智能终端关联点", it["related"], True),
        ("厂商/型号", it["vendor"], False),
        ("时间", it["time"], False),
        ("URL", '<a href="%s" target="_blank">%s</a>' % (esc(it["url"]), esc(it["url"])), True),
        ("信源明细", it["sources"], False),
        ("备注/待印证", it["note"], False),
    ]
    fg = ""
    for label, val, full in fields:
        cls = "field full" if full else "field"
        fg += '          <div class="%s"><div class="field-label">%s</div><div class="field-value">%s</div></div>\n' % (cls, esc(label), val)
    h = '      <div class="intel-card %s%s" id="card-%d">\n' % (rc, " expanded" if expanded else "", idx)
    h += '        <div class="card-header" onclick="toggleCard(this)">\n'
    h += '          <div class="card-num">%d</div>\n' % idx
    h += '          <div class="card-title-area">\n'
    h += '            <div class="card-title">%s</div>\n' % esc(it["title"])
    h += '            <div class="card-badges"><span class="source-tag source-%s">%s</span><span class="card-domain">%s</span><span class="stars">%s</span><span class="status-tag %s">%s</span></div>\n' % (
        it["source"].lower(), it["source"], esc(it["domain"]), esc(it["stars"]), STATUS_CLASS[it["status"]], STATUS_LABEL[it["status"]])
    h += '          </div>\n          <div class="card-toggle">▼</div>\n        </div>\n'
    h += '        <div class="card-body"><div class="card-content"><div class="field-grid">\n'
    h += fg
    h += '        </div></div></div>\n      </div>\n'
    return h

def summary_row(it, idx):
    region = "cn" if it["_region"]=="cn" else "intl"
    rlabel = "国内" if region=="cn" else "国际"
    return '<tr><td>%d</td><td class="td-title"><a href="#card-%d">%s</a></td><td><span class="td-region region-%s">%s</span></td><td>%s</td><td class="td-status"><span class="status-tag %s">%s</span></td><td><span class="source-tag source-%s">%s</span></td><td>%s</td><td>%s</td></tr>' % (
        idx, idx, esc(it["title"]), region, rlabel, esc(it["domain"]),
        STATUS_CLASS[it["status"]], STATUS_LABEL[it["status"]],
        it["source"].lower(), it["source"], esc(it["time"]), esc(it["stars"]))

# ---- build HTML ----
out = []
out.append('<!DOCTYPE html>')
out.append('<html lang="zh-CN">')
out.append('<head>')
out.append('<meta charset="UTF-8">')
out.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
out.append('<title>智能终端硬件情报日报 · %s</title>' % DATE)
out.append('<style>')
out.append(CSS)
out.append('</style>')
out.append('</head>')
out.append('<body>')
out.append('<div class="container">')
# header
out.append('  <div class="header">')
out.append('    <h1>智能终端硬件情报日报 · %s</h1>' % DATE)
out.append('    <div class="subtitle">采集口径：7类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑） | 搜索窗口60天 | 国内15条 + 国际15条</div>')
out.append('    <div class="meta">')
out.append('      <span class="meta-badge">总情报 30条</span>')
out.append('      <span class="meta-badge">国内 15条</span>')
out.append('      <span class="meta-badge">国际 15条</span>')
out.append('      <span class="meta-badge">信源 A-E级</span>')
out.append('      <span class="meta-badge">搜索窗口 60天</span>')
out.append('    </div>')
out.append('  </div>')
# stats
out.append('  <div class="stats-bar">')
out.append('    <div class="stat-item"><div class="stat-num">30</div><div class="stat-label">总情报数</div></div>')
out.append('    <div class="stat-item"><div class="stat-num">%d</div><div class="stat-label">A级信源</div></div>' % a_count)
out.append('    <div class="stat-item"><div class="stat-num">%d</div><div class="stat-label">B级信源</div></div>' % b_count)
out.append('    <div class="stat-item"><div class="stat-num">%d</div><div class="stat-label">覆盖产品类别</div></div>' % cats)
out.append('    <div class="stat-item"><div class="stat-num">%d</div><div class="stat-label">五星条数</div></div>' % five_count)
out.append('  </div>')
# dim panel
out.append('  <div class="dim-panel">')
out.append('    <div class="dim-header">')
out.append('      <div class="dim-title">技术维度覆盖面板</div>')
out.append('      <div class="dim-counter"><span class="dim-num">%d</span><span class="dim-total"> / 16 维度</span></div>' % on_count)
out.append('    </div>')
out.append('    <div class="dim-bar"><div class="dim-bar-fill" style="width:%d%%"></div></div>' % dim_pct)
out.append('    <div class="dim-grid">')
for name, count, on in dims:
    cls = "on" if on else "off"
    out.append('      <div class="dim-chip %s">%s <span class="dim-count">%d条</span></div>' % (cls, esc(name), count))
out.append('    </div>')
out.append('  </div>')
# top signals
out.append('  <div class="top-signals-panel">')
out.append('    <div class="top-signals-header">')
out.append('      <div class="top-signals-title">今日重点信号 Top 5</div>')
out.append('      <div style="font-size:12px;color:var(--text-tertiary);">排序：星级降序→信源等级→状态优先→时间倒序</div>')
out.append('    </div>')
out.append('    <div class="top-signals-grid">')
for i, s in enumerate(top5, 1):
    out.append('      <div class="signal-card">')
    out.append('        <div><span class="sig-rank">%d</span><span class="sig-title">%s</span></div>' % (i, esc(s["title"])))
    out.append('        <div class="sig-tags"><span class="sig-dim">%s</span><span class="sig-stars">%s</span></div>' % (esc(s["dim"]), esc(s["stars"])))
    out.append('        <div class="sig-key">%s</div>' % esc(s["key"]))
    out.append('      </div>')
out.append('    </div>')
out.append('  </div>')
# summary table
out.append('  <div class="summary-section">')
out.append('    <div class="section-title">今日概要表</div>')
out.append('    <table>')
out.append('      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>领域</th><th>上市状态</th><th>信源</th><th>时间</th><th>重要度</th></tr></thead>')
out.append('      <tbody>')
for i, it in enumerate(all_items, 1):
    out.append(summary_row(it, i))
out.append('      </tbody>')
out.append('    </table>')
out.append('  </div>')
# domestic
out.append('  <div class="intel-section">')
out.append('    <div class="section-title">一、国内情报（15条）</div>')
out.append('      <div class="intel-cards">')
for i, it in enumerate(cn, 1):
    out.append(card_html(it, i, expanded=(i==1)))
out.append('      </div>')
out.append('  </div>')
# international
out.append('  <div class="intel-section">')
out.append('    <div class="section-title">二、国际情报（15条）</div>')
out.append('      <div class="intel-cards">')
for i, it in enumerate(intl, 16):
    out.append(card_html(it, i, expanded=False))
out.append('      </div>')
out.append('  </div>')
out.append('</div>')
out.append('')
out.append('<script>')
out.append('function toggleCard(el){ var c=el.closest(\'.intel-card\'); c.classList.toggle(\'expanded\'); }')
out.append('</script>')
out.append('</body>')
out.append('</html>')

content = "\n".join(out)
with open("E:/AI相关/预研究/202608/03_输出/WB_%s_硬件看板.html" % DATE, "w", encoding="utf-8") as f:
    f.write(content)
print("OK len=", len(content))
print("A=%d B=%d C=%d E=%d 5star=%d cats=%d dims=%d/%d" % (a_count, b_count, c_count, e_count, five_count, cats, on_count, len(dims)))
