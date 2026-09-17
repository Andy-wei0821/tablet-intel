# -*- coding: utf-8 -*-
# Generator for WB_2026-09-17_硬件看板.html
# Single HTML, inline CSS, no CDN. 30 cards (CN15 + INTL15).
import datetime

DATE = "2026-09-17"
TITLE = "智能终端硬件情报日报 · " + DATE

# 16 technical dimensions (canonical order for coverage panel)
DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

# Each item: keys
# region, title, category, dim, status, date, source_tier, source_name, url,
# corroboration, stars, vendor, signal_type, key_params, tech_features(list),
# why_important, terminal_link, note
ITEMS = [
 # ---------- CN (1-15) ----------
 {"region":"国内","title":"华为 MatePad Pro 12 英寸(2026) 全球发布：4.7mm 超薄 + 自研麒麟 T93 旗舰生产力平板",
  "category":"平板","dim":"结构/工艺","status":"已上市","date":"2026-09-03","source_tier":"A",
  "source_name":"华为官方（慕尼黑全球发布会 / 美通社通稿）","url":"https://www.toutiao.com/article/7681310334514217499",
  "corroboration":2,"stars":5,"vendor":"华为 MatePad Pro 12(2026)","signal_type":"新品发布",
  "key_params":"12 英寸、4.7mm 超薄一体化金属机身、自研麒麟 T93 芯片、10400mAh 电池、专业生产力定位",
  "tech_features":["4.7mm 超薄一体化金属机身，重量与厚度行业领先","自研麒麟 T93 平台，性能与能效旗舰级","10400mAh 大电池支撑全天生产力","HarmonyOS 全场景生态，平板/手机/PC 协同"],
  "why_important":"华为下半年旗舰平板核心迭代，定义高端生产力平板硬件基准，直接影响竞品产品定义与对标。",
  "terminal_link":"对标 TCL 平板旗舰的屏幕、厚度、续航与生态协同能力。",
  "note":"慕尼黑全球首发、国内随后上市；对应 MatePad Pro 12(2026)，不在 14 天去重表。"},

 {"region":"国内","title":"vivo Pad5 Pro 上架：13 英寸 3.1K 144Hz + 天玑 9400 + 12050mAh",
  "category":"平板","dim":"SoC/芯片","status":"已上市","date":"2026-09-09","source_tier":"A",
  "source_name":"vivo 官方网站产品页","url":"https://www.vivo.com.cn/vivo/vivopad5pro/",
  "corroboration":3,"stars":5,"vendor":"vivo Pad5 Pro","signal_type":"新品上市",
  "key_params":"13 英寸 3.1K 144Hz、天玑 9400、12050mAh、66W 快充、40600mm² 散热、5.96mm/578g",
  "tech_features":["天玑 9400 旗舰平台，蓝晶芯片技术栈","13 英寸 3.1K 144Hz 高刷大屏","40600mm² 均热板散热，重度负载稳帧","OriginOS 5 HD + 小 V 帮记同声传译、PC 级 WPS/CAJ"],
  "why_important":"vivo 旗舰平板补齐大屏生产力与 AI 会议能力，直接对标同档安卓平板产品定义。",
  "terminal_link":"对标天玑旗舰平板的散热与 AI 会议能力，供 TCL 平板规划参考。",
  "note":"9 月 9 日官宣上架，国内在售；非去重表内任何 vivo/其他型号。"},

 {"region":"国内","title":"OPPO Pad 5 标准版亮相：12.1 英寸 2.8K 144Hz + 天玑 9400+ + 5.99mm 金属一体",
  "category":"平板","dim":"手写笔/触控","status":"已上市","date":"2026-09-09","source_tier":"A",
  "source_name":"OPPO 官方支持页","url":"https://support.oppo.com/cn/answer/?aid=2254580",
  "corroboration":2,"stars":5,"vendor":"OPPO Pad 5 标准版","signal_type":"新品上市",
  "key_params":"12.1 英寸 LCD 2.8K 144Hz、天玑 9400+、10420mAh、67W、5.99mm/577g、AI 字迹美化",
  "tech_features":["金属一体化机身，5.99mm 轻薄","天玑 9400+ 旗舰平台","魔力触控笔二代 + 智能磁吸键盘","ColorOS 16 + O+ 互联，AI 字迹美化"],
  "why_important":"OPPO 数字旗舰平板标准版，轻薄金属 LCD 平板厚度突破，强化安卓平板生态。",
  "terminal_link":"对标轻薄金属平板与主动笔体验，供 TCL 平板工艺参考。",
  "note":"为 Pad 5 标准版，独立于已去重的 OPPO Pad 5 柔光版。"},

 {"region":"国内","title":"小米平板 9 Pro 开启预售：12.5 英寸 3.2K 144Hz + 第五代骁龙 8 + 11000mAh",
  "category":"平板","dim":"电池/快充","status":"即将上市","date":"2026-09-14","source_tier":"C",
  "source_name":"中关村在线（ZOL）平板电脑频道","url":"https://pad.zol.com.cn/1248/12481086.html",
  "corroboration":2,"stars":4,"vendor":"小米平板 9 Pro","signal_type":"预售开启",
  "key_params":"12.5 英寸 LCD 3.2K 144Hz、第五代骁龙 8、11000mAh、67W 有线 + 22.5W 反向、5.8mm/494g",
  "tech_features":["莱茵 TÜV 节律/无频闪/硬件低蓝光","澎湃 OS 4 + PC 级专业应用","超级小爱 2.0 语音助手","11000mAh 大电池 + 67W 快充"],
  "why_important":"小米平板数字旗舰迭代，11000mAh 大电池 + 旗舰芯拉升安卓平板续航与性能基准。",
  "terminal_link":"对标大电池安卓平板续航方案，供 TCL 平板电源规划参考。",
  "note":"Pro 版独立于已去重的「小米平板 9 Pro Max」与「小米平板 9 标准版」，按子串规则可采集。"},

 {"region":"国内","title":"OPPO Find X10 Pro Max 定档 9/22：全球首批 2nm 天玑 9600 Pro + 三 2 亿像素 + 8000mAh",
  "category":"手机","dim":"摄像头","status":"即将上市","date":"2026-09-22","source_tier":"A",
  "source_name":"OPPO 官方确认（联发科联合）","url":"https://www.gizguide.com/2026/09/oppo-find-x10-pro-max-dimensity-9600-pro.html",
  "corroboration":3,"stars":5,"vendor":"OPPO Find X10 Pro Max","signal_type":"发布预告",
  "key_params":"天玑 9600 Pro（TSMC 2nm N2P）、三 2 亿像素（主摄+超广角+潜望）、8000mAh 硅碳、100W/50W 无线",
  "tech_features":["Laminar Flow Engine 散热架构","哈苏影像，三 2 亿像素系统","Tiangong Screen 2.0 0.99mm 四等边","ColorOS 17，8000mAh 硅碳电池"],
  "why_important":"首批 2nm 旗舰 SoC 落地，三 2 亿像素重新定义影像旗舰硬件上限。",
  "terminal_link":"2nm 平台与三 2 亿影像方案是 TCL 手机产品定义的标杆信号。",
  "note":"9 月 22 日国内发布，非去重表内 OPPO 机型。"},

 {"region":"国内","title":"荣耀 Magic9 Pro Max 将发：10000nits 黑钻屏 + 骁龙 8 Elite Gen6 Pro 2nm + 双 3D 生物识别",
  "category":"手机","dim":"生物识别","status":"即将上市","date":"2026-09-28","source_tier":"A",
  "source_name":"荣耀官方发布会专题页","url":"https://www.honor.com/cn/activity/honor-magic9-series-launch/",
  "corroboration":3,"stars":5,"vendor":"荣耀 Magic9 Pro Max","signal_type":"发布预告",
  "key_params":"6.8 英寸 OLED 黑钻屏 10000nits、骁龙 8 Elite Gen6 Pro（2nm）、8800mAh+100W、3D 超声波指纹+3D 人脸",
  "tech_features":["ARRI 双 2 亿影像","MagicOS 11","IP68/69K 三防","独立物理拍照键 + AI 快捷按键","双 3D 生物识别（超声波指纹+人脸）"],
  "why_important":"荣耀年度影像旗舰，2nm 平台 + 万尼特屏 + 双 3D 生物识别拉高旗舰硬件门槛。",
  "terminal_link":"双 3D 生物识别与安全/影像方案供 TCL 手机定义参考。",
  "note":"9 月 28 日北京发布；候选不含去重表「荣耀 Magic9 超能版」子串，可采集。"},

 {"region":"国内","title":"OPPO Watch S2 将发：8.9mm 圆表 + FatMax 燃脂 + 98.8% 心率精度",
  "category":"智能手表","dim":"传感器","status":"即将上市","date":"2026-09-22","source_tier":"C",
  "source_name":"Notebookcheck（转引 OPPO 微博官宣）","url":"https://www.notebookcheck.net/Oppo-teases-Watch-S2-ahead-of-September-22-launch.1400948.0.html",
  "corroboration":3,"stars":4,"vendor":"OPPO Watch S2","signal_type":"发布预告",
  "key_params":"8.9mm/34.4g 圆表、FatMax 燃脂模式、光学传感器抗干扰+75%、98.8% 运动心率精度、ECG/血氧/腕温、10 天续航",
  "tech_features":["个性化燃脂心率区 FatMax","双机互联","Watch Fluid Cloud 实时活动小组件","三色配色，34.4g 轻量圆表"],
  "why_important":"OPPO 健康向圆表迭代，FatMax 与高精度传感定义运动健康手表新卖点。",
  "terminal_link":"高精度运动心率传感方案供 TCL 穿戴规划参考。",
  "note":"9 月 22 日随 Find X10 系列发布；非去重表内 OPPO Watch X3。"},

 {"region":"国内","title":"华米 Amazfit Cheetah 2 Ultra 越野跑表发布：30 天续航 + 双频六星 GPS + 钛合金",
  "category":"智能手表","dim":"无线通信","status":"已上市","date":"2026-09-10","source_tier":"D",
  "source_name":"腾讯新闻","url":"https://so.html5.qq.com/page/real/search_news?docid=70000021_0016aa1871932652",
  "corroboration":1,"stars":3,"vendor":"华米科技（Amazfit）Cheetah 2 Ultra","signal_type":"新品发布",
  "key_params":"30 天续航、GPS 精准模式 60h、双频六星圆极化天线、5 级航空钛、1.5 英寸 3000nit AMOLED、4299 元",
  "tech_features":["全彩等高离线地图","CP 分段海拔","双模式返航","白红光手电 + SOS","HYROX 专项训练"],
  "why_important":"国产越野跑表冲击高端，长续航 + 精准定位 + 钛合金用料对标佳明/高驰。",
  "terminal_link":"双频六星定位与长续航方案供 TCL 穿戴规划参考。",
  "note":"国内发布报道；非去重表内 Amazfit/华米任何型号。"},

 {"region":"国内","title":"亮亮视野 Leion Hey2 AR 翻译眼镜服贸会亮相：49g、100+ 语种、8h 续航",
  "category":"AR-VR眼镜","dim":"AI/NPU","status":"已上市","date":"2026-09-10","source_tier":"D",
  "source_name":"手机新浪网","url":"https://www.sina.cn/news/detail/5306814603461133.html",
  "corroboration":1,"stars":3,"vendor":"亮亮视野（LLVision）Leion Hey2","signal_type":"展会亮相/国内推广",
  "key_params":"49g、100+ 语种实时互译、8h 续航、四阵列麦克风、恒玄 BES2800、MicroLED 波导 1500-2500nit",
  "tech_features":["无摄像头/无外放隐私设计","定向传声","离线翻译","演讲提词","会议转写纪要"],
  "why_important":"国产专用翻译 AR 眼镜代表，轻量化 + 长续航破解行业不可能三角，服贸会强化国内曝光。",
  "terminal_link":"轻量翻译 AR 眼镜范式供 TCL AR 眼镜规划参考。",
  "note":"服贸会（9/9-10）展出，产品此前已上市；归入国内区硬件曝光情报。"},

 {"region":"国内","title":"星纪魅族 MYVU 眼镜接入腾讯 WorkBuddy：43g + MicroLED 2000nit + 翻译 95%",
  "category":"AR-VR眼镜","dim":"显示/OLED","status":"已上市","date":"2026-09-02","source_tier":"C",
  "source_name":"叁发未来（行业观察）","url":"https://tkfff.cn/industry/210.html",
  "corroboration":2,"stars":4,"vendor":"星纪魅族（MYVU）","signal_type":"生态合作/AI 能力升级",
  "key_params":"43g、单层树脂衍射光波导 + 0.3cc MicroLED、2000nit、翻译准确率 95%+、183mAh/3h",
  "tech_features":["Flyme AI 大模型","实时翻译/导航/提词/转写","WorkBuddy AI Agent 多端延伸","43g 轻量日常佩戴"],
  "why_important":"AI Agent 首次从手机/电脑明确延伸到可穿戴眼镜，重塑智能眼镜入口价值。",
  "terminal_link":"AI Agent 眼镜入口范式供 TCL 智能终端协同参考。",
  "note":"9 月 1 日官宣、9 月 2 日深圳生态发布会；非去重表内任何 AR 眼镜型号。"},

 {"region":"国内","title":"微星 神影 18 AI 2026 游戏本发布：18 英寸 2.5K 240Hz + 酷睿 Ultra 200HX + RTX50",
  "category":"笔记本电脑","dim":"散热","status":"已上市","date":"2026-09-10","source_tier":"D",
  "source_name":"今日头条","url":"https://www.toutiao.com/article/7683730004777239055/",
  "corroboration":1,"stars":3,"vendor":"微星（MSI）神影 18 AI 2026","signal_type":"新品上市",
  "key_params":"18 英寸 2.5K 240Hz、酷睿 Ultra 200HX、RTX 50 系独显、Cooler Boost 散热",
  "tech_features":["AI 游戏本","高刷大屏","旗舰 CPU+GPU 组合","强化散热模组"],
  "why_important":"微星大屏 AI 游戏本迭代，2.5K 高刷 + 旗舰平台定义高端游戏本硬件基准。",
  "terminal_link":"高刷大屏游戏本散热方案供 TCL 笔电规划参考。",
  "note":"9 月 10 日国内报道；非去重表内机型。"},

 {"region":"国内","title":"微星 神影 16 MAX 2026 发布：Ultra 9 290HX Plus + RTX5060 + 200W 双烤",
  "category":"笔记本电脑","dim":"BMS/电源","status":"已上市","date":"2026-09-11","source_tier":"D",
  "source_name":"腾讯新闻","url":"https://new.qq.com/rain/a/20260911A02DIB00",
  "corroboration":1,"stars":3,"vendor":"微星（MSI）神影 16 MAX 2026","signal_type":"新品上市",
  "key_params":"Ultra 9 290HX Plus、RTX 5060、200W 双烤功耗、16 英寸高刷屏",
  "tech_features":["旗舰 HX 处理器","独显","双烤散热与供电设计","AI 游戏本定位"],
  "why_important":"补齐 16 英寸高性能机型，200W 双烤供电体现高端游戏本电源/散热规格。",
  "terminal_link":"高功耗双烤供电方案供 TCL 笔电电源规划参考。",
  "note":"9 月 11 日报道；非去重表内机型。"},

 {"region":"国内","title":"安克快充护机系列三折叠风冷无线充发布：25W 三合一 + 主动风冷",
  "category":"无线充","dim":"认证/合规","status":"已上市","date":"2026-09-08","source_tier":"D",
  "source_name":"今日头条","url":"https://www.toutiao.com/article/7683101901294076459",
  "corroboration":1,"stars":3,"vendor":"安克（Anker）快充护机系列","signal_type":"新品上市",
  "key_params":"25W 无线充、三折叠结构、内置主动风冷、三合一（手表/耳机/手机）",
  "tech_features":["折叠风冷散热","Qi2/3C 合规","多设备同充","便携收纳"],
  "why_important":"无线充进入主动散热 + 折叠形态，Qi2.2/3C 合规推动多设备一体充新形态。",
  "terminal_link":"Qi2/3C 合规三合一无线充形态供 TCL 配件规划参考。",
  "note":"9 月 8 日报道；非去重表内 Anker MagStand/soundcore 等子型号。"},

 {"region":"国内","title":"华为 Sound X 系列获秋季升级：AI 搜歌 + 自然对话 + HiPlay 投播",
  "category":"智能音箱","dim":"音频","status":"已上市","date":"2026-09-16","source_tier":"B",
  "source_name":"IT之家（新浪科技转引）","url":"https://k.sina.com.cn/article_5953189932_162d6782c06704yeis.html",
  "corroboration":1,"stars":3,"vendor":"华为 Sound X 系列","signal_type":"OTA 能力升级",
  "key_params":"4 款 Sound X（2021/NEW/鎏金剧院版/X4）升级、AI 搜歌、自然对话、百科问答、HiPlay 投播",
  "tech_features":["AI 语音交互升级","无网一步直连 HiPlay","192kHz/24bit 超清母带","鸿蒙生态协同"],
  "why_important":"存量旗舰智能音箱获 AI 能力大版本升级，反映智能音箱从播放工具向 AI 家庭入口演进。",
  "terminal_link":"智能音箱 AI 化演进供 TCL 音频终端规划参考。",
  "note":"9 月 16 日官方宣布 OTA；为现有硬件的 AI 功能升级（非全新硬件）。"},

 {"region":"国内","title":"网易有道 OpenPods AI 耳机正式发售：7g + MFi + AI Agent 工作流",
  "category":"AI耳机·耳穿戴","dim":"音频","status":"已上市","date":"2026-09-10","source_tier":"A",
  "source_name":"新华网（news.cn）","url":"https://www.news.cn/tech/20260829/8fc452655ed141a7971f29899398f58f/c.html",
  "corroboration":4,"stars":5,"vendor":"网易有道 OpenPods","signal_type":"新品发售",
  "key_params":"单耳 7g、苹果 MFi 认证、独立智能耳机舱、20+ 语种/方言、综合续航 32h、充电舱可外放互译",
  "tech_features":["AI Agent 闭环（录音/转写/翻译/总结/问答/知识库）","音色克隆","Ask AI 音频溯源","安卓/鸿蒙规划"],
  "why_important":"全球首款面向 iPhone 的 Agent 耳机，把 AI Agent 从对话框带入真实音频工作流，定义 AI 耳机新形态。",
  "terminal_link":"AI Agent 耳机范式（与平板/手机协同）供 TCL 耳穿戴规划参考。",
  "note":"8 月 27 日预售、9 月 10 日正式发售；非去重表内任何耳机型号。"},

 # ---------- INTL (16-30) ----------
 {"region":"国际","title":"XP-Pen Magic Pro 13 安卓创作平板：12.95 英寸 3K 120Hz + 天玑 8300 + 16384 级压感笔",
  "category":"平板","dim":"手写笔/触控","status":"即将上市","date":"2026-09-05","source_tier":"A",
  "source_name":"XP-Pen 官方","url":"https://www.xp-pen.com/detail/442.html",
  "corroboration":2,"stars":4,"vendor":"XP-Pen Magic Pro 13","signal_type":"新品发布",
  "key_params":"12.95 英寸 3K LCD 120Hz / 天玑 8300 / X4 Smart Chip 触控笔(16384 级压感) / 10200mAh+45W / Android 16 / Wi-Fi 7",
  "tech_features":["独立 X4 绘图芯片触控笔","3K 120Hz 大屏","45W 快充","面向创作者安卓大屏"],
  "why_important":"将 16384 级压感主动笔与独立绘图芯片下放到中端价位，IFA 2026 创作平板亮点。",
  "terminal_link":"高规格主动笔方案供 TCL 平板手写笔规划参考。",
  "note":"预计 2026 年 10 月上市；非去重表内型号。"},

 {"region":"国际","title":"联想 Tab Plus Gen 2 安卓平板：12.1 英寸 2.5K 120Hz + 天玑 7400 + JBL 9 单元",
  "category":"平板","dim":"音频","status":"已上市","date":"2026-09-04","source_tier":"A",
  "source_name":"Lenovo 官方","url":"https://www.lenovo.com/us/en/p/tablets/android-tablets/lenovo-tab-series/lenovo-tab-plus-gen-2-12.1-inch-mediatek/len103l0038",
  "corroboration":2,"stars":4,"vendor":"Lenovo Tab Plus Gen 2","signal_type":"新品发布",
  "key_params":"12.1 英寸 2.5K LCD 120Hz / 天玑 7400 / JBL 9 单元杜比全景声 / 10200mAh+45W / Android 16 / AI Live Transcript / $399.99",
  "tech_features":["JBL 9 单元音响","AI 实时转录","7 年系统更新承诺","10200mAh 大电池"],
  "why_important":"将 JBL 多单元音响与 AI 转录带入中端安卓平板，IFA 2026 主流平板代表。",
  "terminal_link":"多单元音响 + AI 转录平板供 TCL 平板规划参考。",
  "note":"2026 年 9 月开售；非去重表内 Yoga Tab 系列。"},

 {"region":"国际","title":"苹果 iPad mini OLED（传闻）：8.4-8.7 英寸 OLED + A19 Pro + 自研 C1X 基带",
  "category":"平板","dim":"SoC/芯片","status":"即将上市","date":"2026-09-10","source_tier":"B",
  "source_name":"Macworld","url":"https://www.macworld.com/article/3060022/2026-ipad-mini-design-display-specs-release-date.html",
  "corroboration":1,"stars":3,"vendor":"Apple iPad mini（下一代）","signal_type":"泄露/爆料",
  "key_params":"8.4-8.7 英寸 OLED 60Hz / A19 Pro / Wi-Fi 7 + 自研 C1X / 预计 $699 / 预计 2026 年 10 月",
  "tech_features":["首次 mini 采用 OLED","A19 Pro 旗舰芯","自研 C1X 基带","补齐苹果平板 OLED 化版图"],
  "why_important":"iPad mini 首次拥抱 OLED，补全苹果平板 OLED 化版图，对小尺寸高端平板市场影响大。",
  "terminal_link":"小尺寸 OLED 平板趋势供 TCL 平板显示规划参考。",
  "note":"基于泄露信息，苹果尚未官宣；与 14 天去重表无冲突。"},

 {"region":"国际","title":"荣耀 MagicPad 4 12.1 英寸揭晓：165Hz + 骁龙 8s Gen4 + 10100mAh，9/28 同场发布",
  "category":"平板","dim":"显示/OLED","status":"即将上市","date":"2026-09-17","source_tier":"B",
  "source_name":"Notebookcheck","url":"https://www.notebookcheck.net/Honor-reveals-new-12-1-inch-tablet-with-165Hz-refresh-rate-and-large-battery.1394309.0.html",
  "corroboration":2,"stars":4,"vendor":"荣耀 MagicPad 4 12.1","signal_type":"发布预告",
  "key_params":"12.1 英寸 165Hz（LCD，传闻）、骁龙 8s Gen4、10100mAh、最高 12GB+256GB、支持触控笔与 PC 级应用",
  "tech_features":["12.1 英寸 165Hz 高刷","骁龙 8s Gen4 中旗舰平台","10100mAh 大电池","PC 级应用 + 触控笔生产力"],
  "why_important":"MagicPad 4 系列新增更亲民 12.1 英寸 SKU，165Hz + 大电池定义中高端平板硬件基准。",
  "terminal_link":"中高端平板 165Hz + 大电池方案供 TCL 平板规划参考。",
  "note":"与 09-07 已覆盖的 12.3 英寸 MagicPad 4 为不同 SKU（12.1 英寸新变体），按边界 SKU 口径收录。"},

 {"region":"国际","title":"索尼 Xperia 10 VIII 发布：6.1 英寸 OLED 120Hz + 骁龙 6 Gen3 + 5000mAh",
  "category":"手机","dim":"电池/快充","status":"已上市","date":"2026-08-25","source_tier":"A",
  "source_name":"Sony 官方（东南亚新闻稿）","url":"https://www.sony-asia.com/pressrelease?prName=sony-launches-xperia-10-viii-with-a-focus-on-improving-everyday-ease-of-use",
  "corroboration":1,"stars":4,"vendor":"Sony Xperia 10 VIII","signal_type":"新品发布",
  "key_params":"6.1 英寸 OLED 120Hz / 骁龙 6 Gen3 / 8GB+128GB / 5000mAh+27W / Android 16 / €599 / 9 月 18 日上市",
  "tech_features":["紧凑机身 + 大电池","OLED 120Hz","侧边指纹","索尼影像算法下放"],
  "why_important":"索尼主流价位回归 OLED 高刷，欧洲/亚洲主力走量机型。",
  "terminal_link":"紧凑 OLED 高刷机型供 TCL 手机规划参考。",
  "note":"8 月 25 日发布，9 月 18 日开售；非去重表内机型。"},

 {"region":"国际","title":"摩托罗拉 Edge 70 全球发布：6.67 英寸 P-OLED 4500nit + 68W + 5.99mm/159g 军规",
  "category":"手机","dim":"结构/工艺","status":"已上市","date":"2026-09-05","source_tier":"B",
  "source_name":"GeekChamp","url":"https://geekchamp.com/motorola-edge-70-launches-globally-from-e799",
  "corroboration":2,"stars":4,"vendor":"Motorola Edge 70","signal_type":"新品发布",
  "key_params":"6.67 英寸 P-OLED 120Hz 4500nit / 骁龙 7 Gen4 / 4800mAh+68W+15W 无线 / 5.99mm 厚 159g / IP68/IP69 MIL-STD-810H / €799 起",
  "tech_features":["极致轻薄 + 军规耐用","68W 快充 + 无线充电","4500nit 高亮 P-OLED","骁龙 7 Gen4 中端平台"],
  "why_important":"将旗舰级轻薄与军规防护下放到中端，IFA 2026 主流手机代表。",
  "terminal_link":"轻薄 + 军规三防手机供 TCL 手机规划参考。",
  "note":"欧洲/全球 2026 年 8-9 月上市；非去重表内机型。"},

 {"region":"国际","title":"Google Pixel Watch 5 发布：端侧 Gemini + 骁龙 W5 Gen2 + 3000nit",
  "category":"智能手表","dim":"生物识别","status":"已上市","date":"2026-08-12","source_tier":"B",
  "source_name":"Gizmochina","url":"https://www.gizmochina.com/2026/08/12/google-pixel-watch-5-launched-specs-price",
  "corroboration":2,"stars":4,"vendor":"Google Pixel Watch 5","signal_type":"新品发布",
  "key_params":"骁龙 W5 Gen2 / Wear OS 7 / 端侧 Gemini / 41-45mm / 3000nit AMOLED / 40h 续航 / $399",
  "tech_features":["端侧 Gemini AI","3000nit 高亮屏","全天健康传感","Wear OS 7"],
  "why_important":"Pixel Watch 首次引入端侧 Gemini，智能手表 AI 化标杆。",
  "terminal_link":"端侧 Gemini 手表供 TCL 穿戴 AI 规划参考。",
  "note":"2026 年 8 月 12 日发布；非去重表内 Pixel Watch 4 / 新款 Pixel 可穿戴。"},

 {"region":"国际","title":"Garmin Fenix 9 / Fenix 9 Pro 发布：AMOLED + 钛合金 + inReach 卫星通讯",
  "category":"智能手表","dim":"传感器","status":"已上市","date":"2026-08-25","source_tier":"A",
  "source_name":"Garmin 官方新闻室","url":"https://www.garmin.com/en-US/newsroom/press-release/outdoor/garmin-expands-its-flagship-performance-smartwatch-lineup-with-fenix9-and-fenix9-pro/",
  "corroboration":1,"stars":4,"vendor":"Garmin Fenix 9 / Fenix 9 Pro","signal_type":"新品发布",
  "key_params":"AMOLED(Pro 版 2 倍亮度/3000nit) / 钛合金(Pro) / 43-47-51mm / 64GB / inReach 卫星通讯+LTE(Pro) / $999.99 起",
  "tech_features":["inReach 卫星消息","多频 GNSS","钛合金机身","长续航户外传感"],
  "why_important":"旗舰户外表加入卫星通讯与更大存储，强化脱离手机的安全能力。",
  "terminal_link":"卫星通讯户外表供 TCL 穿戴规划参考。",
  "note":"2026 年 8 月 25 日发布；非去重表内机型。"},

 {"region":"国际","title":"Snap Specs 独立 AR 眼镜发布：$2195 + 双骁龙 XR + 51° FOV LCoS 波导",
  "category":"AR-VR眼镜","dim":"SoC/芯片","status":"即将上市","date":"2026-09-16","source_tier":"B",
  "source_name":"Mashable / The Brief","url":"https://mashable.com/tech/snap-announces-specs-ar-glasses-awe-2026",
  "corroboration":3,"stars":4,"vendor":"Snap Specs","signal_type":"新品发布",
  "key_params":"$2195 / 双骁龙 XR(渲染+AI 推理) / 51° FOV LCoS 波导 / 132g(47mm) / 4h 续航 / 9 月 16 日发布，秋季发货",
  "tech_features":["完全独立计算","双手 + 眼动追踪","电致变色镜片","OpenAI + Google AI"],
  "why_important":"迄今最接近日常佩戴的完全独立 AR 眼镜，定义消费级 AR 新形态。",
  "terminal_link":"独立计算 AR 眼镜范式供 TCL AR 眼镜规划参考。",
  "note":"9 月 16 日洛杉矶发布活动，美/英/法秋季上市。"},

 {"region":"国际","title":"Google Android XR 眼镜（Warby Parker 版）：$799 显示版 / $299 纯音频版，10/14 发货",
  "category":"AR-VR眼镜","dim":"AI/NPU","status":"即将上市","date":"2026-09-10","source_tier":"B",
  "source_name":"Smart Wearables / VR.org","url":"https://www.smartwearables.io/news/android-xr-glasses-warby-parker-october-14-799-screenless-299-november-2026",
  "corroboration":2,"stars":4,"vendor":"Google Android XR 眼镜","signal_type":"新品发布",
  "key_params":"$799(显示版)/$299(纯音频版) / 骁龙 AR1 / Gemini AI / 实时翻译+导航叠加 / 10 月 14 日美英加上市",
  "tech_features":["Gemini 实时翻译","镜内单色显示","自然语言交互","骁龙 AR1 平台"],
  "why_important":"首款消费级 Android XR 眼镜，Google 生态切入智能眼镜主战场。",
  "terminal_link":"Android XR 眼镜生态供 TCL 智能眼镜规划参考。",
  "note":"I/O 官宣，10 月 14 日发货；纯音频版 11 月。"},

 {"region":"国际","title":"HP OmniBook Ultra 16（RTX Spark）：NVIDIA 首款 PC SoC + 128GB 统一内存 + 3K OLED",
  "category":"笔记本电脑","dim":"BMS/电源","status":"即将上市","date":"2026-09-05","source_tier":"B",
  "source_name":"NotebookCheck","url":"https://www.notebookcheck.net/HP-s-latest-OmniBooks-get-RTX-Spark-128-GB-LPDDR5X-RAM-and-3K-OLED-displays.1388848.0.html",
  "corroboration":2,"stars":5,"vendor":"HP OmniBook Ultra 16","signal_type":"新品发布",
  "key_params":"NVIDIA RTX Spark N1X(18 核/5120 GPU 或 20 核/6144 GPU) / 16 英寸 3K OLED 120Hz / 最高 128GB LPDDR5X-9400 / 99Wh 17h / IFA 2026",
  "tech_features":["NVIDIA 首款 PC SoC RTX Spark","128GB 统一内存","3K OLED","99Wh 长续航"],
  "why_important":"NVIDIA 自研 Arm PC 芯片落地，统一内存高达 128GB，重塑 AI 创作用本。",
  "terminal_link":"128GB 统一内存 AI 本供 TCL 笔电规划参考。",
  "note":"IFA 2026 发布，2026 秋季上市；非去重表内 HP OmniBook 5 系列。"},

 {"region":"国际","title":"微星 Prestige N16 Flip AI+（RTX Spark）：128GB 统一内存 + 4K Tandem OLED 翻转本",
  "category":"笔记本电脑","dim":"SoC/芯片","status":"即将上市","date":"2026-09-04","source_tier":"A",
  "source_name":"MSI 官方","url":"https://us.msi.com/Landing/2026-new-prestige-series/nb",
  "corroboration":2,"stars":4,"vendor":"MSI Prestige N16 Flip AI+","signal_type":"新品发布",
  "key_params":"RTX Spark SoC(20 核 Arm+Blackwell GPU) / 最高 128GB 统一内存(VRAM) / 16 英寸 4K/UHD+ Tandem OLED 触控(1000nit+) / 360° 翻转 2-in-1 / IFA 2026",
  "tech_features":["RTX Spark 128GB 统一内存","可翻转触控屏","Calman 校色","创意翻转本"],
  "why_important":"将 128GB 统一内存的 RTX Spark 带入创意翻转本，AI 本地大模型能力突出。",
  "terminal_link":"翻转 AI 创作本供 TCL 笔电规划参考。",
  "note":"IFA 2026 亮相，2026 下半年上市；非去重表内机型。"},

 {"region":"国际","title":"mophie 发布 Qi2.2 StealthCharge 无线充：25W 持续快充 + 无风扇静音架构",
  "category":"无线充","dim":"认证/合规","status":"即将上市","date":"2026-09-15","source_tier":"A",
  "source_name":"ZAGG（mophie 官方）","url":"https://eu.zagg.com/learn/mophie-introduces-stealthcharge-technology-?setCurrencyId=2",
  "corroboration":1,"stars":4,"vendor":"mophie（ZAGG）Qi2.2 StealthCharge","signal_type":"新品发布",
  "key_params":"Qi2.2 认证 25W 持续快充、StealthCharge 无风扇静音架构、4-in-1/3-in-1 立式 + Roam 旅行三合一、Apple Store 全球上架",
  "tech_features":["关键充电元件移至底座散热","维持 25W Qi2.2 持续输出","无风扇静音","MagSafe 磁吸对齐 + StandBy"],
  "why_important":"Qi2.2 25W 标准落地代表配件，无风扇架构解决高功率温升痛点，多设备一体充新形态。",
  "terminal_link":"Qi2.2 高功率静音无线充形态供 TCL 配件规划参考。",
  "note":"IFA 2026 发布，Apple Store 全球发售；非去重表内 Zens/贝尔金等型号。"},

 {"region":"国际","title":"Sonos Beam Ultra 智能声霸：$699 + 7.1.2 杜比全景声 + Sonos 27 AI 语音",
  "category":"智能音箱","dim":"音频","status":"即将上市","date":"2026-09-01","source_tier":"B",
  "source_name":"CE Critic / GB News","url":"https://www.gbnews.com/tech/sonos-27-update-speakers",
  "corroboration":2,"stars":4,"vendor":"Sonos Beam Ultra","signal_type":"新品发布",
  "key_params":"7.1.2 声道 / 9 单元(含 2 up-firing) / 杜比全景声 / 4 级 AI 语音增强 / Trueplay / HDMI eARC / Wi-Fi+蓝牙 / $699 / 9 月 29 日发货",
  "tech_features":["Sonos 27 系统 AI 语音助手","便携环绕声","Trueplay 调音","杜比全景声"],
  "why_important":"Sonos 新 OS 与 AI 语音助理落地，中端声霸补齐杜比全景声。",
  "terminal_link":"智能音箱 AI 语音化供 TCL 音频终端规划参考。",
  "note":"9 月 1 日预购，9 月 29 日发货。"},

 {"region":"国际","title":"苹果 AirPods 5 发布：开放式 ANC 全系标配 + H2 芯片 + 实时翻译",
  "category":"AI耳机·耳穿戴","dim":"AI/NPU","status":"已上市","date":"2026-09-09","source_tier":"A",
  "source_name":"Apple 官方","url":"https://www.apple.com/jp/airpods-5/",
  "corroboration":3,"stars":5,"vendor":"Apple AirPods 5","signal_type":"新品发布",
  "key_params":"开放式 ANC(全系标配) / H2 芯片 / Siri AI + Live Translation / $129(标准)/$149(无线充版) / 9 月 18 日上市",
  "tech_features":["开放式耳塞主动降噪","实时翻译","头部手势交互","自适应音频"],
  "why_important":"首次将 ANC 下放到全系入门 AirPods，AI 实时翻译 + 开放式降噪成标配。",
  "terminal_link":"开放式 ANC + 实时翻译耳机范式供 TCL 耳穿戴规划参考。",
  "note":"9 月 9 日发布，9 月 18 日开售。"},
]

