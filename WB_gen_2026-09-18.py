# -*- coding: utf-8 -*-
# Generator for WB_2026-09-18_硬件看板.html
# Single HTML, inline CSS, no CDN. 30 cards (CN15 + INTL15).
import datetime

DATE = "2026-09-18"
TITLE = "智能终端硬件情报日报 · " + DATE

# 16 technical dimensions (canonical order for coverage panel)
DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

ITEMS = [
 # ---------- CN (1-15) ----------
 {"region":"国内","title":"华为 MatePad SE 11 英寸(2026 焕新版)上市：120Hz 护眼 LCD + 7700mAh + 全金属机身",
  "category":"平板","dim":"显示/OLED","status":"已上市","date":"2026-08-02","source_tier":"A",
  "source_name":"华为商城（官方商品页）","url":"https://item.vmall.com/product/comdetail/index.html?prdId=10086545786943&sbomCode=2701010133101",
  "corroboration":2,"stars":4,"vendor":"华为 MatePad SE 11(2026 焕新版)","signal_type":"新品上市",
  "key_params":"11 英寸 1920×1200 LCD 120Hz、骁龙 685、7700mAh、全金属一体机身 6.9mm、HarmonyOS 4.2、1799 元起",
  "tech_features":["11 英寸 120Hz 高刷护眼全面屏，莱茵硬件级护眼双重认证","全金属一体机身，厚约 6.9mm","7700mAh 大电池，长续航","教育中心 + 多屏协同，鸿蒙生态"],
  "why_important":"华为入门平板焕新，以护眼屏 + 全金属机身下探价格带，直接影响入门安卓平板的定价与配置基线。",
  "terminal_link":"TCL 入门平板对标其护眼 LCD、金属机身与鸿蒙学习空间打法。",
  "note":"华为商城在售确认；与 14 天去重表内 MatePad Pro/Mini/11.5/Edge 均为不同 SKU。"},

 {"region":"国内","title":"iQOO Pad Ultra 定档 9/29：8.8 英寸 OLED + 2nm 骁龙8 超级至尊版 + 主动散热风扇",
  "category":"平板","dim":"散热","status":"即将上市","date":"2026-09-17","source_tier":"B",
  "source_name":"网易（巴士数码转引 iQOO 官宣）","url":"https://www.163.com/dy/article/L72G9RKC05118K0I.html",
  "corroboration":3,"stars":4,"vendor":"iQOO Pad Ultra","signal_type":"官宣定档",
  "key_params":"8.8 英寸 OLED、第六代骁龙8 超级至尊版（台积电 2nm）、主动风扇 14500rpm/0.94CFM、9000mAh+66W 旁路供电、298g/5.74mm、9 月 29 日发布",
  "tech_features":["内置 PC 级超薄主动散热风扇，14500rpm、风量 0.94CFM、散热面积 1661mm²","首批第六代骁龙8 超级至尊版，台积电 2nm 工艺","9000mAh 级电池 + 66W 快充 + 旁路供电（游戏直供电）","双边拉伸游戏手柄 + 电竞双面夹套件，可变掌机形态"],
  "why_important":"主流品牌首次把主动风扇带进量产平板并官宣定档，小尺寸电竞平板赛道进入宣发窗口，直接定义竞品对标参数。",
  "terminal_link":"与荣耀 WIN 平板同窗口卡位，为 TCL 小尺寸性能平板的散热架构与配件生态规划提供直接参照。",
  "note":"进展更新：此前已覆盖“iQOO Pad Ultra 曝光”，本期为官方定档 9/29 + 完整规格与配色公布，属重大进展非重复报道。"},

 {"region":"国内","title":"荣耀 WIN 平板开启盲约：骁龙8 至尊版 + 内置主动风扇，电竞平板再添一员",
  "category":"平板","dim":"SoC/芯片","status":"即将上市","date":"2026-09-17","source_tier":"B",
  "source_name":"网易（安卓中文网）/ 荣耀智慧生活官宣","url":"https://www.163.com/dy/article/L729P4GU0511A61R.html",
  "corroboration":2,"stars":4,"vendor":"荣耀 WIN 平板","signal_type":"盲约开启",
  "key_params":"第五代骁龙8 至尊版（官方确认）、内置主动散热风扇（核心降温 10°C+）、WIN 电竞家族设计、盲约已开启、发布时间未官宣",
  "tech_features":["高通骁龙8 Elite Gen5 旗舰平台（官方确认）","内置主动散热风扇，智能调速，重载场景满血输出","镭雕激光纹理电竞背板，红色 WIN 标识","接入荣耀 WIN 生态，跨设备互联与外设拓展"],
  "why_important":"荣耀把手机端主动散热方案延伸到平板，与 iQOO Pad Ultra 同窗口卡位，电竞平板细分赛道正式成型。",
  "terminal_link":"主动风扇进平板的第二家官宣，为 TCL 平板散热架构与电竞子产品线规划提供对照样本。",
  "note":"进展更新：此前已覆盖“荣耀 WIN Pad Mini 官宣”，本期为盲约开启 + 骁龙8E5/风扇官方确认，属进展非重复。"},

 {"region":"国内","title":"Ulefone Armor Pad 5 Ultra 亮相 IFA：11 英寸三防平板塞入 24200mAh + 200 流明投影",
  "category":"平板","dim":"结构/工艺","status":"即将上市","date":"2026-09-11","source_tier":"C",
  "source_name":"Tablet News","url":"https://tablet-news.com/ulefone-s-armor-pad-5-ultra-puts-a-200-lumen-projector-in-a-24-200mah-rugged-tablet/",
  "corroboration":2,"stars":3,"vendor":"Ulefone Armor Pad 5 Ultra","signal_type":"展会亮相",
  "key_params":"11 英寸、天玑 7400X、24200mAh + 120W 快充、200 流明自动对焦投影、uSmart 配件生态",
  "tech_features":["24200mAh 电池 + 120W 快充，面向户外与工业作业场景","一体化集成 200 流明自动对焦投影，可投 120 英寸 1080P","联发科天玑 7400X 平台，同场发布更紧凑的 Armor Pad 6","uSmart 配件生态：内窥镜/数码显微镜，平板作显示与供电中枢"],
  "why_important":"三防平板靠功能拼合（大电池 + 投影 + 测量外设）差异化，是边缘品类不卷轻薄、卷功能集成的路线样本。",
  "terminal_link":"对 TCL 教育/行业定制平板的功能集成策略（电池容量、外设生态、可靠性认证组合）有借鉴意义。",
  "note":"深圳品牌出海 IFA 亮相，归国内区；屏幕分辨率/重量/售价未公布，待量产确认。"},

 {"region":"国内","title":"ColorOS 17 正式发布：端侧大模型 Linear Attention + 128K 上下文，Find X10/一加16 首发",
  "category":"手机","dim":"AI/NPU","status":"进行中","date":"2026-09-17","source_tier":"A",
  "source_name":"央广网（ODC26 官方发布）","url":"https://www.cnr.cn/tech/techgd/20260917/t20260917_527816624.shtml",
  "corroboration":3,"stars":4,"vendor":"OPPO ColorOS 17","signal_type":"系统发布",
  "key_params":"流体设计全感官语言、极光引擎（内存占用 -25%/渲染负载 -30%）、端侧大模型 Linear Attention 128K 上下文（内存 -48%/能耗 -55%）、覆盖 7.7 亿用户、10 月 8 日存量推送",
  "tech_features":["On-Device Compute 端侧大模型首发 Linear Attention 架构，原生 128K 上下文","Persona X 记忆共生引擎：数据/环境/行为三层感知","Agent Matrix 智能体框架，小布覆盖 700+ 细分场景","Find X10 系列与一加 16 首发，10 月 8 日起存量机推送"],
  "why_important":"安卓阵营端侧 AI OS 的年度标杆发布，128K 端侧上下文与智能体生态直接定义手机/平板 AI 体验基线。",
  "terminal_link":"TCL 手机/平板 OS 的端侧大模型架构、智能体与跨端协同路线的对标信号。",
  "note":"珠海 ODC26 发布；软件类信号，状态取“进行中”（10/8 存量推送未完成）。"},

 {"region":"国内","title":"Redmi Note 17 Pro / Pro Max 印度发布：Pro Max 带来 10000mAh + 100W，第二款破万毫安机型",
  "category":"手机","dim":"电池/快充","status":"已上市","date":"2026-09-15","source_tier":"B",
  "source_name":"Beebom Gadgets","url":"https://gadgets.beebom.com/news/all-upcoming-phones-launching-this-week-september-14-september-20",
  "corroboration":3,"stars":4,"vendor":"Redmi Note 17 Pro / Pro Max","signal_type":"新品发布",
  "key_params":"Pro Max：6.83 英寸 1.5K 120Hz AMOLED + 骁龙6 Gen5 + 10000mAh + 100W + 22.5W 反充；Pro：9000mAh + 67W；IP68/69；9 月 15 日印度发布",
  "tech_features":["10000mAh 大电池，官方称轻度使用超 4 天，为全球第二款破万毫安机型（仅次于 realme P4 Power 10001mAh）","Pro Max 100W 有线 + 22.5W 反向充电，Pro 版 9000mAh + 67W","骁龙6 Gen5（Pro Max）/ 骁龙6s Gen4（Pro），6.83 英寸 1.5K 120Hz AMOLED","IP68/69 防护 + 50MP 主摄，squircle Deco 设计"],
  "why_important":"10000mAh 级电池进入主流价位段（全球第二款），电池容量军备竞赛向中端扩散，重塑续航卖点基线。",
  "terminal_link":"TCL 手机中端续航策略与硅碳/大电池方案选型的直接参照。",
  "note":"国产品牌印度市场发布，归国内区；电池容量为官方宣传口径。"},

 {"region":"国内","title":"小米手表 S5 41mm 官宣：首发表端澎湃 OS 4 + 580mAh/14 天续航 + 车家互联",
  "category":"智能手表","dim":"无线通信","status":"即将上市","date":"2026-09-17","source_tier":"B",
  "source_name":"新浪财经（转 IT之家/官方官宣）","url":"https://finance.sina.com.cn/stock/t/2026-09-17/doc-inisczpx0399672.shtml",
  "corroboration":3,"stars":4,"vendor":"小米手表 S5 41mm","signal_type":"官宣",
  "key_params":"1.32 英寸 OLED 3000nits、36g/9.9mm、莹白陶瓷表圈、580mAh 最长 14 天、表端澎湃 OS 4、双频 GNSS、预计与小米 18 Pro 同场",
  "tech_features":["首发搭载表端澎湃 HyperOS 4","深度联动小米汽车：控车/主动提醒，可直看智能门锁摄像头画面","女性生理周期监测 + 饮食热量管理 + 紫外线提示","36g/9.9mm 轻量陶瓷表圈 + 双频 GNSS 定位"],
  "why_important":"小米穿戴 OS 首次表端大版本 + 车家互联深度绑定，手表作为生态入口的价值被强化。",
  "terminal_link":"TCL 手表若做生态互联（车/家/手机），小米的表端 OS 与互联路径值得对标。",
  "note":"9 月 15 日开启预约；电池口径以官方微博 580mAh（上代 320mAh）为准，待发布终确认。"},

 {"region":"国内","title":"秋果计划 Wigain Flow 全彩 AI 眼镜定档 9/23 数贸会全球首发",
  "category":"AR-VR眼镜","dim":"显示/OLED","status":"即将上市","date":"2026-09-09","source_tier":"A",
  "source_name":"秋果计划官网","url":"https://www.qiuguojihua.com/journalism/realtime/1697.html",
  "corroboration":3,"stars":3,"vendor":"秋果计划 Wigain Flow","signal_type":"官宣定档",
  "key_params":"全彩光波导（碳化硅）、自研绿洲多模态大模型 + 原生 AI OS、语音/手势/眼动/指环交互、9 月 23 日数贸会首秀、9 月 25 日全球首发",
  "tech_features":["全彩光波导显示，碳化硅方案，户外显示优化","自研绿洲多模态大模型 + 原生 AI 操作系统，主动智能 Agent","语音 + 手势 + 眼动 + 智能戒指多模态交互","主打无感佩戴，轻量化长时佩戴"],
  "why_important":"国产全彩 AI 眼镜新势力，以无感佩戴差异化切入办公场景，全彩光波导阵营再添新玩家。",
  "terminal_link":"TCL AR 眼镜对标其全彩光波导与无感佩戴路线。",
  "note":"9 月 23 日杭州数贸会 3 号馆，9 月 25 日 4 号馆论坛全球首发。"},

 {"region":"国内","title":"Rokid Ai Glasses Style 日本发布：38.5g 无屏 AI 眼镜 + 76 语种翻译 + 多模型开放生态",
  "category":"AR-VR眼镜","dim":"摄像头","status":"已上市","date":"2026-09-15","source_tier":"C",
  "source_name":"HiFi.Fan（Rokid 日本发布会）","url":"https://hifi.fan/stories/rokid-ai-glasses-style-brings-38-5g-display-free-ai-wearable-design-priced-at-64-990-yen",
  "corroboration":2,"stars":3,"vendor":"Rokid Ai Glasses Style","signal_type":"海外发布",
  "key_params":"38.5g 无显示屏、12MP 索尼 IMX681（109° FOV）、骁龙 AR1、YodaOS 多模型、76 语种在线翻译、64990 日元、约 12h 续航",
  "tech_features":["取消内置显示屏换轻量：38.5g、钛合金铰链、支持 -15D~+15D 处方镜片直装","12MP 索尼 IMX681 摄像头，3K/30fps 视频，录制指示灯","YodaOS + AIUI 开放生态：ChatGPT/Gemini/DeepSeek/Qwen 可切换","开放式双 Hi-Fi 扬声器，翻译结果经音频输出不挡视线"],
  "why_important":"“无屏 + 轻量 + 开放多模型”路线头部玩家落地日本，与带显示路线形成镜像，验证两条产品范式并行。",
  "terminal_link":"TCL AR 眼镜的无屏轻量路线与多模型接入策略参照，处方镜片直装是差异化点。",
  "note":"与去重表内“Rokid 澳洲 49g 双目显示版”为不同产品（无屏 Style）；9 月 1 日预售、9 月 15 日发布。"},

 {"region":"国内","title":"新款华为 MateBook Fold 非凡大师发布：18 英寸双层 OLED 手写折叠屏 + 麒麟 X90 Plus",
  "category":"笔记本电脑","dim":"折叠屏","status":"已上市","date":"2026-08-05","source_tier":"A",
  "source_name":"新华网","url":"https://www.news.cn/tech/20260805/0822750fd7594258b725d6a6d56644ec/c.html",
  "corroboration":3,"stars":5,"vendor":"华为 MateBook Fold 非凡大师(新款)","signal_type":"新品发布",
  "key_params":"18 英寸双层 OLED UTG 柔性玻璃（40 微米）3.3K 1600nit、玄武水滴铰链（锆基液态金属）、麒麟 X90 Plus、手写笔原生支持、24999 元起",
  "tech_features":["量产 18 英寸超薄 UTG 柔性玻璃，40 微米，抗冲击 +90%、抗弯折 +10 倍","玄武水滴铰链，锆基液态金属，100-120 度无级悬停","鸿蒙折叠 PC 首次原生支持手写笔，远场空鼠","双层 OLED LTPO 能效 +30%，屏幕寿命 3 倍，SGS 五星抗跌落"],
  "why_important":"折叠 PC 交互里程碑，大屏手写 + 双屏分屏生产力，直接定义折叠笔记本的可靠性与交互上限。",
  "terminal_link":"TCL 折叠 PC 对标其 18 英寸 UTG 与玄武铰链路线。",
  "note":"8 月 5 日发布、8 月 14 日开售，含 M-Pen 3；与去重表无冲突。"},

 {"region":"国内","title":"七彩虹橘宝 X16 Pro 开售：锐龙7 8745HX + RTX 5060 + 2.5K 180Hz，572 TOPS AI 算力下探主流价",
  "category":"笔记本电脑","dim":"散热","status":"已上市","date":"2026-09-01","source_tier":"D",
  "source_name":"今日头条（柠玖说）","url":"https://m.toutiao.com/article/7680470760281457186",
  "corroboration":1,"stars":2,"vendor":"七彩虹 橘宝 X16 Pro","signal_type":"新品开售",
  "key_params":"锐龙7 8745HX（5nm Zen4）、RTX 5060 8GB GDDR7、2.5K 180Hz、双风扇 + 4 热管矩阵出风、572 TOPS（厂商标称）、9 月 1 日开售",
  "tech_features":["锐龙7 8745HX + RTX 5060：DLSS 4 多帧生成 + 光线追踪","双风扇 + 4 加粗热管 + 矩阵式出风，多性能模式切换","2.5K 180Hz 电竞屏","厂商标称 572 TOPS AI 算力，兼顾本地 AI 应用"],
  "why_important":"二线品牌把 RTX 5060 + 高刷屏压进主流价位，AI 算力成为游戏本新营销参数，反映价格竞争烈度。",
  "terminal_link":"TCL 笔电若走性价比路线，二线品牌的配置-价格卡位与散热方案可作参照。",
  "note":"自媒体单一信源，规格未交叉印证，按 D 级规则取 2 星，待官网/电商页复核。"},

 {"region":"国内","title":"Momax 1-Power S.Pass² Air 获 IFA 创新奖：6mm 超薄半固态磁吸无线充",
  "category":"无线充","dim":"BMS/电源","status":"进行中","date":"2026-09-04","source_tier":"B",
  "source_name":"美通社（PR Newswire）","url":"https://www.prnewswire.com/apac/zh/news-releases/momax--2026-ifa--302878441.html",
  "corroboration":3,"stars":4,"vendor":"Momax 1-Power S.Pass² Air","signal_type":"获奖/发布（IFA 2026）",
  "key_params":"厚 6.0mm 全球最薄不锈钢镜面、半固态电池(SSB)、Qi2 官方认证磁吸无线充、SS Assurance 安全认证（GB38031/UN38.3/CCC/RoHS）",
  "tech_features":["6.0mm 极致超薄不锈钢镜面，口袋级形态","首发半固态电池(SSB)技术，安全新标杆","Qi2 官方认证高速磁吸无线充","SS Assurance 安全体系：通过 GB38031/UN38.3/CCC/RoHS"],
  "why_important":"半固态电池首次落地磁吸无线充品类，超薄 + 安全双方向，IFA 连续两年获奖验证路线。",
  "terminal_link":"TCL 无线充/移动电源对标其半固态电池材料与超薄镜面工艺、安全认证组合。",
  "note":"荣获 IFA 2026 创新大奖 Best in Mobility；量产交付节奏待确认，状态取“进行中”。"},

 {"region":"国内","title":"小米小爱音箱 Play 增强版亮相：新增 LED 时钟 + 红外遥控",
  "category":"智能音箱","dim":"音频","status":"已上市","date":"2026-08-03","source_tier":"C",
  "source_name":"苏宁头条","url":"https://news.suning.com/m/wtoutiao/bcdetail/4421907928.html",
  "corroboration":2,"stars":3,"vendor":"小米小爱音箱 Play 增强版","signal_type":"新品亮相/预售",
  "key_params":"LED 时钟显示（亮度自适应）、红外 + WiFi + 蓝牙网关、360° 导音锥、遥控 6000+ 品牌家电、129 元到手",
  "tech_features":["新增 LED 时钟显示，亮度自适应，床头闹钟场景","红外 + WiFi + 蓝牙 Mesh 网关，遥控 6000+ 品牌家电","360° 导音锥腔体","自动同步 QQ 音乐绿钻/收藏、喜马拉雅/蜻蜓 FM"],
  "why_important":"百元智能音箱以 LED 时钟 + 红外网关强化家居入口属性，低价位入口型音箱的配置打法参照。",
  "terminal_link":"TCL 智能音箱对标其红外网关与多平台内容集成。",
  "note":"8 月 3 日亮相，预售价 129 元。"},

 {"region":"国内","title":"怀芯声学 AuraBuds S1 发布：工业声学 AI 下放，ENC 峰值 73.99dB 商务效率耳机",
  "category":"AI耳机·耳穿戴","dim":"音频","status":"已上市","date":"2026-09-03","source_tier":"B",
  "source_name":"太平洋电脑网","url":"https://g.pconline.com.cn/x/2182/21822060.html",
  "corroboration":3,"stars":4,"vendor":"怀芯声学（SHXVO）AuraBuds S1","signal_type":"新品发布",
  "key_params":"HXUltraEdge NC 极境降噪 ENC 峰值 73.99dB、AI 实时转写 + 智能总结、充电仓独立录音笔、机身独立离线存储、9 月 3 日北京发布",
  "tech_features":["HXUltraEdge NC 极境降噪，ENC 峰值 73.99dB，远超行业常见 20-30dB","自研盲信号处理 + 跨域泛化 + 端侧实时计算，工业声学 AI 降维","AI 实时转写 + 智能总结，通话即生成可检索纪要","充电仓独立录音笔 + 机身离线存储 + 一键物理静音 + 双设备无缝切换"],
  "why_important":"工业声学 AI 移植消费端，超高 ENC 降噪定义商务效率耳机新品类，端侧实时计算是关键路径。",
  "terminal_link":"TCL AI 耳机对标其工业级声学 AI 降噪迁移与会议纪要闭环。",
  "note":"ASG 战略 S 终端首款，9 月 10 日服贸会全球首发。"},

 {"region":"国内","title":"飞书 × 安克第二款 AI 会议耳机发布：录音自动同步飞书工作流",
  "category":"AI耳机·耳穿戴","dim":"AI/NPU","status":"已上市","date":"2026-09-15","source_tier":"B",
  "source_name":"每日经济新闻","url":"https://www.nbd.com.cn/articles/2026-09-15/4581772.html",
  "corroboration":3,"stars":3,"vendor":"飞书 × 安克 AI 会议耳机","signal_type":"新品发布（未来无限大会）",
  "key_params":"记录手机通话 + 线上会议、录音自动同步飞书、转写/总结/翻译/待办提炼、9 月 15 日飞书未来无限大会发布",
  "tech_features":["录音自动同步飞书，跨端无缝沉淀","飞书内完成转写/总结/翻译/待办提炼","覆盖手机通话与线上会议双场景","飞书 × 安克第二款 AI 办公硬件"],
  "why_important":"办公软件厂商 + 硬件厂联合定义 AI 会议耳机，软硬协同把会议变成可管理资产，是 AI 耳机生态绑定新范式。",
  "terminal_link":"TCL AI 耳机对标其软件 + 硬件协同与会议资产管理模式。",
  "note":"飞书 CEO 谢欣发布，与安克合作第二款 AI 硬件。"},

 # ---------- INTL (16-30) ----------
 {"region":"国际","title":"荣耀 Pad X9b Max 国际铺货：13 英寸 2.5K 120Hz + 10100mAh，菲律宾 9/19 开卖",
  "category":"平板","dim":"显示/OLED","status":"即将上市","date":"2026-09-16","source_tier":"C",
  "source_name":"GizNewsDaily","url":"https://giznewsdaily.com/honor-launches-13-inch-android-tablet-with-120hz-display",
  "corroboration":3,"stars":3,"vendor":"荣耀 Pad X9b Max","signal_type":"新品发布",
  "key_params":"13 英寸 2500×1560 LCD 120Hz 700nits、骁龙 6s 4G Gen2、10100mAh + 45W、6.72mm/618g、菲律宾 19999 比索起 9 月 19 日开售",
  "tech_features":["13 英寸 2500×1560 120Hz LCD，峰值 700nits，IMAX Enhanced 认证","骁龙 6s 4G Gen2 六纳米八核，6GB 可扩 12GB 虚拟内存，存储可扩 2TB","10100mAh + 45W SuperCharge，国际版多为纯 Wi-Fi 版","四扬声器 DTS:X + Hi-Res Audio，6.72mm/618g"],
  "why_important":"超大屏 + 流媒体认证切中端大屏市场，10100mAh 与 120Hz 是其在中低价位的差异化组合。",
  "terminal_link":"与 TCL 平板在 200 美元级大屏娱乐平板正面竞争，屏幕/扬声器/电池为最直接对比项。",
  "note":"待印证：国际版命名与中国市场 Pad X10 Pro Max 差异未获官方解释；来源为聚合站。"},

 {"region":"国际","title":"OPPO Pad Mini 柔光版通过 SIRIM/BIS/IMDA 认证：8.8 英寸 144Hz AMOLED + 骁龙8 Gen5",
  "category":"平板","dim":"手写笔/触控","status":"即将上市","date":"2026-09-16","source_tier":"C",
  "source_name":"GizmoIndo","url":"https://gizmoindo.com/news/oppo-s-anti-glare-compact-flagship-tablet-prepares-for-global-debut",
  "corroboration":2,"stars":3,"vendor":"OPPO Pad Mini 柔光版(OPD2516)","signal_type":"认证曝光",
  "key_params":"型号 OPD2516、8.8 英寸 2520×1680 AMOLED 144Hz（微蚀刻柔光）、骁龙8 Gen5、8000mAh、同批认证确认 OPPO Pencil 3 / Pencil 3 Pro",
  "tech_features":["8.8 英寸 AMOLED 144Hz，微蚀刻防眩光柔光层兼顾反射抑制与触控灵敏度","骁龙8 Gen5 旗舰平台下放小尺寸机身","8000mAh 电池，小尺寸高性能平板中的大容量方案","同批认证确认 OPPO Pencil 3 与 Pencil 3 Pro 两支主动笔，指向生产力定位"],
  "why_important":"小尺寸高性能安卓平板长期缺位，OPPO 以柔光屏 + 旗舰芯切入 iPad mini 与电竞平板之间的空档。",
  "terminal_link":"对 TCL NXTPAPER 类纸/防眩光技术路线构成同维度竞品参照，可对比微蚀刻柔光 + 小尺寸高刷组合价值。",
  "note":"待印证：认证仅证明量产前阶段，全球定价与时间未公布；建议回 SIRIM/BIS 原始条目复核。"},

 {"region":"国际","title":"iPad 第 12 代预计秋季发布：A18/A19 + 首次完整下放 Apple Intelligence，349 美元起",
  "category":"平板","dim":"SoC/芯片","status":"即将上市","date":"2026-09-17","source_tier":"B",
  "source_name":"PhoneArena","url":"https://www.phonearena.com/ipad-2026-release-date-price-features-news",
  "corroboration":3,"stars":4,"vendor":"Apple iPad 第 12 代","signal_type":"发布预告",
  "key_params":"10.9 英寸 2360×1640 60Hz LCD、A18 或 A19、约 8GB 内存、约 7698mAh、128GB 版维持 349 美元、秋季发布",
  "tech_features":["入门 iPad 首次完整支持 Apple Intelligence 与重构后 Siri AI","A18 或 A19 替代现款 A16，性能预计提升约两成","预期搭载与 iPhone 17 同源的 N1 无线芯片","iPadOS 27 出厂预装，硬件形态与 60Hz 屏幕维持不变"],
  "why_important":"入门 iPad 首次获得完整端侧 AI 能力，将重新抬高 350 美元档平板的 AI 门槛，压缩中低端安卓平板的软件差异化空间。",
  "terminal_link":"对 TCL 平板在欧洲与新兴市场入门价位段构成最直接的 AI 能力对标压力，需评估端侧 AI 在中低端 SoC 的落地路径。",
  "note":"待印证：型号/芯片/时间均为供应链与媒体推测，苹果未官宣；不排除改名 iPad Neo。"},

 {"region":"国际","title":"谷歌 Pixel Tablet 正式停产下架：安卓平板阵营再失一员，商店平板品类整体移除",
  "category":"平板","dim":"AI/NPU","status":"进行中","date":"2026-09-09","source_tier":"B",
  "source_name":"9to5Google","url":"https://9to5google.com/2026/09/09/google-pixel-tablet-discontinued",
  "corroboration":3,"stars":3,"vendor":"Google Pixel Tablet","signal_type":"产品退市",
  "key_params":"2023 年发布、Tensor G2、10.95 英寸 2560×1600、系统更新支持至 2028 年 6 月、商店平板品类入口已删除",
  "tech_features":["谷歌官方商店删除平板品类入口，Pixel Tablet 链接重定向至首页","Pixel Tablet 2 及第三代机型因盈利问题先后被取消","亚马逊/百思买等第三方渠道新机库存清零","存量设备保留至 2028 年 6 月的系统与安全更新"],
  "why_important":"谷歌退出平板硬件，安卓平板家庭 AI 中枢入口进一步集中到三星/联想与国内厂商，中端竞争更依赖成本与生态整合。",
  "terminal_link":"TCL 平板可承接原属 Pixel Tablet 的中端安卓平板与带底座家庭中枢需求（大屏 + 磁吸底座形态机会）。",
  "note":"待印证：谷歌未发官方停产声明，仅以商店移除释放信号；是否彻底退出平板品类无官方时间表。"},

 {"region":"国际","title":"三星 Galaxy Z Fold 8 Ultra 发布：首款 Ultra 折叠 + 骁龙8 Elite Gen5 for Galaxy + 钛缓震层",
  "category":"手机","dim":"折叠屏","status":"已上市","date":"2026-07-22","source_tier":"A",
  "source_name":"Samsung 香港官网（官方新闻稿）","url":"https://www.samsung.com/hk/news/product/samsung-galaxy-z-fold8-ultra-z-fold8-and-z-flip8-foldables-perfected-for-every-way-of-living",
  "corroboration":3,"stars":5,"vendor":"Samsung Galaxy Z Fold 8 Ultra","signal_type":"新品发布",
  "key_params":"8.0 英寸 QXGA+ Dynamic AMOLED 2X 120Hz、骁龙8 Elite Gen5 for Galaxy、5000mAh + 45W、钛缓震层、S Pen 支持、7 月 22 日伦敦 Unpacked 发布",
  "tech_features":["三星首款 Ultra 定位折叠屏，2 亿像素主摄","钛缓震层结构，可靠性升级","双路充电架构，45W 有线","Galaxy AI + Gemini Intelligence 深度整合"],
  "why_important":"折叠屏首次引入 Ultra 定位，大屏生产力 + 影像旗舰化，重新划分折叠高端市场的对标基准。",
  "terminal_link":"TCL 折叠产品线对标其 Ultra 化定位、钛缓震结构与影像方案。",
  "note":"7 月 22 日发布，8 月 7 日公开发售；与去重表内 Z Fold 8 标准版为不同 SKU（Ultra）。"},

 {"region":"国际","title":"Nothing Phone (4b) 马来西亚上市：6.77 英寸 120Hz AMOLED + 5200mAh，9/20 开卖 1599 林吉特",
  "category":"手机","dim":"电池/快充","status":"即将上市","date":"2026-09-10","source_tier":"B",
  "source_name":"SoyaCincau","url":"https://soyacincau.com/2026/09/10/nothing-phone-4b-malaysia-price-specs-rm1599/",
  "corroboration":3,"stars":3,"vendor":"Nothing Phone (4b)","signal_type":"区域上市",
  "key_params":"6.77 英寸 AMOLED 120Hz 2000nits、骁龙6 Gen 4、8GB+128GB、5200mAh + 33W + 7.5W 反向、1599 林吉特（约 2600 元）",
  "tech_features":["官方称品牌迄今续航最长机型，5200mAh + 33W，30 分钟充至五成","第三代 Glyph Bar 亮度提升四成，保留透明设计语言","IP64、屏下指纹、Wi-Fi 6、蓝牙 6.0、双扬声器","承诺三次安卓大版本升级 + 六年安全补丁"],
  "why_important":"中端机把长续航与六年安全更新打包成核心卖点，软件支持周期正成为中低价位段的新竞争变量。",
  "terminal_link":"TCL 手机在东南亚中端价位的卖点组合与系统支持周期策略参照。",
  "note":"该机 7 月已全球发布，本轮为马来西亚区域上市（9 月 20 日开卖）。"},

 {"region":"国际","title":"三星 Galaxy Watch 9 发布：首发 Snapdragon Wear Elite + 3000nit + 7 年更新",
  "category":"智能手表","dim":"SoC/芯片","status":"已上市","date":"2026-07-22","source_tier":"A",
  "source_name":"Samsung 新加坡官网（官方规格页）","url":"https://www.samsung.com/sg/mobile/mobile-phone-buying-guide/galaxy-watch9-watch-ultra2-specs-features",
  "corroboration":2,"stars":4,"vendor":"Samsung Galaxy Watch 9","signal_type":"新品发布",
  "key_params":"40/44mm、Super AMOLED 3000nit、Snapdragon Wear Elite（W5 系迭代）、390/445mAh、Wear OS、蓝牙 6.0、7 年系统更新",
  "tech_features":["首款搭载 Snapdragon Wear Elite 平台的 Galaxy Watch","3000nit 高亮 Super AMOLED","Galaxy AI 健康套件（7 年更新承诺）","蓝牙 6.0 + 双频定位"],
  "why_important":"穿戴平台芯片换代（高通 Wear 线升级）+ 超长系统支持，智能手表平台选型与生命周期策略的标杆信号。",
  "terminal_link":"TCL 手表平台选型（Snapdragon Wear 路线）与长周期更新承诺的参照。",
  "note":"7 月 22 日 Unpacked 发布；与去重表内 Watch Ultra 2 为不同 SKU。"},

 {"region":"国际","title":"Actxa Spark Band 亮相 IFA：22g 无屏手环以 BGEM 技术实现一分钟无创血糖趋势估算",
  "category":"智能手表","dim":"传感器","status":"即将上市","date":"2026-09-09","source_tier":"D",
  "source_name":"Hungary Journal（公关稿转载）","url":"https://hungaryjournal.com/press-release/actxa-launches-spark-band-targeting-glucose-monitoring-market-at-ifa-2026-usa-2026",
  "corroboration":2,"stars":2,"vendor":"Actxa Spark Band","signal_type":"展会亮相",
  "key_params":"22g 锌合金无屏机身、BGEM 一分钟血糖趋势估算、14 天续航、IP68、149 美元、9 月 24 日预售/11 月 18 日发货",
  "tech_features":["BGEM 技术输出 AI 血糖快照，一分钟给出估算区间（健康参考非医疗诊断）","以睡眠 HRV 七日基线计算恢复度，输出 30 天恢复趋势","无订阅费，蓝牙低功耗，兼容安卓 8.0 / iOS 15.6 以上","亚太/欧洲/中东/北美同步发售，预售最高四折"],
  "why_important":"无创血糖趋势估算下放到百元级无屏手环形态，代谢类传感从专业设备向消费可穿戴下沉的风向标。",
  "terminal_link":"TCL 穿戴健康传感路线与无屏轻量形态、订阅商业模式取舍的参考。",
  "note":"待印证：公关稿多站转载、配图标注 AI 生成，缺第三方实测与医疗合规依据，建议以官网规格页复核。"},

 {"region":"国际","title":"Meta Ray-Ban Display 智能眼镜：右镜全彩波导 5000nit + 神经腕带，799 美元 9/30 开售",
  "category":"AR-VR眼镜","dim":"显示/OLED","status":"即将上市","date":"2026-09-17","source_tier":"B",
  "source_name":"eloutput（Meta Connect 官方发布多源印证）","url":"https://en.eloutput.com/?p=570422/",
  "corroboration":3,"stars":4,"vendor":"Meta Ray-Ban Display","signal_type":"新品发布",
  "key_params":"右镜片全彩波导 600×600 / 5000nit、12MP 摄像头、Neural Band 肌电腕带（sEMG）、69g、6h 续航、799 美元、9 月 30 日美国开售",
  "tech_features":["首款内置私密镜片显示器的 Meta AI 眼镜","Neural Band sEMG 肌电手势控制","实时字幕/翻译/视频通话，600×600 单眼显示","欧洲/加拿大 2026 年内跟进"],
  "why_important":"AI 眼镜从纯音频走向带显示形态 + 腕带交互范式，定义消费级 AI 眼镜的下一代交互基准。",
  "terminal_link":"TCL 智能眼镜路线（显示引入时点、交互外设、定价带）的最直接对标。",
  "note":"Meta 官方因反爬未能直抓，URL 为多源印证聚合稿；9 月 30 日美国开售。"},

 {"region":"国际","title":"三星 Galaxy Glasses（Intelligent Eyewear）亮相 Unpacked：Android XR 首款真智能眼镜",
  "category":"AR-VR眼镜","dim":"AI/NPU","status":"即将上市","date":"2026-07-22","source_tier":"B",
  "source_name":"GCN（Unpacked 官方发布多源印证）","url":"https://gcn.com/samsung-intelligent-eyewear-debuts-london-unpacked/20385",
  "corroboration":2,"stars":4,"vendor":"Samsung Galaxy Glasses","signal_type":"新品发布",
  "key_params":"无屏音频眼镜、Snapdragon AR1 Gen1、Android XR + Gemini、12MP 摄像头、9h 续航（充电盒再充 7 次）、预计秋季上市",
  "tech_features":["Android XR 生态首款真智能眼镜（Google/Gentle Monster/Warby Parker 合作）","Gemini 语音助手 + 白板/会议摄取整理","实时翻译与导航","12MP 摄像头 + 开放式音频"],
  "why_important":"安卓 XR 生态眼镜首发，无屏音频路线先落地 AI 助手场景，与 Meta 显示路线形成两极。",
  "terminal_link":"TCL 眼镜生态选型（Android XR 阵营 vs 自研路线）的参照。",
  "note":"7 月 22 日伦敦 Unpacked 亮相，预计 2026 秋季上市，定价 379-499 美元为传闻。"},

 {"region":"国际","title":"联想 Yoga Slim 7x 全球上市：骁龙 X2 Elite + 14 英寸 1100nit OLED + 80 TOPS NPU",
  "category":"笔记本电脑","dim":"AI/NPU","status":"已上市","date":"2026-09-04","source_tier":"B",
  "source_name":"NotebookCheck","url":"https://www.notebookcheck.net/Lenovo-releases-new-14-inch-laptop-globally-with-Snapdragon-X2-Elite-and-1-100-nit-OLED-display.1264717.0.html",
  "corroboration":2,"stars":4,"vendor":"Lenovo Yoga Slim 7x (14Q8Y11)","signal_type":"全球上市",
  "key_params":"14 英寸 OLED 120Hz 1100nit、骁龙 X2 Elite (X2E-88-100)、32GB LPDDR5X、70Wh/24h+、80 TOPS NPU、1.17kg/13.9mm",
  "tech_features":["首批骁龙 X2 Elite 笔记本，Copilot+ PC","80 TOPS NPU，端侧 AI 算力跃升","1100nit 高亮 OLED 120Hz","1.17kg/13.9mm 轻薄 + 24h+ 标称续航"],
  "why_important":"Arm Windows AI 本的算力/续航/便携新标杆，NPU 80 TOPS 成为高端 AI PC 新基线。",
  "terminal_link":"TCL 笔电 AI 化与 Arm 平台选型的直接参照。",
  "note":"9 月全球静默上架，英国起价 1050 英镑；与去重表内 Yoga Tab 系列不同品类。"},

 {"region":"国际","title":"华硕印度发布 2026 款 Vivobook 五机型：全金属 + 三平台 Copilot+，标称 38 小时续航",
  "category":"笔记本电脑","dim":"结构/工艺","status":"已上市","date":"2026-09-16","source_tier":"B",
  "source_name":"91mobiles","url":"https://www.91mobiles.com/updates/asus-launches-new-vivobook-lineup-on-september-16",
  "corroboration":2,"stars":3,"vendor":"华硕 Vivobook 14 Flip/S14 Flip/S14/S16/Vivobook 16","signal_type":"新品发布",
  "key_params":"14/16 英寸、骁龙 X / 锐龙 AI 7 400 / 酷睿 Ultra 7 Series 3 三平台、全系 Copilot+ PC、最高 70Whr、全金属 + MIL-STD-810H、9 月 16 日印度上市",
  "tech_features":["同一代模具覆盖高通/AMD/英特尔三平台，全系达 Copilot+ PC 门槛","全金属机身 + MIL-STD-810H 军规耐用认证，替代上代塑料混材","标称最高 38 小时续航，70Whr 电池 49 分钟充至六成","Windows Hello 人脸识别 + 物理摄像头遮挡，部分机型可选 OLED"],
  "why_important":"轻薄本把三平台并行与军规全金属下放到学生价位，AI PC 竞争门槛从芯片算力转向整机做工与平台可选性。",
  "terminal_link":"TCL 笔记本入门/主流价位的平台选型、结构工艺与续航标称策略直接对标。",
  "note":"38 小时为实验室最佳值；完整售价发布会当日公布。"},

 {"region":"国际","title":"Twelve South 小号 Valet 充电托盘：Qi2.2 25W 磁吸 + 纳帕皮革家居化设计，129.99 美元",
  "category":"无线充","dim":"认证/合规","status":"已上市","date":"2026-07-28","source_tier":"B",
  "source_name":"9to5Mac","url":"https://9to5mac.com/2026/07/28/twelve-south-debuts-smaller-valet-tray-with-25w-magsafe-charging/",
  "corroboration":3,"stars":3,"vendor":"Twelve South Valet 4.25 英寸版","signal_type":"新品发布",
  "key_params":"4.25 英寸托盘、Qi2.2 最高 25W 无线充（上代 15W）、侧边 USB-C 对外 10W、纳帕皮革 + 锌合金底座、129.99 美元（含 45W 适配器）",
  "tech_features":["无线充功率 15W 提升至 Qi2.2 25W，兼容 iPhone 与 Qi2 安卓机型","充电位磁吸对位，支持磁吸壳直吸","侧边 USB-C 口对外供电 10W（手表/耳机补电）","四种摆放方向，金属外框可换色，附 1.5 米线"],
  "why_important":"桌面无线充从拼瓦数转向热管理与家居形态，25W 磁吸 + 家具化皮革说明配件向高溢价家居品类迁移。",
  "terminal_link":"TCL 生态配件在无线充外观工艺、磁吸对位与散热设计上的产品定义参考。",
  "note":"待印证：缺第三方功率/温升实测；无线充工作时有线口限流 10W 属明确降级。"},

 {"region":"国际","title":"亚马逊 Echo Dot Max 预热：AZ3 端侧 AI 芯片 + Omnisense 传感融合 + Alexa+，99.99 美元",
  "category":"智能音箱","dim":"AI/NPU","status":"即将上市","date":"2026-09-10","source_tier":"C",
  "source_name":"Craving Tech（CNET/亚马逊官方预热印证）","url":"https://www.cravingtech.com/the-smart-speaker-war-just-got-a-lot-more-interesting.html",
  "corroboration":2,"stars":3,"vendor":"Amazon Echo Dot Max (2026)","signal_type":"新品预热",
  "key_params":"AZ3 端侧 AI 芯片、Alexa+ 生成式语音助手、Omnisense 传感融合（音频/超声/WiFi 雷达）、360° 音频、99.99 美元、预计 10 月 29 日发售",
  "tech_features":["新 AZ3 端侧 AI 芯片，本地语音意图处理","Omnisense 传感融合：音频/超声波/WiFi 雷达感知人在何处","Alexa+ 订阅制生成式助手","与 Google Home Speaker 正面对垒的音箱大战新格局"],
  "why_important":"智能音箱进入端侧 AI 芯片 + 传感融合阶段，音箱从播放终端升级为家庭感知 AI 入口。",
  "terminal_link":"TCL 智能音箱 AI 化与家庭感知入口路线的对标价值。",
  "note":"9 月预热为采集点，预计 10 月 29 日发售；与去重表内 Echo Studio（AZ3 Pro）为不同 SKU。"},

 {"region":"国际","title":"TOZO NC9 Pro AI 耳机开售：1.47 英寸触屏充电仓 + LDAC + AI 翻译对话",
  "category":"AI耳机·耳穿戴","dim":"音频","status":"已上市","date":"2026-09-15","source_tier":"B",
  "source_name":"ACCESS Newswire（TOZO 官方稿）","url":"https://www.accessnewswire.com/newsroom/en/consumer-and-retail-products/tozo-officially-launches-nc9-pro-with-smart-touchscreen-and-hi-res-aud-1221135",
  "corroboration":2,"stars":4,"vendor":"TOZO NC9 Pro","signal_type":"新品发布",
  "key_params":"1.47 英寸触控屏充电仓、LDAC/Hi-Res、10mm SDLC 单元、蓝牙 6.0、IPX8、6 麦 ENC、AI 翻译/对话助手、9 月 15 日开售",
  "tech_features":["充电仓变控制中枢：1.47 英寸触屏直接操作耳机","TOZO AI 助手/翻译/聊天，EarTune 听感优化","LDAC + Hi-Res Audio，10mm SDLC 单元","蓝牙 6.0 + 6 麦 ENC + IPX8"],
  "why_important":"耳机充电盒屏幕化 + AI 助手落地，蓝牙 6.0 与 LDAC 向主流价位普及，AI 耳机交互形态新样本。",
  "terminal_link":"TCL 耳机智能化（充电仓交互、AI 助手、蓝牙 6.0）的产品定义参考。",
  "note":"主打 TheScreenThatListens；与去重表内 TOZO AIVU 眼镜为不同产品线。"},
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
print("cn dates:", [it['date'] for it in cn])
print("intl dates:", [it['date'] for it in intl])
