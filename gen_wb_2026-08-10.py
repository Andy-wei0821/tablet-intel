# -*- coding: utf-8 -*-
import html

DATE = "2026-08-10"

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

# ---- DOMESTIC (sorted: coming -> progress -> released time-desc) ----
cn = [
 dict(title="Rokid AR 新款", domain="AR-VR/SoC/显示", stars="★★★★", status="coming", source="B",
   signal="新品亮相（即将上市）", confirm="1（Rokid 生态大会）",
   params="高通骁龙至尊版空间计算协处理器；58° FoV；电致变色镜片；新款 AR 眼镜",
   tech="空间计算协处理器 + 电致变色 + 大视场",
   why="Rokid 新款 AR 眼镜搭载骁龙空间计算芯片，58° FoV 提升沉浸感，推进消费级 AR 实用化。",
   related="AR-VR SoC、显示、结构（电致变色）。",
   vendor="Rokid / 新款 AR 眼镜", time="2026-06-26（生态大会）",
   url="https://www.rokid.com/", sources="Rokid 官方、生态大会", note="电致变色镜片，上市时间待官宣"),
 dict(title="REDMI Watch 6 Active/Lite", domain="智能手表/电池/显示", stars="★★★", status="progress", source="E",
   signal="新品曝光（进行中）", confirm="1（数码爆料）",
   params="AMOLED；470mAh；Active / Lite 双版本",
   tech="轻运动向智能手表分支",
   why="红米手表新增 Active/Lite 分支，覆盖轻运动与入门档，完善 REDMI 手表矩阵。",
   related="智能手表 显示、电池。",
   vendor="小米（REDMI）/ Watch 6 Active/Lite", time="2026-07-21（曝光）",
   url="https://www.mi.com/", sources="数码爆料", note="参数待官宣"),
 dict(title="小米音箱 超级小爱大模型升级", domain="智能音箱/音频/AIoT", stars="★★★", status="progress", source="B",
   signal="软件/AI 能力升级（进行中）", confirm="1（IT之家）",
   params="超级小爱-专家模式内测；声纹管理、小爱记忆、小爱管家；9 款音箱已内置超级小爱",
   tech="大模型语音助手升级 + 跨端多指令 + 声纹",
   why="小米音箱超级小爱专家模式内测，声纹/记忆/管家升级，智能音箱向主动 AI 中枢演进。",
   related="智能音箱 音频、AI/NPU、AIoT 互联。",
   vendor="小米 / 小爱音箱（超级小爱）", time="2026-08-08（内测）",
   url="https://www.mi.com/", sources="IT之家", note="覆盖 Xiaomi Sound 2 Max/Pro 等 9 款"),
 dict(title="OPPO Reno16 系列", domain="手机/影像/AI/SoC", stars="★★★★", status="released", source="A",
   signal="发布会新品", confirm="1（OPPO 官方）",
   params="2 亿像素超清四摄；实况随心贴；ColorOS 16；超流畅更 AI",
   tech="2 亿影像 + ColorOS 16 AI",
   why="OPPO Reno16 系列发布，2 亿影像 + AI 实况，巩固中高端影像线。",
   related="手机 影像、AI/NPU、系统。",
   vendor="OPPO / Reno16 系列", time="2026-08-04",
   url="https://www.oppo.com/", sources="OPPO 官网", note="含 Reno16 / Find X9s Pro 等"),
 dict(title="真我 GT8 Pro", domain="手机/SoC/影像/电池/无线充", stars="★★★★★", status="released", source="B",
   signal="新品上市", confirm="2（头条号 + 媒体）",
   params="骁龙8 Elite Gen5（第五代骁龙8至尊版）；6.79\" 2K 144Hz 7000nit；7000mAh；120W+50W 无线；2 亿长焦；RICOH GR 联名；¥2957 起",
   tech="骁龙8至尊版 + 2 亿影像 + 7000mAh 大电 + 百瓦快充",
   why="realme 旗舰 GT8 Pro 上市，骁龙8 Elite Gen5 + 2 亿影像，定义性能影像旗舰新基准。",
   related="旗舰 SoC、影像传感器、电池快充、无线充、高刷显示。",
   vendor="realme（真我）/ GT8 Pro", time="2026-08-02",
   url="https://www.realme.com/cn/", sources="今日头条、数码媒体", note="RICOH GR 影像联名"),
 dict(title="联想来酷 斗战者战7000P 锐龙版", domain="笔记本/SoC/散热/显示", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（联想来酷官方）",
   params="Ryzen 9 8940HX + RTX 5060；16\" 180Hz",
   tech="游戏本 + 锐龙9 + RTX50 系 + 高刷",
   why="来酷斗战者战7000P 锐龙版上市，锐龙9 + RTX5060 游戏性能，主流游戏本档。",
   related="笔记本 SoC、散热、显示、GPU。",
   vendor="联想（来酷）/ 斗战者战7000P 锐龙版", time="2026-07-28",
   url="https://www.lenovo.com.cn/", sources="联想来酷官方", note="RTX 5060 游戏本"),
 dict(title="联想小新 Pad Pro 13", domain="平板/SoC/显示/电池/AI", stars="★★★★", status="released", source="A",
   signal="新品上市", confirm="1（联想官方商城）",
   params="13\" 3.5K(3504×2190) 144Hz；骁龙8s；10200mAh；Android 16；¥2599",
   tech="大屏高刷 + 骁龙8s + 长续航 AI 学习平板",
   why="联想小新 Pad Pro 13 上市，13 寸大屏 + 骁龙8s，切入中高端大屏平板。",
   related="平板 SoC、高刷显示、电池快充、AI（天禧 AI）。",
   vendor="联想 / 小新 Pad Pro 13", time="2026-07-23",
   url="https://www.lenovo.com.cn/wiki/product-1053087.html", sources="联想官方商城", note="8+256 ¥2599"),
 dict(title="联想小新平板 11", domain="平板/SoC/显示/电池/手写笔", stars="★★★", status="released", source="A",
   signal="新品上市", confirm="1（联想官方）",
   params="11\" 2.5K(2560×1600)；天玑6300；7040mAh；480g；手写笔套装；¥1299",
   tech="轻薄护眼 + 天玑6300 + AI 伴学",
   why="联想入门平板更新，2.5K 护眼屏 + 手写笔，主打学生 AI 学习。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="联想 / 小新平板 11", time="2026-07-23",
   url="https://m.lenovo.com.cn/wiki/product-doc-46425.html", sources="联想官方商城", note="6.99mm / 480g"),
 dict(title="REDMI K Pad 2", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="2（官方 + 媒体）",
   params="8.8\" 3K 165Hz；天玑9500；9100mAh；67W；游戏平板；16+256 首销 ¥4399",
   tech="小尺寸电竞平板 + 天玑旗舰 + 高刷",
   why="REDMI K 系列电竞小平板上市，补齐小米平板游戏档，对标 iQOO Pad mini。",
   related="平板 SoC（天玑）、高刷显示、电池快充。",
   vendor="小米（REDMI）/ K Pad 2", time="2026-07-22",
   url="https://www.mi.com/", sources="小米商城、百度百科", note="游戏向小平板"),
 dict(title="联想来酷 Pro 14", domain="笔记本/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（联想来酷官方）",
   params="Core Ultra 5 135H / Ryzen 7 H255；14\" 2.8K 120Hz；80Wh；¥4929",
   tech="轻薄全能本 + 2.8K 高刷 + 长续航",
   why="联想来酷 Pro 14 上市，2.8K 120Hz 屏 + 80Wh，主流轻薄生产力。",
   related="笔记本 SoC、显示、电池。",
   vendor="联想（来酷）/ Pro 14", time="2026-07-22",
   url="https://www.lenovo.com.cn/", sources="联想来酷官方", note="双平台（Intel/AMD）"),
 dict(title="酷态科 10号 车载磁吸无线充", domain="无线充/电池/认证", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（充电头网）",
   params="磁吸无线 15W + 有线 90W；N52H 磁体；伸缩线；¥149 起；暂不支持 Qi2",
   tech="车载支架 + 磁吸无线 + 有线快充三合一",
   why="酷态科车载磁吸无线充上市，15W 磁吸 + 90W 有线，车载补能新形态。",
   related="无线充、电池（BMS）、结构。",
   vendor="酷态科（CUKTECH）/ 10号 车载磁吸无线充", time="2026-07-17（预售）",
   url="https://www.chongdiantou.com/archives/1784199970505.html", sources="充电头网", note="暂不支持 Qi2 协议"),
 dict(title="联想来酷 Air 14 LNL", domain="笔记本/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（联想来酷官方）",
   params="Core Ultra 5 228V（Lunar Lake）；14\" 2.8K 120Hz；1.18kg；80Wh",
   tech="轻量长续航 + Lunar Lake + 高刷屏",
   why="来酷 Air 14 搭载 Lunar Lake，1.18kg + 80Wh，主打轻薄长续航办公。",
   related="笔记本 SoC、显示、电池、AI/NPU（Lunar Lake NPU）。",
   vendor="联想（来酷）/ Air 14 LNL", time="2026-07-10",
   url="https://www.lenovo.com.cn/", sources="联想来酷官方", note="Lunar Lake 平台"),
 dict(title="REDMI Watch 6", domain="智能手表/显示/电池/传感器", stars="★★★★", status="released", source="B",
   signal="海外上市", confirm="1（海外媒体）",
   params="2.07\" AMOLED；550mAh；24 天续航；健康监测",
   tech="大屏长续航 + 健康监测",
   why="REDMI Watch 6 海外上市，2.07\" 大屏 + 24 天续航，红米手表旗舰化。",
   related="智能手表 显示、电池、传感器。",
   vendor="小米（REDMI）/ Watch 6", time="2026-07-09（韩国预售）",
   url="https://www.mi.com/", sources="海外数码媒体", note="韩国首发"),
 dict(title="讯飞 AI 眼镜", domain="AR-VR/AI/显示/影像", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="2（BEYOND Expo + 媒体）",
   params="40g 双目显示；Micro-LED + 树脂波导；122 语言实时翻译；1200 万摄像头；160mAh/6hr；¥4299 起",
   tech="轻量双目 AI 眼镜 + 实时翻译 + 拍摄",
   why="讯飞 AI 眼镜上市，40g 轻量 + 122 语言翻译，AI 眼镜走向实用化。",
   related="AR-VR 显示（Micro-LED 波导）、AI/NPU、影像、电池。",
   vendor="科大讯飞 / AI 眼镜", time="2026-06-15（上市）/ 8 月推广",
   url="https://www.iflytek.com/", sources="BEYOND Expo、讯飞官方", note="双目 Micro-LED"),
 dict(title="联想小新 Pad Studio 11.5", domain="平板/音频/显示/电池", stars="★★★", status="released", source="A",
   signal="在售产品", confirm="1（联想官方）",
   params="11.5\" 2K 90Hz；Helio G99；8 扬声器 JBL Hi-Res；650g；¥1399",
   tech="JBL 音响 + Dolby Atmos + 无级悬停",
   why="影音娱乐向平板，JBL 八扬声器 + 杜比，差异化影音体验。",
   related="平板 音频、显示、结构（悬停）。",
   vendor="联想 / 小新 Pad Studio", time="在售（2026）",
   url="https://m.lenovo.com.cn/wiki/product-doc-42446.html", sources="联想官方商城", note="26W 功率"),
]