# ---------- helpers ----------
STATUS_RANK = {"即将上市":0, "进行中":1, "已上市":2}
STATUS_CLASS = {"即将上市":"status-coming", "进行中":"status-progress", "已上市":"status-released"}
CIRCLED = ["①","②","③","④","⑤","⑥"]

def star_str(n):
    return "★"*n + "☆"*(5-n)

def sort_key(it):
    # 状态分组：即将上市→进行中→已上市；同状态内时间倒序（最新在前）
    return (STATUS_RANK[it["status"]], -int(it["date"].replace("-", "")))

# split CN / INTL and sort each independently
cn = sorted([it for it in ITEMS if it["region"]=="国内"], key=sort_key)
intl = sorted([it for it in ITEMS if it["region"]=="国际"], key=sort_key)
ordered = cn + intl  # card-1..15 = cn, 16..30 = intl

# dimension coverage counts
dim_count = {d:0 for d in DIMS}
for it in ITEMS:
    if it["dim"] in dim_count:
        dim_count[it["dim"]] += 1
covered = sum(1 for d in DIMS if dim_count[d] > 0)

# tier counts
tier_count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for it in ITEMS:
    tier_count[it["source_tier"]] += 1
five_star = sum(1 for it in ITEMS if it["stars"]==5)

def field(label, value, full=False):
    cls = "field full" if full else "field"
    return f'          <div class="{cls}"><div class="field-label">{label}</div><div class="field-value">{value}</div></div>'

