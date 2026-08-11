# -*- coding: utf-8 -*-
import html

DATE = "2026-08-11"

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
 dict(title="华为 MatePad Pro 12英寸", domain="平板/SoC/显示/电池/手写笔", stars="★★★★★", status="released", source="A",
   signal="发布会新品（已上市）", confirm="1（华为官方发布会）",
   params="12英寸柔性OLED 144Hz；麒麟T93；鸿蒙6.1；10400mAh硅负极；4.70mm/439g；5999元起",
   tech="超轻薄大屏旗舰 + 麒麟T93 + 鸿蒙6.1 + 10400mAh长续航 + 北斗卫星通讯 + 星闪",
   why="华为MatePad Pro 12英寸以439g/4.7mm刷新10英寸以上最轻平板纪录，10400mAh成华为史上续航最长平板，麒麟T93+鸿蒙6.1+卫星通讯切入高端生产力。",
   related="平板 SoC、显示-OLED、电池快充、手写笔、结构（云隼架构/凝光工艺）、无线通信（星闪/北斗）。",
   vendor="华为 / MatePad Pro 12英寸", time="2026-08-05（发布）",
   url="https://new.qq.com/rain/a/20260805A0B9G800", sources="华为终端、IT之家、腾讯新闻", note="悦享款5699元起；柔光版+凝光工艺最高9199元"),
 dict(title="小米平板9 Pro", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="coming", source="B",
   signal="3C认证（即将发布）", confirm="2（3C认证 + 小白测评）",
   params="骁龙8 Gen5；11.16英寸3.2K LCD高刷；9720mAh；67W有线；代号吉他",
   tech="中高端全能平板 + 骁龙8系 + 大电池 + 67W快充",
   why="小米平板9 Pro通过3C认证，搭载骁龙8 Gen5与9720mAh大电池，定位学习/办公/游戏综合场景，补全小米平板旗舰矩阵。",
   related="平板 SoC、显示、电池快充、手写笔/触控。",
   vendor="小米 / 平板9 Pro", time="2026-08-03（3C认证）",
   url="https://www.mi.com/", sources="国家3C认证、百度百科、网易、gizmochina", note="与小米8S Pro同批认证，预计与小米18系列同台亮相"),
 dict(title="小米平板8S Pro", domain="平板/SoC/显示/电池/快充", stars="★★★★★", status="coming", source="B",
   signal="3C认证（即将发布）", confirm="2（3C认证 + gizmochina）",
   params="自研玄戒O3（台积电3nm）；12.5英寸3.2K LCD；12000mAh；120W；HyperOS 4",
   tech="自研玄戒O3芯片 + 120W百瓦快充 + 12000mAh大电 + 3.2K高刷",
   why="小米平板8S Pro首发自研玄戒O3处理器，120W快充+12000mAh，标志小米平板核心算力自研落地，冲击高端。",
   related="平板 SoC（自研）、显示、电池快充、AI/NPU。",
   vendor="小米 / 平板8S Pro", time="2026-08-03（3C认证）",
   url="https://www.mi.com/", sources="国家3C认证、机锋网、gizmochina", note="M367FC型号；前置32MP/后置50MP；澎湃OS 4（Android 17）"),
 dict(title="华为 MatePad SE 11英寸 焕新版", domain="平板/SoC/显示/电池", stars="★★★", status="released", source="A",
   signal="在售新品（2026年7月）", confirm="1（华为VMall官方）",
   params="骁龙685；11英寸1920×1200；7700mAh；HarmonyOS 4.2；1999元",
   tech="高刷护眼全面屏 + 全金属一体机身 + 鸿蒙教育生态",
   why="华为MatePad SE 11英寸焕新版2026年7月上市，1999元档切入入门大屏平板，全金属机身+鸿蒙教育中心，覆盖学生与家用。",
   related="平板 SoC、显示、电池、认证（莱茵护眼）。",
   vendor="华为 / MatePad SE 11英寸焕新版", time="2026年7月（上市）",
   url="https://www.vmall.com/product/comdetail/index.html?prdId=10086426290126&sbomCode=2701010132701", sources="华为VMall商城", note="星云灰/星海蓝；多屏协同/平行视界/智慧多窗"),
 dict(title="REDMI K100 Pro Max", domain="手机/SoC/影像/电池/快充/马达", stars="★★★★★", status="coming", source="B",
   signal="官宣发布（今日）", confirm="2（REDMI官方 + 科技小南）",
   params="第五代骁龙8至尊版；185Hz高刷；2亿像素；8500-9000mAh；120W；Bose独立2.1声道；X轴线性马达",
   tech="第五代骁龙8至尊版 + 2亿影像 + 近9000mAh大电 + 120W + X轴线性马达",
   why="REDMI K100 Pro Max定档8月11日发布，第五代骁龙8至尊版+2亿像素+近9000mAh电池，Redmi性能影像旗舰再进阶。",
   related="手机 SoC、影像、电池快充、马达/触觉、音频（Bose）。",
   vendor="小米（REDMI）/ K100 Pro Max", time="2026-08-11（发布）",
   url="https://www.mi.com/", sources="REDMI官方、科技小南微博", note="深红色；一体化金属Deco"),
 dict(title="iQOO Neo11至尊版", domain="手机/SoC/显示/电池", stars="★★★★", status="coming", source="B",
   signal="官宣（即将发布）", confirm="1（iQOO官方预热）",
   params="天玑9500；2K屏；9100mAh；预计8月18日发布",
   tech="天玑9500旗舰芯 + 2K高刷 + 9100mAh大电",
   why="iQOO Neo11至尊版搭载天玑9500与9100mAh电池，主打性能与续航双优，Neo系列年度至尊款。",
   related="手机 SoC、显示、电池快充。",
   vendor="vivo（iQOO）/ Neo11至尊版", time="2026-08-18（预计发布）",
   url="https://www.iqoo.com/", sources="iQOO官方预热、头条号", note="对标同档性能旗舰"),
 dict(title="vivo X Fold6", domain="手机/折叠屏/SoC/电池/无线充", stars="★★★★★", status="released", source="B",
   signal="已上市（折叠旗舰）", confirm="2（vivo官方 + 头条号）",
   params="天玑9500；7999元起；7000mAh；80W有线 + 40W无线；折叠屏",
   tech="横向折叠屏 + 天玑9500 + 7000mAh硅碳 + 80W/40W双快充",
   why="vivo X Fold6以7999元起切入大折叠旗舰，天玑9500+7000mAh+40W无线，折叠屏赛道主流化再进一步。",
   related="手机 折叠屏、SoC、电池快充、无线充、结构（铰链）。",
   vendor="vivo / X Fold6", time="2026-06-26（发布）/ 07-15（开售）",
   url="https://www.vivo.com.cn/", sources="vivo官方、中国青年网", note="横向内折；大屏多任务"),
 dict(title="华为 WATCH GT 7 Pro", domain="智能手表/结构/电池/传感器", stars="★★★★", status="released", source="A",
   signal="发布会新品", confirm="1（华为官方）",
   params="钛合金 + 纳米微晶陶瓷；21天续航；2688元",
   tech="旗舰运动健康表 + 钛合金/陶瓷机身 + 长续航",
   why="华为WATCH GT 7 Pro采用钛合金+纳米微晶陶瓷，21天续航，GT系列旗舰材质与续航双升级。",
   related="智能手表 结构（钛/陶瓷）、电池、传感器（心率/血氧）。",
   vendor="华为 / WATCH GT 7 Pro", time="2026-08-05",
   url="https://www.huawei.com/cn/", sources="华为官方、数码媒体", note="同期 GT 7 1588元起"),
 dict(title="华为 WATCH GT 7", domain="智能手表/电池/传感器", stars="★★★", status="released", source="B",
   signal="发布会新品", confirm="1（华为官方）",
   params="1588元起；GT系列标准旗舰；健康监测",
   tech="标准旗舰运动表 + 健康传感器 + 长续航",
   why="华为WATCH GT 7以1588元起覆盖主流运动健康表，完善GT 7系列价位梯度。",
   related="智能手表 电池、传感器（心率/血氧/睡眠）。",
   vendor="华为 / WATCH GT 7", time="2026-08-05",
   url="https://www.huawei.com/cn/", sources="华为官方、数码媒体", note="与 GT 7 Pro 同台"),
 dict(title="华硕无畏Pro14/16 2026", domain="笔记本/SoC/显示/AI/电池", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（华硕官方）",
   params="锐龙AI9 H465 / 酷睿Ultra7 356H；OLED；80W；50TOPS NPU",
   tech="轻薄全能本 + OLED高刷 + 50TOPS NPU + 长续航",
   why="华硕无畏Pro14/16 2026搭载锐龙AI9/酷睿Ultra7与50TOPS NPU，OLED屏+80W，主流轻薄AI生产力。",
   related="笔记本 SoC、显示-OLED、AI/NPU、电池。",
   vendor="华硕 / 无畏Pro14/16 2026", time="2026-08-09",
   url="https://www.asus.com.cn/", sources="华硕官方、新浪", note="双平台（AMD/Intel）"),
 dict(title="华硕灵耀14 Air 2026", domain="笔记本/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="新品开售", confirm="1（华硕官方）",
   params="轻薄OLED；预约7-26/开售7-29；长续航",
   tech="轻量长续航 + OLED + 高便携",
   why="华硕灵耀14 Air 2026以轻薄OLED与长续航切入高端轻薄本，主打随身创作与移动办公。",
   related="笔记本 SoC、显示-OLED、电池。",
   vendor="华硕 / 灵耀14 Air 2026", time="2026-07-26（预约）/ 07-29（开售）",
   url="https://www.asus.com.cn/", sources="华硕官方", note="灵耀系列轻盈线"),
 dict(title="影目 INMO Go 2", domain="AR-VR/AI/显示/音频", stars="★★★★", status="released", source="B",
   signal="已上市（翻译眼镜）", confirm="2（成都AI+AR大会 + 实测）",
   params="阵列光波导；40+语种/90+口音；离线翻译；独立安卓；3999元（首发3299）",
   tech="轻量翻译AR眼镜 + 光波导显示 + 实时AI翻译 + 离线引擎",
   why="影目INMO Go 2全球首款商务翻译眼镜，40+语种实时翻译+离线可用，AR眼镜从信息提示走向实用跨语言沟通。",
   related="AR-VR 显示（光波导）、AI/NPU、音频（骨传导）。",
   vendor="影目科技 / INMO Go 2", time="2026（成都AI+AR大会发布）",
   url="https://www.sohu.com/a/1056507448_122645258", sources="影目官方、微博、搜狐实测", note="普通眼镜形态；不漏光"),
 dict(title="雷鸟 GT系列", domain="AR-VR/显示/音频", stars="★★★★", status="released", source="B",
   signal="新品发布", confirm="1（雷鸟创新夏季发布会）",
   params="1899元起；等效267英寸巨幕；全球首款完整支持杜比视界播放的AR眼镜套组",
   tech="AR观影眼镜 + 巨幕投射 + 杜比视界 + 轻量化",
   why="雷鸟GT系列以1899元起打破AR观影定价壁垒，全球首款完整支持杜比视界，把IMAX级影院装进眼镜。",
   related="AR-VR 显示（巨幕）、音频（杜比）、结构（轻量化）。",
   vendor="雷鸟创新 / GT系列", time="2026-07-17",
   url="https://www.toutiao.com/article/7663246048948781608/", sources="雷鸟创新、今日头条", note="GT Max等效6米267英寸"),
 dict(title="绿联二合一无线充套装", domain="无线充/电池/认证", stars="★★★★", status="released", source="B",
   signal="新品开售", confirm="1（绿联官方）",
   params="15W磁吸 + 5W；MFi认证；支架式二合一",
   tech="磁吸无线充 + 有线快充 + MFi认证二合一",
   why="绿联二合一无线充套装8月6日开售，15W磁吸+5W+支架，MFi认证，车载/桌面补能新形态。",
   related="无线充、电池（BMS）、认证（MFi）。",
   vendor="绿联（UGREEN）/ 二合一无线充套装", time="2026-08-06（开售）",
   url="https://www.ugreen.com/", sources="绿联官方", note="磁吸+支架二合一"),
 dict(title="华为 Sound X5", domain="智能音箱/音频", stars="★★★★", status="released", source="A",
   signal="在售旗舰", confirm="1（华为官方）",
   params="八单元三分频；160W；2199元",
   tech="旗舰智能音箱 + 八单元三分频 + 160W大功率",
   why="华为Sound X5以八单元三分频与160W功率成为2026旗舰智能音箱，鸿蒙生态音频中枢再升级。",
   related="智能音箱 音频、AIoT（鸿蒙）。",
   vendor="华为 / Sound X5", time="2026（在售）",
   url="https://www.huawei.com/cn/", sources="华为官方", note="鸿蒙智能音箱旗舰"),
]