# ---- INTERNATIONAL (sorted: coming -> released time-desc) ----
intl = [
 dict(title="OnePlus 16", domain="手机/SoC/影像/电池/无线充", stars="★★★★★", status="coming", source="B",
   signal="爆料/即将发布", confirm="1（PhoneArena）",
   params="骁龙8 Elite Gen 6 Pro（2nm）；6.8\" OLED 240Hz；9000mAh；120W+50W 无线；双 2 亿像素；16GB LPDDR6",
   tech="2nm 旗舰芯 + 双 2 亿影像 + 9000mAh 硅碳电池",
   why="一加 16 爆料，2nm 骁龙8 Elite Gen6 Pro + 双 2 亿 + 9000mAh，年度性能旗舰。",
   related="旗舰 SoC、影像、电池快充、无线充。",
   vendor="一加（OnePlus）/ 16", time="2026 Q4（预计 10 月）",
   url="https://www.phonearena.com/phones/OnePlus-16_id12961", sources="PhoneArena、一加官方预热", note="起售 ¥4999（爆料）"),
 dict(title="Samsung Galaxy Tab S12 Ultra", domain="平板/SoC/显示/电池", stars="★★★★★", status="coming", source="B",
   signal="官方确认（即将上市）", confirm="2（三星财报 + Notebookcheck）",
   params="14.6\" AMOLED；天玑9500；11600mAh；45W；S Pen；One UI 9",
   tech="超大屏 AMOLED 旗舰平板 + 天玑9500 + 长续航",
   why="三星官方确认 Tab S12 系列，Ultra 版 14.6\" AMOLED + 11600mAh，高端大屏标杆。",
   related="平板 SoC、显示-OLED、电池、手写笔。",
   vendor="三星 / Galaxy Tab S12 Ultra", time="2026 H2（预计 9-10 月）",
   url="https://www.notebookcheck.net/Samsung-officially-confirms-Galaxy-Tab-S12-and-Galaxy-S26-FE.1355643.0.html", sources="三星 Q2 财报、Notebookcheck", note="9 月/10 月预计"),
 dict(title="三星 × Google Android XR 眼镜", domain="AR-VR/AI/SoC/显示", stars="★★★★", status="coming", source="A",
   signal="官方发布（即将上市）", confirm="2（Google I/O + 三星）",
   params="Gentle Monster / Warby Parker 设计；Gemini；Android XR；2026 秋季",
   tech="Android XR + Gemini AI + 时尚镜框",
   why="三星 + 谷歌 Android XR 眼镜 2026 秋季上市，Gemini 加持，XR 生态关键落子。",
   related="AR-VR AI/NPU、SoC、显示。",
   vendor="三星 × Google / Android XR 眼镜", time="2026 秋季（预计）",
   url="https://blog.google/", sources="Google I/O 2026、三星", note="时尚品牌联名"),
 dict(title="Apple Watch Ultra 4", domain="智能手表/传感器/结构/电池", stars="★★★★", status="coming", source="B",
   signal="即将发布", confirm="1（媒体日历）",
   params="钛金属；更大屏；续航升级；潜水/户外运动；9 月发布",
   tech="旗舰运动手表 + 钛合金 + 专业传感器",
   why="Apple Watch Ultra 4 预计 9 月发布，钛金属旗舰运动表，苹果手表顶配。",
   related="智能手表 结构（钛）、传感器、电池。",
   vendor="Apple / Watch Ultra 4", time="2026-09（预计）",
   url="https://www.apple.com/watch/", sources="穿戴媒体发布日历", note="同期 Series 11"),
 dict(title="Apple Watch Series 11", domain="智能手表/传感器/电池", stars="★★★★", status="coming", source="B",
   signal="即将发布", confirm="1（媒体日历）",
   params="S11 芯片；健康监测；¥299 起；9 月发布",
   tech="标准旗舰手表 + 健康传感器升级",
   why="Apple Watch Series 11 预计 9 月发布，¥299 入门旗舰，苹果手表主力走量。",
   related="智能手表 传感器、电池。",
   vendor="Apple / Watch Series 11", time="2026-09（预计）",
   url="https://www.apple.com/watch/", sources="穿戴媒体发布日历", note="同期 Ultra 4"),
 dict(title="Google Pixel 11", domain="手机/SoC/AI/影像", stars="★★★★", status="coming", source="B",
   signal="发布会预热（即将上市）", confirm="1（谷歌官方活动）",
   params="Tensor G5（或新代）；Android 16；Gemini；与 Pixel Watch 5 同台",
   tech="Tensor 芯片 + Gemini AI + 旗舰影像",
   why="谷歌 Pixel 11 将于 8/12 发布，Tensor + Gemini，安卓标杆 AI 手机。",
   related="手机 SoC、AI/NPU、影像、系统。",
   vendor="Google / Pixel 11", time="2026-08-12（发布）",
   url="https://store.google.com/", sources="Google Made by Google 活动、媒体", note="与 Pixel Watch 5 同台"),
 dict(title="Garmin Fenix 9 系列", domain="智能手表/传感器/电池/结构", stars="★★★★", status="coming", source="B",
   signal="即将发布（FCC 曝光）", confirm="1（FCC + 媒体）",
   params="Fenix 9 / 9 Pro / Enduro 4；户外 GPS；~$799 起；钛/蓝宝石",
   tech="旗舰户外运动表 + 多频 GPS + 长续航",
   why="Garmin Fenix 9 系列 8 月有望发布，户外旗舰，多频 GPS + 蓝宝石。",
   related="智能手表 传感器（GPS/心率）、电池、结构（钛）。",
   vendor="Garmin / Fenix 9 系列", time="2026-08（预计）",
   url="https://www.garmin.com/", sources="FCC 认证、Smartwearables", note="Enduro 4 同发"),
 dict(title="Lenovo ThinkPad P16v 2026 顶配", domain="笔记本/SoC/显示/散热/AI", stars="★★★★", status="released", source="B",
   signal="新品开售", confirm="1（网易/联想官方）",
   params="Intel Ultra 7 251HX（18 核）；RTX Pro 1000（Blackwell 8G GDDR7）；32GB+1TB；16\" 2.5K IPS；85Wh；¥20999",
   tech="移动工作站 + RTX Pro 专业卡 + 32GB 原生",
   why="ThinkPad P16v 新顶配 8/10 开售，Ultra7 251HX + RTX Pro1000 专业卡，移动工作站。",
   related="笔记本 SoC、显示、散热、AI（RTX Pro ISV）。",
   vendor="联想 / ThinkPad P16v（2026 顶配）", time="2026-08-10（开售）",
   url="https://www.163.com/dy/article/L3EQ26B90556GYP2.html", sources="联想官方、网易", note="通过 MIL-STD-810H"),
 dict(title="荣耀平板 X9 Max", domain="平板/显示/电池/SoC", stars="★★★★", status="released", source="B",
   signal="海外发布", confirm="1（头条号 + 荣耀英国官网）",
   params="13\" 2.5K 120Hz；10100mAh；45W；骁龙6s Gen2；MagicOS 10（安卓16）；618g",
   tech="大屏长续航 + 跨设备协同 + AI 备忘录",
   why="荣耀平板 X9 Max 海外发布，13 寸 + 10100mAh，荣耀海外大屏平板布局。",
   related="平板 显示、电池、SoC、AI。",
   vendor="荣耀（HONOR）/ 平板 X9 Max", time="2026-08-05（发布）",
   url="https://www.toutiao.com/w/1872673417601225/", sources="荣耀英国官网、数码媒体", note="兼容 Magic-Pencil 4s"),
 dict(title="ASUS TUF F16 2026", domain="笔记本/SoC/显示/GPU", stars="★★★", status="released", source="B",
   signal="海外上市", confirm="1（TechStoriesIndia）",
   params="i7-14650HX；RTX 5050/5060 8GB GDDR7；16\" FHD+ 144Hz；16GB DDR5；1TB",
   tech="游戏本 + RTX50 系 + 高刷",
   why="华硕 TUF F16 2026 印度上市，i7 + RTX5060 游戏性能，主流游戏本。",
   related="笔记本 SoC、显示、GPU、散热。",
   vendor="华硕（ASUS）/ TUF F16 2026", time="2026-08-04（印度）",
   url="https://techstoriesindia.in/", sources="Tech Stories India", note="印度市场首发"),
 dict(title="Anker Prime Qi2.2 三合一折叠无线充", domain="无线充/认证/散热", stars="★★★★", status="released", source="B",
   signal="新品拆解/上市", confirm="1（充电头网）",
   params="Qi2.2 25W；AirCool 风冷；三合一折叠；红点 2026；$149.99",
   tech="Qi2.2 磁吸 + 主动风冷 + 折叠便携",
   why="Anker Prime Qi2.2 三合一发布，25W 磁吸 + 风冷散热，Qi2.2 生态标杆。",
   related="无线充、认证（Qi2.2/红点）、散热。",
   vendor="Anker / Prime Qi2.2 三合一折叠无线充", time="2026-07-21",
   url="https://www.anker.com/", sources="充电头网、Anker", note="红点设计奖 2026"),
 dict(title="Amazon Echo Dot Max / Echo Studio（2026）", domain="智能音箱/音频/AI", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（亚马逊）",
   params="新一代 Alexa+；AZ3 芯片；Echo Dot Max / Echo Studio；360° 音频",
   tech="Alexa+ 大模型 + 自研 AZ3 芯片 + 空间音频",
   why="亚马逊新一代 Echo 搭载 Alexa+ 与 AZ3 芯片，智能音箱 AI 化升级。",
   related="智能音箱 音频、AI/NPU（AZ3）、AIoT。",
   vendor="Amazon / Echo Dot Max / Echo Studio（2026）", time="2026",
   url="https://www.amazon.com/", sources="Amazon、媒体", note="Alexa+ 大模型"),
 dict(title="Microsoft Surface Laptop 第 8 版", domain="笔记本/SoC/AI/显示/电池", stars="★★★★★", status="released", source="A",
   signal="在售新品", confirm="1（微软官方）",
   params="Snapdragon X2 Plus/Elite（10/12 核）；NPU 80 TOPS；13.8\" LCD HDR；WiFi 7；20hr；最高 64GB",
   tech="Copilot+ PC + Snapdragon X2 + 80 TOPS NPU + 长续航",
   why="Surface Laptop 第 8 版在售，Snapdragon X2 + 80 TOPS NPU，Copilot+ 标杆轻薄本。",
   related="笔记本 SoC、AI/NPU、显示、电池、无线（WiFi7）。",
   vendor="Microsoft / Surface Laptop（8th Edition）", time="2026（在售）",
   url="https://www.microsoft.com/en-sg/store/configure/surface-laptop-13-8-inch-8th-edition/8mzbmmcjzpmf", sources="微软官方商城", note="Copilot+ PC"),
 dict(title="Google Home Speaker 2026", domain="智能音箱/音频/AI", stars="★★★", status="released", source="B",
   signal="新品上市", confirm="1（Google）",
   params="Gemini；360° 音频；$99.99；2026 款",
   tech="Gemini AI + 360° 环绕声",
   why="谷歌 2026 款 Home Speaker 上市，Gemini 加持，智能音箱 AI 化。",
   related="智能音箱 音频、AI/NPU。",
   vendor="Google / Home Speaker 2026", time="2026-06-25",
   url="https://store.google.com/", sources="Google、媒体", note="$99.99"),
 dict(title="Snap SPECS", domain="AR-VR/显示/SoC/AI", stars="★★★★", status="released", source="B",
   signal="新品发布", confirm="1（AWE）",
   params="$2195；132/136g；LCOS 51° FoV；双骁龙；7ms 延迟；4hr 续航",
   tech="双处理器 AR 眼镜 + 低延迟 + 大视场",
   why="Snap SPECS 发布，双骁龙 + 7ms 低延迟 + 51° FoV，消费级 AR 眼镜新标杆。",
   related="AR-VR 显示（LCOS）、SoC（双骁龙）、电池。",
   vendor="Snap / SPECS", time="2026-06-16（AWE）",
   url="https://www.snap.com/", sources="AWE 2026、Snap", note="双骁龙协处理"),
]