def render_card(idx, it):
    # badges
    badges = (f'<span class="source-tag source-{it["source_tier"].lower()}">{it["source_tier"]}</span>'
              f'<span class="sig-dim" style="background:#f0f9eb;color:#67c23a;border-radius:4px;padding:1px 6px;font-size:11px;">{it["dim"]}</span>'
              f'<span class="stars">{"★"*it["stars"]}{"☆"*(5-it["stars"])}</span>')
    if it["status"] != "已上市":
        badges += f'<span class="status-tag {STATUS_CLASS[it["status"]]}">{it["status"]}</span>'
    else:
        badges += f'<span class="status-tag" style="background:#f0f9eb;color:#67c23a;border:1px solid #c2e7b0;">已上市</span>'
    # tech list
    tech_li = "".join(f'<li data-num="{CIRCLED[i]}">{t}</li>' for i,t in enumerate(it["tech_features"]))
    fields = (
        field("信号类型", it["signal_type"]) +
        field("印证源数", f'{it["corroboration"]} 个独立信源') +
        field("主技术维度", it["dim"]) +
        field("区域", it["region"]) +
        field("厂商/型号", it["vendor"]) +
        field("时间", it["date"]) +
        field("信源等级", f'{it["source_tier"]} 级 — {it["source_name"]}') +
        field("信源明细", it["source_name"]) +
        field("关键参数", it["key_params"], full=True) +
        field("技术特性", f'<ul class="tech-list">{tech_li}</ul>', full=True) +
        field("为什么重要", it["why_important"], full=True) +
        field("智能终端关联点", it["terminal_link"], full=True) +
        field("来源 URL", f'<a href="{it["url"]}" target="_blank" rel="noopener">{it["url"]}</a>', full=True) +
        field("备注待印证", it["note"], full=True)
    )
    expanded = " expanded" if idx == 1 else ""
    return f'''      <div class="intel-card {('cn' if it['region']=='国内' else 'intl')}{expanded}" id="card-{idx}">
        <div class="card-header" onclick="toggleCard('card-{idx}')">
          <div class="card-num">{idx}</div>
          <div class="card-title-area">
            <div class="card-title">{it['title']}</div>
            <div class="card-badges">{badges}</div>
          </div>
          <div class="card-toggle">▼</div>
        </div>
        <div class="card-body"><div class="card-content">
          <div class="field-grid">
{fields}
          </div>
        </div></div>
      </div>'''

