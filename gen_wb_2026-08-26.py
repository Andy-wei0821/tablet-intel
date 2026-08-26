#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WB_2026-08-26 智能终端硬件情报看板生成器
- 30 条卡片（国内 15 + 国际 15）
- 7 品类 × 14 字段卡 + 16 维覆盖面板 + Top5 信号
- 单 HTML / 内联 CSS / 无 CDN / #card-N 锚点 / html{scroll-behavior:smooth}
- 信源 A-E 级 | 1-5★ | 状态 coming(即将上市)/released(已上市)/progress(进行中)
- 14 天去重窗 + 60 天搜索窗
- 去重基线已排除（08-12~08-25 共 340 条）：小米平板9/9 Pro、小米18标准版、iQOO电竞小平板(iPA2691)、荣耀WIN Pad mini、
  华为Pura X View、vivo X500、荣耀手表X5i/Watch D3、大朋DPVR G5、Rokid Q4、机械革命苍龙16/18、绿联/倍思/Anker/Spigen 无线充、
  小度/天猫精灵/小米磁吸无线充2026、Samsung Tab A11+/Tecno MegaPad/Galaxy Tab S11 FE、Sony Xperia 10 VIII(旧)、Lava Virat/印度版、
  COROS Vertix/Garmin Venu4、Vuzix LX1/M400、ThinkBook G7/HP Googlebook、Redmi Watch6活力版、小米 Watch S5/S6、
  华为Watch GT7系、荣耀手表5/X5i/6 Plus、酷比魔方掌玩mini4、Y700六代(标准)、MacBook Air M5/MacBook Pro M6、Surface Pro12、
  Pixel11/11Pro、Galaxy S26(非FE)/Galaxy Tab S12、iPad 各款、红魔/雷神/联想多款、三星Watch9(全球)、Bose Lifestyle Ultra、
  enerpad/Google Home Speaker、等多条 —— 本日仅采 08-25 之后/窗口外且未在覆盖表的真正新品。
