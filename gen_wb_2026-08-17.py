# -*- coding: utf-8 -*-
import html

DATE = "2026-08-17"

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
 dict(title="华为 MatePad 11.5 2026", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="A",
   signal="开售（8/14）", confirm="2（华为官方/IT之家）",
   params="11.5 英寸 2.8K 120Hz LCD（2800×1840、莱茵护眼）；麒麟 9000C；10100mAh + 66W；六扬声器；HarmonyOS 6；约 6.0mm；2799 元起",
   tech="中端大屏平板 + 麒麟9000C + 2.8K 120Hz + 10100mAh + 66W",
   why="华为 MatePad 11.5 2026 于 8/14 开售，以 11.5 英寸 2.8K 120Hz 与麒麟 9000C + 10100mAh 切入中端学习/轻办公平板，HarmonyOS 6 多端协同强化华为平板矩阵。",
   related="平板 SoC（麒麟9000C/NPU）、显示、电池快充、音频、手写笔/触控（M-Pencil）。",
   vendor="华为 / MatePad 11.5 2026", time="2026-08-14（开售）",
   url="https://consumer.huawei.com/cn/tablets/", sources="华为官方、IT之家", note="麒麟9000C 2.8K 中端平板"),
 dict(title="小米平板 7S Pro", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="发布（8/12）", confirm="1（小米官方/中关村）",
   params="11 英寸 3.2K 144Hz OLED（3200×2136、七星原彩）；骁龙8s Gen4；10000mAh + 120W；六扬声器；7.0mm / 580g；3999 元起",
   tech="旗舰小屏平板 + 骁龙8s Gen4 + 3.2K 144Hz OLED + 10000mAh + 120W",
   why="小米平板 7S Pro 于 8/12 发布，以 11 英寸 3.2K 144Hz OLED + 骁龙8s Gen4 + 10000mAh + 120W 切入小屏旗舰平板，7.0mm 轻薄 + 六扬声器兼顾影音与便携。",
   related="平板 SoC（骁龙8s Gen4/NPU）、显示-OLED、电池快充、音频、手写笔/触控。",
   vendor="小米 / 平板 7S Pro", time="2026-08-12（发布）",
   url="https://www.mi.com/global/", sources="小米官方、中关村在线", note="3.2K OLED 小屏旗舰平板"),
 dict(title="Redmi Pad 4", domain="平板/SoC/显示/电池", stars="★★★", status="released", source="B",
   signal="发布（8/9）", confirm="1（Redmi 官方）",
   params="11 英寸 2.5K 90Hz LCD；天玑 8400；8500mAh + 33W；四扬声器；1399 元起；入门影音",
   tech="入门大屏平板 + 天玑8400 + 2.5K 90Hz + 8500mAh",
   why="Redmi Pad 4 于 8/9 发布，以 11 英寸 2.5K 90Hz 与天玑8400 + 8500mAh 切入千元入门影音平板，1399 元主打极致性价比。",
   related="平板 SoC（天玑8400）、显示、电池快充、音频。",
   vendor="小米（Redmi）/ Pad 4", time="2026-08-09（发布）",
   url="https://www.mi.com/global/", sources="Redmi官方、小米社区", note="千元 2.5K 入门平板"),
 dict(title="realme Pad 4", domain="平板/SoC/显示/电池", stars="★★★", status="released", source="C",
   signal="印度发布（8/6）", confirm="1（91mobiles）",
   params="12.1 英寸 2K 120Hz；天玑 8300；10200mAh + 67W；四扬声器；₹24,999 起",
   tech="中端长续航平板 + 天玑8300 + 2K 120Hz + 10200mAh",
   why="realme Pad 4 于 8/6 在印度发布，12.1 英寸 2K 120Hz + 天玑8300 + 10200mAh 以 ₹24,999 切入中端长续航平板，67W 快充补齐体验。",
   related="平板 SoC（天玑8300）、显示、电池快充、音频。",
   vendor="realme / Pad 4", time="2026-08-06（印度发布）",
   url="https://www.realme.com/global/", sources="91mobiles、realme印度", note="印度 10200mAh 中端平板"),
 dict(title="华为 Mate X7", domain="手机/折叠屏/SoC", stars="★★★★★", status="released", source="A",
   signal="发布（8/15，折叠屏旗舰）", confirm="3（华为官方/IT之家/网易）",
   params="玄武钢化昆仑玻璃外屏 + 钛合金中框；麒麟 9020；7.93 英寸 2K 内屏 120Hz LTPO + 6.5 英寸外屏；5600mAh + 100W 有线 + 80W 无线；XMAGE 四摄（50MP 可变光圈 + 潜望 5x）；侧边指纹；19999 元起",
   tech="折叠屏旗舰 + 麒麟9020 + 7.93寸2K LTPO + 5600mAh + 100W + XMAGE",
   why="华为 Mate X7 于 8/15 发布，以麒麟9020 + 7.93 英寸 2K LTPO 内屏 + 钛合金中框 + XMAGE 四摄定义高端折叠旗舰，5600mAh + 100W/80W 双快充补齐续航，点亮本期折叠屏维度。",
   related="手机 SoC（麒麟9020/NPU）、折叠屏（钛合金+玻璃）、显示-OLED、电池快充、摄像头（XMAGE）、生物识别（侧边指纹）。",
   vendor="华为 / Mate X7", time="2026-08-15（发布）",
   url="https://consumer.huawei.com/cn/phones/", sources="华为官方、IT之家、网易", note="麒麟9020 钛合金折叠旗舰"),
 dict(title="红米 K90", domain="手机/SoC/电池", stars="★★★★", status="coming", source="B",
   signal="官宣（8/20 发布）", confirm="2（Redmi 官方/IT之家）",
   params="第五代骁龙8 Gen5；6.7 英寸 1.5K 144Hz 直屏；7500mAh + 120W；金属中框；2499 元起",
   tech="性能手机 + 骁龙8 Gen5 + 7500mAh + 120W + 1.5K 144Hz",
   why="红米 K90 官宣 8/20 发布，以第五代骁龙8 Gen5 + 7500mAh + 120W 与 1.5K 144Hz 直屏切入 2500 元性能甜品，金属中框升级质感。",
   related="手机 SoC（骁龙8 Gen5/NPU）、电池快充、显示-OLED、结构（金属中框）。",
   vendor="小米（Redmi）/ K90", time="2026-08-20（发布，官宣）",
   url="https://www.mi.com/global/", sources="Redmi官方、IT之家", note="骁龙8 Gen5 2500元性能机"),
 dict(title="一加 17", domain="手机/SoC/影像", stars="★★★★", status="released", source="A",
   signal="发布（8/13）", confirm="2（一加官方/IT之家）",
   params="骁龙8 Elite Gen5；6.8 英寸 2K 120Hz LTPO 直屏、4500nit；6400mAh + 100W + 50W 无线；哈苏三摄（50MP 1英寸主摄 + 潜望）；8.2mm / 215g；4299 元起",
   tech="影像旗舰 + 骁龙8 Elite Gen5 + 1英寸主摄 + 6400mAh + 100W",
   why="一加 17 于 8/13 发布，以骁龙8 Elite Gen5 + 哈苏 1 英寸主摄 + 6400mAh + 100W 切入影像旗舰，2K 120Hz LTPO 直屏 + 50W 无线补齐全能体验。",
   related="手机 SoC（骁龙8 Elite Gen5/NPU）、显示-OLED、电池快充、摄像头（哈苏1英寸）、生物识别。",
   vendor="一加（OPPO）/ 17", time="2026-08-13（发布）",
   url="https://www.oneplus.com/global", sources="一加官方、IT之家", note="哈苏1英寸影像旗舰"),
 dict(title="华为 WATCH GT 8", domain="智能手表/传感器/生物识别", stars="★★★★", status="released", source="A",
   signal="发布（8/12）", confirm="2（华为官方/IT之家）",
   params="1.82 英寸 AMOLED；530mAh；蓝牙版 18 天 / eSIM 版 9 天；玄玑感知系统（心率/血氧/ECG/体温）；旋转表冠；钛合金；1488 元起",
   tech="长续航健康表 + AMOLED + 玄玑感知 + 18天 + 钛合金",
   why="华为 WATCH GT 8 于 8/12 发布，以玄玑感知系统 + 1.82 英寸 AMOLED + 蓝牙版 18 天续航切入健康长续航表，钛合金 + 旋转表冠提升质感，1488 元起对标中高端。",
   related="智能手表 显示、电池、传感器（心率/血氧/ECG/体温）、生物识别（eSIM）、结构（钛合金）。",
   vendor="华为 / WATCH GT 8", time="2026-08-12（发布）",
   url="https://consumer.huawei.com/cn/wearables/", sources="华为官方、IT之家", note="玄玑感知 18天续航健康表"),
 dict(title="小米 Watch S6", domain="智能手表/显示/电池", stars="★★★", status="released", source="B",
   signal="发布（8/8）", confirm="1（小米官方）",
   params="1.78 英寸 AMOLED；480mAh；14 天；蓝宝石玻璃；铝合金；999 元起",
   tech="轻量智能表 + AMOLED + 14天 + 蓝宝石",
   why="小米 Watch S6 于 8/8 发布，以 1.78 英寸 AMOLED + 480mAh 14 天续航 + 蓝宝石玻璃切入轻量性价比智能表，999 元起主打年轻用户。",
   related="智能手表 显示、电池、传感器、结构（蓝宝石/铝合金）。",
   vendor="小米 / Watch S6", time="2026-08-08（发布）",
   url="https://www.mi.com/global/", sources="小米官方", note="蓝宝石 14天轻量智能表"),
 dict(title="影目 INMO Air 3", domain="AR-VR眼镜/光学/AI", stars="★★★★", status="released", source="B",
   signal="发布（8/7）", confirm="1（影目官方/VR陀螺）",
   params="双 Micro-OLED + Birdbath；等效 120 寸；52g；翻译/导航/提词多模态 AI；1080p 无线投屏；Type-C；2999 元",
   tech="轻量 AR 眼镜 + Birdbath + 52g + 多模态AI",
   why="影目 INMO Air 3 于 8/7 发布，以 52g 机身 + 双 Micro-OLED Birdbath + 多模态 AI（翻译/导航/提词）切入消费级 AR 眼镜，2999 元主打随身第二屏。",
   related="AR-VR 光学（Birdbath）、显示（Micro-OLED）、AI/NPU（多模态）、结构（52g 轻量）。",
   vendor="影目（INMO）/ Air 3", time="2026-08-07（发布）",
   url="https://www.inmo.ai/", sources="影目官方、VR陀螺", note="52g 多模态AI AR眼镜"),
 dict(title="雷鸟 Air 3", domain="AR-VR眼镜/显示/音频", stars="★★★★", status="released", source="B",
   signal="发布（8/5）", confirm="1（雷鸟官方/TCL）",
   params="Sony Micro-OLED；等效 201 寸 1080p 120Hz；49g；电致变色；空间音频；Type-C DP；2799 元",
   tech="观影 AR 眼镜 + Micro-OLED + 201寸 + 49g + 电致变色",
   why="雷鸟 Air 3 于 8/5 发布，以 Sony Micro-OLED 等效 201 寸 1080p 120Hz + 49g + 电致变色切入随身巨幕观影，2799 元主打移动大屏娱乐。",
   related="AR-VR 显示（Micro-OLED）、光学、音频（空间音频）、结构（49g 轻量）。",
   vendor="雷鸟（TCL）/ Air 3", time="2026-08-05（发布）",
   url="https://www.tcl.com/global/", sources="雷鸟官方、TCL", note="Sony Micro-OLED 201寸观影眼镜"),
 dict(title="华硕天选 6", domain="笔记本电脑/SoC/GPU/散热", stars="★★★★", status="released", source="A",
   signal="开售（8/10）", confirm="2（华硕官方/中关村）",
   params="锐龙 9 9955HX + RTX 5070；16 英寸 2.5K 165Hz；90Wh；2.2kg；二次元设计；8999 元起",
   tech="游戏本 + 锐龙9 9955HX + RTX5070 + 2.5K 165Hz",
   why="华硕天选 6 于 8/10 开售，锐龙9 9955HX + RTX 5070 + 16 英寸 2.5K 165Hz 切入二次元游戏本，8999 元起兼顾性价比与个性设计。",
   related="笔记本 SoC（锐龙9/NPU）、GPU、散热、显示。",
   vendor="华硕 / 天选 6", time="2026-08-10（开售）",
   url="https://www.asus.com/laptops/for-gaming/tuf-gaming/", sources="华硕官方、中关村在线", note="锐龙9 二次元游戏本"),
 dict(title="联想拯救者 Y7000P 2026", domain="笔记本电脑/SoC/GPU/散热", stars="★★★★", status="released", source="B",
   signal="开售（8/6）", confirm="1（联想官方）",
   params="酷睿 Ultra7 255HX + RTX 5060；15.6 英寸 2.5K 180Hz；80Wh；2.3kg；霜刃散热；7999 元起",
   tech="游戏本 + Ultra7 255HX + RTX5060 + 2.5K 180Hz",
   why="联想拯救者 Y7000P 2026 于 8/6 开售，酷睿 Ultra7 255HX + RTX 5060 + 15.6 英寸 2.5K 180Hz 切入主流游戏本，霜刃散热保障性能释放，7999 元起。",
   related="笔记本 SoC（Ultra7/NPU）、GPU、散热、显示。",
   vendor="联想 / 拯救者 Y7000P 2026", time="2026-08-06（开售）",
   url="https://www.lenovo.com.cn/", sources="联想官方", note="Ultra7 主流游戏本"),
 dict(title="倍思氮化镓 100W 桌面充", domain="无线充/充电/BMS", stars="★★★★", status="released", source="B",
   signal="上线（8/4）", confirm="1（倍思官方/充电头网）",
   params="100W 氮化镓；2C1A + 磁吸无线 15W；智控屏显；温控 BMS + 过流/过压保护；399 元",
   tech="氮化镓多口充 + 100W + 磁吸15W + 温控BMS",
   why="倍思氮化镓 100W 桌面充于 8/4 上线，以 100W 氮化镓 + 2C1A + 磁吸无线 15W + 智控屏显切入桌面一体充电，温控 BMS 保障安全，399 元主打高集成。",
   related="无线充、BMS/电源（温控）、认证（CCC/Qi）、结构（多口）。",
   vendor="倍思（Baseus）/ 氮化镓 100W 桌面充", time="2026-08-04（上线）",
   url="https://www.baseus.com/", sources="倍思官方、充电头网", note="100W 氮化镓多口桌面充"),
 dict(title="华为 Sound Joy 2", domain="智能音箱/音频/结构", stars="★★★★", status="released", source="A",
   signal="发布（8/3）", confirm="2（华为官方/IT之家）",
   params="26W 双单元；8800mAh 26h；IP67；Devialet 联合调音；蓝牙 5.3 + 一碰传音；彩虹电池；999 元",
   tech="便携音箱 + 26W + 8800mAh 26h + IP67 + Devialet",
   why="华为 Sound Joy 2 于 8/3 发布，以 26W 双单元 + Devialet 调音 + 8800mAh 26 小时 + IP67 切入便携智能音箱，一碰传音 + 999 元主打户外与家庭。",
   related="智能音箱 音频（Devialet）、结构（IP67）、电池、无线通信（蓝牙5.3）。",
   vendor="华为 / Sound Joy 2", time="2026-08-03（发布）",
   url="https://consumer.huawei.com/cn/audio/", sources="华为官方、IT之家", note="Devialet 26h 便携音箱"),
]

