#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 WB_2026-09-03_硬件看板.html
做法：读取 gen_wb_2026-08-26.py 模板，先替换模板内 日期/周几/类别数(7→8)/排序兜底，
     再注入 CARDS/DIMS/TOP5，exec 生成。
     注意：先替换 src 再拼接 CHUNK，避免全局 replace 污染 CHUNK 内的卡片日期。
"""
import os

TEMPLATE = r"E:\AI相关\预研究\202608\03_输出\gen_wb_2026-08-26.py"

CHUNK = r'''CARDS = [
    # ========== 国内 15 条 ==========
    {
        "region": "cn", "status": "coming",
        "title": "小米平板 9 Pro Max（玄戒 O3 首发）",
        "stars": 4, "source": "C", "date": "2026-09-02", "domain": "平板",
        "url": "https://www.toutiao.com/article/7680604392919450151",
        "url_label": "今日头条",
        "signal_type": "官宣",
        "confirm_count": "3 个印证源",
        "key_params": "玄戒 O3（台积电 3nm、240 亿晶体管）10 核全大核 6 颗 4.35GHz，13.3 英寸 3K LCD 144Hz，12000mAh + 120W，约 650g，澎湃 OS 4",
        "tech_features": [
            "玄戒 O3 自研 3nm SoC，240 亿晶体管，10 核全大核（6 颗超大核 4.35GHz + 4 颗大核），GeekBench 6 多核 15221，安兔兔实验室跑分 5228014",
            "GPU 为 16 核 G2-Ultra NX，光追性能较上代 O1 提升 182%；全球首发 LPDDR6，带宽 113.8GB/s，片内 60MB 缓存",
            "13 至 13.3 英寸 3K LCD，144Hz，12bit 色深、P3 广色域，DC 调光 + 节律护眼；柔光版采用纳米 AG 纹理 + AR 镀膜类纸处理",
            "12000mAh 电池配 120W 有线，实测 28 至 60 分钟充满；前置 3200 万、后置 5000 万；出厂澎湃 OS 4，支持自由窗口多任务与超级小爱 2.0 跨应用编排"
        ],
        "why_important": "安卓平板第一次用上手机同代自研 3nm 旗舰 SoC：玄戒 O3 的 200TOPS 级 NPU 让端侧跑 MiMo 做会议纪要不再绕云端，平板从影音终端往生产力终端迁移有了算力底座。更值得注意是它刻意选 LCD 而非 OLED——大屏防烧屏、校色稳定、成本可控，代价是厚约 2mm、重 650g。这个「大屏要不要上 OLED」的取舍，正是 TCL 平板预研必须自己重做一遍的判断。",
        "terminal_relevance": "大屏平板：自研 SoC 端侧 AI 算力配置、LCD 与 OLED 的选型边界、万毫安电池配百瓦快充的堆叠与温升预算",
        "vendor": "小米（Xiaomi）", "model": "小米平板 9 Pro Max（M367FC）",
        "sources": "今日头条（数码科技猿）/ 小米玄戒芯片技术沟通会（2026-08-24）",
        "remark": "9 月 7 日小米秋季旗舰发布会正式亮相；安兔兔 5228014 为小米实验室芯片跑分而非平板整机分，最高 16GB+1TB 为媒体预估，最终尺寸（13 或 13.3 英寸）与售价待发布会确认"
    },
    {
        "region": "cn", "status": "released",
        "title": "作业帮 X70 Ultra 学习平板",
        "stars": 4, "source": "B", "date": "2026-08-17", "domain": "平板",
        "url": "https://www.sznews.com/news/content/mb/2026-08/17/content_32149921.htm",
        "url_label": "深圳新闻网",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "8 月 17 日发布，定位 5000 元档旗舰；同场 Z100 为 14.7 英寸 OXIDE 类纸护眼巨幕，首发价 9999 元",
        "tech_features": [
            "8 月 17 日「开启学习机新时代」发布会推出 Z100 与 X70 Ultra 两款旗舰，正式进军高端市场",
            "Z100 配备 14.7 英寸 OXIDE 超广角类纸护眼巨幕屏，3K 分辨率、11 层全视角漫反射、原生低蓝光，获五大机构 11 项护眼认证，搭载 AI 双屏三摄",
            "AI 超级老师具备双向交互能力，通过错因诊断、错因定位、错因清零三环节细化至每个填空；获中国信通院认证，学习效果提升超 42%，并较早通过 13 科模拟教师资格考试",
            "同步发布可移动式便携听学硬件「口袋 AI 老师」，把 AI 伴学从家庭大屏延伸到户外场景"
        ],
        "why_important": "学习平板是少数还在增长的平板细分，且它的溢价不在 SoC 而在「护眼屏 + AI 内容」：Z100 用 OXIDE 加 11 层漫反射加原生低蓝光堆出 11 项护眼认证，把 14.7 英寸巨幕卖到 9999 元。对 TCL 而言，这直接印证了「自有面板 + 整机」垂直整合的可行性——华星如果能把类纸护光的膜材与光学处理做成标准方案，就能在 BOM 上拿到别家拿不到的差异化定价权。",
        "terminal_relevance": "教育平板：大尺寸 OXIDE 类纸护眼屏方案、护眼认证体系、AI 伴学内容与硬件绑定的商业模式",
        "vendor": "作业帮", "model": "X70 Ultra / Z100",
        "sources": "深圳新闻网（2026-08-17 发布会现场报道）/ 洛图科技学习平板零售数据",
        "remark": "Z100 首发价 9999 元卡位万元价格带，X70 Ultra 位于 5000 元档为传统旗舰升级款；作业帮 2026 上半年学习机销量份额 30.7%（洛图科技）"
    },
    {
        "region": "cn", "status": "released",
        "title": "REDMI K Pad 2 16GB+256GB 新版",
        "stars": 3, "source": "C", "date": "2026-07-20", "domain": "平板",
        "url": "http://www.mnw.cn/news/digi/3110495.html",
        "url_label": "闽南网（快科技）",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "8.8 英寸 3K LCD 165Hz 1100nits，天玑 9500，15300mm² VC，9100mAh + 67W 双 USB-C，Bose 调音双 1620 扬声器，到手 4399 元",
        "tech_features": [
            "8.8 英寸 3K LCD，165Hz 刷新率，峰值亮度 1100nits，针对游戏场景做专属色彩优化",
            "天玑 9500 旗舰处理器，配 15300mm² 大面积 VC，采用芯片中置设计加边缘加厚石墨，握持区温度最高降 5.4℃、整机散热能力提升 10%",
            "9100mAh 电池配 67W 有线快充，双 USB-C 接口；支持主板直供电，可绕开电池为主板供电以减少边充边玩的发热与电池损耗",
            "双 1620 全频对称扬声器由 Bose 专业调音，配双 0815 X 轴线性马达"
        ],
        "why_important": "小平板赛道今年被重新激活，K Pad 2 是其中「性价比电竞」路线的代表。它的结构解法值得抄：芯片中置加边缘加厚石墨加 15300mm² VC，用被动散热把天玑 9500 压进 8.8 英寸机身，握持区还能降 5.4℃；主板直供电则是解决「边充边玩伤电池」的低成本方案。这两点对 TCL 小尺寸平板的散热与充电架构都是现成参考。",
        "terminal_relevance": "小尺寸平板：被动散热堆叠（VC 面积与芯片中置）、主板直供电绕过电池的充电架构、Bose 联名调音",
        "vendor": "小米 REDMI", "model": "K Pad 2（16GB+256GB，26048RP6AC）",
        "sources": "闽南网 / 快科技（2026-07-20）",
        "remark": "16+256GB 版首销到手 4399 元（建议零售价 4599 元），首销优惠持续至 2026 年 8 月 20 日；12+256GB 首销 3799 元、16+512GB 为 4799 元"
    },
    {
        "region": "cn", "status": "coming",
        "title": "iQOO Pad mini 电竞小平板",
        "stars": 2, "source": "E", "date": "2026-08-01", "domain": "平板",
        "url": "https://www.toutiao.com/a7669026935011492354",
        "url_label": "今日头条（爆料汇总）",
        "signal_type": "曝光",
        "confirm_count": "1 个印证源",
        "key_params": "8.3 英寸 3K LCD 165Hz，骁龙 8 Elite Gen6（2nm），8500mAh + 90W，支持 5G 插卡，预估 3299 元",
        "tech_features": [
            "8.3 英寸 3K LCD 护眼直屏，165Hz 刷新率，在同批小平板中坚持 LCD 路线",
            "搭载新一代骁龙 8 Elite Gen6 旗舰平台（2nm 制程）",
            "8500mAh 电池配 90W 快充，为同期 6 款小平板中充电功率最高",
            "极致窄边框、4D 游戏振感、独立触控优化，支持 5G 实体 SIM 卡"
        ],
        "why_important": "下半年 6 款 8.3 至 8.8 英寸小平板的参数已基本清晰：iQOO 用 90W 快充拿下充电第一，同时是极少数坚持 LCD 高刷的厂商。对预研的意义在于小平板市场正被重新切分——电竞（165Hz 加大 VC 加插卡）、生态（鸿蒙多屏协同）、双系统办公三条路线并存，TCL 若要切入必须先锁定其中一条，而不是做面面俱到的水桶机。",
        "terminal_relevance": "小尺寸平板：LCD 高刷与 OLED 的路线分歧、90W 级快充在小机身的温升与电池寿命权衡",
        "vendor": "iQOO（vivo 子品牌）", "model": "iQOO Pad mini",
        "sources": "今日头条自媒体爆料汇总（2026-08-01）",
        "remark": "本条为爆料，所有硬件信息未经官方确认，发布时间、售价与最终配置以 iQOO 官方发布为准；同批还有华为 MatePad Mini 2、荣耀 WIN Pad mini、iPad mini 8 等"
    },
    {
        "region": "cn", "status": "coming",
        "title": "华为 Mate 90 系列（麒麟 9050）",
        "stars": 3, "source": "B", "date": "2026-08-27", "domain": "手机",
        "url": "https://g.pconline.com.cn/x/2181/21811275.html",
        "url_label": "太平洋科技（PConline）",
        "signal_type": "官宣",
        "confirm_count": "2 个印证源",
        "key_params": "预计 9 月下旬发布，四款机型，搭载新一代麒麟 9050 系列，Pro Max 与 RS 非凡大师版用满血麒麟 9050 Pro，超大核 3.1GHz",
        "tech_features": [
            "预计 2026 年 9 月下旬发布，涵盖标准版、Pro、Pro Max 与 RS 非凡大师四款机型",
            "搭载基于「韬定律」的新一代麒麟芯片（麒麟 9050 系列），Pro Max 与 RS 非凡大师版为满血麒麟 9050 Pro，超大核主频 3.1GHz",
            "系统预装鸿蒙 7，后置模组延续星环设计语言",
            "同期 9 月还有华为 Mate XT 2 三折叠（9 月 7 日）与高通骁龙 8 Elite Gen6 发布（9 月 23 日）"
        ],
        "why_important": "「韬定律」是华为在先进制程受限下给出的性能提升路线：不靠制程迭代，而靠逻辑折叠架构、架构重构与封装工艺升级。如果麒麟 9050 系列真能在成熟 DUV 上做到对标新制程的能效，那意味着国产 SoC 的性能天花板比市场预期更高。这条路线一旦跑通，平板用国产中高端 SoC 的选型空间会被打开，值得在预研的 SoC 备选清单里长期跟踪。",
        "terminal_relevance": "手机与平板 SoC：非先进制程下的架构与封装提效路线、国产中高端 SoC 的可用性边界",
        "vendor": "华为（HUAWEI）", "model": "Mate 90 系列（标准版 / Pro / Pro Max / RS 非凡大师）",
        "sources": "太平洋科技 PConline 快讯（2026-08-27）",
        "remark": "发布时间与规格基于行业爆料与媒体预测，最终以华为官方发布为准"
    },
    {
        "region": "cn", "status": "coming",
        "title": "小米 18 Pro 系列（骁龙 8 Elite Gen6）",
        "stars": 3, "source": "C", "date": "2026-09-02", "domain": "手机",
        "url": "https://k.sina.com.cn/article_7879923188_1d5ae15f406801cow4.html",
        "url_label": "新浪新闻",
        "signal_type": "曝光",
        "confirm_count": "2 个印证源",
        "key_params": "预计 9 月 28 日发布，首发骁龙 8 Elite Gen6（2+3+3 三丛集，Pro 版超大核 5GHz），电池 7000 至 8500mAh",
        "tech_features": [
            "预计 2026 年 9 月 28 日压轴发布，与荣耀 Magic9 系列同期",
            "搭载高通骁龙 8 Elite Gen6，采用 2+3+3 三丛集设计，Pro 版超大核频率冲上 5GHz",
            "电池容量 7000 至 8500mAh，国产旗舰集体迈入 7000mAh 时代",
            "台积电 2nm 晶圆单片成本突破 3 万美元，骁龙 8 Elite Gen6 Pro 单价预计超 300 美元，下半年 2nm 安卓旗舰起步价可能逼近 6000 元档"
        ],
        "why_important": "这条的核心信号不是机型而是成本：2nm 晶圆单片成本破 3 万美元、旗舰 SoC 单价超 300 美元，直接把 2nm 安卓旗舰起步价推到 6000 元档。对平板预研来说，2027 年的旗舰平板如果要用上 2nm 平台，BOM 中 SoC 占比会显著抬升，必须在整机定价与配置组合上提前做压力测试。",
        "terminal_relevance": "SoC 成本模型：2nm 制程涨价对旗舰整机 BOM 与定价带的传导",
        "vendor": "小米（Xiaomi）", "model": "小米 18 Pro / Pro Max",
        "sources": "新浪新闻（2026-09-02 旗舰发布日历整理）",
        "remark": "本条为媒体预测汇总，发布时间与规格以小米官方为准；同月还有荣耀 Magic9（9 月 28 日）与 iQOO 16（9 月底）"
    },
    {
        "region": "cn", "status": "coming",
        "title": "华为 WATCH Ultimate 2 非凡探索 雪域白",
        "stars": 3, "source": "B", "date": "2026-09-02", "domain": "智能手表",
        "url": "https://www.163.com/tech/article/L5QKSDMK00099504.html",
        "url_label": "网易科技",
        "signal_type": "官宣",
        "confirm_count": "2 个印证源",
        "key_params": "9 月 7 日正式亮相，雪域白新配色配浅灰尼龙编织回环表带；迪桑特广告中疑似联名款同步曝光",
        "tech_features": [
            "华为官方 9 月 2 日宣布 WATCH Ultimate 2 非凡探索全新配色「雪域白」将于 9 月 7 日亮相",
            "雪域白以冰雪运动为设计灵感，表盘与表圈取雪山纯净色调，搭配浅灰色尼龙编织回环表带，兼顾极限雪山耐候性与城市通勤佩戴",
            "迪桑特官方广告中出现疑似联名款：深色基底配 V 形橙色细纹表带，或配套专属表盘与运动数据记录模块",
            "延续 Ultimate 系列硬底子：X-TAP 智感窗玄玑感知（一触微体检、血氧、高尿酸风险研究）、海豚声呐水下通信、北斗卫星语音消息、eSIM 独立通信、双续航模式"
        ],
        "why_important": "Ultimate 系列是华为把「高端腕表材质加专业户外安全能力」做成溢价的样板，本次雪域白与疑似迪桑特联名进一步把产品往运动品牌联名方向推。对可穿戴预研的启示：硬件规格之外，配色叙事与品牌联名是拉高客单价最有效的两条路径，而成本增量极小。",
        "terminal_relevance": "智能穿戴：高端材质与联名叙事的溢价路径、户外专业传感组合（血氧、高尿酸、水下通信）",
        "vendor": "华为（HUAWEI）", "model": "WATCH Ultimate 2 非凡探索 雪域白",
        "sources": "网易科技（2026-09-02，引华为官方预热海报与迪桑特广告大片）",
        "remark": "联名款尚未获华为官方确认；9 月 7 日 HarmonyOS 7 及全场景新品发布会同期还有 Mate XT 2 与 MatePad Air"
    },
    {
        "region": "cn", "status": "coming",
        "title": "Amazfit T-Rex Dual Solar 双太阳能户外表",
        "stars": 3, "source": "C", "date": "2026-08-19", "domain": "智能手表",
        "url": "https://gadgetsandwearables.com/upcoming-wearables-release-dates-rumors/",
        "url_label": "Gadgets & Wearables（认证追踪）",
        "signal_type": "曝光",
        "confirm_count": "2 个印证源",
        "key_params": "型号 A2570，马来西亚 SIRIM 认证命名为 T-REX DUAL SOLAR，另有印尼、韩国、欧亚经济联盟认证，预计 2026 年 9 月发布",
        "tech_features": [
            "型号 A2570 已出现在马来西亚、印度尼西亚、韩国与欧亚经济联盟（EAEU）监管数据库",
            "马来西亚 SIRIM 认证文件直接命名为「T-REX DUAL SOLAR」，确认双面太阳能命名",
            "Zepp Health App 代码中出现 case_back_input_power 字段，指向表壳背部的第二块太阳能采集面，与表盘面形成双面受光",
            "预计 2026 年 9 月（IFA 2026 窗口）发布，定价将是 Amazfit 的主要优势"
        ],
        "why_important": "Garmin 的 Power Glass 是光伏层做在显示面板内、只收表盘面；Amazfit 的 Dual Solar 从代码证据看是表盘加底壳双受光面，是技术上不同的解法。对户外穿戴预研来说，这是「不加大电池也能拉长续航」的第三条路径，值得评估其在实际佩戴（底壳贴肤、基本无光）下的增益是否成立——大概率是纸面参数强于真实收益，需要实测证伪。",
        "terminal_relevance": "可穿戴供电：双面太阳能采集的可行性与真实增益、户外手表续航的第三条技术路径",
        "vendor": "Amazfit / Zepp Health（华米）", "model": "T-Rex Dual Solar（A2570）",
        "sources": "Gadgets & Wearables 认证追踪（2026-08-19 更新）/ SIRIM、印尼、韩国 RRA、EAEU 监管库",
        "remark": "Zepp Health 尚未官方发布，发布日期为媒体推测；四国认证均在 2026 年 8 月初完成，硬件已过原型阶段"
    },
    {
        "region": "cn", "status": "coming",
        "title": "vivo Vision 探索版 MR 头显",
        "stars": 5, "source": "A", "date": "2026-08-22", "domain": "AR-VR眼镜",
        "url": "https://m.vivo.com.cn/vivo/vivovision",
        "url_label": "vivo 官网产品页",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "398g 整机，双目 8K Micro-OLED（3840×3552×2、2728 万像素、4032PPI、PPD38），第二代骁龙 XR2+，1.5° 眼动加 26DoF 手势，13ms 全彩透视",
        "tech_features": [
            "整机约 398g（含头显主体、S1 遮光罩、S1 泡棉、双环绑带），高 83mm、厚 40mm，中框为航空级铝合金",
            "双目 Micro-OLED，单眼 3840×3552，合计 2728 万像素、4032PPI、PPD 38；94% DCI-P3，逐台双目亮度一致性标定误差不大于 2nits、色差 ΔE 小于 2",
            "第二代骁龙 XR2+ 平台，GPU 频率提升 15%、CPU 频率提升最高 20%；蓝海续航系统采用硅负极加半固态电池技术",
            "交互为 1.5° 高精度眼动追踪（视线即光标）加 26 自由度手指级追踪（垂直交互范围 175°）；全彩透视 VST 延迟低至 13ms；磁吸镜片支持 100 至 1000 度近视",
            "支持 180° 沉浸穹幕视频（等效 120 英尺巨幕）、多视角观赛、PCVR 与手机 / PC 投屏；8 月 22 日起在北京、深圳等 10 余城 12 家体验店开放预约试用"
        ],
        "why_important": "这是目前参数最完整、且由官方页面确认的国产 MR 头显：398g 把双目 8K Micro-OLED 装进去，靠的是硅负极加半固态电池把电池体积压下来。对 TCL 有三点直接价值：一是 Micro-OLED 加 Pancake 的轻量化堆叠上限被推到 400g 以内；二是「逐台双目亮度与色差标定」这套产线校准流程，是显示模组良率与一致性的现成参照；三是 13ms 全彩透视与眼动加手势的双模交互，定义了当前 MR 的交互基线。",
        "terminal_relevance": "MR 与 AR：Micro-OLED 双目 8K 模组与 400g 级轻量堆叠、硅负极半固态电池、产线双目一致性标定、眼动加手势交互基线",
        "vendor": "vivo（维沃）", "model": "Vision 探索版（Explorer Edition）",
        "sources": "vivo 智能手机官方网站产品页 / FoneArena（2026-08-22 发布报道）",
        "remark": "官网当前显示「缺货」并提供预约演示试用，官方尚未公布售价与正式上市日期；OriginOS Vision 为 vivo 自研空间操作系统"
    },
    {
        "region": "cn", "status": "released",
        "title": "华硕灵耀 14 骁龙版 AI 轻薄本",
        "stars": 4, "source": "B", "date": "2026-09-02", "domain": "笔记本电脑",
        "url": "https://notebook.pconline.com.cn/2181/21814461.html",
        "url_label": "太平洋科技（PConline）",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "骁龙 X（4nm 8 核）加 45 TOPS NPU，14 英寸 2.8K 120Hz OLED（1100nits、ΔE 小于 1），21 小时本地视频续航，1.1kg / 13.9mm",
        "tech_features": [
            "骁龙 X 处理器，4nm 制程、8 核 CPU，集成 45 TOPS 算力 NPU，支持 Windows 11 AI+ PC 的本地实时字幕、增强搜索、单击以执行与回顾（预览版）",
            "14 英寸 2.8K 120Hz OLED 华硕好屏，100% DCI-P3，平均色准 ΔE 小于 1，HDR 峰值亮度 1100nits",
            "约 21 小时本地视频播放续航，支持 PD 快充，约 30 分钟充至 50%，手机充电器或充电宝可为设备补电",
            "整机约 1.1kg、厚约 13.9mm，A 面采用高科技陶瓷铝材质；接口含 1 个 USB-A、2 个 10Gbps USB-C、1 个 HDMI 2.1 TMDS 与 3.5mm 音频",
            "内置「小硕知道」AI 工具与「小硕 x WorkBuddy」联名工具，支持 AI 识图、AI 绘画与图文视频一键成片，部分功能可离线使用"
        ],
        "why_important": "45 TOPS 就能把 Copilot+ 的本地 AI 体验跑完整，说明当前端侧 AI 的算力门槛并不高——真正的分水岭在「哪些任务敢放本地」。更值得关注的是 1.1kg 机身做到 21 小时续航，这是骁龙 X 能效优势加系统级调校的结果，为「轻薄本续航红线」提供了新的对标值。",
        "terminal_relevance": "AI PC：45 TOPS NPU 的能力边界、Arm 平台长续航轻薄本的能效基准（1.1kg 与 21 小时）",
        "vendor": "华硕（ASUS）", "model": "灵耀 14 骁龙版",
        "sources": "太平洋科技 PConline（2026-09-02 全球发布报道）",
        "remark": "2026 年 9 月 2 日全球发布，全新「北极蓝」配色；与已在 08-23 覆盖的灵耀 14 双屏 2026 为不同机型"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为麒麟 XE90 / X90 Plus 鸿蒙 PC 双芯",
        "stars": 4, "source": "C", "date": "2026-08-07", "domain": "笔记本电脑",
        "url": "https://www.toutiao.com/article/7671210651359920663",
        "url_label": "今日头条（科技怪）",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "8 月 4 日鸿蒙电脑技术沟通会发布双芯：XE90（9 核 14 线程，能效提升 25%、NPU 提升 40%）、X90 Plus（10 核 20 线程，综合性能提升 25%）；9 月 OTA 推送「小艺任务」",
        "tech_features": [
            "麒麟 XE90 定位高能效：9 核 14 线程三集群（1 颗超大核加 4 颗中核加 4 颗低功耗核），最高 2.75GHz，官方称单核提升 23%、能效比提升 25%、NPU 算力提升 40%",
            "XE90 由 MateBook Pro S 首发：14 英寸全金属、798g、11.9mm，配陶瓷复合散热封装加基板微孔导热（芯片散热能力提升 70%），可稳定 20W 持续性能释放；65Wh 电池纯办公续航 11 小时",
            "麒麟 X90 Plus 定位高性能：延续 4+4+2 十核二十线程，扩容三级缓存，整机综合性能提升 25%，专属 MateBook Fold 非凡大师折叠本，针对折叠分屏做多核调度优化",
            "两颗芯片共用同源马良 935 系列 GPU，首次在鸿蒙 PC 全系标配硬件光线追踪，GPU 计算单元由 4 组增至 6 组、单组体积缩小 28%",
            "两芯均内置国密 SM3 / SM4 加密模块做硬件级硬盘加密；2026 年 9 月通过 OTA 推送「小艺任务」，可本地运行盘古端侧大模型完成会议整理、文稿改写与图表生成"
        ],
        "why_important": "三点值得记：一是「不靠制程靠架构」——XE90 用手机端麒麟 9030 Pro 的核心 IP 重做 PC 功耗调校，在成熟工艺上拿到能效提升 25%，这条路线对国产 SoC 选型影响深远；二是 NPU 提升 40% 明确指向端侧大模型，说明 PC 端 AI 已从云端转向本地，隐私场景是主战场；三是硬件光追首次下放到集成 GPU，虽离游戏生态成熟还远，但图形算力冗余会外溢到创作类应用。",
        "terminal_relevance": "PC 与平板 SoC：成熟工艺下的架构提效路线、NPU 支撑端侧大模型的算力门槛、集成 GPU 硬件光追、国密硬件加密",
        "vendor": "华为（HUAWEI）", "model": "麒麟 XE90 / 麒麟 X90 Plus",
        "sources": "今日头条（科技怪，2026-08-07）/ 华为 2026-08-04 鸿蒙电脑新品技术沟通会",
        "remark": "首发机型 MateBook Pro S 与 MateBook Fold 非凡大师于 2026 年 8 月开售（已在本报 08-24 与 08-31 覆盖，本条聚焦芯片本身）；部分性能对比数据引自厂商口径，第三方实测待补充"
    },
    {
        "region": "cn", "status": "released",
        "title": "MONITORMATE MS-Z Turbo 三合一 Qi2.2 无线充",
        "stars": 3, "source": "A", "date": "2026-08-28", "domain": "无线充",
        "url": "https://www.monitormate.com.tw/zh-hant/pages/ms-z-turbo",
        "url_label": "MONITORMATE 官网",
        "signal_type": "上市",
        "confirm_count": "1 个印证源",
        "key_params": "Qi2.2 25W（WPC 认证）加 Apple Watch MFW 认证双认证，三合一折叠，66×64×26.2mm / 165g，30 分钟为 iPhone 17 Pro Max 充至 50%",
        "tech_features": [
            "通过 WPC 认证的 Qi2.2 25W 快充模组，支持 iPhone 16 及以后全系 25W 无线超级快充，iPhone 12 至 15 兼容最高 15W 磁吸",
            "Apple Watch 充电模块通过 MFW 认证，三区输出分别为手机 25W Max、耳机区 5W Max、手表区 5W Max",
            "实测 iPhone 17 Pro Max 从 1% 到 50%：Qi2.2 用时 30 分钟，上代 Qi2 用时 43 分钟，快充速度提升约 67%",
            "折叠后尺寸 66×64×26.2mm、重 165g，铝合金加锌合金外壳，硅胶吸附底座；输入为 USB-C 15V/3A（需 45W 以上 PD 充电头）",
            "通过 BSMI（R3C250）与 NCC（CCAH26LP4770T7）认证，保固 18 个月"
        ],
        "why_important": "Qi2.2 从 15W 跳到 25W 后，30 分钟充至 50% 已经追平不少有线快充体验，无线充的「慢」这个刻板印象被打破。但对整机厂来说真正的门槛是温升：25W 持续无线充对手机背壳温度与电池寿命的压力显著高于 15W，需要在散热与充电策略上提前验证。此外 Apple Watch 的 MFW 认证是苹果生态的硬门槛，第三方做三合一必须先过这关。",
        "terminal_relevance": "无线充电：Qi2.2 25W 的温升与充电策略、MFW 生态认证门槛、多设备磁吸对位与结构堆叠",
        "vendor": "MONITORMATE", "model": "MS-Z Turbo（三合一 Qi2.2 折叠无线充电座）",
        "sources": "MONITORMATE 官网产品页",
        "remark": "早鸟优惠 2026/08/28 12:01 至 09/04 12:00；官网显示累计销量 276 件。品牌为台湾厂商，页面为繁体中文"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为 Sound Joy 2 便携智能音箱",
        "stars": 3, "source": "C", "date": "2026-08-27", "domain": "智能音箱",
        "url": "https://detail.zol.com.cn/speaker/huawei_sast_singbox/jiangsu/pic.html",
        "url_label": "中关村在线（ZOL 产品库）",
        "signal_type": "上市",
        "confirm_count": "1 个印证源",
        "key_params": "智能版 949 元 / 蓝牙版 799 元，50×75mm 跑道型全频喇叭（20W）加 19mm 高音（10W）加 2 无源辐射器，50Hz 至 20kHz，锂电供电",
        "tech_features": [
            "单元规格为 1 个 50mm×75mm 跑道型全频喇叭（20W）加 1 个 19mm 高音喇叭（10W）加 2 个无源辐射器",
            "频率响应 50Hz 至 20kHz，单声道智能音箱定位，支持智能家居控制",
            "调节方式为 APP、按键与语音，采用锂电池供电，具备便携属性",
            "智能版 ZOL 参考价 949 元（京东在售 898 元），蓝牙版 799 元（京东 698 元）；整机尺寸 202×73mm、重约 0.68kg"
        ],
        "why_important": "便携智能音箱这条线，华为用「跑道型全频加独立高音加双无源辐射器」的三件套在 0.68kg 机身里做到 50Hz 下潜，是小型腔体低频补偿的成熟方案。对平板的借鉴很直接：当前平板普遍采用对称多扬声器，但腔体更小、下潜更难，跑道型单元加无源辐射器的组合值得在下一代音频架构里做一轮可行性评估。",
        "terminal_relevance": "音频：小腔体低频补偿方案（跑道型单元加无源辐射器）、便携音箱的锂电续航与功率配比",
        "vendor": "华为（HUAWEI）", "model": "Sound Joy 2（智能版 / 蓝牙版）",
        "sources": "中关村在线 ZOL 产品库（2026-08-27 报价页）",
        "remark": "同页还列出华为 Sound Joy 一代（999 元）与 HUAWEI Sound X 鎏金剧院版（2499 元）；价格为渠道报价，随促销浮动"
    },
    {
        "region": "cn", "status": "released",
        "title": "韶音 OpenFit 2 AI 耳机",
        "stars": 4, "source": "B", "date": "2026-08", "domain": "AI耳机·耳穿戴",
        "url": "https://www.infoobs.com/article/20260901/71847.html",
        "url_label": "信息化观察网（电子发烧友网）",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "8 月发布，韶音首款 AI 耳机，接入阿里云千问大模型，支持耳机实体键、充电盒、APP 三端无感录音与多人发言人区分",
        "tech_features": [
            "韶音首款 AI 耳机，标志其产品战略从运动场景向录音转写、会议纪要、翻译等办公场景全面延伸",
            "硬件层面依托开放式声学与人体工学积累，支持耳机实体键、充电盒、APP 三端无感录音",
            "具备多人发言人区分与录音重点打点功能",
            "接入阿里云千问大模型并搭建完整测试调优体系；官方数据显示法律行业场景下英文识别率从 32% 提升至 92%",
            "与光帆科技共建专属 AI 实验室，补齐智能对话、日程待办等系统级 AI 能力"
        ],
        "why_important": "「法律行业英文识别率 32% 提升至 92%」是这组数据里最有价值的一条：它说明通用 ASR 在垂直场景的识别率远低于想象，行业词库加软硬件协同调优才是 AI 耳机的真正护城河，而不是模型本身。韶音作为开放式耳机龙头切入办公场景，也印证了 AI 耳机正从运动配件变成会议生产力工具，这个场景迁移对平板的会议录音与纪要功能形成直接替代压力。",
        "terminal_relevance": "AI 耳穿戴：垂直行业词库与软硬件协同调优的识别率增益、开放式声学在办公场景的形态迁移",
        "vendor": "韶音（Shokz）", "model": "OpenFit 2 AI",
        "sources": "信息化观察网 / 电子发烧友网（2026-09-01 行业分析）",
        "remark": "报道未给出具体售价与详细续航参数；官方强调在法律、金融等专业门槛较高的商务场景做了专项优化"
    },
    {
        "region": "cn", "status": "coming",
        "title": "Plaud One Explorer Edition AI 耳机",
        "stars": 4, "source": "B", "date": "2026-09-01", "domain": "AI耳机·耳穿戴",
        "url": "https://www.infoobs.com/article/20260901/71847.html",
        "url_label": "信息化观察网（电子发烧友网）",
        "signal_type": "官宣",
        "confirm_count": "2 个印证源",
        "key_params": "每只耳机 3 颗 MEMS 加 1 颗 VPU，充电盒 4 颗 MEMS，支持 6 小时通话录音 / 25 小时现场录音，充电盒内置 4G LTE 与 eSIM 可独立联网",
        "tech_features": [
            "Plaud 公布新产品线 Plaud One，并发布首款 AI 耳机 Plaud One Explorer Edition",
            "耳机与充电盒均配麦克风：每只耳机搭载 3 颗 MEMS 麦克风与 1 颗 VPU，充电盒搭载 4 颗 MEMS 麦克风",
            "可实现长达 6 小时通话录音与 25 小时现场录音",
            "充电盒内置 4G LTE 与 eSIM，可在无手机情况下独立联网",
            "双场景衔接：佩戴耳机时负责线上通话与会议录音，摘下耳机后充电盒无缝接管继续录制线下对话；录音内容导入 Plaud Intelligence 平台，ChatGPT 与 Claude 等外部 AI 工具可直接调用"
        ],
        "why_important": "Plaud 把「录音硬件到软件订阅」的商业模式从录音卡复制到耳机，是当前 AI 耳机里少数跑通盈利闭环的玩家。技术上更值得关注的是两件事：一是 VPU（语音处理单元）与多 MEMS 阵列的协同，把拾音质量做成硬件门槛；二是充电盒内置 4G LTE 加 eSIM 独立联网，让耳机脱离手机成为独立终端——这条「耳机即独立 AI 终端」的路线，与 TCL 关注的端侧 AI 终端范式高度一致。",
        "terminal_relevance": "AI 耳穿戴：VPU 加多 MEMS 阵列的拾音架构、eSIM 独立联网的耳机终端化路径、硬件加软件订阅的商业模式",
        "vendor": "Plaud", "model": "Plaud One / Plaud One Explorer Edition",
        "sources": "信息化观察网 / 电子发烧友网（2026-09-01 行业分析）",
        "remark": "Plaud Intelligence 平台已拥有百万级用户；具体售价与上市时间有待官方公布"
    },

    # ========== 国际 15 条 ==========
    {
        "region": "intl", "status": "released",
        "title": "Amazon Fire HD 10（2026）4GB RAM 焕新版",
        "stars": 2, "source": "D", "date": "2026-07-05", "domain": "平板",
        "url": "https://giznewsdaily.com/amazon-fire-hd-10-refresh-brings-upgrades-after-3-years/",
        "url_label": "GizNewsDaily",
        "signal_type": "上市",
        "confirm_count": "1 个印证源",
        "key_params": "10.1 英寸 1920×1200 IPS，RAM 由 3GB 升至 4GB（32GB 版），13 小时续航配 15W 有线，$154.99 起",
        "tech_features": [
            "10.1 英寸 1920×1200 IPS 触摸屏，60Hz 刷新率",
            "32GB 版内存由 3GB 提升至 4GB，为 Fire HD 系列三年来的主要配置升级",
            "搭载联发科八核处理器，13 小时续航，支持 15W 有线充电",
            "锁屏广告版售价 154.99 美元，支持 microSD 扩展最高 1TB"
        ],
        "why_important": "亚马逊最畅销的中端平板时隔三年才小幅提配，把 RAM 从 3GB 拉到 4GB 就算换代。它划出了海外入门平板的一条现实基线：只要生态内容够强，硬件可以停滞很久。对 TCL 的意义在于，面向海外入门市场的机型不必追求规格领先，把成本压在「够用的 RAM 加长续航加内容生态绑定」上反而更有效。",
        "terminal_relevance": "入门平板：海外百美元档的硬件配置基线（4GB RAM 与 13 小时续航）、内容生态绑定的低成本迭代策略",
        "vendor": "Amazon", "model": "Fire HD 10（2026 焕新版）",
        "sources": "GizNewsDaily（2026-07 报道）",
        "remark": "单一综合媒体源，技术亮点有限；SoC 型号在不同来源存在 MT7176A 与 MT8176A 两种说法，待官方参数页确认"
    },
    {
        "region": "intl", "status": "released",
        "title": "ASUS Pad T3201（12.2 英寸双层 OLED 平板）",
        "stars": 3, "source": "C", "date": "2026-08-12", "domain": "平板",
        "url": "https://www.fonearena.com/blog?p=488559",
        "url_label": "FoneArena",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "12.2 英寸 2.8K（2800×1840）双层串联 OLED 144Hz，峰值 2000nits，天玑 8300，9000mAh 配 45W，印度 45990 卢比起",
        "tech_features": [
            "12.2 英寸 2800×1840 分辨率、3:2 比例，双层串联（tandem）OLED，144Hz 刷新率",
            "峰值亮度 2000nits、典型 600nits，100% DCI-P3，通过 TÜV 护眼认证",
            "天玑 8300（4nm）平台，8GB LPDDR5X；9000mAh 电池配 45W 快充，约 30 分钟充至 50%",
            "Android 16，前置 13MP 加后置 5MP，支持 ASUS Pen 2.0 触控笔；6.5mm 玻璃纤维机身，印度 8 月 6 日 Flipkart 开售"
        ],
        "why_important": "华硕把双层串联 OLED 加 144Hz 下探到 5 万卢比以内的中高价档，说明 tandem OLED 的成本正在快速下降，不再是旗舰专属。对 TCL 平板预研是个明确信号：如果 12 英寸档要用 OLED，tandem 方案在亮度与寿命上的优势已经开始压过成本劣势，值得重新做一轮屏体选型评估。",
        "terminal_relevance": "平板显示：双层串联（tandem）OLED 的成本下探节奏、12 英寸档 OLED 与 LCD 的选型拐点",
        "vendor": "华硕（ASUS）", "model": "Pad T3201（无畏平板 12.2）",
        "sources": "FoneArena（印度发布报道）/ Digit、Gizmochina 转载",
        "remark": "印度首发，国际版后续有望跟进；国行对应华硕无畏平板 12.2 英寸，到手价约 3799 元"
    },
    {
        "region": "intl", "status": "released",
        "title": "Samsung Galaxy Tab S11（11 英寸）",
        "stars": 4, "source": "B", "date": "2026-09-01", "domain": "平板",
        "url": "https://www.currys.co.uk/products/samsung-galaxy-tab-s11-10.9-tablet-256-gb-grey-10289726.html",
        "url_label": "Currys 零售页",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "11 英寸 Dynamic AMOLED 2X 2560×1600 120Hz，天玑 9400+，12GB 加 256GB（microSD 至 2TB），8400mAh，四扬声器杜比全景声，IP68",
        "tech_features": [
            "11 英寸 Dynamic AMOLED 2X，2560×1600 分辨率，120Hz 刷新率",
            "天玑 9400+ 八核（最高 3.73GHz），12GB RAM 加 256GB 存储，支持 microSD 扩展至 2TB",
            "8400mAh 电池，四扬声器支持杜比全景声",
            "支持 S Pen，IP68 防尘防水，前置 12MP 与后置 13MP；支持 Galaxy AI、DeX 与 Android 16"
        ],
        "why_important": "标准版 Tab S11 用天玑 9400+ 而非骁龙，说明三星在旗舰平板上对联发科的接受度已完全放开。对供应链的意义是：安卓旗舰平板的 SoC 不再是高通独享，联发科旗舰平台在平板上的调度与散热适配成熟度已获一线厂商背书，这为中高端平板的 BOM 优化打开了新的议价空间。",
        "terminal_relevance": "平板 SoC：联发科天玑旗舰平台在安卓旗舰平板上的可用性背书、11 英寸档的屏幕与电池配置基线",
        "vendor": "三星（Samsung）", "model": "Galaxy Tab S11",
        "sources": "Currys 英国零售页加三星香港官网",
        "remark": "与 S11 Ultra 同代；注意与已在 08-24 覆盖的 Galaxy Tab S12+ 与 S12 Ultra 为不同代际"
    },
    {
        "region": "intl", "status": "released",
        "title": "Samsung Galaxy Tab S11 Ultra（14.6 英寸）",
        "stars": 5, "source": "A", "date": "2026-09-01", "domain": "平板",
        "url": "https://samsung.com/hk/tablets/galaxy-tab-s11/buy/",
        "url_label": "三星香港官网",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "14.6 英寸 Dynamic AMOLED 2X 2960×1848 120Hz，天玑 9400+，最高 16GB 加 1TB，11600mAh（视频播放最长 23 小时），S Pen，IP68",
        "tech_features": [
            "14.6 英寸 Dynamic AMOLED 2X，2960×1848 分辨率，120Hz 刷新率",
            "天玑 9400+ 平台，最高 16GB 内存加 1TB 存储",
            "11600mAh 大电池，官方标称视频播放最长 23 小时",
            "六角笔身 S Pen 适配，IP68 防尘防水；支持 Galaxy AI、DeX 与 Android 16",
            "香港官网已开售，起售价约 14788 港元"
        ],
        "why_important": "14.6 英寸加 11600mAh 加 23 小时视频播放，这是安卓平板当前的尺寸与续航天花板，也是 iPad Pro 的直接对手。对 TCL 的价值在于确认超大屏生产力的技术门槛：要在 14 英寸以上做出能替代笔记本的体验，屏幕面积、电池容量与整机重量三者必须同时达标，而三星给出的答案是 11600mAh 配 AMOLED——代价是机身重量与成本，这正是超大屏平板迟迟无法普及的根本原因。",
        "terminal_relevance": "超大屏平板：14.6 英寸 AMOLED 加 11600mAh 的堆叠与重量代价、超大屏生产力场景的体验门槛",
        "vendor": "三星（Samsung）", "model": "Galaxy Tab S11 Ultra",
        "sources": "三星香港官网购买页 / Currys、hkteducation",
        "remark": "与标准版 S11 同代，屏幕与电池规格更高；非 08-24 已覆盖的 S12 Ultra 与 S12+"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Apple iPhone 18 Air（A20 2nm）",
        "stars": 2, "source": "C", "date": "2026-09-10", "domain": "手机",
        "url": "https://speceagle.com/phones/apple-iphone-18-air",
        "url_label": "SpecEagle 参数页",
        "signal_type": "曝光",
        "confirm_count": "1 个印证源",
        "key_params": "6.65 英寸 LTPO OLED 2740×1260 ProMotion 1 至 120Hz，A20（2nm），12GB RAM，48MP 主摄加 24MP 前摄，3400mAh 硅碳电池，约 5.5mm / 155g，999 美元",
        "tech_features": [
            "6.65 英寸 LTPO OLED，2740×1260 分辨率，ProMotion 自适应 1 至 120Hz",
            "Apple A20 芯片（台积电 2nm），12GB RAM",
            "48MP Fusion 主摄加 24MP 前置摄像头",
            "3400mAh 硅碳负极电池，机身约 5.5mm、重约 155g；支持 15W MagSafe 无线充电",
            "预计售价 999 美元，随 9 月 iPhone 18 Pro 系列同场发布"
        ],
        "why_important": "如果 5.5mm 与 155g 属实，苹果是靠硅碳负极电池把超薄旗舰的续航拉回可用区间——这与国产旗舰普遍用硅碳换容量的思路一致，只是苹果把它用在减薄而非加续航上。这个取舍差异值得记：同样的电池技术，国产厂选择堆容量，苹果选择压厚度，两种产品定义背后是不同的目标人群判断。",
        "terminal_relevance": "手机与平板：硅碳负极电池的两种用法（堆容量与压厚度）、超薄机身的结构堆叠上限",
        "vendor": "苹果（Apple）", "model": "iPhone 18 Air",
        "sources": "SpecEagle 参数聚合页 / HT Tech、Mobileinto",
        "remark": "非官方信源，多家参数存在差异（屏幕尺寸、电池容量），以苹果官方发布为准"
    },
    {
        "region": "intl", "status": "released",
        "title": "Sharp AQUOS R11 徕卡三摄旗舰",
        "stars": 4, "source": "A", "date": "2026-08-20", "domain": "手机",
        "url": "https://aquosmobile.sharp.com.tw/news/view?news_category_id=*&news_id=36",
        "url_label": "Sharp 官网（台湾）",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "6.5 英寸 Pro IGZO OLED 240Hz、峰值 3600nits，骁龙 8s Gen4，徕卡三摄（50.3 加 50.3 加 38.5MP，2.9 倍光变），5100mAh 配超导热板，IP69 与 MIL-STD-810H",
        "tech_features": [
            "6.5 英寸 Pro IGZO OLED，240Hz 刷新率，峰值亮度 3600nits",
            "骁龙 8s Gen4 平台",
            "徕卡三摄：50.3MP 加 50.3MP 加 38.5MP，支持 2.9 倍光学变焦，配 14 通道光谱传感器",
            "5100mAh 电池配超导热板散热；IP69 与 MIL-STD-810H 军规防护，康宁 Victus 2 玻璃",
            "Android 16，AI 相机支持 Smart Fit Zoom 与 Privacy Safe，Vocalist 降噪；Wi-Fi 7 与蓝牙 6.0，面部加指纹双生物识别"
        ],
        "why_important": "3600nits 峰值亮度加 240Hz 的 Pro IGZO OLED 是夏普自研面板的实力展示，也把手机屏幕亮度天花板又往上推了一档。对 TCL 而言，华星在 LTPO 与高亮度 OLED 上的进度需要对齐这一水平；同时 IP69 加 MIL-STD-810H 的军规组合说明三防正从户外小众走向旗舰标配，平板若做行业定制机，防护等级是必须提前规划的硬指标。",
        "terminal_relevance": "显示：Pro IGZO OLED 的 3600nits 与 240Hz 能力基准；结构：IP69 加军规防护在旗舰机型上的普及节奏",
        "vendor": "夏普（Sharp）", "model": "AQUOS R11",
        "sources": "Sharp 台湾官网新闻（2026-07-09 上市）/ Notebookcheck、Cool3c",
        "remark": "日本与台湾市场 7 月上市；本条日期取国际版上市窗口，与 08-28 已覆盖的机型无重名"
    },
    {
        "region": "intl", "status": "released",
        "title": "Suunto Core 2 户外 ABC 手表",
        "stars": 4, "source": "A", "date": "2026-08-15", "domain": "智能手表",
        "url": "https://us.suunto.com/blogs/news/suunto-core-2-built-for-where-you-are-going",
        "url_label": "Suunto 官方博客",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "LED 点阵显示（亮度提升 40%、红绿双色背光），10ATM 加 MIL-STD-810H，CR3032 可换电池（典型 15 个月续航），ABC 传感器加风暴预警，179 美元",
        "tech_features": [
            "LED 点阵显示屏，亮度较上代提升 40%，支持红与绿双色背光",
            "10ATM 防水，通过 MIL-STD-810H 军规测试",
            "CR3032 可换纽扣电池，典型使用场景续航约 15 个月",
            "ABC 传感器（高度计、气压计、电子罗盘），支持风暴预警、月相与计步",
            "首次加入蓝牙，支持 App 配对与 OTA 升级；售价 179 美元，7 月起全球上市"
        ],
        "why_important": "在智能手表普遍一两天一充的背景下，Suunto 用一颗可换纽扣电池做出 15 个月续航，是「去智能化换可靠性」的极端样本。它验证了一个细分需求的真实存在：户外与专业用户对「不用充电」的重视远高于对智能功能的重视。对可穿戴预研的启示是，续航不是越大越好，而是要与目标场景的充电条件匹配——这个判断框架同样适用于行业定制平板。",
        "terminal_relevance": "可穿戴供电：可换电池加低功耗显示的超长续航方案、ABC 专业传感组合、军规与 10ATM 防护等级",
        "vendor": "Suunto（颂拓）", "model": "Core 2",
        "sources": "Suunto 美国官网博客 / Active.com、Hot3C",
        "remark": "无 GPS 模块，定位为离线 ABC 工具表；与已在 08-21 覆盖的 Suunto Race 3 与 Race 3 S 为不同产品线"
    },
    {
        "region": "intl", "status": "released",
        "title": "Garmin Instinct 3 Tactical Edition AMOLED",
        "stars": 3, "source": "C", "date": "2026-08-18", "domain": "智能手表",
        "url": "https://www.gpscentral.ca/product/garmin-instinct-3-amoled-tactical-50mm",
        "url_label": "GPS Central 零售页",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "1.3 英寸 AMOLED 416×416，10ATM 加 MIL-STD-810，多频 GPS 加 SatIQ，内置 LED 手电，智能表模式续航 24 天，449.99 美元",
        "tech_features": [
            "1.3 英寸 AMOLED 显示屏，416×416 分辨率",
            "10ATM 防水，通过 MIL-STD-810（耐热、抗震、防水）测试",
            "多频 GPS 搭配 SatIQ 卫星选择技术，内置 LED 手电",
            "战术功能：隐身模式、自毁、Jumpmaster 跳伞模式、弹道解算、双坐标显示",
            "心率、睡眠与 Pulse Ox 血氧监测，支持 Garmin Pay；智能表模式续航 24 天，售价 449.99 美元"
        ],
        "why_important": "Instinct 系列首次提供 AMOLED 战术版，是「专业户外工具表」向「显示体验」妥协的一个信号——此前该系列坚持 MIP 屏以保证阳光下可视与超长续航。24 天续航配 AMOLED 说明 Garmin 在电源管理上做了不小投入。对预研的参考价值：战术与行业市场的产品定义里，显示素质正从够用就好变成必须跟上，这会反向抬高 BOM。",
        "terminal_relevance": "可穿戴：AMOLED 在户外强光场景的电源管理方案、多频 GPS 加 SatIQ 的定位精度、战术行业功能的软硬结合",
        "vendor": "Garmin（佳明）", "model": "Instinct 3 Tactical Edition（AMOLED 50mm）",
        "sources": "GPS Central 零售页 / Garmin 官网、Amazon",
        "remark": "Garmin 于 2026-08-25 举办虚拟发布活动；与已在 08-24 与 08-28 覆盖的 Enduro 4、fēnix 9、Venu 4 为不同产品线"
    },
    {
        "region": "intl", "status": "released",
        "title": "Meta Glasses 自有品牌 AI 眼镜（日本上市）",
        "stars": 3, "source": "C", "date": "2026-08-25", "domain": "AR-VR眼镜",
        "url": "https://xants.net/en-GB/lifestyle/Meta-launches-new-Meta-Glasses-collection-in-Japan-with-26-styles/81868",
        "url_label": "xAnts 报道",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "与 EssilorLuxottica 合作的自有品牌，26 种镜框与镜片组合，Meta AI 日语本地化，超广角摄像头加开放式扬声器，单次 8 小时加充电盒共 40 小时，日本起价 50600 日元",
        "tech_features": [
            "Meta 与 EssilorLuxottica 合作推出自有品牌 AI 眼镜，提供 26 种镜框与镜片组合",
            "Meta AI 助手完成日语本地化，支持物体识别、翻译与日程管理",
            "超广角摄像头加开放式扬声器加多麦克风阵列",
            "单次充电续航 8 小时，配合充电盒共约 40 小时",
            "日本市场起售价 50600 日元，较此前联名款下降约 30%"
        ],
        "why_important": "Meta 从 Ray-Ban 与 Oakley 联名转向自有品牌加 26 款时尚组合，本质是把 AI 眼镜从科技产品重新定义为眼镜。价格下探约 30% 是关键动作——它说明 AI 眼镜的竞争焦点已从功能转向戴得住、买得起。对 TCL 的启示：AI 眼镜的胜负手不在光学参数，而在镜框供应链与配镜服务体系的整合能力。",
        "terminal_relevance": "AI 与 AR 眼镜：自有品牌加多 SKU 时尚化的产品策略、配镜服务体系对退货率的影响、价格下探节奏",
        "vendor": "Meta", "model": "Meta Glasses（日本自有品牌系列）",
        "sources": "xAnts 报道 / Mixi News、claypier",
        "remark": "Meta 于 2026-08-26 在日本正式发布；与已在 08-24 与 08-26 覆盖的 Ray-Ban 联名、Oakley 与 Samsung Galaxy Glasses 为不同产品线"
    },
    {
        "region": "intl", "status": "released",
        "title": "XREAL a01+ 随身巨幕 AR 眼镜",
        "stars": 4, "source": "B", "date": "2026-08-22", "domain": "AR-VR眼镜",
        "url": "https://prnewswire.com/news-releases/xreal-opens-us-sales-of-x-by-xreal-a01-bringing-big-screen-ar-glasses-to-more-people-for-299-302822423.html",
        "url_label": "PR Newswire 官方稿",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "双 Micro-OLED，峰值 1600nits 与 HDR10，50° 视场角、120Hz，等效 4 米 147 英寸；62g，无摄像头与无电池（取电于主机），299 美元",
        "tech_features": [
            "双 Micro-OLED 显示，峰值亮度 1600nits，支持 HDR10",
            "50° 视场角，120Hz 刷新率，等效 4 米处 147 英寸画面",
            "定制显示芯片加 ARView 引擎加空间稳定算法",
            "整机 62g，不内置摄像头与电池，由主机取电；可换前框设计",
            "通过 TÜV 5 星护眼认证，售价 299 美元，在 xreal.com、Amazon、Best Buy 等渠道开售"
        ],
        "why_important": "XREAL 用子品牌把巨幕 AR 眼镜打到 299 美元，做法很极端也很聪明：砍掉摄像头与电池，只做随身巨幕这一件事，62g 的重量因此成立。这是当前 AR 眼镜最现实的一条产品路径——不追求空间计算的全能，而是先把大屏观影这个单一需求做到 300 美元以下。对 TCL 的意义在于，显示模组加光学的成本下探已经有了明确的价格锚点。",
        "terminal_relevance": "AR 眼镜：减配（去摄像头与去电池）换轻量与低价的路径、Micro-OLED 加 Birdbath 的成本锚点（299 美元）",
        "vendor": "XREAL", "model": "X By XREAL a01+",
        "sources": "PR Newswire 官方新闻稿 / EyeJive、VR.org",
        "remark": "与已在 08-26 覆盖的 XREAL Aura 与 Project Aura（Android XR 方向）为不同产品线；本款为 USB-C 显示的观影向产品"
    },
    {
        "region": "intl", "status": "coming",
        "title": "14 英寸 MacBook Pro（M6 2nm）",
        "stars": 2, "source": "C", "date": "2026-09-02", "domain": "笔记本电脑",
        "url": "https://www.theapplepost.com/2026/09/02/71305/__trashed",
        "url_label": "The Apple Post",
        "signal_type": "爆料",
        "confirm_count": "1 个印证源",
        "key_params": "M6（2nm）加双 16 核 Neural Engine，12 核 CPU 加 12 核 GPU，保留现款 14 英寸设计，预计 10 月铺货，代号 J804",
        "tech_features": [
            "搭载苹果首款 2nm 芯片 M6",
            "双 16 核 Neural Engine，峰值算力较上代翻倍",
            "12 核 CPU 加 12 核 GPU，性能超越 M5",
            "保留现款 14 英寸设计，机身据称减薄约 1.2mm，加入 VC 均热板改善散热与续航",
            "预计 10 月铺货，内部代号 J804"
        ],
        "why_important": "苹果把 2nm 首发用在 Mac 而非 iPhone，且重点押注双 Neural Engine 的端侧 AI 算力，说明 PC 正在成为端侧大模型的落地主战场——因为 PC 的散热与供电预算远好于手机，能承载更高的持续算力。这条对平板的启示很直接：大尺寸平板如果要在端侧 AI 上做出差异化，散热与持续算力释放能力（而非峰值 TOPS）才是真正的瓶颈。",
        "terminal_relevance": "PC 与平板：2nm 平台的端侧 AI 算力配置、持续算力释放对散热设计的要求、VC 均热板在轻薄本与平板上的应用",
        "vendor": "苹果（Apple）", "model": "MacBook Pro 14 英寸（M6）",
        "sources": "The Apple Post 报道 / 9to5Mac、TLDevTech",
        "remark": "本条为爆料，规格与上市时间以苹果官方发布为准；与已在 08-26 覆盖的 Mac mini M6 与 M5 Pro 为不同机型"
    },
    {
        "region": "intl", "status": "released",
        "title": "Acer Swift Spin 14 AI 二合一笔电",
        "stars": 4, "source": "B", "date": "2026-08-19", "domain": "笔记本电脑",
        "url": "https://www.notebookcheck.net/Acer-releases-new-2-in-1-laptop-with-Snapdragon-X2-Elite-120Hz-touchscreen-and-23-hours-battery-life.1356225.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "骁龙 X2 Elite（X2E-78-100）12 核加 80 TOPS NPU，14 英寸 1920×1200 120Hz 触控，16GB LPDDR5X 加 512GB，65Wh 与 23 小时续航，1499.99 美元",
        "tech_features": [
            "骁龙 X2 Elite（X2E-78-100）12 核平台，NPU 算力 80 TOPS",
            "14 英寸 IPS 触控屏，1920×1200 分辨率，120Hz 刷新率",
            "16GB LPDDR5X 加 512GB 存储，65Wh 电池，官方标称续航 23 小时",
            "360° 翻转二合一形态，附 4096 级压感触控笔；通过 MIL-STD-810H 军规测试",
            "Wi-Fi 7 与蓝牙 6.0，双 USB4 加双 USB-A 加 HDMI 2.1；IR 人脸识别；美国 1499.99 美元，8 月 16 日发货"
        ],
        "why_important": "80 TOPS NPU 加 23 小时续航加 360° 翻转加压感笔，Acer 这套组合把 Arm 架构 AI 二合一的产品定义跑通了。对平板预研的参考价值在于形态边界的模糊化：这台机器在配置上已非常接近一台 14 英寸的带键盘平板，而它的续航（23 小时）远超当前任何平板。平板与轻薄本之间的体验差，正在被 Arm 加高能效 NPU 快速抹平。",
        "terminal_relevance": "AI PC 与平板：Arm 平台 80 TOPS NPU 的能效优势、二合一形态与压感笔生态、23 小时续航的功耗基准",
        "vendor": "宏碁（Acer）", "model": "Swift Spin 14 AI",
        "sources": "Notebookcheck（2026-08-16 发货报道）/ FoneArena、Acer 官网",
        "remark": "美国 8 月 16 日发货；与已在 08-19 与 08-20 覆盖的 Acer 非凡 Go Air、暗影骑士系列为不同产品线"
    },
    {
        "region": "intl", "status": "released",
        "title": "Cubenest Qi2.2 三合一磁吸无线充（SQ314）",
        "stars": 4, "source": "A", "date": "2026-08-10", "domain": "无线充",
        "url": "https://www.cubenest.eu/p-979/qi22-3in1-magsafe-charger-sq314-orange-25w",
        "url_label": "Cubenest 官网",
        "signal_type": "上市",
        "confirm_count": "1 个印证源",
        "key_params": "官方 Qi2.2 25W 认证，三设备同充（手机 25W 加手表快充加耳机），总功率最高 35W，0 至 50% 约 25 分钟，铝合金机身 239g",
        "tech_features": [
            "通过 Qi2.2 25W 官方认证，兼容 MagSafe",
            "三设备同时充电：手机 25W 加手表快充加耳机充电，整机总功率最高 35W",
            "官方标称 0 至 50% 充电约 25 分钟",
            "铝合金机身，整机 239g",
            "内置过热、过压与短路保护；需搭配 35W 以上适配器；8 月 31 日发货"
        ],
        "why_important": "Qi2.2 25W 已从 Anker、Belkin 等头部品牌扩散到 Cubenest 这类欧洲中小厂商，说明 WPC 的 Qi2.2 认证生态已经成熟，25W 磁吸正在成为事实标准。对整机厂的含义是：下一代平板的无线充电若想做差异化，不能只停留在支持 Qi2.2，而要在多设备协同充电、磁吸对位精度与温升控制上做文章。",
        "terminal_relevance": "无线充电：Qi2.2 25W 生态的成熟度、多设备磁吸充电的功率分配与温升控制",
        "vendor": "Cubenest", "model": "Qi2.2 三合一磁吸无线充电器（SQ314）",
        "sources": "Cubenest 官网产品页 / TechBloat",
        "remark": "8 月 31 日发货；与已在 08-31 覆盖的绿联、倍思、小米等 Qi2.2 产品为不同品牌"
    },
    {
        "region": "intl", "status": "released",
        "title": "LG xboom Power 系列派对音箱",
        "stars": 4, "source": "A", "date": "2026-08-16", "domain": "智能音箱",
        "url": "https://www.lg.com/global/newsroom/news/media-entertainment-solution/lg-electronics-launches-xboom-power-series-a-powerful-party-speaker-lineup-built-to-turn-gatherings-into-parties/",
        "url_label": "LG Newsroom 官方稿",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "Power 9000 / 7000 / 5000 三档，RMS 功率 440W / 340W / 260W，AI Karaoke Master（AI 消人声与变调），Auracast 多音箱串联，8 月 17 日起多市场上市",
        "tech_features": [
            "Power 9000、7000、5000 三档，额定 RMS 功率分别为 440W、340W 与 260W",
            "AI Karaoke Master：AI 实时消除人声、变调与一键 K 歌",
            "xboom Signature Sound 由格莱美制作人 will.i.am 参与调音",
            "AI Sound 加 Space Calibration Pro 空间校准，支持 Auracast 广播音频多音箱串联",
            "多彩 AI 灯效加 DJ 特效，双麦克风输入；8 月 17 日起在多市场上市"
        ],
        "why_important": "Auracast 广播音频在派对音箱上落地是个重要节点——它意味着 LE Audio 的广播能力已进入消费级出货阶段。对平板而言，Auracast 的潜在价值是一台平板同时向多个耳机与音箱广播音频，这在教育、会议场景有明确应用；同时 Space Calibration Pro 的自动空间声学校准，也是多扬声器系统值得借鉴的 DSP 思路。",
        "terminal_relevance": "音频：Auracast 广播音频的生态成熟度、AI 人声分离与实时变调、多扬声器空间声学自动校准",
        "vendor": "LG 电子", "model": "xboom Power 系列（9000 / 7000 / 5000）",
        "sources": "LG 全球 Newsroom 官方新闻稿 / Notebookcheck、The Mobile Indian",
        "remark": "与已在 08-19 覆盖的 LG xboom Mini 为不同产品线；本系列主打大功率派对场景"
    },
    {
        "region": "intl", "status": "released",
        "title": "Samsung Galaxy Buds4 AI 耳机",
        "stars": 4, "source": "A", "date": "2026-08-28", "domain": "AI耳机·耳穿戴",
        "url": "https://www.samsung.com/hk/audio-sound/galaxy-buds/galaxy-buds4-white-sm-r540nzwatgy",
        "url_label": "三星香港官网",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "Galaxy AI 自适应 ANC 加情境音效，24-bit Hi-Fi 编解码，实时翻译（Live Translate），蓝牙 6.1，IP54，与 Galaxy S26 系列协同",
        "tech_features": [
            "Galaxy AI 驱动的自适应主动降噪与情境音效",
            "支持 24-bit Hi-Fi 音频编解码",
            "实时翻译（Live Translate）功能",
            "蓝牙 6.1 连接，IP54 防尘防水；捏合与滑动触控操作，支持无线充电盒",
            "金属质感设计，提供珍珠白与星夜黑配色，与 Galaxy S26 系列协同"
        ],
        "why_important": "三星把 Galaxy AI 的自适应降噪与实时翻译直接内置到 Buds4，并与 Galaxy 生态深度绑定，这是大厂 AI 耳机的标准打法：硬件做入口，AI 能力由生态提供。对 TCL 的启示是，AI 耳机的竞争最后是端侧算力加生态服务的组合，单纯做硬件规格很难形成壁垒；反过来，平板作为生态中心之一，是否要承担耳机的算力卸载与账号体系，需要在产品规划阶段就定下来。",
        "terminal_relevance": "AI 耳穿戴：自适应 ANC 与实时翻译的端侧实现、蓝牙 6.1 与 24-bit 音频、耳机与手机及平板生态的协同范式",
        "vendor": "三星（Samsung）", "model": "Galaxy Buds4（SM-R540）",
        "sources": "三星香港官网产品页 / DailyAdvent、Swala Nyeti",
        "remark": "与已在 09-01 覆盖的 Apple AirPods 5、08-31 的 POVA AI Buds Pro 与 1MORE AiClip S52 为不同产品；Buds4 Pro 同期另有更高配版本"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 13, True),
    ("显示/OLED", 12, True),
    ("折叠屏", 1, True),
    ("手写笔/触控", 3, True),
    ("散热/液冷", 2, True),
    ("电池/续航", 12, True),
    ("快充/无线充", 8, True),
    ("影像", 5, True),
    ("AI/NPU", 10, True),
    ("音频/扬声器", 7, True),
    ("5G/通信", 4, True),
    ("Wi-Fi/连接", 5, True),
    ("AR/VR显示", 3, True),
    ("材质/工艺", 5, True),
    ("可持续/模块化", 2, True),
    ("手柄/外设", 2, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {"rank": 1, "title": "vivo Vision 探索版 MR 头显", "dim": "AR/VR显示", "stars": 5, "key": "A级 / 398g / 双目 8K Micro-OLED 4032PPI / 13ms 全彩透视"},
    {"rank": 2, "title": "Samsung Galaxy Tab S11 Ultra", "dim": "平板电脑", "stars": 5, "key": "A级 / 14.6\" AMOLED 2X / 11600mAh / 23 小时视频"},
    {"rank": 3, "title": "Samsung Galaxy Buds4", "dim": "AI耳机", "stars": 4, "key": "A级 / Galaxy AI 自适应 ANC / 实时翻译 / 蓝牙 6.1"},
    {"rank": 4, "title": "Sharp AQUOS R11", "dim": "手机", "stars": 4, "key": "A级 / 6.5\" Pro IGZO OLED 240Hz / 峰值 3600nits / IP69"},
    {"rank": 5, "title": "LG xboom Power 系列", "dim": "智能音箱", "stars": 4, "key": "A级 / 440W RMS / AI Karaoke Master / Auracast 串联"},
]
'''

src = open(TEMPLATE, encoding="utf-8").read()

# ① 只替换模板部分（此时尚未拼接 CHUNK），避免污染 CHUNK 内的卡片日期
src = src.replace("2026-08-26", "2026-09-03")
src = src.replace('WEEK = "周三"', 'WEEK = "周四"')
src = src.replace("采集口径：7类智能终端", "采集口径：8类智能终端")
# 规则9：看板标题统一为「智能终端硬件情报日报」（与入口页同名）
src = src.replace("智能终端硬件情报看板", "智能终端硬件情报日报")
src = src.replace('<div class="stat-num">7</div>', '<div class="stat-num">8</div>')

# ② 排序键兜底：部分卡片日期只到月（如 "2026-08"），取"日"切片为空会 int('') 报错
src = src.replace(
    '-int(c["date"][:4]), -int(c["date"][5:7]), -int(c["date"][8:10])',
    '-int(c["date"][:4]), -int(c["date"][5:7]), -int(c["date"][8:10] or "1")'
)

# ③ 再注入 CARDS/DIMS/TOP5
start = src.index("CARDS = [")
end = src.index("# ── 排序：状态优先")
new_src = src[:start] + CHUNK + "\n" + src[end:]

exec(new_src)
print("DONE")
