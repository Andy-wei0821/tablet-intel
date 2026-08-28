#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 WB_2026-08-28_硬件看板.html
做法：读取 gen_wb_2026-08-26.py 模板，替换 日期/副标题类别数(7→8)/CARDS/DIMS/TOP5，再 exec 生成。
"""
import os

TEMPLATE = r"E:\AI相关\预研究\202608\03_输出\gen_wb_2026-08-26.py"

CHUNK = r'''CARDS = [
    # ========== 国内 15 条 ==========
    {
        "region": "cn", "status": "released",
        "title": "华为 MatePad Air 2026",
        "stars": 5, "source": "B", "date": "2026-08-01", "domain": "平板",
        "url": "https://www.phonearena.com/phones/Huawei-MatePad-Air-2026_id13023",
        "url_label": "PhoneArena",
        "signal_type": "上市",
        "confirm_count": "5 个印证源",
        "key_params": "12英寸OLED 144Hz柔光屏 / 麒麟T93C / 10100mAh / 66W / 欧版849欧元起",
        "tech_features": [
            "12英寸OLED PaperMatte柔光屏，2800×1840，144Hz，1200nits峰值亮度",
            "麒麟T93C芯片（7nm），Maleoon 920A GPU，8GB+256GB / 12GB+256GB",
            "10100mAh电池+66W有线快充，机身5.3mm厚、509g重",
            "后置5000万像素主摄（F1.8，PDAF），预装HarmonyOS"
        ],
        "why_important": "华为将麒麟芯片与OLED柔光屏下放至Air系列中高端平板，直接对标iPad Air；国内约3099元起对同价位形成压力。",
        "terminal_relevance": "与华为手机/穿戴鸿蒙生态协同",
        "vendor": "华为（Huawei）", "model": "MatePad Air 2026",
        "sources": "PhoneArena",
        "remark": "全球2026-08-01出货，国内版约3099元起（欧版849欧元）"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为 MatePad SE 11 焕新版",
        "stars": 3, "source": "A", "date": "2026-07-27", "domain": "平板",
        "url": "https://item.vmall.com/product/comdetail/index.html?prdId=10086426290126&sbomCode=2701010132701",
        "url_label": "华为商城(vmall)",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "11英寸LCD 1920×1200 / 骁龙685 / 7700mAh / 1799元",
        "tech_features": [
            "11英寸TFT LCD（IPS）高刷护眼全面屏，1920×1200，SuperMotion自适应刷新率，85%屏占比",
            "高通骁龙685八核，8GB+256GB，HarmonyOS 4.2",
            "7700mAh（典型值）电池+22.5W快充，全金属一体机身，厚6.9mm、重475g",
            "四扬声器+Histen 9.0，多屏协同/平行视界/教育中心"
        ],
        "why_important": "华为入门级平板焕新版，1799元价位提供高刷护眼屏与全金属机身，主攻学生与家庭学习场景，延续鸿蒙教育生态。",
        "terminal_relevance": "与华为手机/穿戴鸿蒙生态协同",
        "vendor": "华为（Huawei）", "model": "MatePad SE 11 焕新版 (AGS6-W00)",
        "sources": "华为商城",
        "remark": "华为商城在售，2026年7月上市"
    },
    {
        "region": "cn", "status": "released",
        "title": "中兴 Axon Pad",
        "stars": 3, "source": "B", "date": "2026-08-21", "domain": "平板",
        "url": "https://detail.zol.com.cn/tablepc/zte/s10668/expensive.html",
        "url_label": "ZOL中关村在线",
        "signal_type": "报价/上市",
        "confirm_count": "4 个印证源",
        "key_params": "12.1英寸2.5K / 骁龙8+Gen1 / 5G全网通 / 2499元起",
        "tech_features": [
            "12.1英寸IPS LCD，2560×1600，120Hz刷新率",
            "高通骁龙8+ Gen1旗舰芯片，8GB+256GB / 12GB+512GB UFS 3.1",
            "5G全网通，10000mAh电池+80W快充，重605g",
            "前置1600万+后置1300万像素，四扬声器，Android 13/MyOS 13"
        ],
        "why_important": "中兴以骁龙8+Gen1旗舰芯切入大屏平板，2499元起主打性价比与5G生产力，补充国产安卓平板阵营。",
        "terminal_relevance": "与中兴手机/平板多端协同",
        "vendor": "中兴（ZTE）", "model": "Axon Pad",
        "sources": "ZOL中关村在线",
        "remark": "ZOL报价页显示2026-08-21上架，8GB+256GB ¥2499、12GB+512GB ¥2999"
    },
    {
        "region": "cn", "status": "released",
        "title": "联想小新 Pad Pro 13 2026",
        "stars": 4, "source": "A", "date": "2026-08-01", "domain": "平板",
        "url": "https://www.lenovo.com.cn/wiki/product-1053087.html",
        "url_label": "联想官方商城",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "13英寸3.5K / 骁龙8s / 10200mAh / 2599元",
        "tech_features": [
            "13英寸3.5K（3504×2190）LCD护眼屏，144Hz刷新率",
            "高通骁龙8s处理器，Android 16系统",
            "10200mAh大容量电池，Type-C接口",
            "AI学习平板定位，同系搭载天禧AI PadClaw大模型，四边等窄全面屏"
        ],
        "why_important": "联想将13英寸3.5K大屏与AI学习结合，2599元主打学生与轻办公，是国产安卓平板在AI学习方向的代表新品。",
        "terminal_relevance": "与联想手机/平板多端AI",
        "vendor": "联想（Lenovo）", "model": "小新 Pad Pro 13 2026",
        "sources": "联想官方商城",
        "remark": "联想官方知识库页（2026-08-01），参考价¥2599"
    },
    {
        "region": "cn", "status": "released",
        "title": "nova 16 SE",
        "stars": 4, "source": "B", "date": "2026-08-12", "domain": "手机",
        "url": "https://www.toutiao.com/article/7670807635604308515",
        "url_label": "今日头条",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "6.84\" 1.5K 8000nit / 麒麟8020 / 8500mAh / 2499元起",
        "tech_features": [
            "6.84英寸1.5K OLED直屏，峰值亮度8000nits，120Hz，1440Hz PWM调光",
            "麒麟8020+HarmonyOS 6.1，性能提升52%",
            "8500mAh巨鲸电池+66W快充，支持双向北斗卫星消息",
            "5000万RYYB主摄+红枫原色镜头+OIS，侧边指纹，WiFi 7/星闪2.0/蓝牙6.0"
        ],
        "why_important": "nova 16 SE以2499元起带来8500mAh超大电池与红枫影像，强化华为中端市场续航与影像竞争力。",
        "terminal_relevance": "与华为平板/穿戴鸿蒙协同",
        "vendor": "华为（Huawei）", "model": "nova 16 SE (CAS-AL50)",
        "sources": "今日头条",
        "remark": "2026-08-05发布、08-12开售；128/256/512GB分别2499/2699/3199元，国补到手2124元起"
    },
    {
        "region": "cn", "status": "released",
        "title": "OPPO A7 Pro Max",
        "stars": 4, "source": "B", "date": "2026-08-07", "domain": "手机",
        "url": "https://economy.southcn.com/node_cc06cbe708/a8a35c4e57.shtml",
        "url_label": "南方网(粤学习)",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "6.78\" 1.5K / 10000mAh七年长寿 / 2199元起",
        "tech_features": [
            "行业首个七年长寿万级大电池：10000mAh硅碳电池+80W闪充，获CQC双金标认证",
            "6.78英寸1.5K直面屏，1800nits，120Hz三档刷新，93.5%屏占比",
            "IP69K防水+超抗摔金刚石架构+航天九项/七项军标测试",
            "全场景AI防诈（通话/换脸/转账）、前后5000万影像、ColorOS 16"
        ],
        "why_important": "以\"七年长寿电池+万级容量\"重定义耐用手机赛道，2199元起将抗造与长续航做成大众卖点，引领电池寿命竞争。",
        "terminal_relevance": "与OPPO手机/平板生态",
        "vendor": "OPPO", "model": "A7 Pro Max (PYC110)",
        "sources": "南方网",
        "remark": "2026-08-04发布、08-07开售；8+128/12+256/12+512GB分别2199/2699/2999元"
    },
    {
        "region": "cn", "status": "coming",
        "title": "小米手环 11",
        "stars": 4, "source": "B", "date": "2026-08-18", "domain": "智能手表",
        "url": "https://www.toutiao.com/article/7674494713759646231/",
        "url_label": "今日头条",
        "signal_type": "预热/官宣",
        "confirm_count": "5 个印证源",
        "key_params": "1.74\" AMOLED 120Hz / 21天续航 / 299元起",
        "tech_features": [
            "1.74英寸AMOLED屏，峰值1800nit，首发120Hz高刷（手环品类罕见）",
            "标准续航21天，开启高刷+全天心率仍14天以上",
            "九轴传感器+150+运动模式，新增皮肤温度/呼吸率监测，5ATM防水",
            "HyperOS穿戴系统，小爱同学、NFC门禁/离线支付、语音录音"
        ],
        "why_important": "小米手环11以120Hz高刷与21天续航打破\"手环=低端\"刻板印象，299元起巩固国民级穿戴地位，推动品类规格升级。",
        "terminal_relevance": "与小米手机/平板澎湃智联",
        "vendor": "小米（Xiaomi）", "model": "小米手环11 (M2616B1标准版)",
        "sources": "今日头条",
        "remark": "2026-08-17官方官宣，预计2026-08-18及以后发布上市；标准版预估299元起"
    },
    {
        "region": "cn", "status": "released",
        "title": "小天才 Z7 Pro",
        "stars": 3, "source": "B", "date": "2026-07-23", "domain": "智能手表",
        "url": "https://smartwear.zol.com.cn/1220/12202426.html",
        "url_label": "ZOL中关村在线",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "紫光展锐W357 / 楼层定位4.0 / 翻转双摄 / 1169元",
        "tech_features": [
            "紫光展锐W357 4G RTOS旗舰穿戴平台，双核CPU+Arm 3D GPU，LTE Cat.4全网通",
            "楼层定位4.0：商场/地下停车场行为预测算法，常去地点守护+危险区域提醒",
            "翻转双摄：前置200万+后置500万像素，全屏视频通话",
            "旗舰级PPG光学传感器，6项运动模式（步行/跑步/骑行/游泳等）"
        ],
        "why_important": "搭载国产紫光展锐W357平台，强化楼层定位与双摄沟通，是儿童安全穿戴标杆迭代，体现国产芯片在儿童手表渗透。",
        "terminal_relevance": "智能穿戴（儿童手表）",
        "vendor": "小天才（BBK）", "model": "Z7 Pro",
        "sources": "ZOL中关村在线",
        "remark": "2026-07-23发布并上架京东，定价1169元，部分地区国补后999元"
    },
    {
        "region": "cn", "status": "released",
        "title": "闪极 loomos L1",
        "stars": 5, "source": "B", "date": "2026-08-18", "domain": "AR-VR眼镜",
        "url": "https://www.toutiao.com/article/7676018531258974758",
        "url_label": "今日头条(中国网科技)",
        "signal_type": "首发/上市",
        "confirm_count": "4 个印证源",
        "key_params": "43g / 高通W5100+恒玄BES2700 / 5秒换电 / 2699元起",
        "tech_features": [
            "航空级钛合金前框+醋酸纤维板材，整机最轻43g，前框体感19g，对标日常光学眼镜",
            "高通骁龙W5100 4nm主芯片+恒玄BES2700低功耗蓝牙异构双芯，AI记忆功耗降38%",
            "5秒极速换电：258mAh电池+充电仓补能3-4次，综合续航最长40小时（记忆模式约12h）",
            "LoomOS主动AI记忆系统：录音转写生成AI日记/待办，接入飞书与腾讯WorkBuddy"
        ],
        "why_important": "loomos L1以\"主动AI记忆+16小时佩戴\"区别于堆参数竞品，用换电与轻量化解决续航与佩戴痛点，是国产AI眼镜日常化落地样本。",
        "terminal_relevance": "AR/VR眼镜（AI拍摄眼镜）",
        "vendor": "闪极科技", "model": "loomos L1",
        "sources": "今日头条(中国网科技)",
        "remark": "2026-08-18武汉发布，首发2699-2999元（含镜片），预计2026年底大规模交付"
    },
    {
        "region": "cn", "status": "coming",
        "title": "闪极 loomos S1",
        "stars": 4, "source": "B", "date": "2026-08-18", "domain": "AR-VR眼镜",
        "url": "https://new.qq.com/rain/a/20260819A05WMN00?refer=cp_1009",
        "url_label": "腾讯新闻",
        "signal_type": "预热",
        "confirm_count": "5 个印证源",
        "key_params": "29g / 真3D显示(LCoS) / 15h / 3999元",
        "tech_features": [
            "整机29g（体感15g），全球最轻AI显示眼镜之一，钛合金柔性镜腿",
            "\"蜻蜓光擎\"单光机双目异显真3D显示（LCoS），呈现通知/提词/翻译/AI信息",
            "0.02cc硅基芯片扬声器，可拆卸换电镜腿，持续工作15小时",
            "AI显示眼镜定位，计划2026年第三季度上市，定价3999元"
        ],
        "why_important": "S1是闪极双屏显示路线旗舰，29g极致轻量化+真3D显示推动AI眼镜从\"拍摄\"走向\"显示交互\"，完善国产AI眼镜产品矩阵。",
        "terminal_relevance": "AR/VR眼镜（AI显示眼镜）",
        "vendor": "闪极科技", "model": "loomos S1",
        "sources": "腾讯新闻",
        "remark": "2025-12首秀、2026-08-18发布会继续预告量产，计划2026 Q3上市"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为 MateBook Pro S",
        "stars": 5, "source": "A", "date": "2026-08-05", "domain": "笔记本",
        "url": "https://www3.xinhuanet.com/tech/20260806/b9ae73f584e94f5bab2470685375eceb/c.html",
        "url_label": "新华网",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "798g / 14.2\" 3.1K柔性OLED防窥屏 / 麒麟XE90 / 7999元起",
        "tech_features": [
            "行业首款柔性OLED灵盾防窥屏：一区双像素，共享/隐私双模无画质损耗，实体隐私开关",
            "798g超轻14英寸金属本，镁锂合金+榫卯无螺丝结构，厚11.9mm",
            "麒麟XE90处理器，3.1K(3120×2080) 120Hz OLED，峰值1600nit，P3广色域",
            "鸿蒙AI：小艺慧记离线会议转写、深度研究，Wi-Fi 7+四天线、66W反向快充、视频续航18h"
        ],
        "why_important": "全球最轻14英寸金属本+首款防窥OLED屏，针对移动商务隐私与离线AI办公刚需，是鸿蒙PC旗舰能力标杆。",
        "terminal_relevance": "笔记本（鸿蒙PC旗舰）",
        "vendor": "华为（Huawei）", "model": "MateBook Pro S (MOR-M1)",
        "sources": "新华网",
        "remark": "2026-08-05发布，售价7999元起"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为 MateBook X Pro 大容量版",
        "stars": 3, "source": "B", "date": "2026-08-28", "domain": "笔记本",
        "url": "https://news.suning.com/m/wtoutiao/bcdetail/6042538867.html",
        "url_label": "苏宁易购",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "8月28日开售 / 酷睿i7 / 集显+8GB+512GB / 10988元",
        "tech_features": [
            "8月28日于华为商城、华为苏宁易购官方旗舰店等四大平台开售",
            "搭载第八代智能英特尔酷睿i7处理器，集成显卡",
            "8GB内存+512GB高速固态硬盘（大容量版定位）",
            "售价10988元，8月28日-10月7日下单享6期免息"
        ],
        "why_important": "大容量版补全MateBook X Pro家族，以10988元提供大存储组合，满足学生与办公用户对容量与轻薄兼得需求，今天是开售首日。",
        "terminal_relevance": "笔记本",
        "vendor": "华为（Huawei）", "model": "MateBook X Pro 大容量版",
        "sources": "苏宁易购",
        "remark": "2026-08-28开售，售价10988元"
    },
    {
        "region": "cn", "status": "released",
        "title": "PANDAER 二合一磁吸无线充",
        "stars": 3, "source": "B", "date": "2026-08-28", "domain": "无线充",
        "url": "https://m.itouchtv.cn/article/a92357db119042b38994dc3d540c1649",
        "url_label": "粤TV(itouchtv)",
        "signal_type": "上市/首发",
        "confirm_count": "4 个印证源",
        "key_params": "15W手机+5W耳机双充 / CNC金属 / 199元",
        "tech_features": [
            "二合一桌面无线充：上方15W磁吸快充（兼容iPhone 12+直吸），下方5W耳机区",
            "CNC全金属骨架+铝合金悬臂+锌合金底座，金属阻尼轴多角度悬停，5000次折叠测试",
            "双充电板独立电路，双设备同充不降功率",
            "魅族PANDAER潮牌设计，黑白配色，8月28日199元开售"
        ],
        "why_important": "以199元将磁吸双设备无线充做成桌面美学单品，补全魅族PANDAER配件矩阵，满足iPhone+耳机同时补能的日常场景。",
        "terminal_relevance": "无线充（配件）",
        "vendor": "魅族（PANDAER）", "model": "PANDAER 二合一磁吸无线充",
        "sources": "粤TV",
        "remark": "2026-08-28发布开售，售价199元"
    },
    {
        "region": "cn", "status": "released",
        "title": "天猫精灵 X5",
        "stars": 3, "source": "C", "date": "2026-08-06", "domain": "智能音箱",
        "url": "https://goods.taobao.com/t/zhinengyinxiang_14660/70a62fb9bedb1d78d5ed0ef7268ad475",
        "url_label": "淘宝好物网",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "AI大模型问答 / 12W单元 / 2麦10m拾音",
        "tech_features": [
            "接入阿里自研AI大模型（AliGenie），支持模糊指令理解与多轮追问",
            "12W钕铁硼单元+自学习动态EQ，800cc音腔，环形悬浮律动灯",
            "2麦克风远场拾音，10米有效接收距离，支持方言识别",
            "可联动1100+品牌智能家居，查快递/健康问答等生活服务"
        ],
        "why_important": "X5把大模型能力下沉到客厅级智能音箱，以\"生活搭子\"定位强化声控生态入口，是阿里在AIoT语音交互的关键基建。",
        "terminal_relevance": "智能音箱（智能家居入口）",
        "vendor": "阿里巴巴（天猫精灵）", "model": "天猫精灵 X5",
        "sources": "淘宝好物网",
        "remark": "AI大模型版在售，原ZOL坏链已替换为淘宝好物网稳定源"
    },
    {
        "region": "cn", "status": "released",
        "title": "漫步者 Comfo Clip Q2",
        "stars": 4, "source": "B", "date": "2026-08-25", "domain": "AI耳机·耳穿戴",
        "url": "https://www.citnews.com.cn/news/221032",
        "url_label": "中文科技资讯(CITNews)",
        "signal_type": "上市/首发",
        "confirm_count": "5 个印证源",
        "key_params": "耳夹开放式 / 海思芯片+开源鸿蒙 / 449元",
        "tech_features": [
            "首款搭载OpenHarmony开源鸿蒙系统的消费级音频设备，全栈自研国产底层架构",
            "海思谛听音频芯片，复杂场景连接稳、游戏延迟低至0.05s",
            "12mm长冲程动圈+PU+PET复合振膜，智能动态低频补偿，4种EQ",
            "豆包+DeepSeek双模型AI翻译，21种语言互译，IP56防水，运动记录"
        ],
        "why_important": "以\"海思芯片+开源鸿蒙\"实现国产音频底层自主，AI翻译与低延迟重新定义开放式耳夹耳机，是端侧AI音频国产化样本。",
        "terminal_relevance": "AI耳机·耳穿戴",
        "vendor": "漫步者（EDIFIER）", "model": "Comfo Clip Q2",
        "sources": "中文科技资讯",
        "remark": "2026-08-25发布，京东到手价399元（日常449元）"
    },

    # ========== 国际 15 条 ==========
    {
        "region": "intl", "status": "released",
        "title": "AGM PAD P3 Compact 发布",
        "stars": 3, "source": "A", "date": "2026-08-19", "domain": "平板",
        "url": "https://www.agmmobile.com/blogs/news/agm-mobile-officially-launches-the-pad-p3-compact-ultra-rugged-8-inch-tablet-now-available",
        "url_label": "AGM Mobile 官方博客",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "8.68英寸 120Hz / Helio G99 / IP68+IP69K+MIL-STD-810H / Android 16 / 7200mAh",
        "tech_features": [
            "8.68英寸 HD 120Hz 显示屏",
            "MediaTek Helio G99 处理器 + 6GB/128GB",
            "IP68、IP69K、MIL-STD-810H 三防认证",
            "内置露营灯 + 50MP 主摄 + 全球版 eSIM/4G"
        ],
        "why_important": "AGM 将三防平板做到 14.5mm 轻薄机身，打破「三防即厚重」的固有印象，面向户外与行业用户。Android 16 + eSIM 使其更贴近主流日常使用。",
        "terminal_relevance": "平板品类，瞄准户外/行业耐用终端细分市场",
        "vendor": "AGM Mobile", "model": "AGM PAD P3 Compact",
        "sources": "AGM Mobile 官方博客",
        "remark": "全球版含 eSIM/4G，美版为 WiFi-only；现已在官网开售"
    },
    {
        "region": "intl", "status": "released",
        "title": "Blackview MEGA 5 发布",
        "stars": 3, "source": "A", "date": "2026-06-02", "domain": "平板",
        "url": "https://blackview.hk/products/item/mega5",
        "url_label": "Blackview 官网",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "12.2英寸 2.4K 120Hz / 10000mAh / 55W / UNISOC T7300 / DokeOS 5.0",
        "tech_features": [
            "12.2英寸 2.4K IPS 120Hz 屏",
            "10000mAh 电池 + 55W 快充",
            "UNISOC T7300 八核 + 最高 36GB 运存扩展",
            "DokeOS 5.0（基于 Android 16）+ 6W 反向充电"
        ],
        "why_important": "MEGA 5 以万毫安大电池和 55W 快充主打长续航，配合 Android 16 新系统，丰富中低端大屏平板选择。12.2 英寸 + 635g 兼顾影音与便携。",
        "terminal_relevance": "平板品类，大屏长续航影音/入门生产力定位",
        "vendor": "Blackview", "model": "Blackview MEGA 5",
        "sources": "Blackview 官网",
        "remark": "提供 Space Grey / Ice Blue 双色；支持 Wi-Fi 6、GPS 多频定位"
    },
    {
        "region": "intl", "status": "released",
        "title": "Teclast T70 Pro 上架",
        "stars": 3, "source": "B", "date": "2026-08-20", "domain": "平板",
        "url": "https://www.gsmchoice.com/en/catalogue/teclast/t70-pro",
        "url_label": "GSMchoice 参数库",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "14英寸 1400×2240 IPS / Helio G100 / 10000mAh / 8GB+128GB / Android 16",
        "tech_features": [
            "14英寸 IPS 2.2K（1400×2240）显示屏",
            "MediaTek Helio G100 八核 + Mali-G57 MC2",
            "10000mAh 电池 + USB-PD 18W",
            "四扬声器 + LDAC 音频 + 蓝牙 5.2"
        ],
        "why_important": "台电以 14 英寸 2.2K 大屏切入平价大屏平板市场，Helio G100 提供够用性能，万毫安电池强化影音续航。是预算型大屏平板的代表新品。",
        "terminal_relevance": "平板品类，平价大屏影音/轻度生产力",
        "vendor": "Teclast", "model": "Teclast T70 Pro",
        "sources": "GSMchoice 参数库",
        "remark": "gsmchoice 标注发布于 2026 Q3；重约 800g，支持 microSD 扩展至 1TB"
    },
    {
        "region": "intl", "status": "released",
        "title": "DOOGEE Tab G6 Pro 发布",
        "stars": 3, "source": "A", "date": "2026-08-15", "domain": "平板",
        "url": "https://www.doogee.com/ru/products/tab-g6-pro",
        "url_label": "DOOGEE 官网",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "12英寸 2K 90Hz / 9000mAh / 7.5mm 轻薄 / 8GB+128GB / Android 16",
        "tech_features": [
            "12英寸 2K 90Hz IPS 屏",
            "9000mAh 电池",
            "7.5mm 超薄机身 + 轻量便携",
            "8GB RAM + 128GB 存储（VIP/基础版可选）"
        ],
        "why_important": "DOOGEE 将 12 英寸 2K 90Hz 大屏做到 7.5mm 轻薄与 9000mAh 续航的平衡，定价 $249.99 主打性价比。延续品牌平价大屏策略。",
        "terminal_relevance": "平板品类，轻薄大屏性价比定位",
        "vendor": "DOOGEE", "model": "DOOGEE Tab G6 Pro",
        "sources": "DOOGEE 官网",
        "remark": "页面显示 EU/US 版本；部分版本已售罄"
    },
    {
        "region": "intl", "status": "released",
        "title": "三星 Galaxy Z Fold8 发布",
        "stars": 5, "source": "A", "date": "2026-07-22", "domain": "手机",
        "url": "https://www.samsung.com/tw/smartphones/galaxy-z-fold8/",
        "url_label": "Samsung 台湾官网",
        "signal_type": "上市",
        "confirm_count": "5 个印证源",
        "key_params": "7.6英寸内屏 / 201g / 4800mAh / Snapdragon 8 Elite Gen 5 / One UI 9",
        "tech_features": [
            "全新 Armor FlexHinge + Flex Titanium 双层钛金属减震层",
            "Snapdragon 8 Elite Gen 5 for Galaxy 定制芯片",
            "内外屏峰值 3000 nits + 抗反光内屏",
            "5000 万双摄 + ProVisual Engine + 8K 录制"
        ],
        "why_important": "Fold8 将折叠屏重量压到 201g、刷新最轻 Fold 纪录，配合定制旗舰芯片与 3000nits 亮屏，标志大折叠向轻薄旗舰化迈进。对安卓折叠生态具有标杆意义。",
        "terminal_relevance": "手机品类，旗舰折叠屏",
        "vendor": "Samsung", "model": "Galaxy Z Fold8",
        "sources": "Samsung 台湾官网",
        "remark": "提供 256/512GB 存储；内置 Galaxy AI"
    },
    {
        "region": "intl", "status": "released",
        "title": "三星 Galaxy Z Flip8 发布",
        "stars": 4, "source": "A", "date": "2026-07-22", "domain": "手机",
        "url": "https://www.samsung.com/nz/smartphones/galaxy-z-flip8-mint-256gb-sm-f776blgaxnz",
        "url_label": "Samsung 新西兰官网",
        "signal_type": "上市",
        "confirm_count": "5 个印证源",
        "key_params": "6.9英寸主屏 / 180g / 4300mAh / 定制 Galaxy 芯片 / One UI 9",
        "tech_features": [
            "6.9英寸主屏 + 4.1英寸 FlexWindow 外屏，峰值 2600 nits",
            "180g 机身（比 Flip7 轻 8g），展开仅 6.1mm",
            "4300mAh 电池，视频续航最长 31 小时",
            "50MP 广角 + 12MP 超广角 + FlexCam 免手持"
        ],
        "why_important": "Flip8 以 180g 刷新最轻翻盖折叠纪录，电池增至 4300mAh、视频续航大幅提升，NPU 较上代快 41%。翻盖折叠在轻薄与续航上取得突破。",
        "terminal_relevance": "手机品类，翻盖折叠屏",
        "vendor": "Samsung", "model": "Galaxy Z Flip8",
        "sources": "Samsung 新西兰官网",
        "remark": "提供 Pink/Graphite/Cream 配色；含 Galaxy AI"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Garmin fēnix 9 发布",
        "stars": 4, "source": "A", "date": "2026-08-26", "domain": "智能手表",
        "url": "https://www.garmin.com/en-PH/newsroom/press-release/news-2026-aug-fenix9/",
        "url_label": "Garmin 菲律宾新闻室",
        "signal_type": "首发",
        "confirm_count": "6 个印证源",
        "key_params": "AMOLED 亮度翻倍 / 蓝宝石镜面 / 40m 潜水 / 64GB / 9月16日开售",
        "tech_features": [
            "AMOLED 显示屏亮度为前代两倍，配防刮蓝宝石镜面",
            "潜水级密封按键，支持 40 米潜水",
            "全新 Garmin Epic 活动故事 + 耐力区间/耐力曲线",
            "64GB 存储，地图下载量翻倍，导航引擎提速 30%"
        ],
        "why_important": "fenix 9 将旗舰户外表的 AMOLED 亮度翻倍并加入潜水与 Epic 叙事功能，强化 Garmin 在专业运动与探险领域的领导地位。9 月 16 日开售，起价 PHP 62,690。",
        "terminal_relevance": "智能手表品类，专业运动/户外旗舰",
        "vendor": "Garmin", "model": "fēnix 9",
        "sources": "Garmin 菲律宾新闻室",
        "remark": "提供 43/47/51mm 三种尺寸；智能模式续航最长 29 天"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Garmin fēnix 9 Pro 发布",
        "stars": 5, "source": "A", "date": "2026-08-26", "domain": "智能手表",
        "url": "https://www.garmin.com/en-PH/newsroom/press-release/news-2026-aug-fenix9/",
        "url_label": "Garmin 菲律宾新闻室",
        "signal_type": "首发",
        "confirm_count": "6 个印证源",
        "key_params": "首款钛金属表壳 / AMOLED 3000nit / 太阳能充电 / 51mm 1.5寸屏 / 9月16日",
        "tech_features": [
            "fēnix 系列首款钛金属表壳（纳米成型工艺）",
            "AMOLED 屏峰值 3000 nits，51mm 版配 1.5 英寸屏",
            "太阳能充电版智能模式最长 57 天",
            "集成 LED 手电筒新增绿色护眼底灯模式"
        ],
        "why_important": "fenix 9 Pro 用钛金属表壳与 3000nits 屏提升质感与可读性，太阳能版续航达 57 天，是 Garmin 旗舰工艺与续航的双重突破。起价 PHP 72,690。",
        "terminal_relevance": "智能手表品类，顶级户外旗舰",
        "vendor": "Garmin", "model": "fēnix 9 Pro",
        "sources": "Garmin 菲律宾新闻室",
        "remark": "含 fenix 9 全部特性；9 月 16 日开售，8/27-9/10 预售"
    },
    {
        "region": "intl", "status": "released",
        "title": "Kmart $89 Anko 摄像眼镜澳洲售罄",
        "stars": 3, "source": "B", "date": "2026-08-03", "domain": "AR-VR眼镜",
        "url": "https://smartglassesdaily.com/en/article/kmart-s-89-anko-camera-glasses-sell-out-down-under-sparking-privacy-fears-eg1a9",
        "url_label": "Smart Glasses Daily",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "$89 / 8MP 摄像 + 1080p 录像 / HeyCyan 软件 / 类 Meta Ray-Ban 设计",
        "tech_features": [
            "8MP 摄像头 + 高清视频录制",
            "集成 HeyCyan 软件：音乐/通话/AI 助手/媒体传输",
            "透明镜片 + 黑框日常化设计",
            "售价仅 $89，远低于 Meta Ray-Ban（$337 起）"
        ],
        "why_important": "Anko 以 $89 超低价摄像眼镜快速售罄，显示平价智能眼镜市场需求爆发，同时引发数字权利组织对非自愿拍摄的隐私担忧。低价化将加速智能眼镜普及与监管讨论。",
        "terminal_relevance": "AR/VR 眼镜品类，入门摄像眼镜",
        "vendor": "Anko (Kmart)", "model": "Anko Camera Glasses",
        "sources": "Smart Glasses Daily",
        "remark": "2026-08-03 澳洲全境售罄；Guardian 报道隐私争议"
    },
    {
        "region": "intl", "status": "released",
        "title": "Samsung Galaxy XR 登陆英国",
        "stars": 4, "source": "B", "date": "2026-07-08", "domain": "AR-VR眼镜",
        "url": "https://www.devicedecode.com/gadgets/samsung-galaxy-xr-uk-price-release-date-specs",
        "url_label": "DeviceDecode",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "Micro-OLED 3552×3840/眼 / Snapdragon XR2+ Gen2 / Android XR / £1699 / 7月8日",
        "tech_features": [
            "双 Micro-OLED，单眼 3552×3840 分辨率，最高 90Hz",
            "高通 Snapdragon XR2+ Gen 2 + 16GB + 256GB",
            "Android XR 系统 + Gemini AI，支持眼/手/语音操控",
            "Wi-Fi 7、蓝牙 5.4，约 545g，外置电池 2-2.5 小时"
        ],
        "why_important": "Galaxy XR 是三星联合 Google、Qualcomm 打造的首款 Android XR 头显，以 £1699 切入高端 MR 市场，提供比 Apple Vision Pro 更开放的安卓生态替代。英国 7 月 8 日开售标志其走向全球。",
        "terminal_relevance": "AR/VR 眼镜品类，混合现实头显",
        "vendor": "Samsung", "model": "Galaxy XR",
        "sources": "DeviceDecode",
        "remark": "109° 水平视场；UK 售价 £1699；支持 Google 应用与 Gemini"
    },
    {
        "region": "intl", "status": "released",
        "title": "MSI Crosshair A16 HX MLG 版全球上市",
        "stars": 4, "source": "B", "date": "2026-08-03", "domain": "笔记本",
        "url": "https://www.back2gaming.com/news/msi-crosshair-a16-hx-mlg-edition-gaming-laptop-now-available-globally",
        "url_label": "Back2Gaming",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "锐龙 9 8940HX（16核） / RTX 5070 12GB / 16寸 QHD+ 240Hz / 最高 190W",
        "tech_features": [
            "AMD Ryzen 9 8940HX 最高 16 核 32 线程",
            "NVIDIA RTX 5070 笔记本 GPU（12GB GDDR7），DLSS 4.5",
            "16 英寸 QHD+（2560×1600）240Hz，100% DCI-P3",
            "Cooler Boost 双风扇五热管 + 最高 96GB DDR5"
        ],
        "why_important": "Crosshair A16 HX MLG 版以锐龙 9 + RTX 5070 满血 190W 输出主打高性能游戏本，240Hz QHD+ 屏兼顾竞技与创作。MLG 联名设计强化品牌个性，8 月 3 日全球开售。",
        "terminal_relevance": "笔记本品类，高性能游戏本",
        "vendor": "MSI", "model": "Crosshair A16 HX MLG Edition",
        "sources": "Back2Gaming",
        "remark": "附赠 MLG 鼠标/耳机/鼠标垫；部分地区有限量手办礼盒"
    },
    {
        "region": "intl", "status": "released",
        "title": "Dell XPS 16 (2026) 评测",
        "stars": 4, "source": "A", "date": "2026-05-11", "domain": "笔记本",
        "url": "https://www.pcmag.com/reviews/dell-xps-16-2026",
        "url_label": "PCMag",
        "signal_type": "评测",
        "confirm_count": "4 个印证源",
        "key_params": "16寸 3.2K OLED 触控 / Intel Core Ultra X7 358H / Arc B390 / 起价 $2039.99",
        "tech_features": [
            "可选 3.2K（3200×2000）OLED 触控屏，400+ nits",
            "Intel Core Ultra X7 358H（Panther Lake）+ Arc B390 核显",
            "4K 网络摄像头（HDR）+ Wi-Fi 7 + 蓝牙 6",
            "全 USB-C（3× Thunderbolt 4），1.6cm 轻薄金属机身"
        ],
        "why_important": "XPS 16 (2026) 在取消 XPS 改名风波后重新复兴，以 OLED 屏、4K 摄像头与精致金属机身定位高端桌面替代。无独显、纯 USB-C 是取舍点，但奢华做工与续航（17 小时）突出。",
        "terminal_relevance": "笔记本品类，高端轻薄创作本",
        "vendor": "Dell", "model": "XPS 16 (2026)",
        "sources": "PCMag",
        "remark": "PCMag 评分 4.0 Excellent；起价 $2039.99，测试机 $3029.99"
    },
    {
        "region": "intl", "status": "released",
        "title": "Apple 新款 MagSafe 充电器（Qi2 25W）",
        "stars": 4, "source": "A", "date": "2025-09-10", "domain": "无线充",
        "url": "https://www.macrumors.com/2025/09/10/apple-releases-new-magsafe-charger",
        "url_label": "MacRumors",
        "signal_type": "上市",
        "confirm_count": "5 个印证源",
        "key_params": "Qi2 25W（Qi 2.2）/ $39(1m)-$49(2m) / 第三代 MagSafe / iOS 26 兼容",
        "tech_features": [
            "通过 Qi2 25W（即 Qi 2.2）认证",
            "可对 iPhone 16/17 及 Google Pixel 10 等以最高 25W 充电",
            "为第三代 MagSafe 充电器",
            "配 1 米/2 米 USB-C 线缆，需另购 30W+ 适配器"
        ],
        "why_important": "新款 MagSafe 获 Qi2 25W 认证，打破此前仅限 iPhone 的 25W 限制，使 Pixel 10 等安卓设备也能 25W 磁吸快充。配合 iOS 26，iPhone 16/17 可用任意 Qi2 25W 充电器满速充电，推动生态互通。",
        "terminal_relevance": "无线充品类，磁吸无线充电器",
        "vendor": "Apple", "model": "MagSafe Charger (2nd Gen, Qi2 25W)",
        "sources": "MacRumors",
        "remark": "发布于 2025-09-10；型号 MGD74LL/A；iPhone 16e 不支持 25W"
    },
    {
        "region": "intl", "status": "released",
        "title": "Sony SRS-ULT10 便携音箱上市",
        "stars": 3, "source": "A", "date": "2026-08-16", "domain": "智能音箱",
        "url": "https://electronics.sony.com/audio/speakers/all-speakers/p/srsult10-w",
        "url_label": "Sony 电子官方",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "ULT POWER SOUND / IP67 / 12 小时续航 / ULT 低音键 / $99.99",
        "tech_features": [
            "ULT 按钮一键增强低音（ULT POWER SOUND）",
            "IP67 防水防尘 + 抗冲击（MIL-STD 810H）",
            "Sound Diffusion Processor 空间扩音，续航 12 小时",
            "多向背带 + 立体声配对 + 蓝牙免提通话"
        ],
        "why_important": "SRS-ULT10 是索尼 ULT POWER SOUND 系列便携代表，以一键重低音与 IP67 三防切入户外音箱市场，定价 $99.99 主打性价比。延续索尼在便携音频的竞争力。",
        "terminal_relevance": "智能音箱品类，便携蓝牙音箱",
        "vendor": "Sony", "model": "SRS-ULT10 (ULT FIELD 1)",
        "sources": "Sony 电子官方",
        "remark": "提供多色；原 sony.com.my 大类页无具体型号，已替换为索尼美国具体产品页"
    },
    {
        "region": "intl", "status": "released",
        "title": "CMF Clip Pro 发布",
        "stars": 4, "source": "A", "date": "2026-08-15", "domain": "AI耳机·耳穿戴",
        "url": "https://www.gadgets360.com/audio/news/cmf-clip-pro-price-india-launch-availability-colour-options-features-specifications-news-11868609",
        "url_label": "Gadgets360",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "10.8mm 单元 / LDAC / 开放夹耳 / 32.5h 续航 / IP54 / $99",
        "tech_features": [
            "10.8mm 动圈（TPU+LCP 振膜），Hi-Res 无线认证",
            "LDAC / AAC / SBC，支持静态空间音频",
            "三点夹耳 C 形结构 + 弹性钛丝，IP54 防护",
            "充电盒集成 Smart Dial 旋钮，蓝牙 5.4 + 双设备连接"
        ],
        "why_important": "CMF Clip Pro 是 Nothing 子品牌首款开放式夹耳耳机，以 10.8mm 单元 + LDAC 高码率音频切入开放佩戴赛道，$99 定价亲民。Smart Dial 与 AI 通话降噪（四麦克风 + Elephant Sound AI）增强差异化。",
        "terminal_relevance": "AI耳机·耳穿戴品类，开放式夹耳耳机",
        "vendor": "CMF (by Nothing)", "model": "CMF Clip Pro",
        "sources": "Gadgets360",
        "remark": "8 月 15 日美/英/日开售，9 月 15 日欧洲等；单机 5.92g"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 26, True),
    ("显示/OLED", 25, True),
    ("折叠屏", 2, True),
    ("手写笔/触控", 3, True),
    ("散热/液冷", 1, True),
    ("电池/续航", 24, True),
    ("快充/无线充", 12, True),
    ("影像", 10, True),
    ("AI/NPU", 15, True),
    ("音频/扬声器", 12, True),
    ("5G/通信", 7, True),
    ("Wi-Fi/连接", 20, True),
    ("AR/VR显示", 4, True),
    ("材质/工艺", 10, True),
    ("可持续/模块化", 2, True),
    ("手柄/外设", 1, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {"rank": 1, "title": "华为 MatePad Air 2026", "dim": "平板电脑", "stars": 5, "key": "B级 / 12英寸OLED柔光屏144Hz / 麒麟T93C / HarmonyOS"},
    {"rank": 2, "title": "三星 Galaxy Z Fold8", "dim": "折叠屏", "stars": 5, "key": "A级 / 201g最轻Fold / 骁龙8 Elite Gen5 / 3000nits"},
    {"rank": 3, "title": "闪极 loomos L1", "dim": "AI眼镜", "stars": 5, "key": "B级 / 43g / 骁龙W5100+恒玄BES2700 / AI记忆"},
    {"rank": 4, "title": "Garmin fēnix 9 Pro", "dim": "智能手表", "stars": 5, "key": "A级 / 钛金属表壳 / 3000nit AMOLED / 太阳能57天"},
    {"rank": 5, "title": "华为 MateBook Pro S", "dim": "笔记本", "stars": 5, "key": "A级 / 798g / 3.1K防窥OLED / 麒麟XE90"},
]
'''

src = open(TEMPLATE, encoding="utf-8").read()
start = src.index("CARDS = [")
end = src.index("# ── 排序：状态优先")
new_src = src[:start] + CHUNK + "\n" + src[end:]

new_src = new_src.replace("2026-08-26", "2026-08-28")
new_src = new_src.replace('WEEK = "周三"', 'WEEK = "周五"')
new_src = new_src.replace("采集口径：7类智能终端", "采集口径：8类智能终端")
new_src = new_src.replace('<div class="stat-num">7</div>', '<div class="stat-num">8</div>')

exec(new_src)
print("DONE")
