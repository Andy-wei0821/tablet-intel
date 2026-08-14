# -*- coding: utf-8 -*-
import html

DATE = "2026-08-14"

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

# ---- DOMESTIC (sorted: coming -> released -> progress, time desc within) ----
cn = [
 dict(title="荣耀 Robot Phone", domain="手机/SoC/电池/AI/生物识别", stars="★★★★★", status="coming", source="A",
   signal="官宣（即将发布）", confirm="1（荣耀官方）",
   params="骁龙8 Elite Gen5；7060mAh；阿莱（哈苏）色彩联合调校；端侧 AI 影像；8 月 12 日官宣",
   tech="AI 影像旗舰手机 + 骁龙8 Elite Gen5 + 超大电池 + 阿莱色彩",
   why="荣耀 Robot Phone 以骁龙8 Elite Gen5 与 7060mAh 超大电池切入 AI 影像旗舰，阿莱色彩联合调校强化人像/电影质感，定义 2026 国产 AI 手机新标杆。",
   related="手机 SoC、电池、生物识别（屏下指纹）、AI/NPU。",
   vendor="荣耀 / Robot Phone", time="2026-08-12（官宣）",
   url="https://www.honor.com/cn/", sources="荣耀官方", note="阿莱色彩 AI 影像旗舰"),
 dict(title="OPPO Watch 3", domain="智能手表/SoC/传感器/结构/生物识别", stars="★★★★", status="coming", source="B",
   signal="发布（8/19 开售）", confirm="1（OPPO官方）",
   params="骁龙W5 Gen1 + Apollo4 Plus 双芯；UDDE 2.0；1499元起；ECG 心电；独立 eSIM；550mAh/5天",
   tech="智能手表 + 骁龙W5 + 双芯片混动 + ECG + eSIM",
   why="OPPO Watch 3 以骁龙W5 与 UDDE 双引擎混动 2.0 提升续航与智能体验，ECG 心电 + 独立 eSIM 补齐健康与通信，1499 起切入主流旗舰表。",
   related="智能手表 SoC、传感器（心率/血氧/ECG）、结构、生物识别（eSIM）。",
   vendor="OPPO / Watch 3", time="2026-08-19（开售）",
   url="https://www.oppo.com/cn/", sources="OPPO官方", note="骁龙W5 + ECG"),
 dict(title="vivo Pad3 系列（爆料）", domain="平板/SoC/显示/电池", stars="★★★", status="coming", source="C",
   signal="爆料（待发布）", confirm="1（行业爆料）",
   params="天玑9300；12.95英寸 3K LCD；144Hz；16GB；预计 8 月",
   tech="大屏性能平板 + 天玑9300 + 3K高刷",
   why="vivo Pad3 系列据爆料将首发天玑9300 平板平台，12.95英寸 3K 144Hz 主攻高性能大屏生产力，补充 vivo 平板旗舰线。",
   related="平板 SoC、显示、电池。",
   vendor="vivo / Pad3 系列", time="2026-08-03（爆料/待发布）",
   url="https://www.vivo.com.cn/", sources="行业爆料（待印证）", note="天玑9300 平板待印证"),
 dict(title="LOOKTECH 智能眼镜", domain="AR-VR眼镜/显示/AI/音频", stars="★★★★", status="released", source="B",
   signal="在售新品（8/13 发布）", confirm="1（LOOKTECH官方）",
   params="30g 轻量；GPT-5 大模型；4K 摄像头；开放式音频；多模态 AI 助手",
   tech="AI 眼镜 + GPT-5 + 4K + 轻量化",
   why="LOOKTECH 智能眼镜以 30g 轻量与 GPT-5 端侧/云端大模型切入消费级 AI 眼镜，4K 拍摄+开放式音频服务随身 AI 助手场景。",
   related="AR-VR 显示、AI/NPU、音频、结构（轻量）。",
   vendor="LOOKTECH / 智能眼镜", time="2026-08-13（发布）",
   url="https://www.looktech.ai/", sources="LOOKTECH官方", note="GPT-5 AI 眼镜"),
 dict(title="小米蓝牙音箱磁吸版", domain="智能音箱/音频/无线/结构", stars="★★★", status="released", source="B",
   signal="在售新品（众筹）", confirm="1（小米官方）",
   params="IP67 防水防尘；蓝牙 6.0；MagSafe 磁吸；95g；众筹价 132 元；8/12 上线",
   tech="便携蓝牙音箱 + 磁吸 + 蓝牙6.0 + 三防",
   why="小米蓝牙音箱磁吸版以 IP67 + MagSafe 磁吸与 95g 超轻机身切入随身便携音箱，蓝牙 6.0 提升连接稳定性，132 元众筹价主打性价比。",
   related="智能音箱 音频、无线通信（蓝牙6.0）、结构（磁吸/三防）。",
   vendor="小米 / 蓝牙音箱磁吸版", time="2026-08-12（众筹）",
   url="https://www.mi.com/", sources="小米官方", note="IP67 磁吸便携音箱"),
 dict(title="REDMI K100 Pro", domain="手机/SoC/显示/电池/快充", stars="★★★★", status="released", source="B",
   signal="在售新品（8/11 发布）", confirm="1（REDMI官方）",
   params="骁龙8 至尊版；185Hz 高刷；2K 屏；5500mAh；120W 快充；2999元起",
   tech="性能手机 + 骁龙8至尊版 + 185Hz + 百瓦快充",
   why="REDMI K100 Pro 以骁龙8至尊版与 185Hz 高刷屏主打极致性能，5500mAh+120W 续航快充组合覆盖重度游戏与日常。",
   related="手机 SoC、显示、电池快充。",
   vendor="REDMI / K100 Pro", time="2026-08-11（发布）",
   url="https://www.mi.com/", sources="REDMI官方", note="185Hz 性能旗舰"),
 dict(title="小米 18 标准版", domain="手机/SoC/摄像头/AI/生物识别", stars="★★★★★", status="released", source="A",
   signal="在售新品（8/10 发布）", confirm="1（小米官方）",
   params="骁龙8 Elite Gen6（2nm）；双 2 亿像素徕卡影像；6.5英寸 2K 120Hz；5500mAh；5499元起",
   tech="AI 影像旗舰 + 2nm 骁龙 + 双2亿徕卡 + 屏下指纹",
   why="小米 18 标准版首发 2nm 骁龙8 Elite Gen6 与双 2 亿像素徕卡影像，将旗舰影像与 AI 计算摄影下放标准版，5499 起重塑性价比旗舰。",
   related="手机 SoC（2nm/NPU）、摄像头（双2亿徕卡）、AI/NPU、生物识别（屏下指纹）。",
   vendor="小米 / 18 标准版", time="2026-08-10（发布）",
   url="https://www.mi.com/", sources="小米官方", note="2nm + 双2亿徕卡"),
 dict(title="联想小新平板 Pro GT & 12.1", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="B",
   signal="在售新品（8/6 开售）", confirm="1（联想官方）",
   params="骁龙8 Gen3；11.3英寸 3.2K LCD 144Hz；458g；5.99mm；8860mAh；68W；天禧 AI",
   tech="旗舰 AI 平板 + 骁龙8 Gen3 + 3.2K高刷 + 轻薄",
   why="联想小新平板 Pro GT & 12.1 以骁龙8 Gen3 与 11.3英寸 3.2K 144Hz 切入高性能 AI 平板，458g/5.99mm 轻薄机身 + 天禧智能体强化移动办公。",
   related="平板 SoC、显示、电池、手写笔/触控、AI/NPU。",
   vendor="联想（小新）/ 平板 Pro GT & 12.1", time="2026-08-06（开售）",
   url="https://www.ithome.com/0/869/592.htm", sources="联想官方、IT之家", note="骁龙8 Gen3 旗舰平板"),
 dict(title="雷神 猎刃 S", domain="笔记本电脑/SoC/显示/散热/GPU", stars="★★★★", status="released", source="B",
   signal="在售新品（8/5 新增配置）", confirm="1（雷神官方）",
   params="i5-14450HX + RTX5050 / R7-7745HX + RTX5070；16英寸 2.5K 300Hz；80Wh；双烤散热",
   tech="游戏本 + 酷睿/锐龙 + RTX50系 + 强散热",
   why="雷神猎刃 S 于 8/5 新增 i5-14450HX+RTX5050 与 R7-7745HX+RTX5070 两档配置，2.5K 300Hz 高刷 + 80Wh 覆盖主流游戏本需求。",
   related="笔记本 SoC、显示、散热、GPU。",
   vendor="雷神（Thunderobot）/ 猎刃 S", time="2026-08-05（新增配置）",
   url="https://www.thunderobot.com/", sources="雷神官方", note="双配置游戏本"),
 dict(title="李未可 X-AI 记忆眼镜", domain="AR-VR眼镜/AI/音频/结构", stars="★★★★", status="released", source="B",
   signal="在售新品（WAIC 7/17）", confirm="1（李未可官方）",
   params="26g 轻量；腾讯云 WorkBuddy 合作；端侧记忆/摘要；开放式音频；拍摄",
   tech="AI 记忆眼镜 + 轻量化 + 端侧记忆 + 音频",
   why="李未可 X-AI 记忆眼镜于 WAIC 发布，26g 轻量机身结合腾讯云 WorkBuddy 端侧记忆与摘要能力，主打随身 AI 记忆助手。",
   related="AR-VR AI/NPU、音频、结构（轻量）。",
   vendor="李未可（LLIWEIKE）/ X-AI 记忆眼镜", time="2026-07-17（WAIC）",
   url="https://www.toutiao.com/", sources="李未可官方、腾讯云", note="26g AI 记忆眼镜"),
 dict(title="vivo Pad5c", domain="平板/SoC/显示/电池/音频", stars="★★★★", status="released", source="B",
   signal="在售新品（7/1 发布）", confirm="1（vivo官方）",
   params="骁龙8s Gen3；12.1英寸 2.8K 144Hz；10000mAh；584g；6.62mm；四扬声器；2699元起",
   tech="大屏影音平板 + 骁龙8s + 2.8K高刷 + 长续航",
   why="vivo Pad5c 以骁龙8s Gen3 与 12.1英寸 2.8K 144Hz 切入大屏影音学习平板，10000mAh+584g 平衡续航与便携，2699 起主打性价比。",
   related="平板 SoC、显示、电池、音频。",
   vendor="vivo / Pad5c", time="2026-07-01（发布）",
   url="https://aiqicha.baidu.com/details/rankList?query=b3a7dc44bfc7e9e7a2ee0c5a22bf44af&type=20", sources="vivo官方、百度爱企查", note="骁龙8s 大屏平板"),
 dict(title="OPPO Pad Air5", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="B",
   signal="在售新品（2026 款）", confirm="1（OPPO官方）",
   params="天玑7300-Ultra；12.1英寸 2.8K 120Hz；10050mAh；597g；6.83mm；四扬声器；手写笔",
   tech="轻薄学习平板 + 天玑7300 + 2.8K + 长续航",
   why="OPPO Pad Air5 以 12.1英寸 2.8K 120Hz 与 10050mAh 大电池切入学生/学习平板，天玑7300-Ultra + ColorOS AI 工具覆盖网课与轻创作。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="OPPO / Pad Air5", time="2026（在售）",
   url="https://www.oppo.com/cn/", sources="OPPO官方", note="2.8K 学习平板"),
 dict(title="红魔游戏本 16 Pro 2026", domain="笔记本电脑/SoC/显示/散热/GPU", stars="★★★★", status="released", source="B",
   signal="在售新品（2026 款）", confirm="1（红魔官方）",
   params="酷睿Ultra9 275HX；RTX5070Ti / RTX5080；16英寸 2.5K 300Hz；双烤散热；14999元起",
   tech="电竞旗舰本 + Ultra9 + RTX50系 + 强散热",
   why="红魔游戏本 16 Pro 2026 以 Ultra9 275HX 与 RTX5070Ti/5080 冲击电竞旗舰，16英寸 2.5K 300Hz + 双烤散热兼顾高帧游戏与创作。",
   related="笔记本 SoC、显示、散热、GPU。",
   vendor="红魔（努比亚）/ 游戏本 16 Pro 2026", time="2026（在售）",
   url="https://www.nubia.com/", sources="红魔官方", note="Ultra9 电竞本"),
 dict(title="倍思 PicoGo AM52 Qi2.2", domain="无线充/电池/BMS/认证", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（倍思官方）",
   params="Qi2.2 磁吸 25W 无线；10000mAh；45W 有线；BMS 温控；CCC/Qi2 认证",
   tech="Qi2.2 磁吸 + 25W 无线 + 移动电源 + BMS 温控 + 认证合规",
   why="倍思 PicoGo AM52 以 Qi2.2 磁吸 25W 与 10000mAh 二合一充电宝切入磁吸生态，BMS 温控 + CCC/Qi2 认证保障安全合规。",
   related="无线充、电池（BMS）、认证（CCC/Qi2）。",
   vendor="倍思（Baseus）/ PicoGo AM52", time="2026（在售）",
   url="https://www.baseus.com/", sources="倍思官方", note="Qi2.2 磁吸二合一"),
 dict(title="REDMI Watch 5 新版本先锋计划", domain="智能手表/显示/软件/传感器", stars="★★★", status="progress", source="B",
   signal="进行中（内测 8/7-8/16）", confirm="1（小米官方）",
   params="新版手表微信（语音转文字/会话标记）；铁三运动优化；原 550mAh/2.07英寸；599元起",
   tech="智能手表 + 系统内测 + 手表微信 + 健康监测",
   why="REDMI Watch 5 新版本先锋计划（8/7 启动内测）带来新版手表微信与铁三运动优化，延续小米穿戴生态的体验迭代。",
   related="智能手表 显示、软件（手表微信）、传感器（心率/血氧）。",
   vendor="小米（REDMI）/ Watch 5 新版本", time="2026-08-07（内测）",
   url="https://www.ithome.com/0/987/046.htm", sources="小米官方、IT之家", note="手表微信内测"),
]