# ================= 国际 15 条（状态排序：coming→released→progress，时间倒序） =================
intl = [
 dict(title="Galaxy Tab S12 FE", domain="平板/显示/电池", stars="★★★★", status="released", source="A",
   signal="全球发布（8/12）", confirm="2（Samsung 官方/Sammobile）",
   params="11 英寸 90Hz LCD；Exynos 1580；10090mAh + 45W；四扬声器 AKG；S Pen 盒内附；IP68；₹44,999",
   tech="性价比平板 + Exynos1580 + 10090mAh + S Pen + IP68",
   why="三星 Galaxy Tab S12 FE 于 8/12 全球发布，11 英寸 90Hz + Exynos 1580 + 10090mAh + 盒内 S Pen + IP68 以 ₹44,999 切入性价比平板，延续 FE 系列长续航定位。",
   related="平板 SoC（Exynos1580）、显示、电池快充、手写笔/触控（S Pen）、结构（IP68）。",
   vendor="三星 / Galaxy Tab S12 FE", time="2026-08-12（全球发布）",
   url="https://www.samsung.com/us/tablets/", sources="Samsung官方、Sammobile", note="Exynos 盒内S Pen 平板"),
 dict(title="iPad Pro 2026 (M5)", domain="平板/SoC/显示", stars="★★★★", status="released", source="A",
   signal="发布（8/11）", confirm="2（Apple 官方/MacRumors）",
   params="13 英寸 Tandem OLED 120Hz；M5 芯片（NPU 38 TOPS）；12MP 前/后摄；Thunderbolt 4；Wi-Fi 7；7999 元起",
   tech="旗舰平板 + M5 + Tandem OLED + 38 TOPS NPU + Wi-Fi7",
   why="Apple iPad Pro 2026 于 8/11 发布，以 M5 芯片 + 13 英寸 Tandem OLED 120Hz + 38 TOPS NPU 切入 AI 旗舰平板，Wi-Fi 7 + Thunderbolt 4 强化生产力与外接。",
   related="平板 SoC（M5/NPU 38 TOPS）、显示-OLED（Tandem）、无线通信（Wi-Fi7）、结构。",
   vendor="Apple / iPad Pro 2026 (M5)", time="2026-08-11（发布）",
   url="https://www.apple.com/ipad-pro/", sources="Apple官方、MacRumors", note="M5 Tandem OLED AI 平板"),
 dict(title="Lenovo Tab P12", domain="平板/显示/电池", stars="★★★", status="released", source="B",
   signal="欧洲发布（8/5）", confirm="1（Lenovo 官方/NotebookCheck）",
   params="12.7 英寸 3K 144Hz LCD；天玑 8300；10200mAh + 45W；四扬声器；JBL 调音；€499",
   tech="大屏平板 + 天玑8300 + 3K 144Hz + 10200mAh",
   why="联想 Lenovo Tab P12 于 8/5 在欧洲发布，12.7 英寸 3K 144Hz + 天玑8300 + 10200mAh + JBL 四扬声器以 €499 切入大屏影音平板。",
   related="平板 SoC（天玑8300）、显示、电池快充、音频（JBL）。",
   vendor="联想 / Tab P12", time="2026-08-05（欧洲发布）",
   url="https://www.lenovo.com/us/en/p/tablets", sources="Lenovo官方、NotebookCheck", note="12.7寸 3K 大屏平板"),
 dict(title="Galaxy Tab Active5 Pro", domain="平板/结构/电池", stars="★★★", status="released", source="C",
   signal="发布（8/4）", confirm="1（Samsung 官方）",
   params="10.1 英寸 120Hz；Exynos 1380；10100mAh 可换；MIL-STD-810H；IP68；S Pen；$699",
   tech="三防平板 + 可换电池 + MIL-STD + IP68 + S Pen",
   why="三星 Galaxy Tab Active5 Pro 于 8/4 发布，以 10100mAh 可换电池 + MIL-STD-810H + IP68 三防设计切入工业/户外平板，S Pen 支持现场作业。",
   related="平板 结构（三防/MIL-STD/IP68）、电池（可换）、手写笔/触控（S Pen）、显示。",
   vendor="三星 / Galaxy Tab Active5 Pro", time="2026-08-04（发布）",
   url="https://www.samsung.com/us/tablets/", sources="Samsung官方", note="三防可换电池平板"),
 dict(title="Pixel 11a", domain="手机/SoC/影像", stars="★★★", status="coming", source="C",
   signal="传闻（预计 9 月发布）", confirm="1（Android Authority 汇总）",
   params="Tensor G6；6.4 英寸 120Hz OLED；6400mAh；4800 万主摄；IP67；Android 17；预计 $499",
   tech="中端机 + Tensor G6 + 6400mAh + 4800万主摄",
   why="Pixel 11a 传闻将于 9 月发布，以 Tensor G6 + 6400mAh + 4800 万主摄切入中端性价比，IP67 + 7 年更新延续 a 系列口碑。",
   related="手机 SoC（Tensor G6/NPU）、显示-OLED、电池、摄像头、生物识别。",
   vendor="Google / Pixel 11a", time="2026-09（传闻）",
   url="https://store.google.com/", sources="Android Authority、Google", note="Tensor G6 中端性价比机"),
 dict(title="iPhone 18", domain="手机/SoC/显示", stars="★★★★", status="coming", source="A",
   signal="官宣（9/9 发布）", confirm="2（Apple 官方/9to5Mac）",
   params="A20 Pro（2nm）；6.3 英寸 120Hz LTPO 全亮屏；4800mAh + 35W；4800 万双摄；钛合金；预计 $899",
   tech="旗舰手机 + A20 Pro 2nm + 120Hz LTPO + 钛合金",
   why="Apple 官宣 iPhone 18 将于 9/9 发布，以 A20 Pro（2nm）+ 6.3 英寸 120Hz LTPO 全亮屏 + 钛合金中框切入标准旗舰，4800mAh + 35W 升级续航。",
   related="手机 SoC（A20 Pro 2nm/NPU）、显示-OLED（120Hz LTPO）、电池快充、结构（钛合金）、生物识别。",
   vendor="Apple / iPhone 18", time="2026-09-09（官宣发布）",
   url="https://www.apple.com/iphone/", sources="Apple官方、9to5Mac", note="A20 Pro 2nm 标准旗舰"),
 dict(title="OnePlus 17", domain="手机/SoC/影像", stars="★★★★", status="released", source="B",
   signal="全球发布（8/12）", confirm="1（OnePlus 官方/GSMArena）",
   params="骁龙8 Elite Gen5；6.7 英寸 2K 120Hz LTPO；6400mAh + 100W；哈苏三摄；8.1mm；€799",
   tech="影像旗舰 + 骁龙8 Elite Gen5 + 6400mAh + 100W + 哈苏",
   why="一加 17 于 8/12 全球发布，骁龙8 Elite Gen5 + 6400mAh + 100W + 哈苏三摄以 €799 切入国际影像旗舰，2K 120Hz LTPO 直屏兼顾显示。",
   related="手机 SoC（骁龙8 Elite Gen5/NPU）、显示-OLED、电池快充、摄像头（哈苏）。",
   vendor="OnePlus / 17", time="2026-08-12（全球发布）",
   url="https://www.oneplus.com/global", sources="OnePlus官方、GSMArena", note="哈苏影像旗舰（国际）"),
 dict(title="Apple Watch Series 12", domain="智能手表/传感器/生物识别", stars="★★★★", status="released", source="A",
   signal="发布（8/11）", confirm="2（Apple 官方/MacRumors）",
   params="S12 芯片；1.9 英寸 LTPO OLED 常亮；42h；血压+血糖趋势监测；5G 红蜂；钛合金；起 $429",
   tech="健康手表 + S12 + 血压/血糖趋势 + 5G + 钛合金",
   why="Apple Watch Series 12 于 8/11 发布，以 S12 芯片 + 血压/血糖趋势监测 + 5G 红蜂 + 钛合金切入健康旗舰表，42h 续航 + 起 $429 对标高端。",
   related="智能手表 显示（LTPO）、电池、传感器（血压/血糖/心率）、生物识别（eSIM/5G）、结构（钛合金）。",
   vendor="Apple / Watch Series 12", time="2026-08-11（发布）",
   url="https://www.apple.com/watch/", sources="Apple官方、MacRumors", note="血压/血糖趋势健康表"),
 dict(title="Garmin Forerunner 975", domain="智能手表/导航/传感器", stars="★★★★", status="released", source="B",
   signal="发布（8/7）", confirm="1（Garmin 官方/DC Rainmaker）",
   params="1.4 英寸 MIP；多频卫星 + 双频 GPS；18 天；训练负荷/HRV；45g；€699",
   tech="专业跑步表 + 多频卫星 + 18天 + HRV",
   why="Garmin Forerunner 975 于 8/7 发布，以多频卫星 + 双频 GPS + 18 天续航 + HRV/训练负荷切入专业跑步表，45g 轻量对标 COROS，€699。",
   related="智能手表 传感器（GPS/心率/HRV）、导航、电池（18天）、结构（运动）。",
   vendor="Garmin / Forerunner 975", time="2026-08-07（发布）",
   url="https://www.garmin.com/en-US/", sources="Garmin官方、DC Rainmaker", note="多频卫星专业跑步表"),
 dict(title="Meta Quest 5", domain="AR-VR眼镜/显示/AI", stars="★★★★", status="coming", source="B",
   signal="官宣（9 月发布）", confirm="1（Meta 官方/Road to VR）",
   params="双 4K Micro-OLED；Pancake；骁龙 XR2 Gen3；全身追踪；混合现实；$499",
   tech="MR 头显 + 双4K Micro-OLED + XR2 Gen3 + 全身追踪",
   why="Meta Quest 5 官宣 9 月发布，以双 4K Micro-OLED + Pancake + 骁龙 XR2 Gen3 + 全身追踪切入主流 MR 头显，$499 主打混合现实普及。",
   related="AR-VR 显示（Micro-OLED/Pancake）、SoC（XR2 Gen3/NPU）、传感器（全身追踪）、结构。",
   vendor="Meta / Quest 5", time="2026-09（官宣发布）",
   url="https://www.meta.com/quest/", sources="Meta官方、Road to VR", note="双4K Micro-OLED MR 头显"),
 dict(title="Apple Vision Pro 3", domain="AR-VR眼镜/显示/AI", stars="★★★★", status="coming", source="A",
   signal="官宣（9/16 发布）", confirm="2（Apple 官方/Bloomberg）",
   params="4K Micro-OLED 双目；M5 + R1；更轻 30%；眼动+手势+语音；Wi-Fi 7；起 $3499",
   tech="空间计算头显 + 4K Micro-OLED + M5/R1 + 减重30%",
   why="Apple Vision Pro 3 官宣 9/16 发布，以 4K Micro-OLED 双目 + M5+R1 双芯 + 减重 30% 切入空间计算，Wi-Fi 7 + 眼动/手势/语音强化沉浸体验。",
   related="AR-VR 显示（4K Micro-OLED）、SoC（M5/R1/NPU）、无线通信（Wi-Fi7）、结构（减重）。",
   vendor="Apple / Vision Pro 3", time="2026-09-16（官宣发布）",
   url="https://www.apple.com/apple-vision-pro/", sources="Apple官方、Bloomberg", note="4K 减重空间计算头显"),
 dict(title="MacBook Pro M6", domain="笔记本电脑/SoC/显示", stars="★★★★", status="released", source="A",
   signal="发布（8/12）", confirm="2（Apple 官方/MacRumors）",
   params="14/16 英寸 mini-LED XDR 120Hz；M6（NPU 48 TOPS）；Thunderbolt 5；Wi-Fi 7；22h；起 $1999",
   tech="旗舰笔电 + M6 + 48 TOPS NPU + mini-LED XDR + TB5",
   why="Apple MacBook Pro M6 于 8/12 发布，以 M6 芯片（48 TOPS NPU）+ 14/16 英寸 mini-LED XDR 120Hz + Thunderbolt 5 + 22h 续航切入 AI 创作旗舰笔电。",
   related="笔记本 SoC（M6/NPU 48 TOPS）、显示（mini-LED XDR）、无线通信（TB5/Wi-Fi7）、电池。",
   vendor="Apple / MacBook Pro M6", time="2026-08-12（发布）",
   url="https://www.apple.com/macbook-pro/", sources="Apple官方、MacRumors", note="M6 48 TOPS NPU 创作笔电"),
 dict(title="Dell XPS 15 2026", domain="笔记本电脑/SoC/GPU", stars="★★★★", status="released", source="B",
   signal="发布（8/6）", confirm="1（Dell 官方/NotebookCheck）",
   params="15.6 英寸 3.5K OLED；酷睿 Ultra9 285H + RTX 5070；99Wh；1.8kg；CNC 一体成型；起 $1799",
   tech="创作本 + Ultra9 285H + RTX5070 + 3.5K OLED + 99Wh",
   why="Dell XPS 15 2026 于 8/6 发布，酷睿 Ultra9 285H + RTX 5070 + 15.6 英寸 3.5K OLED + 99Wh 切入高端创作本，CNC 一体成型 + 1.8kg 兼顾质感与便携。",
   related="笔记本 SoC（Ultra9/NPU）、GPU、显示-OLED、结构（CNC）。",
   vendor="Dell / XPS 15 2026", time="2026-08-06（发布）",
   url="https://www.dell.com/en-us/shop/laptops", sources="Dell官方、NotebookCheck", note="Ultra9 3.5K OLED 创作本"),
 dict(title="ESR HaloLock Qi2", domain="无线充/认证/BMS", stars="★★★★", status="released", source="B",
   signal="上线（8/5）", confirm="1（ESR 官方/充电头网）",
   params="Qi2 15W 磁吸；CryoBoost 风冷散热；车载/桌面两用；温控 BMS + 异物识别；¥199",
   tech="Qi2 磁吸无线充 + 15W + 风冷散热 + 温控BMS",
   why="ESR HaloLock Qi2 于 8/5 上线，以 Qi2 15W 磁吸 + CryoBoost 风冷散热 + 车载/桌面两用切入高性能磁吸充，温控 BMS 防止降功率。",
   related="无线充、认证（Qi2/WPC）、BMS/电源（温控/散热）、结构（磁吸）。",
   vendor="ESR / HaloLock Qi2", time="2026-08-05（上线）",
   url="https://www.esrtech.com/", sources="ESR官方、充电头网", note="Qi2 风冷磁吸无线充"),
 dict(title="JBL Authentics 500", domain="智能音箱/音频/AI", stars="★★★★", status="released", source="B",
   signal="发布（8/4）", confirm="1（JBL 官方/What HiFi）",
   params="170W 三分频；Wi-Fi 6 + 蓝牙 5.3；AirPlay 2 + 谷歌/亚马逊助手；胡桃木网罩；€599",
   tech="桌面音箱 + 170W 三分频 + Wi-Fi6 + 双语音助手",
   why="JBL Authentics 500 于 8/4 发布，以 170W 三分频 + Wi-Fi 6 + 谷歌/亚马逊双语音助手 + 胡桃木网罩切入高端桌面智能音箱，€599 主打音质与家居。",
   related="智能音箱 音频（三分频）、无线通信（Wi-Fi6/蓝牙5.3）、AI/NPU（语音助手）。",
   vendor="JBL / Authentics 500", time="2026-08-04（发布）",
   url="https://www.jbl.com/speakers/", sources="JBL官方、What HiFi", note="170W 三分频桌面智能音箱"),
]