# ---- INTERNATIONAL (sorted: coming -> released time-desc) ----
intl = [
 dict(title="Samsung Galaxy Z Fold 8", domain="手机/折叠屏/SoC/影像", stars="★★★★★", status="released", source="A",
   signal="官方发布（已上市）", confirm="2（三星Unpacked + 科技小南）",
   params="7.6英寸内屏120Hz Dynamic AMOLED 2X；骁龙8 Elite Gen5 for Galaxy；5000mAh；45W",
   tech="横向折叠旗舰 + 骁龙8至尊版 + 大屏多任务",
   why="三星Galaxy Z Fold 8于7月22日Unpacked发布，7.6英寸内屏+骁龙8 Elite Gen5 for Galaxy，折叠旗舰标杆。",
   related="手机 折叠屏、SoC、显示-OLED、影像。",
   vendor="三星 / Galaxy Z Fold 8", time="2026-07-22（发布）",
   url="https://www.samsung.com/", sources="三星Unpacked 2026、科技小南", note="同期 Flip8 / Watch Ultra2 / Watch9"),
 dict(title="Motorola Edge 70 Max", domain="手机/SoC/显示/电池/无线充", stars="★★★★★", status="released", source="B",
   signal="海外发布（印度）", confirm="2（Flipkart + 科技媒体）",
   params="骁龙8 Gen5（3nm Oryon）；6.82英寸QHD+ LTPO 144Hz 7000nit；7100mAh；90W+25W Qi2磁吸无线；IP69/MIL-STD-810H",
   tech="2K LTPO旗舰 + 7100mAh硅碳 + 90W有线 + 原生Qi2.2.1磁吸无线 + 独立AI键",
   why="摩托罗拉Edge 70 Max 7月15日印度发布，骁龙8 Gen5+7100mAh+原生Qi2.2.1磁吸无线，安卓首批内置磁吸无线充电旗舰。",
   related="手机 SoC、显示-OLED、电池快充、无线充（Qi2）、结构（IP69/军规）、AI（Moto AI/NPU）。",
   vendor="摩托罗拉（Motorola）/ Edge 70 Max", time="2026-07-15（印度发布）",
   url="https://www.androidpure.com/motorola-edge-70-max-india-price/", sources="Motorola India、Flipkart、AndroidPure、gizchina", note="首款内置磁吸无线充电安卓旗舰；₹54999"),
 dict(title="MacBook Pro M5", domain="笔记本/SoC/AI/显示/电池", stars="★★★★★", status="released", source="A",
   signal="在售新品", confirm="1（苹果官方）",
   params="M5 Pro/Max；14.2英寸120Hz；雷雳；20hr+；NPU",
   tech="Apple Silicon + M5 Pro/Max + 120Hz XDR + 长续航",
   why="MacBook Pro M5在售，M5 Pro/Max芯片+120Hz XDR屏+20小时续航，苹果专业创作本旗舰。",
   related="笔记本 SoC、AI/NPU、显示、电池、无线（WiFi）。",
   vendor="Apple / MacBook Pro M5", time="2026（在售）",
   url="https://www.apple.com/macbook-pro/", sources="Apple官方", note="Pro级创作本"),
 dict(title="华为 MatePad 11.5 2026（印度）", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="海外发布", confirm="1（华为印度官网）",
   params="麒麟T82；11.5英寸2.5K 120Hz；10100mAh；40W；HarmonyOS 6.0",
   tech="大屏长续航 + 麒麟T82 + 2.5K高刷",
   why="华为MatePad 11.5 2026于8月7日登陆印度，麒麟T82+10100mAh，华为海外平板大屏长续航布局。",
   related="平板 SoC、显示、电池。",
   vendor="华为 / MatePad 11.5 2026（印度）", time="2026-08-07（印度发布）",
   url="https://consumer.huawei.com/in/", sources="华为印度官网、数码媒体", note="鸿蒙6.0；515g"),
 dict(title="Moto Pad 70 Pro", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="B",
   signal="海外发布（印度开售）", confirm="1（IT之家）",
   params="骁龙8s Gen4；13英寸3.5K IPS 144Hz；10200mAh；45W；附Moto Pen Pro",
   tech="大屏高刷 + 骁龙8s + 长续航 + JBL四扬声器",
   why="联想摩托罗拉6月27日海外发布Moto Pad 70 Pro，13英寸3.5K 144Hz+10200mAh，7月4日印度开售，海外大屏平板新选择。",
   related="平板 SoC、显示、电池、手写笔、音频（JBL）。",
   vendor="联想（Motorola）/ Moto Pad 70 Pro", time="2026-06-27（发布）/ 07-04（印度开售）",
   url="https://www.motorola.com/", sources="IT之家、摩托罗拉", note="承诺Android 17/18升级至2030"),
 dict(title="Garmin Enduro 4", domain="智能手表/传感器/结构/电池", stars="★★★★", status="coming", source="B",
   signal="FCC曝光（即将发布）", confirm="2（FCC + 5krunner）",
   params="MIP太阳能屏；LTE/SOS卫星消息；Elevate Gen6；51mm/47mm；钛边框；45-50天续航",
   tech="超长续航户外表 + MIP太阳能 + 卫星SOS + 钛合金",
   why="Garmin Enduro 4已clearing FCC（型号A05216），预计8-9月发布，MIP太阳能+卫星SOS+45天续航，超长续航户外旗舰。",
   related="智能手表 传感器（GPS/心率/HRV）、电池、结构（钛）、无线通信（卫星）。",
   vendor="Garmin / Enduro 4", time="2026-08/09（预计）",
   url="https://the5krunner.com/2026/06/23/garmin-enduro-4-fcc-a05216/", sources="FCC认证、the5krunner、watchesreviewed", note="双频WiFi；取代Enduro 3"),
 dict(title="Amazfit Balance Ultra", domain="智能手表/结构/电池/传感器", stars="★★★★", status="released", source="B",
   signal="已发售", confirm="2（纽约发布会 + IT之家）",
   params="5级钛合金；1.5英寸AMOLED 3000nit；蓝宝石；LED手电；30天续航；4299元",
   tech="钛合金旗舰运动表 + AMOLED + 30天续航 + 混合训练系统",
   why="华米Amazfit Balance Ultra 6月20日发售，5级钛合金+1.5英寸3000nit AMOLED+30天续航，全球运动健康表高端化。",
   related="智能手表 结构（钛/蓝宝石）、电池、传感器（心率/血氧/体温）。",
   vendor="Amazfit（华米）/ Balance Ultra", time="2026-06-20（发售）",
   url="https://www.163.com/dy/article/KVSFL7ME0511B8LM.html", sources="Amazfit、IT之家、Zepp", note="纽约发布；HYROX官方穿戴伙伴"),
 dict(title="Garmin Forerunner 70/170", domain="智能手表/传感器/电池", stars="★★★★", status="released", source="B",
   signal="海外发布（印度）", confirm="2（Garmin官方 + 印度发布）",
   params="1.2英寸AMOLED；13天续航（70）/10天（170）；Garmin Coach；HRV；80+运动",
   tech="跑步GPS智能表 + AMOLED + 自适应训练 + Garmin Pay",
   why="Garmin Forerunner 70/170于7月3-4日印度发布，1.2英寸AMOLED+13天续航，入门跑步表AMOLED化。",
   related="智能手表 传感器（GPS/心率/HRV）、电池、AI（Garmin Coach）。",
   vendor="Garmin / Forerunner 70 / 170", time="2026-07-03/04（印度发布）",
   url="https://www.garmin.com/en-US/newsroom/press-release/sports-fitness/run-further-with-forerunner-70-and-forerunner-170-from-garmin/", sources="Garmin Newsroom、The Mobile Indian", note="$249.99起；170支持Garmin Pay/音乐"),
 dict(title="Dell XPS 14 2026", domain="笔记本/SoC/显示/AI", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（戴尔官方）",
   params="Panther Lake；OLED；轻薄；AI引擎",
   tech="轻薄创作本 + Panther Lake + OLED + AI",
   why="戴尔XPS 14 2026搭载Panther Lake与OLED屏，延续XPS轻薄创作定位，AI PC阵营再扩充。",
   related="笔记本 SoC、显示-OLED、AI/NPU。",
   vendor="Dell / XPS 14 2026", time="2026",
   url="https://www.dell.com/", sources="Dell官方", note="Panther Lake平台"),
 dict(title="LG gram 16 16Z90TL", domain="笔记本/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（LG官方）",
   params="Lunar Lake；16英寸；1.24kg；77Wh；长续航",
   tech="轻量长续航 + Lunar Lake + 大屏",
   why="LG gram 16（16Z90TL）搭载Lunar Lake，1.24kg+77Wh，延续gram系列轻量长续航标杆。",
   related="笔记本 SoC、显示、电池、AI/NPU（Lunar Lake）。",
   vendor="LG / gram 16 16Z90TL", time="2026-07-20",
   url="https://www.lg.com/", sources="LG官方、数码媒体", note="1.24kg轻量化"),
 dict(title="XREAL a01+", domain="AR-VR/显示/音频", stars="★★★★", status="released", source="B",
   signal="美国上市", confirm="1（XREAL官方）",
   params="299美元；62g；Micro-OLED；120Hz；轻量AR眼镜",
   tech="轻量消费AR眼镜 + Micro-OLED + 120Hz",
   why="XREAL a01+ 7月16日美国上市，299美元/62g，Micro-OLED+120Hz，消费级AR眼镜轻量化普及。",
   related="AR-VR 显示（Micro-OLED）、音频。",
   vendor="XREAL / a01+", time="2026-07-16（美国上市）",
   url="https://www.xreal.com/", sources="XREAL官方", note="62g轻量；299美元"),
 dict(title="Rokid Glasses 加拿大", domain="AR-VR/AI/显示", stars="★★★★", status="released", source="B",
   signal="海外上市（北美）", confirm="1（北京商报）",
   params="999加元；Micro-LED；89种语言；多伦多发布",
   tech="轻量AI眼镜 + Micro-LED + 多语种实时翻译",
   why="Rokid Glasses 8月1日登陆加拿大多伦多，继法国/德国后深耕北美，Micro-LED+89语言，国产AR眼镜出海加速。",
   related="AR-VR 显示（Micro-LED）、AI/NPU、结构（轻量）。",
   vendor="灵伴科技（Rokid）/ Glasses 加拿大版", time="2026-08-01（多伦多发布）",
   url="https://www.rokid.com/", sources="北京商报、Rokid", note="与明氏光学合作配镜"),
 dict(title="UGREEN MagFlow Qi2.2", domain="无线充/认证/散热", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（绿联/充电头网）",
   params="Qi2.2 25W；世界首款Qi2.2认证磁吸；风冷散热",
   tech="Qi2.2磁吸 + 25W + 主动风冷 + 认证首发",
   why="绿联MagFlow成为业界首款通过Qi2.2认证的磁吸无线充，25W+风冷散热，Qi2.2生态标准落地标杆。",
   related="无线充、认证（Qi2.2/WPC）、散热。",
   vendor="绿联（UGREEN）/ MagFlow Qi2.2", time="2026",
   url="https://www.ugreen.com/", sources="绿联、充电头网", note="世界首款Qi2.2认证"),
 dict(title="JBL VIENNA 悬浮歌词音箱", domain="智能音箱/音频/显示", stars="★★★★", status="released", source="B",
   signal="新品上市", confirm="1（JBL官方）",
   params="18.5英寸悬浮歌词屏；100W；8299元",
   tech="歌词悬浮显示 + 100W大功率 + 智能音箱",
   why="JBL VIENNA以18.5英寸悬浮歌词屏+100W功率切入高端智能音箱，视觉与音频融合新形态。",
   related="智能音箱 音频、显示（悬浮屏）。",
   vendor="JBL / VIENNA 悬浮歌词音箱", time="2026-07-13/19",
   url="https://www.jbl.com/", sources="JBL官方", note="8299元；歌词悬浮"),
 dict(title="JBL PULSE 6", domain="智能音箱/音频", stars="★★★★", status="released", source="B",
   signal="新品推出", confirm="1（JBL官方）",
   params="2499元；IP68；40W；360°灯光；08-31开售",
   tech="便携灯光音箱 + IP68防水 + 40W",
   why="JBL PULSE 6于8月10日推出、8月31日开售，2499元/IP68/40W，便携灯光音箱迭代。",
   related="智能音箱 音频、结构（IP68）。",
   vendor="JBL / PULSE 6", time="2026-08-10（推出）/ 08-31（开售）",
   url="https://www.jbl.com/", sources="JBL官方", note="IP68防水；360°灯光"),
]

