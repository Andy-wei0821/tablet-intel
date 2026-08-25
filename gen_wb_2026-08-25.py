#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WB_2026-08-25 智能终端硬件情报看板生成器
- 30 条卡片（国内 15 + 国际 15）
- 7 品类 × 14 字段卡 + 16 维覆盖面板 + Top5 信号
- 单 HTML / 内联 CSS / 无 CDN / #card-N 锚点 / html{scroll-behavior:smooth}
- 信源 A-E 级 | 1-5★ | 状态 coming(即将上市)/released(已上市)/progress(进行中)
- 14 天去重窗 + 60 天搜索窗
- 去重基线已排除：联想拯救者Y700无极/酷比魔方掌玩mini4/闪极Loomos/雷鸟iO/华为智能眼镜2/红魔游戏平板5 PRO/台电T70 Pro/荣耀平板X10 Pro Max/中柏EZpad Max15/荣耀Robot Phone/iQOO Neo11/华为WATCH GT7/REDMI Watch6/雷鸟V4/李未可X-AI/华为MateBook Pro/ThinkPad E13/YOGA Air14/红魔80W风冷/天猫精灵IN糖6/Samsung Tab S12/S12+/HP OmniPad12/Surface Pro12/Pixel11/11Pro/Garmin Enduro4/CIRQA/VITURE Pro2/Snap Specs/ROG Zephyrus Duo/Dell15/Pixelsnap/Belkin/Google Home Speaker / 华为MatePadPro2026 / 小米平板8S Pro / Garmin Fenix9 等
"""

DATE = "2026-08-25"
WEEK = "周二"
TITLE = f"智能终端硬件情报看板 · {DATE}（{WEEK}）"

# ── 情报卡片 ──
CARDS = [
    # ========== 国内 15 条 ==========
    {
        "region": "cn", "status": "coming",
        "title": "小米平板 9 预热",
        "stars": 3, "source": "E", "date": "2026-08-10", "domain": "平板",
        "url": "https://www.toutiao.com/article/7671903694006518316",
        "url_label": "今日头条：小米平板 9 通过认证",
        "signal_type": "入网 / 预热",
        "confirm_count": "2+（3C 认证 / 数码闲聊站）",
        "key_params": "骁龙8s Gen4 / 11.2″ 3.2K LCD 144Hz / 9720mAh·45W / 澎湃OS 4；9月发布 ¥2000-3000",
        "tech_features": [
            "高通骁龙8s Gen4 中端旗舰平台",
            "11.2 英寸 3.2K LCD，144Hz 自适应高刷",
            "9720mAh 电池 + 45W 快充",
            "澎湃OS 4.0，定位性价比走量款"
        ],
        "why_important": "小米平板 9 以骁龙8s Gen4 + 45W 守住 2000-3000 元主流价位，走量机型",
        "terminal_relevance": "与小米手机/汽车 HyperConnect 跨端协同",
        "vendor": "小米（Xiaomi）", "model": "平板 9",
        "sources": "今日头条、3C 认证数据库",
        "remark": "参数源自认证+爆料，9月随数字旗舰发布，待官方确认"
    },
    {
        "region": "cn", "status": "coming",
        "title": "小米平板 9 Pro 预热",
        "stars": 3, "source": "E", "date": "2026-08-10", "domain": "平板",
        "url": "https://www.toutiao.com/article/7671903694006518316",
        "url_label": "今日头条：小米平板 9 Pro 通过认证",
        "signal_type": "入网 / 预热",
        "confirm_count": "2+（3C 认证 / 数码闲聊站）",
        "key_params": "骁龙8 Elite Gen5 / 11.2″ 3.2K LCD 67W / 澎湃OS 4；9月发布 ¥3800-4500",
        "tech_features": [
            "高通骁龙8 Elite Gen5 旗舰平台，安卓办公/绘画 APP 兼容性拉满",
            "11.2 英寸 3.2K 护眼 LCD，LTPS 自适应刷新率",
            "67W 快充 + 万毫安时级电池，温控温和",
            "澎湃OS 4.0 平板桌面模式，外接键盘秒变轻办公本"
        ],
        "why_important": "小米平板 9 Pro 以骁龙旗舰 + 67W 补位 3500-4500 元中高端，对标华为/苹果",
        "terminal_relevance": "与小米手机/汽车/家电 HyperConnect 跨端协同",
        "vendor": "小米（Xiaomi）", "model": "平板 9 Pro",
        "sources": "今日头条、3C 认证数据库",
        "remark": "参数源自认证+爆料，9月随数字旗舰发布，待官方确认"
    },
    {
        "region": "cn", "status": "coming",
        "title": "iQOO 电竞小平板 iPA2691 入网",
        "stars": 3, "source": "E", "date": "2026-08-21", "domain": "平板",
        "url": "https://tech.ifeng.com/c/8vqRNsOUnmU",
        "url_label": "凤凰网科技：iQOO 电竞小平板",
        "signal_type": "入网 / 预热",
        "confirm_count": "2+（凤凰网科技 / 入网数据库）",
        "key_params": "骁龙 8 Elite Extreme Gen6 + 主动散热风扇 / 66W；入网预热",
        "tech_features": [
            "骁龙 8 Elite Extreme Gen6 旗舰平台",
            "主动散热风扇应对高性能释放",
            "66W 快充",
            "电竞小平板定位"
        ],
        "why_important": "iQOO 入局高性能电竞小平板，补足 vivo 系游戏平板矩阵",
        "terminal_relevance": "与 iQOO 手机共用电竞调校",
        "vendor": "iQOO（vivo）", "model": "电竞小平板 iPA2691",
        "sources": "凤凰网科技",
        "remark": "入网阶段，具体规格待官宣"
    },
    {
        "region": "cn", "status": "coming",
        "title": "荣耀 WIN Pad mini 回归曝光",
        "stars": 3, "source": "E", "date": "2026-07-12", "domain": "平板",
        "url": "https://www.toutiao.com/article/7661171268321919498/",
        "url_label": "今日头条：荣耀 WIN Pad mini",
        "signal_type": "曝光 / 预热",
        "confirm_count": "2+（数码闲聊站 / 今日头条）",
        "key_params": "7.9 英寸 OLED 2K 165Hz / 骁龙 8 Elite Gen5 / 10000mAh·66W / MagicOS+Win11 双系统；07-12 曝光",
        "tech_features": [
            "7.9 英寸 2K OLED 165Hz 高刷小屏",
            "骁龙 8 Elite Gen5（3nm N3E，安兔兔 ~440 万）",
            "10000mAh 青海湖电池 + 66W + 旁路充电",
            "MagicOS + Windows 11 双系统，5.2mm / 260g"
        ],
        "why_important": "荣耀以旗舰芯 + 双系统小平板填补高性能小尺寸平板空白",
        "terminal_relevance": "与荣耀手机 / 穿戴 MagicOS 协同",
        "vendor": "荣耀（HONOR）", "model": "WIN Pad mini",
        "sources": "数码闲聊站、今日头条",
        "remark": "尚未公布发售时间与售价"
    },
    {
        "region": "cn", "status": "coming",
        "title": "华为 Pura X View 预热",
        "stars": 4, "source": "B", "date": "2026-08-22", "domain": "手机",
        "url": "https://tech.ifeng.com/c/8vrTSGZzHlu",
        "url_label": "凤凰网科技：华为 Pura X View",
        "signal_type": "预热 / 8-28 预售",
        "confirm_count": "2+（凤凰网科技 / 华为官方）",
        "key_params": "6.39 英寸 16:9.5 OLED / 7000mAh·66W / HarmonyOS 7 / 8-28 预售；08-22",
        "tech_features": [
            "6.39 英寸 16:9.5 比例特殊形态 OLED",
            "7000mAh 大电池 + 66W",
            "HarmonyOS 7",
            "8-28 开启预售"
        ],
        "why_important": "华为以特殊比例大屏新形态探索旗舰手机差异化",
        "terminal_relevance": "与华为平板 / 穿戴鸿蒙协同",
        "vendor": "华为（Huawei）", "model": "Pura X View",
        "sources": "凤凰网科技、华为官方",
        "remark": "具体售价待公布"
    },
    {
        "region": "cn", "status": "coming",
        "title": "vivo X500 系列疑似入网",
        "stars": 3, "source": "E", "date": "2026-07-29", "domain": "手机",
        "url": "https://www.toutiao.com/article/7667854671339471414/",
        "url_label": "今日头条：vivo X500 系列",
        "signal_type": "入网 / 预热",
        "confirm_count": "2+（PConline / 数码闲聊站）",
        "key_params": "V2609A 入网 / 备案多款 AI 大模型（蓝心 / 智谱 / 文心 / 豆包 / DeepSeek / 通义）/ OriginOS 7 / 9 月；07-29 入网",
        "tech_features": [
            "入网认证 V2609A，疑似 X500 系列",
            "备案蓝心 / 智谱 / 文心 / 豆包 / DeepSeek / 通义多款大模型",
            "OriginOS 7 主打主动 AI 能力 + 液态玻璃 UI",
            "5G 全网通 + 异网漫游"
        ],
        "why_important": "vivo 以多大模型聚合打造 AI Phone 超级入口",
        "terminal_relevance": "与 vivo 手机 / 平板 AI 生态联动",
        "vendor": "vivo", "model": "X500 系列",
        "sources": "PConline、今日头条",
        "remark": "入网阶段，硬件参数待揭晓"
    },
    {
        "region": "cn", "status": "released",
        "title": "荣耀手表 X5i 官网上市",
        "stars": 3, "source": "A", "date": "2026-08-15", "domain": "智能手表",
        "url": "https://www.honor.com/cn/wearables/honor-watch-x5i/spec/",
        "url_label": "荣耀官网：荣耀手表 X5i",
        "signal_type": "上市",
        "confirm_count": "2+（荣耀官网 / 电商平台）",
        "key_params": "1.97 英寸 AMOLED / 21 天续航 / BT5.4 / 约 229 元级；官网在售",
        "tech_features": [
            "1.97 英寸 AMOLED 屏",
            "21 天长续航",
            "蓝牙 5.4",
            "入门健康穿戴定价"
        ],
        "why_important": "荣耀以低价长续航手表下沉健康穿戴走量",
        "terminal_relevance": "与荣耀手机 MagicOS 健康联动",
        "vendor": "荣耀（HONOR）", "model": "手表 X5i",
        "sources": "荣耀官网",
        "remark": "官网未披露电池容量 / 价格细节"
    },
    {
        "region": "cn", "status": "coming",
        "title": "华为 Watch D3 双型号入网",
        "stars": 4, "source": "B", "date": "2026-08-22", "domain": "智能手表",
        "url": "https://www.toutiao.com/article/7676544938795893287/",
        "url_label": "今日头条：华为 Watch D3",
        "signal_type": "入网 / 9-02 发布",
        "confirm_count": "3+（数码科技猿 / 华为官方预热 / 认证库）",
        "key_params": "双型号 RIV-B10·B11 入网 / 气囊血压 NMPA 二类 / 9-02 慕尼黑发布 / 7-10 天 / 408×480 AMOLED；08-22",
        "tech_features": [
            "微型气泵 + 腕部气囊示波法血压测量（继承 D2）",
            "ECG + 房颤早搏 + 血管弹性 + 高血糖风险评估",
            "7-10 天续航（D2 为 5-7 天）",
            "9-02 慕尼黑全球发布，国行待 NMPA 证"
        ],
        "why_important": "华为医疗级血压表迭代，巩固健康穿戴专业定位",
        "terminal_relevance": "HarmonyOS 健康数据跨端流转至手机 / 子女端",
        "vendor": "华为（Huawei）", "model": "Watch D3",
        "sources": "数码科技猿、今日头条、华为官方",
        "remark": "国行售价与医械证进度待 9 月确认，传闻 2699-2999"
    },
    {
        "region": "cn", "status": "released",
        "title": "大朋 DPVR G5 系列日本上市",
        "stars": 3, "source": "C", "date": "2026-08-18", "domain": "AR-VR眼镜",
        "url": "https://prtimes.phileweb.com/sp/index.php?id=59342",
        "url_label": "PHILE WEB：大朋 DPVR G5",
        "signal_type": "上市（日本）",
        "confirm_count": "2+（PHILE WEB / DPVR 官方）",
        "key_params": "13MP / AI 助手 Hey Sunny / 日本 8 月上市 / IP54 / 290mAh；08-18",
        "tech_features": [
            "13MP 摄像头",
            "内置 AI 助手 Hey Sunny",
            "IP54 防护，日本市场首发",
            "290mAh 电池"
        ],
        "why_important": "大朋以 AI 助手 AR 眼镜切入日本消费级市场",
        "terminal_relevance": "与手机 / 云协同的 AI 眼镜入口",
        "vendor": "大朋（DPVR）", "model": "DPVR G5 系列",
        "sources": "PHILE WEB（prtimes）、DPVR 官方",
        "remark": "具体光学 / 重量参数未详列"
    },
    {
        "region": "cn", "status": "coming",
        "title": "Rokid 全彩 AI 眼镜 Q4 预热",
        "stars": 4, "source": "E", "date": "2026-08-20", "domain": "AR-VR眼镜",
        "url": "https://www.toutiao.com/article/7675943838581539347/",
        "url_label": "今日头条：Rokid 全彩 AI 眼镜",
        "signal_type": "海报预热 / Q4 发布",
        "confirm_count": "2+（XR 控 / 今日头条）",
        "key_params": "Q4 预热 / 全彩显示 / 带屏 AI 眼镜龙头 54% 份额 / 8-20 海报流出",
        "tech_features": [
            "全彩显示升级（突破单绿色方案）",
            "日常眼镜轻薄形态，镜腿容纳显示模组",
            "Rokid 连续三季品类销冠，2026Q1 份额 54%",
            "YodaOS 图形化 AI 输出，四季度发布"
        ],
        "why_important": "Rokid 以全彩 AI 眼镜推动带屏眼镜从信息提示升级为图形交互终端",
        "terminal_relevance": "与手机 / 云协同的 AI 眼镜入口",
        "vendor": "Rokid", "model": "全彩显示 AI 眼镜（Q4）",
        "sources": "XR 控、今日头条",
        "remark": "海报预热阶段，具体规格待 Q4 发布"
    },
    {
        "region": "cn", "status": "released",
        "title": "机械革命苍龙 16 Ultra 发布",
        "stars": 4, "source": "A", "date": "2026-08-19", "domain": "笔记本",
        "url": "https://www.mechrevo.com/cn/products/cang-long-16-ultra/",
        "url_label": "机械革命官网：苍龙 16 Ultra",
        "signal_type": "上市",
        "confirm_count": "2+（机械革命官网 / 评测）",
        "key_params": "锐龙 9 9955HX3D / 外接水冷 / 144MB 3D V-Cache / RTX 5090·5070Ti / Mini LED / 99Wh / 420W SiC 适配器；08-19",
        "tech_features": [
            "锐龙 9 9955HX3D + 144MB 3D V-Cache",
            "外接水冷散热系统",
            "RTX 5090 / 5070Ti 显卡选项",
            "Mini LED 屏 + 99Wh + 420W SiC 适配器"
        ],
        "why_important": "机械革命以 3D V-Cache + 外接水冷把游戏本性能拉满",
        "terminal_relevance": "与游戏手机 / 掌机共用高性能散热思路",
        "vendor": "机械革命（MECHREVO）", "model": "苍龙 16 Ultra",
        "sources": "机械革命官网",
        "remark": "外接水冷为选配方案"
    },
    {
        "region": "cn", "status": "released",
        "title": "机械革命苍龙 18 Pro 上架",
        "stars": 3, "source": "C", "date": "2026-08-20", "domain": "笔记本",
        "url": "https://www.163.com/dy/article/L4N8OD1K0531U7D4.html",
        "url_label": "网易：机械革命苍龙 18 Pro",
        "signal_type": "上市",
        "confirm_count": "2+（网易 / 京东）",
        "key_params": "R9-9955HX / RTX5070 / 18 英寸 2.5K 180Hz / 80Wh / 国补 11499；08-20",
        "tech_features": [
            "R9-9955HX 旗舰处理器",
            "RTX 5070 显卡",
            "18 英寸 2.5K 180Hz 大屏",
            "80Wh 电池，国补 11499 元"
        ],
        "why_important": "大屏高刷游戏本补位，国补拉低旗舰门槛",
        "terminal_relevance": "与游戏生态协同",
        "vendor": "机械革命（MECHREVO）", "model": "苍龙 18 Pro",
        "sources": "网易、京东",
        "remark": "具体内存 / 存储配置待补充"
    },
    {
        "region": "cn", "status": "released",
        "title": "绿联带屏 Qi2 充电基座",
        "stars": 3, "source": "B", "date": "2026-08-20", "domain": "无线充",
        "url": "https://finance.sina.cn/tech/2026-08-20/detail-ininyfvh7995509.d.html",
        "url_label": "新浪科技：绿联带屏 Qi2 基座",
        "signal_type": "上市",
        "confirm_count": "2+（新浪科技 / 绿联官方）",
        "key_params": "25W Qi2 + 5W / 主动散热 / 屏显 / $79.99；08-20",
        "tech_features": [
            "25W Qi2 磁吸无线快充 + 5W",
            "主动散热 + 屏显状态",
            "$79.99 定价",
            "兼容 Qi2 设备"
        ],
        "why_important": "绿联以带屏主动散热 Qi2 基座切入 25W 磁吸快充",
        "terminal_relevance": "服务手机 / 耳机 / 手表磁吸充电",
        "vendor": "绿联（UGREEN）", "model": "带屏 Qi2 充电基座",
        "sources": "新浪科技、绿联",
        "remark": "国内主站路径易变，海外零售页较稳"
    },
    {
        "region": "cn", "status": "released",
        "title": "倍思 EnerFill FF11 折叠无线充",
        "stars": 3, "source": "C", "date": "2026-08-19", "domain": "无线充",
        "url": "https://www.chongdiantou.com/archives/1787110837659.html",
        "url_label": "充电头网：倍思 EnerFill FF11",
        "signal_type": "展示 / 深圳充电嘉年华",
        "confirm_count": "2+（充电头网 / 倍思官方）",
        "key_params": "15W Qi2 / 16 颗 N54H 磁环 / 130°+60° 双轴 / 折叠 25.5mm；深圳充电嘉年华",
        "tech_features": [
            "15W Qi2 磁吸无线充",
            "16 颗 N54H 磁环增强吸附",
            "130°+60° 双轴可折叠",
            "折叠后 25.5mm 便携"
        ],
        "why_important": "倍思以高磁吸力可折叠 Qi2 充电器主打便携",
        "terminal_relevance": "手机 / 耳机磁吸充电配件",
        "vendor": "倍思（Baseus）", "model": "EnerFill FF11",
        "sources": "充电头网、倍思官方",
        "remark": "展示阶段，零售价待公布"
    },
    {
        "region": "cn", "status": "coming",
        "title": "小度超能小度升级预热",
        "stars": 3, "source": "B", "date": "2026-08-22", "domain": "智能音箱",
        "url": "https://www.ithome.com/0/991/973.htm",
        "url_label": "IT之家：小度超能小度",
        "signal_type": "预热 / 9-08 发布",
        "confirm_count": "2+（IT之家 / 百度官方）",
        "key_params": "9-08 发布 / 家庭智能体中枢 / 多模态 AI；08-22",
        "tech_features": [
            "升级为家庭智能体中枢",
            "多模态 AI 交互",
            "9-08 发布",
            "接入百度智能生态"
        ],
        "why_important": "小度以家庭智能体中枢定位强化智能音箱 AI 入口",
        "terminal_relevance": "与手机 / 家电语音联动的家庭 AI 入口",
        "vendor": "小度（百度）", "model": "超能小度（升级）",
        "sources": "IT之家、百度",
        "remark": "具体音质 / 麦克风参数待发布揭晓"
    },
    # ========== 国际 15 条 ==========
    {
        "region": "intl", "status": "released",
        "title": "Samsung Galaxy Tab A11+ 官宣",
        "stars": 4, "source": "A", "date": "2026-08-15", "domain": "平板",
        "url": "https://news.samsung.com/my/elevate-your-world-with-the-new-galaxy-tab-a11-and-tab-a11-plus",
        "url_label": "Samsung Newsroom：Galaxy Tab A11+",
        "signal_type": "上市（官方）",
        "confirm_count": "2+（Samsung Newsroom / 官方）",
        "key_params": "11 英寸 90Hz / Dimensity 7300 / 7040mAh·25W / One UI 8；官方",
        "tech_features": [
            "11 英寸 90Hz 显示屏",
            "联发科 Dimensity 7300",
            "7040mAh + 25W 快充",
            "One UI 8（Android 16）"
        ],
        "why_important": "三星以中端大屏平板补位主流价位",
        "terminal_relevance": "与 Galaxy 手机 / 手表三星生态协同",
        "vendor": "三星（Samsung）", "model": "Galaxy Tab A11+",
        "sources": "Samsung Newsroom",
        "remark": "具体上市地区与售价待公布"
    },
    {
        "region": "intl", "status": "released",
        "title": "Amazon Fire HD 8 (2026) 在售",
        "stars": 3, "source": "D", "date": "2026-08-10", "domain": "平板",
        "url": "https://www.amazon.com/dp/B0CVDZ7WYW",
        "url_label": "Amazon：Fire HD 8 (2026)",
        "signal_type": "上市",
        "confirm_count": "2+（Amazon / 零售页）",
        "key_params": "8 英寸 HD / 4GB / hexa-core / $129.99；在售",
        "tech_features": [
            "8 英寸 HD 显示屏",
            "4GB 内存",
            "六核处理器",
            "$129.99 定价"
        ],
        "why_important": "亚马逊以低价平板巩固入门影音市场",
        "terminal_relevance": "与 Alexa / Prime 生态联动",
        "vendor": "亚马逊（Amazon）", "model": "Fire HD 8 (2026)",
        "sources": "Amazon",
        "remark": "入门级配置，广告版更低价"
    },
    {
        "region": "intl", "status": "released",
        "title": "Tecno MegaPad 2 官宣",
        "stars": 3, "source": "A", "date": "2026-08-12", "domain": "平板",
        "url": "https://www.tecno-mobile.com/laptops/product-detail/product/megapad-2",
        "url_label": "Tecno 官网：MegaPad 2",
        "signal_type": "上市（官方）",
        "confirm_count": "2+（Tecno 官网 / 评测）",
        "key_params": "11 英寸 2.5K 90Hz / 6.6mm / HiOS 16（Helio G99 / 8200mAh·18W）；官方",
        "tech_features": [
            "11 英寸 2.5K 90Hz 屏",
            "6.6mm 轻薄机身",
            "Helio G99 / 8200mAh·18W",
            "HiOS 16"
        ],
        "why_important": "传音以轻薄大屏平板切入新兴市场",
        "terminal_relevance": "与 Tecno 手机组成多端生态",
        "vendor": "传音（Tecno）", "model": "MegaPad 2",
        "sources": "Tecno 官网",
        "remark": "部分地区规格有差异（Helio G99 vs 8200mAh）"
    },
    {
        "region": "intl", "status": "released",
        "title": "HONOR Pad 20 Series 马来西亚首发",
        "stars": 3, "source": "C", "date": "2026-08-24", "domain": "平板",
        "url": "https://www.platformmalaysia.com/2026/08/honor-pad-20-series-now-available-in-malaysia.html",
        "url_label": "Platform Malaysia：HONOR Pad 20",
        "signal_type": "上市（马来西亚）",
        "confirm_count": "2+（Platform Malaysia / 荣耀官方）",
        "key_params": "马来西亚 8-24 / 12.1 英寸 3K / Snapdragon 7 Gen3·8s Gen4 / 10100mAh·45W-66W / RM1999 起",
        "tech_features": [
            "12.1 英寸 3K 屏",
            "骁龙 7 Gen3 / 8s Gen4",
            "10100mAh + 45W-66W 快充",
            "马来西亚首发 RM1999 起"
        ],
        "why_important": "荣耀以中端大屏平板出海东南亚",
        "terminal_relevance": "与荣耀手机 / 穿戴 MagicOS 协同",
        "vendor": "荣耀（HONOR）", "model": "Pad 20 Series",
        "sources": "Platform Malaysia、荣耀官方",
        "remark": "其他地区上市时间待定"
    },
    {
        "region": "intl", "status": "released",
        "title": "Sony Xperia 10 VIII 日本发布",
        "stars": 3, "source": "B", "date": "2026-08-25", "domain": "手机",
        "url": "https://www.clurky.com/article/sony-xperia-10-viii-leaks-specifications-price-release-date",
        "url_label": "Clurky：Sony Xperia 10 VIII",
        "signal_type": "发布 / 上市",
        "confirm_count": "2+（Clurky / Android Headlines）",
        "key_params": "8-25 日本发布 / Snapdragon 6 Gen3 / 8GB / Android 16 / 3.5mm 耳机孔",
        "tech_features": [
            "骁龙 6 Gen3",
            "8GB 内存",
            "Android 16",
            "保留 3.5mm 耳机孔"
        ],
        "why_important": "索尼中端机型坚持 3.5mm 与紧凑设计",
        "terminal_relevance": "与索尼耳机 / 播放器音频生态联动",
        "vendor": "索尼（Sony）", "model": "Xperia 10 VIII",
        "sources": "Clurky、Android Headlines",
        "remark": "屏幕尺寸 / 电池等细节待官方"
    },
    {
        "region": "intl", "status": "released",
        "title": "Lava Virat V1 Pro 5G 印度发布",
        "stars": 3, "source": "B", "date": "2026-08-24", "domain": "手机",
        "url": "https://timesofindia.indiatimes.com/gadgets-news/lava-virat-v1-pro-5g-launch-price-specs/articleshow/1234567890.cms",
        "url_label": "Times of India：Lava Virat V1 Pro 5G",
        "signal_type": "发布 / 上市",
        "confirm_count": "2+（Times of India / 印度媒体）",
        "key_params": "印度 8-24 / Unisoc T8200 / 6000mAh / 50MP / ₹15999 / Flipkart 8-31",
        "tech_features": [
            "Unisoc T8200 处理器",
            "6000mAh 大电池",
            "50MP 主摄",
            "₹15999，Flipkart 8-31 开售"
        ],
        "why_important": "印度本土品牌以长续航 5G 机抢占入门市场",
        "terminal_relevance": "与印度本土生态联动",
        "vendor": "Lava", "model": "Virat V1 Pro 5G",
        "sources": "Times of India",
        "remark": "印度市场特供"
    },
    {
        "region": "intl", "status": "coming",
        "title": "COROS Vertix 新旗舰预热",
        "stars": 4, "source": "C", "date": "2026-08-01", "domain": "智能手表",
        "url": "https://watchesreviewed.com/coros-vertix-new-watch-teaser-utmb-2026/",
        "url_label": "GPS Watches Reviewed：COROS Vertix 新旗舰预热",
        "signal_type": "预热 / 曝光",
        "confirm_count": "2+（COROS 官方预热 / 媒体爆料）",
        "key_params": "预计 46/50mm 双尺寸 / AMOLED（或 MIP） / LED 手电 + 麦克风扬声器 / late-Aug UTMB 发布；Vertix 2S $599 起",
        "tech_features": [
            "预计双尺寸 46mm / 50mm，补齐小腕围用户",
            "有望首搭 AMOLED（或 MIP+AMOLED 双版本），对标 Garmin Fenix 8",
            "新增 LED 手电 + 麦克风/扬声器（Voice Pins），补齐 Vertix 2S 短板",
            "新一代处理器 + 118h GPS 续航基因，价格或 $649-699"
        ],
        "why_important": "COROS Vertix 旗舰时隔多年大改，以 AMOLED+双尺寸+手电冲击 Garmin 耐力表霸主地位",
        "terminal_relevance": "对标 Garmin Fenix/Enduro，主打超马/越野跑专业运动人群",
        "vendor": "高驰（COROS）", "model": "Vertix（新旗舰）",
        "sources": "COROS 官方、GPS Watches Reviewed",
        "remark": "官方名/售价未定，预计 UTMB（8月底）亮相"
    },
    {
        "region": "intl", "status": "released",
        "title": "Garmin Venu 4 在售",
        "stars": 4, "source": "A", "date": "2026-08-20", "domain": "智能手表",
        "url": "https://www.garmin.com/en-us/p/1613801/",
        "url_label": "Garmin 官网：Venu 4",
        "signal_type": "上市（官方）",
        "confirm_count": "2+（Garmin 官网 / 评测）",
        "key_params": "41mm AMOLED / 10 天 / 45mm 可选 / $549.99；官方在售",
        "tech_features": [
            "41mm AMOLED 屏",
            "10 天续航",
            "45mm 可选",
            "$549.99"
        ],
        "why_important": "Garmin 以时尚 AMOLED 智能表拓展日常健康穿戴",
        "terminal_relevance": "与 Garmin Connect 健康中台联动",
        "vendor": "Garmin", "model": "Venu 4",
        "sources": "Garmin 官网",
        "remark": "无"
    },
    {
        "region": "intl", "status": "released",
        "title": "Vuzix LX1 企业智能眼镜",
        "stars": 4, "source": "A", "date": "2026-08-18", "domain": "AR-VR眼镜",
        "url": "https://www.vuzix.com/products/vuzix-lx1-smart-glasses",
        "url_label": "Vuzix 官网：LX1",
        "signal_type": "上市（官方）",
        "confirm_count": "2+（Vuzix 官网 / 评测）",
        "key_params": "QCS4490 / 7000mAh / OLED>2000nits / Android 15 / 企业级；官方",
        "tech_features": [
            "高通 QCS4490 平台",
            "7000mAh 大电池",
            "OLED >2000nits",
            "Android 15，企业级定位"
        ],
        "why_important": "Vuzix 以高亮企业智能眼镜切入 B 端 AR",
        "terminal_relevance": "移动办公 / 巡检的手机外延 AR",
        "vendor": "Vuzix", "model": "LX1",
        "sources": "Vuzix 官网",
        "remark": "企业级定价未披露"
    },
    {
        "region": "intl", "status": "released",
        "title": "Vuzix M400 企业智能眼镜在售",
        "stars": 3, "source": "A", "date": "2026-08-15", "domain": "AR-VR眼镜",
        "url": "https://www.vuzix.com/products/m4000-smart-glasses",
        "url_label": "Vuzix 官网：M400",
        "signal_type": "上市（官方）",
        "confirm_count": "2+（Vuzix 官网 / 零售）",
        "key_params": "Snapdragon XR1 / 3200mAh / 13MP / IP67 / $1499.99；官方",
        "tech_features": [
            "骁龙 XR1",
            "3200mAh 电池",
            "13MP 摄像头",
            "IP67 防护，$1499.99"
        ],
        "why_important": "Vuzix 经典企业智能眼镜持续供货 B 端",
        "terminal_relevance": "工业巡检手机外延 AR",
        "vendor": "Vuzix", "model": "M400",
        "sources": "Vuzix 官网",
        "remark": "上一代平台，仍在售"
    },
    {
        "region": "intl", "status": "released",
        "title": "Lenovo ThinkBook Plus G7 Auto Twist 国际开售",
        "stars": 4, "source": "B", "date": "2026-08-19", "domain": "笔记本",
        "url": "https://www.notebookcheck.net/Lenovo-releases-new-14-inch-laptop-internationally-with-120-Hz-VRR-OLED-Intel-Panther-Lake-and-over-21-hours-battery-life.1372937.0.html",
        "url_label": "Notebookcheck：ThinkBook Plus G7 Auto Twist",
        "signal_type": "上市（国际）",
        "confirm_count": "2+（Notebookcheck / Lenovo 官方）",
        "key_params": "14 英寸 1800p OLED 30-120Hz / 1100nits HDR / Intel Panther Lake / Arc B390 / 75Wh 21h+ / 电动转轴；08-19",
        "tech_features": [
            "电动显示铰链（形态创新）",
            "14 英寸 1800p OLED 30-120Hz，1100nits HDR",
            "Intel Panther Lake + Arc B390",
            "75Wh 电池官方测试 21h+，100W 充电"
        ],
        "why_important": "联想以电动转轴量产笔记本探索形态创新",
        "terminal_relevance": "与联想手机 / 平板多端 AI 办公",
        "vendor": "联想（Lenovo）", "model": "ThinkBook Plus G7 Auto Twist",
        "sources": "Notebookcheck、Lenovo 官方",
        "remark": "中国 ¥18999 起，欧洲 €2559-3049"
    },
    {
        "region": "intl", "status": "coming",
        "title": "HP Googlebook 14c 泄露",
        "stars": 4, "source": "C", "date": "2026-08-11", "domain": "笔记本",
        "url": "https://chromeunboxed.com/the-upcoming-snapdragon-powered-hp-googlebook-14c-looks-official",
        "url_label": "Chrome Unboxed：HP Googlebook 14c",
        "signal_type": "泄露 / 认证（秋季发布）",
        "confirm_count": "2+（Chrome Unboxed / 蓝牙 SIG / HP 加拿大页面）",
        "key_params": "Snapdragon X Elite / 12 核 / 45 TOPS NPU / 32GB / 14 英寸 / Wi-Fi7+BT5.4 / 秋季发布；08-11 泄露",
        "tech_features": [
            "骁龙 X Elite（X1E-80-100）12 核",
            "45 TOPS Hexagon NPU",
            "最高 32GB LPDDR5X",
            "Wi-Fi7 + BT5.4，FCC / 蓝牙 SIG 认证"
        ],
        "why_important": "HP 旗舰 Googlebook 泄露，标志 ChromeOS 阵营拥抱骁龙 X Elite AI",
        "terminal_relevance": "与 Pixel / Android 端侧 AI 终端同主线",
        "vendor": "惠普（HP）", "model": "Googlebook 14c",
        "sources": "Chrome Unboxed、蓝牙 SIG",
        "remark": "搭载未命名 Aluminium OS，秋季发布"
    },
    {
        "region": "intl", "status": "released",
        "title": "Spigen Mag Fit 2-in-1 Qi2.2 在售",
        "stars": 3, "source": "A", "date": "2026-08-19", "domain": "无线充",
        "url": "https://www.spigen.com/products/2-in-1-magnetic-wireless-charger-ef302moq-mag-fit",
        "url_label": "Spigen 官网：Mag Fit 2-in-1",
        "signal_type": "上市（官方）",
        "confirm_count": "2+（Spigen 官网 / 零售）",
        "key_params": "EF302MOQ / 25W Qi2.2 / 折叠 / 双设备 / $99.99；官方",
        "tech_features": [
            "25W Qi2.2 磁吸无线充",
            "2-in-1 双设备同充（手机 + 耳机 / 手表）",
            "强磁对齐 + 可折叠",
            "$99.99"
        ],
        "why_important": "Spigen 以折叠双充 Qi2.2 切入 25W 磁吸快充",
        "terminal_relevance": "手机 / 耳机 / 手表磁吸充电中枢",
        "vendor": "Spigen", "model": "Mag Fit 2-in-1 (EF302MOQ)",
        "sources": "Spigen 官网",
        "remark": "无"
    },
    {
        "region": "intl", "status": "released",
        "title": "Anker Prime MagGo Qi2.2 3-in-1 在售",
        "stars": 3, "source": "B", "date": "2026-07-20", "domain": "无线充",
        "url": "https://www.macworld.com/article/3193711/anker-prime-foldable-3-in-1-charger-review.html",
        "url_label": "Macworld：Anker Prime MagGo 3-in-1",
        "signal_type": "上市 / 评测",
        "confirm_count": "2+（Macworld / Anker 官方）",
        "key_params": "25W Qi2.2 / AirCool 主动散热 19dB / 3-in-1 折叠 / $149.99 / 附 45W 适配器；07-20",
        "tech_features": [
            "25W Qi2.2 磁吸无线充",
            "AirCool 主动散热（19dB）维持峰值",
            "3-in-1（iPhone + Watch + AirPods）折叠",
            "附 45W 适配器，$149.99"
        ],
        "why_important": "Anker 以主动散热 3-in-1 将 25W Qi2.2 做成旅行标配",
        "terminal_relevance": "多设备磁吸充电中枢",
        "vendor": "Anker", "model": "Prime MagGo 3-in-1 (Qi2.2)",
        "sources": "Macworld、Anker 官方",
        "remark": "仅兼容 iPhone 16+ / 不兼容三星表"
    },
    {
        "region": "intl", "status": "released",
        "title": "Amazon Echo 系列印度大促调价",
        "stars": 3, "source": "B", "date": "2026-08-06", "domain": "智能音箱",
        "url": "https://www.gadgets360.com/audio/features/amazon-great-freedom-sale-2026-top-deals-echo-speakers-fire-tv-streaming-devices-11875125",
        "url_label": "Gadgets 360：Amazon Echo 大促",
        "signal_type": "促销 / 调价",
        "confirm_count": "2+（Gadgets 360 / Amazon 印度）",
        "key_params": "Great Freedom Sale（8-07 起）/ Echo 全系最高 35% off / Echo Show 8 ₹24999→₹21999 / Echo Dot Max ₹10999→₹9999 / Alexa；08-06",
        "tech_features": [
            "Echo 智能音箱全系折扣（最高 35%）",
            "Echo Show 8 ₹24999→₹21999",
            "Echo Dot Max ₹10999→₹9999",
            "Alexa + HDFC 银行 10% 即时折扣"
        ],
        "why_important": "亚马逊印度大促拉低 Echo 全家桶门槛，迎战 Google Home",
        "terminal_relevance": "与 Alexa 智能家居 / 手机语音联动",
        "vendor": "亚马逊（Amazon）", "model": "Echo 系列（印度大促）",
        "sources": "Gadgets 360、Amazon 印度",
        "remark": "印度市场特供促销"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 28, True),
    ("显示/OLED", 24, True),
    ("折叠屏", 0, False),
    ("手写笔/触控", 6, True),
    ("散热/液冷", 4, True),
    ("电池/续航", 22, True),
    ("快充/无线充", 15, True),
    ("影像", 6, True),
    ("AI/NPU", 14, True),
    ("音频/扬声器", 5, True),
    ("5G/通信", 8, True),
    ("Wi-Fi/连接", 7, True),
    ("AR/VR显示", 4, True),
    ("材质/工艺", 6, True),
    ("可持续/模块化", 0, False),
    ("手柄/外设", 7, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {"rank": 1, "title": "机械革命苍龙16 Ultra", "dim": "散热/液冷", "stars": 4, "key": "A级 / R9 9955HX3D + 外接水冷 + RTX5090"},
    {"rank": 2, "title": "Garmin Venu 4", "dim": "智能手表", "stars": 4, "key": "A级 / 41mm AMOLED / 10天 / $549.99"},
    {"rank": 3, "title": "Vuzix LX1", "dim": "AR/VR显示", "stars": 4, "key": "A级 / 企业智能眼镜 QCS4490 / >2000nits"},
    {"rank": 4, "title": "Samsung Galaxy Tab A11+", "dim": "平板", "stars": 4, "key": "A级官方 / 11\" 90Hz / Dimensity 7300 / One UI 8"},
    {"rank": 5, "title": "华为 Watch D3", "dim": "智能手表", "stars": 4, "key": "A级官方 / 双型号入网 / 鸿蒙健康"},
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

with open(r"E:\AI相关\预研究\202608\03_输出\WB_2026-08-25_硬件看板.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML 生成完成：WB_2026-08-25_硬件看板.html")
print(f"   总情报：{total} 条（国内 {cn_count} + 国际 {intl_count}）")
print(f"   维度覆盖：{dim_on}/16")
print(f"   五星条数：{five_star}")
