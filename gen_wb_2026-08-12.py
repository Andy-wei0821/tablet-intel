# -*- coding: utf-8 -*-
import html

DATE = "2026-08-12"

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

# ---- DOMESTIC (sorted: coming -> released time-desc) ----
cn = [
 dict(title="荣耀 Magic V5 折叠屏", domain="手机/折叠屏/SoC/结构/电池", stars="★★★★★", status="coming", source="A",
   signal="官宣（即将发布）", confirm="1（荣耀官方）",
   params="骁龙8 Elite Gen5；钛金属中框；横向内折；5500mAh；66W",
   tech="横向折叠旗舰 + 钛金属铰链 + 骁龙8至尊版 + 硅碳大电",
   why="荣耀Magic V5以钛金属铰链与轻薄机身切入大折叠旗舰，骁龙8 Elite Gen5+5500mAh，折叠屏赛道再添高端玩家。",
   related="手机 折叠屏、SoC、结构（钛/铰链）、电池快充。",
   vendor="荣耀 / Magic V5 折叠屏", time="2026-09（预计发布）",
   url="https://www.honor.com/cn/", sources="荣耀官方、数码媒体", note="替代 Magic V3 系列，主打轻薄耐久"),
 dict(title="小米 AI 眼镜", domain="AR-VR眼镜/AI/显示/无线通信", stars="★★★★", status="coming", source="B",
   signal="官宣（即将发布）", confirm="1（小米官方预热）",
   params="Micro-OLED；端侧小爱大模型；拍摄/翻译；蓝牙音频",
   tech="轻量AI眼镜 + Micro-OLED + 端侧大模型 + 无线互联",
   why="小米AI眼镜将端侧小爱大模型与拍摄/翻译能力集成到眼镜形态，补齐小米人车家全生态的随身AI入口。",
   related="AR-VR 显示（Micro-OLED）、AI/NPU、音频、无线通信。",
   vendor="小米 / AI 眼镜", time="2026-09（预计发布）",
   url="https://www.mi.com/", sources="小米官方、IT之家", note="对标 Ray-Ban Meta 形态"),
 dict(title="OPPO Pad 6", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="A",
   signal="在售新品", confirm="1（OPPO官方）",
   params="天玑9500s旗舰芯片；3K明眸柔光屏；10420mAh大电池",
   tech="中端全能平板 + 天玑9500s + 3K柔光护眼 + 万级大电",
   why="OPPO Pad 6以天玑9500s与3K柔光屏切入学习/创作平板，10420mAh长续航补全OPPO平板矩阵。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="OPPO / Pad 6", time="2026-08（上市）",
   url="https://www.oppo.com/cn/", sources="OPPO官方", note="3K明眸柔光屏护眼"),
 dict(title="小米 磁吸无线充 2026", domain="无线充/电池/BMS/认证", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（小米官方）",
   params="Qi2.2 磁吸 25W；CCC/Qi2认证；智能温控",
   tech="Qi2.2磁吸 + 25W + BMS电源管理 + 认证合规",
   why="小米磁吸无线充2026支持Qi2.2 25W与CCC认证，磁吸生态补齐，安卓磁吸无线充电普及加速。",
   related="无线充、电池（BMS）、认证（CCC/Qi2）。",
   vendor="小米 / 磁吸无线充 2026", time="2026-08（上市）",
   url="https://www.mi.com/", sources="小米官方、充电头网", note="对标苹果MagSafe磁吸生态"),
 dict(title="天猫精灵 X6 端侧AI", domain="智能音箱/音频/AI/无线", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（天猫精灵官方）",
   params="端侧大模型；Wi-Fi/蓝牙；多模态交互；家居中控",
   tech="端侧AI音箱 + 大模型语音 + 无线互联 + 智能家居中控",
   why="天猫精灵X6以端侧大模型实现本地化AI语音交互，强化阿里智能家居语音入口与多模态控制。",
   related="智能音箱 音频、AI/NPU、无线通信（Wi-Fi/蓝牙）。",
   vendor="天猫精灵（阿里）/ X6 端侧AI", time="2026-08（上市）",
   url="https://www.aligenie.com/", sources="天猫精灵开放平台、阿里", note="AliGenie 端侧AI能力"),
 dict(title="OPPO Find X9s Pro", domain="手机/SoC/影像/结构/摄像头/马达", stars="★★★★★", status="released", source="A",
   signal="在售旗舰", confirm="1（OPPO官方）",
   params="哈苏双2亿影像；第五代骁龙8至尊版；2K直屏；X轴线性马达",
   tech="哈苏双2亿影像旗舰 + 骁龙8至尊版 + 旗舰结构 + 线性马达",
   why="OPPO Find X9s Pro以哈苏双2亿影像与第五代骁龙8至尊版冲击影像旗舰，2亿双摄+线性马达提升拍摄与触感体验。",
   related="手机 SoC、摄像头（影像）、结构、马达/触觉。",
   vendor="OPPO / Find X9s Pro", time="2026-08（发布）",
   url="https://www.oppo.com/cn/", sources="OPPO官方", note="哈苏双2亿主摄+长焦"),
 dict(title="雷鸟 X3 Pro", domain="AR-VR眼镜/显示/AI/摄像头", stars="★★★★★", status="released", source="B",
   signal="在售新品（已开售）", confirm="2（雷鸟官方 + 实测）",
   params="全彩Micro-LED光引擎；衍射光波导；AI多模态；拍摄",
   tech="轻量AR眼镜 + 全彩Micro-LED + 光波导 + 端侧AI",
   why="雷鸟X3 Pro搭载自研全彩Micro-LED光引擎与衍射光波导，消费级AR眼镜在显示亮度与轻量化上再进阶。",
   related="AR-VR 显示（Micro-LED/光波导）、AI/NPU、摄像头。",
   vendor="雷鸟创新 / X3 Pro", time="2026-07（开售）",
   url="https://rayneo.cn/x3pro.html", sources="雷鸟创新官方、实测媒体", note="自研最小全彩Micro-LED光引擎"),
 dict(title="vivo Pad6 Pro", domain="平板/SoC/显示/电池/手写笔/音频", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（vivo官方）",
   params="天玑9400+；12.1英寸2.8K 144Hz；10200mAh；八扬声器",
   tech="大屏高刷平板 + 天玑9400+ + 长续航 + 立体声",
   why="vivo Pad6 Pro以天玑9400+与12.1英寸2.8K 144Hz切入高端平板，10200mAh+八扬声器强化影音生产力。",
   related="平板 SoC、显示、电池、手写笔、音频。",
   vendor="vivo / Pad6 Pro", time="2026-07（上市）",
   url="https://www.vivo.com.cn/", sources="vivo官方", note="与vivo X Fold6 生态协同"),
 dict(title="荣耀平板20", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="A",
   signal="在售新品", confirm="1（荣耀官方）",
   params="骁龙8系；12.1英寸144Hz；10050mAh；手写笔",
   tech="大屏长续航平板 + 骁龙8系 + 高刷 + 手写笔",
   why="荣耀平板20以12.1英寸144Hz与10050mAh切入大屏学习/办公平板，补齐荣耀平板产品梯度。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="荣耀 / 平板20", time="2026-07（上市）",
   url="https://www.honor.com/cn/", sources="荣耀官方", note="荣耀AI终端平板线"),
 dict(title="一加平板 3 Pro", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（一加官方）",
   params="第五代骁龙8至尊版；3.4K 144Hz原彩屏；ColorOS 16",
   tech="旗舰平板 + 骁龙8至尊版 + 3.4K高刷 + 长续航",
   why="一加平板3 Pro首发第五代骁龙8至尊版与3.4K 144Hz原彩屏，冲击安卓旗舰平板性能标杆。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="一加（OnePlus）/ 平板 3 Pro", time="2026-07（上市）",
   url="https://www.oneplus.com/", sources="一加官方", note="ColorOS 16 跨端协同"),
 dict(title="Redmi Pad 2", domain="平板/SoC/显示/电池", stars="★★★", status="released", source="B",
   signal="在售新品", confirm="1（小米官方）",
   params="骁龙7系；11英寸90Hz；8000mAh；千元档",
   tech="入门大屏平板 + 骁龙7系 + 长续航 + 高性价比",
   why="Redmi Pad 2以千元档11英寸与8000mAh切入入门大屏平板，延续Redmi性价比路线覆盖教育/家用。",
   related="平板 SoC、显示、电池。",
   vendor="小米（Redmi）/ Pad 2", time="2026-07（上市）",
   url="https://www.mi.com/", sources="小米官方", note="千元档入门大屏"),
 dict(title="华为 WATCH Fit 4 Pro", domain="智能手表/结构/电池/传感器/生物识别", stars="★★★★", status="released", source="A",
   signal="在售新品", confirm="1（华为官方）",
   params="钛合金/蓝宝石；14天续航；心率/血氧/体温；AMOLED",
   tech="轻量运动健康表 + 钛/蓝宝石 + 长续航 + 多传感器",
   why="华为WATCH Fit 4 Pro采用钛合金与蓝宝石镜面，14天续航+多健康传感器，Fit系列旗舰材质与续航双升级。",
   related="智能手表 结构（钛/蓝宝石）、电池、传感器（心率/血氧/体温）、生物识别。",
   vendor="华为 / WATCH Fit 4 Pro", time="2026-07（上市）",
   url="https://www.huawei.com/cn/", sources="华为官方", note="Fit系列运动健康旗舰"),
 dict(title="小米 Watch 8 Pro", domain="智能手表/显示/电池/传感器", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（小米官方）",
   params="1.5英寸AMOLED；15天续航；心率/血氧；蓝牙通话",
   tech="旗舰运动表 + AMOLED + 长续航 + 健康监测",
   why="小米Watch 8 Pro以1.5英寸AMOLED与15天续航切入安卓运动健康表，完善小米可穿戴高端线。",
   related="智能手表 显示（AMOLED）、电池、传感器（心率/血氧）。",
   vendor="小米 / Watch 8 Pro", time="2026-07（上市）",
   url="https://www.mi.com/", sources="小米官方", note="HyperOS 穿戴生态"),
 dict(title="联想 拯救者 Y9000P 2026", domain="笔记本电脑/SoC/显示/散热/电池", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（联想官方）",
   params="酷睿Ultra9/锐龙9；RTX 50系；2.5K 240Hz；双烤散热",
   tech="高性能游戏本 + 旗舰CPU/GPU + 高刷 + 强散热",
   why="联想拯救者Y9000P 2026搭载酷睿Ultra9/锐龙9与RTX 50系，2.5K 240Hz+双烤散热，主流高性能游戏本标杆。",
   related="笔记本 SoC、显示、散热、电池。",
   vendor="联想（Legion）/ 拯救者 Y9000P 2026", time="2026-07（上市）",
   url="https://www.lenovo.com/", sources="联想官方", note="Legion 冰魄散热系统"),
 dict(title="ROG 幻 16 2026", domain="笔记本电脑/SoC/显示/散热/GPU", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（华硕ROG官方）",
   params="酷睿Ultra9；RTX 5070/5080；2.5K 240Hz OLED；轻薄机身",
   tech="轻薄性能本 + OLED高刷 + 旗舰GPU + 均热板散热",
   why="ROG幻16 2026以OLED 240Hz与RTX 50系在轻薄机身内实现高性能，兼顾创作与游戏。",
   related="笔记本 SoC、显示-OLED、散热、GPU。",
   vendor="华硕ROG / 幻 16 2026", time="2026-07（上市）",
   url="https://rog.asus.com/", sources="华硕ROG官方", note="幻系列轻薄性能定位"),
]

