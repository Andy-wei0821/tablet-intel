#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 WB_2026-08-20_硬件看板.html"""
import datetime

DATE = "2026-08-20"
TITLE = f"智能终端硬件情报日报 · {DATE}"

# ── 14 条 FRESH 候选（国内 7 + 国际 7）──
CARDS = [
    # ── 即将上市 ──
    {
        "id": 1, "region": "cn", "status": "coming",
        "title": "Acer 暗影骑士·龙8Pro",
        "stars": 4, "source": "B",
        "date": "2026-08-17 上架 / 08-25 开售",
        "domain": "笔记本电脑",
        "url": "https://news.qq.com/rain/a/20260817A06L9C00",
        "url_label": "腾讯新闻/快科技",
        "signal_type": "产品发布",
        "confirm_count": "3+",
        "key_params": "AMD 锐龙9 9955HX3D / RTX 5070 Ti / 16\" 2560×1600 240Hz / 215W / 92Wh / 22999元",
        "tech_features": ["9955HX3D 携带 3D V-Cache 堆叠缓存，游戏 L3 缓存翻倍", "RTX 5070 Ti 175W 满血版（总功耗 215W）", "16\" 2560×1600 240Hz 高刷高分辨率兼顾", "92Wh 电池容量逼近航空上限"],
        "why_important": "AMD 3D V-Cache 技术首次下放至移动旗舰 HX3D 系列，对游戏帧率提升显著；RTX 5070 Ti 满血版在 16\" 机身内实现 215W 总功耗释放。",
        "terminal_relevance": "高性能笔记本散热与功耗方案可为平板旗舰散热设计提供参考；240Hz 面板供应链趋于成熟。",
        "vendor": "Acer（宏碁）",
        "model": "暗影骑士·龙8Pro",
        "sources": "腾讯新闻/快科技、中关村在线、ifeng",
        "remark": "8/25 正式开售，首发 9955HX3D+RTX5070Ti 组合"
    },
    {
        "id": 2, "region": "intl", "status": "coming",
        "title": "DPVR P1 Max 企业级 VR 头显",
        "stars": 4, "source": "B",
        "date": "2026-08-12 公布 / 11月样机",
        "domain": "AR-VR眼镜",
        "url": "https://www.vrarworld.cn/xinwenrili/13631.html",
        "url_label": "VRAR星球",
        "signal_type": "产品发布",
        "confirm_count": "4+",
        "key_params": "$549/$799 / 骁龙XR2 / 3664×1920 / 8K解码 / 6GB+128GB / 4000mAh / Wi-Fi 6",
        "tech_features": ["主动式双通风口散热，效率较前代+50%", "可选顶部DC电源输入，支持外接稳定供电持续运行", "Type-C 扩展接口，眼动追踪模块后续配件", "OEM 全栈定制：硬件规格/工业设计/品牌/固件/软件均可定制", "3DOF 独立定位（非6DoF）"],
        "why_important": "微软 HoloLens 停产、Meta 停售企业级 Quest SKU 后，专业 VR 厂商承接企业级 XR 部署缺口；主动散热+外接供电方案针对长时间高负载场景。",
        "terminal_relevance": "双通风口主动散热方案可为平板/眼镜类设备高负载散热设计提供参考；OEM 定制模式对行业终端定制化有借鉴意义。",
        "vendor": "DPVR",
        "model": "P1 Max",
        "sources": "VRAR星球、Auganix、VR.org、OFweek VR网",
        "remark": "11月起接受企业样机订单，定位 B 端部署而非消费级"
    },
    {
        "id": 3, "region": "intl", "status": "coming",
        "title": "Garmin Venu X1 旗舰运动手表",
        "stars": 4, "source": "B",
        "date": "2026-08-06 发布 / 秋季上市",
        "domain": "智能手表",
        "url": "https://mensreporter.com/garmin-unveils-new-venu-x1-smartwatch-expanding-premium-fitness-wearable-lineup",
        "url_label": "Men's Reporter",
        "signal_type": "产品发布",
        "confirm_count": "3+",
        "key_params": "$699.99 / 2\" AMOLED 448×486 / 蓝宝石+钛后壳 / 8天续航 / 7.9mm / 40g / 2000nit",
        "tech_features": ["Elevate Gen5 光学心率传感器（第五代）", "蓝宝石玻璃+钛合金后壳，顶级耐用材质组合", "7.9mm 超薄机身+40g 轻量化", "2000nit 峰值亮度，户外可视性领先"],
        "why_important": "Garmin 在 Apple Watch Ultra 2 和 Galaxy Watch Ultra 之外开辟高端运动手表赛道；蓝宝石+钛合金+2000nit 组合在手表领域属顶级配置。",
        "terminal_relevance": "蓝宝石+钛合金结构方案对高端终端外壳工艺有参考价值；Elevate Gen5 传感器方案可关注健康监测精度提升。",
        "vendor": "Garmin",
        "model": "Venu X1",
        "sources": "Men's Reporter、WearableXP、Garmin 官方",
        "remark": "秋季正式上市，定位高端运动健康市场"
    },
    {
        "id": 4, "region": "cn", "status": "coming",
        "title": "Huawei Pura 90s Pro Max",
        "stars": 4, "source": "C",
        "date": "2026-08-01 信息曝光",
        "domain": "手机",
        "url": "https://phonedady.com/huawei-Pura-90s-Pro-Max",
        "url_label": "PhoneDady",
        "signal_type": "规格曝光",
        "confirm_count": "2+",
        "key_params": "$1323 / 6.9\" / 麒麟9030S / 5500-6000mAh / 100W / 2亿像素长焦",
        "tech_features": ["麒麟 9030S 新一代旗舰 SoC", "5500-6000mAh 超大电池+100W 快充", "2亿像素潜望长焦", "6.9\" 大屏旗舰形态"],
        "why_important": "麒麟 9030S 芯片迭代进展值得关注；6000mAh 级电池在旗舰手机中属超大容量，硅负极渗透趋势加速。",
        "terminal_relevance": "麒麟 SoC 性能进展可对标平板旗舰芯片选型；大电池+百瓦快充方案对平板续航设计有直接参考。",
        "vendor": "Huawei（华为）",
        "model": "Pura 90s Pro Max",
        "sources": "PhoneDady、多渠道爆料",
        "remark": "尚未正式发布，规格基于多源爆料汇总，待官方确认"
    },
    # ── 进行中 ──
    {
        "id": 5, "region": "intl", "status": "progress",
        "title": "Moto Snap Qi2 磁吸充电器",
        "stars": 3, "source": "D",
        "date": "2026-08-19 泄漏",
        "domain": "无线充",
        "url": "https://www.notebookcheck.net/Motorola-s-magnet-offensive-Leak-reveals-Moto-Snap-for-Motorola-Edge-70-Max.1372559.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "产品泄漏",
        "confirm_count": "1",
        "key_params": "25W+ / Qi2 磁吸 / 配套 Edge 70 Max MPP",
        "tech_features": ["Motorola 首款磁吸 Qi2 充电器", "Evan Blass 爆料，可信度较高", "配套 Edge 70 Max 使用 MPP（磁吸定位）协议"],
        "why_important": "Qi2 磁吸充电在 Android 阵营加速渗透；Motorola 跟进意味着 Qi2 生态正从 Apple 独占走向通用化。",
        "terminal_relevance": "Qi2 磁吸方案对平板/手机无线充电模组设计有直接参考；MPP 协议标准化值得关注。",
        "vendor": "Motorola",
        "model": "Moto Snap Qi2",
        "sources": "Notebookcheck（Evan Blass 爆料）",
        "remark": "爆料阶段，25W+ 功率为推测值"
    },
    {
        "id": 6, "region": "intl", "status": "progress",
        "title": "OpenAI 甜甜圈 AI 音箱",
        "stars": 5, "source": "D",
        "date": "2026-08-06 爆料",
        "domain": "智能音箱",
        "url": "https://me.mashable.com/tech/74779/openais-smart-speaker-leaked-uae-pricing-design-and-specifications",
        "url_label": "Mashable",
        "signal_type": "产品泄漏",
        "confirm_count": "3+",
        "key_params": "$300-400 / Jony Ive 设计 / 无屏 / 摄像头+机械活动件 / GPT-Live / 2026亮相·2027上市",
        "tech_features": ["Jony Ive / LoveFrom 操刀工业设计", "冰球大小、无屏幕形态", "内置摄像头+机械活动部件（非静态设备）", "搭载 GPT-Live 实时对话 AI", "苹果商业秘密诉讼风险背景"],
        "why_important": "OpenAI 首款硬件产品，Jony Ive 设计，标志着 AI 公司跨界硬件的里程碑；摄像头+机械活动件组合在音箱品类中前所未有。",
        "terminal_relevance": "GPT-Live 端侧实时 AI 交互方案对智能终端 AI 助手体验有前瞻指引；机械活动件设计思路可启发终端形态创新。",
        "vendor": "OpenAI",
        "model": "甜甜圈 AI 音箱（暂称）",
        "sources": "Mashable、The Information、多渠道爆料",
        "remark": "2026 年内亮相、2027 年上市，仍处于早期阶段"
    },
    # ── 已上市 ──
    {
        "id": 7, "region": "cn", "status": "released",
        "title": "iQOO Neo11 至尊版",
        "stars": 4, "source": "A",
        "date": "2026-08-18 发布并开售",
        "domain": "手机",
        "url": "https://www.toutiao.com/article/7675364954656866854/",
        "url_label": "今日头条/羊城晚报",
        "signal_type": "产品发布",
        "confirm_count": "5+",
        "key_params": "天玑9500M 3nm / 9100mAh / 100W / 6.83\" 2K 144Hz / 3399元起（国补后2899元）",
        "tech_features": ["行业首发天玑9500M（台积电3nm N3P，全大核CPU，4.21GHz，11核GPU）", "9100mAh 蓝海大电池（第四代硅负极+第二代半固态电池技术）", "8K冰穹3D VC均热板，散热性能+5%", "自研Q2电竞芯片：2K+144FPS超分超帧并发", "寰宇电竞Wi-Fi三芯片，220米连接距离", "维信诺F2发光材料，514PPI，2000nit峰值，≤5%蓝光", "IP68/IP69防尘防水+3D超声波指纹+KPL赛事用机认证"],
        "why_important": "9100mAh 硅负极电池在手机品类中创纪录；天玑9500M 3nm 首发性能对标旗舰；2K+144FPS超分超帧并发技术方案领先。",
        "terminal_relevance": "硅负极+半固态电池技术方案对平板大电池设计有直接参考价值；3D VC均热板散热方案可迁移至平板；Wi-Fi三芯片方案对终端网络体验有启示。",
        "vendor": "iQOO（vivo 旗下）",
        "model": "Neo11 至尊版",
        "sources": "今日头条/羊城晚报、PChome、腾讯新闻、百度百科、新浪网",
        "remark": "8/18 首销，国补后 2899 元起，定位 3K 档 2K 屏性能旗舰"
    },
    {
        "id": 8, "region": "cn", "status": "released",
        "title": "Acer 暗影骑士·擎8",
        "stars": 3, "source": "B",
        "date": "2026-08-17",
        "domain": "笔记本电脑",
        "url": "https://news.pconline.com.cn/2180/21804724.html",
        "url_label": "太平洋科技",
        "signal_type": "产品发布",
        "confirm_count": "2+",
        "key_params": "i7-14650HX / RTX 5060 / 16.1\" 2.5K 180Hz / 10999元起 / 双风扇五热管",
        "tech_features": ["Intel i7-14650HX（16核24线程）+ RTX 5060", "16.1\" 2560×1600 180Hz 高刷屏", "双风扇五热管散热架构", "10999 元起售价"],
        "why_important": "RTX 5060 游戏本进入万元档，50 系显卡下沉至主流价位段。",
        "terminal_relevance": "双风扇五热管散热方案对平板高性能散热设计有参考；RTX 5060 功耗与散热数据可对标。",
        "vendor": "Acer（宏碁）",
        "model": "暗影骑士·擎8",
        "sources": "太平洋科技、PConline",
        "remark": "8/17 上架，万元档 RTX 5060 游戏本"
    },
    {
        "id": 9, "region": "cn", "status": "released",
        "title": "Acer 非凡Go Air（Wildcat Lake 版）",
        "stars": 4, "source": "B",
        "date": "2026-08-17",
        "domain": "笔记本电脑",
        "url": "https://diy.zol.com.cn/1234/12342762.html",
        "url_label": "中关村在线",
        "signal_type": "产品发布",
        "confirm_count": "3+",
        "key_params": "酷睿5 320 / Intel 18A / 6核 / NPU 16TOPS / 12.99mm / 1.19kg / 70Wh / 5099元起",
        "tech_features": ["Intel 18A 工艺（Cougar Cove P核 2P + Darkmont E核 4E = 6核）", "NPU 5 16TOPS AI 算力", "12.99mm 超薄机身 / 1.19kg 轻量化", "70Wh 大电池+双雷电4 接口", "120Hz 刷新率"],
        "why_important": "Intel 18A 工艺首次在消费级笔记本中落地；NPU 16TOPS 标志 AI PC 算力门槛持续下放。",
        "terminal_relevance": "Intel 18A 工艺良率与功耗表现对平板 SoC 选型有参考；NPU 16TOPS 方案可对标平板端侧 AI 算力配置。",
        "vendor": "Acer（宏碁）",
        "model": "非凡Go Air",
        "sources": "中关村在线、腾讯新闻、网易/快科技",
        "remark": "Intel 18A 工艺首发消费级产品，轻薄本形态"
    },
    {
        "id": 10, "region": "intl", "status": "released",
        "title": "NUU X10 5G",
        "stars": 2, "source": "C",
        "date": "2026-08-16/17 上市",
        "domain": "手机",
        "url": "https://phonedady.com/nuu-mobile-X10-5G",
        "url_label": "PhoneDady",
        "signal_type": "产品发布",
        "confirm_count": "2+",
        "key_params": "$219.99 / 6.8\" HD+ 90Hz / Dimensity 6100+ / 4+128GB / 5000mAh / 50MP三摄",
        "tech_features": ["Dimensity 6100+ 入门 5G SoC", "完全解锁美国运营商（全频段兼容）", "50MP 三摄系统", "5000mAh 电池"],
        "why_important": "$219.99 价位段 5G 手机持续下探；全频段兼容方案对入门终端射频设计有参考。",
        "terminal_relevance": "入门级 5G SoC 方案对平板 5G 版本选型有参考价值；全频段射频方案可关注。",
        "vendor": "NUU Mobile",
        "model": "X10 5G",
        "sources": "PhoneDady、CIVL",
        "remark": "主打美国市场入门 5G，全频段兼容"
    },
    {
        "id": 11, "region": "intl", "status": "released",
        "title": "Alldocube iPlay 80 mini Turbo",
        "stars": 4, "source": "B",
        "date": "2026-08-16",
        "domain": "平板",
        "url": "https://www.notebookcheck.net/Affordable-Alldocube-tablet-launches-with-120Hz-display-thin-design-and-SD-card-support.1369407.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "产品发布",
        "confirm_count": "3+",
        "key_params": "$199.99 / 8.8\" 120Hz IPS 2560×1600 / Dimensity 7400 / 8+128GB / 6500mAh / 20W / 6.95mm / 295g",
        "tech_features": ["8.8\" 小尺寸+2560×1600 高分辨率+120Hz 高刷新率（小屏平板罕见组合）", "Dimensity 7400（4nm 8核）", "6500mAh 大电池+20W 充电", "6.95mm / 295g 超薄轻量", "RGB 环形补光灯设计"],
        "why_important": "8.8\" 小尺寸平板市场持续有新品涌入；$199.99 价位段 2560×1600+120Hz+Dimensity 7400 组合性价比突出。",
        "terminal_relevance": "直接对标产品——小尺寸平板的屏幕/电池/芯片选型方案可逐项参考；6.95mm 超薄设计工艺值得关注。",
        "vendor": "Alldocube（台电）",
        "model": "iPlay 80 mini Turbo",
        "sources": "Notebookcheck、Gizmochina、Alldocube 官方",
        "remark": "8.8\" 小屏平板细分市场竞品，$199.99 性价比突出"
    },
    {
        "id": 12, "region": "intl", "status": "released",
        "title": "GOBOULT Stallion Ignite Gold / Nitro Ice",
        "stars": 2, "source": "C",
        "date": "2026-08-10",
        "domain": "智能手表",
        "url": "https://technosports.co.in/goboult-stallion-ignite-gold-nitro-ice/",
        "url_label": "TechnoSports",
        "signal_type": "产品发布",
        "confirm_count": "2+",
        "key_params": "₹5999/₹4999 / 1.43\" AMOLED 700nit / 120+运动 / 300mAh 7天 / IP67 / 福特Mustang联名",
        "tech_features": ["1.43\" AMOLED 700nit 亮度", "120+ 运动模式", "300mAh 7 天续航", "IP67 防水", "福特 Mustang 品牌联名"],
        "why_important": "印度市场智能手表竞争白热化；品牌联名（Mustang）是差异化营销新趋势。",
        "terminal_relevance": "入门级 AMOLED 手表方案对可穿戴终端成本控制有参考；印度市场渠道策略可关注。",
        "vendor": "GOBOULT",
        "model": "Stallion Ignite Gold / Nitro Ice",
        "sources": "TechnoSports、Times of India",
        "remark": "印度市场 ₹5K 档，目标 15% 市场份额"
    },
    {
        "id": 13, "region": "cn", "status": "released",
        "title": "Lenovo Lecoo P900A 学习平板",
        "stars": 3, "source": "B",
        "date": "2026-08-09/10",
        "domain": "平板",
        "url": "https://www.gizmochina.com/2026/08/09/lenovo-lecoo-pad-mini-launched-specs-price/",
        "url_label": "Gizmochina",
        "signal_type": "产品发布",
        "confirm_count": "2+",
        "key_params": "CN¥899/$133 / 8\" IPS / MediaTek 8核 / 8+128GB / 5000mAh / 4G VoLTE / 324g / ZUXOS",
        "tech_features": ["8\" IPS 小尺寸平板定位教育市场", "MediaTek 8 核 SoC", "4G VoLTE 通话功能", "ZUXOS 系统+超级互联 3.0", "324g 轻量化"],
        "why_important": "联想 Lecoo 子品牌聚焦教育/入门平板市场；¥899 价位段 4G 通话平板方案。",
        "terminal_relevance": "直接对标产品——入门教育平板的芯片/屏幕/电池/系统方案可逐项参考。",
        "vendor": "Lenovo（联想）Lecoo",
        "model": "P900A",
        "sources": "Gizmochina、Latestly",
        "remark": "8\" 教育平板，¥899 入门价位"
    },
    {
        "id": 14, "region": "cn", "status": "released",
        "title": "Amazfit Active Edge 跃我运动手表",
        "stars": 3, "source": "B",
        "date": "2026-08 上市",
        "domain": "智能手表",
        "url": "https://m.aeawr.com/product/22.html",
        "url_label": "Amazfit 官网",
        "signal_type": "产品发布",
        "confirm_count": "2+",
        "key_params": "¥1049 / 10ATM 100m防水 / 1.32\" 360×360 / 370mAh / 16天续航 / 内置GPS / Zepp Coach",
        "tech_features": ["10ATM 100m 专业级防水", "内置 GPS（不依赖手机）", "1.32\" 360×360 圆形表盘", "370mAh 16 天超长续航", "Zepp Coach AI 运动教练"],
        "why_important": "¥1049 价位段 10ATM 100m 防水+内置 GPS+16 天续航组合性价比突出；Zepp Coach AI 方案持续迭代。",
        "terminal_relevance": "10ATM 防水结构方案对终端密封设计有参考；Zepp Coach AI 运动健康方案可关注。",
        "vendor": "Amazfit（跃我）",
        "model": "Active Edge",
        "sources": "Amazfit 官网、京东",
        "remark": "¥1049 运动手表，10ATM 防水+16天续航"
    },
]