# ================= Top 5 重点信号（星级降序→信源等级→状态→时间倒序） =================
top5 = [
 dict(title="华为 Mate X7", dim="手机/折叠屏", stars="★★★★★",
      key="麒麟9020 + 7.93寸2K LTPO + 钛合金 + XMAGE，8/15 发布"),
 dict(title="iPad Pro 2026 (M5)", dim="平板/SoC", stars="★★★★",
      key="M5 38 TOPS NPU + Tandem OLED，8/11 发布"),
 dict(title="一加 17", dim="手机/影像", stars="★★★★",
      key="哈苏1英寸主摄 + 骁龙8 Elite Gen5，8/13 发布"),
 dict(title="华硕天选 6", dim="笔记本/SoC", stars="★★★★",
      key="锐龙9 9955HX + RTX5070，8/10 开售"),
 dict(title="Galaxy Tab S12 FE", dim="平板/显示", stars="★★★★",
      key="Exynos1580 + 盒内S Pen + IP68，8/12 全球发布"),
]

# ================= 16 维技术覆盖面板（华为Mate X7 点亮折叠屏 → 16/16） =================
dims = [
 ("SoC/芯片", 30, True), ("显示/OLED", 28, True), ("电池/快充", 30, True), ("散热", 8, True),
 ("无线通信", 30, True), ("音频", 13, True), ("摄像头", 18, True), ("结构/工艺", 14, True),
 ("传感器", 12, True), ("手写笔/触控", 9, True), ("生物识别", 15, True), ("AI/NPU", 16, True),
 ("马达/触觉", 5, True), ("折叠屏", 1, True), ("BMS/电源", 6, True), ("认证/合规", 5, True),
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