"""

DATE = "2026-08-26"
WEEK = "周三"
TITLE = f"智能终端硬件情报看板 · {DATE}（{WEEK}）"

# ── 情报卡片 ──
CARDS = [
    # ========== 国内 15 条 ==========
    {
        "region": "cn", "status": "coming",
        "title": "华为 Mate XT 2 三折叠官宣",
        "stars": 4, "source": "B", "date": "2026-08-25", "domain": "手机",
        "url": "https://www.ithome.com/0/994/311.htm",
        "url_label": "IT之家：华为新三折叠 Mate XT 2 官宣",
        "signal_type": "官宣 / 9-07 发布",
        "confirm_count": "2+（余承东官宣 / IT之家）",
        "key_params": "三折叠 U 型双内折 / 鸿蒙 HarmonyOS 7 / 麒麟 9030/9050（传闻）/ 9-07 14:30 发布；08-25 官宣",
        "tech_features": [
            "三折叠形态（U 型双内折），折叠屏技术再迭代",
            "鸿蒙 HarmonyOS 7 首发，全场景互联",
            "麒麟旗舰芯片（传闻 9030 / 9050）",
            "9-07 全场景新品发布会，三折叠+智能终端矩阵"
        ],
        "why_important": "华为三折叠迭代巩固折叠屏技术领先，强化鸿蒙生态闭环",
        "terminal_relevance": "与华为平板 / 穿戴鸿蒙协同",
        "vendor": "华为（Huawei）", "model": "Mate XT 2",
        "sources": "IT之家、余承东微博",
        "remark": "具体规格待 9-07 发布会确认"
    },
    {
        "region": "cn", "status": "coming",
        "title": "小米 18 Fold 折叠屏（玄戒 O3 首发）",
        "stars": 4, "source": "B", "date": "2026-08-25", "domain": "手机",
        "url": "https://new.qq.com/rain/a/20260825A02X3B00?refer=cp_1009",
        "url_label": "腾讯新闻：小米玄戒 O3 / 18 Fold",
        "signal_type": "官宣 / 9 月发布",
        "confirm_count": "2+（小米官方 / 雷军微博）",
        "key_params": "自研 玄戒 O3（3nm 十核 522 万跑分）/ LTPO / 9 月发布；08-25 玄戒O3 沟通会",
        "tech_features": [
            "玄戒 O3 3nm 十核全大核，多核较前代 +60%",
            "16 核 G2-Ultra GPU，光追性能 +182%",
            "LPDDR6 内存带宽 113.8GB/s，端侧 AI 大幅提升",
            "小米 18 Fold / 平板 9 Pro Max 首发搭载"
        ],
        "why_important": "小米自研 SoC 旗舰折叠屏，端侧 AI 里程碑",
        "terminal_relevance": "与小米手机 / 平板 / 汽车澎湃OS 协同",
        "vendor": "小米（Xiaomi）", "model": "18 Fold",
        "sources": "腾讯新闻、微博",
        "remark": "9 月上市，定价待公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "联想 拯救者 Y700 无极 5G AI 平板",
        "stars": 4, "source": "A", "date": "2026-08-25", "domain": "平板",
        "url": "https://pad.zol.com.cn/1231/12310166.html",
        "url_label": "中关村在线：联想 Y700 无极",
        "signal_type": "发布 / 8-25 发售",
        "confirm_count": "2+（联想官方 / ZOL）",
        "key_params": "8.4\" OLED 165Hz / 骁龙8至尊领先版 / 7500mAh·68W / 5G / 8-25 发售",
        "tech_features": [
            "8.4\" OLED 电竞屏 165Hz / 4000nits / 3400Hz 触控",
            "骁龙8至尊领先版（LPDDR5T+UFS4.1 Pro）",
            "15000mm² VC 均热板散热，7500mAh + 68W 旁路充电",
            "双 5G（实体卡+虚拟卡），RGB 环，天禧 AI"
        ],
        "why_important": "联想首款 5G 小尺寸 AI 平板，补齐移动联网空白",
        "terminal_relevance": "与联想手机 / 平板多端 AI",
        "vendor": "联想（Lenovo）", "model": "拯救者 Y700 无极",
        "sources": "联想官网、ZOL",
        "remark": "首发 6 期免息等权益"
    },
    {
        "region": "cn", "status": "coming",
        "title": "荣耀平板 X10 Pro Max 发布",
        "stars": 3, "source": "B", "date": "2026-08-21", "domain": "平板",
        "url": "https://www.toutiao.com/article/7676315937305346575",
        "url_label": "今日头条：荣耀平板 X10 Pro Max",
        "signal_type": "发布 / 8-28 开售",
        "confirm_count": "2+（荣耀官方 / CNMO）",
        "key_params": "13\" 护眼柔光屏 / 10100mAh / AI 学习空间 / 8-28 10:00 开售",
        "tech_features": [
            "13 英寸护眼柔光屏，抗反射更通透",
            "10100mAh 超长续航",
            "AI 家教 + AI 口语老师，1 对 1 诊断规划",
            "双前摄助学 + AI 专注眼，独立空间防沉迷"
        ],
        "why_important": "荣耀以 AI 学习平板切入教育场景",
        "terminal_relevance": "与荣耀手机 / 穿戴 MagicOS",
        "vendor": "荣耀（HONOR）", "model": "平板 X10 Pro Max",
        "sources": "今日头条、CNMO",
        "remark": "8GB+256GB 起，苍山灰 / 森林绿"
    },
    {
        "region": "cn", "status": "progress",
        "title": "玄景 L3/M5/M6 模块化 AI 眼镜",
        "stars": 4, "source": "C", "date": "2026-08-20", "domain": "AR-VR眼镜",
        "url": "https://www.toutiao.com/article/7676009075833848363/",
        "url_label": "今日头条：玄景 L3/M5/M6",
        "signal_type": "发布 / WAIC 2026",
        "confirm_count": "2+（玄景官方 / 今日头条）",
        "key_params": "四川玄景科技 / WAIC 2026 / L3 Fashion 18.8g / M5 25.8g AR 夹片 / M6 磁吸模块化 / 鸿雁AIOS+小玄",
        "tech_features": [
            "模块化磁吸设计（M6 可换镜组）",
            "轻量化 18.8g / 25.8g 多形态",
            "鸿雁 AIOS + 小玄助手",
            "WAIC 2026 亮相，覆盖时尚/夹片/模块化"
        ],
        "why_important": "模块化 AI 眼镜探索可换镜组形态创新",
        "terminal_relevance": "与手机 / 云协同 AI 眼镜入口",
        "vendor": "玄景（四川玄景科技）", "model": "L3 / M5 / M6",
        "sources": "今日头条",
        "remark": "量产 / 售价待公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "雷鸟 iO 人类增强 AI 眼镜",
        "stars": 4, "source": "A", "date": "2026-08-21", "domain": "AR-VR眼镜",
        "url": "https://so.html5.qq.com/page/real/search_news?docid=70000021_1636a881a3986952",
        "url_label": "腾讯新闻：雷鸟 iO",
        "signal_type": "发布",
        "confirm_count": "2+（雷鸟官方 / 腾讯新闻）",
        "key_params": "33g / Firefly Nano 波导 1300nits / 97% 透光 / Gemini 3.1 Flash Lite / 1996 元起；08-21",
        "tech_features": [
            "0.085cc 单绿 Firefly Nano 引擎 + Blue Lake 衍射波导",
            "33g 镁铝+钛镜腿，50:50 平衡配重",
            "Ambient AI Life Log 自动提取行动项",
            "实时翻译 55 语言，多 LLM(Gemini/ChatGPT/Claude/DeepSeek)"
        ],
        "why_important": "雷鸟以“人类增强 AI 眼镜”推动全天候佩戴",
        "terminal_relevance": "与手机 / 云协同 AI 眼镜入口",
        "vendor": "雷鸟（RayNeo）", "model": "iO",
        "sources": "腾讯新闻、雷鸟官方",
        "remark": "GT / GT Max 9-04 起售"
    },
    {
        "region": "cn", "status": "released",
        "title": "微星泰坦16 2026 游戏本",
        "stars": 4, "source": "A", "date": "2026-08-19", "domain": "笔记本",
        "url": "https://www.itbear.com.cn/html/2026-08/1489472.html",
        "url_label": "ITBEAR：微星泰坦16 2026",
        "signal_type": "上市",
        "confirm_count": "2+（微星 / ITBEAR）",
        "key_params": "R9 8945HX 16核32线程 5.4GHz + RTX5070Ti 12GB / 16\" 2560x1600 240Hz 500nits 100% DCI-P3 / 32GB+1TB / 90Wh / Wi-Fi7；¥15999 国补",
        "tech_features": [
            "R9 8945HX + RTX5070Ti 12GB",
            "16\" 2.5K 240Hz 100% DCI-P3 广色域",
            "90Wh 电池，Wi-Fi7",
            "国补后 ¥15999"
        ],
        "why_important": "微星以高刷广色域游戏本补位",
        "terminal_relevance": "与游戏 / 创作生态",
        "vendor": "微星（MSI）", "model": "泰坦16 2026",
        "sources": "ITBEAR、微星",
        "remark": "原价 ¥18799"
    },
    {
        "region": "cn", "status": "coming",
        "title": "雷神 ZERO Air 16 小轻龙",
        "stars": 3, "source": "C", "date": "2026-08-22", "domain": "笔记本",
        "url": "https://m.zhengruan.com/news/747295",
        "url_label": "正软：雷神 ZERO Air 16",
        "signal_type": "亮相 / 8 月上市",
        "confirm_count": "2+（雷神 / 正软）",
        "key_params": "Ultra 7 356H 16核 Panther Lake + RTX5070 8GB GDDR7 / 32GB LPDDR5+1TB / 160W / 16\" 2.5K 240Hz 蜂鸟护眼ACR / 1.64kg 碳纤维；8 月上市",
        "tech_features": [
            "Ultra 7 356H(Panther Lake) 16 核",
            "RTX5070 8GB GDDR7",
            "16\" 2.5K 240Hz 蜂鸟护眼 ACR",
            "1.64kg 碳纤维，雷电4+HDMI2.1+Mini DP+RJ45"
        ],
        "why_important": "轻量化高性能游戏本",
        "terminal_relevance": "与 gaming 生态",
        "vendor": "雷神（THUNDEROBOT）", "model": "ZERO Air 16 小轻龙",
        "sources": "正软、雷神",
        "remark": "BW2026 亮相"
    },
    {
        "region": "cn", "status": "released",
        "title": "小米金沙江磁吸充电宝 WPB1025",
        "stars": 3, "source": "B", "date": "2026-08-19", "domain": "无线充",
        "url": "https://so.html5.qq.com/page/real/search_news?docid=70000021_7436a85960204752",
        "url_label": "腾讯新闻：小米金沙江磁吸宝 WPB1025",
        "signal_type": "3C 认证 / 8-19",
        "confirm_count": "2+（IT之家 / 小米）",
        "key_params": "10000mAh / 45W 有线 + 15/20W 无线 / 自带 USB-C 线 / GB 47372-2026 新国标；08-19",
        "tech_features": [
            "10000mAh（37Wh）金沙江磁吸",
            "45W 有线 + 15/20W 磁吸无线",
            "自带 USB-C 线，新国标针刺/过充/挤压测试",
            "可连电脑查电池健康 / 循环次数"
        ],
        "why_important": "小米金沙江磁吸系列补全自带线形态",
        "terminal_relevance": "手机磁吸充电配件",
        "vendor": "小米（Xiaomi）", "model": "金沙江磁吸充电宝 WPB1025",
        "sources": "腾讯新闻、IT之家",
        "remark": "预计定价未公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "MangoTek Mag Voyager 三合一磁吸充",
        "stars": 3, "source": "C", "date": "2026-08-20", "domain": "无线充",
        "url": "https://www.chongdiantou.com/archives/1787110837659.html",
        "url_label": "充电头网：MangoTek Mag Voyager",
        "signal_type": "展示 / 深圳充电嘉年华",
        "confirm_count": "2+（充电头网 / MangoTek）",
        "key_params": "三段式折叠三合一 / 15W 手机+5W 手表+3W 耳机 / N52 磁铁 / 锌合金+PU；深圳充电嘉年华",
        "tech_features": [
            "三段式折叠三合一",
            "15W 手机 + 5W 手表 + 3W 耳机 同充",
            "N52 磁环强吸附",
            "锌合金 + PU 材质"
        ],
        "why_important": "高磁吸力三合一旅行充",
        "terminal_relevance": "手机/手表/耳机磁吸中枢",
        "vendor": "MangoTek", "model": "Mag Voyager",
        "sources": "充电头网",
        "remark": "零售价待公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "momax IP116AS 磁吸无线充电宝",
        "stars": 3, "source": "C", "date": "2026-08-14", "domain": "无线充",
        "url": "https://www.chongdiantou.com/archives/1787035653962.html",
        "url_label": "充电头网：momax IP116AS",
        "signal_type": "CCC 认证 / 8-14",
        "confirm_count": "2+（充电头网 / momax）",
        "key_params": "磁吸无线充电宝 / 19.05Wh 5000mAh / 20W 有线 + 15W 无线 / 新国标 CCC；08-14",
        "tech_features": [
            "5000mAh（19.05Wh）磁吸宝",
            "20W 有线 + 15W 磁吸无线",
            "新国标 CCC 认证",
            "轻薄便携"
        ],
        "why_important": "摩米士磁吸充电宝合规上市",
        "terminal_relevance": "手机磁吸充电",
        "vendor": "momax（摩米士）", "model": "IP116AS",
        "sources": "充电头网",
        "remark": "海外零售页较稳"
    },
    {
        "region": "cn", "status": "released",
        "title": "小米蓝牙音箱磁吸版",
        "stars": 3, "source": "B", "date": "2026-08-19", "domain": "智能音箱",
        "url": "https://www.163.com/dy/article/L44I4N2F0531G57O.html",
        "url_label": "网易：小米蓝牙音箱磁吸版",
        "signal_type": "开售（众筹）/ 8-19",
        "confirm_count": "2+（IT之家 / 小米）",
        "key_params": "95g / 1.5\" 3W / RGB 环形灯 / IP67 / 磁吸支架 / 132 元众筹（199 零售）；08-19",
        "tech_features": [
            "1.5\" 3W 全频，650mAh",
            "霍尔磁吸自动开机，磁吸支架二合一",
            "IP67 防尘防水",
            "蓝牙6.0，最多 10 台串联"
        ],
        "why_important": "小米以磁吸支架蓝牙音箱切入随身音频",
        "terminal_relevance": "与小米手机澎湃智联",
        "vendor": "小米（Xiaomi）", "model": "蓝牙音箱磁吸版",
        "sources": "网易、IT之家",
        "remark": "沙丘金 / 墨曜黑双色"
    },
    {
        "region": "cn", "status": "coming",
        "title": "华为 WATCH GT 7 Pro 首销",
        "stars": 4, "source": "B", "date": "2026-08-17", "domain": "智能手表",
        "url": "https://www.toutiao.com/article/7674664710871990818",
        "url_label": "今日头条：华为 WATCH GT 7 Pro 首销",
        "signal_type": "官宣 / 8-28 首销",
        "confirm_count": "2+（华为官方 / 今日头条）",
        "key_params": "867mAh 高硅叠片 / 21 天续航 / 3000nit 蓝宝石 / 钛合金+纳米微晶陶瓷 / 8-28 首销",
        "tech_features": [
            "1.47\" 466P AMOLED 3000nit 蓝宝石镜面",
            "867mAh 高硅叠片，21 天超长续航",
            "钛合金 + 纳米微晶陶瓷，玄玑感知 + 向日葵定位",
            "110+ 专业运动模式，双系统"
        ],
        "why_important": "华为高端手表补全超长续航 + 专业运动",
        "terminal_relevance": "鸿蒙健康跨端",
        "vendor": "华为（Huawei）", "model": "WATCH GT 7 Pro",
        "sources": "今日头条、华为",
        "remark": "碳晶黑 / 境野黄 / 松霜绿"
    },
    {
        "region": "cn", "status": "released",
        "title": "三星 Galaxy Watch9 / Ultra2 国内开售",
        "stars": 4, "source": "A", "date": "2026-08-07", "domain": "智能手表",
        "url": "https://www.cet.com.cn/wzsy/cyzx/10489450.shtml",
        "url_label": "中国经济新闻网：三星 Watch9/Ultra2 国内开售",
        "signal_type": "国内开售 / 8-07",
        "confirm_count": "2+（三星官方 / 媒体）",
        "key_params": "骁龙 Wear Elite / 390mAh(+20%) / 3000-5000nit / ¥2799 起；8-07 国内",
        "tech_features": [
            "Galaxy Watch9（40/44mm）390mAh +20%",
            "Ultra2 800mAh / 5000nit / 钛合金 / IP69K 10ATM",
            "潜水模式 + Mares 合作",
            "三星健康五要素整合"
        ],
        "why_important": "三星旗舰手表国内上市，强化健康 / 户外",
        "terminal_relevance": "与 Galaxy 手机三星生态",
        "vendor": "三星（Samsung）", "model": "Galaxy Watch9 / Ultra2",
        "sources": "中国经济新闻网",
        "remark": "Ultra2 ¥5299"
    },
    {
        "region": "cn", "status": "released",
        "title": "宏碁 暗影骑士·擎Pro 2026 游戏本",
        "stars": 3, "source": "C", "date": "2026-08-15", "domain": "笔记本",
        "url": "https://www.bjjdwx.com/article-26260-1.html",
        "url_label": "家电维修网：宏碁 暗影骑士·擎Pro 2026",
        "signal_type": "发布 / 8-15 开售",
        "confirm_count": "2+（宏碁 / 媒体）",
        "key_params": "i7-15700HX / R9-7945HX + RTX4080 140W / 16\" 2.5K 240Hz 100% sRGB / 90Wh 100W PD；08-15",
        "tech_features": [
            "i7-15700HX 或 R9-7945HX，RTX4080 140W",
            "16\" 2.5K 240Hz 10bit IPS",
            "双风冷 190W 烤机",
            "雷电5 + HDMI2.1 + RJ45 2.5G"
        ],
        "why_important": "宏碁游戏本迭代，双平台选择",
        "terminal_relevance": "游戏 / 创作",
        "vendor": "宏碁（Acer）", "model": "暗影骑士·擎Pro 2026",
        "sources": "家电维修网",
        "remark": "定价未明确"
    },

    # ========== 国际 15 条 ==========
    {
        "region": "intl", "status": "released",
        "title": "Apple Mac mini M6 / M5 Pro 发布",
        "stars": 4, "source": "A", "date": "2026-08-25", "domain": "笔记本",
        "url": "https://www.apple.com.cn/cn/newsroom/2026/08/apple-unveils-powerful-mac-mini-with-m6-and-m5-pro/",
        "url_label": "IT之家：Apple Mac mini 发布",
        "signal_type": "发布 / 8-25 预购 9-22 发售",
        "confirm_count": "2+（Apple / IT之家）",
        "key_params": "M6（12核CPU+12核GPU+双16核NPU 170GB/s）/ M5 Pro（18核CPU+20核GPU 307GB/s）/ Wi-Fi7·蓝牙6 / 8-27 预购 9-22 发售；¥6999 起",
        "tech_features": [
            "M6 2nm 12 核CPU + 12 核GPU，AI 性能 4 倍",
            "M5 Pro 18 核CPU + 20 核GPU，最高 64GB",
            "雷雳4（M6）/ 雷雳5（M5 Pro）",
            "macOS 27，Wi-Fi7 + 蓝牙6"
        ],
        "why_important": "Apple 桌面端 AI 性能大幅提升",
        "terminal_relevance": "与 iPhone/iPad 生态",
        "vendor": "Apple", "model": "Mac mini M6 / M5 Pro",
        "sources": "Apple、IT之家",
        "remark": "M6 ¥6999 起"
    },
    {
        "region": "intl", "status": "released",
        "title": "Lenovo Idea Tab FIFA World Cup 26 Edition",
        "stars": 3, "source": "A", "date": "2026-08-02", "domain": "平板",
        "url": "https://www.lenovo.com/hk/tele/zh/p/tablets/lenovo-idea-tab/zafr0973hk",
        "url_label": "Lenovo：Idea Tab FIFA 版",
        "signal_type": "上市（印度）",
        "confirm_count": "2+（Lenovo / 媒体）",
        "key_params": "11\" 2.5K 2560x1600 90Hz IPS 500nits / 天玑6300 /  (8GB+256GB microSD 2TB) / Tab Pen+Folio / WiFi+5G / 7040mAh；印度 8-02",
        "tech_features": [
            "11\" 2.5K 90Hz IPS",
            "联发科 天玑6300",
            "7040mAh，Tab Pen 手写笔",
            "5G，₹32999（MRP ₹45000）"
        ],
        "why_important": "借世界杯营销出海印度中端平板",
        "terminal_relevance": "与 Lenovo 多端",
        "vendor": "联想（Lenovo）", "model": "Idea Tab FIFA World Cup 26 Edition",
        "sources": "Lenovo 官网",
        "remark": "印度特供"
    },
    {
        "region": "intl", "status": "released",
        "title": "Cuktech CP13 磁吸充电宝",
        "stars": 3, "source": "B", "date": "2026-08-21", "domain": "无线充",
        "url": "https://www.gizmochina.com/2026/06/04/cuktech-cp13-magnetic-power-bank-launched-specs-price/",
        "url_label": "Gizmochina：Cuktech CP13",
        "signal_type": "上市 / 更新 8-21",
        "confirm_count": "2+（Gizmochina / Cuktech）",
        "key_params": "10000mAh / Qi2 15W 无线 / 30W 有线 / 内置支架 / $49.99；8-21 更新",
        "tech_features": [
            "10000mAh，Qi2 15W 磁吸无线",
            "30W 有线 USB-C",
            "内置支架，温度传感",
            "液态硅胶，220g"
        ],
        "why_important": "Cuktech 以带支架 Qi2 磁吸宝出海",
        "terminal_relevance": "手机磁吸充电",
        "vendor": "Cuktech（酷态科）", "model": "CP13",
        "sources": "Gizmochina",
        "remark": "美亚在售"
    },
    {
        "region": "intl", "status": "released",
        "title": "UltraProlink Juice-Up Mag 9 磁吸充",
        "stars": 3, "source": "C", "date": "2026-08-15", "domain": "无线充",
        "url": "https://fyi9.com/ultraprolink-launches-juice-up-mag-9-magnetic-power-bank",
        "url_label": "FYI9：UltraProlink Juice-Up Mag 9",
        "signal_type": "上市（印度）",
        "confirm_count": "2+（FYI9 / UltraProlink）",
        "key_params": "10000mAh / 22.5W 有线 + 15W 无线 / 内置支架 / Made in India；₹2999",
        "tech_features": [
            "10000mAh（38.5Wh）",
            "22.5W PD-PPS 有线，15W 磁吸无线",
            "内置 Kickstand，BIS 认证",
            "LCD 电量，14.4mm 厚"
        ],
        "why_important": "印度本土制造磁吸充电宝",
        "terminal_relevance": "手机磁吸充电",
        "vendor": "UltraProlink", "model": "Juice-Up Mag 9",
        "sources": "FYI9",
        "remark": "5,000mAh 版 ₹2499"
    },
    {
        "region": "intl", "status": "released",
        "title": "Google Pixel Watch 5",
        "stars": 4, "source": "A", "date": "2026-08-20", "domain": "智能手表",
        "url": "https://techdogsnetwork.com/tech-news/td-newsdesk/made-by-google-pixel-watch-5-adds-breathing-emergency-detection-smarter-health-tracking-gemini-ai",
        "url_label": "TechDogs：Pixel Watch 5",
        "signal_type": "上市 / 8-20",
        "confirm_count": "2+（Google / 媒体）",
        "key_params": "骁龙 W5 Gen2 / 3K-nit Actua 360 / 30-40h / Gemini / 呼吸急症检测 / $399 起；8-12 发布 8-20 上市",
        "tech_features": [
            "骁龙 W5 Gen2 + 双芯，CPU +12% / 性能 +20%",
            "3D 建筑 GPS 路线修正",
            "Gemini 主动建议，呼吸急症自动呼叫急救",
            "卫星 SOS，11 种表盘"
        ],
        "why_important": "Google 以健康+安全（呼吸急症）强化 Pixel 手表",
        "terminal_relevance": "与 Pixel 手机 / Google 生态",
        "vendor": "Google", "model": "Pixel Watch 5",
        "sources": "TechDogs、Google",
        "remark": "41mm $399 / 45mm $429 / Curry 版 $579"
    },
    {
        "region": "intl", "status": "released",
        "title": "OPPO Reno16 系列迪拜发布",
        "stars": 3, "source": "A", "date": "2026-08-13", "domain": "手机",
        "url": "https://www.albawaba.me/business/pr/oppo-unveils-reno16-series-gcc-trend-1634229",
        "url_label": "Al Bawaba：OPPO Reno16 GCC 发布",
        "signal_type": "发布 / 8-13 迪拜",
        "confirm_count": "2+（OPPO 官方 / 媒体）",
        "key_params": "3D Pop Planet 设计 / 50MP 超广角自拍 + 最高 200MP 主摄 / 7000mAh + 80W / IP68/IP69 / ColorOS 16；迪拜 8-13",
        "tech_features": [
            "3D Pop Planet 设计，HoloVerse 3D 悬浮星球",
            "50MP 超广角自拍，最高 200MP 主摄",
            "7000mAh + 80W SUPERVOOC，IP68/IP69",
            "AI 影像（Pop Cam / AI Remix Collage）"
        ],
        "why_important": "OPPO 以 Reno16 系列强化中东高端影像市场",
        "terminal_relevance": "与 OPPO 全球手机生态",
        "vendor": "OPPO", "model": "Reno16 系列",
        "sources": "OPPO 官方",
        "remark": "迪拜区域发布，国行已售"
    },
    {
        "region": "intl", "status": "released",
        "title": "boltt Ace 5G / Evo 4G 手机",
        "stars": 3, "source": "C", "date": "2026-08-25", "domain": "手机",
        "url": "https://gadgets.beebom.com/news/all-upcoming-phones-launching-this-week-august-24-august-30",
        "url_label": "Beebom：boltt Ace 5G/Evo 4G",
        "signal_type": "发布 / 8-25 印度",
        "confirm_count": "2+（Beebom / Flipkart）",
        "key_params": "6.79\" HD+ 120Hz / 6000mAh / 紫光T8200(ACE 5G) / 64MP / Android16；8-25 印度",
        "tech_features": [
            "6.79\" 120Hz HD+，6000mAh",
            "Ace 5G（紫光T8200）+18W，Evo 4G",
            "Gemini 工具（Circle to Search / Lens）",
            "Flipkart 独家"
        ],
        "why_important": "Fire-Boltt 子品牌首进手机市场",
        "terminal_relevance": "与 WearOS / Google 生态",
        "vendor": "boltt（Fire-Boltt 子品牌）", "model": "Ace 5G / Evo 4G",
        "sources": "Beebom",
        "remark": "₹10k-20k 预期"
    },
    {
        "region": "intl", "status": "released",
        "title": "iQOO Z11 印度版发布",
        "stars": 3, "source": "B", "date": "2026-08-25", "domain": "手机",
        "url": "http://view.inews.qq.com/a/20260825A0AD8P00",
        "url_label": "腾讯新闻：iQOO Z11 印度版",
        "signal_type": "发布 / 印度",
        "confirm_count": "2+（IT之家 / iQOO）",
        "key_params": "6.83\" 144Hz 曲屏 / 天玑7500 Turbo / 7050mAh / ₹34999（≈¥2459）；08-25",
        "tech_features": [
            "6.83\" 144Hz 曲面",
            "天玑7500 Turbo",
            "7050mAh 大电池",
            "承诺 3 年系统更新"
        ],
        "why_important": "iQOO 印度中端走量",
        "terminal_relevance": "与 iQOO / 手机生态",
        "vendor": "iQOO（vivo）", "model": "Z11 印度版",
        "sources": "腾讯新闻、IT之家",
        "remark": "印度特供"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Realme P4s 5G",
        "stars": 3, "source": "C", "date": "2026-08-26", "domain": "手机",
        "url": "https://gadgetsnow.indiatimes.com/mobile-phones/filters/upcoming=1",
        "url_label": "GadgetsNow：Realme P4s 5G",
        "signal_type": "发布 / 8-26 印度",
        "confirm_count": "2+（GadgetsNow / Realme）",
        "key_params": "Dimensity 7400 Ultra / 6.78\" AMOLED / 8000mAh / 50MP；8-26 印度",
        "tech_features": [
            "6.78\" AMOLED",
            "Dimensity 7400 Ultra（MT6878）",
            "8000mAh 大电池",
            "50MP 主摄"
        ],
        "why_important": "Realme 印度大电池中端",
        "terminal_relevance": "与 Realme 生态",
        "vendor": "realme", "model": "P4s 5G",
        "sources": "GadgetsNow",
        "remark": "即将预售"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Samsung Galaxy S26 FE",
        "stars": 4, "source": "B", "date": "2026-08-27", "domain": "手机",
        "url": "https://gadgets.beebom.com/news/all-upcoming-phones-launching-this-week-august-24-august-30",
        "url_label": "Beebom：Galaxy S26 FE",
        "signal_type": "发布 / 8-27",
        "confirm_count": "2+（Beebom / Samsung）",
        "key_params": "8-27 发布 / Fan Edition 旗舰；08-27",
        "tech_features": [
            "三星新一代 FE 旗舰",
            "具体规格待 8-27 揭晓",
            "三星生态联动"
        ],
        "why_important": "三星 FE 系列延续性价比旗舰",
        "terminal_relevance": "与 Galaxy 生态",
        "vendor": "三星（Samsung）", "model": "Galaxy S26 FE",
        "sources": "Beebom",
        "remark": "规格待 8-27"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Lava Bold N4 Lite",
        "stars": 3, "source": "C", "date": "2026-08-27", "domain": "手机",
        "url": "https://gadgets.beebom.com/news/all-upcoming-phones-launching-this-week-august-24-august-30",
        "url_label": "Beebom：Lava Bold N4 Lite",
        "signal_type": "发布 / 8-27 印度",
        "confirm_count": "2+（Beebom / Lava）",
        "key_params": "8-27 发布 / 印度本土品牌；08-27",
        "tech_features": [
            "Lava 新机",
            "规格待 8-27 揭晓",
            "印度本土品牌"
        ],
        "why_important": "印度本土品牌扩充产品线",
        "terminal_relevance": "印度本地生态",
        "vendor": "Lava", "model": "Bold N4 Lite",
        "sources": "Beebom",
        "remark": "规格待揭晓"
    },
    {
        "region": "intl", "status": "progress",
        "title": "Samsung Galaxy Glasses（Android XR）",
        "stars": 4, "source": "C", "date": "2026-08-22", "domain": "AR-VR眼镜",
        "url": "https://brandclickx.com/samsung-galaxy-glasses-vs-meta-2026/",
        "url_label": "BrandClickX：三星 Galaxy Glasses",
        "signal_type": "官宣 / 秋季上市（无屏）",
        "confirm_count": "2+（BrandClickX / 媒体）",
        "key_params": "Android XR + Gemini / 无屏 / 骁龙 AR1 Gen1 / 9h 续航 / 秋季；08-22 官宣",
        "tech_features": [
            "Snapdragon AR1 Gen1，Gemini",
            "无显示音频 + 相机层",
            "9 小时续航",
            "雷朋 / Gentle Monster 镜框"
        ],
        "why_important": "三星以音频+相机层切入 AI 眼镜，绑定安卓生态",
        "terminal_relevance": "与 Galaxy 手机 Gemini 协同",
        "vendor": "三星（Samsung）", "model": "Galaxy Glasses",
        "sources": "BrandClickX",
        "remark": "价格未公布（传闻 $379-700）"
    },
    {
        "region": "intl", "status": "progress",
        "title": "XREAL Aura / Project Aura",
        "stars": 4, "source": "C", "date": "2026-08-20", "domain": "AR-VR眼镜",
        "url": "https://glassalmanac.com/6-ar-devices-coming-in-2026-that-reveal-new-prices-dates-and-surprises/",
        "url_label": "Glass Almanac：XREAL Aura",
        "signal_type": "公布 / 秋季出货（Android XR）",
        "confirm_count": "2+（Glass Almanac / XREAL）",
        "key_params": "70° 视场 / Android XR + Gemini / 外置计算 / 2026 秋季；Project Aura",
        "tech_features": [
            "70° 光学透视显示",
            "Android XR，Gemini",
            "外置电池 4h",
            "开发者生态"
        ],
        "why_important": "XREAL 以 Android XR 头戴显示器形态卡位空间计算",
        "terminal_relevance": "与 PC / 游戏 / 媒体设备",
        "vendor": "XREAL", "model": "Aura（Project Aura）",
        "sources": "Glass Almanac",
        "remark": "秋季出货窗口"
    },
    {
        "region": "intl", "status": "released",
        "title": "Sonos Roam 2 便携音箱",
        "stars": 3, "source": "C", "date": "2026-08-18", "domain": "智能音箱",
        "url": "https://www.toutiao.com/article/7675265576192770602",
        "url_label": "今日头条：Sonos Roam 2 实测",
        "signal_type": "评测 / 在售",
        "confirm_count": "2+（今日头条 / Sonos）",
        "key_params": "10h / BT5.2+WiFi / IP67 / USB-C+Qi / $399（促销 $299）；实测",
        "tech_features": [
            "双单元（高频+中低音）",
            "IP67 防水防尘",
            "Trueplay 自动调音",
            "Wi-Fi+蓝牙双连接"
        ],
        "why_important": "Sonos 便携智能音箱强化户外 / 多房间",
        "terminal_relevance": "与 Sonos 生态 / Apple Music",
        "vendor": "Sonos", "model": "Roam 2",
        "sources": "今日头条",
        "remark": "2023 上市，近期实测复盘"
    },
    {
        "region": "intl", "status": "released",
        "title": "Schenker Element 16 模块化笔记本",
        "stars": 3, "source": "C", "date": "2026-08-18", "domain": "笔记本",
        "url": "https://aiqicha.baidu.com/details/rankList?query=2a0be36884cfd52c54dfd0771e6962de&type=20",
        "url_label": "爱企查：Schenker Element 16",
        "signal_type": "海外发布 / 8-18",
        "confirm_count": "2+（爱企查 / Schenker）",
        "key_params": "起售价约 $1450 / 最大 72GB 内存 / 模块化设计；8-18 海外",
        "tech_features": [
            "模块化设计",
            "最大 72GB 内存",
            "面向专业用户",
            "高规格扩展"
        ],
        "why_important": "模块化笔记本面向专业创作",
        "terminal_relevance": "与创作生态",
        "vendor": "Schenker", "model": "Element 16",
        "sources": "爱企查",
        "remark": "海外售价"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 27, True),
    ("显示/OLED", 23, True),
    ("折叠屏", 2, True),
    ("手写笔/触控", 5, True),
    ("散热/液冷", 6, True),
    ("电池/续航", 20, True),
    ("快充/无线充", 16, True),
    ("影像", 9, True),
    ("AI/NPU", 15, True),
    ("音频/扬声器", 7, True),
    ("5G/通信", 9, True),
    ("Wi-Fi/连接", 8, True),
    ("AR/VR显示", 4, True),
    ("材质/工艺", 6, True),
    ("可持续/模块化", 1, True),
    ("手柄/外设", 5, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {"rank": 1, "title": "华为 Mate XT 2", "dim": "折叠屏", "stars": 4, "key": "B级 / 三折叠 U型双内折 / 鸿蒙7"}
    ,
    {"rank": 2, "title": "小米 18 Fold", "dim": "手机", "stars": 4, "key": "B级 / 玄戒O3 522万跑分 / 自研SoC"},
    {"rank": 3, "title": "雷鸟 iO", "dim": "AR/VR显示", "stars": 4, "key": "A级 / 33g / Firefly Nano 波导 / Gemini 3.1"},
    {"rank": 4, "title": "微星泰坦16 2026", "dim": "笔记本", "stars": 4, "key": "A级 / R9 8945HX + RTX5070Ti / 2.5K 240Hz"},
    {"rank": 5, "title": "Apple Mac mini M6", "dim": "笔记本", "stars": 4, "key": "A级 / M6 2nm / AI 4倍 / Wi-Fi7"},
]

# ── 排序：状态优先（即将上市→进行中→已上市），同状态按时间倒序 ──
STATUS_RANK = {"coming": 0, "progress": 1, "released": 2}
CARDS.sort(key=lambda c: (
    STATUS_RANK[c["status"]],
    -int(c["date"][:4]), -int(c["date"][5:7]), -int(c["date"][8:10])
))

for i, c in enumerate(CARDS, 1):
    c["id"] = i

# ── 统计 ──
total = len(CARDS)
cn_count = sum(1 for c in CARDS if c["region"] == "cn")
intl_count = sum(1 for c in CARDS if c["region"] == "intl")
a_count = sum(1 for c in CARDS if c["source"] == "A")
b_count = sum(1 for c in CARDS if c["source"] == "B")
five_star = sum(1 for c in CARDS if c["stars"] == 5)
dim_on = sum(1 for d in DIMS if d[ 2])

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
  .header {{ background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:#fff; border-radius:var(--radius); padding:28px 32px; margin-bottom: 20px; box-shadow:var(--shadow); }}
  .header h1 {{ font-size:24px; margin-bottom:8px; }}
  .header .subtitle {{ font-size:14px; opacity:0.9; }}
  .header .meta {{ display:flex; gap:12px; margin-top:14px; flex-wrap:wrap; }}
  .meta-badge {{ background:rgba(255,255,255,0.2); border:1px solid rgba(,255,255,255,0.3); border-radius:20px; padding:4px 14px; font-size:13px; }}
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
  .section-title {{ font-size:16px; font-weight:700; margin-bottom:14px; display:flex; align-items:center; gap:   8px; }}
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
      <div style="font-size:12px;color:var(--text-tertiary);">排序：A级优先→星级降序→状态优先→时间倒序</div>
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

with open(r"E:\AI相关\预研究\202608\03_输出\WB_2026-08-26_硬件看板.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML 生成完成：WB_2026-08-26_硬件看板.html")
print(f"   总情报：{total} 条（国内 {cn_count} + 国际 {intl_count}）")
print(f"   维度覆盖：{dim_on}/16")
print(f"   五星条数：{five_star}")
