# -*- coding: utf-8 -*-
import html

DATE = "2026-08-15"

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
 dict(title="iQOO Z11S", domain="手机/电池/快充/SoC", stars="★★★★", status="coming", source="B",
   signal="官宣（8/18 发布）", confirm="3（IT之家头条/百度百科/网易多源）",
   params="天玑7500 满血版；10000mAh 宁德电芯；44W 快充；144Hz 2K 屏；IP68 & IP69；8/18 发布",
   tech="续航性能手机 + 天玑7500满血 + 10000mAh + IP69 三防",
   why="iQOO Z11S 以 10000mAh 宁德电芯与 IP68/IP69 双三防切入长续航耐用机型，144Hz 2K + 天玑7500 满血版兼顾游戏与日常，8/18 发布补齐 iQOO 中端续航线。",
   related="手机 SoC、电池（宁德电芯）、快充、结构（三防）。",
   vendor="iQOO / Z11S", time="2026-08-18（发布）",
   url="https://www.ithome.com/0/988/789.htm", sources="IT之家、百度百科、网易", note="10000mAh 续航神机"),
 dict(title="小米 MIX Fold 5", domain="手机/折叠屏/SoC/影像", stars="★★★★★", status="coming", source="A",
   signal="入网（8 月底发布）", confirm="2（头条/新浪/百度爱企查多源）",
   params="玄戒 O3 自研 3nm；8.03 英寸 2K+ OLED LTPO 内屏 + 6.56 英寸外屏；6000mAh 硅碳；100W 有线 + 50W 无线；2 亿徕卡；澎湃 OS 4 / Android 17；万元定价；已入网",
   tech="折叠影像旗舰 + 玄戒O3 3nm + 双2亿徕卡 + 硅碳大电池 + 百瓦快充",
   why="小米 MIX Fold 5 首发玄戒 O3 自研 3nm 并搭载双 2 亿徕卡影像，6000mAh 硅碳电池 + 100W/50W 双快充解决折叠续航痛点，定义国产折叠影像新标杆，点亮本期折叠屏维度。",
   related="手机 SoC（玄戒O3/NPU）、折叠屏、摄像头（双2亿徕卡）、电池快充、无线充电。",
   vendor="小米 / MIX Fold 5", time="2026-08（入网，月底发布）",
   url="https://www.toutiao.com/article/7659417226432381484", sources="今日头条、新浪、百度爱企查", note="玄戒O3 3nm 折叠旗舰"),
 dict(title="小米平板 8S Pro", domain="平板/SoC/显示/电池", stars="★★★★", status="coming", source="C",
   signal="入网（8 月底发布）", confirm="1（工信部入网 + 供应链爆料）",
   params="玄戒 O3 3nm 自研 SoC；澎湃 OS 4.0；8 月底发布会；旗舰平板定位；学生/办公/创作",
   tech="旗舰平板 + 玄戒O3 + 澎湃OS 4.0 + 大屏生产力",
   why="小米平板 8S Pro 已完成工信部入网，锁定 8 月底发布会，首发玄戒 O3 自研旗舰芯片与澎湃 OS 4.0，主攻安卓平板生产力上限，与同期竞品拉开体验差。",
   related="平板 SoC（玄戒O3）、显示、电池、手写笔/触控、AI/NPU。",
   vendor="小米 / 平板 8S Pro", time="2026-08-06（入网，月底发布）",
   url="https://www.toutiao.com/article/7670791116165366295", sources="今日头条、工信部入网", note="玄戒O3 旗舰平板"),
 dict(title="华为 MatePad Pro 2026 首销", domain="平板/显示/电池/快充", stars="★★★★", status="released", source="B",
   signal="首销（8/14）", confirm="1（腾讯新闻/华为官方）",
   params="轻薄机身；大电池；旗舰芯片；鸿蒙系统；8/14 首销（具体厚度/重量/电池以官方页为准）",
   tech="高端生产力平板 + 轻薄 + 长续航 + 鸿蒙生态",
   why="华为 MatePad Pro 2026 于 8/14 启动首销，以轻薄机身与鸿蒙多端协同强化高端平板生产力定位，延续华为在平板市场的旗舰竞争力。",
   related="平板 SoC、显示-OLED、电池快充、手写笔/触控、AI/NPU。",
   vendor="华为 / MatePad Pro 2026", time="2026-08-14（首销）",
   url="https://new.qq.com/rain/a/20260814A044UJ00", sources="腾讯新闻、华为官方", note="鸿蒙高端平板首销"),
 dict(title="联想 V14 Gen 7", domain="笔记本电脑/SoC/电池", stars="★★★★", status="released", source="B",
   signal="全球开售（8/14）", confirm="1（联想官方/Notebookcheck）",
   params="英特尔 Wildcat Lake 平台；最高 32GB DDR5-5600；1TB PCIe Gen4；14 英寸；续航超 17 小时（JEITA-BAT 3.0）；轻薄本",
   tech="轻薄商务本 + Wildcat Lake + 32GB 内存 + 17h 长续航",
   why="联想 V14 Gen 7 于 8/14 面向全球开售，Wildcat Lake 平台 + 最高 32GB 内存 + 官方宣称 17 小时续航，精准切中通勤与学生的轻薄长续航痛点。",
   related="笔记本 SoC（Wildcat Lake/NPU）、电池、显示、结构（轻薄）。",
   vendor="联想 / V14 Gen 7", time="2026-08-14（全球开售）",
   url="https://www.mydigit.cn/thread-616360-1-1.html", sources="联想官方、Notebookcheck、我的数码", note="17h 续航轻薄本"),
 dict(title="vivo S2", domain="手机/显示/电池/影像", stars="★★★★", status="released", source="B",
   signal="印度发布（8/6 发布 / 8/11 开售）", confirm="2（The Hindu / Economic Times）",
   params="6.83 英寸 1.5K 3D 曲屏 AMOLED 120Hz、HDR10+、3000nits；天玑 7360 Turbo；7050mAh + 44W；IP68/IP69K；50MP 主摄 + 32MP 前摄；OriginOS 6 / Android 16；₹39,999 起",
   tech="影像中端机 + 3D曲屏 + 7050mAh + 天玑7360 + IP69K",
   why="vivo S2 于 8/6 在印度发布、8/11 开售，以 6.83 英寸 3D 曲屏与 7050mAh 大电池切入影像中端，IP68/IP69K 三防 + 50MP 索尼主摄补齐日常耐用与拍摄。",
   related="手机 SoC（天玑7360）、显示-OLED、电池快充、摄像头、结构（三防）。",
   vendor="vivo / S2", time="2026-08-11（开售）",
   url="https://thehindu.com/sci-tech/technology/gadgets/vivo-s2-launched-in-india-for-premium-segment-buyers/article71312617.ece", sources="The Hindu、Economic Times", note="3D曲屏 7050mAh 中端机"),
 dict(title="OPPO Watch X3 Mini 粉黛海", domain="智能手表/传感器/生物识别", stars="★★★★", status="released", source="B",
   signal="开售（新配色）", confirm="1（今日头条/OPPO官方）",
   params="粉黛海新配色；骁龙 W5 双芯；eSIM 独立通信；ECG 心电；血氧/心率；长续航；8/15 前后开售",
   tech="小尺寸旗舰表 + 骁龙W5 + eSIM + ECG 健康",
   why="OPPO Watch X3 Mini 推出粉黛海新配色，骁龙 W5 双芯 + eSIM 独立通信 + ECG 心电延续小尺寸旗舰表定位，丰富女性与轻商务穿戴选择。",
   related="智能手表 SoC、传感器（心率/血氧/ECG）、生物识别（eSIM）、电池。",
   vendor="OPPO / Watch X3 Mini", time="2026-08（粉黛海开售）",
   url="https://www.toutiao.com/article/7672233651677020687/", sources="今日头条、OPPO官方", note="小尺寸 ECG 旗舰表"),
 dict(title="小米 Watch S5", domain="智能手表/显示/电池", stars="★★★★", status="released", source="B",
   signal="在售（46mm）", confirm="1（小米官方）",
   params="46mm；1.48 英寸 AMOLED 2500nits；815mAh；21 天续航；316L 不锈钢；HyperOS 3；双频五系统 GNSS；1199/1399 元",
   tech="长续航智能表 + AMOLED 2500nits + 双频GNSS + 不锈钢",
   why="小米 Watch S5 以 46mm 表盘与 815mAh 电池实现 21 天续航，1.48 英寸 2500nits AMOLED + 双频五系统 GNSS 兼顾户外可视与定位精度，1199 起主打高性价比。",
   related="智能手表 显示、电池、传感器（GNSS/心率/血氧）、结构（不锈钢）。",
   vendor="小米 / Watch S5", time="2026（在售）",
   url="https://www.mi.com/global/product/xiaomi-watch-s5-46mm", sources="小米官方", note="21天续航不锈钢表"),
 dict(title="Redmi Watch 5", domain="智能手表/显示/电池", stars="★★★", status="released", source="B",
   signal="在售（2026 款）", confirm="1（小米官方）",
   params="2.07 英寸 AMOLED 1500nits、60Hz；550mAh；蓝牙版 24 天 / eSIM 版 12 天；5ATM；蓝牙通话；不锈钢旋转表冠；澎湃 OS 2；599/799 元起",
   tech="入门长续航表 + AMOLED + 蓝牙/eSIM + 5ATM",
   why="Redmi Watch 5 以 2.07 英寸 AMOLED 与蓝牙版 24 天续航切入入门长续航，eSIM 版支持独立通话，不锈钢旋转表冠 + 5ATM 提升质感与防水。",
   related="智能手表 显示、电池、传感器（心率/血氧）、生物识别（eSIM）。",
   vendor="小米（Redmi）/ Watch 5", time="2026（在售）",
   url="https://www.mi.com/sg/product/redmi-watch-5", sources="小米官方", note="入门 24天续航表"),
 dict(title="华为智能眼镜 2（钛空圆框光学镜）", domain="AR-VR眼镜/AI/音频", stars="★★★★", status="released", source="B",
   signal="在售（钛空圆框光学镜）", confirm="1（京东/华为官方）",
   params="钛空圆框光学镜；盘古 + 小艺大模型；开放式音频；轻盈钛合金镜框；语音助手/导航/翻译；可配度数镜片",
   tech="AI 音频眼镜 + 盘古/小艺 + 钛合金轻量 + 开放式音频",
   why="华为智能眼镜 2 钛空圆框光学镜以钛合金轻量镜框结合盘古 + 小艺大模型，开放式音频 + 语音导航/翻译服务随身 AI 助手，补全华为可穿戴音频线。",
   related="AR-VR AI/NPU、音频、结构（钛合金轻量）。",
   vendor="华为 / 智能眼镜 2", time="2026（在售）",
   url="https://item.jd.com/100211153870.html", sources="京东、华为官方", note="盘古小艺 AI 音频眼镜"),
 dict(title="机械革命 翼龙 15 Air", domain="笔记本电脑/SoC/GPU/散热", stars="★★★★", status="released", source="B",
   signal="在售（轻薄游戏本）", confirm="1（今日头条/机械革命官方）",
   params="新平台处理器；独显 GPU；15 英寸轻薄机身；强散热（双风扇/均热板）；高刷屏；长续航与便携兼顾",
   tech="轻薄游戏本 + 高性能 SoC/GPU + 强散热 + 轻薄机身",
   why="机械革命翼龙 15 Air 以 15 英寸轻薄机身融合高性能 SoC/GPU 与强散热方案，主打便携游戏本市场，平衡帧率、温度与重量。",
   related="笔记本 SoC、GPU、散热、显示、电池。",
   vendor="机械革命 / 翼龙 15 Air", time="2026（在售）",
   url="https://www.toutiao.com/article/7672678984479539721/", sources="今日头条、机械革命官方", note="轻薄游戏本"),
 dict(title="联想 昭阳 X5 Air", domain="笔记本电脑/SoC/结构", stars="★★★★", status="released", source="B",
   signal="全新上市（8/4）", confirm="1（今日头条/联想中国官方）",
   params="12.9mm 超薄；低至 1kg；A/C/D 三面金属；英特尔酷睿 Ultra7（MoP 封装 LPDDR5x）；54.7/65Wh 电池；Fn+Q；双 SSD；1 小时充至 80%",
   tech="商务轻薄本 + 酷睿Ultra7 + 1kg + MoP 封装内存 + 快充",
   why="联想昭阳 X5 Air 作为昭阳 X 系列首款 1kg 轻薄本，12.9mm 金属机身 + 酷睿 Ultra7（MoP 封装 LPDDR5x）主打 AI 办公与全天候续航，1 小时充至 80% 缓解补能焦虑。",
   related="笔记本 SoC（酷睿Ultra/NPU）、结构（1kg金属）、电池快充、AI/NPU。",
   vendor="联想（昭阳）/ X5 Air", time="2026-08-04（上市）",
   url="https://www.toutiao.com/article/7670070319457059355", sources="今日头条、联想中国官方", note="1kg 商务轻薄本"),
 dict(title="小度智能屏 X10 Ultra", domain="智能音箱/音频/AI", stars="★★★★", status="released", source="B",
   signal="在售评测（8/4）", confirm="1（搜狐/小度官方）",
   params="10.1 英寸屏；360° 全景看护；文心大模型；1099 元；家庭看护/视频/智能中控",
   tech="智能屏 + 10.1寸 + 360°看护 + 文心大模型",
   why="小度智能屏 X10 Ultra 以 10.1 英寸屏与 360° 全景看护切入家庭智能中枢，文心大模型赋能语音交互与看护，1099 元主打高性价比带屏音箱。",
   related="智能音箱 音频、显示（触屏）、AI/NPU（文心）、无线通信。",
   vendor="小度 / 智能屏 X10 Ultra", time="2026-08-04（在售）",
   url="https://www.sohu.com/a/1058397816_122645258", sources="搜狐、小度官方", note="文心大模型带屏音箱"),
 dict(title="绿联 25W 磁吸无线充电器", domain="无线充/认证/BMS", stars="★★★★", status="released", source="B",
   signal="在售（6/19）", confirm="1（IT之家/绿联官方）",
   params="25W 磁吸无线充；N48H 磁体、8N 磁力；Themal Guard 温控；适配 iPhone 12-17；139 元",
   tech="Qi2 磁吸无线充 + 25W + N48H 磁体 + 温控 BMS",
   why="绿联 25W 磁吸无线充以 N48H 磁体与 8N 磁力保证吸附稳固，Themal Guard 温控 + 139 元定价切入高性价比磁吸生态，适配 iPhone 12-17。",
   related="无线充、认证（Qi2）、BMS/电源温控、结构（磁吸）。",
   vendor="绿联（UGREEN）/ 25W 磁吸无线充", time="2026-06-19（在售）",
   url="https://www.ithome.com/0/966/361.htm", sources="IT之家、绿联官方", note="Qi2 25W 磁吸充"),
 dict(title="小米三款旗舰平板入网", domain="平板/SoC/认证", stars="★★★", status="progress", source="B",
   signal="进行中（工信部入网）", confirm="1（微博/CMIIT 入网）",
   params="三款小米平板通过工信部入网；含旗舰型号；自研芯片/高刷屏/快充；具体型号与参数陆续公示",
   tech="旗舰平板矩阵 + 自研 SoC + 高刷 + 百瓦快充（进行中）",
   why="小米三款旗舰平板集体入网，标志小米平板旗舰矩阵进入发布倒计时，自研芯片 + 高刷屏 + 百瓦快充组合预计重塑安卓平板性能梯队。",
   related="平板 SoC、显示、电池快充、认证（入网）、AI/NPU。",
   vendor="小米 / 三款旗舰平板（入网）", time="2026-08-15（入网进行中）",
   url="https://weibo.com/1640337222/5332130609234801", sources="微博、工信部入网", note="三款平板入网进行中"),
]

