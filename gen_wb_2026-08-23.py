#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WB_2026-08-21 智能终端硬件情报看板生成器
- 14 条卡片（5 国内 + 9 国际）
- 7 品类 × 14 字段卡 + 16 维覆盖面板 + Top5 信号
- 单 HTML / 内联 CSS / 无 CDN / #card-N 锚点 / html{scroll-behavior:smooth}
- 信源 A-E 级 | 1-5★ | 状态 coming/released/leaked
- 14 天去重窗 + 60 天搜索窗
"""

DATE = "2026-08-23"
WEEK = "周日"
TITLE = f"智能终端硬件情报看板 · {DATE}（{WEEK}）"

# ── 情报卡片 ──
CARDS = [
    # ========== 国内 5 条 ==========
    {
        "id": 1,
        "region": "cn",
        "status": "coming",
        "title": "荣耀 X80 GT 工信部入网 即将月底发布",
        "stars": 5,
        "source": "B",
        "date": "2026-08-23",
        "domain": "手机",
        "url": "https://www.toutiao.com/article/7671581565901832748/",
        "url_label": "今日头条：荣耀 X80 GT 工信部入网",
        "signal_type": "工信部入网 + 即将发布",
        "confirm_count": "3+（今日头条/快科技/中关村在线）",
        "key_params": "骁龙8 Gen3 满血版；6.78\" 1.5K OLED 120Hz；13080mAh 青海湖硅碳电池；80W 有线 + 30W 反向；5000万 OIS 主摄；IP68 防尘防水；¥1999 起（国补）",
        "tech_features": [
            "13080mAh 青海湖硅碳负极电池，容量领先同价位旗舰",
            "骁龙8 Gen3 满血版，性能对标旗舰平台",
            "80W 有线 + 30W 反向双快充，补能灵活",
            "6.79\" 1.5K OLED 120Hz 高刷护眼屏",
            "IP68 防尘防水 + 5000万 OIS 主摄，旗舰级耐用与影像"
        ],
        "why_important": "荣耀 X80 GT 以 ¥1999 起将 13080mAh 硅碳电池 + 骁龙8 Gen3 + IP68 下放到中端价位，是 2026 年'大电池续航'旗舰性价比路线的代表；对手机/平板的硅碳电池路线有标杆意义",
        "terminal_relevance": "青海湖硅碳负极电池在 13080mAh 量级的量产应用，对平板/手机电池能量密度提升有直接参考价值；大电池 + 百瓦快充组合是续航焦虑的解法",
        "vendor": "荣耀（HONOR）",
        "model": "X80 GT",
        "sources": "今日头条、快科技、中关村在线",
        "remark": "工信部认证已完成，正式发布待 8 月底；续航与性价比为核心卖点"
    },
    {
        "id": 2,
        "region": "cn",
        "status": "released",
        "title": "华硕 a豆14 Air 2026 上架",
        "stars": 4,
        "source": "B",
        "date": "2026-08-20",
        "domain": "笔记本电脑",
        "url": "https://so.html5.qq.com/page/real/search_news?docid=70000021_0616a5337aa75052",
        "url_label": "腾讯新闻：华硕 a豆14 Air 2026 上架",
        "signal_type": "首发上市",
        "confirm_count": "2+（腾讯新闻/京东/华硕官网）",
        "key_params": "AMD 锐龙 R9 8945H / AI 9 H 365；32GB LPDDR5X；14\" 2.8K 120Hz OLED 1100nits；990g / 14.9mm；70Wh；Wi-Fi 6；¥6799 起",
        "tech_features": [
            "990g 超轻机身 + 14.9mm 薄，便携性突出",
            "14\" 2.8K 120Hz OLED 1100nits 高亮广色域屏",
            "锐龙 R9 8945H / AI 9 H 365，32GB LPDDR5X 板载",
            "70Wh 电池 + 轻薄设计，长续航与便携兼顾",
            "¥6799 起下探轻薄本价位"
        ],
        "why_important": "华硕 a豆14 Air 2026 以 990g + 2.8K OLED 切入轻薄本市场，是 AMD 平台轻薄本在屏幕与重量上的标杆",
        "terminal_relevance": "轻薄 + 高亮 OLED 的取舍对平板/手机屏幕选型有参考；LPDDR5X 板载内存趋势",
        "vendor": "华硕（ASUS）",
        "model": "a豆14 Air 2026",
        "sources": "腾讯新闻、京东、华硕官网",
        "remark": "8/20 上架；Ryzen AI 9 H 365 版为 AI 轻薄定位"
    },
    {
        "id": 3,
        "region": "cn",
        "status": "released",
        "title": "华硕 天选Air 2026 上市",
        "stars": 4,
        "source": "B",
        "date": "2026-08-20",
        "domain": "笔记本电脑",
        "url": "https://www.asus.com.cn/laptops/for-gaming/tuf-gaming/filter?Category=Ultra-slim-designs",
        "url_label": "华硕官网：天选 Air 2026",
        "signal_type": "首发上市",
        "confirm_count": "2+（华硕官网/京东）",
        "key_params": "AMD 锐龙 R9 AI 9 H 465；RTX 5060 8GB GDDR7 115W；14\" 2.5K 165Hz IPS；32GB；73Wh；1.46kg；Wi-Fi 6E；¥13699",
        "tech_features": [
            "RTX 5060 8GB GDDR7 115W 满血，轻薄游戏本性能释放",
            "14\" 2.5K 165Hz IPS 高刷电竞屏",
            "锐龙 R9 AI 9 H 465 处理器，AI 算力加持",
            "1.46kg 轻量机身 + 73Wh 电池，便携与续航平衡",
            "Wi-Fi 6E + 双接口，连接性到位"
        ],
        "why_important": "天选 Air 2026 把 RTX 5060 满血 + 锐龙 AI 9 塞进 1.46kg 机身，是 14\" 轻薄游戏本的性能代表",
        "terminal_relevance": "轻薄游戏本的散热/性能释放组合对平板 SoC 散热设计有参考",
        "vendor": "华硕（ASUS）",
        "model": "天选 Air 2026",
        "sources": "华硕官网、京东",
        "remark": "8/20 上市；定位轻薄高性能游戏本"
    },
    {
        "id": 4,
        "region": "cn",
        "status": "released",
        "title": "华硕 灵耀14双屏 2026 上市",
        "stars": 4,
        "source": "B",
        "date": "2026-08-20",
        "domain": "笔记本电脑",
        "url": "https://g.pconline.com.cn/x/2104/21044192.html",
        "url_label": "太平洋电脑网：华硕灵耀14双屏 2026",
        "signal_type": "首发上市",
        "confirm_count": "3+（太平洋电脑网/新浪财经/京东）",
        "key_params": "Intel Ultra X9 378H / 388H；32GB LPDDR5X 9600；14\" 2.8K 144Hz OLED 双触；99Wh；1.65kg；Wi-Fi 7；180 TOPS NPU；¥14999/16999/20499",
        "tech_features": [
            "14\" 双屏 OLED 2.8K 144Hz 双触控，多任务效率翻倍",
            "Ultra X9 378H/388H，NPU 180 TOPS 本地 AI 算力",
            "32GB LPDDR5X-9600 高频内存",
            "99Wh 大电池 + 1.65kg，续航与轻薄兼顾",
            "Wi-Fi 7 + 双雷电，连接旗舰级"
        ],
        "why_important": "灵耀14双屏 2026 以双触 OLED + 180 TOPS NPU 重新定义创作本形态，是双屏 AI 笔电的代表",
        "terminal_relevance": "双屏 + 触控 + 高 NPU 的创作形态对平板/二合一设备有借鉴",
        "vendor": "华硕（ASUS）",
        "model": "灵耀14双屏 2026（Zenbook Duo）",
        "sources": "太平洋电脑网、新浪财经、京东",
        "remark": "¥14999 起；双屏翻转设计"
    },
    {
        "id": 5,
        "region": "cn",
        "status": "released",
        "title": "小米 Mijia 智能音频眼镜发布",
        "stars": 4,
        "source": "B",
        "date": "2026-08-17",
        "domain": "AR-VR眼镜",
        "url": "https://smartglassesdaily.com/en/article/xiaomi-debuts-audio-smart-glasses-targets-ray-ban-meta-market-zj4kw",
        "url_label": "Smart Glasses Daily：小米 Mijia 智能音频眼镜发布",
        "signal_type": "正式发布",
        "confirm_count": "3+（Smart Glasses Daily/小米官方/多家科技媒体）",
        "key_params": "2026-08-17 发布；音频优先；对标 Ray-Ban Meta；€234.40；开放声场 + 指向麦克风；AI 语音助手；轻量镜框",
        "tech_features": [
            "音频优先设计，对标 Ray-Ban Meta 智能眼镜",
            "开放声场扬声器 + 指向性麦克风阵列，通话降噪",
            "内置 AI 语音助手，支持拍照/导航/问答",
            "轻量化镜框，日常佩戴无负担",
            "€234.40 定价，性价比切入智能眼镜市场"
        ],
        "why_important": "小米以音频优先路线切入智能眼镜，€234.40 对标 Ray-Ban Meta，是国产智能眼镜规模化的重要信号",
        "terminal_relevance": "音频眼镜是手机 AI 语音助手的延伸载体；轻量化 + 音频优先路线对可穿戴终端有借鉴",
        "vendor": "小米（Xiaomi）",
        "model": "Mijia 智能音频眼镜",
        "sources": "Smart Glasses Daily、小米官方",
        "remark": "8/17 发布；音频优先而非显示优先"
    },
    # ========== 国际 9 条 ==========
    {
        "id": 6,
        "region": "intl",
        "status": "coming",
        "title": "HUMAIN Horizon Ultra 骁龙 X2 Elite AI 笔电预热",
        "stars": 4,
        "source": "C",
        "date": "2026-08-20",
        "domain": "笔记本电脑",
        "url": "https://tbreak.com/humain-horizon-ultra-snapdragon-x2-elite-agentic-ai-laptop",
        "url_label": "tbreak：HUMAIN Horizon Ultra 骁龙 X2 Elite 笔电",
        "signal_type": "预热/即将发布",
        "confirm_count": "3+（tbreak/网易/laptopscheck）",
        "key_params": "Snapdragon X2 Elite；定制 agentic-AI OS；8/19-20 预热；LEAP 8/31-9/3 利雅得发布；5G；银灰；2×USB-C + 3.5mm",
        "tech_features": [
            "Snapdragon X2 Elite 平台，高能效 ARM 架构",
            "定制 agentic-AI OS，强调自主智能体工作流",
            "内置 5G 连接，移动生产力",
            "LEAP 大会（8/31-9/3 利雅得）正式发布",
            "2×USB-C + 3.5mm 接口布局"
        ],
        "why_important": "HUMAIN（沙特）以 Snapdragon X2 Elite + 自研 agentic-AI OS 切入 AI 笔电，是中东科技自主化的代表",
        "terminal_relevance": "ARM 高能效 + agentic AI OS 对平板/手机 AI 操作系统路线有参考",
        "vendor": "HUMAIN（沙特）",
        "model": "Horizon Ultra",
        "sources": "tbreak、网易、laptopscheck",
        "remark": "LEAP 8/31-9/3 利雅得发布；agentic AI 为卖点"
    },
    {
        "id": 7,
        "region": "intl",
        "status": "released",
        "title": "ASUS ProArt P16 2026 多区域发售",
        "stars": 4,
        "source": "C",
        "date": "2026-08-15",
        "domain": "笔记本电脑",
        "url": "https://store.asus.com/jp/asus-proart-p16-h7606.html",
        "url_label": "华硕日本商城：ProArt P16 2026",
        "signal_type": "发售",
        "confirm_count": "3+（华硕日本/墨西哥/澳洲商城）",
        "key_params": "AMD 锐龙 R9 AI 9 HX370；RTX 5070 8GB GDDR7；64GB + 2TB；16\" 3K OLED 120Hz 1000nits 触；90Wh；1.85kg / 14.9mm；Wi-Fi 7；50 TOPS NPU",
        "tech_features": [
            "RTX 5070 8GB GDDR7 创作级显卡",
            "16\" 3K OLED 120Hz 1000nits 触控，创作色彩精准",
            "锐龙 R9 AI 9 HX370 + 50 TOPS NPU",
            "64GB + 2TB 大内存大存储创作配置",
            "90Wh + Wi-Fi 7，续航与连接旗舰级"
        ],
        "why_important": "ProArt P16 2026 是华硕创作本旗舰，RTX 5070 + 3K OLED 触控 + 64GB 组合对标 MacBook Pro",
        "terminal_relevance": "创作本的高色准 OLED + 大内存对平板创作场景有参考",
        "vendor": "华硕（ASUS）",
        "model": "ProArt P16 2026（H7606）",
        "sources": "华硕日本/墨西哥/澳洲商城",
        "remark": "多区域发售；创作工作站定位"
    },
    {
        "id": 8,
        "region": "intl",
        "status": "coming",
        "title": "Lenovo Legion Y700 Infinite 旗舰小平板曝光",
        "stars": 5,
        "source": "B",
        "date": "2026-08-25",
        "domain": "平板",
        "url": "https://www.gizmochina.com/2026/08/15/lenovo-legion-y700-infinite-tipped-with-oled-screen-and-dual-usb-c-ports/",
        "url_label": "Gizmochina：联想 Legion Y700 Infinite 曝光",
        "signal_type": "即将发布 + 参数曝光",
        "confirm_count": "3+（Gizmochina/NotebookCheck/Lowyat）",
        "key_params": "8/25 中国发布；8.4\" OLED 2560×1600 165Hz 3400Hz 采样；超频骁龙8 Elite Gen5；7470mAh；68W；双 USB-C；5G；双 X 轴马达；安兔兔 4,585,844；15000mm² VC；6.5mm / 298g；8MP+50MP",
        "tech_features": [
            "8.4\" OLED 2560×1600 165Hz + 3400Hz 触控采样，旗舰小平板屏",
            "超频骁龙8 Elite Gen5，安兔兔 4,585,844 分",
            "7470mAh + 68W 快充，双 USB-C 接口",
            "15000mm² VC 均热板 + 双 X 轴线性马达",
            "6.5mm / 298g 轻薄，5G 连接"
        ],
        "why_important": "Legion Y700 Infinite 以 8.4\" OLED 165Hz + 超频骁龙8 Elite Gen5 重新定义小尺寸旗舰平板性能上限，8/25 国内发布对标红魔 Astra 2",
        "terminal_relevance": "小尺寸 OLED 高刷平板 + 主动散热是平板性能赛道新标杆；对 TCL 平板旗舰有对标价值",
        "vendor": "联想（Lenovo）",
        "model": "Legion Y700 Infinite",
        "sources": "Gizmochina、NotebookCheck、Lowyat",
        "remark": "8/25 19:00 中国发布；骁龙8 Elite Gen5 超频版"
    },
    {
        "id": 9,
        "region": "intl",
        "status": "released",
        "title": "Samsung EP-P2900 Qi2.2 磁吸无线充电器上市",
        "stars": 3,
        "source": "B",
        "date": "2026-08-15",
        "domain": "无线充",
        "url": "https://www.samsung.com/tw/mobile-accessories/magnet-wireless-charger-dark-gray-ep-p2900bbtgtw/",
        "url_label": "三星台湾：EP-P2900 磁吸无线充电器",
        "signal_type": "上市",
        "confirm_count": "3+（三星台湾/美国/新西兰零售商）",
        "key_params": "25W Qi2.2；4.4mm 超薄；1.5m 线；Galaxy S26 Ultra 31 分钟充 50%；NT$1290；支持 Galaxy Buds",
        "tech_features": [
            "25W Qi2.2 磁吸无线充电，符合最新 Qi2.2 标准",
            "4.4mm 超薄机身，便携",
            "Galaxy S26 Ultra 31 分钟充至 50%",
            "1.5m 长线，使用自由",
            "兼容 Galaxy Buds 等配件"
        ],
        "why_important": "三星 EP-P2900 是首批 Qi2.2 25W 磁吸充电器，标志 Qi2.2 标准落地",
        "terminal_relevance": "Qi2.2 25W 磁吸标准对手机/平板无线充配件有参考",
        "vendor": "三星（Samsung）",
        "model": "EP-P2900",
        "sources": "三星台湾、三星美国、PP 零售商",
        "remark": "NT$1290；Qi2.2 首发之一"
    },
    {
        "id": 10,
        "region": "intl",
        "status": "released",
        "title": "Google Pixelsnap Qi2 磁吸充电器上架",
        "stars": 3,
        "source": "B",
        "date": "2026-08-21",
        "domain": "无线充",
        "url": "https://9to5google.com/2026/06/26/googles-official-qi2-wireless-charging-stand-for-pixel-10-is-almost-worth-buying-right-now/",
        "url_label": "9to5Google：Google Pixelsnap Qi2 充电器",
        "signal_type": "上市 + 折扣",
        "confirm_count": "3+（9to5Google/nextapple/ojeo）",
        "key_params": "Qi2 25W 磁吸；Pixel 10 Pro XL；可拆 puck + 支架；$56-70（折扣）；1m USB-C；三配件 ¥1009/1349/2349",
        "tech_features": [
            "Qi2 25W 磁吸无线充电，适配 Pixel 10 系列",
            "可拆 puck + 支架二合一设计",
            "1m USB-C 线，桌面自由",
            "近期折扣至 $35-70，性价比提升",
            "三配件组合 ¥1009/1349/2349"
        ],
        "why_important": "Google Pixelsnap 是 Pixel 10 生态首款 Qi2 磁吸配件，标志 Google 进入磁吸无线充阵营",
        "terminal_relevance": "磁吸无线充生态对手机/平板配件标准化有参考",
        "vendor": "Google",
        "model": "Pixelsnap",
        "sources": "9to5Google、nextapple、ojeo",
        "remark": "适配 Pixel 10 Pro XL；近期折扣"
    },
    {
        "id": 11,
        "region": "intl",
        "status": "released",
        "title": "绿联 W776 Qi2 主动制冷无线充支架发布",
        "stars": 3,
        "source": "B",
        "date": "2026-08-20",
        "domain": "无线充",
        "url": "https://finance.sina.cn/tech/2026-08-20/detail-ininyfvh7995509.d.html",
        "url_label": "新浪财经：绿联 W776 Qi2 无线充电基座",
        "signal_type": "发布 + 上市",
        "confirm_count": "3+（Gizmo/腾讯新闻/新浪财经）",
        "key_params": "8/20；$79.99；25W Qi2 + 5W AirPods；主动 TEC 制冷(<20℃)；内置 LED 屏；90° 倾角；1.5m",
        "tech_features": [
            "25W Qi2 + 5W AirPods 双区无线充",
            "主动 TEC 半导体制冷，充电温度 <20℃",
            "内置 LED 屏显示充电状态",
            "90° 可调倾角支架",
            "1.5m 线，$79.99"
        ],
        "why_important": "绿联 W776 把主动制冷 + LED 屏引入 Qi2 支架，是无线充配件差异化的代表",
        "terminal_relevance": "主动制冷无线充对手机/平板快充温控有借鉴",
        "vendor": "绿联（UGREEN）",
        "model": "W776 Qi2 无线充电支架",
        "sources": "Gizmo、腾讯新闻、新浪财经",
        "remark": "$79.99；8/20 发布"
    },
    {
        "id": 12,
        "region": "intl",
        "status": "released",
        "title": "Redmi Watch 6 活力版发布",
        "stars": 3,
        "source": "B",
        "date": "2026-08-20",
        "domain": "智能手表",
        "url": "https://finance.sina.cn/tech/2026-08-20/detail-ininxqxq8008273.d.html?vt=4",
        "url_label": "新浪财经：Redmi Watch 6 活力版发布",
        "signal_type": "发布 + 上市",
        "confirm_count": "3+（新浪财经/今日头条/搜狐）",
        "key_params": "8/20；¥349；1.85\" AMOLED 390×450 1200nits；470mAh；18天；26g；140+ 运动；BT 通话；IP68；兼容小米快拆表带",
        "tech_features": [
            "1.85\" AMOLED 390×450 1200nits 高亮屏",
            "470mAh + 18 天续航，长续航性价比",
            "140+ 运动模式 + BT 通话",
            "26g 轻量 + IP68 防水",
            "兼容小米快拆表带生态"
        ],
        "why_important": "Redmi Watch 6 活力版以 ¥349 将 AMOLED + 18 天续航下放到入门手表，是性价比智能表代表",
        "terminal_relevance": "长续航 + 轻量腕表对手机/平板蓝牙配件生态有参考",
        "vendor": "红米（Redmi / 小米）",
        "model": "Watch 6 活力版",
        "sources": "新浪财经、今日头条、搜狐",
        "remark": "¥349；8/20 发布"
    },
    {
        "id": 13,
        "region": "intl",
        "status": "leaked",
        "title": "OpenAI 甜甜圈造型 AI 智能音箱泄露",
        "stars": 4,
        "source": "C",
        "date": "2026-08-07",
        "domain": "智能音箱",
        "url": "https://me.mashable.com/tech/74779/openais-smart-speaker-leaked-uae-pricing-design-and-specifications",
        "url_label": "Mashable：OpenAI 甜甜圈 AI 音箱泄露",
        "signal_type": "泄露/预告",
        "confirm_count": "3+（Mashable/AIProductHub/PivotNews）",
        "key_params": "甜甜圈造型；Jony Ive / LoveFrom 设计；$300-400；2026-08-06/07 泄露；电池供电；摄像头；可动机械部件；GPT-Live；2027 上市；无屏",
        "tech_features": [
            "甜甜圈造型，Jony Ive / LoveFrom 操刀设计",
            "电池供电 + 摄像头 + 可动机械部件",
            "GPT-Live 实时对话 AI",
            "无屏设计，纯语音交互",
            "$300-400 定价，2027 上市"
        ],
        "why_important": "OpenAI 首款消费硬件（Jony Ive 设计）以无屏甜甜圈音箱形态切入，是 AI 原生硬件的标志事件",
        "terminal_relevance": "AI 原生无屏语音终端对手机/平板的语音助手形态有启示",
        "vendor": "OpenAI",
        "model": "AI 智能音箱（代号甜甜圈）",
        "sources": "Mashable、AIProductHub、PivotNews",
        "remark": "2027 上市；GPT-Live 驱动"
    },
    {
        "id": 14,
        "region": "intl",
        "status": "released",
        "title": "Nothing Phone 4a 发布",
        "stars": 3,
        "source": "B",
        "date": "2026-03-05",
        "domain": "手机",
        "url": "https://www.yugatech.com/news/nothing-phone-4a-unveiled",
        "url_label": "YugaTech：Nothing Phone 4a 发布",
        "signal_type": "发布",
        "confirm_count": "3+（YugaTech/BDMobilePrice/多家媒体）",
        "key_params": "2026-03-05 发布；骁龙7s Gen4；6.78\" AMOLED 120Hz 4500nits；50MP OIS 主摄 + 50MP 潜望 3.5x + 超广；32MP 前；5080mAh；50W；€349 起；Nothing OS 4.1 / Android 16；IP64",
        "tech_features": [
            "骁龙7s Gen4 中端平台",
            "6.78\" AMOLED 120Hz 4500nits 高亮屏",
            "50MP OIS 主摄 + 50MP 潜望 3.5x 长焦 + 超广，影像越级",
            "5080mAh + 50W 快充",
            "Nothing OS 4.1 / Android 16，IP64"
        ],
        "why_important": "Nothing Phone 4a 以 €349 将 50MP 潜望长焦 + 4500nits 屏下放到中端，是性价比影像手机代表",
        "terminal_relevance": "中端机的潜望长焦 + 高亮屏对平板/手机影像与屏幕选型有参考",
        "vendor": "Nothing",
        "model": "Phone 4a",
        "sources": "YugaTech、BDMobilePrice",
        "remark": "€349 起；2026-03-05 发布"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 8, True),
    ("显示/OLED", 9, True),
    ("折叠屏", 0, False),
    ("手写笔/触控", 2, True),
    ("散热/液冷", 3, True),
    ("电池/续航", 8, True),
    ("快充/无线充", 6, True),
    ("影像", 3, True),
    ("AI/NPU", 4, True),
    ("音频/扬声器", 2, True),
    ("5G/通信", 2, True),
    ("Wi-Fi/连接", 4, True),
    ("AR/VR显示", 1, True),
    ("材质/工艺", 5, True),
    ("可持续/模块化", 0, False),
    ("手柄/外设", 1, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {
        "rank": 1,
        "title": "荣耀 X80 GT",
        "dim": "电池/续航",
        "stars": 5,
        "key": "13080mAh 硅碳 + 骁龙8 Gen3 + IP68 + ¥1999"
    },
    {
        "rank": 2,
        "title": "Lenovo Legion Y700 Infinite",
        "dim": "显示/OLED",
        "stars": 5,
        "key": "8.4\" OLED 165Hz + 骁龙8 Elite Gen5 + 8/25 发布"
    },
    {
        "rank": 3,
        "title": "小米 Mijia 智能音频眼镜",
        "dim": "AR/VR显示",
        "stars": 4,
        "key": "对标 Ray-Ban Meta + €234 + 音频优先"
    },
    {
        "rank": 4,
        "title": "OpenAI AI 智能音箱",
        "dim": "音频/扬声器",
        "stars": 4,
        "key": "Jony Ive 设计 + 甜甜圈造型 + GPT-Live"
    },
    {
        "rank": 5,
        "title": "ASUS ProArt P16 2026",
        "dim": "AI/NPU",
        "stars": 4,
        "key": "RTX 5070 + 50 TOPS NPU + 3K OLED 触控"
    },
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
    return {"coming": "即将上市", "released": "已上市", "leaked": "泄露/预告"}[s]

def status_class(s):
    return {"coming": "status-coming", "released": "status-released", "leaked": "status-progress"}[s]

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

with open("WB_2026-08-23_硬件看板.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML 生成完成：WB_2026-08-23_硬件看板.html")
print(f"   总情报：{total} 条（国内 {cn_count} + 国际 {intl_count}）")
print(f"   维度覆盖：{dim_on}/16")
print(f"   五星条数：{five_star}")