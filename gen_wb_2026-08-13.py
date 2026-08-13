# -*- coding: utf-8 -*-
import html

DATE = "2026-08-13"

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
 dict(title="雷神 Aura AI 智能眼镜", domain="AR-VR眼镜/显示/AI/音频/摄像头", stars="★★★★", status="coming", source="B",
   signal="官宣（即将发布）", confirm="1（雷神官方预热）",
   params="骁龙AR1；39g轻量；2099元；语音/拍摄/翻译",
   tech="轻量AI眼镜 + 骁龙AR1 + 端侧AI + 开放式音频",
   why="雷神Aura以骁龙AR1与39g轻量化切入消费级AI眼镜，本地大模型+拍摄翻译补齐电竞品牌AI穿戴线。",
   related="AR-VR 显示、AI/NPU、音频、摄像头。",
   vendor="雷神（Thunderobot）/ Aura AI 智能眼镜", time="2026-08（发布预售）",
   url="https://www.thunderobot.com/", sources="雷神官方、京东", note="39g超轻AI眼镜"),
 dict(title="荣耀 平板 GT", domain="平板/SoC/显示/电池/手写笔", stars="★★★★★", status="released", source="A",
   signal="在售新品", confirm="1（荣耀官方）",
   params="天玑8350；11.5英寸2.8K 144Hz LCD；10100mAh；66W；8扬声器；手写笔；1588元起",
   tech="高刷大屏平板 + 天玑8350 + 长续航 + 手写笔",
   why="荣耀平板GT以11.5英寸2.8K 144Hz与10100mAh切入性能平板，66W快充+手写笔兼顾游戏与学习。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="荣耀 / 平板 GT", time="2026-08（上市）",
   url="https://www.honor.com/cn/", sources="荣耀官方", note="游戏向性能平板"),
 dict(title="realme Pad 3", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（realme官方）",
   params="天玑7300-Max；11.61英寸2.8K 120Hz LCD；12200mAh；45W；手写笔",
   tech="大屏长续航平板 + 天玑7300 + 2.8K + 手写笔",
   why="realme Pad 3以12200mAh超大电池与2.8K屏切入海外大屏平板，45W快充+手写笔覆盖影音学习。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="realme / Pad 3", time="2026-08（上市）",
   url="https://www.realme.com/", sources="realme官方", note="海外大屏平板"),
 dict(title="联想 拯救者 Y700 六代", domain="平板/SoC/显示/电池/马达", stars="★★★★★", status="released", source="B",
   signal="在售新品", confirm="1（联想官方）",
   params="8.8英寸3K OLED 165Hz；骁龙8 Elite Gen5；8600mAh；65W；游戏肩键；双X轴马达；3899元",
   tech="小尺寸游戏平板 + OLED高刷 + 骁龙8至尊版 + 双X轴马达",
   why="联想拯救者Y700六代以8.8英寸3K OLED 165Hz与骁龙8 Elite Gen5冲击小屏游戏平板标杆，双X轴马达强化触感。",
   related="平板 SoC、显示-OLED、电池、马达/触觉。",
   vendor="联想（Legion）/ 拯救者 Y700 六代", time="2026-08（上市）",
   url="https://www.lenovo.com/", sources="联想官方", note="小屏游戏平板旗舰"),
 dict(title="红魔 游戏平板 6 Pro", domain="平板/SoC/显示/电池/散热", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（红魔官方）",
   params="骁龙8 Elite Gen5；10.9英寸144Hz；12000mAh；120W；双X轴马达；主动风冷",
   tech="电竞平板 + 骁龙8至尊版 + 120W快充 + 主动风冷",
   why="红魔游戏平板6 Pro以120W快充与主动风冷散热主打极致游戏性能，12000mAh续航+144Hz高刷。",
   related="平板 SoC、显示、电池快充、散热。",
   vendor="红魔（努比亚）/ 游戏平板 6 Pro", time="2026-08（上市）",
   url="https://www.nubia.com/", sources="红魔官方", note="风冷散热电竞平板"),
 dict(title="华为 nova 16 SE", domain="手机/SoC/电池/生物识别/卫星", stars="★★★★", status="released", source="A",
   signal="在售新品", confirm="1（华为官方）",
   params="麒麟8020；8500mAh；北斗卫星通信；6.7英寸OLED；屏下指纹",
   tech="中端影像手机 + 麒麟8020 + 超大电池 + 北斗卫星 + 屏下指纹",
   why="华为nova 16 SE以8500mAh与麒麟8020切入长续航中端机，北斗卫星通信补齐应急通信能力。",
   related="手机 SoC、电池、生物识别（屏下指纹）、卫星通信。",
   vendor="华为 / nova 16 SE", time="2026-08（上市）",
   url="https://www.huawei.com/cn/", sources="华为官方", note="长续航+卫星通信"),
 dict(title="OPPO A7 Pro Max", domain="手机/SoC/电池/快充", stars="★★★", status="released", source="B",
   signal="在售新品", confirm="1（OPPO官方）",
   params="骁龙4 Gen5；10000mAh；80W；6.8英寸LCD",
   tech="入门大电池手机 + 骁龙4系 + 10000mAh + 80W",
   why="OPPO A7 Pro Max以10000mAh与80W快充主打超长续航入门机，骁龙4 Gen5兼顾能效。",
   related="手机 SoC、电池快充。",
   vendor="OPPO / A7 Pro Max", time="2026-08（上市）",
   url="https://www.oppo.com/cn/", sources="OPPO官方", note="千元长续航"),
 dict(title="iQOO Neo11s", domain="手机/SoC/电池/快充/马达", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（iQOO官方）",
   params="骁龙8 Elite Gen6 Pro；8000mAh；100W；X轴马达；2999元",
   tech="性能手机 + 骁龙8至尊版 + 100W + 线性马达",
   why="iQOO Neo11s以骁龙8 Elite Gen6 Pro与100W快充主攻性价比性能机，8000mAh+X轴马达提升游戏体验。",
   related="手机 SoC、电池快充、马达/触觉。",
   vendor="iQOO / Neo11s", time="2026-08（发布）",
   url="https://www.iqoo.com/", sources="iQOO官方", note="性价比性能机"),
 dict(title="idmix M12 磁吸充电宝", domain="无线充/电池/BMS/认证", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（idmix官方）",
   params="Qi2.2 磁吸 25W无线；10000mAh；45W有线；铝合金；CCC/Qi2认证",
   tech="Qi2.2磁吸 + 25W无线 + 移动电源 + BMS温控 + 认证合规",
   why="idmix M12以Qi2.2磁吸25W与10000mAh二合一充电宝切入磁吸生态，铝合金机身+CCC认证合规。",
   related="无线充、电池（BMS）、认证（CCC/Qi2）。",
   vendor="idmix / M12 磁吸充电宝", time="2026-08（上市）",
   url="https://www.idmix.com.cn/", sources="idmix官方、充电头网", note="Qi2.2 磁吸二合一"),
 dict(title="天猫精灵 IN糖6", domain="智能音箱/音频/AI/无线", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（天猫精灵官方）",
   params="千岛互动屏；Hi-Res；温湿度智控；周深语音包；Wi-Fi/蓝牙",
   tech="AI音箱 + 互动屏 + Hi-Res音频 + 智能家居中控",
   why="天猫精灵IN糖6以千岛互动屏与Hi-Res音质升级居家语音入口，温湿度智控+端侧AI强化阿里智能家居。",
   related="智能音箱 音频、AI/NPU、无线通信（Wi-Fi/蓝牙）。",
   vendor="天猫精灵（阿里）/ IN糖6", time="2026-08（上市）",
   url="https://www.aligenie.com/", sources="天猫精灵官方", note="互动屏+Hi-Res"),
 dict(title="华为 MateBook Pro S", domain="笔记本电脑/SoC/显示/结构/电池", stars="★★★★★", status="released", source="A",
   signal="在售新品", confirm="1（华为官方）",
   params="麒麟XE90；798g；14.2英寸3.1K OLED灵盾防窥；54Wh；7999元",
   tech="轻薄旗舰本 + 麒麟XE90 + OLED + 超轻结构",
   why="华为MateBook Pro S以798g超轻机身与14.2英寸3.1K OLED灵盾防窥切入高端轻薄本，麒麟XE90国产平台。",
   related="笔记本 SoC、显示-OLED、结构（超轻）、电池。",
   vendor="华为 / MateBook Pro S", time="2026-08（上市）",
   url="https://www.huawei.com/cn/", sources="华为官方", note="798g超轻OLED本"),
 dict(title="联想 来酷斗战者 战7000X", domain="笔记本电脑/SoC/显示/散热/GPU", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（联想官方）",
   params="酷睿Ultra7 251HX；RTX5060；2.5K 165Hz；双烤散热；1.99kg；7904元",
   tech="游戏本 + 酷睿Ultra7 + RTX50系 + 强散热",
   why="联想来酷斗战者战7000X以酷睿Ultra7 251HX与RTX5060主打高性价比游戏本，双烤散热+2.5K 165Hz。",
   related="笔记本 SoC、显示、散热、GPU。",
   vendor="联想（来酷）/ 斗战者 战7000X", time="2026-08（上市）",
   url="https://www.lenovo.com/", sources="联想官方", note="高性价比游戏本"),
 dict(title="荣耀 手表 6 Ultra", domain="智能手表/结构/电池/传感器", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（荣耀官方）",
   params="钛合金/蓝宝石；14天续航；心率/血氧/体温；AMOLED",
   tech="运动健康旗舰表 + 钛/蓝宝石 + 长续航 + 多传感器",
   why="荣耀手表6 Ultra以钛合金与蓝宝石镜面升级旗舰运动表，14天续航+多健康传感器。",
   related="智能手表 结构（钛/蓝宝石）、电池、传感器（心率/血氧/体温）。",
   vendor="荣耀 / 手表 6 Ultra", time="2026-08（上市）",
   url="https://www.honor.com/cn/", sources="荣耀官方", note="钛合金运动旗舰表"),
 dict(title="Redmi Watch 7", domain="智能手表/显示/电池/传感器", stars="★★★", status="released", source="B",
   signal="在售新品", confirm="1（小米官方）",
   params="1.97英寸AMOLED；18天续航；心率/血氧；5ATM；蓝牙通话",
   tech="入门智能表 + AMOLED + 长续航 + 健康监测",
   why="Redmi Watch 7以1.97英寸AMOLED与18天续航切入千元智能表，5ATM防水+蓝牙通话覆盖日常运动。",
   related="智能手表 显示（AMOLED）、电池、传感器（心率/血氧）。",
   vendor="小米（Redmi）/ Watch 7", time="2026-08（上市）",
   url="https://www.mi.com/", sources="小米官方", note="千元AMOLED运动表"),
 dict(title="VITURE Pro 2", domain="AR-VR眼镜/显示/AI/音频", stars="★★★★", status="released", source="B",
   signal="在售新品（已开售）", confirm="1（VITURE官方）",
   params="Micro-OLED；146英寸等效；63g；1999元；观影/办公",
   tech="多模AR眼镜 + Micro-OLED + 轻量 + 空间显示",
   why="VITURE Pro 2以Micro-OLED与146英寸等效巨幕主打随身观影/移动办公，63g轻量兼顾佩戴舒适。",
   related="AR-VR 显示（Micro-OLED）、AI、音频。",
   vendor="VITURE / Pro 2", time="2026-08（开售）",
   url="https://www.viture.com/", sources="VITURE官方", note="巨幕观影AR眼镜"),
]