def render_summary_row(idx, it):
    region_cls = "region-cn" if it["region"]=="国内" else "region-intl"
    region_txt = "国内" if it["region"]=="国内" else "国际"
    if it["status"] != "已上市":
        st = f'<span class="status-tag {STATUS_CLASS[it["status"]]}">{it["status"]}</span>'
    else:
        st = f'<span class="status-tag" style="background:#f0f9eb;color:#67c23a;border:1px solid #c2e7b0;">已上市</span>'
    return f'''      <tr>
        <td>{idx}</td>
        <td class="td-title"><a href="#card-{idx}">{it['title']}</a></td>
        <td><span class="td-region {region_cls}">{region_txt}</span></td>
        <td>{it['category']}</td>
        <td><span class="source-tag source-{it['source_tier'].lower()}">{it['source_tier']}</span></td>
        <td class="td-status">{st}</td>
        <td>{it['date']}</td>
        <td><span class="stars">{"★"*it['stars']}{"☆"*(5-it['stars'])}</span></td>
      </tr>'''

# dim panel chips
def dim_chip(d):
    n = dim_count[d]
    if n > 0:
        return f'<div class="dim-chip on">{d} <span class="dim-count">{n}条</span></div>'
    return f'<div class="dim-chip off">{d} <span class="dim-count">0条</span></div>'