# ── 16 维覆盖面板 ──
DIMS = [
    ("SoC/芯片", 9, True), ("显示/OLED", 12, True), ("电池/快充", 10, True), ("散热", 4, True),
    ("无线通信", 6, True), ("音频", 1, True), ("摄像头", 3, True), ("结构/工艺", 14, True),
    ("传感器", 5, True), ("手写笔/触控", 0, False), ("生物识别", 2, True), ("AI/NPU", 4, True),
    ("马达/触觉", 1, True), ("折叠屏", 0, False), ("BMS/电源", 3, True), ("认证/合规", 8, True),
]

# ── Top 5 信号（星级降→信源升→状态优先→时间降）──
TOP5 = [
    {"rank": 1, "title": "OpenAI 甜甜圈 AI 音箱", "dim": "AI/NPU", "stars": 5, "key": "Jony Ive设计·GPT-Live·无屏+摄像头+机械件"},
    {"rank": 2, "title": "iQOO Neo11 至尊版", "dim": "SoC/电池", "stars": 4, "key": "天玑9500M 3nm首发·9100mAh硅负极·2K 144Hz"},
    {"rank": 3, "title": "Acer 暗影骑士·龙8Pro", "dim": "SoC/散热", "stars": 4, "key": "9955HX3D+RTX5070Ti·240Hz·215W"},
    {"rank": 4, "title": "DPVR P1 Max 企业VR", "dim": "AR-VR/散热", "stars": 4, "key": "骁龙XR2·8K解码·主动散热+50%·$549"},
    {"rank": 5, "title": "Garmin Venu X1", "dim": "显示/结构", "stars": 4, "key": "蓝宝石+钛·2000nit·8天续航·7.9mm/40g"},
]

