# -*- coding: utf-8 -*-
# Generator for WB_2026-09-23_硬件看板.html
# Single HTML, inline CSS, no CDN. 30 cards (CN15 + INTL15).
import datetime

DATE = "2026-09-23"
TITLE = "智能终端硬件情报日报 · " + DATE

# 16 technical dimensions (canonical order for coverage panel)
DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

ITEMS = [
 # ---------- CN (1-15) ----------
 {"region":"国内","title":"华为 MatePad Air 12 英寸 OLED 柔光屏发布：麒麟 T93 + 2.8K 144Hz + 10100mAh","category":"平板","dim":"显示/OLED","status":"已上市","date":"2026-09-07","source_tier":"B","source_name":"中关村在线（ZOL）/ 腾讯新闻","url":"https://news.qq.com/rain/a/20260907A0DWCU00","corroboration":2,"stars":4,"vendor":"华为 MatePad Air（12 英寸）","signal_type":"新品上市","key_params":"12 英寸 2.8K OLED 云晰柔光屏(2000nits/144Hz/P3)、麒麟 T93 系列、10100mAh/66W、5.3mm/509g、M-Pencil Pro","tech_features":["12 英寸超亮 OLED 云晰柔光屏，峰值 2000nits/2.8K/144Hz","麒麟 T93 系列芯片 + 鸿蒙多设备协同","M-Pencil Pro 手写笔(快乐胶囊/空鼠模式/手写空间)","机身 5.3mm/509g 轻薄 + 幻彩珠光工艺"],"why_important":"华为平板首次在 Air 线普及 OLED 柔光屏，以轻薄 + 手写创作定义中端生产力平板新基准，对 TCL 平板的护眼 OLED 与手写笔生态构成直接压力。","terminal_link":"TCL 平板(如 NXTPAPER/雷鸟)可对标其 OLED 柔光 + 手写笔组合；TCL 移动终端可借雷鸟近眼显示经验强化平板多屏协同。","note":"信源为 ZOL 原创(9/7)，与百度百科、多家媒体互证；9/7-10/11 首销优惠 300 元，国补到手 3699 起；非去重清单已有型号。"},

 {"region":"国内","title":"小米平板 9 Pro Max 发布：13.3 英寸 3.4K + 满血玄戒 O3 + 12000mAh，4799 元起专业生产力旗舰","category":"平板","dim":"SoC/芯片","status":"已上市","date":"2026-09-08","source_tier":"B","source_name":"新浪财经（新浪数码）","url":"https://finance.sina.cn/tech/2026-09-08/detail-inirayqy4667468.d.html","corroboration":2,"stars":4,"vendor":"小米平板 9 Pro Max","signal_type":"新品上市","key_params":"13.3 英寸 3.4K(3408×2272/144Hz/1000nits)、满血玄戒 O3(10 核全大核 + G2-Ultra NX)、12000mAh + 120W、Wi-Fi7、DP-in","tech_features":["自研满血玄戒 O3(安兔兔 561 万/全大核架构)","13.3 英寸 3.4K 专业原色屏 + 多屏同色","12000mAh + 120W 闪充 + 27W 反向","首发 6 Mic 阵列 + Wi-Fi7 + DP-in 副屏"],"why_important":"小米自研玄戒 O3 下放平板，3.4K + 120W + DP-in 把安卓大平板推向桌面级生产力，对 TCL 平板 SoC 自研路线有参照。","terminal_link":"TCL 平板可参考其 DP-in 便携副屏与自研芯片路线；TCL 雷鸟显示技术可强化大屏专业色准。","note":"新浪数码/新浪香港双源互证；9/7 发布 9/8 开售，国补 4299 起；非去重清单(仅 9 标准版/9 Pro 预售)。"},

 {"region":"国内","title":"小米平板 9 / 9 Pro 开启预售：全系 3.2K 护眼屏，Pro 版第五代骁龙 8，2999 元起","category":"平板","dim":"显示/OLED","status":"即将上市","date":"2026-09-14","source_tier":"B","source_name":"网易（快科技）","url":"https://www.163.com/dy/article/L6PJFNGG0511CPVM.html","corroboration":2,"stars":4,"vendor":"小米平板 9 / 9 Pro","signal_type":"开启预售","key_params":"全系 3.2K 护眼屏(3200×2136/144Hz/12bit/DCI-P3/莱茵 TUV 三认证)、平板 9=11.2 英寸 LCD+第四代骁龙 8s+9720mAh+45W、平板 9 Pro=12.5 英寸 LCD+第五代骁龙 8+11000mAh+67W、2999/3799 元起，本月正式发布","tech_features":["全系 3.2K 高清护眼屏，莱茵 TUV 节律友好/无频闪/硬件级低蓝光三重认证","小米平板 9 搭载第四代骁龙 8s，平板 9 Pro 升级第五代骁龙 8","小米平板 9 Pro 内置 11000mAh + 67W 快充 + 22.5W 反向，平板 9 为 9720mAh + 45W","全系澎湃 OS 4 + PC 级专业应用，强化生产力体验"],"why_important":"小米以 3.2K 护眼屏 + 旗舰芯 + 大电池重新定义 3000-4000 元档平板，护眼与性能双线压制同价位竞品。","terminal_link":"TCL 平板(雷鸟/NXTPAPER)在 3000-4000 元主流档需对标其 3.2K 护眼屏与 65W 级快充；TCL 可借 NXTPAPER 类纸护眼强化差异化。","note":"快科技 9/14；9/14 开启预售、本月正式发布；非去重清单(小米平板 9 Pro Max 为不同旗舰)。"},

 {"region":"国内","title":"华为 MatePad Pro 12.2 发布：PaperMatte OLED + 麒麟 + 10100mAh + 100W，生产力旗舰","category":"平板","dim":"显示/OLED","status":"已上市","date":"2026-09-06","source_tier":"B","source_name":"TechNews（综合华为全球页 / GSM Arena）","url":"https://www.technews.site/2026/09/huawei-launches-matepad-pro-122-inch.html","corroboration":2,"stars":4,"vendor":"华为 MatePad Pro 12.2","signal_type":"新品发布","key_params":"12.2 英寸 PaperMatte OLED(2800×1800/QHD)、麒麟 9000S 或 T92A、10100mAh + 100W、12GB+512GB 起、HarmonyOS、GoPaint/PC 级应用","tech_features":["12.2 英寸 PaperMatte OLED 漫反射柔光屏，降低眩光","麒麟平台(9000S/T92A variant) + HarmonyOS 生态","10100mAh 大电池 + 100W 有线快充","预装 WPS/华为笔记/GoPaint，定位 PC 级生产力"],"why_important":"华为把 PaperMatte 柔光 OLED + 100W 快充 + 麒麟平台下放到 12.2 英寸生产力平板，对安卓高端平板护眼与快充基线形成标杆压力。","terminal_link":"TCL 平板需对标其 PaperMatte 柔光 OLED 与 100W 快充；TCL 雷鸟显示技术可强化大屏专业色准与护眼。","note":"TechNews 9/6 综合报道；芯片配置华为官方与 GSM Arena 略有出入，电池/充电两源一致；非去重清单型号。"},

 {"region":"国内","title":"小米 18 Pro 系列发布：首发第六代骁龙 8 至尊版(2nm) + 徕卡双 2 亿 + 7000/8500mAh，6999 元起","category":"手机","dim":"摄像头","status":"即将上市","date":"2026-09-23","source_tier":"B","source_name":"快科技（IT之家同源）","url":"https://news.mydrivers.com/1/1153/1153229.htm","corroboration":2,"stars":4,"vendor":"小米 18 Pro / 18 Pro Max","signal_type":"官宣定档/新品发布","key_params":"第六代骁龙 8 至尊版/超级至尊版(台积电 2nm GAA/5GHz+/Oryon3+Adreno850+Hexagon NPU)、徕卡双 2 亿(75mm 3.2X)、7000/8500mAh 100W+50W、4000nits/0.99mm 边框、AI 百变背屏","tech_features":["台积电 2nm GAA 第六代骁龙 8 至尊版(CPU 破 5GHz)","徕卡双 2 亿全焦段三摄 + 传奇一瞬影像大模型","32% 超高硅金沙江电池 7000/8500mAh + 100W/50W","超级像素 2.0 4000nits 直屏 + AI 百变背屏"],"why_important":"2nm 旗舰芯国内首发 + 双 2 亿影像树立安卓旗舰新标杆，NPU 端侧 AI 算力暴涨推动端侧大模型普及。","terminal_link":"TCL 手机(如 TCL/雷鸟)需关注 2nm 旗舰平台与端侧影像大模型趋势；TCL 可借雷鸟 AI 能力探索背屏交互。","note":"快科技/环球网/高通峰会多源互证；9/23 晚 19:00 国内发布；非去重清单型号。"},

 {"region":"国内","title":"华为 Mate XT 2 二代三折叠发布：麒麟 9050 Pro + 10.2 英寸 3K OLED + 5600mAh，19999 元起","category":"手机","dim":"折叠屏","status":"已上市","date":"2026-09-07","source_tier":"B","source_name":"中国经济新闻网","url":"https://www.cet.com.cn/wzsy/cjcj/10544400.shtml","corroboration":3,"stars":4,"vendor":"华为 Mate XT 2 非凡大师","signal_type":"新品上市","key_params":"展翼三折叠/10.2 英寸 3K OLED(内屏)/6.5 英寸外屏、麒麟 9050 Pro(逻辑折叠/性能 +42%)、5600mAh/66W+50W、IP58/59、鸿蒙 OS7","tech_features":["展翼三折叠形态 + 超可靠玄武架构 + 二代天工铰链","首发麒麟 9050 Pro(逻辑折叠/端侧 300 亿参数大模型)","业界首发折叠机灵盾硬件防窥屏","第三代红枫影像 + IP58/59 + 双卫星通信"],"why_important":"全球唯一量产三折叠再迭代，玄武架构/铰链/防窥屏定义折叠工艺上限，对 TCL 折叠与结构工艺路线具标杆意义。","terminal_link":"TCL 折叠手机/平板可借鉴其玄武架构与铰链耐久方案；TCL 显示(柔性与 OLED)与华为三折叠供应链有协同想象。","note":"中国经济新闻网/经济日报/hot3c 多源互证；9/7 发布 9/12 开售；非去重清单型号。"},

 {"region":"国内","title":"vivo WATCH 6 发布：全系蓝宝石表镜 + 钛合金 37.6g + 1.47 英寸 3500nits，999 元起","category":"智能手表","dim":"生物识别","status":"已上市","date":"2026-09-22","source_tier":"B","source_name":"网易（快科技）","url":"https://www.163.com/dy/article/L7EM79AO0511CPVM.html","corroboration":2,"stars":4,"vendor":"vivo WATCH 6","signal_type":"新品上市","key_params":"蓝宝石表镜(莫氏 9 级)、钛合金 37.6g/9.5mm、1.47 英寸 AMOLED 3500nits、21 天续航、ECG 二类医械(脉搏波心律失常)、eSIM 五星双频 GNSS","tech_features":["全系蓝宝石玻璃表镜 + 钛合金轻量化(37.6g)","1.47 英寸 AMOLED 3500nits/85.8% 屏占比","多通道光路心率 + 二类医械脉搏波心律失常分析","60 秒体检 + 睡眠呼吸暂停预警 + eSIM 双频 GNSS"],"why_important":"千元价位给到蓝宝石 + 钛合金 + 医械级心率监测，拉高安卓手表健康与材质基准。","terminal_link":"TCL/雷鸟穿戴可参考其蓝宝石 + 钛合金轻量化与医械级健康监测方案，强化 TCL 智能手表健康卖点。","note":"网易/快科技 9/22 图赏，微博同步；9/21 晚发布 999 起；非去重清单型号。"},

 {"region":"国内","title":"华为 WATCH Ultimate 2 新色开售：非晶锆合金 + 双卫星通信 + 20 项微体检，6999 元","category":"智能手表","dim":"结构/工艺","status":"已上市","date":"2026-09-17","source_tier":"B","source_name":"新浪财经（财经头条）","url":"https://t.cj.sina.com.cn/articles/view/7879996057/1d5af3299068020asy?finpagefr=p_103","corroboration":2,"stars":4,"vendor":"华为 WATCH Ultimate 2 非凡探索","signal_type":"进展更新（新色开售）","key_params":"超坚固非晶锆合金表壳 + 纳米微晶陶瓷圈 + 蓝宝石镜、双卫星(北斗语音/海豚声呐水下 150m)、微体检 20 项、6999 元","tech_features":["非晶锆合金表壳 + 纳米微晶陶瓷表圈(高端材质)","业界首款北斗卫星语音消息大众手表 + 海豚声呐水下通信","鸿蒙 OS7 + 微体检升级至 20 项健康指标","滑雪登山/高尔夫专业运动模式 + 150m 潜水"],"why_important":"把卫星通信与专业潜水/滑雪做进消费手表，定义户外高端智能表材质与通信上限。","terminal_link":"TCL 穿戴可关注卫星通信与高端材质路线；雷鸟可思考将户外健康与近眼导航结合。","note":"新浪财经 9/17，新色(雪域白/迪桑特联名)开售；非去重清单(WATCH D3/6/GT7 之外的新品)。"},

 {"region":"国内","title":"Rokid 新一代乐奇 AI 眼镜定档 9/24 数贸会：Micro LED + 衍射光波导，强化多模型 AI Agent","category":"AR-VR眼镜","dim":"显示/OLED","status":"即将上市","date":"2026-09-21","source_tier":"B","source_name":"网易（IT之家）","url":"https://www.163.com/dy/article/L7BC99HQ05568W0A.html","corroboration":2,"stars":3,"vendor":"Rokid 乐奇 AI 眼镜（新一代）","signal_type":"官宣定档","key_params":"9/24 杭州数贸会全球首发；初代基于高通 AR1 + Micro LED 衍射光波导(480×640/1500nits/FOV30°)；二代强化 AI Agent/视觉识别/实时翻译","tech_features":["Micro LED + 衍射光波导双目显示(初代 480×640/1500nits/FOV30°)","高通 AR1 SoC + 2 扬声器 4 麦克风","多模型生态 + 视觉识别/实时翻译/会议实录","49g 日常眼镜形态 + 近视散光定制"],"why_important":"二代强调多模型 Agent 与全场景第一视角，推动 AI 眼镜从录音翻译走向'感官延伸'。","terminal_link":"TCL 雷鸟与 Rokid 同处 AR 眼镜第一梯队，可对标其多模型 Agent 与轻量化形态，强化雷鸟 iO 的主动记忆能力。","note":"IT之家/网易/LEDinside 多源；二代完整硬件规格 9/24 发布会揭晓，当前参数为初代参照；非去重清单(初代澳洲上市为不同事件)。"},

 {"region":"国内","title":"影目 INMO GO3 获 IFA 2026 创新奖：58g 轻量 AI HUD + 98 语种实时翻译 + 5 秒换电","category":"AR-VR眼镜","dim":"显示/OLED","status":"已上市","date":"2026-09-08","source_tier":"B","source_name":"今日头条（屏显时代）","url":"https://www.toutiao.com/article/7683174710632301110/","corroboration":2,"stars":4,"vendor":"影目 INMO GO3","signal_type":"获奖（IFA 2026 创新奖）","key_params":"约 58g、双眼单色 Micro-LED 波导(覆盖 98+ 语种 AI 实时翻译)、ChatGPT/Gemini 双 AI 助手、免提 AR 导航、自动会议转写/提词器、5 秒可换电池、海外 $599/国内 2999 元、紫光展锐芯片、260+ 语种双向翻译","tech_features":["58g 轻量机身，把 AI 眼镜做'轻'获 IFA Innovation Award Honoree(9/4 公布)","双眼单色 Micro-LED 波导显示，98+ 语种 AI 实时翻译","集成 ChatGPT 与 Gemini 双 AI 助手的免提语音交互","免提 AR 导航 + 自动会议转写 + 内置提词器 + 5 秒可换电池"],"why_important":"国内 AI+AR 眼镜龙头以'轻量 HUD'路线拿下 IFA 创新奖，验证'隐形助手'范式对'面部计算机'的胜出，对 AR 产品定义有方向性意义。","terminal_link":"TCL 雷鸟与影目同处 AI+AR 第一梯队，可对标其轻量 HUD 与双 AI 助手路线；TCL 手机/平板的端侧翻译与会议转写可借势协同。","note":"今日头条 9/8 IFA 落幕综述；GO3 4/2 Kickstarter、7/30 日本上市、国内 2999 元；沙利文 2021-2025 中国 AI+AR 累计销量份额 37.8% 居首。"},

 {"region":"国内","title":"七彩虹灵创 K16 移动 AI 工作站：锐龙 AI Max+395 + 128GB 统一内存，本地跑大模型笔记本","category":"笔记本电脑","dim":"SoC/芯片","status":"已上市","date":"2026-09-12","source_tier":"B","source_name":"ExcelDisc（快科技同源）","url":"http://exceldisc.com/blog/colorfire-unveils-ryzen-ai-max-pro-495-mini-pc-with-up-to-192gb-memory-plus-ryzen-ai-max-395-laptop","corroboration":2,"stars":4,"vendor":"COLORFIRE 七彩虹 灵创 K16","signal_type":"新品上市","key_params":"锐龙 AI Max+395(16 核/40CU Radeon8060S)、128GB LPDDR5X(96GB 显存)、16 英寸 2560×1600 165Hz、99Wh、Wi-Fi7、¥34999","tech_features":["AMD 锐龙 AI Max+395(40CU Radeon8060S)","128GB 统一内存可划拨 96GB 为显存","16 英寸 2.5K 165Hz + Wi-Fi7 + 99Wh","本地离线运行大模型/智能体工作流"],"why_important":"把 128GB 统一内存塞进笔记本，证明无独显也能本地跑大模型，重塑 AI 笔记本内存与算力边界。","terminal_link":"TCL 笔记本可借鉴其统一内存本地大模型方案，结合 TCL 终端 AI 助手做离线智能。","note":"ExcelDisc/快科技/七彩虹官方多源；AMD 沙龙(9/10)展出，JD 已上架；非去重清单(橘宝 X16 Pro 为游戏本)。"},

 {"region":"国内","title":"华硕天选 Air 2026 锐龙 AI Max 版新配置开售：锐龙 AI Max+388 + 50TOPS NPU + 73Wh，11999 元内","category":"笔记本电脑","dim":"散热","status":"已上市","date":"2026-09-23","source_tier":"B","source_name":"网易（大京新闻网）","url":"https://www.163.com/news/article/L7GJ7BNS00019UD6.html","corroboration":2,"stars":4,"vendor":"华硕 天选 Air 2026 锐龙 AI Max 版","signal_type":"进展更新（新配置开售）","key_params":"锐龙 AI Max+388(8 核 Zen5/40CU Radeon8060S/50TOPS NPU)、32GB LPDDR5X+1TB、14 英寸 2.5K 165Hz、73Wh/100W PD、冰川散热双风扇","tech_features":["AMD 锐龙 AI Max+388 + 50TOPS NPU 本地 AI","冰川散热(双 97 叶液态轴承风扇 + 0.1mm 纯铜鳍片 + 内吹)","14 英寸 2.5K 165Hz 100%sRGB + IR 人脸识别","1.48kg/16.9mm + 73Wh + USB4/双 USB-A"],"why_important":"新配置把锐龙 AI Max+ 价格下探至 11999 内，50TOPS NPU + 强散热让 14 寸轻薄本具备本地 AI 创作能力。","terminal_link":"TCL 笔记本可参考其冰川散热与 50TOPS NPU 组合，强化 TCL 轻薄本 AI 散热设计。","note":"网易 9/23；为初版(9 月已收录)的新配置进展更新；非新机型，依规则可作进展更新收录。"},

 {"region":"国内","title":"安克 MagGo 磁吸移动电源 2.0 曝光：Qi2.2 25W 无线充 + 内置支架 + 彩屏","category":"无线充","dim":"BMS/电源","status":"即将上市","date":"2026-08-27","source_tier":"B","source_name":"网易（IT之家）","url":"https://www.163.com/dy/article/L5C5I9S70511B8LM.html","corroboration":2,"stars":3,"vendor":"Anker 安克 MagGo 2.0 移动电源","signal_type":"曝光（预计近期上市）","key_params":"磁吸移动电源、Qi2.2 25W 无线充(由 Qi2 15W 升级)、内置支架、底部散热孔、侧面彩屏(显示 iPhone 机型)、预计近期上市","tech_features":["无线充电由 Qi2 15W 升级至 Qi2.2 25W，兼容机型充得更快","内置支架，底部新增散热孔改善空气流通","机身侧面彩屏，新增支持显示 iPhone 机型","磁吸移动电源形态，出门一贴即充"],"why_important":"安克把 Qi2.2 25W 带进磁吸移动电源，标志无线充功率升级从桌面底座向便携电源扩散，加速 Qi2.2 生态普及。","terminal_link":"TCL 手机/耳机(如 TCL Buds)可借 Qi2.2 25W 趋势规划磁吸生态配件；TCL 无线充应加速 Qi2.2 认证以进入苹果周边供应链。","note":"IT之家 8/27 引 NotebookCheck 曝光；预计近期上市，具体国行时间未官宣；非去重清单(安克三折叠风冷无线充为不同产品)。"},

 {"region":"国内","title":"绿联 HomeAgent 家庭 AIoT 中枢发布：本地存储 + 本地计算 + 后摩 M50 160TOPS，连接智能音箱","category":"智能音箱","dim":"AI/NPU","status":"即将上市","date":"2026-09-12","source_tier":"B","source_name":"澎湃新闻（今日头条）","url":"https://www.toutiao.com/article/7685311539372524038","corroboration":3,"stars":4,"vendor":"UGREEN 绿联 HomeAgent HA100 / HA100 Pro","signal_type":"新品发布","key_params":"HA100(16GB/64GB eMMC)、HA100 Pro(32GB+128GB/后摩 M50 160TOPS/10W)、本地 NAS+本地 AI+全屋智控、连接智能音箱/摄像头","tech_features":["本地存储 + 本地计算 + 全屋智能控制一体","HA100 Pro 搭载后摩智能 M50 存算一体 160TOPS","Uliya AI 助手自然语言控家/事件查询","Matter/Thread/蓝牙多协议 + 连接绿联智能音箱"],"why_important":"把 AIoT 中枢从云端搬回本地，以存算一体芯片实现家庭主动智能，重塑智能音箱/中枢定位。","terminal_link":"TCL 智能家居与音箱可借鉴'本地 AI + 主动服务'范式，结合 TCL 终端做跨设备本地协同。","note":"澎湃/网易/百度百科多源；9/4 IFA 首发 + 9/12 厦门发布；非去重清单型号(归类为智能音箱/家庭中枢)。"},

 {"region":"国内","title":"韶音 OpenFit 2 AI 亮相云栖：Qwen 大模型 + 实时翻译 30 语种 + AI 会议总结，耳机变生产力终端","category":"AI耳机·耳穿戴","dim":"音频","status":"即将上市","date":"2026-09-22","source_tier":"B","source_name":"ZAKER 新闻（潮新闻/雷科技）","url":"https://app.myzaker.com/news/article.php?pk=6ab23cbe1bc8e0c861000008","corroboration":3,"stars":4,"vendor":"Shokz 韶音 OpenFit 2 AI","signal_type":"新品亮相（功能后续 OTA）","key_params":"Qwen 大模型底座、长时录音 + AI 会议总结 + 实时翻译(30 语种 19 方言)、12 大行业热词调优、19 套纪要模板、AI 实验室(对话/待办/随口记/消息助手)","tech_features":["Qwen 大模型端侧/云端 AI 能力","长时录音 + AI 会议总结 + 结构化纪要","30 语种 19 方言实时翻译","AI 实验室：智能对话/日程待办/随口记/消息助手"],"why_important":"开放式耳机首次深度融合大模型做生产力，把耳机从音频配件升级为'耳边 AI 终端'，定义 AI 耳机新形态。","terminal_link":"TCL 耳机(如 TCL Buds/雷鸟音频)可借鉴其 Qwen 大模型 + 会议转写路线，结合 TCL 终端做跨设备 AI 协同。","note":"Zaker/潮新闻/雷科技多源；9/22 云栖大会首秀，AI 实验室后续 OTA；非去重清单(韶音未收录)。"},

 # ---------- INTL (16-30) ----------
 {"region":"国际","title":"Samsung Galaxy Tab S12 Ultra 规格泄露：Dimensity 9500 + 14.6 寸 AMOLED2X 120Hz + IP68","category":"平板","dim":"SoC/芯片","status":"即将上市","date":"2026-09-19","source_tier":"C","source_name":"MobileBurn","url":"https://mobileburn.com/news/galaxy-tab-s12-plus-and-ultra-full-specs-leak-ahead-of-october-launch","corroboration":1,"stars":2,"vendor":"Samsung","signal_type":"规格泄露","key_params":"MediaTek Dimensity 9500 / 14.6 寸 Dynamic AMOLED 2X 120Hz / 11600mAh+45W / S Pen+IP68 / 欧洲起价 €1539","tech_features":["MediaTek Dimensity 9500 旗舰芯片（三星平板首次弃用骁龙/Exynos）","14.6 英寸 Dynamic AMOLED 2X 120Hz 2K+ 屏","11600mAh 电池 + 45W 快充","内置 S Pen + IP68 防护 + microSD 最高 2TB"],"why_important":"三星旗舰平板转向联发科并强化 IP68 与主动笔，定义 2026 大屏安卓平板新基线，对高端平板芯片选型与生态壁垒影响大。","terminal_link":"三星旗舰平板转向 Dimensity 9500 并强化 IP68 与 S Pen，对 TCL 平板（NXTPAPER/ALCATEL）在高端大屏市场的芯片选型与生态壁垒具对标意义；AMOLED2X 120Hz 已成旗舰标配，TCL 需在大屏 OLED 与类纸护眼双线跟进。","note":"单一欧洲爆料源，10 月 7 日发布前仍有变数；Ultra 与 Plus 同芯不同尺寸，建议关注上市后实测能效。"},

 {"region":"国际","title":"TCL Note A1 NXTPAPER 海外评测：11.5 寸类纸护眼屏 + T-Pen Pro 主动笔","category":"平板","dim":"显示/OLED","status":"已上市","date":"2026-08-09","source_tier":"B","source_name":"WIRED","url":"https://www.wired.com/review/tcl-note-a1-nxtpaper-tablet/","corroboration":3,"stars":4,"vendor":"TCL","signal_type":"评测/上市","key_params":"11.5 寸 NXTPAPER 1440x2200 120Hz 类纸 LCD / MediaTek Helio G100 / 8GB+256GB / 8000mAh / 5.5mm 500g / 标配 T-Pen Pro","tech_features":["11.5 英寸 NXTPAPER 专有类纸护眼屏 120Hz（抗眩光纳米纹理）","T-Pen Pro 主动笔，低延迟高灵敏度压感，附手写转文字","5.5mm 超薄铝合金机身、500g，接近 Kindle Scribe 体量","Helio G100 + AI 会议摘要/音频转写/手写识别"],"why_important":"TCL 自有差异化护眼生产力平板获国际一线媒体背书，验证'类纸屏 + 主动笔 + AI'混合形态在海外市场的接受度。","terminal_link":"TCL 自有 NXTPAPER 类纸护眼屏+主动笔+AI 转写产品，是 TCL 移动终端在生产力/学习平板赛道的差异化旗舰，可直接参照 Wired 评测反馈（缺实体音量键、键盘壳偏重）优化国际上市与定价（$550-600 区间）。","note":"WIRED 评测指出 UI 仍偏半成品、缺硬件音量键；TCL 通过 Kickstarter 起步后已进主流零售渠道，含 Google Play。"},

 {"region":"国际","title":"Redmagic Astra 2 全球开售：量产液冷 + 9.06 寸 OLED 185Hz 游戏平板","category":"平板","dim":"散热","status":"已上市","date":"2026-09-09","source_tier":"C","source_name":"PhoneArena","url":"https://www.phonearena.com/news/the-super-powered-redmagic-astra-2-gaming-tablet-is-now-for-sale-grab-an-early-bird-price_id182484","corroboration":3,"stars":3,"vendor":"Redmagic (nubia)","signal_type":"上市/发售","key_params":"Snapdragon 8 Elite Gen5 + RedCore R4 / 9.06 寸 2.4K OLED 185Hz / AquaCore 2.0 液冷 / 8300mAh+75W / 起价 $749","tech_features":["AquaCore 2.0 量产液冷散热（行业首款液冷平板，液态金属 3.0+4D VC）","Snapdragon 8 Elite Gen5 + RedCore R4 游戏协处理器","9.06 英寸 2.4K OLED 185Hz，Synaptics S3930 触控芯片 2000Hz 采样","8300mAh + 75W 快充，支持旁路充电，双 USB-C"],"why_important":"以'小尺寸 OLED + 量产液冷'重新定义 Android 游戏平板性能上限，给同价位产品设下散热与刷新率新标杆。","terminal_link":"红魔 Astra 2 以量产液冷+小尺寸 OLED 185Hz 定义游戏平板新标杆；TCL 游戏/性能向平板可借鉴其液冷结构与 75W 快充方案，并关注 $749 定价对中高端市场的冲击与双 X 轴马达/旁路充电体验。","note":"PhoneArena 文章为红魔赞助的'开售/早鸟价'稿（已标注赞助），规格另经 Android Central、Uswitch 独立评测交叉确认；无蜂窝版、仅 IP54。"},

 {"region":"国际","title":"Lenovo Legion Y700 AI 发布：8.4 寸 OLED + 5G 独立联网小屏游戏平板","category":"平板","dim":"SoC/芯片","status":"已上市","date":"2026-08-27","source_tier":"C","source_name":"Tablet-News","url":"https://tablet-news.com/?p=67567","corroboration":2,"stars":3,"vendor":"Lenovo","signal_type":"新品发布","key_params":"Snapdragon 8 Elite Gen5 / 8.4 寸 OLED 165Hz 4000nit / 7470mAh+68W / 5G 双卡+Wi-Fi7 / 15000mm² VC+双 X 轴马达","tech_features":["Snapdragon 8 Elite Gen5 + LPDDR5T + UFS 4.1 Pro","8.4 英寸 OLED 2560x1600 165Hz，Dolby Vision，3840Hz PWM","15000mm² 均热板 + 双 X 轴线性马达 + 杜比全景声","5G 双卡独立联网 + Wi-Fi 7 + 蓝牙 5.4，7470mAh 68W"],"why_important":"小尺寸旗舰游戏平板首次加入 5G 独立联网与超大均热板，验证'便携 + 旗舰芯 + 独立蜂窝'组合需求。","terminal_link":"联想以 8.4 寸 OLED+5G 独立联网+15000mm² 均热板切入小屏游戏平板，验证'便携+旗舰芯+独立蜂窝'组合需求；TCL 同类小尺寸平板需强化散热与联网差异化，避免仅拼参数。","note":"中国首发（5499 元起），国际版节奏待观察；6.5mm/298g 超轻薄，AnTuTu 约 458 万。"},

 {"region":"国际","title":"Apple iPhone 18 Pro 发布：A20 Pro 2nm + 可变光圈 + 新一代 VC 均热板","category":"手机","dim":"SoC/芯片","status":"已上市","date":"2026-09-09","source_tier":"A","source_name":"Apple Newsroom","url":"https://nr.apple.com/Dl1b9K0uH9","corroboration":5,"stars":5,"vendor":"Apple","signal_type":"新品发布","key_params":"A20 Pro 2nm 双 16 核神经引擎 / 4800 万主摄可变光圈 / 新一代 VC 均热板(3 倍表面积) / N1 芯片 Wi-Fi7+蓝牙6+Thread / 视频 34h","tech_features":["A20 Pro 2nm 制程，双 16 核神经网络引擎（端侧 AI 翻倍）","4800 万像素融合主摄，六叶片可变光圈（ƒ/1.48）","新一代 VC 均热板，表面积达前代 3 倍，持续性能提升最高 40%","N1 芯片支持 Wi-Fi 7 / 蓝牙 6 / Thread，C2 调制解调器"],"why_important":"定义 2026 旗舰手机技术基线：2nm 芯片、端侧 NPU、可变光圈影像与 VC 均热板散热全面升级。","terminal_link":"苹果 A20 Pro 2nm+双 16 核神经引擎+VC 均热板+可变光圈，定义 2026 旗舰手机技术基线；TCL 旗舰机型在 NPU、散热与影像可控光圈上需对标，并关注 Wi-Fi7/Thread 外围生态与 eSIM 全球策略。","note":"Pro Max 视频续航 43h；约 15 分钟充至 50%；65 国 09-18 发售，另 20 国 09-25 发售。"},

 {"region":"国际","title":"OnePlus 15 印度上市：7300mAh + 120W 有线 / 50W 无线 + 165Hz","category":"手机","dim":"电池/快充","status":"已上市","date":"2026-09-10","source_tier":"A","source_name":"OnePlus India 官网","url":"https://www.oneplus.in/oneplus-15?sku=5011116580","corroboration":3,"stars":4,"vendor":"OnePlus","signal_type":"上市/发售","key_params":"Snapdragon 8 Elite Gen5 / 6.78 寸 165Hz / 7300mAh + 120W 有线 + 50W AIRVOOC / 三摄 50MP+3.5x 潜望 / Wi-Fi7","tech_features":["7300mAh 双芯电池 + 120W SUPERVOOC 有线 + 50W AIRVOOC 无线","Snapdragon 8 Elite Gen5，Oryon CPU @4.608GHz","6.78 英寸 1.15mm 极窄边 165Hz（游戏态），10-bit 100% DCI-P3","三摄 50MP（主+3.5x 潜望+超广）+ 4K 120fps Dolby Vision"],"why_important":"大电池与百瓦快充 + 无线充组合成为安卓旗舰新主流，潜望长焦下放中杯机型。","terminal_link":"一加 15 以 7300mAh+120W/50W 无线+165Hz 刷新凸显大电池快充趋势；TCL 手机在续航与无线充组合上可参考其 50W AIRVOOC 与三摄潜望配置，强化'续航+快充'卖点包装。","note":"印度定价 ₹85,999 起（12+256）；超声波屏下指纹、X 轴线性马达、Wi-Fi7/蓝牙 6；国行/全球节奏相近。"},

 {"region":"国际","title":"Apple Watch Ultra 4 发售：S11 + 高血压通知首发 + 50h 续航","category":"智能手表","dim":"传感器","status":"已上市","date":"2026-09-18","source_tier":"C","source_name":"SmartWearables","url":"https://www.smartwearables.io/news/apple-watch-series-12-ultra-4-launch-day-reviews-praise-health-upgrades-2026","corroboration":3,"stars":3,"vendor":"Apple","signal_type":"发售/评测","key_params":"S11 SiP + Health Sensing System / 高血压通知(首发) + ECG / 钛金属机身 / 50h 续航 / 卫星 SOS","tech_features":["S11 SiP 驱动 Health Sensing System（三代电极 + 常亮光学心率）","首发高血压趋势通知 + ECG app（非直接血压读数）","钛金属更薄机身，50 小时续航（Apple Watch 最长）","卫星紧急 SOS，Ceramic Shield 2"],"why_important":"健康传感跃升为智能手表核心卖点，高血压通知将成行业跟进方向，拉高传感器门槛。","terminal_link":"Apple Watch Ultra 4 首发高血压通知+50h 续航+钛金属，拉升健康传感门槛；TCL 智能手表（MOVETIME）在健康传感与长续航方向需跟进 S11 级 Health Sensing 能力，并前置相关医疗合规。","note":"SmartWearables 为发售日评测汇总；血压/血糖传感器据苹果页面并未列入，属通知而非读数。"},

 {"region":"国际","title":"Apple Watch Series 12 发售：S11 健康传感 + 高血压/睡眠呼吸暂停通知","category":"智能手表","dim":"传感器","status":"已上市","date":"2026-09-12","source_tier":"B","source_name":"Macobserver","url":"https://www.macobserver.com/news/apple-watch-series-12-ultra-4-health-sensing-questions-answered/","corroboration":3,"stars":3,"vendor":"Apple","signal_type":"发售/解读","key_params":"S11 SiP / 高血压+睡眠呼吸暂停通知 / ECG / Ceramic Shield 2 / 128GB / 5G+蓝牙 5.3","tech_features":["S11 SiP + 三代电气心率传感 + 常亮光学心率（最准穿戴心率宣称）","高血压通知 + 睡眠呼吸暂停通知 + ECG app","Ceramic Shield 2（比前代 Ion-X 强 60%），128GB 存储","5G 连接 + 蓝牙 5.3，42/46mm 双尺寸"],"why_important":"健康通知功能向主力走量机型下放，推动全行业智能手表健康算法军备竞赛。","terminal_link":"Series 12 的 S11 三代心率/ECG 与高血压、睡眠呼吸暂停通知，标志健康传感成智能手表核心卖点；TCL 手表产品规划应前置健康算法与认证，关注 watchOS 27 周期追踪等软件能力。","note":"Macobserver 解读苹果官方页边界：血压/血糖传感器均不在列，仅为通知而非诊断；研究样本 1000+ 人（2026 年 7-8 月）。"},

 {"region":"国际","title":"Apple Vision Pro 2 (M5) 传闻：芯片能效与电池内部升级","category":"AR-VR眼镜","dim":"SoC/芯片","status":"进行中","date":"2026-09-03","source_tier":"E","source_name":"AppleScoop","url":"https://applescoop.org/next?id=1630","corroboration":2,"stars":2,"vendor":"Apple","signal_type":"传闻/爆料","key_params":"M5 级芯片 / 沿用设计 / 性能+电池改善 / 更强神经引擎端侧 AI / 轻量化眼镜路线分流","tech_features":["M5 级芯片（性能与能效内部升级，非 redesign）","沿用现款设计，重点改善续航与散热","更强神经网络引擎，提升端侧 AI（实时翻译/环境映射/手眼追踪）","苹果资源向轻量智能眼镜倾斜，Vision Pro 定位高端锚点"],"why_important":"印证 XR 头显'芯片先行、轻量化随后'的产品路线，对 AR/VR 平台迭代节奏有指示意义。","terminal_link":"苹果 Vision Pro 2 以 M5 级芯片做能效/电池内部升级，印证 XR 头显'芯片先行、轻量化随后'路线；TCL/雷鸟(RayNeo)在 AR 眼镜可复用同一定位，优先以芯片能效与重量控制建立差异化。","note":"爆料源（E 级），苹果未官宣；M5 Vision Pro 为小幅升级，transformative 轻量头显/眼镜更晚。"},

 {"region":"国际","title":"RayNeo 雷鸟 iO/GT 系列 AR 眼镜 IFA 亮相：33g MicroLED HUD + B&O 调音 + 40 国上市","category":"AR-VR眼镜","dim":"显示/OLED","status":"已上市","date":"2026-09-04","source_tier":"A","source_name":"PR Newswire / Morningstar","url":"https://www.morningstar.com/news/pr-newswire/20260904cn41011/rayneo-showcases-next-generation-cinematic-ar-and-ai-smart-glasses-at-ifa-2026-with-dolby-and-bang-olufsen","corroboration":2,"stars":5,"vendor":"RayNeo (TCL 体系)","signal_type":"新品发布","key_params":"iO 33g MicroLED HUD / GT Max 微 OLED 影院镜 + Dolby Vision / B&O 调音 / 售价 $499/$429 / 9-4 起 40 国","tech_features":["RayNeo iO：33g 近眼 MicroLED HUD 抬头显示，AI 实时字幕/多语翻译/手势控制","RayNeo GT Max：微 OLED 私人影院镜，全球首款支持 Dolby Vision 播放的 AR 眼镜","Bang & Olufsen 联合调音，Dolby 合作","IFA 2026 创新奖，9 月 4 日起覆盖 40 国（欧美日澳等）"],"why_important":"TCL 体系雷鸟以轻量 MicroLED HUD 与微 OLED 影院镜双线切入全球 AR 眼镜，是国产 AR 出海标杆。","terminal_link":"雷鸟(RayNeo，TCL 体系)以 33g MicroLED HUD+微 OLED 影院镜+B&O 调音+40 国上市，是 TCL 在 AR 眼镜赛道最直接的全球标杆；TCL 移动终端可借势联动手机/平板的 AI 与显示能力，形成'手机+AR 眼镜'多端协同生态。","note":"RayNeo 为 TCL 家族企业，Counterpoint 2026 H1 全球 AR 眼镜出货第一；iO $499/GT Max $429，均为 IFA 创新奖。"},

 {"region":"国际","title":"M6 MacBook Pro 路线图：2nm 芯片秋季落地，跳过 M6 Pro/Max 聚焦 M7 AI","category":"笔记本电脑","dim":"SoC/芯片","status":"进行中","date":"2026-09-09","source_tier":"C","source_name":"TheresMac","url":"https://www.theresmac.com/blog/Mac-Roadmap-Late-2026-What-Is-Coming","corroboration":3,"stars":3,"vendor":"Apple","signal_type":"路线图/爆料","key_params":"M6 2nm 制程 / 14 寸沿用机身 秋季 2026 / 无 M6 Pro/Max / OLED 触控版推迟至 2027 M7 / 起价约 $1999","tech_features":["M6 为苹果首批 2nm 制程芯片，能效显著跃升","14 英寸 M6 MacBook Pro 秋季 2026，沿用现款机身无 redesign","苹果跳过 M6 Pro/Max，集中资源推 AI 向 M7（2027）","OLED+触控 redesign 机型延至 2027，搭 M5 Pro/Max"],"why_important":"PC 芯片向端侧 AI 与能效倾斜，苹果以 2nm 先发并拉大与 Windows 阵营的 NPU 代差。","terminal_link":"苹果 M6 2nm 秋季落地、跳过 M6 Pro/Max 聚焦 M7 AI，预示 PC 芯片向端侧 AI 与能效倾斜；TCL 笔记本/二合一在 NPU 与 Windows on ARM 路线可对标，关注 2nm 带来的续航与本地 AI 体验差距。","note":"TheresMac 为苹果 9-9 发布会后综合供应链与媒体报道的路线图（C 级）；非官方承诺，时间仍可能变动。"},

 {"region":"国际","title":"ASUS Zenbook A14 入选最佳 Windows 本：Snapdragon X2 Elite + 80 TOPS NPU + 27.5h","category":"笔记本电脑","dim":"SoC/芯片","status":"已上市","date":"2026-09-09","source_tier":"B","source_name":"Mashable","url":"https://mashable.com/tech/best-windows-laptops-tested-2026","corroboration":2,"stars":3,"vendor":"ASUS","signal_type":"评测/榜单","key_params":"Snapdragon X2 Elite / 80 TOPS NPU / 14 寸 OLED 2K / 27.5h 续航 / Copilot+ PC","tech_features":["Snapdragon X2 Elite ARM 芯片，NPU 达 80 TOPS","14 英寸 OLED 2K 显示屏","27.5 小时长续航，轻薄机身","Copilot+ PC，端侧 AI 体验"],"why_important":"ARM 平台轻薄本以长续航 + 高 NPU 算力成为 MacBook Air 替代，定义 2026 轻薄 AI 本标准。","terminal_link":"华硕 Zenbook A14 以 Snapdragon X2 Elite 80 TOPS NPU+27.5h 续航定义轻薄 AI 本；TCL 笔记本在 ARM 平台长续航与 Copilot+ 体验上需跟进，关注 NPU TOPS 与电池密度的国际竞争水位。","note":"Mashable 2026-09-09 更新榜单将其列为综合最佳；同期新增 Dell XPS 13 为预算首选，反映 RAM 涨价下的定价分化。"},

 {"region":"国际","title":"Belkin UltraCharge Pro 三合一磁力充电座上架苹果官方店：Qi2 25W","category":"无线充","dim":"认证/合规","status":"已上市","date":"2026-09-09","source_tier":"A","source_name":"Apple Store (HK)","url":"https://www.apple.com/hk-zh/shop/product/hsjk2b/a/belkin-ultracharge-pro-%E4%B8%89%E5%90%88%E4%B8%80%E7%A3%81%E5%8A%9B%E5%85%85%E9%9B%BB%E5%BA%A7","corroboration":2,"stars":3,"vendor":"Belkin","signal_type":"上架/在售","key_params":"Qi2 25W 磁吸 / 三设备同时充(iPhone+Watch+AirPods) / 45W 适配器 / 620g 配重底座","tech_features":["Qi2 技术 25W 磁吸无线充电（较旧 7.5/15W 提速明显）","同时为 3 部 Apple 设备无线充电（iPhone/Watch/AirPods）","附 45W USB-C 电源适配器 + 1.5m C-C 线","可旋转配重底座（620g），苹果官方店独家销售"],"why_important":"Qi2.2(25W) 生态成熟标志，苹果官方渠道主推三合一磁吸充，带动配件认证升级。","terminal_link":"Belkin 三合一 25W Qi2 磁吸充电座上架苹果官方店，标志 Qi2.2(25W) 生态成熟；TCL 无线充配件应加速 Qi2.2 认证以进入苹果周边供应链，并参考其'多设备同充+配重底座'形态。","note":"区别于 dedup 中 Belkin UltraCharge Modular Dock（WIZ052 模块化款）；本款为三合一磁吸 HSJK2，非同一产品。"},

 {"region":"国际","title":"Bose Ultra Open Earbuds (2nd Gen) 发布：OpenAudio + Snapdragon Sound","category":"AI耳机·耳穿戴","dim":"音频","status":"已上市","date":"2026-09-17","source_tier":"A","source_name":"Bose Pressroom","url":"https://www.bose.com/pressroom/bose-sport-open-earbuds-and-bose-ultra-open-earbuds-2nd-gen","corroboration":2,"stars":3,"vendor":"Bose","signal_type":"新品发布","key_params":"开放式耳挂设计 / Bose OpenAudio / Snapdragon Sound aptX Adaptive / 9h+19.5h 续航 无线充盒 / SpeechClarity AI","tech_features":["Bose OpenAudio 开放式声学架构（非骨传导，不提供 ANC）","Snapdragon Sound 支持 aptX Adaptive（安卓高码率低延迟）","9h 单次 + 19.5h 充电盒（支持无线充电），立式收纳","SpeechClarity AI 通话降噪 + Cinema Mode 空间声场"],"why_important":"开放式耳穿戴成高端音频新形态，二代强化声学结构与 AI 通话，带动'舒适 + 通透'需求。","terminal_link":"Bose 二代开放式耳机强化 OpenAudio+Snapdragon Sound+AI 通话降噪，开放式耳穿戴成高端音频新形态；TCL 耳机/耳穿戴可借鉴其声学结构与 9h+19.5h 续航，并探索与手机 AI 翻译/通话的协同。","note":"与 Bose Sport Open Earbuds 同期发布；配色含黑/白烟及限量樱桃巧克力等；无 ANC 为开放式设计取舍。"},

 {"region":"国际","title":"Apple HomePod 3 预期秋季发布：A 系芯片 + Apple Intelligence + Wi-Fi 7","category":"智能音箱","dim":"AI/NPU","status":"进行中","date":"2026-09-09","source_tier":"B","source_name":"Macworld","url":"https://www.macworld.com/article/671090/new-apple-products-iphone-ipad-mac-watch.html","corroboration":2,"stars":3,"vendor":"Apple","signal_type":"路线图/传闻","key_params":"A 系芯片升级 / Apple Intelligence 端侧 AI / Wi-Fi 7 + Thread / 智能家居中枢 / Fall 2026","tech_features":["搭载更新 A 系芯片，支持 Apple Intelligence 端侧 AI","Wi-Fi 7 + Thread，强化全屋智能互联","空间音频升级，作为 Siri/家居中枢","与 HomePod mini 2 同预期 Fall 2026 亮相"],"why_important":"智能音箱向端侧 AI 与全屋互联演进，芯片与无线规格升级将抬升行业基准。","terminal_link":"HomePod 3 预期搭载 A 系芯片+Apple Intelligence+Wi-Fi7/Thread，智能音箱向端侧 AI 与全屋互联演进；TCL 智能音箱应前置 AI 语音与 Matter/Thread 生态兼容，避免仅做播放终端。","note":"Macworld 为持续更新的'即将发布'汇总（B 级），HomePod 3 行标注 Fall 2026 introduction；非官方确认，时间或微调。"},
]