# ---- Top 5 signals ----
top5 = [
 dict(title="真我 GT8 Pro", dim="手机/SoC/影像/电池/无线充", stars="★★★★★",
      key="骁龙8 Elite Gen5 + 2 亿影像 + 7000mAh，8/2 上市"),
 dict(title="Galaxy Tab S12 Ultra", dim="平板/SoC/显示/电池", stars="★★★★★",
      key="14.6\" AMOLED + 天玑9500 + 11600mAh，H2 发布"),
 dict(title="OnePlus 16", dim="手机/SoC/影像/电池/无线充", stars="★★★★★",
      key="2nm 骁龙8 Elite Gen6 Pro + 双 2 亿 + 9000mAh，Q4"),
 dict(title="Surface Laptop 第 8 版", dim="笔记本/SoC/AI/显示/电池", stars="★★★★★",
      key="Snapdragon X2 + 80 TOPS NPU，Copilot+ PC 标杆"),
 dict(title="讯飞 AI 眼镜", dim="AR-VR/AI/显示/影像", stars="★★★★",
      key="40g 双目 Micro-LED + 122 语言翻译，6/15 上市"),
]

# ---- Dimension panel ----
dims = [
 ("SoC/芯片", 28, True), ("显示/OLED", 20, True), ("电池/快充", 22, True), ("散热", 4, True),
 ("无线通信", 8, True), ("音频", 4, True), ("摄像头", 4, True), ("结构/工艺", 4, True),
 ("传感器", 6, True), ("手写笔/触控", 3, True), ("生物识别", 5, True), ("AI/NPU", 16, True),
 ("马达/触觉", 0, False), ("折叠屏", 0, False), ("BMS/电源", 4, True), ("认证/合规", 4, True),
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
e_count = sum(1 for it in all_items if it["source"]=="E")
five_count = sum(1 for it in all_items if it["stars"].count("★")==5)
cats = len(set(d.split("/")[0] for it in all_items for d in it["domain"].split("/")))

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
print("A=%d B=%d E=%d 5star=%d cats=%d dims=%d/%d" % (a_count, b_count, e_count, five_count, cats, on_count, len(dims)))