# ── 统计 ──
total = len(CARDS)
cn_count = sum(1 for c in CARDS if c["region"] == "cn")
intl_count = sum(1 for c in CARDS if c["region"] == "intl")
a_count = sum(1 for c in CARDS if c["source"] == "A")
b_count = sum(1 for c in CARDS if c["source"] == "B")
five_star = sum(1 for c in CARDS if c["stars"] == 5)
dim_on = sum(1 for d in DIMS if d[2])

def stars_str(n):
    return "★" * n + "☆" * (5 - n)

def status_label(s):
    return {"coming": "即将上市", "released": "已上市", "progress": "进行中"}[s]

def status_class(s):
    return {"coming": "status-coming", "released": "status-released", "progress": "status-progress"}[s]

def source_class(s):
    return f"source-{s.lower()}"

# ── HTML 生成 ──
html = f"""<!DOCTYPE html>
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
  .header {{ background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:#fff; border-radius:var(--radius); padding:28px 32px; margin-bottom:20px; box-shadow:var(--shadow); }}
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
  .dim-bar-fill {{ height:100%; background:linear-gradient(90deg,#67c23a,#95d475); border-radius:4px; transition:width 0.5s; }}
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
  .status-progress {{ background:#f4f4f5; color:#909399; border:1px solid #e4e7ed; }}
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
    <div class="subtitle">采集口径：7类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑） | 搜索窗口60天 | 去重窗口14天</div>
    <div class="meta">
      <span class="meta-badge">总情报 {total}条</span>
      <span class="meta-badge">国内 {cn_count}条</span>
      <span class="meta-badge">国际 {intl_count}条</span>
      <span class="meta-badge">信源 A-E级</span>
      <span class="meta-badge">搜索窗口 60天</span>
    </div>
  </div>
  <div class="stats-bar">
    <div class="stat-item"><div class="stat-num">{total}</div><div class="stat-label">总情报数</div></div>
    <div class="stat-item"><div class="stat-num">{a_count}</div><div class="stat-label">A级信源</div></div>
    <div class="stat-item"><div class="stat-num">{b_count}</div><div class="stat-label">B级信源</div></div>
    <div class="stat-item"><div class="stat-num">7</div><div class="stat-label">覆盖产品类别</div></div>
    <div class="stat-item"><div class="stat-num">{five_star}</div><div class="stat-label">五星条数</div></div>
  </div>
  <div class="dim-panel">
    <div class="dim-header">
      <div class="dim-title">技术维度覆盖面板</div>
      <div class="dim-counter"><span class="dim-num">{dim_on}</span><span class="dim-total"> / 16 维度</span></div>
    </div>
    <div class="dim-bar"><div class="dim-bar-fill" style="width:{dim_on*100//16}%"></div></div>
    <div class="dim-grid">
"""

