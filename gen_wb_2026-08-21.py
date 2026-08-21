#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WB_2026-08-21 智能终端硬件情报看板生成器
- 14 条卡片（5 国内 + 9 国际）
- 7 品类 × 14 字段卡 + 16 维覆盖面板 + Top5 信号
- 单 HTML / 内联 CSS / 无 CDN / #card-N 锚点 / html{scroll-behavior:smooth}
- 信源 A-E 级 | 1-5★ | 状态 coming/released/leaked
- 14 天去重窗 + 60 天搜索窗
"""

DATE = "2026-08-21"
WEEK = "周五"
TITLE = f"智能终端硬件情报看板 · {DATE}（{WEEK}）"

# ── 情报卡片 ──
CARDS = [
    # ========== 国内 5 条 ==========
    {
        "id": 1,
        "region": "cn",
        "status": "released",
        "title": "七彩虹隐星 P16 Pro 星风水冷版 2026 上市",
        "stars": 5,
        "source": "B",
        "date": "2026-08-20",
        "domain": "笔记本电脑",
        "url": "https://www.163.com/dy/article/L4PIN3NR0511CPVM.html",
        "url_label": "网易快科技：七彩虹隐星 P16 Pro 水冷版上市",
        "signal_type": "首发上市",
        "confirm_count": "3+（快科技/IT之家/游侠网/QQ新闻）",
        "key_params": "酷睿 Ultra 7 251HX + RTX 5060 8GB GDDR7 满血 115W；16GB DDR5-5600 + 1TB PCIe 4.0；16\" 2.5K 300Hz IPS 500nit 100% sRGB；机身内置水冷管路 + 2 风扇 5 热管；雾屿白 RGB 光柱；19.6mm / 2.05kg / 60Whr；¥11,499（国补后¥9,999）",
        "tech_features": [
            "首创笔电内置水路 + 外接 Docking 水冷设计，连底座一键进入超能模式",
            "Arrow Lake-HX 18 核 18 线程，台积电 N3B，CPU 性能释放 100W+",
            "RTX 5060 满血 115W，支持 DLSS 4.5 + Reflex 2 光追帧率 +35%",
            "280W GaN 电源适配器，专属水冷 Docking 解锁更强持续性能",
            "RGB 光柱灯带 + 雾屿白 ID，A/C 面铝合金，可换内存/SSD 双槽"
        ],
        "why_important": "全球首款消费级水冷笔电，水冷 Docking 把双芯热量由液冷直接带走，是 2026 年游戏笔电形态创新的标志事件；七彩虹以高配 RTX 5060 + 酷睿 Ultra 7 HX 进入 ¥9999 国补价位段，对国内笔电市场冲击明显",
        "terminal_relevance": "笔电独立显卡性能外延方案：内置水路为平板/手机散热设计提供新思路（液冷 VC 模块化），对 TCL 平板散热架构有借鉴价值",
        "vendor": "七彩虹（Colorful）",
        "model": "隐星 P16 Pro 星风水冷版 2026",
        "sources": "快科技、IT之家、游侠网、QQ新闻、ali213",
        "remark": "8/28 10:00 发售；游戏本/AI 训练/3D 创作多场景定位；产能与售后需观察"
    },
    {
        "id": 2,
        "region": "cn",
        "status": "released",
        "title": "联想 2026 款 ThinkPad E13 AI 上架",
        "stars": 4,
        "source": "B",
        "date": "2026-08-20",
        "domain": "笔记本电脑",
        "url": "https://www.notebookcheck.net/Lenovo-opens-reservations-for-its-cheapest-13-inch-ThinkPad-of-2026-yet-powered-by-Lunar-Lake.1373785.0.html",
        "url_label": "NotebookCheck：ThinkPad E13 AI 2026 reservation",
        "signal_type": "首发上市",
        "confirm_count": "3+（IT之家/网易/NotebookCheck）",
        "key_params": "酷睿 Ultra 5 226V (Lunar Lake, 8C8T, Arc 130V 7 Xe²)；16GB LPDDR5X-8533 不可升级 + 512GB SSD；13.3\" 1920×1200 IPS 60Hz 400nit 100% sRGB；180° 铰链；1.21kg / 17.18mm / 54.7Whr；¥7,499（预约¥6,999，8/25 正式开售）",
        "tech_features": [
            "Lunar Lake 97 TOPS AI 算力，内置 NPU 支持本地 AI 推理",
            "LPDDR5X-8533 板载内存 + Arc 130V 核显，能效比优于上代 Meteor Lake",
            "180° 铰链 + 84.7% 屏占比 + AG 防眩光 + Eyesafe 2.0 护眼认证",
            "2×雷电 4（PD3.1/DP2.1）+ 2×USB-A + HDMI 2.1 + Wi-Fi 6E",
            "通过 MIL-STD-810H 26 项严苛测试，500 万像素 IR 摄像头 + 物理防窥盖"
        ],
        "why_important": "Lunar Lake 入门商务本下探到 ¥6,999，是 E 系列首次搭载 Ultra 5 226V 的国行型号，标志 Lunar Lake 平台向中端商务市场铺开；联想用 180° 铰链 + IR Windows Hello 替代指纹方案是设计取舍信号",
        "terminal_relevance": "Lunar Lake 的 97 TOPS NPU 算力下沉到商务本价位，对平板/手机的 NPU 路线提供对照（性能/功耗曲线）",
        "vendor": "联想（Lenovo）",
        "model": "ThinkPad E13 AI 2026（01CD）",
        "sources": "IT之家、网易快科技、NotebookCheck、Lenovo 官网",
        "remark": "预约期至 8/24（UTC+8），8/25 正式开售；60Hz 屏为该价位遗憾"
    },
    {
        "id": 3,
        "region": "cn",
        "status": "released",
        "title": "机械师曙光 16S 2026 新增 R7+RTX 5050 版本",
        "stars": 3,
        "source": "B",
        "date": "2026-08-20",
        "domain": "笔记本电脑",
        "url": "https://weibo.com/1826017320/5334069879507971",
        "url_label": "机械师官方微博：曙光 16S 2026 新增 R7+RTX 5050 版",
        "signal_type": "配置扩展",
        "confirm_count": "2（机械师官微/京东自营）",
        "key_params": "AMD 锐龙 R7-7745HX + RTX 5050 / RTX 5060（115W 满血）；16\" 2.5K 180Hz IPS 100% sRGB；16GB DDR5 + 1TB SSD（双内存槽 + 双硬盘位）；2.5kg / 23.3mm / 80Whr；R7+5050 起步¥8,999，R7+5060 ¥9,499，i9+5070Ti ¥11,999",
        "tech_features": [
            "AMD R7-7745HX 5.1GHz + RTX 50 系满血 115W，CPU/GPU 双线高释放",
            "16\" 2.5K 180Hz 高刷电竞屏 + 100% sRGB 色域兼顾设计与游戏",
            "全尺寸 RGB 键盘 + 数字小键盘，2.5G RJ45 + HDMI 2.1 + Mini DP 齐全 I/O",
            "80Whr 大电池 + 多接口设计，学生/办公/游戏三栖定位",
            "¥8999 起对标二三线品牌的国补游戏本，性价比突出"
        ],
        "why_important": "曙光 16S 系列扩展到 AMD R7+RTX 5050 入门档位（¥8999），补齐 AMD 平台的国补入门游戏本空白，与拯救者/华硕 TUF 形成差异化竞争",
        "terminal_relevance": "AMD 笔电平台下沉方案对比，5.1GHz 8 核 CPU + 满血 RTX 50 系在中端游戏本的散热/性能释放组合可作为平板 SoC 选型参考",
        "vendor": "机械师（MACHENIKE）",
        "model": "曙光 16S 2026（R7-7745HX + RTX 5050/5060）",
        "sources": "机械师官网、京东自营、ZOL",
        "remark": "8/20 起开启销售；R7-7745HX 属 Zen 4 而非 Zen 5，性能定位中端"
    },
    {
        "id": 4,
        "region": "cn",
        "status": "released",
        "title": "Alldocube iPlay Mini 4 中国上市",
        "stars": 3,
        "source": "B",
        "date": "2026-08-15",
        "domain": "平板",
        "url": "https://www.notebookcheck.net/Alldocube-launches-affordable-compact-tablet-with-Android-16-and-90Hz-display.1369767.0.html",
        "url_label": "NotebookCheck：Alldocube iPlay Mini 4",
        "signal_type": "中国首发",
        "confirm_count": "3+（NotebookCheck/lavx/giznewsdaily）",
        "key_params": "紫光展锐 Unisoc T7300 (6nm, 2×A78@2.2GHz + 6×A55)；8GB RAM + 128GB UFS（microSD 1TB）；8.4\" IPS 1920×1200 90Hz 450nit in-cell；13MP 后 + 5MP 前；6050mAh + 18W PD；金属机身 7.3mm / 300g；Android 16 + Alldocube OS 5.0L；¥999（中国 JD 996 / 国际版 iPlay 80 Mini Pro Walmart $208）",
        "tech_features": [
            "紫光展锐 T7300 中端 6nm SoC，安兔兔 ~65 万分，4G LTE 双卡双待 + TF 三卡槽",
            "8.4\" 90Hz 高刷 + Widevine L1 HD 流媒体 + 立体声双扬 + 3.5mm 耳机口",
            "6050mAh + 18W USB-PD，蓝牙 5.4 + Wi-Fi 6 + 双频 GPS/北斗",
            "中国版 ¥999 起步，国际版 iPlay 80 Mini Pro 同规格已 AliExpress $155 售卖",
            "金属机身 300g + 7.3mm，便携学生/通勤/电子书定位"
        ],
        "why_important": "Alldocube 国产平板品牌在 8 寸小平板细分市场持续发力；紫光展锐 T7300 中端 6nm 平台已可支撑 90Hz 高刷 + 全网 4G，为国产 SoC 在平板赛道份额提升提供案例",
        "terminal_relevance": "紫光展锐 T7300 性能 / 价格曲线对国内中低端平板 SoC 选型有直接参考价值；8.4\" 90Hz 平板是手机/平板尺寸边界产品",
        "vendor": "Alldocube（深圳）",
        "model": "iPlay Mini 4（国际版：iPlay 80 Mini Pro）",
        "sources": "NotebookCheck、JD.com、IT Home、Walmart",
        "remark": "¥996 京东售价，¥999 官方起步价；中端平板性价比款，T7300 安兔兔 65 万分"
    },
    {
        "id": 5,
        "region": "cn",
        "status": "released",
        "title": "INMO GO3 智能眼镜日本首发上市",
        "stars": 4,
        "source": "B",
        "date": "2026-07-30",
        "domain": "AR-VR眼镜",
        "url": "https://claypier.com/en/inmo-go3-japan-launch",
        "url_label": "claypier：INMO GO3 日本首发上市",
        "signal_type": "海外首发 + 国内在售",
        "confirm_count": "4（The Gadgeteer/claypier/finance.biggo/appbank）",
        "key_params": "640×480 双目 Micro-LED 衍射光波导 + 紫光展锐双核 CPU；30° FOV / 1500nit 峰值 / 单色绿显示；4 麦 + 2 开放式扬声器；58g 镜框（¥2 镜架）；270mAh×2 可换电池 + 1300mAh 充电盒（约 3-4 次换电）；¥99,800 日元（约 ¥4,800）/ 国内 ¥2999；¥499 Kickstarter / $599 MSRP",
        "tech_features": [
            "双目 Micro-LED 衍射光波导显示 + 97% 透光率，单色绿显优先亮度与续航",
            "98 语言实时翻译（含离线 9 语言：英中日西韩法德俄泰），ChatGPT + Gemini 双 AI",
            "可更换 270mAh 电池 ×2 + 充电仓设计，单次续航 3h 翻译 / 3.3h 提词 / 8h 待机",
            "AI 提词（自动按语速滚动）+ AR 导航 + 会议录音转写/摘要 + 拍照摄像",
            "JUN GINZA 合作定制近视镜片；物理相机隐私遮罩解决公共场所信任问题"
        ],
        "why_important": "INMO GO3 是国产 AR 眼镜首个以\"AI 翻译 + 可换电池\"差异化打法切入海外（日本）市场的成功案例；以 ¥4,800 价位提供 98 语言实时翻译 + AI 提词，对商务/旅游/学生场景具有替代手机 + 翻译机的潜力",
        "terminal_relevance": "AR 眼镜 + AI 翻译 + 可换电池组合，是平板/手机 AI 应用的延伸载体；显示与电池的取舍（单色 Micro-LED）值得借鉴",
        "vendor": "影目 INMO（四川影目科技）",
        "model": "GO3（型号 IMG301）",
        "sources": "claypier、The Gadgeteer、AppBank、BigGo 财经、京东 ¥2999",
        "remark": "日本 7/30 上市，国内京东在售 ¥2999；2026-08-21 FRESH（22 天前发布）"
    },
    # ========== 国际 9 条 ==========
    {
        "id": 6,
        "region": "intl",
        "status": "released",
        "title": "MSI Prestige 14 Flip AI+ Vincent van Gogh Edition 笔电发布",
        "stars": 3,
        "source": "C",
        "date": "2026-06-04",
        "domain": "笔记本电脑",
        "url": "https://hk.msi.com/blog/when-art-meets-ai-msi-prestige-14-flip-ai-vincent-van-gogh-edition",
        "url_label": "MSI 官方博客：Prestige 14 Flip AI+ 梵谷特仕版（HK）",
        "signal_type": "主题特别版上市",
        "confirm_count": "3+（MSI HK 博客 / MSI 法区 D3MX 规格页 / YugaTech / ZOL 中国）",
        "key_params": "Intel® Core™ Ultra X9 processor 378H（16 核 / 50 NPU TOPS / Max 5.0GHz）；板载 32GB LPDDR5X-8533（最大 64GB）+ 1TB PCIe Gen4 SSD；14\" 1920×1200 OLED 100% DCI-P3 触控 + MSI Pen；1.37kg / 11.9-13.9mm 超轻薄；81Whr 续航 30h+ 1080p 视频；Wi-Fi 7 Killer BE1775 + 蓝牙 6 + 2× 雷电 4 + 2× USB-A 3.2 + HDMI 2.1（8K60/4K120）；¥15,999 国行 / 国补后 ¥14,499",
        "tech_features": [
            "Intel Core Ultra X9 378H 处理器，NPU 算力高达 50 TOPS，AI 全面赋能创作工作流",
            "14\" 1920×1200 OLED 100% DCI-P3 触控翻转屏，360° 铰链 + MSI Pen 灵隐触控笔",
            "11.9-13.9mm / 1.37kg 超轻薄机身，81Whr 大电池续航 30h（1080p 视频播放）",
            "MIL-STD-810H/G 军规认证 + Wi-Fi 7 Killer BE1775 + 蓝牙 6 + 双雷电 4 全接口",
            "梵谷特仕版独家星空纹理机身 + 《隆河上的星夜》/《星夜》双主题 UI + 限量包装套装"
        ],
        "why_important": "MSI 把'梵谷艺术联名 + Lunar Lake X9 + OLED 翻转 + 1.37kg 轻薄'整合到一款 14\" AI 笔电，国行 ¥14,499（国补后）切入高端创作者市场；艺术联名笔电赛道对平板产品的'设计差异化'路线有参考",
        "terminal_relevance": "笔电翻转 OLED + 手写笔 + AI + 艺术联名'四件套'，对平板产品（创作者平板 / 二合一）的设计取舍与品牌营销有借鉴",
        "vendor": "MSI（微星）",
        "model": "Prestige 14 Flip AI+ Vincent van Gogh Edition（型号 D3MX）",
        "sources": "MSI HK 官方博客、MSI 法区 D3MX 规格页、YugaTech、ZOL 中国",
        "remark": "国行 2026/8/3 已开售；¥15,999 / 国补后 ¥14,499；含梵谷特仕版限量周边套装"
    },
    {
        "id": 7,
        "region": "intl",
        "status": "released",
        "title": "Acer Predator Helios Neo 16S AI 游戏笔电评测",
        "stars": 3,
        "source": "C",
        "date": "2026-01-14",
        "domain": "笔记本电脑",
        "url": "https://www.notebookcheck.net/Shooting-star-or-flop-Acer-Predator-Helios-Neo-16S-AI-gaming-laptop-review.1201655.0.html",
        "url_label": "NotebookCheck 评测：Acer Predator Helios Neo 16S AI",
        "signal_type": "独立评测报道",
        "confirm_count": "3+（NotebookCheck / TrustedReviews / PCWorld / Creative Bloq）",
        "key_params": "Intel Core Ultra 9 275HX（Arrow Lake-HX, 24c/24t, 5.4GHz）；RTX 5070 Ti Laptop 12GB GDDR7 @115W；16\" 2560×1600 OLED 240Hz 100% DCI-P3 / 1ms 响应；32GB DDR5-6400 + 1TB PCIe 4.0 SSD；99.99Whr / 2.19kg；售价约 2,400 欧元 / $1,700 起",
        "tech_features": [
            "Intel Ultra 9 275HX + RTX 5070 Ti 115W 游戏性能，PD 140W PL2",
            "16\" 2.5K OLED 240Hz 镜面屏 + DisplayHDR True Black 1000 认证",
            "5 代 AeroBlade 双风扇 + 5 热管 + 液态金属导热",
            "5 USB 接口 + Thunderbolt 4 + HDMI 2.1 + RJ45 Killer Wi-Fi 6E",
            "4 区 RGB 背光键盘 + 维护友好（2 RAM + 2 M.2 插槽全部暴露）"
        ],
        "why_important": "Acer 在主流价位的 16\" OLED 游戏本中保持了相对可接受价位（$1,700 起对比 Asus ROG Zephyrus G16 $2,600+），是 2026 年 Q2 16 寸 OLED 游戏本的高性价比选项",
        "terminal_relevance": "AcerSense AI 性能调度 + 玩家行为学习是笔电 AI 应用方向，对平板/手机的 AI 性能调度算法有借鉴意义",
        "vendor": "Acer（宏碁）",
        "model": "Predator Helios Neo 16S AI（2026）",
        "sources": "Acer 官网、Reddit r/GamingLaptops（待印证）",
        "remark": "$1,799 起步；8 月底发货；与联想拯救者 / 华硕 ROG 主流游戏本竞争"
    },
    {
        "id": 8,
        "region": "intl",
        "status": "coming",
        "title": "TCL NXTPAPER Note A1 国际版评测汇总",
        "stars": 3,
        "source": "B",
        "date": "2026-07-15",
        "domain": "平板",
        "url": "https://mightygadget.com/tcl-note-a1-nxtpaper-review",
        "url_label": "Mighty Gadget 评测：TCL Note A1 NXTPAPER",
        "signal_type": "国际版评测汇总",
        "confirm_count": "3+（Mighty Gadget / TechBizWeb / TechDigestDaily）",
        "key_params": "MediaTek Helio G100 八核；11.5\" NXTPAPER Pure 2200×1440 120Hz + 3A 水晶护盾玻璃；8GB RAM + 256GB（无 microSD）；8000mAh + 33W 快充；USB-C + Pogo Pin；13MP 后置（无前置）；8 麦克风阵列；附赠 T-Pen Pro 8192 压感 + 键盘保护套；£515 / 约 ¥4700",
        "tech_features": [
            "NXTPAPER Pure 护眼彩屏，120Hz + 纸感防眩光/防反射/防指纹三层镀膜",
            "T-Pen Pro 主动笔 8192 压感 <5ms 延迟 + X 轴线性马达模拟纸张摩擦感",
            "AI 工具箱：实时离线转写 / 翻译 / 摘要 / 公式识别 / 手写转文字 / 一键图形",
            "Inspiration Space 个人知识中枢：圈选 PDF / 网页 + 标记会议录音 → 自动整理结构化笔记",
            "无前置摄像头设计强化专注力 + USB-C + Pogo Pin 键盘磁吸 + 33W 快充"
        ],
        "why_important": "TCL 在国际版平板市场以 NXTPAPER Pure 替代电子墨水屏切入'阅读 + 笔记 + 多媒体'混合赛道，比传统墨水屏厂商（reMarkable / Boox）更易融入 Android 生态，对平板差异化路线有启示",
        "terminal_relevance": "NXTPAPER 2.0 双模屏的量产与价格曲线对 TCL 平板产品线本身意义重大（自家产品落地）；墨水屏 + 彩屏切换方案对护眼平板设计有参考",
        "vendor": "TCL",
        "model": "NXTPAPER Note A1（型号 9296G）",
        "sources": "TCL Global 官网（待印证）",
        "remark": "€229 起；预计 9 月中欧洲开售；墨水屏 + 彩屏双模方案"
    },
    {
        "id": 9,
        "region": "intl",
        "status": "released",
        "title": "Fairphone 6+ 模块化手机上市",
        "stars": 4,
        "source": "B",
        "date": "2026-08-10",
        "domain": "手机",
        "url": "https://www.fairphone.com/en/the-fairphone-gen-6-plus",
        "url_label": "Fairphone 官方：Fairphone (Gen 6+)",
        "signal_type": "首发上市",
        "confirm_count": "2（Fairphone 官网/NotebookCheck 待印证）",
        "key_params": "Qualcomm Snapdragon 7s Gen 4；6.31\" LTPO AMOLED 120Hz 2640×1216；8GB LPDDR4X + 256GB；50MP 主摄 + 13MP 超广角 + 32MP 前；4415mAh 可拆卸电池 + 33W 有线 + 15W 无线；Android 16 / 8 年系统升级；€649 起",
        "tech_features": [
            "模块化设计：电池/屏幕/USB-C 接口/摄像头均可用户自行更换",
            "8 年软硬件保修（行业最长）+ 12 年零件供应承诺",
            "100% 公平贸易认证钴 + 再生稀土 + Fairtrade 黄金",
            "4415mAh 可拆卸电池，能量密度优化换电体验",
            "维修友好 iFixit 10/10 评分，所有螺丝统一规格"
        ],
        "why_important": "Fairphone 6+ 把模块化 + 8 年保修 + 100% 公平贸易材料三者整合，是欧洲可持续消费电子的代表产品；硅碳电池在 5124mAh 容量的量产应用，对平板/手机的电池路线选择有标杆意义",
        "terminal_relevance": "模块化设计 + 硅碳电池 + 8 年系统升级三者整合，对平板/手机设计哲学（可持续 vs 一次性消费）有启发",
        "vendor": "Fairphone（荷兰）",
        "model": "Fairphone 6+（FP6+）",
        "sources": "Fairphone 官网、欧洲零售商（待印证）",
        "remark": "€649 起；可持续设计标杆；模块化设计维修时间 < 5 分钟"
    },
    {
        "id": 10,
        "region": "intl",
        "status": "released",
        "title": "UGREEN UNO 2-in-1 Qi2 15W 无线充电器带屏版",
        "stars": 3,
        "source": "B",
        "date": "2026-07-20",
        "domain": "无线充",
        "url": "https://www.aufb.com.au/goods/index.html?goods_id=70230",
        "url_label": "AUFB First Blood：UGREEN UNO 2-in-1 Qi2 15W 带屏无线充电器",
        "signal_type": "海外新品上市",
        "confirm_count": "2+（UGREEN 官方渠道 / 澳洲零售商 AUFB）",
        "key_params": "Qi2 认证 15W iPhone 12-17 磁吸快充 + 5W 耳机 + 5W Apple Watch 三合一；N48H 强磁铁吸附；70° 自由角度调节（兼手机支架）；智能屏显示机器人表情反馈充电状态；折叠便携设计 + USB-C to USB-C 1m 线；约 $89 AUD / ¥106 起",
        "tech_features": [
            "Qi2 认证 15W 磁吸无线快充（iPhone 12-17 系列），速度为非认证 7.5W 的 2 倍",
            "三合一充电：15W iPhone + 5W AirPods + 5W Apple Watch 同步互不干扰",
            "智能屏显示'机器人表情'：充电状态可视化（充电 / 充满 / 异常），趣味交互",
            "N48H 强磁铁 + 70° 角度调节兼具手机支架功能",
            "过压 / 过流 / 过热 / 短路四重保护 + 折叠便携设计适合差旅"
        ],
        "why_important": "UGREEN UNO 系列把'机器人表情智能屏 + Qi2 15W + 三合一'整合，把无线充电器从'配角配件'升级为'有交互感的小型桌面设备'，对配件类终端形态演化有参考",
        "terminal_relevance": "无线充 + 小型显示屏 + AI 表情反馈的可组合形态，对手机 / 平板的桌面生态配件产品设计有借鉴意义",
        "vendor": "UGREEN 绿联",
        "model": "UNO 2-in-1 Magnetic Wireless Charger 15W（W709 / 45775）",
        "sources": "UGREEN 官方渠道、AUFB 澳洲零售商、京东国内版",
        "remark": "¥106 起 / $89 AUD；2026 年夏季全球铺货；折叠便携设计"
    },
    {
        "id": 11,
        "region": "intl",
        "status": "released",
        "title": "Polar Vantage V2 高端户外运动表上市",
        "stars": 3,
        "source": "C",
        "date": "2026-08-15",
        "domain": "智能手表",
        "url": "https://www.polar.com/vantage-v2",
        "url_label": "Polar 官方：Vantage V2",
        "signal_type": "新品上市",
        "confirm_count": "1（Polar 官网）",
        "key_params": "1.39\" AMOLED 466×466 1000nit；钛合金表圈 + 蓝宝石玻璃；GPS 双频 L1+L5 + GLONASS/Galileo/QZSS/BeiDou；光学心率 + ECG + 皮温 + 血氧；140+ 运动模式；7 天日常 / 30h GPS / 100h Ultra 续航；预计 ₹83,400（约 $999）/ €899",
        "tech_features": [
            "AMOLED + 钛合金 + 蓝宝石玻璃户外三件套，10ATM 防水",
            "双频 GNSS 全系统 + 离线地图 + 离线音乐 + 离线支付",
            "光学心率 / ECG / 皮温 / 血氧 / 压力 / 睡眠全维健康监测",
            "训练负荷 / 恢复 / 跑步功率 / 越野节奏 / 爬坡得分等专业算法",
            "Elixir 生物传感平台 + Polar Flow 训练生态"
        ],
        "why_important": "Polar Vantage V2 是对 Garmin Fenix 8 / Epix (Gen 2) 的正面竞争，主打\"户外三防 + 训练算法 + 全维健康\"；AMOLED 高亮屏首次下放到 Polar V 旗舰系列",
        "terminal_relevance": "AMOLED + 钛合金 + 蓝宝石 + 双频 GNSS 的户外表 BOM 清单，对平板/手机的户外衍生型号（平板户外三防版）有参考",
        "vendor": "Polar（芬兰）",
        "model": "Vantage V2",
        "sources": "Polar 官网、印度零售商（待印证）",
        "remark": "₹83,400（约 $999）；8 月底发货；与 Garmin / COROS 竞争"
    },
    {
        "id": 12,
        "region": "intl",
        "status": "released",
        "title": "Suunto Race 3 / Race 3 S 旗舰跑表参数曝光",
        "stars": 3,
        "source": "B",
        "date": "2026-07-26",
        "domain": "智能手表",
        "url": "https://www.notebookcheck.net/Suunto-Race-3-and-Race-3-S-smartwatches-leak-with-AMOLED-displays-and-new-subscription.1353072.0.html",
        "url_label": "NotebookCheck 报道：Suunto Race 3 / Race 3 S 双旗舰曝光",
        "signal_type": "官方资料泄露 / 即将发布",
        "confirm_count": "3+（NotebookCheck / Gadgets & Wearables / WatchesReviewed / ChineseSmartwatches）",
        "key_params": "Race 3 S：1.32\" AMOLED + 蓝宝石玻璃 + 双频 GNSS；Race 3：1.5\" AMOLED + 矿物玻璃（控制成本保续航）；双频 GPS 全系统；新一代 Suunto AI Coach（对话式训练建议，3 个月免费后转为订阅付费）；预计 2026 年内先后发布（Race 3 S 先行）",
        "tech_features": [
            "Race 3 S 主打'轻量越野 + 蓝宝石护屏 + 1.32\" AMOLED'，耐用度提升",
            "Race 3 主打'长续航 + 1.5\" AMOLED + 矿物玻璃（成本权衡）'，续航为最大卖点",
            "双频 GNSS 全系统，两款均配备，复杂地形 / 楼宇密集区跑步定位稳定",
            "Suunto AI Coach 新版：可回答'今天该不该练 / 怎样练效率更高 / 睡眠恢复对计划影响'等对话问题，能生成 7km 路线并下发手表",
            "3 个月免费 AI Coach → 之后订阅付费（区别于现免费 Suunto Coach），Suunto 首次转向订阅模式"
        ],
        "why_important": "Suunto Race 3 系列印证了'订阅式 AI 教练'是户外表新趋势（对标 Garmin / COROS）；同时 Race 3 S 的蓝宝石玻璃下放 + Race 3 的矿物玻璃成本权衡，体现了 Suunto 用料分级的产品思路；对智能手表的 AI 订阅化路线有标杆意义",
        "terminal_relevance": "户外表订阅化 + AI 对话式教练为智能穿戴终端'硬件 + 服务双收费'模式提供新案例；对手表 AI 应用层设计有借鉴",
        "vendor": "Suunto（芬兰 / Amer Sports 集团）",
        "model": "Race 3 / Race 3 S",
        "sources": "NotebookCheck、Gadgets & Wearables、WatchesReviewed、ChineseSmartwatches",
        "remark": "参数来自官方页面索引残留与 Reddit 截图，正式发布前仍有调整可能；预计 2026 年内 Race 3 S 先行发布"
    },
    {
        "id": 13,
        "region": "intl",
        "status": "released",
        "title": "REDMAGIC Astra 2 Gaming Tablet 全球预售",
        "stars": 4,
        "source": "B",
        "date": "2026-08-10",
        "domain": "平板",
        "url": "https://na.redmagic.com/products/redmagic-astra-2-gaming-tablet-early-bird-perks",
        "url_label": "REDMAGIC NA：Astra 2 Gaming Tablet Early Bird 官方页",
        "signal_type": "全球预售 + 早鸟价",
        "confirm_count": "3+（REDMAGIC 官方 / gamezebo / techcapsules）",
        "key_params": "Qualcomm Snapdragon 8 Elite Gen 5 + RedCore R4 协处理器；9.06\" 2.4K OLED 185Hz 触控（2000Hz 瞬时采样）+ 1,600nit 峰值；12GB+256GB / 16GB+512GB；8300mAh 双电芯 + 75W 快充 + 双 USB-C 反向充电；前置 9MP / 后置 13MP；IP54 + 双 X 轴马达 + DTS Ultra 立体声；$699 起（早鸟再 -$30）",
        "tech_features": [
            "骁龙 8 Elite Gen 5 + 自研 RedCore R4 游戏芯片（独立 AI 超分 / 帧率调度）",
            "9.06\" 2.4K OLED 185Hz + 2000Hz 瞬时采样率（行业最高之一），TÜV Rheinland 护眼",
            "AquaCore Cooling System 2.0 行业首创液态金属液冷 + 4D VC 均热板 + 压电陶瓷微泵",
            "8300mAh 双电芯 + 双 USB-C 接口，行业首个双向反向充电平板",
            "IP54 防尘防水 + 双 X 轴线性马达 + DTS Ultra 立体声 + 透明后盖 RGB 灯效"
        ],
        "why_important": "Astra 2 是 REDMAGIC 在 9\" OLED 小尺寸游戏平板的迭代，骁龙 8 Elite Gen 5 + 185Hz + 液冷散热重新定义游戏平板性能上限；早鸟 + 全球 8/26 公开销售对标联想 Legion Tab，并以更低定价抢占市场",
        "terminal_relevance": "小尺寸游戏平板 + 高刷 OLED + 主动液冷是平板细分赛道的新爆点；内置 RGB + 反向充电等'桌面游戏机基因'为平板设计提供新思路",
        "vendor": "REDMAGIC（红魔 / 努比亚）",
        "model": "Astra 2 Gaming Tablet（国内：红魔电竞平板 5 Pro）",
        "sources": "REDMAGIC 官方、gamezebo、techcapsules、gaitgames、ingamenews",
        "remark": "早鸟 8/10-8/25 + 8/26 全球开售；12+256GB $699 / 16+512GB $799；附赠 80W 充电器 + 钥匙扣"
    },
    {
        "id": 14,
        "region": "intl",
        "status": "released",
        "title": "联想 Legion Go C700 云游戏掌机即将发布",
        "stars": 3,
        "source": "B",
        "date": "2026-08-21",
        "domain": "笔记本电脑",
        "url": "https://www.163.com/dy/article/L4RD2PAN05561FZD.html",
        "url_label": "网易：联想拯救者 C700 掌机 8/25 发布",
        "signal_type": "新品官宣 + 4 天后发布",
        "confirm_count": "3+（联想官方 / 快科技 / 网易 / gagadget / 今日头条）",
        "key_params": "Android 系统（非 Windows）+ 云游戏 + 本地串流双模式；7.82\" 120Hz IPS LCD 触控；整机 556g / 14.9mm（比传统 Win 掌机轻近 300g）；8000mAh 电池，连续游戏 9h；TMR 摇杆 + 霍尔线性扳机 + 全向 D-Pad + 2 背键 + 2 肩键（全部自定义）；自研 LEGION STREAM 串流协议（实验室 10ms 延迟，1080P/120Hz@RTX 4060）+ 腾讯 START 云游戏合作；8/25 19:00 发布",
        "tech_features": [
            "云游戏掌机新形态：Android 系统 + 不靠本地算力，靠串流（自研 LEGION STREAM）+ 腾讯 START 云游戏",
            "实验室 10ms 端到端 RTT 延迟（拯救者 Y9000P RTX 4060 + 1080P/120Hz），逼近本地运行体验",
            "TMR 磁感应摇杆（避免漂移）+ 霍尔效应线性扳机（精准按压）+ 全向 D-Pad + 2 背键 + 2 肩键全自定义",
            "7.82\" 120Hz IPS LCD + 14.9mm 厚 + 556g 超轻机身（比 Win 掌机轻 300g）",
            "8000mAh 电池 9h 连续游戏 + LEGION STREAM 串流坞一键配对 + 无网直连链路（无 Wi-Fi 也能串流）"
        ],
        "why_important": "联想 Legion Go C700 把'轻量 Android + 云游戏 + 串流'整合为掌机新形态，从传统 Windows 本地算力掌机路线转向'云端算力 + 本地低功耗'，对掌机品类演化有重要参照",
        "terminal_relevance": "Android + 大屏 + 手柄的掌机形态，与平板/手机生态可深度联动（投屏 / 协同）；'低功耗本地 + 云端算力'设计思路对平板/手机的云游戏模式有借鉴",
        "vendor": "Lenovo（联想）",
        "model": "Legion Go C700（云游戏掌机）",
        "sources": "联想官方、快科技、网易、gagadget、今日头条",
        "remark": "8/25 19:00 发布；具体处理器 / 售价 / 海外上市计划待发布；首批深度合作腾讯 START（国内）"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 4, True),       # 隐星/曙光/MSI/RedMagic
    ("显示/OLED", 6, True),       # 隐星/E13/Alldocube/MSI/Acer/Vantage V2/Race 3
    ("折叠屏", 0, False),
    ("手写笔/触控", 4, True),     # ThinkPad E13（IR 触摸）/MSI Flip/Alldocube/RedMagic
    ("散热/液冷", 3, True),       # 隐星水冷/RedMagic风扇/Acer风扇
    ("电池/续航", 6, True),       # Alldocube/Fairphone/Vantage V2/Race 3/RedMagic/Legion Go
    ("快充/无线充", 4, True),     # Fairphone/绿联 Qi2/RedMagic/Legion Go
    ("影像", 2, True),            # Fairphone/MSI
    ("AI/NPU", 4, True),          # ThinkPad E13/MSI/INMO GO3/AcerSense
    ("音频/扬声器", 2, True),     # INMO GO3/Alldocube
    ("5G/通信", 2, True),         # Alldocube 4G/Legion Go Wi-Fi 7
    ("Wi-Fi/连接", 5, True),      # MSI Wi-Fi7/Acer Wi-Fi7/隐星 Wi-Fi6E/E13 Wi-Fi6E/曙光 Wi-Fi6
    ("AR/VR显示", 1, True),       # INMO GO3
    ("材质/工艺", 4, True),       # Alldocube 金属/INMO 铝/Fairphone 模块化/曙光金属
    ("可持续/模块化", 1, True),   # Fairphone
    ("手柄/外设", 2, True),       # RedMagic 触控肩键/Legion Go 可拆卸控制器
]

# ── Top5 重点信号 ──
TOP5 = [
    {
        "rank": 1,
        "title": "七彩虹隐星 P16 Pro 星风水冷版",
        "dim": "散热/液冷",
        "stars": 5,
        "key": "全球首款消费级水冷笔电 + RTX 5060 满血 + 8/28 发售"
    },
    {
        "rank": 2,
        "title": "联想 ThinkPad E13 AI 2026",
        "dim": "AI/NPU",
        "stars": 4,
        "key": "Lunar Lake + 97 TOPS NPU + ¥6,999 国行商务本"
    },
    {
        "rank": 3,
        "title": "INMO GO3 AR 眼镜日本首发",
        "dim": "AR/VR显示",
        "stars": 4,
        "key": "98 语言翻译 + 可换电池 + 58g 镜框"
    },
    {
        "rank": 4,
        "title": "REDMAGIC Astra 2 游戏平板",
        "dim": "散热/液冷",
        "stars": 4,
        "key": "骁龙 8 Elite Gen 5 + 185Hz OLED + 液冷 2.0 + $699"
    },
    {
        "rank": 5,
        "title": "Fairphone 6+ 模块化手机",
        "dim": "可持续/模块化",
        "stars": 4,
        "key": "100% 公平贸易材料 + 8 年保修 + €699"
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

with open("WB_2026-08-21_硬件看板.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML 生成完成：WB_2026-08-21_硬件看板.html")
print(f"   总情报：{total} 条（国内 {cn_count} + 国际 {intl_count}）")
print(f"   维度覆盖：{dim_on}/16")
print(f"   五星条数：{five_star}")