dim_html = "".join(dim_chip(d) for d in DIMS)
pct = round(covered/16*100)

# Top5 selection: 5-star first, A before B, 即将上市 before 已上市, time desc
def top_key(it):
    return (-it["stars"], 0 if it["source_tier"]=="A" else 1, STATUS_RANK[it["status"]], -int(it["date"].replace("-","")))
top5 = sorted(ITEMS, key=top_key)[:5]

top_cards = ""
for i, it in enumerate(top5, 1):
    top_cards += f'''      <div class="signal-card">
        <div><span class="sig-rank">{i}</span><span class="sig-title">{it['title']}</span></div>
        <div class="sig-tags"><span class="sig-dim">{it['category']}</span><span class="sig-stars">{"★"*it['stars']}{"☆"*(5-it['stars'])}</span></div>
        <div class="sig-key">{it['source_tier']}级 / {it['key_params']}</div>
      </div>'''

# summary rows + cards
summary_rows = "".join(render_summary_row(i+1, it) for i, it in enumerate(ordered))
cards_html = "".join(render_card(i+1, it) for i, it in enumerate(ordered))
cn_cards = "".join(render_card(i+1, it) for i, it in enumerate(cn))
intl_cards = "".join(render_card(15+i+1, it) for i, it in enumerate(intl))