for name, count, on in DIMS:
    cls = "on" if on else "off"
    html += f'      <div class="dim-chip {cls}">{name} <span class="dim-count">{count}条</span></div>\n'

html += """    </div>
  </div>
  <div class="top-signals-panel">
    <div class="top-signals-header">
      <div class="top-signals-title">今日重点信号 Top 5</div>
      <div style="font-size:12px;color:var(--text-tertiary);">排序：星级降序→信源等级→状态优先→时间倒序</div>
    </div>
    <div class="top-signals-grid">
"""

for sig in TOP5:
    html += f"""      <div class="signal-card">
        <div><span class="sig-rank">{sig['rank']}</span><span class="sig-title">{sig['title']}</span></div>
        <div class="sig-tags"><span class="sig-dim">{sig['dim']}</span><span class="sig-stars">{'★' * sig['stars']}</span></div>
        <div class="sig-key">{sig['key']}</div>
      </div>
"""

html += """    </div>
  </div>
  <div class="summary-section">
    <div class="section-title">情报摘要表</div>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>类别</th><th>信源</th><th>状态</th><th>时间</th></tr></thead>
      <tbody>
"""

for c in CARDS:
    region_cls = "region-cn" if c["region"] == "cn" else "region-intl"
    region_label = "国内" if c["region"] == "cn" else "国际"
    status_cls = status_class(c["status"])
    status_lbl = status_label(c["status"])
    src_cls = source_class(c["source"])
    src_lbl = c["source"]
    html += f"""      <tr>
        <td>{c['id']}</td>
        <td class="td-title"><a href="#card-{c['id']}">{c['title']}</a></td>
        <td><span class="td-region {region_cls}">{region_label}</span></td>
        <td>{c['domain']}</td>
        <td><span class="source-tag {src_cls}">{src_lbl}</span></td>
        <td class="td-status"><span class="status-tag {status_cls}">{status_lbl}</span></td>
        <td>{c['date']}</td>
      </tr>
"""

