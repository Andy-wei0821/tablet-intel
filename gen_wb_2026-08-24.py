#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WB_2026-08-24 智能终端硬件情报看板生成器
- 30 条卡片（国内 15 + 国际 15）
- 7 品类 × 14 字段卡 + 16 维覆盖面板 + Top5 信号
- 单 HTML / 内联 CSS / 无 CDN / #card-N 锚点 / html{scroll-behavior:smooth}
- 信源 A-E 级 | 1-5★ | 状态 coming(即将上市)/released(已上市)/progress(进行中)
- 14 天去重窗 + 60 天搜索窗
- 去重基线已排除：联想拯救者Y700无极(08-08)、酷比魔方掌玩mini4(08-19)、闪极Loomos(08-09)、雷鸟iO(08-08)、华为智能眼镜2(08-15)等
"""

DATE = "2026-08-24"
WEEK = "周一"
TITLE = f"智能终端硬件情报看板 · {DATE}（{WEEK}）"

# ── 情报卡片 ──
# 字段：region, status, title, stars, source, date, domain, url, url_label,
#       signal_type, confirm_count, key_params, tech_features(list), why_important,
#       terminal_relevance, vendor, model, sources, remark
CARDS = [
    # ========== 国内 15 条 ==========
    {
        "region": "cn", "status": "released",
        "title": "红魔游戏平板 5 PRO 氘锋透明银翼开售",
        "stars": 4, "source": "B", "date": "2026-08-21", "domain": "平板",
        "url": "https://www.ithome.com/0/991/861.htm",
        "url_label": "IT之家：红魔游戏平板 5 PRO 氘锋透明银翼开售",
        "signal_type": "上市 / 新配色开售",
        "confirm_count": "2+（IT之家 / 京东）",
        "key_params": "第五代骁龙8至尊版 + 红芯R4；9.06英寸 2.4K OLED 185Hz；8300mAh + 80W 有线；双 USB-C；旁路充电Pro；首销 4999 元起 / 国补 4499 元起；6-30 发布 / 8-21 银色开售",
        "tech_features": [
            "ICE 魔冷散热架构（水冷 + RGB 灯效 + 液态金属）",
            "全新 PC 模拟器 Steam 直连模式，低门槛畅玩 PC 大作",
            "AI 战术教练 + AI 魔姬嘴替（DeepSeek），游戏内实时辅助",
            "9.06\" 2.4K OLED 185Hz 电竞屏，双 USB-C",
            "透明水冷设计，电竞双芯把平板游戏性能拉满"
        ],
        "why_important": "红魔游戏平板 5 PRO 以透明水冷 + 电竞双芯 + 80W 快充把平板游戏性能拉满，拓展 PC 游戏平替场景，是安卓游戏平板旗舰代表",
        "terminal_relevance": "与红魔手机共用电竞芯片 / 散热 / AI 玩法，强化游戏生态协同；对高性能平板散热设计有参考价值",
        "vendor": "红魔（RedMagic / 努比亚）", "model": "红魔游戏平板 5 PRO（氘锋透明银翼）",
        "sources": "IT之家、京东",
        "remark": "银翼款因产能限制仅满足部分需求，供应节奏待观察"
    },
    {
        "region": "cn", "status": "released",
        "title": "台电 T70 Pro 安卓平板上架",
        "stars": 3, "source": "B", "date": "2026-08-20", "domain": "平板",
        "url": "https://www.163.com/dy/article/L4Q98LTI0511B8LM.html",
        "url_label": "网易 / IT之家：台电 T70 Pro 上架",
        "signal_type": "上市",
        "confirm_count": "2+（IT之家 / 网易）",
        "key_params": "14英寸 2240×1400 IPS LCD；联发科 G100；8GB+128GB；10000mAh；双 4G；前置 8MP / 后置 13MP；1299 元；08-20 上架",
        "tech_features": [
            "14 英寸大屏便携影音定位",
            "10000mAh 长续航 + 双 4G 插卡通话 / 上网",
            "1299 元低价位段，千元级大屏",
            "前置 8MP + 后置 13MP 双摄"
        ],
        "why_important": "千元级大屏续航平板，填补入门影音 / 网课需求，是低价位段新选择",
        "terminal_relevance": "与手机 / 电视组成家庭轻娱乐多屏场景",
        "vendor": "台电（Teclast）", "model": "T70 Pro",
        "sources": "IT之家、网易",
        "remark": "无"
    },
    {
        "region": "cn", "status": "coming",
        "title": "荣耀平板 X10 Pro Max 开启预约",
        "stars": 4, "source": "B", "date": "2026-08-21", "domain": "平板",
        "url": "https://pad.zol.com.cn/1235/12355997.html",
        "url_label": "中关村在线：荣耀平板 X10 Pro Max 预约",
        "signal_type": "预热 / 预约",
        "confirm_count": "2+（中关村在线 / IT之家）",
        "key_params": "13英寸护眼柔光屏（苍山灰柔光版）；10100mAh；8+128 / 8+256GB；双前置（800万 + 200万 AI 专注眼）；荣耀学习空间；08-21 开预约 / 08-28 开售；价格未公布",
        "tech_features": [
            "200 万像素 AI 专注眼，实时检测 6 大不专注行为",
            "荣耀学习空间 1对1 AI 精准辅导 + 独立防沉迷",
            "较 X10 Pro 的 11.5 英寸升级至 13 英寸大屏",
            "AI 家教 + 专注监测做成大屏学习平板差异化卖点"
        ],
        "why_important": "把「AI 家教 + 专注监测」做成大屏学习平板差异化卖点，是教育平板赛道新势力",
        "terminal_relevance": "与荣耀手机 / 平板生态共享 MagicOS 学习空间与跨端协同",
        "vendor": "荣耀（HONOR）", "model": "平板 X10 Pro Max",
        "sources": "中关村在线、IT之家",
        "remark": "屏幕分辨率 / 刷新率 / 处理器型号及售价待公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "中柏 EZpad Max15 安卓平板上架",
        "stars": 3, "source": "B", "date": "2026-08-22", "domain": "平板",
        "url": "https://www.ithome.com/0/993/093.htm",
        "url_label": "IT之家：中柏 EZpad Max15 上架",
        "signal_type": "上市",
        "confirm_count": "2+（IT之家 / 网易 / 京东）",
        "key_params": "15.4英寸 1920×1080 IPS；联发科 G99；8GB+256GB；四扬声器；10000mAh + 18W；U 型支架可外接键盘；1899 元；08-22 上架",
        "tech_features": [
            "15.4 英寸 1080P 大屏 + U 型支架，可作轻办公本",
            "联发科 G99 + 8G + 256G 轻办公配置",
            "四扬声器 + 10000mAh 大电池",
            "1899 元千元级大屏安卓平板"
        ],
        "why_important": "千元级大屏安卓平板，主打影音 / 教育 / 轻办公，补位低价大屏市场",
        "terminal_relevance": "与手机 / 笔记本组成多屏轻办公场景",
        "vendor": "中柏（Jumper）", "model": "EZpad Max15",
        "sources": "IT之家、网易、京东",
        "remark": "无"
    },
    {
        "region": "cn", "status": "released",
        "title": "荣耀 Robot Phone 机器人手机首销",
        "stars": 5, "source": "B", "date": "2026-08-18", "domain": "手机",
        "url": "https://www.toutiao.com/article/7674795429388747306",
        "url_label": "今日头条 / 极目新闻：荣耀 Robot Phone 首销",
        "signal_type": "上市 / 首销",
        "confirm_count": "3+（今日头条 / 极目新闻 / 中关村在线）",
        "key_params": "四自由度钛合金灵巧云台（360°/秒、±0.005mm 精度）；第五代骁龙8至尊版；7060mAh 青海湖电池；6.31英寸 6800nits 屏；2亿云台主摄 + 2亿潜望 + 5000万超广角；9999 元起（16+1TB 12999 元）；08-18 首销 / 08-12 发布",
        "tech_features": [
            "机身内置可弹出机械云台，AI 自动跟拍",
            "ARRI LogC3 / Wide Gamut 3 / 11 种 Looks 电影滤镜、4K 120fps",
            "YOYO 机器人模式 + 终身 SVIP",
            "钛合金云台 + 青海湖电池，形态级创新"
        ],
        "why_important": "全球首款「机器人手机」，把具身智能机械结构塞进手机，是荣耀高端 AI 终端探路者",
        "terminal_relevance": "与平板 / 耳机共享 YOYO Agentic OS 生态，是荣耀高端 AI 终端形态创新代表",
        "vendor": "荣耀（HONOR）", "model": "Robot Phone（机器人手机）",
        "sources": "今日头条、极目新闻、中关村在线",
        "remark": "全版本首销即售罄，产能与维修备件价（主摄 3079 元）争议待解"
    },
    {
        "region": "cn", "status": "released",
        "title": "iQOO Neo11 至尊版发布即开售",
        "stars": 4, "source": "B", "date": "2026-08-18", "domain": "手机",
        "url": "https://new.qq.com/rain/a/20260818A025ZM00",
        "url_label": "腾讯数码：iQOO Neo11 至尊版发布",
        "signal_type": "上市",
        "confirm_count": "2+（腾讯数码 / 科技美学）",
        "key_params": "天玑 9500M（台积电 3nm，联发科联合定制）；9100mAh + 100W；6.83英寸 2K 144Hz 护眼超冠屏；5000万 索尼大底；IP68/IP69；225g / 8.6mm；国补 2899 元起；08-18",
        "tech_features": [
            "天玑 9500M 写入 Monster 超核引擎至 SoC 底层",
            "9100mAh 蓝海电池（实测 MOBA 13.7h）",
            "同档唯一真 2K 屏",
            "IP68/IP69 + 超冠护眼屏"
        ],
        "why_important": "中端性能旗舰以「2K 屏 + 巨电池」刷新 2500-3000 元档性价比天花板",
        "terminal_relevance": "与 iQOO 家族共用蓝海电池与电竞调校，承接手机换机需求",
        "vendor": "iQOO（vivo）", "model": "Neo11 至尊版",
        "sources": "腾讯数码、科技美学",
        "remark": "无"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为 WATCH GT 7 系列上市",
        "stars": 4, "source": "B", "date": "2026-08-05", "domain": "智能手表",
        "url": "https://m.zol.com.cn/article/12264362.html",
        "url_label": "中关村在线：华为 WATCH GT 7 系列",
        "signal_type": "上市",
        "confirm_count": "2+（中关村在线 / 华为官方）",
        "key_params": "标准版 46mm / Pro 版 41mm；3000 尼特峰值亮度；高硅叠片异形电池（典型 1-2 周续航）；钛合金表体 + 纳米微晶陶瓷圈 + 蓝宝石镜；64GB 存储；08-05 发布",
        "tech_features": [
            "新一代玄玑感知系统（心率 / 体温 / 血氧 + 疲劳评估 + 高原预警）",
            "首发室内滑雪模式 + 腕上转弯检测 / G-Force",
            "爬坡规划 + 智能急弯提醒 + 高尔夫坡度补偿",
            "钛合金 + 蓝宝石 + 陶瓷，高端材质"
        ],
        "why_important": "GT 系列延续「颜值 + 长续航 + 专业运动健康」，巩固华为腕戴出货第一地位",
        "terminal_relevance": "与华为手机 / 平板 / 鸿蒙协同，健康数据跨端流转",
        "vendor": "华为（Huawei）", "model": "WATCH GT 7 系列",
        "sources": "中关村在线、华为官方",
        "remark": "具体国行售价各版本差异待补充"
    },
    {
        "region": "cn", "status": "released",
        "title": "小米 REDMI Watch 6 活力版发布",
        "stars": 3, "source": "B", "date": "2026-08-20", "domain": "智能手表",
        "url": "https://www.toutiao.com/article/7675943766447931923/",
        "url_label": "今日头条 / 华商网：REDMI Watch 6 活力版",
        "signal_type": "上市",
        "confirm_count": "2+（今日头条 / 华商网）",
        "key_params": "1.85英寸方屏；1200nits 局部峰值亮度；470mAh（至长 18 天）；9.9mm 轻薄；140+ 运动模式；349 元；08-20 发布并开售",
        "tech_features": [
            "高亮方屏 + 9.9mm 轻薄潮流外观",
            "470mAh 长续航 18 天",
            "多维健康管理 + 140+ 运动模式",
            "349 元走量定价"
        ],
        "why_important": "349 元价位把高亮大屏与 18 天续航下沉，是入门健康穿戴走量款",
        "terminal_relevance": "与小米 / REDMI 手机及米家生态联动，入门健康穿戴入口",
        "vendor": "小米 / 红米（Redmi）", "model": "REDMI Watch 6 活力版",
        "sources": "今日头条、华商网（IT之家）",
        "remark": "无"
    },
    {
        "region": "cn", "status": "released",
        "title": "雷鸟 V4 拍摄眼镜 32GB 版上市",
        "stars": 4, "source": "A", "date": "2026-08-21", "domain": "AR-VR眼镜",
        "url": "https://www.news.cn/tech/20260821/1329d3f89e064ea1a60ee2a9c0aed9c3/c.html",
        "url_label": "新华网：雷鸟 V4 拍摄眼镜 32GB 版",
        "signal_type": "上市",
        "confirm_count": "2+（新华网 / 雷鸟官方）",
        "key_params": "雷鸟创新 V4 拍摄眼镜 32GB 版；2026-08-21 与 iO 同期推出；国补后 1699 元（iO 售价 2499 元 / 首发 1996 元起）",
        "tech_features": [
            "与 iO 同场发布，承接雷鸟拍摄眼镜产品线",
            "32GB 存储版本",
            "雷鸟自研光波导 + 影像能力延续",
            "在 iO 之外提供带拍摄能力的 AR 眼镜选择"
        ],
        "why_important": "在 iO 主打「无摄像头 AI 日常化」之外，提供带拍摄能力的 AR 眼镜选择，完善雷鸟产品矩阵",
        "terminal_relevance": "拍摄素材可跨手机 / 云协同，布局「眼镜上的 AI 入口」",
        "vendor": "雷鸟创新（TCL 孵化）", "model": "雷鸟 V4 拍摄眼镜 32GB 版",
        "sources": "新华网、雷鸟官方",
        "remark": "V4 具体光学 / 重量 / 拍摄参数官方未随文详列，待补充"
    },
    {
        "region": "cn", "status": "released",
        "title": "李未可 X-AI 记忆眼镜发布（WAIC）",
        "stars": 4, "source": "B", "date": "2026-07-20", "domain": "AR-VR眼镜",
        "url": "https://dy.163.com/article/L2A3IVRE0526LS4I.html",
        "url_label": "网易 / VR陀螺：李未可 X-AI 记忆眼镜",
        "signal_type": "上市（WAIC 首发）",
        "confirm_count": "2+（网易 / VR陀螺）",
        "key_params": "售价 799 元起；主体约 26 克；透明镜腿 + 快拆镜框；约 10 克磁吸摄像模组（1200 万像素 / 1440P）；机身 4mic（装模组后 6mic）；10h+ 录音 / 约 30 天待机；07-20 WAIC 发布",
        "tech_features": [
            "全球首款以「长期记忆」定义的 AI 眼镜（WakeeMemory OS）",
            "主动式场景感应自动启停记录",
            "摄像模组可拆下形成隐私边界",
            "联动腾讯云 WorkBuddy 生成文档 / PPT / 日程"
        ],
        "why_important": "把 AI 眼镜从「拍摄工具」升级为「个人记忆终端」，低价切入记忆赛道",
        "terminal_relevance": "记录—理解—召回—执行链路与手机 / 云协同，补位可穿戴 AI 入口",
        "vendor": "李未可（LAWK）", "model": "X-AI 记忆眼镜",
        "sources": "网易、VR陀螺",
        "remark": "属 WAIC（7 月）发布，略早于 7 日窗口，但为近 60 天内国产 AR 代表新品"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为 MateBook Pro（麒麟 X90 Plus）开售",
        "stars": 4, "source": "B", "date": "2026-08-14", "domain": "笔记本",
        "url": "https://www.163.com/dy/article/L3J8D6EC0511CPVM.html",
        "url_label": "快科技 / 网易：华为 MateBook Pro",
        "signal_type": "上市",
        "confirm_count": "2+（快科技 / 网易）",
        "key_params": "麒麟 X90 Plus 高性能 PC 处理器；40W 性能释放；970g；14.2英寸 3:2 OLED 3120×2080 120Hz（1000nits）；70Wh（10.2h）；140W 快充 + 66W 反向；3×USB-C；星闪；9999 元起；08-14 开售",
        "tech_features": [
            "云隼架构 + 泡沫铜 VC 实现 970g 机身 40W 释放",
            "HarmonyOS PC + 盘古端侧大模型（文档摘要 / 会议转写）",
            "云晰柔光屏版本",
            "星闪 + 140W 快充 + 66W 反向供电"
        ],
        "why_important": "鸿蒙 PC 第二阶段高性能生产力旗舰，国产 ARM 笔记本标杆",
        "terminal_relevance": "与华为手机 / 平板 / 手表鸿蒙多端协同，AI 办公闭环",
        "vendor": "华为（Huawei）", "model": "MateBook Pro（麒麟 X90 Plus）",
        "sources": "快科技、网易",
        "remark": "无"
    },
    {
        "region": "cn", "status": "released",
        "title": "联想 2026 款 ThinkPad E13 上架",
        "stars": 3, "source": "B", "date": "2026-08-20", "domain": "笔记本",
        "url": "https://new.qq.com/rain/a/20260821A088TU00",
        "url_label": "腾讯 / IT之家：联想 ThinkPad E13 2026",
        "signal_type": "上市",
        "confirm_count": "2+（腾讯 / IT之家）",
        "key_params": "酷睿 Ultra 5 226V；16GB 内存；512GB SSD；13英寸屏；1.21kg；6999 元；08-20 上架",
        "tech_features": [
            "酷睿 Ultra 5 226V 低功耗能效比",
            "1.21kg 商务轻薄",
            "ThinkPad 商务键盘与稳定性",
            "开学换机季主流补位"
        ],
        "why_important": "主流商务轻薄本补位，承接开学换机季",
        "terminal_relevance": "与联想手机 / 平板组成 AI 终端办公矩阵，跨端文件协同",
        "vendor": "联想（Lenovo）", "model": "ThinkPad E13 2026",
        "sources": "腾讯、IT之家",
        "remark": "屏幕分辨率 / 刷新率等细节待补充"
    },
    {
        "region": "cn", "status": "released",
        "title": "联想 YOGA Air 14 2026 新增 Ultra7 266V 版",
        "stars": 4, "source": "B", "date": "2026-08-22", "domain": "笔记本",
        "url": "https://www.toutiao.com/article/7676817442403992100/",
        "url_label": "IT之家：联想 YOGA Air 14 2026 新增 Ultra7 266V",
        "signal_type": "上市",
        "confirm_count": "3+（IT之家 / 超能网 / ITBear）",
        "key_params": "酷睿 Ultra 7 266V（Lunar Lake，8 核 8 线程，118 TOPS）；16GB LPDDR5x-8533；1TB PCIe4.0；14英寸 2880×1800 OLED 触控 120Hz HDR 1100nits；70Wh；1.2kg / 13.9mm；Wi-Fi 7；9999 元；08-22 开售",
        "tech_features": [
            "Lunar Lake Ultra7 266V 118 TOPS 端侧 AI 算力",
            "14\" 2.8K OLED 触控 120Hz + 1100nits HDR",
            "Wi-Fi 7 + 70Wh 办公续航 10.6h",
            "PUREBRIGHT 珍宝工艺，1.2kg / 13.9mm 轻薄"
        ],
        "why_important": "轻薄本引入 118 TOPS 端侧 AI 与高色准 OLED，面向创作 / 办公 AI 场景",
        "terminal_relevance": "与联想手机 / 平板 / ThinkPad 组成多端 AI 办公生态",
        "vendor": "联想（Lenovo）", "model": "YOGA Air 14 2026（Ultra7 266V）",
        "sources": "IT之家、超能网、ITBear",
        "remark": "补贴价 8500 元，内存 16GB 为板载不可扩"
    },
    {
        "region": "cn", "status": "coming",
        "title": "红魔氘锋 80W 桌面风冷无线充电座预热",
        "stars": 3, "source": "C", "date": "2026-08-19", "domain": "无线充",
        "url": "https://www.chongdiantou.com/archives/1787110837659.html",
        "url_label": "充电头网：红魔氘锋 80W 风冷无线充",
        "signal_type": "预热 / 展示",
        "confirm_count": "2+（充电头网 / 红魔官方）",
        "key_params": "斜立式支架（横竖屏）；红魔 11 Pro+ 最高 80W 无线快充（需配 120W 充电器）；其他设备最高 7.5W；内置 5000 转高速风扇；过充 / 过温 / 过流 / 过压 / 异物检测；08-19 嘉年华预热",
        "tech_features": [
            "80W 高功率风冷无线充",
            "支架形态兼顾充电与观影 / 游戏",
            "多重安全保护持续散热",
            "红魔 80W 无线快充协议匹配"
        ],
        "why_important": "把手机无线充功率推到 80W 并解决发热，推动高功率无线充普及",
        "terminal_relevance": "与红魔手机 80W 无线快充协议匹配，完善电竞桌面生态",
        "vendor": "红魔（RedMagic）", "model": "红魔氘锋 80W 桌面风冷无线充电座",
        "sources": "充电头网、红魔官方",
        "remark": "正式发售日期与零售价待深圳充电嘉年华（9-19）公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "天猫精灵 IN 糖 6 智能音箱发布",
        "stars": 3, "source": "B", "date": "2026-08-05", "domain": "智能音箱",
        "url": "https://www.top168.com/news/show-26454.html",
        "url_label": "头部财经：天猫精灵 IN 糖 6 发布",
        "signal_type": "上市",
        "confirm_count": "2+（天猫精灵官方 / 头部财经）",
        "key_params": "圆形像素屏（可换壁纸、「跳科目三」动态）；黑糖 / 奶糖 / 橘糖配色；周深礼盒版；标价 666 元；08-05 发布",
        "tech_features": [
            "像素屏动态交互（科目三等）",
            "天猫精灵 AI 语音助手 + 生态联动",
            "周深礼盒版粉丝向差异化",
            "千元内带屏智能音箱"
        ],
        "why_important": "千元内带屏智能音箱以「萌系交互」拉动换机",
        "terminal_relevance": "接入阿里天猫精灵智能家居中枢，与手机 / 家电语音联动",
        "vendor": "天猫精灵（阿里）", "model": "IN 糖 6",
        "sources": "天猫精灵官方、头部财经",
        "remark": "音频单元 / 功率等完整参数未披露"
    },
    # ========== 国际 15 条 ==========
    {
        "region": "intl", "status": "coming",
        "title": "Samsung Galaxy Tab S12 Ultra 确认 H2 发布",
        "stars": 4, "source": "B", "date": "2026-08-02", "domain": "平板",
        "url": "https://www.news18.com/tech/samsung-galaxy-tab-s12-series-confirmed-as-plus-model-nears-launch-ws-l-10243438.html",
        "url_label": "News18：三星 Galaxy Tab S12 Ultra",
        "signal_type": "预告（财报电话会官宣）",
        "confirm_count": "2+（News18 / 三星移动高管）",
        "key_params": "14.6\" Dynamic AMOLED 2X 120Hz；MediaTek Dimensity 9500 / 9500+；12GB+256GB；IP68 S Pen；45W 快充；Android 17 / One UI 9；Wi-Fi 7 + 5G；预期约 $1,400",
        "tech_features": [
            "旗舰天玑 9500 / 9500+ 强化端侧 AI 图像处理",
            "14.6\" AMOLED 2X 120Hz 大屏 + 附带 IP68 S Pen",
            "7 代 Android 升级 + 7 年安全更新",
            "对标 iPad Pro 的高端安卓平板旗舰"
        ],
        "why_important": "三星将安卓平板旗舰节奏押注 2026 下半年，直接对标 iPad Pro，巩固安卓高端平板阵营",
        "terminal_relevance": "与 Galaxy S26、Galaxy Watch Ultra 2 组成三星下半年高端矩阵，共享 Galaxy AI 与 DeX",
        "vendor": "三星（Samsung）", "model": "Galaxy Tab S12 Ultra",
        "sources": "News18、三星移动体验高管（Q3 财报电话会）",
        "remark": "标准版 S12 已确认取消，系列仅 Plus + Ultra；屏幕 / 电池细节仍来自泄露"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Samsung Galaxy Tab S12+ 多国认证",
        "stars": 4, "source": "C", "date": "2026-08-18", "domain": "平板",
        "url": "https://samsung.gadgethacks.com/news/samsung-galaxy-tab-s12-plus-leak-no-base-model-in-2026-lineup/",
        "url_label": "Gadget Hacks：Galaxy Tab S12+ 泄露",
        "signal_type": "认证（FCC / 印度 BIS / 韩国安全）",
        "confirm_count": "2+（Gadget Hacks / Notebookcheck）",
        "key_params": "12. 4\" QHD+ OLED 120Hz；Dimensity 9500+；12GB+256GB；10,392mAh（典型 ~10,500mAh）+ 45W；IP68 S Pen；Android 17；型号 SM-X840 / X846B / X848U；5G + Wi-Fi 7 + BT 6.0",
        "tech_features": [
            "FCC 认证 SM-X848U，确认 S Pen 与快充",
            "12.4\" AMOLED 2X 120Hz + IP68 防水 S Pen",
            "7 代 Android + 7 年安全更新",
            "S12+ 成为 S 系列新入门档（标准版取消）"
        ],
        "why_important": "S12+ 承担走量重任，定价配置影响中高价位竞争",
        "terminal_relevance": "与 S12 Ultra、Galaxy S26 FE 同台 Galaxy Unpacked，延续 DeX 多端协同",
        "vendor": "三星（Samsung）", "model": "Galaxy Tab S12+",
        "sources": "Gadget Hacks、Notebookcheck",
        "remark": "最终售价与确切发布日未定，预计 2026 年 8–9 月 Galaxy Unpacked"
    },
    {
        "region": "intl", "status": "released",
        "title": "HP OmniPad 12 印度首发",
        "stars": 3, "source": "C", "date": "2026-08-11", "domain": "平板",
        "url": "https://odishastand.com/hp-omnipad-12-launch-india-price-specs",
        "url_label": "Odisha Stand：HP OmniPad 12 发布",
        "signal_type": "上市",
        "confirm_count": "2+（Odisha Stand / Deccan Herald）",
        "key_params": "12\" 2K（2000×1200）90Hz 400nits；Snapdragon 6 Gen 3；8GB + 128/256GB（可扩 1TB）；Android 16；31Wh（约 18h）；600g；13MP + 8MP；可拆卸键盘；Rs 48,999 起",
        "tech_features": [
            "12\" 2K 90Hz 触控 + 可拆卸键盘（平板 / 笔记本双模）",
            "骁龙 6 Gen3 + Android16，预装 AI 套件（GPT5 / Claude4 / Gemini 年包）",
            "EPEAT Silver + ENERGY STAR，Wi-Fi 6E",
            "印度首发 2-in-1 安卓平板"
        ],
        "why_important": "HP 以印度首发 2-in-1 安卓平板切入学生与中小企业，标志传统 PC 厂加码 AI 平板",
        "terminal_relevance": "搭 Gemini 等云端 AI 订阅包，可作安卓手机 / Chromebook 外接生产力屏",
        "vendor": "惠普（HP）", "model": "OmniPad 12",
        "sources": "Odisha Stand、Deccan Herald",
        "remark": "印度市场特供首发，全球其他区域上市时间未公布；AI 软件包为限时促销"
    },
    {
        "region": "intl", "status": "released",
        "title": "Microsoft Surface Pro 12（2026）上市",
        "stars": 4, "source": "C", "date": "2026-07-14", "domain": "平板",
        "url": "https://www.windowsnews.ai/article/surface-pro-12-debuts-with-snapdragon-x2-1499-and-copilot-ai-features.426929",
        "url_label": "Windows News AI：Surface Pro 12",
        "signal_type": "上市（企业 SKU / 国行 / 5G 版）",
        "confirm_count": "2+（Windows News AI / 微软官方）",
        "key_params": "13\" PixelSense Flow 120Hz（可选 OLED / LCD）；Snapdragon X2 Plus（10 核）/ X2 Elite（12 核）；16GB–64GB LPDDR5X；Hexagon NPU 45+ TOPS；双 USB4 / Thunderbolt 5；15.5h；$1,499 起",
        "tech_features": [
            "独占骁龙 X2，NPU 45+ TOPS 驱动 Copilot+ 本地 AI（Recall / Live Captions / Studio Effects）",
            "可选 OLED 13\" 120Hz + 触控笔",
            "无风扇被动散热、15.5h 续航",
            "5G 版 8 月上市"
        ],
        "why_important": "微软将 Windows on Arm 推进到主流价位并首供 OLED，标志 ARM 平板 / 笔记本成熟",
        "terminal_relevance": "Copilot+ PC 与 Pixel / Galaxy 等端侧 AI 终端同处「本地大模型」竞争主线",
        "vendor": "微软（Microsoft）", "model": "Surface Pro 12（2026）",
        "sources": "Windows News AI、微软官方",
        "remark": "消费版全球发售日 2026-06-16 略超窗口；企业 SKU / 国行 / 5G 版在窗口内"
    },
    {
        "region": "intl", "status": "released",
        "title": "Google Pixel 11 发布开售",
        "stars": 4, "source": "B", "date": "2026-08-20", "domain": "手机",
        "url": "https://9to5google.com/2026/08/12/made-by-google-2026-announcements/",
        "url_label": "9to5Google：Made by Google 2026",
        "signal_type": "发布 / 上市",
        "confirm_count": "3+（9to5Google / PhoneArena）",
        "key_params": "6.3\" Actua OLED 120Hz 3000nits；Tensor G6（3nm）+ Titan M3；12GB+256GB 起；4985mAh；30W 有线 + 25W Qi2.2 Pixelsnap；Android 17；IP68；48MP 主 + 13MP 超广 + 10.8MP 5x；₹89,999 / $899",
        "tech_features": [
            "首发 Tensor G6，端侧 Gemini Nano 4（算力 +50%、带宽 2×）",
            "全系 25W Qi2.2 磁吸无线（较上代 15W 提速）",
            "更薄玻璃相机条、30x SuperRes Zoom、7 年系统 / 安全更新",
            "50MP + 13MP + 10.8MP 三摄"
        ],
        "why_important": "Pixel 11 将 2nm 级 Tensor G6 与 7 年更新带入主流价位，确立 Google 硬件 AI 化标杆",
        "terminal_relevance": "与 Pixel Watch 5、Pixelsnap 配件、Google Home Speaker 共用 Gemini 生态",
        "vendor": "Google", "model": "Pixel 11",
        "sources": "9to5Google、PhoneArena",
        "remark": "₹89,999 为印度定价，美国起售 $899；部分 AI 功能受地区 / 语言限制"
    },
    {
        "region": "intl", "status": "released",
        "title": "Google Pixel 11 Pro 发布",
        "stars": 4, "source": "B", "date": "2026-08-19", "domain": "手机",
        "url": "https://www.phonearena.com/phones/Google-Pixel-11-Pro_id12940",
        "url_label": "PhoneArena：Google Pixel 11 Pro",
        "signal_type": "发布 / 上市",
        "confirm_count": "2+（PhoneArena / 9to5Google）",
        "key_params": "6.3\" Super Actua OLED 1–120Hz 3600nits；Tensor G6；12GB（256）/ 16GB（512–1TB）；4850mAh；30W 有线 + 25W Qi2.2；Android 17；IP68；50MP 主 + 48MP 超广 + 48MP 5x 潜望（120x Pro Zoom）；42MP 前摄；HiLight 环；$1,099 起",
        "tech_features": [
            "50MP + 48MP + 48MP 三摄，5x 光学 + 120x Pro Zoom，8K 视频",
            "HiLight 环形环境灯（face-down 也能提示 Gemini / 来电）",
            "Tensor G2 + Titan M3，7 年更新，全系 25W Qi2.2",
            "42MP 前摄"
        ],
        "why_important": "Pro 以 120x 变焦与 HiLight 交互刷新安卓影像与形态创新，巩固高端定位",
        "terminal_relevance": "与 Pixel 11 / Watch 5 / Pixelsnap 组 Gemini 全家桶，HiLight 与 Google Home Speaker 灯光语言互通",
        "vendor": "Google", "model": "Pixel 11 Pro",
        "sources": "PhoneArena、9to5Google",
        "remark": "256GB 版配 12GB RAM（较上代 16GB 缩减）；1TB 版 $1,449"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Garmin Enduro 4 多国认证完成",
        "stars": 4, "source": "C", "date": "2026-07-14", "domain": "智能手表",
        "url": "https://www.smartwearables.io/news/garmin-fenix-9-enduro-4-indonesian-telecom-filings-three-models-launch-imminent-august-2026",
        "url_label": "Smart Wearables：Garmin Enduro 4",
        "signal_type": "量产（多国认证完成）",
        "confirm_count": "2+（Smart Wearables / FCC / 印尼电信）",
        "key_params": "型号 A05216（FCC ID IPH-05216）；transflective MIP 太阳能屏；双频 Wi-Fi（首搭 5GHz）；ANT+；预期 90–100+ 天续航（太阳能）；无蜂窝 / 卫星；预期约 $999",
        "tech_features": [
            "FCC + 印尼电信 / 韩国 NRRA 多国认证完成，Connect App 代码现 \"Enduro_4\"",
            "延续 MIP 太阳能（非 AMOLED），主打极致续航与超耐力",
            "双频 Wi-Fi 为新硬件代际，传输更快",
            "与 Fenix 9 同窗发布"
        ],
        "why_important": "Enduro 4 延续 Garmin 超长续航户外表节奏，直击 Apple Watch Ultra / Galaxy Watch Ultra 续航短板",
        "terminal_relevance": "与 Fenix 9 同窗发布，补全 Garmin 户外旗舰矩阵，可与手机健康 App 深度联动",
        "vendor": "Garmin", "model": "Enduro 4",
        "sources": "Smart Wearables、FCC、印尼电信",
        "remark": "具体屏幕 / 电池数字未官宣，价格与 8–9 月发布日为供应链预测"
    },
    {
        "region": "intl", "status": "released",
        "title": "Garmin CIRQA 无屏健康带上市",
        "stars": 3, "source": "B", "date": "2026-08-06", "domain": "智能手表",
        "url": "https://techradar.com/health-fitness/fitness-trackers/garmin-cirqa-review",
        "url_label": "TechRadar：Garmin CIRQA 评测",
        "signal_type": "上市",
        "confirm_count": "2+（TechRadar / Garmin 官方）",
        "key_params": "无屏织物健身带；21g；约 1 周续航（每周 3–4 次训练）；Garmin Elevate V4 心率阵列（HRV / Pulse Ox）；4 色；侧边实体按钮；$199.99 / £179.99 / AU$299.99；无强制订阅",
        "tech_features": [
            "无屏幕极简设计 + 织物表带，主打「少干扰」健康追踪",
            "Elevate V4：睡眠分期、HRV、血氧、训练就绪、身体电量、VO2 Max、健身年龄",
            "自动活动检测（>15 分钟）、智能唤醒闹钟",
            "Connect App 免费数据层丰富"
        ],
        "why_important": "CIRQA 是 Garmin 首次以「无屏健康带」切入极简穿戴，拓展非手表形态健康监测",
        "terminal_relevance": "数据沉淀 Garm  in Connect，可与手机 / Garmin 手表 / 码表形成健康数据中台",
        "vendor": "Garmin", "model": "CIRQA",
        "sources": "TechRadar、Garmin 官方",
        "remark": "原文未宣传防水等级；AI 教练 / 营养追踪为付费项"
    },
    {
        "region": "intl", "status": "released",
        "title": "VITURE Pro 2 AR 眼镜上市",
        "stars": 4, "source": "A", "date": "2026-08-06", "domain": "AR-VR眼镜",
        "url": "https://www.viture.com/en-SG/blog/best-smart-glasses-2026-viture-wins-both-ar-xr-glasses-crowns-flagship-and-budget",
        "url_label": "VITURE 官方：Pro 2 获双榜最佳",
        "signal_type": "上市",
        "confirm_count": "2+（VITURE 官方 / Tom's Guide / PCMag）",
        "key_params": "XR/AR 眼镜；单眼 1920×1080 Sony Micro-OLED；50° FOV；1600nits；120Hz；等效 146\" 巨幕；63g；0–500° 独立近视调节；USB-C DP 直连；UltraClarity 3.0；$299 / ¥1999",
        "tech_features": [
            "Sony Micro-OLED + UltraClarity 3.0，1600nits 户外可见",
            "双眼独立 0–500° 近视调节无需插片，63g 轻量",
            "SpaceWalker 支持 2D→3D、360° VR、多屏 / 空间视频",
            "兼容 Switch2 / PS / Xbox / PC / 手机"
        ],
        "why_important": "VITURE Pro 2 以 $299 拿下 Tom's Guide / PCMag 双「最佳入门 AR 眼镜」，把虚拟巨幕压到千元档",
        "terminal_relevance": "通过 USB-C DP 直连手机 / 掌机 / 笔记本，是移动游戏与影音终端的「外接第二屏」",
        "vendor": "VITURE", "model": "Pro 2",
        "sources": "VITURE 官方、Tom's Guide、PCMag",
        "remark": "中国首发 ¥1999（2026-08-06），海外 $299；Ultra 接收器（Switch2 适配）另售 $399"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Snap Spectacles（Specs）独立 AR 眼镜 9/16 发布",
        "stars": 5, "source": "B", "date": "2026-09-16", "domain": "AR-VR眼镜",
        "url": "https://www.androidheadlines.com/2026/07/snap-confirms-september-16-launch-event-for-specs-ar-glasses.html",
        "url_label": "Android Headlines：Snap Specs 9/16 发布",
        "signal_type": "预告 / 发布活动",
        "confirm_count": "2+（Android Headlines / Snap 财报）",
        "key_params": "消费级独立 AR 眼镜；自研 LCoS 显示，51° FOV，1600 万色；电致变色镜片（10 秒透明↔墨镜）；双高通骁龙；4h 混合续航（充电盒至 20h）；132–136g；47/52mm 两尺寸；OpenAI + Google AI；$2,195；9/16 洛杉矶发布",
        "tech_features": [
            "完全独立（无手机 / 线缆），双骁龙分别负责计算机视觉与 AR 渲染",
            "LCoS 见透显示 + 51° FOV + 电致变色，叠加数字内容于现实",
            "情境感知 AI（实时导航 / 翻译 / 帮助）+ 数百款 AR Lens，预购已开",
            "132–136g 轻量"
        ],
        "why_important": "Specs 是 Snap 首款面向大众的 standalone AR 眼镜，以 $2,195 切入下一代计算平台，对标 Vision Pro 形态",
        "terminal_relevance": "与手机 / 社交生态绑定，AR Lens 开发依赖移动端工具，是「手机外延 AR」代表",
        "vendor": "Snap", "model": "Spectacles（Specs）",
        "sources": "Android Headlines、Snap 财报电话会",
        "remark": "9/16 为深度展示而非开售；实际发货 2026 秋季且仅美 / 英 / 法"
    },
    {
        "region": "intl", "status": "released",
        "title": "Asus ROG Zephyrus Duo 2026（GX651）发售",
        "stars": 5, "source": "A", "date": "2026-08-20", "domain": "笔记本",
        "url": "https://rog.asus.com/si/laptops/rog-zephyrus/rog-zephyrus-duo-2026/spec",
        "url_label": "ASUS ROG 官方：Zephyrus Duo 2026",
        "signal_type": "上市",
        "confirm_count": "2+（ASUS ROG 官方 / Notebookcheck）",
        "key_params": "16\" 3K（2880×1800）OLED 120Hz ROG Nebula HDR；Intel Core Ultra 9 386H（Panther Lake）；RTX 5090 24GB GDDR7；64GB LPDDR5X-8533；2TB PCIe5.0 SSD；双屏（副屏触控）；90Wh；250W；Wi-Fi 7 / BT 6.0；2.82kg；~€6,700",
        "tech_features": [
            "Panther Lake + RTX 5090 双屏电竞，主副双 OLED 触控，5 种使用模式",
            "64GB 板载 LPDDR5X + PCIe5.0 SSD，Intel NPU 50 TOPS",
            "Slash Lighting 灯效 + ROG 智能散热（均温板 + 双风扇）",
            "Copilot 键"
        ],
        "why_important": "2026 旗舰双屏创作 / 游戏本，把桌面级 RTX 5090 塞入轻薄机身，定义高端移动算力",
        "terminal_relevance": "与 Pixel / Galaxy 等同处「本地大模型 + 高算力」主线，Intel NPU 50 TOPS 支撑 Copilot+",
        "vendor": "华硕（ASUS）", "model": "ROG Zephyrus Duo 2026（GX651）",
        "sources": "ASUS ROG 官方、Notebookcheck",
        "remark": "多地陆续开售，价格随配置浮动；部分市场先上 32GB 版"
    },
    {
        "region": "intl", "status": "released",
        "title": "Dell 15（D15266）国际发售",
        "stars": 3, "source": "B", "date": "2026-08-19", "domain": "笔记本",
        "url": "https://www.notebookcheck.net/Dell-releases-new-15-inch-laptop-internationally-with-AMD-Ryzen-processors-and-up-to-32-GB-RAM.1373226.0.html",
        "url_label": "Notebookcheck：Dell 15 发售",
        "signal_type": "上市",
        "confirm_count": "2+（Notebookcheck / Dell 官方）",
        "key_params": "15.3\" IPS 1200p 16:10 400nits 60Hz；AMD Ryzen 3 210 / 5 220 / 7 250；8–32GB DDR5-5600（可升级）；512GB–1TB M.2；54Wh；1.54kg；起价 ~$740；亚太 / 大洋洲首发",
        "tech_features": [
            "15.3\" 16:10 400nits 屏，Ryzen 200 系列三档可选",
            "RAM / SSD 用户可升级（DDR5-5600 + M.2 2230）",
            "54Wh 续航优先（为保续航刷新率定 60Hz）",
            "Ryzen AI 核可承载轻量端侧 AI"
        ],
        "why_important": "Dell 以可升级 RAM / SSD 的主流 15\" 本回应「焊接内存」趋势，主打性价比与可维护性",
        "terminal_relevance": "与手机 / 平板组多终端办公，Ryzen AI 核可承载轻量端侧 AI 任务",
        "vendor": "戴尔（Dell）", "model": "Dell 15（D15266）",
        "sources": "Notebookcheck、Dell 官方",
        "remark": "现仅部分亚太 / 大洋洲发售，美国等后续上线"
    },
    {
        "region": "intl", "status": "released",
        "title": "Google Pixelsnap Charger（Qi2.2 25W）上市",
        "stars": 3, "source": "B", "date": "2026-08-12", "domain": "无线充",
        "url": "https://9to5google.com/2026/08/07/deals-pixelsnap-charger-galaxy-a57-nothing-phone/",
        "url_label": "9to5Google：Google Pixelsnap Charger",
        "signal_type": "上市",
        "confirm_count": "2+（9to5Google / 官方）",
        "key_params": "官方 Qi2.2 磁吸无线充电器；最高 25W；带 / 不带支架两版（$39.99 / $69.99）；磁吸对齐 + 竖 / 横摆放；兼容 Pixel 11 全系及任意 Qi2 设备；1m 集成 USB-C 线",
        "tech_features": [
            "首发 Qi2.2（即 Qi2 25W），较 Qi2 的 15W 提升明显",
            "磁吸对齐，Pixel 11 全系（含 Fold）支持 25W",
            "支架版可竖 / 横停靠显示屏保 / 天气 / 智能家居控件",
            "需自备 ≥30W USB-C 适配器"
        ],
        "why_important": "Google 首次在 Pixel 全线铺开 25W 磁吸无线快充，标志安卓阵营正式拥抱 Qi2.2",
        "terminal_relevance": "直接服务 Pixel 11 / Pro / Fold 的 Pixelsnap 磁吸生态，与手机 / 手表 / 耳机组磁吸充电矩阵",
        "vendor": "Google", "model": "Pixelsnap Charger（Qi2.2 25W）",
        "sources": "9to5Google、Google 官方",
        "remark": "兼容 Pixel 10 系列与 iPhone 17；裸充版 $39.99"
    },
    {
        "region": "intl", "status": "released",
        "title": "Belkin Qi2.2 25W 三合一磁吸充电站",
        "stars": 3, "source": "C", "date": "2026-08-17", "domain": "无线充",
        "url": "https://sammyguru.com/belkin-qi2-2-25w-magnetic-charging-stand-deal-59-amazon",
        "url_label": "SammyGuru：Belkin Qi2.2 三合一",
        "signal_type": "上市（历史最低价）",
        "confirm_count": "2+（SammyGuru / 亚马逊在售）",
        "key_params": "Belkin Qi2.2 25W Magnetic Wireless Charging Station（3-in-1）；手机磁吸臂 + 手表位 + 耳机位；含 45W 电源与 5ft C-C 线；黑 / 蓝 / 白；现价 $59.99（原价约 $99.99）；回收塑料机身，2 年质保",
        "tech_features": [
            "Qi2.2 25W，较 Qi2 15W 翻倍，支持 Galaxy S26 Ultra / Z Fold8 / Pixel 11",
            "三设备同充（手机 + 手表 + 耳机），磁吸臂 + 硅胶定位环",
            "折叠便携，45W 套装出厂即配",
            "回收塑料机身"
        ],
        "why_important": "第三方大厂率先把 Qi2.2 25W 三合一做成主流价，加速安卓 / 苹果跨生态磁吸快充普及",
        "terminal_relevance": "同时服务 Galaxy / Pixel / iPhone 17 等多品牌终端，是「多设备无线充电中枢」代表",
        "vendor": "Belkin", "model": "Qi2.2 25W 三合一磁吸充电站",
        "sources": "SammyGuru、亚马逊",
        "remark": "Galaxy 手机需磁吸壳或附赠硅胶环；手表位兼容性因型号而异"
    },
    {
        "region": "intl", "status": "released",
        "title": "Google Home Speaker（Gemini Nano）上市",
        "stars": 4, "source": ", B".replace(", ", ""), "date": "2026-08-04", "domain": "智能音箱",
        "url": "https://techtimes.com/articles/323216/20260805/google-home-speaker-lands-germany-gemini-device-thread-spec-already-outdated.htm",
        "url_label": "TechTimes：Google Home Speaker 德国上市",
        "signal_type": "上市",
        "confirm_count": "2+（TechTimes / Google 官方）",
        "key_params": "360° 智能音箱；58mm 全频单元；3 远场麦克风 + 硬件静音开关；四核 ARM Cortex-A55 2GHz + 专用 NPU（本地 Gemini Nano）；1GB RAM / 4GB 闪存；Wi-Fi 6 + BT 5.4；Thread 1.3；€119.99 / $99.99；黑 / 白",
        "tech_features": [
            "首款为 Gemini 从零设计的 Google 音箱，本地 NPU 跑 Gemini Nano，响应 <100ms",
            "58mm 360° 单元 + 底座光环，可立体声配对 / 接 Google TV 组环绕",
            "Thread 1.3 + Matter 中枢，Google Home Premium（€10/月）解锁 Gemini Live",
            "硬件静音开关"
        ],
        "why_important": "Google 六年来首款新智能音箱，以端侧大模型重塑语音助手，迎战 Alexa+ / Siri AI",
        "terminal_relevance": "与 Pixel 11 的 HiLight、Gemini 生态联动，是家庭场景「始终在线 AI 入口」",
        "vendor": "Google", "model": "Google Home Speaker（Gemini Nano）",
        "sources": "TechTimes、Google 官方",
        "remark": "全球首发 6/25 距窗口约 60 天临界；Thread 1.3 规格已被 Thread Group 停止认证"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 28, True),
    ("显示/OLED", 22, True),
    ("折叠屏", 0, False),
    ("手写笔/触控", 7, True),
    ("散热/液冷", 4, True),
    ("电池/续航", 18, True),
    ("快充/无线充", 13, True),
    ("影像", 5, True),
    ("AI/NPU", 13, True),
    ("音频/扬声器", 5, True),
    ("5G/通信", 7, True),
    ("Wi-Fi/连接", 6, True),
    ("AR/VR显示", 4, True),
    ("材质/工艺", 6, True),
    ("可持续/模块化", 3, True),
    ("手柄/外设", 7, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {"rank": 1, "title": "荣耀 Robot Phone", "dim": "形态创新", "stars": 5, "key": "全球首款机器人手机 + 钛合金云台 + 2亿相机"},
    {"rank": 2, "title": "Snap Spectacles", "dim": "AR/VR显示", "stars": 5, "key": "独立 AR 眼镜 + 双骁龙 + $2,195 + 9/16 发布"},
    {"rank": 3, "title": "Asus ROG Zephyrus Duo 2026", "dim": "AI/NPU", "stars": 5, "key": "RTX 5090 + 50 TOPS + 双屏 OLED"},
    {"rank": 4, "title": "雷鸟 V4 拍摄眼镜", "dim": "AR/VR显示", "stars": 4, "key": "A级信源 + 新华网 + 1699 元国补"},
    {"rank": 5, "title": "VITURE Pro 2", "dim": "AR/VR显示", "stars": 4, "key": "A级信源 + $299 + 1600nits + Sony Micro-OLED"},
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
              <div class="field full"><div class="field-label"">关键参数</div><div class="field-value">{c['key_params']}</div></div>
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

with open("WB_2026-08-24_硬件看板.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML 生成完成：WB_2026-08-24_硬件看板.html")
print(f"   总情报：{total} 条（国内 {cn_count} + 国际 {intl_count}）")
print(f"   维度覆盖：{dim_on}/16")
print(f"   五星条数：{five_star}")