# ================= 国际 15 条（状态排序：coming→released，时间倒序） =================
intl = [
 dict(title="RedMagic Astra 2 游戏平板", domain="平板/SoC/显示/电池", stars="★★★★", status="coming", source="C",
   signal="即将上市（Upcoming）", confirm="1（Smartprix 汇总）",
   params="骁龙 8 Elite Gen 5；12GB；8300mAh + 80W；9.06 英寸 1504×2400 165Hz；Android 16；₹47,990",
   tech="电竞平板 + 骁龙8 Elite Gen5 + 165Hz + 80W",
   why="RedMagic Astra 2 以骁龙 8 Elite Gen 5 与 9.06 英寸 165Hz 高刷屏切入电竞平板，8300mAh + 80W 快充保障重度游戏续航，₹47,990 定位高端游戏平板。",
   related="平板 SoC、显示（165Hz）、电池快充、散热、GPU。",
   vendor="红魔（努比亚）/ Astra 2", time="2026（Upcoming）",
   url="https://www.smartprix.com/tablets/redmagic-astra-2-gaming-tablet-ppd1qk0pge43", sources="Smartprix", note="骁龙8 Elite Gen5 电竞平板"),
 dict(title="Honor Pad V9", domain="平板/SoC/显示/电池", stars="★★★", status="coming", source="C",
   signal="即将上市（Upcoming）", confirm="1（Smartprix 汇总）",
   params="天玑 8350；8GB；10100mAh + 66W；11.5 英寸 2800×1840 144Hz；Android 15；₹22,990",
   tech="大屏长续航平板 + 天玑8350 + 144Hz + 10100mAh",
   why="Honor Pad V9 以 11.5 英寸 144Hz 与 10100mAh 大电池切入大屏长续航平板，天玑 8350 平衡性能与功耗，₹22,990 主打中端性价比。",
   related="平板 SoC、显示（144Hz）、电池快充。",
   vendor="荣耀 / Pad V9", time="2026（Upcoming）",
   url="https://www.smartprix.com/tablets/honor-pad-v9-ppd1rn12ucjy", sources="Smartprix", note="10100mAh 长续航平板"),
 dict(title="Xiaomi Redmi Pad 3 Pro 5G", domain="平板/SoC/电池", stars="★★★", status="coming", source="C",
   signal="即将上市（Upcoming）", confirm="1（Smartprix 汇总）",
   params="八核处理器；8GB；12500mAh + 33W；12.1 英寸 1600×2560；5G；₹30,999",
   tech="大电池 5G 平板 + 12500mAh + 5G 通信",
   why="Xiaomi Redmi Pad 3 Pro 5G 以 12500mAh 超大电池与 5G 通信切入移动生产力平板，12.1 英寸 2K 屏 + ₹30,999 定位中端 5G 平板。",
   related="平板 SoC、电池（12500mAh）、无线通信（5G）、显示。",
   vendor="小米（Redmi）/ Pad 3 Pro 5G", time="2026（Upcoming）",
   url="https://www.smartprix.com/tablets/xiaomi-redmi-pad-3-pro-5g-ppd1z6bmkbx7", sources="Smartprix", note="12500mAh 5G 平板"),
 dict(title="Lenovo ThinkTab X11 Gen 1", domain="平板/SoC/显示/电池", stars="★★★", status="coming", source="C",
   signal="即将上市（Upcoming）", confirm="1（Smartprix 汇总）",
   params="骁龙 7s Gen 3；8GB/256GB；10200mAh；10.95 英寸 2560×1600 90Hz；5G/Wi-Fi/NFC；₹19,999",
   tech="商务平板 + 骁龙7s Gen3 + 90Hz + 5G",
   why="Lenovo ThinkTab X11 Gen 1 以骁龙 7s Gen 3 与 10.95 英寸 2K 90Hz 切入商务平板，10200mAh + 5G/NFC 兼顾移动办公与通信，₹19,999 主打入门商务。",
   related="平板 SoC、显示、电池、无线通信（5G/NFC）。",
   vendor="联想 / ThinkTab X11 Gen 1", time="2026（Upcoming）",
   url="https://www.smartprix.com/tablets/lenovo-thinktab-x11-gen-1-ppd1fbag5asc", sources="Smartprix", note="骁龙7s 商务平板"),
 dict(title="Oakley Meta HSTN 运动 AI 眼镜", domain="AR-VR眼镜/AI/摄像头", stars="★★★★", status="coming", source="B",
   signal="发布（运动聚焦 AI 眼镜）", confirm="1（AI Crunch X / Meta 官方）",
   params="Meta 首款运动聚焦 AI 眼镜；Oakley 联名；摄像头拍摄；电池续航；AI 助手；运动场景",
   tech="运动 AI 眼镜 + Meta + 拍摄 + 语音助手",
   why="Oakley Meta HSTN 是 Meta 首款聚焦运动的 AI 眼镜，Oakley 联名镜框 + 拍摄/AI 助手切入运动记录与随身计算，补全 Meta 可穿戴产品矩阵。",
   related="AR-VR 显示、AI/NPU、摄像头、音频、结构（运动镜框）。",
   vendor="Meta × Oakley / HSTN", time="2026（发布）",
   url="https://www.aicrunchx.com/oakley-meta-hstn-metas-first-sport-focused-ai-glasses-launch", sources="AI Crunch X、Meta官方", note="Meta 运动 AI 眼镜"),
 dict(title="Google AI Glasses", domain="AR-VR眼镜/AI/显示", stars="★★★★", status="coming", source="B",
   signal="预热（预计上市）", confirm="1（Renovate QR 汇总）",
   params="Gemini 深度集成；显示方案（预计 Micro-LED 光波导）；AI 实时翻译/导航/问答；轻量设计；与三星/眼镜厂合作",
   tech="消费级 AI 眼镜 + Gemini + 光波导显示 + 实时 AI",
   why="Google AI Glasses 以 Gemini 深度集成与光波导显示切入下一代随身 AI 终端，实时翻译/导航/问答服务日常，是 Google 在 AI 眼镜赛道的核心落子。",
   related="AR-VR 显示（光波导）、AI/NPU（Gemini）、音频、结构（轻量）。",
   vendor="Google / AI Glasses", time="2026（预热/待上市）",
   url="https://renovateqr.com/blog/best-ai-smart-glasses-2026", sources="Renovate QR 汇总、Google", note="Gemini AI 眼镜"),
 dict(title="Redmi Note 17 5G", domain="手机/SoC/电池/快充", stars="★★★★", status="released", source="B",
   signal="已发布（中国 7/14，印度预计 8/6）", confirm="1（Smartprix India 汇总）",
   params="骁龙 4 Gen 4；8000mAh + 45W（22.5W 反向）；7 英寸 FHD+ OLED 120Hz、1800nits、3840Hz PWM；中国 CNY 1,299",
   tech="长续航手机 + 骁龙4 Gen4 + 8000mAh + OLED 120Hz",
   why="Redmi Note 17 5G 以 8000mAh 超大电池与 7 英寸 OLED 120Hz 切入长续航大屏，骁龙 4 Gen 4 + 45W 快充 + 反向充电覆盖重度使用，中国 1299 元起性价比突出。",
   related="手机 SoC、电池快充、显示-OLED、无线通信（5G）。",
   vendor="小米（Redmi）/ Note 17 5G", time="2026-07-14（中国发布）",
   url="https://us.smartprix.com/bytes/upcoming-smartphone-launches-in-india-august-2026/", sources="Smartprix India", note="8000mAh 长续航大屏"),
 dict(title="Poco M8 Power 5G", domain="手机/SoC/电池", stars="★★★", status="released", source="B",
   signal="印度发布（8/4）", confirm="1（Smartprix India 汇总）",
   params="骁龙 4 Gen 4；8000mAh + 45W；7 英寸 AMOLED 120Hz、1800nits；Flipkart 印度发布；预计 < ₹20,000",
   tech="长续航手机 + 骁龙4 Gen4 + 8000mAh + AMOLED",
   why="Poco M8 Power 5G 于 8/4 在印度发布，与 Redmi Note 17 高度同平台（骁龙 4 Gen 4 + 8000mAh），7 英寸 AMOLED 120Hz 主打印度长续航性价比市场。",
   related="手机 SoC、电池快充、显示-AMOLED、无线通信（5G）。",
   vendor="小米（Poco）/ M8 Power 5G", time="2026-08-04（印度发布）",
   url="https://us.smartprix.com/bytes/upcoming-smartphone-launches-in-india-august-2026/", sources="Smartprix India", note="印度长续航性价比机"),
 dict(title="Samsung Galaxy F70 Pro 5G", domain="手机/SoC/电池", stars="★★★", status="released", source="B",
   signal="印度发布（8/3，价格已公布）", confirm="1（Smartprix India 汇总）",
   params="骁龙 6 Gen 3；6000mAh + 45W；6.7 英寸 FHD+ sAMOLED 120Hz、Victus+；₹25,999 起（6+128）/ ₹29,999 / ₹34,999",
   tech="中端手机 + 骁龙6 Gen3 + 6000mAh + sAMOLED",
   why="Samsung Galaxy F70 Pro 5G 于 8/3 在印度发布并公布完整价格，骁龙 6 Gen 3 + 6000mAh + 6.7 英寸 sAMOLED 120Hz 主打三星中端长续航，₹25,999 起对抗国产性价比机型。",
   related="手机 SoC、电池快充、显示-AMOLED、结构（Victus+玻璃）。",
   vendor="三星 / Galaxy F70 Pro 5G", time="2026-08-03（印度发布）",
   url="https://us.smartprix.com/bytes/upcoming-smartphone-launches-in-india-august-2026/", sources="Smartprix India、Samsung India", note="三星中端长续航机"),
 dict(title="Garmin Instinct 本我系列 新配色", domain="智能手表/传感器/结构", stars="★★★★", status="released", source="B",
   signal="在售（军风配色）", confirm="1（买得易/ Garmin 官方）",
   params="军规三防；多频 GPS；心率/血氧/海拔；太阳能续航；军风新配色；户外耐用",
   tech="户外军规腕表 + 多频GPS + 太阳能 + 三防",
   why="Garmin Instinct 本我系列推出军风新配色，军规三防 + 多频 GPS + 太阳能续航延续户外耐用定位，服务徒步/登山等严苛场景。",
   related="智能手表 传感器（GPS/气压/心率）、结构（军规）、电池（太阳能）。",
   vendor="Garmin / Instinct 本我系列", time="2026（在售）",
   url="https://www.maideyi.com/a41881", sources="买得易、Garmin官方", note="军规太阳能户外表"),
 dict(title="COROS Vertix 新旗舰", domain="智能手表/传感器/导航", stars="★★★★", status="released", source="B",
   signal="亮相（UTMB 2026 倒计时）", confirm="1（Watches Reviewed 汇总）",
   params="高端户外/登山旗舰；UTMB 2026（8 月底）前发布；长续航；多频卫星定位；海拔/气压；蓝宝石/钛合金",
   tech="登山旗舰表 + 多频卫星 + 长续航 + 钛合金",
   why="COROS 于 UTMB 2026（8 月底）前预热新 Vertix 旗舰，面向高海拔登山与超马，多频卫星定位 + 长续航 + 钛合金/蓝宝石强化专业户外能力。",
   related="智能手表 传感器（GPS/气压/海拔）、结构（钛合金）、电池（长续航）、导航。",
   vendor="COROS（高驰）/ Vertix 新旗舰", time="2026-08（UTMB 前发布）",
   url="https://watchesreviewed.com/coros-vertix-new-watch-teaser-utmb-2026/", sources="Watches Reviewed、COROS", note="UTMB 登山旗舰表"),
 dict(title="ASUS TUF A16 (2026)", domain="笔记本电脑/SoC/GPU/散热", stars="★★★★", status="released", source="B",
   signal="印度发布（8/6）", confirm="1（Tech Stories India / 华硕）",
   params="AMD Ryzen 7 260；RTX 5060 8GB GDDR7（115W）；16 英寸 FHD+ 144Hz；16GB DDR5；512GB；2.2kg；₹1,99,990；MIL-STD-810H",
   tech="游戏本 + Ryzen7 260 + RTX5060 + 军规耐用",
   why="ASUS TUF A16 (2026) 于 8/6 在印度发布，Ryzen 7 260 + RTX 5060 8GB 切入主流游戏本，16 英寸 144Hz + MIL-STD-810H 军规耐用兼顾帧率与可靠性。",
   related="笔记本 SoC（Ryzen/NPU）、GPU、散热、显示、结构（军规）。",
   vendor="华硕 / TUF A16 2026", time="2026-08-06（印度发布）",
   url="https://techstoriesindia.in/2026/08/asus-tuf-a16-fa608umi-tu288ws-price-india-specs-amazon/", sources="Tech Stories India、华硕", note="Ryzen7+RTX5060 游戏本"),
 dict(title="Lenovo LOQ 15AHP10 (2026)", domain="笔记本电脑/SoC/GPU", stars="★★★", status="released", source="B",
   signal="印度发布（8 月）", confirm="1（Tech Stories India / 联想）",
   params="AMD Ryzen 7 250；RTX 5060 8GB GDDR7（100W TGP，572 AI TOPS）；15.6 英寸 144Hz FHD；16GB DDR5；512GB；₹1,70,990",
   tech="游戏本 + Ryzen7 250 + RTX5060 + AI TOPS",
   why="Lenovo LOQ 15AHP10 (2026) 于 8 月在印度发布，Ryzen 7 250 + RTX 5060（100W/572 AI TOPS）切入主流游戏本，15.6 英寸 144Hz 兼顾高帧与本地 AI 算力。",
   related="笔记本 SoC（Ryzen/NPU）、GPU、散热、显示、AI/NPU。",
   vendor="联想 / LOQ 15AHP10 2026", time="2026-08（印度发布）",
   url="https://techstoriesindia.in/2026/08/lenovo-laptops-august-2026-new-launches-amazon-india", sources="Tech Stories India、联想", note="Ryzen7+RTX5060 游戏本"),
 dict(title="Mophie Qi2.2 StealthCharge 无线充", domain="无线充/认证/BMS", stars="★★★★", status="released", source="B",
   signal="发布（6/16）", confirm="1（The Verge / Mophie 官方）",
   params="Qi2.2 磁吸；持续 25W；StealthCharge 技术（线圈移至底座 + 散热片，无风扇）；4-in-1 / 3-in-1 / Roam 三合一旅行充；Apple Store 独占；$149.95-$179.95",
   tech="Qi2.2 磁吸无线充 + 25W + 无风扇静音散热 + 三合一",
   why="Mophie 于 6/16 推出 StealthCharge 技术，将 Qi2.2 充电组件移至底座并用散热片导热，实现持续 25W 且无风扇静音，4-in-1/3-in-1/Roam 三形态覆盖居家与旅行。",
   related="无线充、认证（Qi2.2/WPC）、BMS/电源温控、结构（无风扇）。",
   vendor="Mophie / StealthCharge Qi2.2", time="2026-06-16（发布）",
   url="https://www.theverge.com/tech/950192/mophie-stealthcharge-wireless-charger-qi2-stands-travel", sources="The Verge、Mophie官方", note="Qi2.2 无风扇静音充"),
 dict(title="Marshall Stockwell III 便携音箱", domain="智能音箱/音频/结构", stars="★★★★", status="released", source="B",
   signal="发布（6/10）", confirm="1（今日头条/DoNews）",
   params="约 35 小时续航；True Stereophonic 360° 环绕声；IP55 防尘防水；动态响度；模块化可维修；黑金/油彩白；1699 元",
   tech="便携蓝牙音箱 + 360°环绕声 + IP55 + 模块化可维修",
   why="Marshall Stockwell III 于 6/10 发布，约 35 小时续航 + True Stereophonic 360° 环绕声切入便携音箱，IP55 三防 + 模块化可维修（含 27% 再生材料）兼顾户外与可持续。",
   related="智能音箱 音频、结构（IP55/模块化）、电池、无线通信（蓝牙）。",
   vendor="Marshall / Stockwell III", time="2026-06-10（发布）",
   url="https://www.toutiao.com/article/7649600842622616104", sources="今日头条、DoNews、Marshall官方", note="35h 360° 便携音箱"),
]

# ================= Top 5 重点信号（星级降序→信源等级→状态→时间倒序） =================
top5 = [
 dict(title="小米 MIX Fold 5", dim="手机/折叠屏/SoC", stars="★★★★★",
      key="玄戒O3 3nm + 双2亿徕卡 + 6000mAh硅碳，8月底发布"),
 dict(title="华为 MatePad Pro 2026", dim="平板/显示/电池", stars="★★★★",
      key="鸿蒙高端平板首销，8/14 开售"),
 dict(title="iQOO Z11S", dim="手机/电池/快充", stars="★★★★",
      key="10000mAh + IP69 + 天玑7500满血，8/18 发布"),
 dict(title="Oakley Meta HSTN", dim="AR-VR/AI", stars="★★★★",
      key="Meta 首款运动 AI 眼镜，Oakley 联名"),
 dict(title="RedMagic Astra 2", dim="平板/游戏/SoC", stars="★★★★",
      key="骁龙8 Elite Gen5 + 165Hz + 80W，电竞平板"),
]

# ================= 16 维技术覆盖面板（全亮 16/16） =================
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