html += """      </tbody>
    </table>
  </div>
  <div class="intel-section">
    <div class="section-title">情报详情卡片</div>
    <div class="intel-cards">
"""

for i, c in enumerate(CARDS):
    expanded = "expanded" if i == 0 else ""
    region_cls = "cn" if c["region"] == "cn" else "intl"
    status_cls = status_class(c["status"])
    status_lbl = status_label(c["status"])
    src_cls = source_class(c["source"])
    tech_list = ""
    for j, tech in enumerate(c["tech_features"], 1):
        tech_list += f'        <li data-num="{j}">{tech}</li>\n'

    html += f"""      <div class="intel-card {region_cls} {expanded}" id="card-{c['id']}">
        <div class="card-header" onclick="toggleCard(this)">
          <div class="card-num">{c['id']}</div>
          <div class="card-title-area">
            <div class="card-title">{c['title']}</div>
            <div class="card-badges">
              <span class="stars">{stars_str(c['stars'])}</span>
              <span class="source-tag {src_cls}">{c['source']}</span>
              <span class="status-tag {status_cls}">{status_lbl}</span>
              <span class="card-domain">{c['domain']}</span>
            </div>
          </div>
          <div class="card-toggle">▼</div>
        </div>
        <div class="card-body">
          <div class="card-content">
            <div class="field-grid">
              <div class="field"><div class="field-label">信号类型</div><div class="field-value">{c['signal_type']}</div></div>
              <div class="field"><div class="field-label">印证源数</div><div class="field-value">{c['confirm_count']}</div></div>
              <div class="field full"><div class="field-label">关键参数</div><div class="field-value">{c['key_params']}</div></div>
              <div class="field full"><div class="field-label">技术特性</div><div class="field-value"><ul class="tech-list">
{tech_list}      </ul></div></div>
              <div class="field full"><div class="field-label">为什么重要</div><div class="field-value">{c['why_important']}</div></div>
              <div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">{c['terminal_relevance']}</div></div>
              <div class="field"><div class="field-label">厂商</div><div class="field-value">{c['vendor']}</div></div>
              <div class="field"><div class="field-label">型号</div><div class="field-value">{c['model']}</div></div>
              <div class="field"><div class="field-label">时间</div><div class="field-value">{c['date']}</div></div>
              <div class="field"><div class="field-label">来源URL</div><div class="field-value"><a href="{c['url']}" target="_blank">{c['url_label']}</a></div></div>
              <div class="field full"><div class="field-label">信源明细</div><div class="field-value">{c['sources']}</div></div>
              <div class="field full"><div class="field-label">备注/待印证</div><div class="field-value">{c['remark']}</div></div>
            </div>
          </div>
        </div>
      </div>
"""

html += """    </div>
  </div>
</div>
<script>
function toggleCard(header) {
  var card = header.parentElement;
  card.classList.toggle('expanded');
}
</script>
</body>
</html>
"""

with open("WB_2026-08-20_硬件看板.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✓ 已生成 WB_2026-08-20_硬件看板.html（{total} 条情报，{cn_count} 国内 + {intl_count} 国际，{dim_on}/16 维度）")
