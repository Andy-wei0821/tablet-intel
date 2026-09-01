#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 WB_2026-09-01_硬件看板.html
做法：读取 gen_wb_2026-08-26.py 模板，先替换模板内 日期/周几/类别数(7→8)/排序兜底，
     再注入 CARDS/DIMS/TOP5，exec 生成。
     注意：先替换 src 再拼接 CHUNK，避免全局 replace 污染 CHUNK 内的卡片日期。
"""
import os

TEMPLATE = r"E:\AI相关\预研究\202608\03_输出\gen_wb_2026-08-26.py"

CHUNK = r'''CARDS = [
    # ========== 国内 15 条 ==========
    {
        "region": "cn", "status": "released",
        "title": "华为 MatePad Pro 12.2 英寸（2026）",
        "stars": 5, "source": "C", "date": "2026-08-14", "domain": "平板",
        "url": "https://www.toutiao.com/a7673912753634935359",
        "url_label": "今日头条",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "12 英寸柔性 OLED 3036×1952 144Hz / 1600nits，机身 4.7mm、约 439g，麒麟 T93/T93A，10400mAh + 66W，5699 元起",
        "tech_features": [
            "12 英寸柔性 OLED 全面屏，3036×1952 分辨率，144Hz 刷新率，峰值亮度 1600nits，可选 PaperMatte 云晰柔光屏版本",
            "整机厚度 4.7mm、重量约 439g，全金属一体化 + 凝光工艺背板",
            "麒麟 T93（标准版）/ T93A（悦享版），官方称整体性能提升约 25%；HarmonyOS 6.1 支持四指滑动切换平板与 PC 双桌面模式",
            "10400mAh 电池，66W 有线快充 + 40W 反向有线充电；悦享版 12GB+256GB 售 5699 元起，标准版 5999 元起"
        ],
        "why_important": "4.7mm/439g 把 12 英寸 OLED + 10400mAh 压进近乎轻薄本的机身，是当前高端平板结构堆叠的上限样本，值得 TCL 在屏体选型、中框材料与电池能量密度上直接对标。HarmonyOS 6.1 的「平板/PC 双桌面」说明国产 OS 正把平板往生产力方向推，预研需提前考虑多窗口与 PC 级应用的散热、内存冗余。",
        "terminal_relevance": "大屏旗舰：轻薄结构、柔性 OLED 柔光方案、大电池+66W 快充温升预算",
        "vendor": "华为（HUAWEI）", "model": "MatePad Pro 12.2 英寸 2026",
        "sources": "今日头条",
        "remark": "中国区 8 月上市开售；9 月 2 日慕尼黑发布会推出全球版，国内外节奏仅差约 1 个月"
    },
    {
        "region": "cn", "status": "released",
        "title": "酷比魔方 iPlay 70 Max Pro",
        "stars": 2, "source": "C", "date": "2026-08-27", "domain": "平板",
        "url": "https://www.toutiao.com/article/7678243202767274498",
        "url_label": "今日头条",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "13 英寸 2.5K LCD，紫光展锐 T7300，8GB+128GB，10000mAh + 30W，7.1mm/684g，1399 元",
        "tech_features": [
            "13 英寸 2.5K 分辨率 LCD 屏，定位「可当电脑用」的大屏入门机型",
            "紫光展锐 T7300 平台，安兔兔跑分约 65 万，8GB+128GB 起，支持 TF 卡扩展至 512GB",
            "10000mAh 电池配 30W 快充，机身厚 7.1mm、重 684g",
            "配四扬声器、3.5mm 耳机孔、OTG、磁吸键盘与 4096 级压感手写笔，售价 1399 元"
        ],
        "why_important": "1399 元把 13 英寸 2.5K + 10000mAh + 磁吸键盘/手写笔全部下放，说明国产入门平板的整机 BOM 已被压到极低，是评估低价位大屏平板成本红线的直接参照。T7300 约 65 万跑分也反向证明「大屏 + 低功耗国产 SoC」这一定位的可行边界。",
        "terminal_relevance": "千元级大屏：屏体/电池/键盘笔生态成本包，国产中低端 SoC 替代路径",
        "vendor": "酷比魔方（Alldocube）", "model": "iPlay 70 Max Pro",
        "sources": "今日头条",
        "remark": "京东标注 Android 16、可插 SIM 卡、前置 1300W/后置 500W"
    },
    {
        "region": "cn", "status": "released",
        "title": "vivo Pad5c",
        "stars": 4, "source": "B", "date": "2026-07", "domain": "平板",
        "url": "https://www.163.com/dy/article/L0QT6LFF05118EDB.html",
        "url_label": "网易（超能网）",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "12.1 英寸 2800×1968 144Hz LCD（900nits），第三代骁龙 8s，10000mAh，6.62mm/584g，2699 元起",
        "tech_features": [
            "12.1 英寸 LCD，2800×1968、7:5 比例，最高 144Hz，全屏峰值亮度 900nits，支持 10bit 色深、P3 广色域、HDR10",
            "第三代骁龙 8s（台积电 4nm，1×Cortex-X4 3.0GHz + 4×A720 2.8GHz + 3×A520 2.0GHz），LPDDR5X 四通道 + UFS 4.1",
            "散热堆 32200mm² 石墨面积，对称式四扬声器 + 自研 Super Audio 6.0 音效",
            "机身 266.43×192×6.62mm、约 584g，支持 DC 调光与 TÜV 莱茵硬件级低蓝光；8+128GB 2699 元 / 12+256GB 3499 元"
        ],
        "why_important": "把 144Hz 2.8K + 32200mm² 石墨散热塞进 6.62mm/584g，是 2500-3500 元档「影音+学习」平板的结构与散热参考点。vivo 用上代旗舰架构下放中端，配合 PC 级 WPS 与 AI 转记，说明中端平板卖点正向「屏幕规格 + 被动散热冗余 + 办公套件」迁移。",
        "terminal_relevance": "中端大屏：144Hz LCD 选型、石墨散热面积与整机厚度/重量三角平衡",
        "vendor": "vivo（维沃）", "model": "vivo Pad5c",
        "sources": "网易/超能网",
        "remark": "支持 vivo Pencil3 与触控键盘，学生用户下单赠触控笔"
    },
    {
        "region": "cn", "status": "released",
        "title": "台电 2026 款 P30T 平板",
        "stars": 2, "source": "A", "date": "2026-08-05", "domain": "平板",
        "url": "https://www.ithome.com/0/985/764.htm",
        "url_label": "IT之家",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "10.1 英寸 1280×800 120Hz IPS LCD，紫光展锐 T7250 + 3GB + 128GB，6000mAh，599 元",
        "tech_features": [
            "10.1 英寸 1280×800 分辨率 120Hz IPS LCD 面板，亮度 300nits",
            "紫光展锐 T7250 处理器，3GB RAM + 128GB 存储，支持 MicroSD 卡扩展",
            "6000mAh 电池，金属机身，重 440g、厚 7.8mm",
            "保留 3.5mm 耳机孔，后置 5MP 主摄，京东售价 599 元"
        ],
        "why_important": "599 元档已能给到 10.1 英寸 120Hz + 金属机身 + 6000mAh，反映入门平板的结构件与屏体成本已见底，对判断「教育/老人/网课」细分市场的定价地板有参考价值。展锐 T7250 + 3GB 组合也印证紫光展锐是国产唯一稳定供货中低端平板 SoC 的厂商。",
        "terminal_relevance": "入门/教育平板：600 元价位段 BOM 结构与国产 SoC 选型底线",
        "vendor": "台电（Teclast）", "model": "2026 款 P30T",
        "sources": "IT之家",
        "remark": "京东标注 Android 16，国补后约 569 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "REDMI K100 Pro Max",
        "stars": 5, "source": "B", "date": "2026-08-11", "domain": "手机",
        "url": "https://news.yesky.com/hotnews/368/369868.shtml",
        "url_label": "天极网",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "6.9 英寸 185Hz 超级像素屏，第五代骁龙 8 至尊版 + D2 独显，9070mAh + 100W 有线/50W 无线，4499 元起",
        "tech_features": [
            "6.9 英寸 185Hz 超级像素屏，全亮度 DC 调光，通过四重莱茵认证 + S++ 视觉认证",
            "第五代骁龙 8 至尊版 + AI 游戏独显 D2 + LPDDR5X + UFS 4.1，综合跑分 455.5 万",
            "散热采用 6300mm² 大面积循环冷泵 + 高性能石墨，整机散热物料面积超 35000mm²",
            "9070mAh 电池 + 100W 有线 + 50W 无线 + 旁路充电；触控链路 480Hz 十指 + 4800Hz 瞬时采样；Sound by Bose 三扬声器 2.1 声道"
        ],
        "why_important": "9070mAh + 6300mm² 循环冷泵 + 35000mm² 散热物料，是「大电池 + 重散热」手机/小平板共用的技术包，可直接迁移到小尺寸高性能平板的续航与持续性能释放设计。480Hz 十指 + 4800Hz 瞬时触控的三路采样链路，也是电竞向平板触控方案的现成标杆。",
        "terminal_relevance": "游戏/高性能平板：大电池+循环冷泵散热、高刷触控采样链路、旁路供电",
        "vendor": "小米 REDMI（Xiaomi Redmi）", "model": "REDMI K100 Pro Max",
        "sources": "天极网",
        "remark": "12+256GB 起售 4499 元，国补后 3999 元起；16+512GB 5499 元、16GB+1TB 顶配 5999 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "iQOO Z11S",
        "stars": 3, "source": "C", "date": "2026-08-30", "domain": "手机",
        "url": "https://www.163.com/dy/article/L5HP8C6H0531G57O.html",
        "url_label": "网易订阅",
        "signal_type": "开售",
        "confirm_count": "2 个印证源",
        "key_params": "10000mAh 超薄蓝海电池，天玑 7500 满血版，6.83 英寸 1.5K 144Hz AMOLED，首销 1799 元起",
        "tech_features": [
            "10000mAh 超薄蓝海电池，采用魔方封装 2.0 + 核舟堆叠架构压缩体积，支持 44W 有线快充",
            "天玑 7500 满血版（4nm，4×Arm C1-Pro 2.6GHz + 4×Arm C1-Nano 2.0GHz，Mali G625），整机跑分约 130 万",
            "6.83 英寸 1.5K AMOLED 电竞屏，144Hz 刷新率，手动亮度 1000nits、全局亮度 2000nits，游戏触控采样最高 300Hz",
            "IP68/IP69 双防 + 磐石缓震架构，前置 800 万 + 后置 5000 万单摄；8GB+128GB 首销 1799 元"
        ],
        "why_important": "万毫安电池已下探到 1799 元档，靠的是「魔方封装 2.0 + 核舟堆叠」的电池体积优化，这套方案对在小尺寸平板上塞大电池有直接借鉴意义。2000nits 全局亮度的 1.5K 144Hz AMOLED 下放到中端，也说明高亮屏体成本在快速下降。",
        "terminal_relevance": "电池堆叠与中端屏体选型：万毫安电池体积控制、全局高亮 AMOLED 成本下探",
        "vendor": "iQOO（vivo 旗下）", "model": "iQOO Z11S",
        "sources": "网易订阅",
        "remark": "首销已于 8 月 31 日结束；属 Z11 同系列，与印度版 Z11 为不同型号"
    },
    {
        "region": "cn", "status": "released",
        "title": "荣耀手表 6 Plus 张雪机车联名款",
        "stars": 3, "source": "C", "date": "2026-07-27", "domain": "智能手表",
        "url": "https://www.sina.cn/media/1609499537",
        "url_label": "新浪新闻",
        "signal_type": "开售",
        "confirm_count": "3 个印证源",
        "key_params": "1.46 英寸 AMOLED 3000nits，1000mAh 青海湖电池，常规 17 天/长续航 35 天/GPS 42 小时，1699 元",
        "tech_features": [
            "1.46 英寸 AMOLED 圆形屏（464×464），峰值亮度 3000nits，支持湿手触控",
            "内置 1000mAh 青海湖电池，常规使用续航 17 天、长续航模式 35 天、独立 GPS 模式 42 小时",
            "机身薄至 10.8mm、整机约 41g，支持 120+ 运动模式、双频六星 GPS 与荣耀北极星定位",
            "专属机车骑行模式（实时速度/心率/轨迹 + 智能超速振动提醒 + 自动骑行报告）；官方定价 1699 元，国补后 1359.15 元起"
        ],
        "why_important": "1000mAh 青海湖硅碳电池把 1.46 英寸 AMOLED 手表推到 35 天续航，是国产腕戴在「电池材料 + 低功耗平台」上的最新成果，可与终端大电池路线共享供应链判断。深度定制垂直场景（机车骑行）说明穿戴正从通用健康转向细分运动模式，生态合作是低成本差异化路径。",
        "terminal_relevance": "智能穿戴：硅碳负极电池能量密度、垂直运动场景算法与联名定制打法",
        "vendor": "荣耀（HONOR）", "model": "荣耀手表 6 Plus 张雪机车联名款",
        "sources": "新浪新闻",
        "remark": "全渠道开售，活动周期 7 月 3 日至 7 月 31 日；首发当日荣耀官方商城即显示售罄"
    },
    {
        "region": "cn", "status": "released",
        "title": "荣耀手环 11 系列",
        "stars": 4, "source": "A", "date": "2026-08-12", "domain": "智能手表",
        "url": "https://www.ithome.com/0/988/679.htm",
        "url_label": "IT之家",
        "signal_type": "开售",
        "confirm_count": "3 个印证源",
        "key_params": "标准版 1.57 英寸 AMOLED / 250mAh / 18 天 / 15.3g；Pro 版 1.61 英寸 2000nits / 400mAh 硅碳 / 26 天，首销 229 元起",
        "tech_features": [
            "标准版 1.57 英寸 AMOLED，支持最高 60Hz 刷新率，250mAh 电池，典型续航 12 天、超长续航模式 18 天",
            "标准版采用增强型聚合纤维机身，厚约 8.99mm、整机重 15.3g，表带支持快拆",
            "Pro 版升级 1.61 英寸 AMOLED 2.5D 曲面屏，常规亮度 700nits、峰值 2000nits；400mAh 硅碳负极电池，典型续航 19 天、超长模式 26 天",
            "全系新增专业羽毛球模式，支持睡眠 HRV、呼吸暂停监测、防猝筛查与 5ATM 防水；首销标准版 229 元 / Pro 299 元"
        ],
        "why_important": "15.3g/8.99mm 配 250mAh 做到 18 天续航，Pro 版用硅碳负极把 400mAh 顶到 26 天——硅碳电池在腕戴上的量产落地数据，对评估同类电池在平板/穿戴上的体积收益很关键。229 元起还全系下放 HRV、呼吸暂停、防猝筛查，说明健康算法已成百元腕戴标配门槛。",
        "terminal_relevance": "智能穿戴与平板电池：硅碳负极能量密度、低功耗架构、健康传感算法成本",
        "vendor": "荣耀（HONOR）", "model": "荣耀手环 11 / 11 Pro / 11 Pro GPS",
        "sources": "IT之家",
        "remark": "8 月 3 日预售，8 月 12 日 10:00 全渠道开售；学生专享价低至 186.15 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "Moonix（莫奈）AI 眼镜标准版",
        "stars": 5, "source": "B", "date": "2026-07-17", "domain": "AR-VR眼镜",
        "url": "https://www.360kuai.com/pc/detail?check=73ba2254f54f3014&market=pc_def&stype=portal&sv=4&tj_cmode=pc_look&ucheck=fb7cdd2e793a3a24b11affdf9ad8cde5&url=http%3A%2F%2Fzm.news.so.com%2F99ba45af8bac1c0adfbd1ca2d2b82fdf&v=1",
        "url_label": "快资讯（智东西）",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "β钛款整机仅 14.9g，无显示模组，综合续航 16 小时，39+ 款可换镜框，2299 元起",
        "tech_features": [
            "整机重量最低 14.9g（β钛款），镜腿最薄处仅 4mm，采用镜腿快插模块式结构",
            "上市初期提供 39+ 款可换前镜框，覆盖 β钛、纳米尼龙、板材、不锈钢四种材质",
            "综合续航约 16 小时（6 小时主动录音 + 10 小时智能录音），内置 6 麦克风双模拾音 + 92mAh 电池",
            "主动式 AI 无感记录（按设定间隔自动采集环境音频与状态，App 侧 AI 生成会议纪要/行为洞察）；2299 元起，100 家博士眼镜门店同步开售"
        ],
        "why_important": "把 AI 眼镜做到 14.9g（与普通光学眼镜同重量级）并主动砍掉翻译/提词器/导航等低频功能，代表「先做一副能久戴的眼镜」的减法路线，是做眼镜类终端时最值得抄的产品定义逻辑。镜腿快插 + 39 款可换框的模块化结构，也是把电子产品接入传统眼镜渠道与配镜服务的关键工程方案。",
        "terminal_relevance": "AR/AI 眼镜预研：14.9g 级结构堆叠、模块化可换框、端侧低功耗长时录音与隐私架构",
        "vendor": "心眸科技（Moonix / 莫奈）", "model": "Moonix AI 眼镜标准版",
        "sources": "智东西",
        "remark": "运营主体心眸科技，核心团队来自网易/商汤/海康威视；Pro 版约 19.9g 支持视频记录，计划 8-9 月上市"
    },
    {
        "region": "cn", "status": "released",
        "title": "科大讯飞 AI 眼镜（标准版）",
        "stars": 5, "source": "B", "date": "2026-07", "domain": "AR-VR眼镜",
        "url": "https://reportify.cn/reports/1285323181976064000",
        "url_label": "Reportify（国泰海通研报）",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "约 40g，双目单色显示 640×480 / 25° FOV / 1500nits，122 种语言翻译 + 唇动识别，4299 元",
        "tech_features": [
            "整机约 40g，采用双目单色显示方案，分辨率 640×480，视场角 25°，入眼亮度 1500nits",
            "支持 122 种语言翻译（语音 + 文字显示，含离线翻译），具备唇动识别与多模态降噪，内置 6 麦克风 + 定向传声双扬声器",
            "160mAh 电池，30 分钟充至 80%，综合续航约 6 小时；1200 万像素摄像头，单次录像 5 分钟",
            "64GB 机身存储 + 512MB 运行内存，型号 XF-AIGlasses-01，京东售价 4299 元"
        ],
        "why_important": "双目单色（非全彩）路线把整机压到 40g 且成本可控，配合 122 语种 + 唇动识别降噪，验证了「单色显示 + 翻译刚需场景」是当前最容易量产放量的 AI 眼镜形态，对判断 AR 眼镜技术路线取舍很关键。25° FOV / 640×480 的规格选择，也划出了当前可量产光波导显示模组的能力边界。",
        "terminal_relevance": "AR 眼镜预研：单色 vs 全彩微显示方案、光波导 FOV 与入眼亮度指标、离线翻译降噪",
        "vendor": "科大讯飞（iFLYTEK）", "model": "科大讯飞 AI 眼镜标准版（XF-AIGlasses-01）",
        "sources": "国泰海通研报",
        "remark": "2026 年 7 月 WAIC 重点展品，已发布开售；同场价格带 799-4599 元，20 余家企业 40 余款产品集中亮相"
    },
    {
        "region": "cn", "status": "released",
        "title": "华硕灵耀 14 2026 酷睿版",
        "stars": 4, "source": "A", "date": "2026-08-31", "domain": "笔记本",
        "url": "https://www.ithome.com/0/996/257.htm",
        "url_label": "IT之家",
        "signal_type": "首销",
        "confirm_count": "3 个印证源",
        "key_params": "14 英寸 2880×1800 120Hz OLED（1100nits / 100% DCI-P3），酷睿 Ultra 5 325 / Ultra 7 365（35W），16GB+1TB，7999 元起",
        "tech_features": [
            "14 英寸 2880×1800 分辨率 120Hz OLED 面板，峰值亮度 1100nits，覆盖 100% DCI-P3 色域",
            "8 核心 8 线程酷睿 Ultra 5 325 或 Ultra 7 365，性能释放 35W",
            "16GB LPDDR5X 内存 + 1TB PCIe 4.0 SSD，70Wh 电池",
            "整机厚 13.9mm、重 1.2kg，1.7mm 长键程键盘；接口含雷电 4 40Gbps、USB-C 10Gbps、USB-A 5Gbps、HDMI 2.1"
        ],
        "why_important": "1.2kg/13.9mm 的 14 英寸 OLED 轻薄本把 35W 释放与 70Wh 电池做成新一代基线，是评估轻薄本/大屏平板二合一形态的整机工程参照。同日同模具还有骁龙 X 版本（1.1kg/50Wh），构成罕见的「同机身 x86 vs ARM」对照样本，对架构预研价值很高。",
        "terminal_relevance": "笔记本/大屏平板：OLED 轻薄本结构与散热、35W 性能释放下的续航配比",
        "vendor": "华硕（ASUS）", "model": "华硕灵耀 14 2026 酷睿版",
        "sources": "IT之家",
        "remark": "8 月 31 日晚 8 点京东首销；Ultra 5 版 7999 元 / Ultra 7 版 8999 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "华硕灵耀 14 骁龙版",
        "stars": 4, "source": "B", "date": "2026-08-31", "domain": "笔记本",
        "url": "https://www.toutiao.com/article/7680216094761583142/",
        "url_label": "今日头条（IT之家）",
        "signal_type": "首销",
        "confirm_count": "2 个印证源",
        "key_params": "骁龙 X（X1-26-100）8 核 8 线程，16GB LPDDR5X-8448 + 512GB，14 英寸 2.8K 120Hz OLED，首发 6999 元",
        "tech_features": [
            "高通骁龙 X（X1-26-100）处理器，8 核心 8 线程",
            "16GB LPDDR5X 内存（频率 8448MT/s）+ 512GB PCIe 4.0 SSD",
            "14 英寸 2880×1800 分辨率 120Hz OLED，峰值亮度 1100nits，100% DCI-P3；整机 13.9mm / 1.1kg，50Wh 电池",
            "接口为 USB-A 3.2 Gen 1 + 双 USB-C 3.2 Gen 2 + HDMI 2.1 TMDS + 3.5mm；建议零售价 7999 元，首发 6999 元"
        ],
        "why_important": "与同日首销的酷睿版共用同一套 13.9mm 模具，但重量降到 1.1kg、电池缩到 50Wh，是观察 ARM PC 在续航/性能/体积上相对 x86 真实差异的稀缺同源样本。LPDDR5X-8448 的内存规格也提示 ARM 平台对内存带宽的依赖更高，是评估 ARM 架构平板/二合一时的关键约束。",
        "terminal_relevance": "ARM 架构终端：骁龙 X 平台整机功耗与电池配比、LPDDR5X 高带宽内存成本",
        "vendor": "华硕（ASUS）", "model": "华硕灵耀 14 骁龙版",
        "sources": "IT之家",
        "remark": "8 月 31 日晚正式开售；与酷睿版为不同 SKU，两条卡片构成 ARM/x86 同模具对照"
    },
    {
        "region": "cn", "status": "coming",
        "title": "安克 Anker MagGo 磁吸移动电源 2.0",
        "stars": 3, "source": "B", "date": "2026-08-27", "domain": "无线充",
        "url": "https://www.toutiao.com/article/7678678672399663616/",
        "url_label": "今日头条（IT之家）",
        "signal_type": "爆料",
        "confirm_count": "2 个印证源",
        "key_params": "无线充电由 15W Qi2 升级至 25W Qi2.2，内置支架 + 底部新增散热孔，侧面彩屏可显示 iPhone 机型",
        "tech_features": [
            "无线充电规格由现款的 15W Qi2 升级至 25W Qi2.2",
            "机身底部新增 1 个散热孔，改善 25W 高功率无线充电时的空气流通与温升",
            "机身侧面带 1 块彩屏，新增支持显示所充 iPhone 机型",
            "延续内置折叠支架的一体化磁吸移动电源形态，主打 25W 档 Qi2.2 与散热结合"
        ],
        "why_important": "Qi2.2 把磁吸无线充从 15W 推到 25W，随之而来的温升问题已迫使厂商在移动电源上加开散热孔——这是 25W 磁吸生态普及的关键工程信号。若平板要做磁吸配件或反向磁吸充电，25W 是必须对齐的新功率基线，散热与线圈对位结构要同步重做。",
        "terminal_relevance": "平板磁吸生态/配件：Qi2.2 25W 线圈与磁阵列、高功率无线充温升控制",
        "vendor": "安克创新（Anker）", "model": "Anker MagGo 磁吸移动电源 2.0",
        "sources": "IT之家（引 NotebookCheck）",
        "remark": "尚未正式上市，由外媒 NotebookCheck 曝光，预计近期上市；与在售的 Anker Prime MagGo Qi2.2 3-in-1 为不同型号"
    },
    {
        "region": "cn", "status": "released",
        "title": "小米 Xiaomi Sound 2 Max 智能音箱",
        "stars": 4, "source": "B", "date": "2026-08-31", "domain": "智能音箱",
        "url": "https://dcdv.zol.com.cn/1241/12413930.html",
        "url_label": "中关村在线",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "双高音 + 双低音 + 无源辐射器四重发声系统，360° 全景声场，杜比 + LDAC，蓝牙 5.3 + Wi-Fi 6，1799 元",
        "tech_features": [
            "双高音单元 + 双低音单元 + 无源辐射器四重发声系统，360° 全景声场",
            "支持杜比音效与 LDAC 高清音频解码（三分频声学配置）",
            "内置超级小爱 AI 大模型，可语音控制全屋智能设备；蓝牙 5.3 + Wi-Fi 6 双模连接",
            "金属网罩 + 织物外观；京东活动价 1799 元，叠加满减与补贴后实付约 1444 元"
        ],
        "why_important": "三分频 + 四单元 + LDAC 的组合下探到约 1444 元实付价，说明高端声学物料成本已进入大众价位，若要布局智能音箱或带屏音频终端，声学配置基线需相应上移。蓝牙 5.3 + Wi-Fi 6 双模已是智能音箱标配，与平板/电视的音频接力协议值得统一考虑。",
        "terminal_relevance": "智能音箱/带屏音频：三分频声学方案、LDAC 与杜比解码、跨端音频接力",
        "vendor": "小米（Xiaomi）", "model": "Xiaomi Sound 2 Max",
        "sources": "中关村在线",
        "remark": "京东自营标注金属机身、蓝牙 5.3、约 21 小时续航"
    },
    {
        "region": "cn", "status": "coming",
        "title": "网易有道 OpenPods AI 耳机",
        "stars": 5, "source": "B", "date": "2026-08-27", "domain": "AI耳机·耳穿戴",
        "url": "https://ai.zol.com.cn/1238/12388496.html",
        "url_label": "中关村在线",
        "signal_type": "首发",
        "confirm_count": "3 个印证源",
        "key_params": "全球首款专为 iPhone 深度优化的 Agent 耳机，单耳 7g，10.8mm 动圈，8h/32h 续航，1499 元（9 月 10 日发售）",
        "tech_features": [
            "搭载苹果官方授权芯片并通过 MFi 认证，锁屏状态下仍可调用核心功能，支持系统级一键通话录音（无提示音）",
            "独立智能耳机舱内置高灵敏麦克风 + 立体声扬声器 + 256MB 本地存储，拾音距离约 5-8 米，双击外放实时中英互译",
            "开放式半入耳设计，单耳仅 7g，耳挂连接处最细 3.2mm，搭载 10.8mm 动圈单元；单次 8 小时、综合 32 小时续航",
            "覆盖 20 余种语言并支持粤语、上海话等方言，支持双向同声传译、音视频实时字幕；AI 会议助手可区分发言人、生成纪要/待办/思维导图"
        ],
        "why_important": "把「录音—转写—翻译—总结—知识库」整合成一条 Agent 工作流，而非单个语音功能，是 AI 耳机从配件升级为终端的分水岭，对规划 AI 音频品类极具参考性。耳机舱集麦克风+扬声器+256MB 存储于一体的形态创新，也说明「耳机 + 独立计算/存储单元」是绕开耳机本体体积限制的可行路径。",
        "terminal_relevance": "AI 音频/穿戴：端侧 Agent 工作流、耳机舱独立算力与存储、跨生态认证与离线翻译",
        "vendor": "网易有道（NetEase Youdao）", "model": "OpenPods 有道 AI 耳机",
        "sources": "中关村在线",
        "remark": "8 月 27 日京东开启预售，9 月 10 日全面发售，黑/白两色，售价 1499 元"
    },

    # ========== 国际 15 条 ==========
    {
        "region": "intl", "status": "released",
        "title": "TCL TAB A1 / TAB A1 NXTPAPER",
        "stars": 5, "source": "B", "date": "2026-08-31", "domain": "平板",
        "url": "https://www.notebookcheck.net/TCL-launches-affordable-11-inch-tablets-with-90Hz-display-8-000mAh-battery-and-Helio-G100.1384271.0.html",
        "url_label": "NotebookCheck",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "11 英寸 2112×1320 90Hz LCD，Helio G100 + 6GB/128GB，8000mAh/20W，IP54，官网 $189.99 / $249.99（亚马逊 $179.99 / $229.99）",
        "tech_features": [
            "11 英寸 LCD，2112×1320 分辨率、16:10、90Hz、10 点触控，标准版 500nits / NXTPAPER 版 400nits（日光模式 500nits）",
            "NXTPAPER 版搭载 NXTPAPER 3A Crystal 类纸技术，支持 Color Paper / Ink Paper 模式，标配 4096 级压感 T-Pen 2 与翻盖保护套",
            "8000mAh 电池 + 20W 充电，机身 251.28×163.2×6.2mm，标准版 430g / NXTPAPER 版 426g，IP54",
            "Helio G100 + 6GB RAM + 128GB 存储，microSD 最高 2TB，四扬声器，内置 Google Gemini 与 Circle to Search"
        ],
        "why_important": "这是 TCL 自家在北美以 180/250 美元双 SKU 打穿 11 英寸入门段的完整方案：同一套 Helio G100 主板，靠「类纸屏 + 手写笔 + 皮套」把 BOM 只加 60 美元就拉出 50 美元价差，属于典型的显示技术差异化定价模型。对平板事业部而言，可直接对标其 NXTPAPER 膜材/AG 处理成本与 2.1K 90Hz 面板的降本空间，也是判断 11 英寸 6.2mm/426g 结构件可行性的现成参照。",
        "terminal_relevance": "11 英寸入门平板：自家海外定价与显示技术基准，直接竞品参照",
        "vendor": "TCL（TCL 通讯）", "model": "TAB A1、TAB A1 NXTPAPER",
        "sources": "NotebookCheck / PR Newswire（TCL 官方稿）",
        "remark": "美国官网标价 $189.99/$249.99；亚马逊实际挂牌 $179.99/$229.99。与已收录的 NXTPAPER Note A1 为不同产品线"
    },
    {
        "region": "intl", "status": "released",
        "title": "Motorola Pad 70",
        "stars": 3, "source": "C", "date": "2026-08-08", "domain": "平板",
        "url": "https://www.gadgets360.com/pad-70-price-in-india-137206",
        "url_label": "Gadgets360",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "12.1 英寸 1600×2560，天玑 6400 + 8GB/128GB，10200mAh，530g / 6.49mm，Android 16，₹33,999",
        "tech_features": [
            "12.10 英寸 1600×2560 触控屏，机身 278.80×181.05×6.49mm、530g",
            "联发科天玑 6400 八核处理器 + 8GB RAM + 128GB 存储",
            "10200mAh 电池，Android 16（Hello UI），蓝牙 5.2",
            "1300 万像素后置 + 800 万像素前置，Pantone Sea Angel 配色"
        ],
        "why_important": "把「12.1 英寸 2.5K + 10200mAh + 天玑 6400」压到 530g/6.49mm、₹33,999（约 2800 元人民币），说明大电池与轻薄在大尺寸平板上已可同时成立，关键在于 SoC 降档与电池能量密度。这是 12 英寸档定价与堆叠的直接参照。",
        "terminal_relevance": "12 英寸大电池平板：轻薄/续航/成本三角对标",
        "vendor": "摩托罗拉（Motorola / 联想旗下）", "model": "Pad 70",
        "sources": "Gadgets360",
        "remark": "与同门 Pad 70 Groove、Pad 70 Pro 构成三档矩阵，本条为标准版"
    },
    {
        "region": "intl", "status": "released",
        "title": "Moto Pad 70 Groove",
        "stars": 5, "source": "B", "date": "2026-08-07", "domain": "平板",
        "url": "https://www.notebookcheck-cn.com/9-JBL-12-1.1357551.0.html",
        "url_label": "NotebookCheck",
        "signal_type": "开售",
        "confirm_count": "4 个印证源",
        "key_params": "12.1 英寸 2560×1600 120Hz IPS（800nits / 98% DCI-P3），天玑 7400 + 8GB/256GB，9 单元 JBL Pro 扬声器，10200mAh，₹38,999",
        "tech_features": [
            "9 单元 JBL Pro 扬声器系统（4 高音 + 3 低音 + 2 被动辐射器）+ 杜比全景声，配对后可整体当作蓝牙音箱使用",
            "12.1 英寸 2560×1600 IPS，120Hz、800nits 峰值、98% DCI-P3、杜比视界 + HDR10",
            "天玑 7400 + 8GB LPDDR5 + 256GB UFS 3.1，microSD 最高扩展 2TB",
            "10200mAh 电池，随附 68W 适配器（机身实际约 45W TurboPower），金属机身 IP52，最薄 6.8mm / 775g，内置 360° 支架"
        ],
        "why_important": "把 9 颗扬声器（含 2 颗被动辐射器）塞进 775g 平板、并附赠内置支架，是「影音平板」形态的一次结构性重构（代价是扬声器凸起处厚度到 22.7mm）。价值在于：它验证了多单元声学腔体 + 被动辐射器在大屏机身上的堆叠与配重方案，以及「平板即蓝牙音箱」这一产品定义能否支撑 ₹38,999（约 3200 元）的溢价。",
        "terminal_relevance": "影音平板：多单元扬声器腔体、被动辐射器、支架一体化结构",
        "vendor": "摩托罗拉（Motorola / 联想旗下）", "model": "Moto Pad 70 Groove",
        "sources": "NotebookCheck",
        "remark": "本质上是联想 Tab Plus Gen 2（美国 $349.99）的印度换标版；官方标价 ₹38,999，优惠价约 ₹33,999–36,999"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Apple iPad mini（OLED 版）",
        "stars": 3, "source": "B", "date": "2026-08-30", "domain": "平板",
        "url": "https://9to5mac.com/2026/08/30/apples-next-ipad-mini-is-almost-here-heres-what-to-expect/",
        "url_label": "9to5Mac",
        "signal_type": "爆料",
        "confirm_count": "3 个印证源",
        "key_params": "8.x 英寸 OLED（现款 8.3 英寸 LCD），A19 Pro / A20 Pro，振动式扬声器，重新设计外壳提升防水，预计 10 月底前开售",
        "tech_features": [
            "首次由 8.3 英寸 Liquid Retina LCD 换装 OLED 面板，为 2024 年 10 月以来首次更新",
            "处理器由 A17 Pro 升级，爆料指向 A19 Pro 或 A20 Pro（最终未确认）",
            "引入振动式扬声器系统，取代传统扬声器开孔，有望带来全线防水能力",
            "起售价已由 499 美元上调至 599 美元，OLED 版是否继续上探未定"
        ],
        "why_important": "8.x 英寸小平板是 11 英寸以下产品线的直接空白参照。苹果用 OLED + 振动发声（取消扬声器开孔）解决小机身音腔与防水矛盾，这条路径对小尺寸平板的堆叠有直接借鉴意义。需注意传闻称其为 LTPS OLED、刷新率仍可能停留在 60Hz。",
        "terminal_relevance": "小尺寸平板：OLED 化 + 无开孔振动发声 + 防水结构",
        "vendor": "苹果（Apple）", "model": "iPad mini（下一代 OLED）",
        "sources": "9to5Mac / Bloomberg（Gurman）",
        "remark": "纯爆料条目，无官方确认，规格可能在发布前变化，建议作为路线图信号跟踪"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Apple iPhone 18 Pro / Pro Max",
        "stars": 5, "source": "B", "date": "2026-08-31", "domain": "手机",
        "url": "https://9to5mac.com/2026/08/31/iphone-18-pro-is-coming-heres-whats-new-with-each-model/",
        "url_label": "9to5Mac",
        "signal_type": "爆料",
        "confirm_count": "5 个印证源",
        "key_params": "A20 Pro（2nm），6.3/6.9 英寸 LTPO+ 120Hz，灵动岛缩 35%，三颗 48MP，12GB 内存 + 自研 C2 基带",
        "tech_features": [
            "全球首发 A20 Pro，与 M6 同属一个芯片家族，工艺指向 TSMC 2nm",
            "6.3 英寸（Pro）/ 6.9 英寸（Pro Max）LTPO+ OLED，保留 120Hz ProMotion，功耗与频闪进一步改善",
            "灵动岛开孔面积缩小约 35%，部分 Face ID 组件移至屏下；背板玻璃与铝中框色彩过渡统一",
            "后置三颗 4800 万像素，可变光圈据最新口径为 Pro Max 独占；全系 12GB 内存 + 自研 C2 基带"
        ],
        "why_important": "A20 Pro 是首颗「AI 时代」定位的旗舰移动 SoC，配合自研 C2 基带与 LTPO+ 屏，三者共同决定端侧 AI 的能效上限——这正是平板端侧 AI 预研要盯的同一套技术栈。灵动岛缩 35% 意味着屏下 Face ID 模组工程化已可量产，对平板全面屏前摄方案的路线判断有直接参考价值。",
        "terminal_relevance": "2nm 旗舰 SoC、屏下 3D 传感、LTPO+ 面板、自研基带共同决定平板端侧 AI 上限",
        "vendor": "苹果（Apple）", "model": "iPhone 18 Pro、iPhone 18 Pro Max",
        "sources": "9to5Mac / Bloomberg（Gurman）",
        "remark": "9 月 9 日发布会，预计 9 月 12 日预购、9 月 18 日上市（均为传闻）；可变光圈归属存在矛盾报道"
    },
    {
        "region": "intl", "status": "coming",
        "title": "POCO X8 / POCO X8 Power",
        "stars": 4, "source": "B", "date": "2026-08-31", "domain": "手机",
        "url": "https://www.gsmarena.com/poco_reveals_more_x8_and_x8_power_specs_ahead_of_their_september_4_launch-news-74413.php",
        "url_label": "GSMArena",
        "signal_type": "官宣",
        "confirm_count": "4 个印证源",
        "key_params": "X8：9000mAh + 67W 有线 + 22.5W 反充；X8 Power：10000mAh + 100W 有线 + 27W 反充；6.83 英寸 1.5K 120Hz AMOLED（3500nits）",
        "tech_features": [
            "X8 内置 9000mAh 电池，支持 67W 有线与 22.5W 反向有线，官方称可续航 3.2 天",
            "X8 Power 内置 10000mAh（POCO 史上最大电池），支持 100W 有线与 27W 反向充电，官方称可续航 3.5 天",
            "6.83 英寸 1.5K AMOLED，120Hz、3500nits 峰值亮度、康宁大猩猩 Victus 2 玻璃，双立体声扬声器",
            "同时通过 IP66 / IP68 / IP69 / IP69K 四重防护认证，电池标称 6 年寿命；9 月 4 日 12:00 印度发布"
        ],
        "why_important": "10000mAh 硅碳负极电池进入 6.83 英寸手机机身，且仍保留 100W 快充与 IP69K，意味着高硅体系电芯的循环与结构强度已进入可量产区间。对平板而言，这条供应链节点是判断 12000mAh 级平板电芯成本与厚度的关键前置信号。",
        "terminal_relevance": "万毫安硅碳电芯 + 百瓦快充 + IP69K 的量产信号，直接外溢到平板电池选型",
        "vendor": "小米旗下 POCO（Xiaomi POCO）", "model": "POCO X8 5G、POCO X8 Power 5G",
        "sources": "GSMArena / POCO India 官方",
        "remark": "印度市场首发；X8 疑为 Redmi Note 17 Pro 换标、X8 Power 疑为 Redmi Note 17 Pro Max 换标，但本条为海外 SKU"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Apple Watch Ultra 4",
        "stars": 4, "source": "B", "date": "2026-08-28", "domain": "智能手表",
        "url": "https://9to5mac.com/2026/08/28/heres-how-apple-watch-ultra-4-will-differentiate-itself-from-prior-models/",
        "url_label": "9to5Mac",
        "signal_type": "爆料",
        "confirm_count": "3 个印证源",
        "key_params": "全新 S 系列芯片（S11/S12），内部传感器元件数量翻倍，高血压相关新功能已过 FDA 审查，续航或较 Ultra 3 的 42 小时提升约 20%",
        "tech_features": [
            "Digitimes 多次爆料称内部传感器元件数量将「翻倍」，为历代最大幅度传感层升级",
            "搭载全新 S 系列芯片（预计命名 S11 或 S12），为 2023 年 S9 以来首次真正的 CPU 性能跃升",
            "与 watchOS 27 的 Siri AI 同期落地，芯片升级重点在本地算力、内存管理与神经网络单元",
            "续航据爆料较 Ultra 3 的 42 小时提升约 20%；Gurman 口径为「无重大设计改款」，陶瓷表壳可能回归"
        ],
        "why_important": "苹果在手表上把「传感器数量翻倍 + 首颗 AI 时代 S 芯片」打包落地，验证了多传感器融合下穿戴端侧 AI 的功耗可行性。价值在于：它给出了「传感密度 × 端侧 NPU × 续航」三者的现实平衡点，可作为平板/穿戴协同健康功能的架构参照。",
        "terminal_relevance": "智能手表：多传感器融合 + 端侧 AI 芯片的功耗平衡基准",
        "vendor": "苹果（Apple）", "model": "Apple Watch Ultra 4",
        "sources": "9to5Mac / Digitimes / Bloomberg",
        "remark": "9 月 9 日发布会；设计是否改款存在 Digitimes 与 Gurman 的矛盾口径；高血压功能为趋势预警而非直接测血压值"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Apple Watch Series 12",
        "stars": 3, "source": "B", "date": "2026-08-21", "domain": "智能手表",
        "url": "https://9to5mac.com/2026/08/21/apple-watch-series-12-and-ultra-4-to-get-one-big-upgrade-at-perfect-time/",
        "url_label": "9to5Mac",
        "signal_type": "爆料",
        "confirm_count": "3 个印证源",
        "key_params": "与 Ultra 4 同代全新 S11/S12 芯片，陶瓷表壳回归，心率传感器支持全天持续采集，健康/健身 App 重新设计",
        "tech_features": [
            "搭载全新 S 系列芯片（S11 或 S12），为 2024 年 S10 之后的首次架构级迭代",
            "陶瓷表壳回归，为 2017 年 Series 3 之后首次，苹果已测试白色与深灰色两种方案",
            "心率传感器升级为全天持续采集数据，突破此前非运动场景数分钟一读的限制",
            "健康与健身 App 重新设计，呈现方式参考 Whoop 与 Oura；今年不推出 Apple Watch SE 4"
        ],
        "why_important": "「全天连续心率采集」从定时抽样走向连续流式，是穿戴传感器功耗与算法的一次分水岭——连续采样带来的功耗增量必须由新 S 芯片的能效抵消。这个权衡对平板上健康外设/配件（连续体征监测底座）的架构设计有直接参考。",
        "terminal_relevance": "连续体征采样 + 芯片能效的权衡，可外溢到平板健康配件架构",
        "vendor": "苹果（Apple）", "model": "Apple Watch Series 12",
        "sources": "9to5Mac / Bloomberg（Gurman）",
        "remark": "与 Ultra 4 同为 9 月 9 日发布；外观预计无大改，核心升级在内部"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Halliday G2 显示 AI 眼镜",
        "stars": 5, "source": "A", "date": "2026-07-21", "domain": "AR-VR眼镜",
        "url": "https://www.hallidayglobal.com/",
        "url_label": "Halliday 官网",
        "signal_type": "官宣",
        "confirm_count": "4 个印证源",
        "key_params": "双目光波导 + 双 microLED，单眼 600×300 / FOV 25.2° / 峰值 1600nits，49g / 210mAh / 12 小时，无摄像头，$599",
        "tech_features": [
            "双目衍射光波导 + 双 microLED 光机，单眼 600×300 分辨率、25.2° 视场角、峰值亮度 1600nits，显示色为单绿色",
            "整机 49g（镜宽 47mm / 镜高 41mm / 镜腿 167mm），210mAh 电池、12 小时常规续航、磁吸充电，IP54",
            "4 麦克风阵列 + 4 单元开放式扬声器（含反相抵消提升私密性），蓝牙 5.4 LE Audio，右镜腿 73mm 触控条",
            "完全无摄像头设计；支持 45+ 语言实时翻译；处方镜片 SPH -9.00~+2.00D、CYL ±3.00D，镜片透光率 98%"
        ],
        "why_important": "Halliday G2 是「去摄像头 + 双目光波导 + 49g」路线的代表：砍掉摄像头换来 12 小时续航与办公场景的社交可接受度，并用双 microLED 把亮度顶到 1600nits 解决户外可读。这条「单绿、低分辨率、高亮度、轻重量」的技术取向，与彩色全彩 MicroLED 路线形成清晰分叉，对近眼显示的物料选型是重要的成本/体验对照样本。",
        "terminal_relevance": "AR 眼镜：双目光波导 + 双 microLED 光机、无摄像头轻量化架构、处方镜片一体化",
        "vendor": "Halliday（Halliday Global）", "model": "Halliday G2",
        "sources": "Halliday 官网（含 G2 Spec Sheet）",
        "remark": "7 月 21 日发布，预计 9 月开始发货；MSRP $599，$10 优先预约可抵 $100（实付 $499）并含 $199 处方镜片抵扣"
    },
    {
        "region": "intl", "status": "coming",
        "title": "ROG XREAL R1 Edition 20 电竞 AR 眼镜",
        "stars": 4, "source": "A", "date": "2026-08-26", "domain": "AR-VR眼镜",
        "url": "https://press.asus.com/news/press-releases/rog-xbox-ally-x20-bundle-taiwan-preorder",
        "url_label": "ASUS Pressroom（华硕官方）",
        "signal_type": "官宣",
        "confirm_count": "3 个印证源",
        "key_params": "双 1080p Micro-OLED，4 米等效 171 英寸虚拟屏，240Hz / 0.01ms，57° FOV，原生 3DoF + 电致变色，Bose 音效",
        "tech_features": [
            "双 1080p Micro-OLED，通过 USB-C 在 4 米距离呈现最高 171 英寸虚拟巨幕，视场角 57°",
            "240Hz 刷新率与 0.01ms 响应时间，支持悬停（Anchor）与跟随两种显示模式",
            "内置原生 3DoF 头部追踪，并支持实时 2D 转 3D 功能；搭配电致变色镜片适配不同环境",
            "采用 Bose 音效技术；单根 USB-C 直连 ROG Xbox Ally X20；同捆套装限量 200 组，单机 $1,299"
        ],
        "why_important": "240Hz 刷新率把「AR 眼镜」的显示规格推到电竞显示器级别，说明 Micro-OLED + 显示驱动链已能支撑高刷；同时用一根 USB-C（DP Alt Mode）完成供电 + 视频 + 与掌机联动，是「主机/掌机外挂屏」形态的成熟工程解。对平板预研的价值：它是 USB-C DP 输出 + 近眼显示协同方案的现成参照。",
        "terminal_relevance": "AR 眼镜：240Hz Micro-OLED 驱动链、单线缆 USB-C DP 直连、电致变色片",
        "vendor": "华硕 ROG / XREAL", "model": "ROG XREAL R1 Edition 20",
        "sources": "ASUS Pressroom 官方新闻稿",
        "remark": "同捆的 ROG Xbox Ally X20 掌机 10 月 15 日上市；眼镜可单独购买，单机 $1,299、套装 $2,499"
    },
    {
        "region": "intl", "status": "released",
        "title": "Samsung Galaxy Book6 14 英寸（入门款）",
        "stars": 4, "source": "A", "date": "2026-09-01", "domain": "笔记本",
        "url": "https://news.samsung.com/uk/samsung-expands-the-galaxy-book6-lineup-making-galaxy-book-more-accessible",
        "url_label": "Samsung Newsroom U.K.（官方）",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "14 英寸 WUXGA 1920×1200 LCD（350nits），Intel Core 5 + NPU 最高 15 TOPS，61.2Wh / 25 小时视频，15.7mm / 1.35kg，£799",
        "tech_features": [
            "14.0 英寸 16:10 WUXGA（1920×1200）LCD，350nits，抗反射处理",
            "英特尔酷睿 5 处理器 + 英特尔 NPU 最高 15 TOPS，支持 Galaxy AI（AI Select、Note Assist 等）",
            "61.2Wh（典型值）电池，标称本地视频播放最长 25 小时，45W USB-C 充电 30 分钟充入约 33%",
            "313.0×221.0×15.7mm / 1.35kg，双 USB-C + USB-A + HDMI 1.4（4K@30）+ 3.5mm，Wi-Fi 6E + 蓝牙 5.4"
        ],
        "why_important": "三星用「Core 5 + 15 TOPS NPU + 61.2Wh」把 AI PC 的价格打到 £799，关键是主动把 NPU 从 49 TOPS 砍到 15 TOPS、内存从 16GB 降到 8GB 起。这个「NPU 分级 + 存储降档」的降本模型，对平板的 AI PC 化定价有直接参考价值——也侧面印证当前内存涨价对整机 BOM 的压力。",
        "terminal_relevance": "入门 AI PC 的 NPU 分级降本模型、25 小时续航的功耗设计",
        "vendor": "三星电子（Samsung Electronics）", "model": "Galaxy Book6 14 英寸（Core 5 / Core 3 版本）",
        "sources": "Samsung Newsroom U.K. 官方稿",
        "remark": "2026 年 9 月 1 日在英国与韩国同步上市；8GB/16GB LPDDR5X、256GB/512GB PCIe 可选，首发 Violet Silver 与 Grey"
    },
    {
        "region": "intl", "status": "released",
        "title": "ASUS Zenbook A14（UX3480QA）",
        "stars": 4, "source": "B", "date": "2026-08-31", "domain": "笔记本",
        "url": "https://www.notebookcheck.net/Asus-releases-new-14-inch-laptop-internationally-with-Snapdragon-X-and-30-hours-of-battery-life.1383926.0.html",
        "url_label": "NotebookCheck",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "14 英寸 1920×1200 OLED（100% DCI-P3），骁龙 X（X1-26-100）八核，50Wh / 30 小时本地视频，1.1kg，£799 起",
        "tech_features": [
            "高通骁龙 X（X1-26-100）八核平台，搭配 LPDDR5X 内存与 M.2 2280 PCIe 4.0 SSD",
            "14 英寸 1920×1200 OLED，60Hz，100% DCI-P3 色域覆盖",
            "50Wh 三芯电池，官方标称本地视频播放最长 30 小时、网页浏览最长 18 小时，支持 68W 充电",
            "整机 1.1kg，蓝牙 5.3 + Wi-Fi 6E；英国 £799（8GB+256GB）起，16GB+512GB 版 £1,199"
        ],
        "why_important": "在 1.1kg 机身里做到 OLED + 30 小时本地视频续航，说明骁龙 X 平台在轻薄本上的能效比已能与 x86 拉开身位；代价是 8GB 起步与 60Hz 刷新率。这个「能效优先、体验让位」的配置取舍，恰好是平板做 Windows/ARM 双平台预研时要权衡的同一组变量。",
        "terminal_relevance": "ARM 平台能效上限、OLED 低功耗调校、1.1kg 轻薄结构",
        "vendor": "华硕（ASUS）", "model": "Zenbook A14 UX3480QA",
        "sources": "NotebookCheck",
        "remark": "6 月 Computex 2026 首发、8 月先在中国开售，8 月 31 日起国际版上市（英国/欧元区/加拿大/德国/美国）"
    },
    {
        "region": "intl", "status": "released",
        "title": "Anker Prime Qi2 25W 折叠三合一无线充电站",
        "stars": 3, "source": "B", "date": "2026-08-31", "domain": "无线充",
        "url": "https://9to5mac.com/2026/08/31/ankers-foldable-3-in-1-charger-brings-25w-qi2-charging-into-something-pocket-sized/",
        "url_label": "9to5Mac",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "Qi2.2 认证 25W，iPhone 17 Pro 26 分钟充至 50%，AirCool 主动温控 19dB，随附 45W USB-C 适配器",
        "tech_features": [
            "通过 Qi2.2 认证，最高 25W 磁吸无线充电（此前多数 MagSafe 配件长期停留在 7.5W 上限）",
            "官方称可让 iPhone 17 Pro 在 26 分钟内充至 50%，约为标准 5W 无线充电的 5 倍",
            "内置 AirCool 主动温控，运行噪音 19dB，可将手机温度控制在 37°C 以下并维持满速 25W",
            "三合一布局：主 MagSafe 区 + 侧边 MFi 认证 Apple Watch 充电器 + 底部 AirPods 充电板；随附 45W USB-C 墙插"
        ],
        "why_important": "Qi2.2 的 25W 已把无线充推到「必须配主动散热」的门槛——Anker 用 19dB 风扇把机身温度压在 37°C 以内换满速输出，这是该功率段的热设计范式。若未来在平板上做高功率磁吸/反向无线充，这套「风扇噪音 vs 温升 vs 充电曲线」的工程三角就是必须复用的参考。",
        "terminal_relevance": "Qi2.2 25W 的热设计范式，可迁移到平板高功率无线充/反向充",
        "vendor": "安克（Anker Innovations）", "model": "Anker Prime Qi2 25W Foldable 3-in-1（A25N1）",
        "sources": "9to5Mac / Anker 官网",
        "remark": "已在 Amazon 与 Anker 官网开售，可折叠至接近 iPhone 17 Pro Max 的体积；与在售的 Anker Prime MagGo Qi2.2 3-in-1 为不同型号"
    },
    {
        "region": "intl", "status": "released",
        "title": "JBL Pulse 6",
        "stars": 4, "source": "A", "date": "2026-08-26", "domain": "智能音箱",
        "url": "https://m.news.harman.com/releases/jbl-pulse-6-is-here-to-light-up-every-beat",
        "url_label": "HARMAN Newsroom（官方）",
        "signal_type": "官宣",
        "confirm_count": "3 个印证源",
        "key_params": "AI Sound Boost + 新声学设计，16 套灯效主题，360° 灯效提手，蓝牙 6.0 + USB-C 无损，Auracast，IP68，12 小时，$329.95",
        "tech_features": [
            "AI Sound Boost 实时分析音乐并最大化声学表现、降低失真，配合新声学设计强化低频",
            "360° 可编程灯效共 16 套主题（10 套氛围 + 6 套派对），提手集成灯带，整机 1.49kg",
            "蓝牙 6.0 + USB-C 无损音频播放，支持 Auracast 多音箱串联与两台立体声配对",
            "IP68 防尘防水、12 小时续航；Sunset Mode 最长 60 分钟渐暗倒计时，双击触发 Bedside Lamp 模式"
        ],
        "why_important": "蓝牙 6.0 + USB-C 无损 + Auracast 广播音频在便携音箱上同时到位，意味着 LE Audio/Auracast 生态已进入消费级出货阶段；AI Sound Boost 的「实时失真抑制」则是小腔体大动态的 DSP 解法。这两点都能反向输入到平板的音频架构：多扬声器腔体的 DSP 调校路径、以及是否要预埋 Auracast 广播发射能力。",
        "terminal_relevance": "蓝牙 6.0/Auracast 生态成熟度、小腔体 AI DSP 调校，可反哺平板多扬声器音频架构",
        "vendor": "JBL / HARMAN（哈曼国际）", "model": "JBL Pulse 6",
        "sources": "HARMAN Newsroom 官方新闻稿",
        "remark": "JBL 80 周年节点发布，售价 $329.95，9 月 6 日发货；提手采用含 93% 回收金属的材料"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Apple AirPods 5",
        "stars": 3, "source": "B", "date": "2026-08-31", "domain": "AI耳机·耳穿戴",
        "url": "https://9to5mac.com/2026/08/31/airpods-5-heres-what-rumors-say-will-launch-next-week",
        "url_label": "9to5Mac",
        "signal_type": "爆料",
        "confirm_count": "3 个印证源",
        "key_params": "9 月 9 日随 iPhone 18 Pro 发布，分「带 ANC」与「不带 ANC」双版本；不含摄像头（摄像头版推迟至 2027）",
        "tech_features": [
            "推出两个明确版本：带主动降噪（ANC）与不带 ANC，延续 AirPods 4 的双版本策略",
            "带红外摄像头的版本（用于 Siri 视觉智能、环境感知）已确认推迟到 2027 年",
            "苹果正在研发 H3 芯片，主打更低延迟与更好音质，但是否用于 AirPods 5 尚未确认",
            "历代节奏：AirPods 2016、AirPods 2 2019、AirPods 3 2021、AirPods 4 2024，AirPods 5 预计不继承 Pro 3 的心率传感器"
        ],
        "why_important": "苹果把「视觉智能」从眼镜迁移到耳机的关键原因，是照顾戴眼镜人群——把摄像模块剥离到耳机后，用户可继续佩戴自己的近视镜，且左右耳各一颗可合成立体视觉。这条「分布式双目传感 + 耳机形态」的路线，是 AI 穿戴形态学上的重要分叉，值得在 AI 眼镜/耳机产品定义阶段同步跟踪。",
        "terminal_relevance": "视觉智能的「眼镜 vs 耳机」形态分叉、双目分布式传感路线判断",
        "vendor": "苹果（Apple）", "model": "AirPods 5（ANC 版 / 标准版）",
        "sources": "9to5Mac / Bloomberg（Gurman）",
        "remark": "本条为爆料，发布前规格可能变化；摄像头版内部代号传闻为 B790 / B798，已移出 2026 路线图"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 15, True),
    ("显示/OLED", 18, True),
    ("折叠屏", 0, True),
    ("手写笔/触控", 3, True),
    ("散热/液冷", 3, True),
    ("电池/续航", 24, True),
    ("快充/无线充", 12, True),
    ("影像", 4, True),
    ("AI/NPU", 12, True),
    ("音频/扬声器", 12, True),
    ("5G/通信", 3, True),
    ("Wi-Fi/连接", 6, True),
    ("AR/VR显示", 3, True),
    ("材质/工艺", 6, True),
    ("可持续/模块化", 2, True),
    ("手柄/外设", 1, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {"rank": 1, "title": "TCL TAB A1 / TAB A1 NXTPAPER", "dim": "平板电脑", "stars": 5, "key": "B级 / 11\"90Hz+8000mAh / NXTPAPER 3A Crystal / $179.99 起（自家产品）"},
    {"rank": 2, "title": "网易有道 OpenPods AI 耳机", "dim": "AI耳机", "stars": 5, "key": "B级 / 单耳 7g / 耳机舱独立麦克风+256MB 存储 / 32h"},
    {"rank": 3, "title": "REDMI K100 Pro Max", "dim": "手机", "stars": 5, "key": "B级 / 9070mAh 硅碳 / 6300mm² 循环冷泵 / 185Hz"},
    {"rank": 4, "title": "Halliday G2", "dim": "AR/VR眼镜", "stars": 5, "key": "A级 / 49g 双目光波导 / 1600nits / 无摄像头 12h"},
    {"rank": 5, "title": "Moonix AI 眼镜标准版", "dim": "AR/VR眼镜", "stars": 5, "key": "B级 / 14.9g / 39+ 可换镜框 / 16h 续航"},
]
'''

src = open(TEMPLATE, encoding="utf-8").read()

# ① 只替换模板部分（此时尚未拼接 CHUNK），避免污染 CHUNK 内的卡片日期
src = src.replace("2026-08-26", "2026-09-01")
src = src.replace('WEEK = "周三"', 'WEEK = "周二"')
src = src.replace("采集口径：7类智能终端", "采集口径：8类智能终端")
src = src.replace('<div class="stat-num">7</div>', '<div class="stat-num">8</div>')

# ② 排序键兜底：部分卡片日期只到月（如 "2026-07"），取"日"切片为空会 int('') 报错
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