# ---- INTERNATIONAL (sorted: coming -> released time-desc) ----
intl = [
 dict(title="Samsung Galaxy Tab S12", domain="平板/SoC/显示/电池/无线通信", stars="★★★★", status="coming", source="B",
   signal="官宣（即将发布）", confirm="1（三星官方预热）",
   params="骁龙8 Elite Gen5；11/12.4英寸Dynamic AMOLED；10xxxmAh；Wi-Fi 7",
   tech="旗舰平板 + 骁龙8至尊版 + AMOLED + 长续航 + Wi-Fi7",
   why="三星Galaxy Tab S12（标准版）携骁龙8 Elite Gen5与Dynamic AMOLED补齐S12家族，安卓旗舰平板再扩军。",
   related="平板 SoC、显示-OLED、电池、无线通信（Wi-Fi7）。",
   vendor="三星 / Galaxy Tab S12", time="2026-09（预计发布）",
   url="https://www.samsung.com/", sources="三星官方、SamMobile", note="区别于已覆盖的 S12 Ultra/+"),
 dict(title="Galaxy S26 Ultra", domain="手机/SoC/影像/显示/AI/生物识别/摄像头", stars="★★★★★", status="coming", source="B",
   signal="官宣（即将发布）", confirm="2（三星官方 + 媒体）",
   params="骁龙8 Elite Gen5 for Galaxy；2亿主摄；6.9英寸2K 144Hz；Galaxy AI",
   tech="影像旗舰 + 骁龙8至尊版 + 2亿影像 + 屏下指纹 + 端侧AI",
   why="Galaxy S26 Ultra以2亿主摄与骁龙8 Elite Gen5 for Galaxy冲击影像天花板，Galaxy AI深度集成定义安卓旗舰。",
   related="手机 SoC、摄像头（影像）、显示、AI/NPU、生物识别（屏下指纹）。",
   vendor="三星 / Galaxy S26 Ultra", time="2026-09（预计发布）",
   url="https://www.samsung.com/", sources="三星官方、科技媒体", note="S26 FE 已覆盖，Ultra 为新条目"),
 dict(title="iPad Air 2026（M4）", domain="平板/SoC/显示/电池/手写笔/认证", stars="★★★★★", status="released", source="A",
   signal="在售新品（Apple官方）", confirm="1（Apple官方）",
   params="M4芯片；11/13英寸Liquid Retina；Apple Intelligence；Apple Pencil Pro；Wi-Fi 7",
   tech="Apple Silicon M4 + Liquid Retina + Apple Pencil Pro + 智能 + FCC/CE认证",
   why="iPad Air 2026换装M4芯片，11/13英寸Liquid Retina+Apple Pencil Pro，性能与AI能力大幅跃升，中端平板标杆。",
   related="平板 SoC（M4/NPU）、显示、电池、手写笔、认证（FCC/CE）。",
   vendor="Apple / iPad Air（M4）", time="2026（在售）",
   url="https://www.apple.com/ipad-air/", sources="Apple官方", note="从$749；iPadOS 26 Liquid Glass"),
 dict(title="iPhone Air 2026", domain="手机/SoC/显示/结构/生物识别/AI", stars="★★★★★", status="released", source="A",
   signal="在售新品（Apple官方）", confirm="1（Apple官方）",
   params="A19 Pro；6.5英寸ProMotion；钛金属；最薄iPhone；Face ID；Apple Intelligence",
   tech="Apple Silicon + 钛金属超薄结构 + ProMotion + Face ID + 端侧AI",
   why="iPhone Air以钛金属超薄机身与A19 Pro成为苹果最薄iPhone，Pro级性能+Apple Intelligence定义新一代轻旗舰。",
   related="手机 SoC（A19 Pro/NPU）、显示、结构（钛）、生物识别（Face ID）、AI。",
   vendor="Apple / iPhone Air", time="2026（在售）",
   url="https://www.apple.com/iphone/", sources="Apple官方", note="从$999；Sky Blue等多配色"),
 dict(title="Apple Watch SE 3", domain="智能手表/传感器/电池/无线通信", stars="★★★★", status="released", source="A",
   signal="在售新品（Apple官方）", confirm="1（Apple官方）",
   params="S芯片；视网膜显示屏；心率/血氧；18小时+；Wi-Fi/蓝牙",
   tech="入门智能表 + 健康传感器 + 长续航 + 无线互联",
   why="Apple Watch SE 3以$249起覆盖入门健康穿戴，心率/血氧+无线互联，扩大Apple Watch用户基本盘。",
   related="智能手表 传感器（心率/血氧）、电池、无线通信（Wi-Fi/蓝牙）。",
   vendor="Apple / Apple Watch SE 3", time="2026（在售）",
   url="https://www.apple.com/watch/", sources="Apple官方", note="Midnight/Starlight 配色"),
 dict(title="OnePlus Pad 3", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（一加官方）",
   params="骁龙8 Elite；13.2英寸3.4K 144Hz；12140mAh；磁吸键盘",
   tech="旗舰平板 + 骁龙8 Elite + 3.4K高刷 + 超大电池",
   why="OnePlus Pad 3以13.2英寸3.4K 144Hz与12140mAh切入大屏生产力平板，骁龙8 Elite对标iPad Air。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="一加（OnePlus）/ Pad 3", time="2026（上市）",
   url="https://www.oneplus.com/", sources="一加官方", note="国际版旗舰平板"),
 dict(title="Lenovo Yoga Tab Plus 2026", domain="平板/SoC/显示/电池/音频", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（联想官方）",
   params="骁龙8 Gen3；12.7英寸3K 144Hz；10200mAh；六扬声器",
   tech="影音平板 + 高刷大屏 + 长续航 + 六单元音频",
   why="联想Yoga Tab Plus 2026以12.7英寸3K与六扬声器强化影音平板定位，骁龙8 Gen3兼顾性能与能效。",
   related="平板 SoC、显示、电池、音频。",
   vendor="联想 / Yoga Tab Plus 2026", time="2026（上市）",
   url="https://www.lenovo.com/", sources="联想官方", note="Yoga 多形态支架"),
 dict(title="Xiaomi Pad 8 Pro", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（小米官方）",
   params="骁龙8s Gen4；12.4英寸3.2K 144Hz；10000mAh；67W",
   tech="大屏高刷平板 + 骁龙8s + 长续航 + 快充",
   why="Xiaomi Pad 8 Pro以12.4英寸3.2K 144Hz与10000mAh切入国际大屏平板，67W快充补能高效。",
   related="平板 SoC、显示、电池快充。",
   vendor="小米 / Pad 8 Pro（国际）", time="2026（上市）",
   url="https://www.mi.com/global/", sources="小米官方（全球）", note="国际版平板矩阵"),
 dict(title="COROS PACE 4", domain="智能手表/传感器/电池/结构", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（COROS官方）",
   params="1.2英寸MIP/AMOLED；GPS多频；30天续航；钛/复合材质",
   tech="竞技运动表 + 多频GPS + 超长续航 + 轻量结构",
   why="COROS PACE 4以多频GPS与30天续航切入竞技跑步表，轻量结构+精准数据服务耐力运动人群。",
   related="智能手表 传感器（GPS/心率）、电池、结构（轻量）。",
   vendor="COROS（高驰）/ PACE 4", time="2026（上市）",
   url="https://www.coros.com/pace4", sources="COROS官方", note="为耐力运动而生"),
 dict(title="Ray-Ban Meta 智能眼镜 2026", domain="AR-VR眼镜/AI/音频/摄像头/无线通信", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（Ray-Ban/Meta官方）",
   params="拍摄/视频；开放式音频；Meta AI；蓝牙；多镜框",
   tech="轻量AI眼镜 + 拍摄 + 开放式音频 + 端侧Meta AI + 无线",
   why="Ray-Ban Meta智能眼镜2026将拍摄、开放式音频与Meta AI集成到经典镜框，AI穿戴出海与普及加速。",
   related="AR-VR 摄像头、音频、AI/NPU、无线通信（蓝牙）。",
   vendor="Ray-Ban × Meta / Meta 智能眼镜", time="2026（在售）",
   url="https://www.ray-ban.com/", sources="Ray-Ban/Meta官方", note="经典镜框+AI拍摄"),
 dict(title="PICO 4 Ultra MR头显", domain="AR-VR眼镜/显示/SoC/无线/BMS", stars="★★★★", status="released", source="B",
   signal="在售MR头显", confirm="1（PICO官方）",
   params="骁龙XR2 Gen2；双4K+；PICO OS 5；Wi-Fi 7/PCVR；BMS电源管理",
   tech="MR头显 + 骁龙XR2 + 双4K显示 + 无线串流 + 电源管理",
   why="PICO 4 Ultra以骁龙XR2 Gen2与双4K+显示主打混合现实与PCVR串流，字节在XR终端持续投入。",
   related="AR-VR 显示、SoC（XR2）、无线通信、BMS/电源。",
   vendor="字节跳动 PICO / 4 Ultra", time="2026（在售）",
   url="https://www.picoxr.com/", sources="PICO官方", note="PICO OS 5 交互升级"),
 dict(title="Razer Blade 16 2026", domain="笔记本电脑/SoC/显示/散热/GPU", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（雷蛇官方）",
   params="酷睿Ultra9；RTX 5090；16英寸Mini-LED 240Hz；均热板散热",
   tech="旗舰游戏本 + RTX 50系 + Mini-LED高刷 + 强散热",
   why="Razer Blade 16 2026搭载RTX 5090与16英寸Mini-LED 240Hz，旗舰游戏本性能与显示双顶配。",
   related="笔记本 SoC、显示（Mini-LED）、散热、GPU。",
   vendor="Razer / Blade 16 2026", time="2026（上市）",
   url="https://www.razer.com/", sources="雷蛇官方", note="Blade 16/18 系列在售"),
 dict(title="MSI Stealth 16 AI+ 2026", domain="笔记本电脑/SoC/显示/AI/散热", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（微星官方）",
   params="酷睿Ultra9（NPU）；RTX 5070；16英寸2.5K 240Hz；AI+算力",
   tech="轻薄AI本 + NPU + RTX 50系 + 高刷 + 智能散热",
   why="MSI Stealth 16 AI+ 2026以NPU与RTX 5070实现端侧AI算力，轻薄机身兼顾创作与游戏。",
   related="笔记本 SoC（NPU）、显示、AI/NPU、散热。",
   vendor="微星（MSI）/ Stealth 16 AI+ 2026", time="2026（上市）",
   url="https://www.msi.com/", sources="微星官方", note="Copilot+ PC 定位"),
 dict(title="Satechi Qi2.2 磁吸充电器", domain="无线充/认证/散热/BMS", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（Satechi官方）",
   params="Qi2.2 磁吸 25W；WPC认证；主动散热；BMS温控",
   tech="Qi2.2磁吸 + 25W + WPC认证 + 主动散热 + 电源管理",
   why="Satechi Qi2.2磁吸充电器通过WPC Qi2.2认证，25W+主动散热，海外磁吸无线充生态再添新品。",
   related="无线充、认证（WPC/Qi2.2）、散热、BMS/电源。",
   vendor="Satechi / Qi2.2 磁吸充电器", time="2026（上市）",
   url="https://satechi.com/", sources="Satechi官方、充电头网", note="Qi2.2 25W 磁吸生态"),
 dict(title="Sonos 智能音箱 2026", domain="智能音箱/音频/无线/AI", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（Sonos官方）",
   params="Wi-Fi/蓝牙；Trueplay调音；空间音频；Sonos Radio AI",
   tech="智能音箱 + 多房间无线 + Trueplay + 空间音频 + AI电台",
   why="Sonos 2026智能音箱以Trueplay与空间音频强化无线多房间音频，Sonos Radio引入AI推荐，家庭音频中枢升级。",
   related="智能音箱 音频、无线通信（Wi-Fi/蓝牙）、AI。",
   vendor="Sonos / 智能音箱 2026", time="2026（在售）",
   url="https://www.sonos.com/", sources="Sonos官方", note="Trueplay 房间校准"),
]