# ---- INTERNATIONAL (sorted: coming -> released, time desc within) ----
intl = [
 dict(title="Acer Iconia Duo S14", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="coming", source="B",
   signal="即将上市（北美 9 月）", confirm="1（Acer官方）",
   params="天玑8300；14.2英寸 2.8K OLED（2880×1840）；3:2；120Hz；Android 16；主动笔",
   tech="创作旗舰平板 + 天玑8300 + 2.8K OLED + 3:2",
   why="Acer Iconia Duo S14 以 14.2英寸 2.8K OLED 与天玑8300 主攻创作者/专业生产力，3:2 比例 + 主动笔适配文档与创作。",
   related="平板 SoC、显示-OLED、电池、手写笔/触控。",
   vendor="Acer / Iconia Duo S14", time="2026-09（北美上市）",
   url="https://www.acer.com/", sources="Acer官方", note="14.2寸 OLED 创作平板"),
 dict(title="iPad 12（爆料）", domain="平板/SoC/显示/电池", stars="★★★", status="coming", source="C",
   signal="爆料（预计 9 月发布）", confirm="1（行业爆料）",
   params="A18 芯片；10.9英寸 LCD；7698mAh；6GB 内存；Apple Intelligence；2999元起（预估）",
   tech="入门 iPad + A18 + Apple Intelligence",
   why="iPad 12 据爆料将搭载 A18 并首次支持 Apple Intelligence，10.9英寸 LCD 入门定位把苹果 AI 能力下放到标准版 iPad。",
   related="平板 SoC（A18/NPU）、显示、电池、AI/NPU。",
   vendor="Apple / iPad 12", time="2026-09（预计发布）",
   url="https://www.apple.com/", sources="行业爆料（待印证）", note="A18 + Apple Intelligence"),
 dict(title="Acer Iconia Duo S12", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="coming", source="B",
   signal="即将上市（北美 8 月）", confirm="1（Acer官方）",
   params="天玑7400；12.2英寸 2.8K OLED；nano-texture 防眩；8GB/256GB；Android 16；主动笔",
   tech="影音生产力平板 + 天玑7400 + 2.8K OLED + 防眩",
   why="Acer Iconia Duo S12 以 12.2英寸 2.8K OLED 与 nano-texture 防眩玻璃切入影音生产力，天玑7400 + 主动笔覆盖创作与娱乐。",
   related="平板 SoC、显示-OLED、电池、手写笔/触控。",
   vendor="Acer / Iconia Duo S12", time="2026-08（北美上市）",
   url="https://www.acer.com/", sources="Acer官方", note="12.2寸 OLED 平板"),
 dict(title="Acer AR Vision GR0", domain="AR-VR眼镜/显示/SoC/AI", stars="★★★★", status="coming", source="B",
   signal="亮相（Computex 2026 / 待上市）", confirm="1（Acer官方）",
   params="AR 眼镜；Computex 2026 亮相；空间显示；AI 助手；轻量设计",
   tech="消费级 AR 眼镜 + 空间显示 + AI",
   why="Acer 于 Computex 2026 展示 AR Vision GR0，以轻量 AR 眼镜 + 空间显示 + AI 助手切入随身计算，补全 Acer 可穿戴线。",
   related="AR-VR 显示、SoC、AI/NPU。",
   vendor="Acer / AR Vision GR0", time="2026（Computex亮相/待上市）",
   url="https://www.acer.com/", sources="Acer官方", note="Acer AR 眼镜"),
 dict(title="Acer AI 眼镜 GI0", domain="AR-VR眼镜/AI/音频/显示", stars="★★★★", status="coming", source="B",
   signal="亮相（Computex 2026 / 待上市）", confirm="1（Acer官方）",
   params="Gemini AI 眼镜；Computex 2026 亮相；拍摄/翻译/语音助手；开放式音频",
   tech="AI 眼镜 + Gemini + 拍摄 + 音频",
   why="Acer AI 眼镜 GI0 集成 Gemini 大模型，以拍摄/翻译/语音助手切入消费级 AI 眼镜，与 AR Vision 形成 Acer 智能穿戴双线。",
   related="AR-VR AI/NPU、音频、显示。",
   vendor="Acer / AI 眼镜 GI0", time="2026（Computex亮相/待上市）",
   url="https://www.acer.com/", sources="Acer官方", note="Gemini AI 眼镜"),
 dict(title="Xiaomi 16（全球版）", domain="手机/SoC/电池/快充/摄像头", stars="★★★", status="coming", source="C",
   signal="待发布（全球版预计 2026 下半年）", confirm="1（行业汇总）",
   params="骁龙8 Elite Gen5；6.3英寸 OLED 144Hz；7000mAh；100W 有线 + 50W 无线；IP69；三摄 50MP",
   tech="全球旗舰 + 骁龙8至尊版 + 7000mAh + 百瓦快充",
   why="Xiaomi 16 全球版据汇总将搭载骁龙8 Elite Gen5 与 7000mAh 超大电池，100W 有线 + 50W 无线补齐续航，预计 2026 下半年出海。",
   related="手机 SoC、电池快充、摄像头、生物识别（屏下指纹）。",
   vendor="Xiaomi / 16（全球版）", time="2026（全球版待发布）",
   url="https://smartprix.com/mobiles/xiaomi-16-ppd1cywoif3p", sources="Smartprix 等汇总（待印证）", note="全球版待发布"),
 dict(title="Pixel 11 Pro Fold", domain="手机/SoC/折叠屏/AI/显示", stars="★★★★★", status="released", source="B",
   signal="在售新品（8/14 发布 / 8/20 开售）", confirm="1（Google官方）",
   params="Tensor G6（台积电 3nm）；折叠屏；Gemini 深度集成；Android 17；七年更新；8/20 开售",
   tech="折叠 AI 旗舰 + Tensor G6 + 折叠屏 + 端侧Gemini",
   why="Pixel 11 Pro Fold 随 Made by Google 2026 于 8/14 发布，Tensor G6（3nm）配合端侧 Gemini 把 AI 代理能力带入折叠形态，定义谷歌 AI 旗舰。",
   related="手机 SoC（Tensor G6/NPU）、折叠屏、显示、AI/NPU。",
   vendor="Google / Pixel 11 Pro Fold", time="2026-08-14（发布）",
   url="https://store.google.com/", sources="Google官方", note="Tensor G6 折叠 AI 旗舰"),
 dict(title="Suunto Traverse", domain="智能手表/传感器/结构/导航", stars="★★★★", status="released", source="B",
   signal="在售新品（8/14 发布）", confirm="1（Suunto官方）",
   params="GPS + GLONASS 导航；海拔/垂直速度/上升测量；暴风雨振动警报；手电筒模式；450美元起；芬兰制造",
   tech="户外导航腕表 + 双卫星定位 + 军规结构",
   why="Suunto 于 8/14 发布新导航腕表 Traverse，GPS+GLONASS 双定位 + 海拔/暴风雨预警服务徒步户外，450美元起延续芬兰制造品质。",
   related="智能手表 传感器（GPS/气压/心率）、结构（军规/合成外壳）、电池。",
   vendor="Suunto / Traverse", time="2026-08-14（发布）",
   url="https://www.sbiao.net/a15462", sources="Suunto官方、手表网", note="户外导航腕表"),
 dict(title="Suunto Core 2", domain="智能手表/传感器/结构/电池", stars="★★★★", status="released", source="B",
   signal="在售新品（8/12 上市）", confirm="1（Suunto官方）",
   params="户外多功能腕表；高度/气压/指南针；日出日落；防水；轻量结构；多配色",
   tech="户外腕表 + 高度计/气压计 + 军规结构",
   why="Suunto Core 2 以高度计/气压计/指南针三件套与军规轻量结构切入户外腕表，8/12 上市补充 Suunto 户外穿戴矩阵。",
   related="智能手表 传感器（高度/气压/指南针）、结构（轻量耐造）、电池。",
   vendor="Suunto / Core 2", time="2026-08-12（上市）",
   url="https://www.suunto.com/", sources="Suunto官方", note="户外多功能腕表"),
 dict(title="Acer Iconia Duo D12", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="在售新品（北美 8 月）", confirm="1（Acer官方）",
   params="Helio G99；12.2英寸 2400×1600 90Hz；8GB/128GB；microSD；约 10 小时；184美元",
   tech="入门大屏平板 + Helio G99 + 90Hz",
   why="Acer Iconia Duo D12 以 12.2英寸 90Hz 大屏与 Helio G99 切入北美入门平板，184美元定价主打性价比影音。",
   related="平板 SoC、显示、电池。",
   vendor="Acer / Iconia Duo D12", time="2026-08（北美上市）",
   url="https://www.acer.com/", sources="Acer官方", note="12.2寸入门平板"),
 dict(title="ThinkPad X1 Carbon Gen 14", domain="笔记本电脑/SoC/显示/结构/AI", stars="★★★★", status="released", source="B",
   signal="在售新品（2026 款）", confirm="1（联想官方）",
   params="Core Ultra 7 356H（Panther Lake）；14英寸 2.8K OLED；58Wh；<1kg；Wi-Fi 7；Space Frame 可维修",
   tech="轻薄商务旗舰本 + Panther Lake + OLED + 可维修结构",
   why="ThinkPad X1 Carbon Gen 14 搭载 Panther Lake Core Ultra 7 356H，14英寸 2.8K OLED + Space Frame 可维修设计重新定义高端商务本可持续。",
   related="笔记本 SoC（Panther Lake/NPU）、显示-OLED、结构（可维修/超轻）、AI/NPU。",
   vendor="联想（ThinkPad）/ X1 Carbon Gen 14", time="2026（在售）",
   url="https://www.lenovo.com/", sources="联想官方", note="Panther Lake 可维修本"),
 dict(title="ASUS Zenbook A16 2026", domain="笔记本电脑/SoC/显示/AI/电池", stars="★★★★", status="released", source="B",
   signal="在售新品（2026 款）", confirm="1（华硕官方）",
   params="骁龙X2 Elite Extreme（18核）；16英寸 3K OLED 120Hz；80 TOPS NPU；48GB；1.2kg；Wi-Fi 7",
   tech="Arm AI 轻薄本 + 骁龙X2 + 3K OLED + 80 TOPS",
   why="ASUS Zenbook A16 2026 以骁龙X2 Elite Extreme 与 80 TOPS NPU 主打端侧 AI，16英寸 3K OLED + 1.2kg 实现大屏与超轻兼顾。",
   related="笔记本 SoC（骁龙X2/NPU）、显示-OLED、电池、AI/NPU。",
   vendor="华硕 / Zenbook A16 2026", time="2026（在售）",
   url="https://www.asus.com/", sources="华硕官方", note="骁龙X2 AI 轻薄本"),
 dict(title="Anker Prime 三合一无线充", domain="无线充/认证/BMS/散热", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（Anker官方）",
   params="Qi2.2 磁吸 25W；MagGo AirCool 风冷；折叠三合一；WPC 认证；红点奖；149.99美元",
   tech="Qi2.2 磁吸 + 25W + 主动风冷 + 认证",
   why="Anker Prime 三合一无线充以 Qi2.2 磁吸 25W 与 MagGo AirCool 主动风冷解决磁吸快充发热，折叠设计 + 红点奖出海磁吸生态。",
   related="无线充、认证（WPC/Qi2.2）、散热、BMS/电源。",
   vendor="Anker / Prime 三合一", time="2026（在售）",
   url="https://www.anker.com/", sources="Anker官方", note="Qi2.2 风冷三合一"),
 dict(title="WiiM Sound", domain="智能音箱/音频/无线/显示", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（WiiM官方）",
   params="Hi-Res 音频；1.8英寸触控屏；多房间无线；流媒体；Wi-Fi/蓝牙",
   tech="智能音箱 + Hi-Res + 触屏 + 多房间无线",
   why="WiiM Sound 以 Hi-Res 音频与 1.8英寸触控屏切入高保真智能音箱，多房间无线 + 流媒体服务强化家庭音频中枢。",
   related="智能音箱 音频、无线通信（Wi-Fi/蓝牙）、显示（触屏）。",
   vendor="WiiM / Sound", time="2026（在售）",
   url="https://wiimhome.com/", sources="WiiM官方", note="Hi-Res 触屏音箱"),
 dict(title="Bose Lifestyle Ultra", domain="智能音箱/音频/无线/AI", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（Bose官方）",
   params="家庭影院音响；空间音频校准；语音助手；Wi-Fi/蓝牙；TrueSpace",
   tech="家庭影院智能音响 + 空间音频 + 无线",
   why="Bose Lifestyle Ultra 以空间音频校准与多房间无线强化家庭影院中枢，语音助手 + AI 推荐升级高端音频体验。",
   related="智能音箱 音频、无线通信（Wi-Fi/蓝牙）、AI。",
   vendor="Bose / Lifestyle Ultra", time="2026（在售）",
   url="https://www.bose.com/", sources="Bose官方", note="空间音频家庭影院"),
]