# ---------- helpers ----------
STATUS_RANK = {"即将上市":0, "进行中":1, "已上市":2}
STATUS_CLASS = {"即将上市":"status-coming", "进行中":"status-progress", "已上市":"status-released"}
CIRCLED = ["①","②","③","④","⑤","⑥"]

def star_str(n):
    return "★"*n + "☆"*(5-n)

def sort_key(it):
    return (STATUS_RANK[it["status"]], -int(it["date"].replace("-", "")))

cn = sorted([it for it in ITEMS if it["region"]=="国内"], key=sort_key)
intl = sorted([it for it in ITEMS if it["region"]=="国际"], key=sort_key)
ordered = cn + intl

dim_count = {d:0 for d in DIMS}
for it in ITEMS:
    if it["dim"] in dim_count:
        dim_count[it["dim"]] += 1
covered = sum(1 for d in DIMS if dim_count[d] > 0)

tier_count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for it in ITEMS:
    tier_count[it["source_tier"]] += 1
five_star = sum(1 for it in ITEMS if it["stars"]==5)

def field(label, value, full=False):
    cls = "field full" if full else "field"
    return f'          <div class="{cls}"><div class="field-label">{label}</div><div class="field-value">{value}</div></div>'

def render_card(idx, it):
    badges = (f'<span class="source-tag source-{it["source_tier"].lower()}">{it["source_tier"]}</span>'
              f'<span class="sig-dim" style="background:#f0f9eb;color:#67c23a;border-radius:4px;padding:1px 6px;font-size:11px;">{it["dim"]}</span>'
              f'<span class="stars">{"★"*it["stars"]}{"☆"*(5-it["stars"])}</span>')
    if it["status"] != "已上市":
        badges += f'<span class="status-tag {STATUS_CLASS[it["status"]]}">{it["status"]}</span>'
    else:
        badges += f'<span class="status-tag" style="background:#f0f9eb;color:#67c23a;border:1px solid #c2e7b0;">已上市</span>'
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

def dim_chip(d):
    n = dim_count[d]
    if n > 0:
        return f'<div class="dim-chip on">{d} <span class="dim-count">{n}条</span></div>'
    return f'<div class="dim-chip off">{d} <span class="dim-count">0条</span></div>'
dim_html = "".join(dim_chip(d) for d in DIMS)
pct = round(covered/16*100)

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
print("cn dates:", [it['date'] for it in cn])
print("intl dates:", [it['date'] for it in intl])
print("cn categories:", {c: sum(1 for it in cn if it['category']==c) for c in ['平板','手机','智能手表','AR-VR眼镜','笔记本电脑','无线充','智能音箱','AI耳机·耳穿戴']})
print("intl categories:", {c: sum(1 for it in intl if it['category']==c) for c in ['平板','手机','智能手表','AR-VR眼镜','笔记本电脑','无线充','智能音箱','AI耳机·耳穿戴']})