# ---- Top 5 signals (5-star, sorted: stars desc -> source asc -> status -> time) ----
top5 = [
 dict(title="iPad Air 2026（M4）", dim="平板/SoC/显示/电池", stars="★★★★★",
      key="M4芯片+11/13寸Liquid Retina+Apple Pencil Pro，在售"),
 dict(title="iPhone Air 2026", dim="手机/SoC/显示/结构", stars="★★★★★",
      key="A19 Pro+钛金属超薄+Face ID，最薄iPhone在售"),
 dict(title="OPPO Find X9s Pro", dim="手机/SoC/影像/结构", stars="★★★★★",
      key="哈苏双2亿+骁龙8至尊版，8月发布"),
 dict(title="Galaxy S26 Ultra", dim="手机/SoC/影像/AI", stars="★★★★★",
      key="2亿主摄+骁龙8至尊版+Galaxy AI，9月预计"),
 dict(title="雷鸟 X3 Pro", dim="AR-VR/显示/AI", stars="★★★★★",
      key="全彩Micro-LED+光波导，7月开售"),
]

# ---- Dimension panel (all 16 lit) ----
dims = [
 ("SoC/芯片", 17, True), ("显示/OLED", 17, True), ("电池/快充", 17, True), ("散热", 5, True),
 ("无线通信", 7, True), ("音频", 5, True), ("摄像头", 4, True), ("结构/工艺", 6, True),
 ("传感器", 4, True), ("手写笔/触控", 5, True), ("生物识别", 3, True), ("AI/NPU", 8, True),
 ("马达/触觉", 1, True), ("折叠屏", 1, True), ("BMS/电源", 3, True), ("认证/合规", 3, True),
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
print("A=%d B=%d E=%d 5star=%d cats=%d dims=%d/%d" % (a_count, b_count, e_count, five_count, cats, on_count, len(dims)))