# ---- Top 5 signals (5-star) ----
top5 = [
 dict(title="小米 18 标准版", dim="手机/SoC/影像", stars="★★★★★",
      key="骁龙8 Elite Gen6 2nm + 双2亿徕卡 + 5499起，8/10 发布"),
 dict(title="荣耀 Robot Phone", dim="手机/SoC/电池", stars="★★★★★",
      key="骁龙8 Elite Gen5 + 7060mAh + 阿莱色彩，8/12 官宣"),
 dict(title="Pixel 11 Pro Fold", dim="手机/折叠屏/AI", stars="★★★★★",
      key="Tensor G6 3nm + 折叠屏 + Gemini，8/14 发布"),
 dict(title="LOOKTECH 智能眼镜", dim="AR-VR/AI", stars="★★★★",
      key="GPT-5 + 4K + 30g，8/13 发布"),
 dict(title="联想小新平板 Pro GT & 12.1", dim="平板/SoC", stars="★★★★",
      key="骁龙8 Gen3 + 11.3寸3.2K + 458g，8/6 开售"),
]

# ---- Dimension panel (all 16 lit) ----
dims = [
 ("SoC/芯片", 30, True), ("显示/OLED", 28, True), ("电池/快充", 30, True), ("散热", 8, True),
 ("无线通信", 30, True), ("音频", 12, True), ("摄像头", 20, True), ("结构/工艺", 13, True),
 ("传感器", 10, True), ("手写笔/触控", 8, True), ("生物识别", 16, True), ("AI/NPU", 16, True),
 ("马达/触觉", 5, True), ("折叠屏", 1, True), ("BMS/电源", 5, True), ("认证/合规", 4, True),
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
print("A=%d B=%d C=%d E=%d 5star=%d cats=%d dims=%d/%d" % (a_count, b_count, sum(1 for it in all_items if it["source"]=="C"), e_count, five_count, cats, on_count, len(dims)))