HTML = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
  <style>
  :root {{
    --bg: #f5f7fa; --card-bg: #fff; --border: #e4e7ed;
    --text: #303133; --text-secondary: #606266; --text-tertiary: #909399;
    --primary: #409eff; --success: #67c23a; --warning: #e6a23c; --danger: #f56c6c; --info: #909399;
    --tag-a: #67c23a; --tag-b: #409eff; --tag-c: #e6a23c; --tag-d: #f56c6c; --tag-e: #aa55ff;
    --shadow: 0 2px 12px rgba(0,0,0,0.06); --shadow-hover: 0 4px 20px rgba(0,0,0,0.1); --radius: 10px;
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--text); line-height:1.6; padding:20px; }}
  .container {{ max-width:1200px; margin:0 auto; }}
  .header {{ background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:#fff; border-radius:var(--radius); padding:28px 32px; margin-bottom: 20px; box-shadow:var(--shadow); }}
  .header h1 {{ font-size:24px; margin-bottom:8px; }}
  .header .subtitle {{ font-size:14px; opacity:0.9; }}
  .header .meta {{ display:flex; gap:12px; margin-top:14px; flex-wrap:wrap; }}
  .meta-badge {{ background:rgba(255,255,255,0.2); border:1px solid rgba(255,255,255,0.3); border-radius:20px; padding:4px 14px; font-size:13px; }}
  .stats-bar {{ display:flex; gap:16px; margin-bottom:24px; flex-wrap:wrap; }}
  .stat-item {{ background:var(--card-bg); border-radius:var(--radius); padding:14px 20px; box-shadow:var(--shadow); flex:1; min-width:140px; text-align:center; }}
  .stat-num {{ font-size:22px; font-weight:700; color:var(--primary); }}
  .stat-label {{ font-size:12px; color:var(--text-tertiary); margin-top:4px; }}
  .dim-panel {{ background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }}
  .dim-header {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }}
  .dim-title {{ font-size:16px; font-weight:700; display:flex; align-items:center; gap:8px; }}
  .dim-title::before {{ content:''; width:4px; height:18px; background:var(--success); border-radius:2px; }}
  .dim-counter {{ font-size:14px; color:var(--text-secondary); }}
  .dim-counter .dim-num {{ font-size:18px; font-weight:600; color:var(--success); }}
  .dim-counter .dim-total {{ color:var(--text-tertiary); }}
  .dim-bar {{ width:100%; height:8px; background:#f0f2f5; border-radius:4px; margin-bottom:16px; overflow:hidden; }}
  .dim-bar-fill {{ height:100%; background:linear-gradient(90deg,#67c23a,#95d475); border-radius: 4px; transition:width 0.5s; }}
  .dim-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }}
  .dim-chip {{ padding:8px 12px; border-radius:8px; font-size:13px; font-weight:500; display:flex; justify-content:space-between; align-items:center; }}
  .dim-chip.on {{ background:#f0f9eb; border:1px solid #c2e7b0; color:#67c23a; }}
  .dim-chip.off {{ background:#f5f7fa; border:1px solid #e4e7ed; color:#c0c4cc; }}
  .dim-chip .dim-count {{ font-size:11px; opacity:0.7; font-weight:400; }}
  .summary-section {{ background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }}
  .section-title {{ font-size:16px; font-weight:700; margin-bottom:14px; display:flex; align-items:center; gap:8px; }}
  .section-title::before {{ content:''; width:4px; height:18px; background:var(--primary); border-radius:2px; }}
  table {{ width:100%; border-collapse:collapse; font-size:13px; }}
  thead th {{ background:#f0f2f5; padding:10px 12px; text-align:left; font-weight:600; color:var(--text-secondary); border-bottom:2px solid var(--border); white-space:nowrap; }}
  tbody td {{ padding:10px 12px; border-bottom:1px solid var(--border); vertical-align:top; }}
  tbody tr:hover {{ background:#f5f7fa; }}
  tbody tr:last-child td {{ border-bottom:none; }}
  .td-title {{ font-weight:600; color:var(--text); }}
  .td-region {{ font-size:12px; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; }}
  .region-cn {{ background:#ecf5ff; color:#409eff; }}
  .region-intl {{ background:#fdf6ec; color:#e6a23c; }}
  .source-tag {{ display:inline-block; font-size:12px; font-weight:700; padding:2px 10px; border-radius:12px; white-space:nowrap; }}
  .source-a {{ background:#f0f9eb; color:var(--tag-a); border:1px solid #c2e7b0; }}
  .source-b {{ background:#ecf5ff; color:var(--tag-b); border:1px solid #b3d8ff; }}
  .source-c {{ background:#fdf6ec; color:var(--tag-c); border:1px solid #f5dab1; }}
  .source-d {{ background:#fef0f0; color:var(--tag-d); border:1px solid #fbc4c4; }}
  .source-e {{ background:#f3f0ff; color:var(--tag-e); border:1px solid #d3c2ff; }}
  .status-tag {{ display:inline-block; font-size:11px; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; margin-left:8px; }}
  .td-status .status-tag {{ margin-left:0; font-size:10px; padding:1px 6px; }}
  .status-coming {{ background:#ecf5ff; color:#409eff; border:1px solid #b3d8ff; }}
  .status-released {{ background:#f0f9eb; color:#67c23a; border:1px solid #c2e7b0; }}
  .status-progress {{ background:#ecf5ff; color:#409eff; border:1px solid #b3d8ff; }}
  .intel-section {{ margin-bottom:24px; }}
  .intel-cards {{ display:grid; grid-template-columns:1fr; gap:16px; }}
  .intel-card {{ background:var(--card-bg); border-radius:var(--radius); box-shadow:var(--shadow); overflow:hidden; transition:box-shadow 0.3s; border-left:4px solid var(--primary); }}
  .intel-card.cn {{ border-left-color:var(--tag-b); }}
  .intel-card.intl {{ border-left-color:var(--tag-c); }}
  .intel-card:hover {{ box-shadow:var(--shadow-hover); }}
  .card-header {{ padding:16px 20px; cursor:pointer; display:flex; align-items:flex-start; gap:12px; user-select:none; }}
  .card-num {{ flex-shrink:0; width:28px; height:28px; border-radius:50%; background:#f0f2f5; color:var(--text-secondary); font-size:13px; font-weight:700; display:flex; align-items:center; justify-content:center; margin-top:2px; }}
  .intel-card.cn .card-num {{ background:#ecf5ff; color:var(--tag-b); }}
  .intel-card.intl .card-num {{ background:#fdf6ec; color:var(--tag-c); }}
  .card-title-area {{ flex:1; }}
  .card-title {{ font-size:15px; font-weight:600; color:var(--text); margin-bottom:6px; }}
  .card-badges {{ display:flex; gap:8px; flex-wrap:wrap; align-items:center; }}
  .card-badges .stars {{ font-size:12px; color:var(--warning); letter-spacing:1px; }}
  .card-domain {{ font-size:12px; color:var(--text-tertiary); background:#f5f7fa; padding:2px 8px; border-radius:4px; }}
  .card-toggle {{ flex-shrink:0; color:var(--text-tertiary); font-size:14px; transition:transform 0.3s; margin-top:4px; }}
  .intel-card.expanded .card-toggle {{ transform:rotate(180deg); }}
  .card-body {{ max-height:0; overflow:hidden; transition:max-height 0.4s ease; }}
  .intel-card.expanded .card-body {{ max-height:3000px; }}
  .card-content {{ padding:0 20px 18px 20px; border-top:1px solid var(--border); padding-top:16px; }}
  .field-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:12px 20px; }}
  .field {{ display:flex; flex-direction:column; gap:4px; }}
  .field.full {{ grid-column:1 / -1; }}
  .field-label {{ font-size:12px; font-weight:600; color:var(--text-tertiary); letter-spacing:0.5px; }}
  .field-value {{ font-size:13px; color:var(--text-secondary); line-height:1.7; }}
  .field-value a {{ color:var(--primary); text-decoration:none; word-break:break-all; }}
  .field-value a:hover {{ text-decoration:underline; }}
  .field-value .tech-list {{ padding-left:0; list-style:none; }}
  .field-value .tech-list li {{ padding:2px 0; padding-left:18px; position:relative; }}
  .field-value .tech-list li::before {{ content:attr(data-num); position:absolute; left:0; font-weight:700; color:var(--primary); }}
  @media (max-width:768px) {{ .field-grid {{ grid-template-columns:1fr; }} .dim-grid {{ grid-template-columns:repeat(2,1fr); }} table {{ font-size:12px; }} thead th,tbody td {{ padding:8px 6px; }} }}
  html {{ scroll-behavior: smooth; }}
  .td-title a {{ color: inherit; text-decoration: none; }}
  .td-title a:hover {{ color: var(--primary); text-decoration: underline; }}
  .top-signals-panel {{ background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }}
  .top-signals-header {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }}
  .top-signals-title {{ font-size:16px; font-weight:700; display:flex; align-items:center; gap:8px; }}
  .top-signals-title::before {{ content:''; width:4px; height:18px; background:var(--warning); border-radius:2px; }}
  .top-signals-grid {{ display:grid; grid-template-columns:repeat(5,1fr); gap:12px; }}
  .signal-card {{ background:linear-gradient(135deg,#f5f7fa,#fafafa); border-radius:8px; padding:12px 14px; border-left:3px solid var(--success); transition:box-shadow 0.3s; }}
  .signal-card:hover {{ box-shadow:var(--shadow-hover); }}
  .signal-card .sig-rank {{ display:inline-block; font-size:11px; font-weight:700; color:#fff; background:var(--success); border-radius:50%; width:18px; height:18px; text-align:center; line-height:18px; margin-right:6px; }}
  .signal-card .sig-title {{ font-size:13px; font-weight:600; color:var(--text); line-height:1.4; }}
  .signal-card .sig-tags {{ display:flex; gap:4px; flex-wrap:wrap; margin-bottom:4px; margin-top:6px; }}
  .signal-card .sig-dim {{ font-size:11px; background:#f0f9eb; color:#67c23a; border-radius:4px; padding:1px 6px; }}
  .signal-card .sig-stars {{ font-size:12px; color:#e6a23c; }}
  .signal-card .sig-key {{ font-size:11px; color:var(--text-secondary); line-height:1.5; margin-top:4px; }}
  </style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>{TITLE}</h1>
    <div class="subtitle">采集口径：8类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑/AI耳机·耳穿戴） | 搜索窗口60天 | 国内15条 + 国际15条</div>
    <div class="meta">
      <span class="meta-badge">总情报 30条</span>
      <span class="meta-badge">国内 15条</span>
      <span class="meta-badge">国际 15条</span>
      <span class="meta-badge">信源 A-E级</span>
      <span class="meta-badge">搜索窗口 60天</span>
    </div>
  </div>
  <div class="stats-bar">
    <div class="stat-item"><div class="stat-num">30</div><div class="stat-label">总情报数</div></div>
    <div class="stat-item"><div class="stat-num">{tier_count['A']}</div><div class="stat-label">A级信源</div></div>
    <div class="stat-item"><div class="stat-num">{tier_count['B']}</div><div class="stat-label">B级信源</div></div>
    <div class="stat-item"><div class="stat-num">8</div><div class="stat-label">覆盖产品类别</div></div>
    <div class="stat-item"><div class="stat-num">{five_star}</div><div class="stat-label">五星条数</div></div>
  </div>
  <div class="dim-panel">
    <div class="dim-header">
      <div class="dim-title">技术维度覆盖面板</div>
      <div class="dim-counter"><span class="dim-num">{covered}</span><span class="dim-total"> / 16 维度</span></div>
    </div>
    <div class="dim-bar"><div class="dim-bar-fill" style="width:{pct}%"></div></div>
    <div class="dim-grid">
      {dim_html}
    </div>
  </div>
  <div class="top-signals-panel">
    <div class="top-signals-header">
      <div class="top-signals-title">今日重点信号 Top 5</div>
      <div style="font-size:12px;color:var(--text-tertiary);">排序：星级降序→A级优先→状态优先→时间倒序</div>
    </div>
    <div class="top-signals-grid">
      {top_cards}
    </div>
  </div>
  <div class="summary-section">
    <div class="section-title">情报摘要表</div>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>类别</th><th>信源</th><th>状态</th><th>时间</th><th>重要度</th></tr></thead>
      <tbody>
      {summary_rows}
      </tbody>
    </table>
  </div>
  <div class="intel-section">
    <div class="section-title">一、国内情报（15条）</div>
    <div class="intel-cards">
{cn_cards}
    </div>
  </div>
  <div class="intel-section">
    <div class="section-title">二、国际情报（15条）</div>
    <div class="intel-cards">
{intl_cards}
    </div>
  </div>
</div>
<script>
function toggleCard(id) {{
  var el = document.getElementById(id);
  if (el.classList.contains('expanded')) el.classList.remove('expanded');
  else el.classList.add('expanded');
}}
</script>
</body>
</html>'''

out = f"E:/AI相关/预研究/202608/03_输出/WB_{DATE}_硬件看板.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print("written:", out, "bytes:", len(HTML.encode('utf-8')))
print("covered dims:", covered, "/16  pct:", pct)
print("tier A/B/C/D/E:", tier_count)
print("5-star:", five_star)
print("cn sorted dates:", [it['date'] for it in cn])
print("intl sorted dates:", [it['date'] for it in intl])