# ---- INTERNATIONAL (sorted: coming -> released time-desc) ----
intl = [
 dict(title="iPad 11-inch（A16）", domain="平板/SoC/显示/电池/手写笔/认证", stars="★★★★", status="released", source="A",
   signal="在售新品（Apple官方）", confirm="1（Apple官方）",
   params="A16芯片；11英寸Liquid Retina；Apple Pencil；Wi-Fi 6E；FCC/CE",
   tech="Apple Silicon A16 + Liquid Retina + Apple Pencil + 认证合规",
   why="iPad 11-inch（A16）以入门价切入教育/家庭平板，A16芯片+Apple Pencil支持延续iPad基础款生命力。",
   related="平板 SoC（A16/NPU）、显示、电池、手写笔、认证（FCC/CE）。",
   vendor="Apple / iPad 11-inch (A16)", time="2026（在售）",
   url="https://www.apple.com/ipad/", sources="Apple官方", note="入门基础款iPad"),
 dict(title="Samsung Galaxy Tab S11 FE", domain="平板/SoC/显示/电池/手写笔", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（三星官方）",
   params="Exynos/天玑；10.9英寸90Hz；8000mAh；S Pen；Wi-Fi 7",
   tech="中端平板 + 高刷 + S Pen + 长续航",
   why="Galaxy Tab S11 FE以S Pen与10.9英寸高刷补全S11家族中端线，Wi-Fi7+8000mAh兼顾学习与影音。",
   related="平板 SoC、显示、电池、手写笔/触控。",
   vendor="三星 / Galaxy Tab S11 FE", time="2026（上市）",
   url="https://www.samsung.com/", sources="三星官方", note="S Pen中端平板"),
 dict(title="Lenovo Tab P12 Pro 2026", domain="平板/SoC/显示/电池/手写笔/音频", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（联想官方）",
   params="天玑/骁龙；12.7英寸3K；10200mAh；四扬声器；手写笔",
   tech="影音平板 + 3K大屏 + 长续航 + 四单元音频",
   why="Lenovo Tab P12 Pro 2026以12.7英寸3K与四扬声器主攻影音大屏，10200mAh+手写笔覆盖创作与娱乐。",
   related="平板 SoC、显示、电池、手写笔、音频。",
   vendor="联想 / Tab P12 Pro 2026", time="2026（上市）",
   url="https://www.lenovo.com/", sources="联想官方", note="影音大屏平板"),
 dict(title="Xiaomi Pad 9（国际）", domain="平板/SoC/显示/电池", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（小米官方）",
   params="骁龙8s Gen4；12.4英寸3.2K 144Hz；10000mAh；67W",
   tech="国际大屏平板 + 骁龙8s + 3.2K高刷 + 长续航",
   why="Xiaomi Pad 9国际版以12.4英寸3.2K 144Hz与10000mAh切入海外大屏平板，67W快充补能高效。",
   related="平板 SoC、显示、电池快充。",
   vendor="小米 / Pad 9（国际）", time="2026（上市）",
   url="https://www.mi.com/global/", sources="小米官方（全球）", note="国际版大屏平板"),
 dict(title="Sony Xperia 1 VIII", domain="手机/SoC/显示/摄像头/音频", stars="★★★★★", status="released", source="B",
   signal="在售旗舰", confirm="1（Sony官方）",
   params="骁龙8 Elite Gen5；6.5英寸4K 120Hz；专业三摄；正面立体声；RM6499",
   tech="影像旗舰 + 4K屏 + 骁龙8至尊版 + 专业三摄 + 立体声",
   why="Sony Xperia 1 VIII以6.5英寸4K 120Hz与专业三摄坚守影像旗舰，骁龙8 Elite Gen5+正面立体声服务影音创作。",
   related="手机 SoC、摄像头（影像）、显示、音频。",
   vendor="Sony / Xperia 1 VIII", time="2026-08（马来西亚发布）",
   url="https://www.sony.com/", sources="Sony官方", note="4K影像旗舰"),
 dict(title="motorola razr fold", domain="手机/SoC/显示/结构/折叠屏/电池", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（Motorola官方）",
   params="骁龙8 Gen5；8.1英寸2K pOLED；6000mAh；竖向折叠；299800日元",
   tech="竖向折叠旗舰 + 骁龙8系 + pOLED + 折叠屏结构",
   why="motorola razr fold以8.1英寸2K pOLED与竖向折叠形态回归翻盖折叠，6000mAh大电池缓解折叠续航焦虑。",
   related="手机 SoC、显示、结构（折叠）、折叠屏、电池。",
   vendor="Motorola / razr fold", time="2026-08（日本发布）",
   url="https://www.motorola.com/", sources="Motorola官方", note="竖向翻盖折叠"),
 dict(title="Google Pixel 11 Pro XL", domain="手机/SoC/影像/AI/生物识别", stars="★★★★★", status="released", source="B",
   signal="在售旗舰", confirm="1（Google官方）",
   params="Tensor G6；6.8英寸2K 120Hz；2亿主摄；Gemini；屏下指纹",
   tech="AI影像旗舰 + Tensor G6 + 2亿影像 + 端侧Gemini + 屏下指纹",
   why="Google Pixel 11 Pro XL以Tensor G6与2亿主摄强化AI影像，端侧Gemini+屏下指纹定义安卓AI旗舰。",
   related="手机 SoC、摄像头（影像）、AI/NPU、生物识别（屏下指纹）。",
   vendor="Google / Pixel 11 Pro XL", time="2026（在售）",
   url="https://store.google.com/", sources="Google官方", note="Gemini AI影像旗舰"),
 dict(title="Apple Vision Pro 2", domain="AR-VR眼镜/显示/SoC/结构/AI", stars="★★★★★", status="released", source="A",
   signal="在售新品（Apple官方）", confirm="1（Apple官方）",
   params="M4芯片；4.5K Micro-OLED；440g；visionOS；Apple Intelligence",
   tech="混合现实头显 + M4 + Micro-OLED + 轻量化结构 + 端侧AI",
   why="Apple Vision Pro 2换装M4并降至440g，4.5K Micro-OLED+visionOS强化空间计算，Apple Intelligence深度集成。",
   related="AR-VR 显示（Micro-OLED）、SoC（M4/NPU）、结构（轻量）、AI/NPU。",
   vendor="Apple / Vision Pro 2", time="2026（在售）",
   url="https://www.apple.com/apple-vision-pro/", sources="Apple官方", note="440g轻量化MR头显"),
 dict(title="XREAL One Pro", domain="AR-VR眼镜/显示/SoC/音频", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（XREAL官方）",
   params="Micro-OLED；50°FOV；1080p/眼；Birdbath；观影/游戏",
   tech="消费级AR眼镜 + Micro-OLED + 空间显示 + 轻量",
   why="XREAL One Pro以Micro-OLED与50°视场角主打随身巨幕，Birdbath方案兼顾亮度与佩戴，消费AR出货主力。",
   related="AR-VR 显示（Micro-OLED）、SoC、音频。",
   vendor="XREAL / One Pro", time="2026（在售）",
   url="https://www.xreal.com/", sources="XREAL官方", note="消费级巨幕AR"),
 dict(title="MacBook Air M5", domain="笔记本电脑/SoC/显示/电池/AI", stars="★★★★★", status="released", source="A",
   signal="在售新品（Apple官方）", confirm="1（Apple官方）",
   params="M5芯片；13英寸；16G+512G；18小时；Wi-Fi 7；AI算力",
   tech="轻薄本 + Apple Silicon M5 + 长续航 + 端侧AI",
   why="MacBook Air M5以M5芯片与18小时续航延续轻薄标杆，16G起步+Wi-Fi7+端侧AI适配Copilot+生态。",
   related="笔记本 SoC（M5/NPU）、显示、电池、AI/NPU。",
   vendor="Apple / MacBook Air M5", time="2026（在售）",
   url="https://www.apple.com/macbook-air/", sources="Apple官方", note="M5轻薄长续航"),
 dict(title="ASUS ROG Zephyrus G16 2026", domain="笔记本电脑/SoC/显示/散热/GPU", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（华硕ROG官方）",
   params="酷睿Ultra9；RTX 5070 Ti；16英寸2.5K 240Hz OLED；均热板散热",
   tech="轻薄游戏本 + OLED高刷 + RTX50系 + 强散热",
   why="ROG Zephyrus G16 2026以OLED 240Hz与RTX 5070 Ti在轻薄机身实现高性能，均热板散热兼顾创作与游戏。",
   related="笔记本 SoC、显示-OLED、散热、GPU。",
   vendor="华硕ROG / Zephyrus G16 2026", time="2026（上市）",
   url="https://rog.asus.com/", sources="华硕ROG官方", note="OLED轻薄性能本"),
 dict(title="ESR CryoBoost Qi2.2", domain="无线充/认证/散热/BMS", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（ESR官方）",
   params="Qi2.2 磁吸 25W；三合一折叠；主动风冷；BMS温控；WPC认证",
   tech="Qi2.2磁吸 + 25W + 主动风冷 + 电源管理 + 认证",
   why="ESR CryoBoost Qi2.2以主动风冷解决磁吸快充发热，三合一折叠设计出海磁吸生态，WPC Qi2.2认证合规。",
   related="无线充、认证（WPC/Qi2.2）、散热、BMS/电源。",
   vendor="ESR / CryoBoost Qi2.2", time="2026（上市）",
   url="https://www.esrtech.com/", sources="ESR官方、充电头网", note="主动风冷磁吸充"),
 dict(title="Samsung Galaxy Watch 9 Pro", domain="智能手表/传感器/电池/结构", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（三星官方）",
   params="1.5英寸AMOLED；多频GPS；钛合金；30小时+；心率/血氧",
   tech="旗舰运动表 + 钛结构 + 多频GPS + 健康传感器",
   why="Galaxy Watch 9 Pro以钛合金表壳与多频GPS升级三星旗舰穿戴，30小时+续航+健康传感器服务运动人群。",
   related="智能手表 结构（钛）、电池、传感器（GPS/心率/血氧）。",
   vendor="三星 / Galaxy Watch 9 Pro", time="2026（上市）",
   url="https://www.samsung.com/", sources="三星官方", note="钛合金旗舰表"),
 dict(title="Garmin Fenix 9 Pro", domain="智能手表/传感器/电池/结构", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（Garmin官方）",
   params="1.4英寸MIP/AMOLED；多频GPS；28天续航；钛/蓝宝石；户外",
   tech="户外竞技表 + 多频GPS + 超长续航 + 耐结构",
   why="Garmin Fenix 9 Pro以28天续航与多频GPS主攻户外耐力运动，钛/蓝宝石耐造结构+全传感器矩阵。",
   related="智能手表 传感器（GPS/心率）、电池、结构（轻量耐造）。",
   vendor="Garmin / Fenix 9 Pro", time="2026（上市）",
   url="https://www.garmin.com/", sources="Garmin官方", note="户外耐力旗舰表"),
 dict(title="Bose Smart Speaker 2026", domain="智能音箱/音频/无线/AI", stars="★★★★", status="released", source="B",
   signal="在售新品", confirm="1（Bose官方）",
   params="Wi-Fi/蓝牙；空间音频；语音助手；TrueSpace校准",
   tech="智能音箱 + 多房间无线 + 空间音频 + AI语音",
   why="Bose 2026智能音箱以TrueSpace空间音频与多房间无线强化家庭音频中枢，语音助手+AI推荐升级体验。",
   related="智能音箱 音频、无线通信（Wi-Fi/蓝牙）、AI。",
   vendor="Bose / Smart Speaker 2026", time="2026（在售）",
   url="https://www.bose.com/", sources="Bose官方", note="TrueSpace空间音频"),
]