# ---- Top 5 signals ----
top5 = [
 dict(title="REDMI K100 Pro Max", dim="手机/SoC/影像/电池/快充", stars="★★★★★",
      key="第五代骁龙8至尊版+2亿+近9000mAh，8/11发布"),
 dict(title="华为 MatePad Pro 12英寸", dim="平板/SoC/显示/电池", stars="★★★★★",
      key="439g/4.7mm+麒麟T93+10400mAh，8/5发布"),
 dict(title="小米平板8S Pro", dim="平板/SoC/显示/电池", stars="★★★★★",
      key="自研玄戒O3+120W+12000mAh，8/3认证"),
 dict(title="Samsung Galaxy Z Fold 8", dim="手机/折叠屏/SoC", stars="★★★★★",
      key="7.6寸内屏+骁龙8至尊版，7/22发布"),
 dict(title="Motorola Edge 70 Max", dim="手机/SoC/电池/无线充", stars="★★★★★",
      key="骁龙8 Gen5+7100mAh+原生Qi2.2磁吸，7/15印度"),
]

# ---- Dimension panel (all 16 lit) ----
dims = [
 ("SoC/芯片", 28, True), ("显示/OLED", 22, True), ("电池/快充", 26, True), ("散热", 6, True),
 ("无线通信", 10, True), ("音频", 7, True), ("摄像头", 9, True), ("结构/工艺", 7, True),
 ("传感器", 9, True), ("手写笔/触控", 6, True), ("生物识别", 6, True), ("AI/NPU", 12, True),
 ("马达/触觉", 3, True), ("折叠屏", 2, True), ("BMS/电源", 4, True), ("认证/合规", 6, True),
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