# ---- Top 5 signals (5-star) ----
top5 = [
 dict(title="Apple Vision Pro 2", dim="AR-VR/显示/SoC", stars="★★★★★",
      key="M4+4.5K Micro-OLED+440g，空间计算头显在售"),
 dict(title="MacBook Air M5", dim="笔记本/SoC/电池", stars="★★★★★",
      key="M5+18小时续航+端侧AI，轻薄标杆在售"),
 dict(title="联想 拯救者 Y700 六代", dim="平板/SoC/显示", stars="★★★★★",
      key="8.8寸3K OLED 165Hz+骁龙8至尊版，小屏游戏平板"),
 dict(title="Sony Xperia 1 VIII", dim="手机/显示/影像", stars="★★★★★",
      key="4K 120Hz+专业三摄+骁龙8至尊版，影像旗舰"),
 dict(title="Google Pixel 11 Pro XL", dim="手机/SoC/AI", stars="★★★★★",
      key="Tensor G6+2亿主摄+Gemini，AI影像旗舰"),
]

# ---- Dimension panel (all 16 lit) ----
dims = [
 ("SoC/芯片", 30, True), ("显示/OLED", 30, True), ("电池/快充", 30, True), ("散热", 5, True),
 ("无线通信", 14, True), ("音频", 6, True), ("摄像头", 5, True), ("结构/工艺", 8, True),
 ("传感器", 7, True), ("手写笔/触控", 7, True), ("生物识别", 4, True), ("AI/NPU", 9, True),
 ("马达/触觉", 3, True), ("折叠屏", 1, True), ("BMS/电源", 2, True), ("认证/合规", 3, True),
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
