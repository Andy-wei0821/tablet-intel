#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 WB_2026-09-07_硬件看板.html
做法：读取 gen_wb_2026-08-26.py 模板，先替换模板内 日期/周几/类别数(7→8)/副标题补全/排序兜底，
     再注入 CARDS/DIMS/TOP5，exec 生成。
     注意：先替换 src 再拼接 CHUNK，避免全局 replace 污染 CHUNK 内的卡片日期。
"""
import os

TEMPLATE = r"E:\AI相关\预研究\202608\03_输出\gen_wb_2026-08-26.py"

CHUNK = r'''CARDS = [
    # ========== 国内 15 条 ==========
    {
        "region": "cn", "status": "released",
        "title": "联想 Yoga Tab Plus Gen 2",
        "stars": 5, "source": "B", "date": "2026-09-03", "domain": "平板",
        "url": "https://tech.ifeng.com/c/8w94W6qyZrD",
        "url_label": "凤凰网科技（转 IT之家）",
        "signal_type": "首发",
        "confirm_count": "4 个印证源",
        "key_params": "13 英寸 3840×2560 144Hz OLED 1100nits，骁龙 8 Elite，12700mAh + 68W，哈曼卡顿 6 扬，849 欧元起（约 999.99 美元），Android 17 + 7 次 OS 升级",
        "tech_features": [
            "13 英寸 3:2 纯平 3840×2560 PureSight Pro 屏，144Hz 自适应刷新，峰值亮度 1100nits，100% DCI-P3，杜比视界认证",
            "骁龙 8 Elite（Oryon CPU）+ 最高 16GB+512GB，预装 Android 17，承诺 7 次 OS 升级至 Android 24、安全更新至 2033 年",
            "12700mAh 大电池配 68W 快充，双频 Wi-Fi 7 + 蓝牙 6.0，支持 2TB microSD 扩展",
            "哈曼卡顿 6 扬声器，Tab Pen Pro 2 手写笔 8192 级压感磁吸收纳，国内型号即拯救者 Y900 13"
        ],
        "why_important": "这是安卓平板首个把骁龙 8 Elite、13 英寸 4K 144Hz、12700mAh 和 7 年系统更新打包进 849 欧元价位的旗舰，直接抬高了大屏创作平板的 BOM 标杆。对 TCL 预研而言，7 年更新承诺正在成为高端安卓平板的准入门槛；面板侧 4K 144Hz + 1100nits + 杜比视界的组合值得对标，68W 快充在大电池平板上的取舍也值得抄作业。联想用 Yoga 国际版与拯救者国内版双名运作，同样是渠道策略参考。",
        "terminal_relevance": "大屏创作平板：4K 144Hz 旗舰屏 / 12700mAh 长续航 / 7 年系统更新",
        "vendor": "联想", "model": "Yoga Tab Plus Gen 2（拯救者 Y900 13）",
        "sources": "凤凰网科技 / IT之家 / Android Authority / Notebookcheck",
        "remark": "IFA 2026 发布，海外 9 月上市，国行时间未公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "联想 Yoga Tab Gen 2",
        "stars": 4, "source": "B", "date": "2026-09-03", "domain": "平板",
        "url": "https://www.notebookcheck.net/Lenovo-packs-a-4K-144-Hz-display-and-11-000-mAh-battery-into-a-compact-Android-tablet.1387258.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "首发",
        "confirm_count": "4 个印证源",
        "key_params": "11.1 英寸 3840×2560 144Hz 415PPI 1100nits，天玑 9500s，11000mAh + 68W，480g / 8.56mm，649 欧元起，Android 17 + 7 年更新",
        "tech_features": [
            "11.1 英寸 4K 屏（3840×2560，3:2，415PPI），144Hz 自适应（30/60/90/120/144Hz 多档），1100nits，杜比视界",
            "天玑 9500s + 最高 12GB+256GB（2TB microSD），480g / 8.56mm，主打便携创作",
            "11000mAh + 68W 快充，4 扬声器，后置 13MP、前置 8MP+0.3MP",
            "可拆卸支架+键盘 2 合 1 套装（pogo 三点磁吸），预装 Android 17 并支持 7 年更新，内置联想 Qira AI"
        ],
        "why_important": "11 英寸档把 4K 分辨率下放到 649 欧元且做到 480g，说明 3:2 高分屏在中尺寸平板上的成本已压到主流价位——直接挤压 TCL 中端平板的规格空间。天玑 9500s 的引入显示联发科旗舰 SoC 正加速渗透非三星平板，预研选型时天玑 9500 系应作为骁龙之外的第二路线认真评估。注意其 4K 屏全亮度续航压力，12700/11000mAh 的电池军备竞赛还在加码。",
        "terminal_relevance": "中尺寸便携平板：4K 屏下放 / 轻量化 480g / 天玑 9500s 选型",
        "vendor": "联想", "model": "Yoga Tab Gen 2（拯救者 Y900 11）",
        "sources": "Notebookcheck / IT之家 / Android Authority / AndroidPure",
        "remark": "海外 9 月上市；另确认 Plus 版国内型号为拯救者 Y900 13，与已报 Y700 为不同产品"
    },
    {
        "region": "cn", "status": "coming",
        "title": "荣耀 MagicPad 4（国行开启预约）",
        "stars": 4, "source": "B", "date": "2026-09-07", "domain": "平板",
        "url": "https://www.ithome.com/0/999/137.htm",
        "url_label": "IT之家",
        "signal_type": "预约",
        "confirm_count": "2 个印证源",
        "key_params": "12.3 英寸 3K OLED 3000×1920 165Hz 2400nits，第五代骁龙 8，10100mAh，边框 3.9mm、厚 4.8mm（IT之家口径），海外 699/799 欧元",
        "tech_features": [
            "12.3 英寸 3K OLED，3000×1920 分辨率 290PPI，165Hz 高刷，HDR 峰值亮度 2400nits，DCI-P3 广色域 + 10.7 亿色",
            "高通第五代骁龙 8（骁龙 8 Gen 5）移动平台，预装基于 Android 16 的 MagicOS 10",
            "10100mAh 电池（典型值），屏幕边框仅 3.9mm，机身厚度 4.8mm（IT之家口径）",
            "海外版 12GB+256GB 699 欧 / 16GB+512GB 799 欧；国行商城已开启预约，赠生活礼包与视频月卡"
        ],
        "why_important": "荣耀把 12.3 英寸 2400nits OLED + 骁龙 8 Gen 5 + 10100mAh 的组合带向国行，4.8mm 厚度若属实将刷新大屏平板轻薄纪录——直接对标华为 MatePad Air 2026 的 5.3mm/509g，两家在「OLED 大屏轻薄化」上的军备竞赛已白热化。对 TCL 预研的信号很直接：2400nits 峰值亮度 OLED 正在从中高端向主力价位下探，柔光/护眼仍是荣耀的差异化抓手，13-14 英寸档的亮度与轻薄权重明显高于分辨率。",
        "terminal_relevance": "大屏 OLED 平板：2400nits 亮度下探 / 4.8mm 轻薄 / 国行预约启动",
        "vendor": "荣耀", "model": "MagicPad 4",
        "sources": "IT之家 / 荣耀商城",
        "remark": "海外版今年 3 月已发布，本条为国行 9 月 7 日开启预约事件；厚度 4.8mm 为 IT之家口径"
    },
    {
        "region": "cn", "status": "coming",
        "title": "酷比魔方 7.5 英寸 1.5K LCD 插卡平板",
        "stars": 3, "source": "C", "date": "2026-09-06", "domain": "平板",
        "url": "https://www.163.com/dy/article/L653NIL60553TKK8.html",
        "url_label": "网易号（酷安预热汇总）",
        "signal_type": "预热",
        "confirm_count": "2 个印证源",
        "key_params": "7.5 英寸 1.5K 120Hz LCD（京东方 ADS Pro，1300nits），实体 SIM 插卡，处理器不弱于天玑 8300，预计 2499-2999 元",
        "tech_features": [
            "京东方 7.5 英寸 1.5K LCD，ADS Pro 高端 IPS 技术，1300nits 峰值亮度，全亮度 DC 调光",
            "圆偏振光护眼 + SGS 硬件低蓝光，有害蓝光占比压到 30% 以下，120Hz 高刷，18.7:9 类手机比例",
            "实体 SIM 卡槽支持通话，Pad Phone 跨界形态，暂定处理器不弱于天玑 8300（台积电 4nm）",
            "12GB+256GB 版本预计到手价 2499-2999 元，对标已消失的高端 LCD 手机市场"
        ],
        "why_important": "这条的价值不在产品本身，而在信号：LTPS LCD 手机屏出货占比已从 2025 年的 4.4% 跌到 2026 年 2.5%，三星 LG 关停产线后，京东方 ADS Pro 成了中高端 LCD 唯一供给。TCL 华星自有面板线，恰好在护眼 LCD/类纸屏上握有差异化筹码——教育平板和护眼细分完全可以复用这块 1300nits 圆偏振光的方案，把大厂放弃的 LCD 护眼心智接过来。插卡 Pad Phone 形态对出海市场也值得评估。",
        "terminal_relevance": "护眼 LCD 平板：高端 LCD 供给窗口 / 圆偏振光护眼 / 插卡跨界形态",
        "vendor": "酷比魔方", "model": "7.5 英寸 1.5K LCD 插卡平板（型号未定）",
        "sources": "酷安预热 / 网易号",
        "remark": "爆料/预热阶段，最终配置价格未敲定"
    },
    {
        "region": "cn", "status": "coming",
        "title": "努比亚 NaviX Ultra（AI 智能体手机）",
        "stars": 4, "source": "B", "date": "2026-09-01", "domain": "手机",
        "url": "https://www.toutiao.com/article/7680781954052014628",
        "url_label": "今日头条·PChome科技",
        "signal_type": "入网",
        "confirm_count": "4 个印证源",
        "key_params": "9 月 1 日获工信部入网，6.78 英寸 1.5K 144Hz，7100mAh，骁龙 8 Elite Gen5（爆料），9 月正式上市，豆包手机助手端侧运行",
        "tech_features": [
            "全球首款完成大模型备案到终端入网全合规流程的 AI 智能体手机，字节跳动+中兴联合打造",
            "跨应用交互弃用读屏模拟点击，改用 MCP 协议，需应用厂商开放接口，豆包团队正谈头部 App 适配",
            "大模型核心运算全部端侧本地完成，数据不上云，侧边橙色 AI 实体键一键唤醒",
            "6.78 英寸 1.5K 144Hz 直屏，7100mAh 电池，5000 万全焦段三摄，四配色"
        ],
        "why_important": "MCP 取代 GUI 模拟点击，意味着端侧 AI 的落地范式从猜屏幕变成标准协议接口——这对 TCL 平板的 AI 助手预研是路线级参考：平板屏幕大、常驻桌面，恰是跨应用智能体任务（比价、日程、文档流转）的最佳载体，谁先在平板上跑通 MCP 生态谁就占位。同时它验证了 7100mAh+端侧大模型的供电冗余设计思路，大电池不再是手游专属，而是 AI 终端刚需。",
        "terminal_relevance": "AI 终端范式：MCP 端侧智能体 / AI 实体键 / 7100mAh 供电冗余",
        "vendor": "努比亚（中兴）×字节跳动", "model": "NaviX Ultra（豆包手机二代）",
        "sources": "财联社 / PChome / 上海证券报",
        "remark": "骁龙 8 Elite Gen5 为媒体爆料口径，高通仅确认搭载高通芯片"
    },
    {
        "region": "cn", "status": "released",
        "title": "Poco F9 Ultra",
        "stars": 3, "source": "B", "date": "2026-09-01", "domain": "手机",
        "url": "https://www.gadgets360.com/poco-f9-ultra-price-in-india-137380",
        "url_label": "Gadgets360（NDTV）",
        "signal_type": "首发开售",
        "confirm_count": "3 个印证源",
        "key_params": "9 月 1 日全球发布，6.9 英寸 2608×1200 185Hz AMOLED 4500nits，骁龙 8 Elite Gen 5，8050mAh 硅碳电池，100W 有线 + 50W 无线，799 美元起",
        "tech_features": [
            "6.9 英寸 HyperRGB AMOLED，185Hz 刷新率，峰值亮度 4500nits（HDR 局部 10000nits），Gorilla Glass 7i",
            "8050mAh 硅碳负极电池（16% 含硅量，POCO F 系最大），100W 有线 HyperCharge + 50W 无线 + 27W 有线反充",
            "200MP OIS 主摄 + 50MP 5x 潜望长焦 + 50MP 超广角，10x 无损 / 20x AI 超级变焦",
            "Sound by Bose 2.1 声道：双 1115D 对称扬声器 + 1620 独立低音单元（带 LED 节奏灯），VisionBoost D8 独显"
        ],
        "why_important": "小米系把 8050mAh 硅碳+100W 快充+独立低音炮做到 799 美元，证明大容量硅碳电池的成本曲线已陡峭下探——平板电池预研应据此重估 2027 年 10000mAh+ 硅碳方案的 BOM 可行性。手机塞独立低音单元的做法，对平板八扬声器的低频下潜方案也是反向提示：与其堆数量不如给一个真低音。它与 Redmi K100 共用供应链的平台化打法，同样是 TCL 多品牌复用模组的对照样本。",
        "terminal_relevance": "相邻终端 BOM：8050mAh 硅碳 / 100W+50W 双快充 / 手机独立低音单元",
        "vendor": "Poco（小米系）", "model": "Poco F9 Ultra",
        "sources": "Gadgets360 / 多家独立媒体交叉印证",
        "remark": "电池容量以 4 个独立媒体一致口径 8050mAh 硅碳为准；Gadgets360 规格页标注的 10000mAh 为孤例且与其正文不符，已弃用"
    },
    {
        "region": "cn", "status": "released",
        "title": "moto watch ultra",
        "stars": 3, "source": "B", "date": "2026-09-04", "domain": "智能手表",
        "url": "https://gadgets.beebom.com/news/moto-watch-ultra-launched-globally-specifications-features-pricing-availability",
        "url_label": "Beebom Gadgets",
        "signal_type": "发布",
        "confirm_count": "4 个印证源",
        "key_params": "IFA 2026 发布，1.5 英寸 466×466 pOLED 2700nits，骁龙 W5+ Gen 1，550mAh 2 天续航，15 分钟充电 24 小时，429 欧元起，9 月 10 日美国开售",
        "tech_features": [
            "1.5 英寸 2.5D 曲面 pOLED 圆表，466×466，1-60Hz LTPO 可变刷新，峰值 2700nits，Gorilla Glass 3",
            "46mm 不锈钢表壳重 51g，IP68+5ATM，22mm 通用表带，PANTONE 认证配色",
            "摩托罗拉首款 LTE 手表：eSIM 独立通话，双频 GPS，NFC Google Wallet，Wear OS 6 保证升级 Wear OS 7/8",
            "首次内置 Qira 个人 AI：抬腕或喊 Hey Qira 跨 Motorola/Lenovo 设备调用记忆；Polar 运动算法整包引入"
        ],
        "why_important": "Qira 的意义在跨设备记忆：手表抬腕即可调取联想 PC/摩托手机上沉淀的上下文，这是联想系全场景 AI 的腕上入口。对 TCL 的启示是，平板作为家中最大屏的常驻设备，天然应是个人 AI 记忆的沉淀端与展示端，跨端 Agent 检索可以在 TCL 系（平板+雷鸟眼镜+电视）复刻。Polar 算法整包引入而非自研，也提示健康算法可采购化。",
        "terminal_relevance": "跨设备 AI：Qira 记忆入口 / 腕上 Agent / 平板作 AI 沉淀端",
        "vendor": "摩托罗拉（联想系）", "model": "moto watch ultra",
        "sources": "Motorola 官方 / Beebom / PhoneBunch / Gadgetbyte",
        "remark": "欧洲 429 欧元，美国 349.99 美元 9 月 10 日开售，亚太随后"
    },
    {
        "region": "cn", "status": "progress",
        "title": "阿里 Qoder 眼镜版（接入千问 AI 眼镜）",
        "stars": 4, "source": "B", "date": "2026-09-03", "domain": "AR-VR眼镜",
        "url": "https://www.toutiao.com/article/7681140816353509926",
        "url_label": "今日头条·鞭牛士",
        "signal_type": "官宣",
        "confirm_count": "3 个印证源",
        "key_params": "9 月 3 日阿里云官宣 Qoder 眼镜版，首批接入千问 AI 眼镜和乐奇 AI 眼镜，定向邀测已开启，完整功能 2026 云栖大会发布",
        "tech_features": [
            "全双工语音方案：可随时打断、连续交代任务、追问进展、追加要求，非单轮问答",
            "高风险操作与关键节点以卡片投射视野边角，语音确认或轻触镜腿两种审批方式，进度语音播报",
            "眼镜端摄像头第一视角感知：识别代码报错、设备运行状态、白板草图、屏幕内容",
            "桌面端（深度执行）+ 移动端（远程管控）+ 眼镜版（第一视角输入）三端协同架构"
        ],
        "why_important": "眼镜被阿里定义为 Agent 的眼睛+审批终端，而计算在云端和桌面——这给了一个清晰分工模型：眼镜负责第一视角输入与低带宽确认，平板这类大屏负责展示完整任务流与深度交互。TCL 若做自有 Agent，平板+眼镜的组合里平板应是任务控制台，而不是把所有 AI 塞进眼镜。云栖大会前的定向邀测节奏，也提示 Q4 国产 AI 眼镜生态战将围绕谁接入谁的平台展开。",
        "terminal_relevance": "AI 生态：眼镜作第一视角入口 / 平板作任务控制台 / 云端 Agent 分工",
        "vendor": "阿里云", "model": "Qoder 眼镜版（千问 AI 眼镜/乐奇 AI 眼镜）",
        "sources": "阿里云官宣 / 鞭牛士 / 凤凰网科技",
        "remark": "目前为平台侧生态接入事件，千问眼镜硬件参数官方未披露"
    },
    {
        "region": "cn", "status": "progress",
        "title": "GOSIGHT P1（双目全彩 AI+AR 眼镜）",
        "stars": 4, "source": "A", "date": "2026-09-04", "domain": "AR-VR眼镜",
        "url": "https://www.globenewswire.com/news-release/2026/09/04/3356376/0/en/gosight-p1-moves-full-color-ar-into-continuous-use-with-binocular-display-and-seamless-battery-swapping.html",
        "url_label": "GlobeNewswire（GOSIGHT 官方通稿）",
        "signal_type": "官宣",
        "confirm_count": "2 个印证源",
        "key_params": "IFA 2026 首发，双目 0.3 英寸全彩 Micro-OLED + 阵列光波导，等效 105 英寸@6 米 60Hz，透光率 85%+，约 69g，内置桥接电池 + 热插拔外置电池，12MP 摄像头",
        "tech_features": [
            "双目 0.3 英寸 Micro-OLED + 全彩阵列光波导，等效 6 米外 105 英寸画面，60Hz，自动亮度调节，低畸变高对比",
            "目标透光率 85% 以上，抑制彩虹纹/网格纹/漏光，息屏态接近普通眼镜",
            "整机目标约 69g，锻造碳纤维纹理镜腿，六种配色，可换偏光太阳镜片",
            "供电架构：内置桥接电池 + 可热插拔外置电池，换电不断电不重启；12MP 第一视角摄像头 1080p 视频，取景器直投双目，硬件级隐私指示灯"
        ],
        "why_important": "全彩 AR 眼镜的竞争正从「能不能显示」转向「能不能一直用」，GOSIGHT 把热插拔换电做成不断电架构，与 INMO GO3 的可换电路线互相印证——电池形态创新正在取代亮度堆料成为全彩 AR 的主战场。GlaxReality 光学底座 + 自有整机品牌的组合，说明国内光波导供应链已能支撑新品牌直接下场整机。众筹前才公布最终续航与换电参数的节奏也提醒：这类目标值尚需验证，TCL 跟踪时要以实测口径为准。",
        "terminal_relevance": "全彩 AR 眼镜：热插拔换电不断电 / 阵列光波导量产 / 目标值待验证",
        "vendor": "GOSIGHT（GlaxReality 光学底座）", "model": "P1",
        "sources": "GlobeNewswire 官方通稿 / IFA 现场",
        "remark": "IFA 2026 展位 H5.2-429；众筹时间/定价/市场待公布，规格为官方目标值"
    },
    {
        "region": "cn", "status": "released",
        "title": "联想 YOGA Pro 9n（RTX Spark）",
        "stars": 5, "source": "B", "date": "2026-09-04", "domain": "笔记本",
        "url": "https://www.toutiao.com/article/7681490689716208162",
        "url_label": "今日头条·快科技",
        "signal_type": "首发",
        "confirm_count": "3 个印证源",
        "key_params": "IFA 2026 发布，英伟达 RTX Spark（20 核 Grace CPU + 6144 CUDA Blackwell GPU），128GB 9400MT/s 统一内存，15.3 英寸 2.5K 165Hz OLED，80W TDP / 16.7mm，FP4 算力 1 PFLOPS",
        "tech_features": [
            "RTX Spark 平台：20 核 Grace CPU 与 6144 CUDA 核心 Blackwell RTX GPU 经 NVLink-C2C 融合，FP4 算力 1 PFLOPS",
            "最高 128GB 9400MT/s LPDDR5X 统一内存，CPU/GPU 同时访问，本地运行 1200 亿参数、100 万 token 上下文大模型",
            "联想 X Power 散热，80W TDP 塞进最薄 16.7mm 机身，1.65kg，双 M.2 2242 位（PCIe 4.0+5.0，最高 4TB）",
            "15.3 英寸 2.5K 165Hz PureSight Pro OLED，1100nits HDR，100% P3；920 万像素红外摄像头，Force Pad 触觉反馈触控板"
        ],
        "why_important": "RTX Spark 把 128GB 统一内存+千亿参数本地推理带进了 16.7mm 轻薄本，这不是传统笔电升级，而是端侧 AI 算力的重新定价——平板预研必须回答的问题是：当笔记本能本地跑 120B 模型时，平板的 AI 卖点边界在哪里？短期内平板跟进 N1X 类芯片的功耗与散热仍有难度，但统一内存架构消解 CPU/GPU 数据搬运的思路，对下一代平板 SoC 定制（TCL+玄戒类路线）是明确的风向标。",
        "terminal_relevance": "端侧 AI 算力：128GB 统一内存 / 本地 120B 模型 / 平板 AI 卖点边界重估",
        "vendor": "联想", "model": "YOGA Pro 9n（国内型号 YOGA Pro 15 Spark）",
        "sources": "快科技 / 联想 Innovation World / 腾讯新闻",
        "remark": "海外上市时间待公布，国行时间另行通知"
    },
    {
        "region": "cn", "status": "released",
        "title": "联想 YOGA 9n 二合一",
        "stars": 4, "source": "B", "date": "2026-09-04", "domain": "笔记本",
        "url": "https://www.toutiao.com/article/7681490689716208162",
        "url_label": "今日头条·快科技",
        "signal_type": "首发",
        "confirm_count": "2 个印证源",
        "key_params": "16 英寸 2.8K 120Hz OLED 360 度翻转，RTX Spark 平台，64GB 统一内存，双表面手写，六扬声器可旋转音棒",
        "tech_features": [
            "16 英寸 2.8K 120Hz OLED，360 度翻转五模式，笔记本/平板/帐篷形态切换",
            "同平台 RTX Spark，至高 64GB 统一内存，面向 AIGC 创作",
            "双表面手写：屏幕与触控板均可落笔，第二代手写笔低延迟、倾斜识别、自定义按键",
            "六扬声器杜比全景声，高音单元集成于可旋转音棒，声音始终朝向用户"
        ],
        "why_important": "双表面手写把触控板变成第二块书写面，是对二合一设备书写面积不足的巧妙解法，这套交互可以直接移植到磁吸键盘平板套装上，解决平板键盘中无地方手写批注的老问题。可旋转音棒让扬声器方向跟随形态变化，对平板横竖屏切换时的声场自适应同样是现成答案。联想正把 RTX Spark 统一内存从创作本下探到翻转形态，端侧 AI 在多形态终端的扩散速度比预期快。",
        "terminal_relevance": "二合一形态：双表面手写 / 可旋转声场 / 大内存 AI 下探翻转本",
        "vendor": "联想", "model": "YOGA 9n 2-in-1",
        "sources": "快科技 / 联想官方",
        "remark": "国内上市时间另行通知"
    },
    {
        "region": "cn", "status": "coming",
        "title": "ESR Cyclone 25W 磁吸充电垫（CryoBoost 主动散热）",
        "stars": 4, "source": "A", "date": "2026-09-04", "domain": "无线充",
        "url": "https://www.prnewswire.com/news-releases/esr-launches-next-generation-charging-and-protection-innovations-at-ifa-2026-302869766.html",
        "url_label": "PR Newswire（ESR 官方通稿）",
        "signal_type": "官宣",
        "confirm_count": "3 个印证源",
        "key_params": "IFA Innovation Award 2026 获奖产品，CryoBoost 主动风冷 + Qi2 25W 磁吸，较无主动散热快约 28%（EQS 口径），可调节支架，9 月起上市（欧洲渠道称 10 月底）",
        "tech_features": [
            "CryoBoost 主动散热与 Qi2 25W 磁吸充电结合，以更低温度维持更高充电功率，获 IFA Innovation Award 2026 Honoree",
            "EQS 分发稿口径：散热加持下充电速度最高提升约 28%，充电中主动保护电池健康",
            "紧凑充电垫 + 可调节支架，边充边用；黑/灰/酒红三色",
            "同场发布 Xtend 45W/100W 伸缩线充电器（100W 双伸缩线 + USB-A，笔电手机同充）与 Geo Wallet（Find My 内置，同获 IFA 创新奖）"
        ],
        "why_important": "Qi2 25W 之后散热正式取代线圈成为无线充竞争主战场：绿联押液冷、安克风冷、ESR 把风冷做到充电垫并直接拿奖——主动散热已是高端无线充的入场券而非卖点。对 TCL 有两层参考：一是平板若支持 Qi2 类无线充，背面散热结构要预留与充电模组的热协同；二是无线充 25W 化的温升数据，可直接反推平板自充 120W 级方案的热预算。ESR 以亿色（深圳）品牌身份在海外拿下创新奖，也是国产配件品牌打法样本。",
        "terminal_relevance": "散热工程：主动风冷进无线充 / Qi2 25W 温升治理 / IFA 创新奖背书",
        "vendor": "ESR（亿色）", "model": "Cyclone 25W Magnetic Charging Pad",
        "sources": "PR Newswire 官方通稿 / EQS 分发稿 / IFA 现场",
        "remark": "9 月起上市，欧洲渠道称 10 月底；28% 快充提升为 EQS 分发稿口径"
    },
    {
        "region": "cn", "status": "coming",
        "title": "Sonos Play 便携音箱（Sonos 27 系统）",
        "stars": 3, "source": "B", "date": "2026-09-02", "domain": "智能音箱",
        "url": "https://www.163.com/dy/article/L5QKJSA2051100B9.html",
        "url_label": "网易·雷科技",
        "signal_type": "官宣",
        "confirm_count": "3 个印证源",
        "key_params": "Sonos Play 便携音箱 9 月 9 日中国大陆全渠道开售；Sonos 27 系统开放 MCP 接入任意 AI 助手，自研 27voice 助手同步上线",
        "tech_features": [
            "Sonos Play：蓝牙 + Wi-Fi 双模便携音箱，家中为系统一员、出门随身携带",
            "Sonos Positioning 高频声波互测定位：Play 挪到合适位置即刻变身后置环绕，Portable Surrounds 自适应角色",
            "Sonos 27mcp 抢先体验版 9 月 9 日同步上线，ChatGPT 等外部 AI 可直接操控全屋播放；预告 Custom Agents 自定义智能体",
            "同场四款新品：Beam Ultra 回音壁（7.1.2 杜比全景声，9 驱动，699 美元，9 月 29 日）、Ace Ultra 头戴（449 美元）、Amp Multi 功放（GaN+PFFB，8 通道 4 分区）"
        ],
        "why_important": "Sonos 把音箱系统开放给任意 MCP 协议的 AI 智能体，等于宣布语音助手的终局是可插拔的——这对国内音箱厂商的小爱/小度/天猫精灵封闭助手路线是釜底抽薪式挑战。对 TCL 预研：雷鸟 AI 眼镜+平板+电视的组合完全可以借鉴这套 MCP 开放架构，让第三方 Agent 接入 TCL 系终端，而不是自研一个永远追不上 GPT 的助手。Sonos Positioning 的声场自适应也值得在平板外放配件化时参考。",
        "terminal_relevance": "AI 开放平台：MCP 可插拔助手 / 声波互测定位 / 便携环绕自适应",
        "vendor": "Sonos", "model": "Sonos Play（便携）",
        "sources": "雷科技 / Sonos 官方新闻稿 / Bloomberg",
        "remark": "Beam Ultra/Ace Ultra/Amp Multi 国内销售信息待公布；9 月 9 日起 27mcp 抢先体验"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为 FreeBuds Neo",
        "stars": 3, "source": "B", "date": "2026-09-02", "domain": "AI耳机·耳穿戴",
        "url": "https://www.toutiao.com/article/7680951732583449129",
        "url_label": "今日头条·CNMO科技",
        "signal_type": "发布",
        "confirm_count": "4 个印证源",
        "key_params": "9 月 2 日全球发布，首发 109 欧元（英国 119.99 英镑，9 月 23 日开售），单耳 4.8g，30dB 全频段自适应降噪，降噪开启 6.5h/整机 40h",
        "tech_features": [
            "第三代自研音频芯片 + 双通道降噪架构，每秒采集 40 万次环境噪音，噪声处理延迟 8 微秒，全频段平均降噪 30dB",
            "三麦 + 骨传导麦克风通话方案，95dB 嘈杂环境、9m/s 大风下通话清晰",
            "11mm 四磁体动圈，频响 20Hz-40kHz，LDAC 990kbps，华为生态内无损传输 2.3Mbps，360 度头部追踪空间音频跨安卓/iOS/Windows",
            "单耳 4.8g + 盒 31.4g，关降噪单耳 10h、整机 40h；支持华为手表端 HUAWEI Audio Connect 控降噪/音效/电量"
        ],
        "why_important": "8 微秒噪声处理延迟+每秒 40 万次采样是端侧实时音频处理的新标杆，说明华为把自研音频芯片的边缘算力又推高了一档。跨生态空间音频（不锁定华为设备）+手表端控制耳机的组合，勾勒出多设备协同音频的标准化方向——TCL 平板+电视+雷鸟眼镜的音频接力场景可以直接对照落地。华为在中端价位（约 849 元）塞入旗舰降噪芯片，也给竞品平板配套耳机定价施压。",
        "terminal_relevance": "端侧音频芯片：8 微秒降噪延迟 / 跨生态空间音频 / 手表-耳机协同",
        "vendor": "华为", "model": "FreeBuds Neo",
        "sources": "CNMO / 快科技 / 华为官方 / 中电网",
        "remark": "四种配色，9 月 23 日英国率先开售"
    },
    {
        "region": "cn", "status": "coming",
        "title": "华为 FreeBuds 7 悦彰",
        "stars": 3, "source": "B", "date": "2026-09-07", "domain": "AI耳机·耳穿戴",
        "url": "https://www.163.com/dy/article/L6539ONA0512ER4R.html",
        "url_label": "网易·搞机小帝",
        "signal_type": "发布会",
        "confirm_count": "2 个印证源",
        "key_params": "9 月 7 日华为全场景新品发布会登场，半入耳形态主动降噪新突破，主打机舱/地铁等高噪音场景，经典短直杆设计 + 半椭圆胶囊充电盒，价格待公布（预计 899-1099 元档）",
        "tech_features": [
            "半入耳形态主动降噪新突破：在保留半入耳舒适度的同时真正提升主动降噪效果",
            "官方定位：机舱、地铁等高噪音场景下压住环境噪音，半入耳被动隔音差的短板被针对性补齐",
            "回归经典短直杆设计，充电盒改为半椭圆胶囊形态，8 月底已官宣并开启预售入口",
            "与 Mate XT2/MatePad Air 2026/WATCH 6 Pro 陶瓷白同场发布，HarmonyOS 7 生态联动"
        ],
        "why_important": "半入耳降噪是耳机行业公认的两难：舒适与隔音天然互斥，华为把「高噪音场景的半入耳降噪」作为发布会核心叙事，说明其自研音频芯片的算力余量已能补偿被动隔音缺口。对 TCL 的参考在生态协同：FreeBuds 7 悦彰与平板/手表同场发布，多设备音频接续正成为旗舰标配——TCL 平板+电视+耳机的音频流转若要在体验上不落败，跨端无缝切换时延需要进入预研指标。价格未公布前，具体规格以发布会官方口径为准。",
        "terminal_relevance": "半入耳主动降噪 / 高噪音场景补偿 / 鸿蒙生态音频接续",
        "vendor": "华为", "model": "FreeBuds 7 悦彰",
        "sources": "网易 / 腾讯新闻（发布会前瞻）",
        "remark": "9 月 7 日发布会当日价格与详细规格待官宣，899-1099 元为媒体预估档位"
    },
    # ========== 国际 15 条 ==========
    {
        "region": "intl", "status": "coming",
        "title": "Acer Iconia X16 / Iconia X14（OLED 大屏平板）",
        "stars": 4, "source": "B", "date": "2026-09-02", "domain": "平板",
        "url": "https://www.androidheadlines.com/2026/09/acer-unveils-four-new-android-tablets-at-ifa-2026-coming-in-q4.html",
        "url_label": "Android Headlines",
        "signal_type": "Announced",
        "confirm_count": "2 个印证源",
        "key_params": "16/14 英寸 1920×1200 OLED 400nits，Helio G80+6GB，8000mAh，双 USB-C（一个专用于视频输入），2026 Q4 北美与 EMEA 上市",
        "tech_features": [
            "Iconia X16 配 16 英寸 OLED，1920×1200 分辨率、400nits、DCI-P3 95% 色域，X14 亮度同级但 DCI-P3 达 100%",
            "双 USB-C 设计：其一专用于视频输入，平板可秒变外接便携显示器，另一口负责充电与数据",
            "四款机型平台完全一致：联发科 Helio G80 + 6GB LPDDR4X + 8000mAh 电池，全系 60Hz",
            "预装 Android 16，支持可拆卸键盘与触控笔，X 系哑光黑，Q4 2026 登陆北美与 EMEA"
        ],
        "why_important": "16 英寸 OLED 下探到 Helio G80 入门平台，说明大尺寸 OLED 面板成本已被压到入门价位段——这对 TCL 平板在 14-16 英寸档的屏幕选型与 BOM 定价是直接的压力测试。第二 USB-C 做视频输入等于白送便携显示器功能，是低成本高感知的差异化，值得 TCL 评估跟进。其全系 60Hz 恰恰暴露低价本质，TCL 可用高刷加护眼方案形成区隔。",
        "terminal_relevance": "大屏平板 / OLED 成本下探 / 接口差异化",
        "vendor": "Acer", "model": "Iconia X16 / Iconia X14",
        "sources": "Android Headlines / Notebookcheck",
        "remark": "IFA 2026 发布，价格未公布；与同场 Iconia A16/A14 为同一公告高低两档"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Acer Iconia A16 / Iconia A14（IPS 入门平板）",
        "stars": 3, "source": "B", "date": "2026-09-02", "domain": "平板",
        "url": "https://www.androidheadlines.com/2026/09/acer-unveils-four-new-android-tablets-at-ifa-2026-coming-in-q4.html",
        "url_label": "Android Headlines",
        "signal_type": "Announced",
        "confirm_count": "2 个印证源",
        "key_params": "16/14 英寸 1920×1200 IPS，Helio G80+6GB，8000mAh，双 USB-C 视频输入，预计 250 美元内，Q4 北美与 EMEA",
        "tech_features": [
            "与 X 系同规格 1920×1200 面板但改为 IPS，分辨率一致、无 OLED，60Hz",
            "同样保留双 USB-C 之一专用视频输入，入门档也提供便携显示器能力",
            "Helio G80 + 6GB LPDDR4X + 8000mAh，Acer 现款 Iconia A13 仅 200 美元，A 系大概率低于 250 美元",
            "预装 Android 16，Vapor Silver 单配色，Q4 2026 上市北美与 EMEA"
        ],
        "why_important": "A 系把视频输入便携显示器功能下放到 200-250 美元档，这个价位段正是 TCL TAB 入门海外主战场，直接冲击海外渠道价格锚点。存储涨价周期里 Acer 仍敢用大屏走量，说明其面板与平台 BOM 已锁到极低水平，TCL 入门线需要在护眼（NXTPAPER）、插卡与配件生态上找回差异化，而不是拼分辨率。",
        "terminal_relevance": "入门平板 / 价格锚点 / 便携显示器",
        "vendor": "Acer", "model": "Iconia A16 / Iconia A14",
        "sources": "Android Headlines / Notebookcheck",
        "remark": "与 X16/X14 同一 IFA 公告，因显示技术、价位与定位不同而独立成卡"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Oukitel RT10 工业三防平板",
        "stars": 3, "source": "C", "date": "2026-09-02", "domain": "平板",
        "url": "https://realhacker.news/oukitel-has-a-rugged-industrial-tablet-a-laptop-with-a-solar-panel-and-home-solar-batteries",
        "url_label": "Real Hacker News（源 GSMArena）",
        "signal_type": "Announced",
        "confirm_count": "3 个印证源",
        "key_params": "11 英寸 1080p 120Hz，天玑 7400X+12GB+512GB，25000mAh，IP68/IP69K/MIL-STD-810H，-45 至 75 摄氏度工作认证",
        "tech_features": [
            "11 英寸 1080p 120Hz 屏，天玑 7400X + 12GB + 512GB 可扩展，25000mAh 大电池",
            "工业版带 2D 条码扫描器与指纹模块，pogo pin 触点充电，配 USB-A、RJ45 网口与 RS-232 串口",
            "IP68、IP69K、MIL-STD-810H 三重认证，-45 至 75 摄氏度环境工作认证",
            "64MP 主摄 + 20MP 夜视摄像头，双 5W 扬声器音量超 130dB"
        ],
        "why_important": "工业三防平板（RS-232、RJ45、扫码、宽温）是欧洲户外与行业客户的刚需细分，利润率好于消费档。TCL 平板若拓展 B2B 行业版本，RT10 的接口组合与宽温认证清单就是现成的需求规格书；25000mAh 巨电池思路对户外版平板的续航定位也有直接借鉴。消费版会砍掉串口与扫码，说明该品牌在做软硬分档而非单一 SKU。",
        "terminal_relevance": "行业三防平板 / 宽温与串口 / 巨电池",
        "vendor": "Oukitel", "model": "RT10",
        "sources": "GSMArena / Real Hacker News / Notebookcheck",
        "remark": "IFA 2026 亮相；另有民用精简版，价格与开售时间未公布"
    },
    {
        "region": "intl", "status": "coming",
        "title": "DOOGEE U14 VIP Edition（14 英寸巨屏平板）",
        "stars": 3, "source": "A", "date": "2026-09-04", "domain": "平板",
        "url": "https://uk.doogee.com/products/doogee-u14-large-screen-tablet",
        "url_label": "DOOGEE 官方商城（英国）",
        "signal_type": "Announced",
        "confirm_count": "2 个印证源",
        "key_params": "14 英寸 2.2K 90Hz IPS，RK3576S 8nm，14000mAh 33W，Android 16+Gemini AI，858g/8.5mm，官网 369 美元",
        "tech_features": [
            "14 英寸 IPS In-Cell 面板，2240×1400 分辨率、90Hz、86% 屏占比",
            "RK3576S 八核 8nm 至 2.1GHz，8GB LPDDR4X 可扩展至 48GB，256GB UFS 支持 2TB TF 卡",
            "14000mAh 电池配 33W 快充，六扬声器环绕声，Widevine L1 与 Wi-Fi 6，保留 3.5mm 耳机孔",
            "323.4×211.3×8.5mm 金属机身重 858g，16MP+8MP 摄像头，预装 Android 16 并前置 Gemini AI 卖点"
        ],
        "why_important": "14 英寸巨屏加 14000mAh 塞进 8.5mm 与 858g，官网价仅 369 美元，把大屏大电池的价格锚点进一步砸穿，TCL TAB 海外中低端定价必须对此对标。更值得注意的是 Gemini AI 被写进官方头版卖点——端侧 AI 助手已从旗舰话术变成入门平板标配，TCL 出海机型的 AI 叙事需要提前布局而非跟随。VIP 版捆绑键鼠笔全套配件也是欧洲渠道打法参考。",
        "terminal_relevance": "巨屏入门平板 / 价格锚 / 端侧 AI 话术",
        "vendor": "DOOGEE", "model": "U14 VIP Edition",
        "sources": "DOOGEE 官网（IFA 2026） / DOOGEE 英国官方商城",
        "remark": "IFA 2026 Hall 4.2 展出；罗马尼亚渠道已开启 345-422 欧元预售"
    },
    {
        "region": "intl", "status": "released",
        "title": "vivo V80 Lite 5G（马来西亚版，10000mAh 硅碳电池）",
        "stars": 4, "source": "B", "date": "2026-09-04", "domain": "手机",
        "url": "https://soyacincau.com/2026/09/04/vivo-v80-lite-5g-malaysia-mid-ranger-with-massive-10000mah-battery-promo-priced-from-rm1399/",
        "url_label": "SoyaCincau",
        "signal_type": "Release",
        "confirm_count": "4 个印证源",
        "key_params": "6.83 英寸 1.5K AMOLED 120Hz 2000nits，天玑 7300e，10000mAh 第四代硅碳负极 BlueVolt，44W 快充，IP68/IP69，RM1,399 起（约 331 美元）",
        "tech_features": [
            "10000mAh BlueVolt 电池采用第四代硅碳负极，官方称 1400 次充电循环后容量保持不低于 80%",
            "44W FlashCharge 有线快充且标配 44W 充电器，支持 USB-C 反向充电与 1% 电量低功耗应急模式",
            "6.83 英寸 2800×1260 120Hz AMOLED，HBM 峰值 2000nits、1.35mm 边框，Q10+ 发光材料",
            "IP68+IP69+IP6X 三重防护并通过 MIL-STD-810H，机身 8.59mm/224g，3.8K 超大面积 VC 均热板"
        ],
        "why_important": "10000mAh 硅碳电池首次以 330 美元级价位出海（马来西亚 9 月 3 日发布、9 月 12 日首销），证明第四代硅负极电芯的 BOM 成本已能进入中端——这是给 TCL 大屏平板的强信号：同级硅碳方案完全可把平板容量推到 12000-15000mAh 而不牺牲厚度。其 44W 的保守快充与 3.8K VC 散热组合也暴露了硅碳高倍率发热的短板，预研侧的热管理设计需提前对齐。",
        "terminal_relevance": "硅碳负极 / 大电池中端化 / 快充热管理",
        "vendor": "vivo", "model": "V80 Lite 5G",
        "sources": "SoyaCincau / TechTimes / vivo 马来西亚官网",
        "remark": "与 08-16 报道的 V80 系传闻为不同 SKU（骁龙 7 Gen4 旗舰线 vs 天玑 7300e 中端线）；吉尼斯最长电子产品测试直播 32 小时 37 分为其背书"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Tecno Bezelless Concept Phone（无边框概念机）",
        "stars": 2, "source": "B", "date": "2026-09-04", "domain": "手机",
        "url": "https://www.techadvisor.com/article/3227215/best-of-ifa-2026-awards.html",
        "url_label": "Tech Advisor（IFA 2026 获奖榜）",
        "signal_type": "Announced",
        "confirm_count": "2 个印证源",
        "key_params": "6.78 英寸 144Hz OLED 概念机，边框隐藏于显示层下，肉眼近乎无边框，保留打孔前摄",
        "tech_features": [
            "6.78 英寸 144Hz OLED 面板，边框被藏进显示层下方而非真正消除",
            "仍有极窄区域不响应触控输入，中框刻意加宽以便握持",
            "保留单打孔前摄，为整机唯一可见开孔",
            "概念展示，无量产计划与价格信息"
        ],
        "why_important": "屏占比竞赛从做窄边框转向藏边框，本质是显示堆叠与边缘走线工艺的再设计，若成熟大概率先落地中端机型。对 TCL 的价值在显示侧预研观察：这类方案若被证明可靠，可反哺手机与平板的 ID 语言；但当前无量产时间表，不具备 BOM 参考价值，关注即可。",
        "terminal_relevance": "显示工艺 / 无边框形态 / 概念预研",
        "vendor": "Tecno（传音）", "model": "Bezelless Concept",
        "sources": "Tech Advisor",
        "remark": "Tech Advisor IFA 2026 获奖榜收录；Tecno 同场还展示了 Camon 影像与 AI 生态"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Circular Ring 3 Slim / Ring 3 Pro（智能指环）",
        "stars": 2, "source": "B", "date": "2026-09-04", "domain": "智能手表",
        "url": "https://www.techadvisor.com/article/3227175/circular-ring-3-slim-pro-get-nfc-payments-vibration-alerts-blood-pressure.html",
        "url_label": "Tech Advisor",
        "signal_type": "Announced",
        "confirm_count": "3 个印证源",
        "key_params": "钛金属指环，NFC 支付+振动马达，Pro 加血压趋势与 12 天续航，Slim 宽 5.9mm 厚 2.35mm，50m 防水，预计 2027 年初上市",
        "tech_features": [
            "NFC 非接触支付直接上指环，支持 Mastercard 与 Visa，竞品 Oura Ring 5 尚无此功能",
            "内置振动马达，用于静音闹钟、用药提醒、健康警报与呼吸引导等触觉通知",
            "Ring 3 Pro 宽 6.8mm，增加血压趋势追踪，续航达 12 天；Slim 宽 5.9mm 厚 2.35mm",
            "钛金属机身、50m 防水，金/玫瑰金/银/黑四色，美码 6-14 尺码"
        ],
        "why_important": "指环品类开始补齐支付与触觉反馈两块原本属于手表的功能拼图，正在从健康记录器走向可替代表。对 TCL 穿戴预研的判断是：无屏穿戴的价值点正从传感堆料转向交互能力，NFC 加振动是成本最低的组合。若 TCL 平板未来做穿戴联动，指环形态反而是比手表更轻的生态入口，值得小规模预研立项。",
        "terminal_relevance": "智能指环 / NFC 支付 / 触觉交互",
        "vendor": "Circular", "model": "Ring 3 Slim / Ring 3 Pro",
        "sources": "Tech Advisor / iFitness Mag",
        "remark": "指环形态归入智能手表口径统计；价格与上市日期未定，预计 2027 年初"
    },
    {
        "region": "intl", "status": "released",
        "title": "Luna Band（无屏健康带，全球发售）",
        "stars": 2, "source": "B", "date": "2026-09-04", "domain": "智能手表",
        "url": "https://www.techadvisor.com/article/3226383/luna-band-get-global-release-date-shipping-now.html",
        "url_label": "Tech Advisor",
        "signal_type": "Release",
        "confirm_count": "3 个印证源",
        "key_params": "无屏健康带，129 英镑/149 美元/149 欧元，无订阅，LifeOS 支持用户自制 Micro Apps，9 月 4 日起全球发货",
        "tech_features": [
            "无屏设计，靠 LifeOS 按用户日程建议运动、进食与咖啡因摄入时机，走调度式健康管理路线",
            "售价 129 英镑/149 美元/149 欧元，核心卖点为无月费订阅，直接对标 Fitbit Air 与 Garmin CIRQA",
            "LifeOS 开放用户创建 Micro Apps 自行扩展设备功能，复制 Garmin IQ 商店的社区路线",
            "三色可选，宣布半年后即从邀请制 waitlist 转入全球现货发货"
        ],
        "why_important": "无屏穿戴赛道（Whoop、CIRQA、Luna）已被卷到 149 美元价位且集体去订阅化，说明纯传感加算法的硬件 BOM 已极低，价值全在软件生态。对 TCL 的启示：平板与穿戴联动若立项，屏幕不是必需件、生态绑定才是护城河；这类腕带作为平板套装赠品或配件的边际成本很低，可纳入配件生态评估。",
        "terminal_relevance": "无屏穿戴 / 去订阅化 / 平板配件生态",
        "vendor": "Luna", "model": "Luna Band",
        "sources": "Tech Advisor / iFitness Mag / lunazone.com",
        "remark": "无屏手环形态，归入智能手表口径统计；Garmin CIRQA 为同类竞品、非同产品"
    },
    {
        "region": "intl", "status": "progress",
        "title": "BleeqUp Ranger（4 合 1 运动摄像眼镜）",
        "stars": 3, "source": "C", "date": "2026-09-04", "domain": "AR-VR眼镜",
        "url": "https://www.smartwearables.io/news/ifa-2026-day-1-wearable-highlights-beyerdynamic-rayneo-xiaomi-ulefone-september-4",
        "url_label": "Smart Wearables",
        "signal_type": "Announced",
        "confirm_count": "3 个印证源",
        "key_params": "37g，16MP 摄像头 120 度 FOV 3K60 EIS，骁龙 W5，260mAh+1600mAh PowerPlus 外挂电池，5 麦克风 4 扬声器，IP54，可选 ZEISS 镜片",
        "tech_features": [
            "16MP 摄像头 120 度第一人称视角，支持 3K 60fps 电子防抖录制与 AI 自动高光剪辑",
            "眼镜本体 260mAh 续航 1 小时视频，外挂 1600mAh PowerPlus 挂包后连续录制可达 5 小时",
            "5 麦克风阵列加 4 扬声器开放音频，40km/h 风速下降噪通话，内置实时群组对讲",
            "高通骁龙 W5 平台、32GB 存储，TR90 框架 37g、IP54 防护，UV400 基础镜片可升级 ZEISS"
        ],
        "why_important": "摄像、音频、对讲、运动数据四合一且已量产，证明无显示智能眼镜的量产路径靠场景聚合而非堆显示。37g 整机重量与 260mAh 本体加可换外挂电池的供电架构，对雷鸟系眼镜的 ID 与电池设计有直接参考价值；运动垂类是避开 Meta 正面战场的差异化打法，TCL 平板的骑行/户外用户群可与之做场景联动。",
        "terminal_relevance": "运动眼镜 / 第一人称摄像 / 轻量化供电",
        "vendor": "BleeqUp（致敬未知）", "model": "Ranger",
        "sources": "Smart Wearables / BleeqUp 官网 / TechTimes",
        "remark": "无显示形态；本次 IFA 为 IFA Next 展区展示，产品此前已在新加坡等市场发售（559 新币档）"
    },
    {
        "region": "intl", "status": "released",
        "title": "HTC VIVE Eagle 圆框版（手机线退场转型 AI/XR）",
        "stars": 4, "source": "B", "date": "2026-09-06", "domain": "AR-VR眼镜",
        "url": "https://www.toutiao.com/article/7682459329764573696/",
        "url_label": "今日头条·93913产业周报",
        "signal_type": "发布",
        "confirm_count": "2 个印证源",
        "key_params": "正式发布圆形镜框版本 VIVE Eagle AI 智能眼镜，同步登陆北美/欧洲/澳大利亚；HTC 确认智能手机产品线 2026 年底结束生命周期，全面转型 AI 硬件与 XR",
        "tech_features": [
            "圆形镜框版本 VIVE Eagle AI 智能眼镜正式发布，同步登陆北美、欧洲、澳大利亚三大市场",
            "以「无边框」设计、轻量化形态及简化连接为核心卖点，向普通光学眼镜的日常体验靠拢",
            "HTC 高级副总裁黄朝英同日确认：现有智能手机产品线 2026 年底逐步结束生命周期，下一代智能手机暂无规划",
            "曾经的安卓手机巨头将企业核心运营重心从智能手机全面切换至 AI 硬件与扩展现实（XR）领域"
        ],
        "why_important": "这是本周最重的战略级信号：曾经定义安卓肾上腺素的 HTC 直接砍掉手机生命线，把全部筹码押到 AI 眼镜与 XR——手机巨头的退场路线图正在被眼镜厂商改写。对 TCL 的含义有两层：一是 AI 眼赛道的玩家在快速扩容与洗牌（手机厂商转身为竞争者），雷鸟所在赛道的中期竞争烈度会上一个台阶；二是「手机厂→AI 硬件」的转型样本说明，无屏/轻屏穿戴是手机能力最顺的迁移出口，TCL 平板+眼镜的组合应加快卡位。圆框版改型也提示：AI 眼镜的 ID 时尚化正在加速。",
        "terminal_relevance": "战略信号：手机巨头退场转 AI/XR / 眼镜三市场同步发售 / ID 时尚化",
        "vendor": "HTC", "model": "VIVE Eagle（圆形镜框版）",
        "sources": "93913 产业周报 / HTC 官方",
        "remark": "周报覆盖 8 月 31 日-9 月 6 日产业动态；手机退场时间表为 HTC 高管媒体采访口径"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Lenovo ThinkBook 14 Gen 9 Q8Y（骁龙 X2 Plus 商务本）",
        "stars": 3, "source": "B", "date": "2026-09-04", "domain": "笔记本",
        "url": "https://finance.sina.com.cn/tech/digi/2026-09-04/doc-iniqryew6150542.shtml",
        "url_label": "新浪科技（源 IT之家）",
        "signal_type": "Announced",
        "confirm_count": "2 个印证源",
        "key_params": "骁龙 X2 Plus 25W TDP，1920×1200 60Hz 400nits，17.39mm/1.3kg，50Whr，1099 欧元起 10 月欧洲开售",
        "tech_features": [
            "高通骁龙 X2 Plus 平台，25W TDP，为该新平台首次下探到 1099 欧元主流商用价位",
            "32GB LPDDR5X 内存，双 M.2 盘位预装至多 1TB 存储",
            "1920×1200 60Hz 400nits 屏可选触控，17.39mm 厚、起始 1.3kg、50Whr 电池",
            "Wi-Fi 7 320MHz 频宽；2 个 USB-C 10Gbps、USB-A、HDMI 2.1、SD 读卡器，FHD IR 摄像头"
        ],
        "why_important": "骁龙 X2 Plus 首次进入千元欧元级主流商务本，标志 ARM Windows 笔电从旗舰向主力价位铺货，X86 之外的第三极平台成本曲线值得 TCL 长期跟踪。其低色域 60Hz 屏明显是为控价妥协，说明高通版整机仍在贴线定价——TCL 若规划平板-PC 融合形态或海外商用本，可等 X2 Plus 机型价格企稳后评估性价比窗口。",
        "terminal_relevance": "ARM 笔电 / 平台成本曲线 / 商用形态",
        "vendor": "Lenovo", "model": "ThinkBook 14 Gen 9 Q8Y",
        "sources": "IT之家（新浪转载）",
        "remark": "与去重表内 ThinkBook Plus G7 Auto Twist 为不同产品线（数字商务本系列 vs Plus 双屏扭转系列）"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Oukitel RG14-P（太阳能三防笔电）",
        "stars": 3, "source": "C", "date": "2026-09-03", "domain": "笔记本",
        "url": "https://techno.express/oukitels-new-rugged-laptop-charges-via-sunlight-and-survives-water-jets.html",
        "url_label": "techno.express（源 Notebookcheck）",
        "signal_type": "Announced",
        "confirm_count": "3 个印证源",
        "key_params": "14.1 英寸 1000nits 触控，14 代酷睿 i7，95Wh 双电池可热插拔，10-15W 太阳能背板，3.7kg，IP69K",
        "tech_features": [
            "14.1 英寸阳光可读触控屏，亮度 1000nits，配 180 度旋转磁吸摄像头",
            "14 代 Intel Core i7 + 16GB + 512GB SSD，带 RS-232 串口、RJ45、多 HDMI、NFC 与指纹",
            "95Wh 电池拆分为 3000mAh 内置段与 5200mAh 可热插拔段，可备多块电池无限续航",
            "屏幕背板集成太阳能板，官方称 10-15W 输入、6 小时充至 50%；整机 IP68/IP69K 重 3.7kg"
        ],
        "why_important": "太阳能背板加热插拔电池把离网续航做成了笔电的硬差异化，指向户外与工业场景而非通用市场，3.7kg 也说明它与便携绝缘。对 TCL 的真正参考在于：能源自治形态能不能反哺三防平板产品线——欧洲之外电力不稳市场对太阳能补电的终端确有需求，若 TCL 平板行业版考虑太阳能充电盖，RG14-P 是第一个量产先例。",
        "terminal_relevance": "三防笔电 / 太阳能补电 / 可换电池",
        "vendor": "Oukitel", "model": "RG14-P",
        "sources": "techno.express / Notebookcheck / Real Hacker News",
        "remark": "IFA 2026 发布；另有去太阳能改 LED 照明的 RG14-L 变体；价格与开售时间未公布"
    },
    {
        "region": "intl", "status": "released",
        "title": "Belkin UltraCharge Pro（BoostSolid Cell 半固态移动电源）",
        "stars": 4, "source": "B", "date": "2026-09-04", "domain": "无线充",
        "url": "https://new.qq.com/rain/a/20260904A080GJ00",
        "url_label": "腾讯新闻（美国商业资讯通稿）",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "IFA 2026 首发，BoostSolid Cell 半固态电池（液态电解质旁加凝胶层），寿命最高 3 倍，5K 版 8.8mm/15W Qi2/69.99 美元，10K 版 60W/89.99 美元，9 月起全球开售",
        "tech_features": [
            "BoostSolid Cell 半固态架构：在液态电解质旁增加凝胶状物质，设计寿命为普通移动电源最高 3 倍（1000 次循环后容量约 80%）",
            "安全设计：双模拟+数字温度传感器每 250 毫秒监测电池，越限自动断电；0-40°C 宽温稳定输出；满足 UL2056:2025 与 TSA 随身行李要求",
            "UltraCharge Pro 5K（BPD024）：厚仅 8.8mm（同级薄 40%）、5000mAh、Qi2 认证 15W 磁吸无线 + 22.5W USB-C 有线，69.99 美元",
            "UltraCharge Pro 10K（BPB044）：10000mAh、60W USB-C（iPhone 17 Pro 约 24 分钟充至 50%）、双 USB-C+USB-A、智能屏显，89.99 美元"
        ],
        "why_important": "半固态电池从 Kuxiu/BMX/Zens 的小众玩法升级为 Belkin 这种一线配件大牌的主流货架产品，且直接打进磁吸超薄形态——便携储能的电化学升级周期已经启动，2-3 年内会下探到中端价位。对 TCL 的参考有二：一是平板包装内随附充电宝这类配件的电池选型，半固态的寿命与安全叙事值得跟进；二是无线充磁吸生态（Qi2 15W/25W）与平板背面结构件的兼容设计要提前布局。",
        "terminal_relevance": "半固态电池 / 便携储能升级 / 磁吸 Qi2 配件",
        "vendor": "Belkin", "model": "UltraCharge Pro with BoostSolid Cell（BPD024/BPB044）",
        "sources": "美国商业资讯（腾讯转载）/ Tech Advisor / The Next Web",
        "remark": "与去重表 08-24「Belkin Qi2.2 三合一磁吸充电站」为不同产品（充电站 vs 半固态移动电源）；黑色/沙色两色"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Sonos S59（代号 Gambit，Beam 2 继任 soundbar）",
        "stars": 2, "source": "B", "date": "2026-08-19", "domain": "智能音箱",
        "url": "https://www.notebookcheck.net/Sonos-reportedly-preparing-new-soundbar-for-September-launch.1372755.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "Certification",
        "confirm_count": "3 个印证源",
        "key_params": "FCC 型号 S59、代号 Gambit，Beam 2 继任紧凑 soundbar，三频 Wi-Fi 6E+蓝牙 2×2 MIMO，9 月与 Ace Ultra 同场发布，细节保密至 2027 年 1 月",
        "tech_features": [
            "FCC 文件显示型号 S59、内部代号 Gambit，定位无线智能音箱，尺寸接近 25.6 英寸宽的 Beam 2",
            "支持 2.4/5/6GHz 三频 Wi-Fi 与蓝牙，2×2 MIMO，连接层较 2021 年的 Beam 2 大幅升级",
            "驱动单元、杜比全景声实现与 HDMI 接口等音频细节尚未披露",
            "内部与外部照片等 FCC 文件保密期至 2027 年 1 月；Bloomberg 称 9 月正式发布"
        ],
        "why_important": "三频 Wi-Fi 6E 级连接下放到紧凑型 soundbar，说明音箱正在为多房间低延迟与高码率串流重构连接层；Beam 2 五年才迭代一次，也反映头部品牌产品周期显著拉长。对 TCL 音箱品类的直接参考有限，但 Sonos 把新 soundbar 与 Ace Ultra 耳机、TV Audio Swap 互传捆绑成影院生态的打法，值得 TCL 平板+音箱+耳机的组合营销借鉴。",
        "terminal_relevance": "soundbar / Wi-Fi 6E / 生态联动",
        "vendor": "Sonos", "model": "S59（Gambit）",
        "sources": "Notebookcheck（源 US FCC、Bloomberg） / ecoustics",
        "remark": "去重表内 Sonos Roam 2 为便携音箱、Sonos Play 为国内条线产品，均非同产品"
    },
    {
        "region": "intl", "status": "coming",
        "title": "Sonos Ace Ultra（ANC 头戴耳机）",
        "stars": 3, "source": "D", "date": "2026-08-14", "domain": "AI耳机·耳穿戴",
        "url": "https://www.notebookcheck.net/Sonos-Ace-Ultra-price-specs-and-release-date-leaked.1368561.0.html",
        "url_label": "Notebookcheck（源 billbil-kun）",
        "signal_type": "Leak",
        "confirm_count": "3 个印证源",
        "key_params": "449 美元/449 欧元/399 英镑，ANC 效果号称一代 2 倍，ANC 开启 35 小时续航，3 分钟快充约 3 小时播放，黑/白/Agave 三色，9 月 1 日官宣 9 月 29 日发售",
        "tech_features": [
            "主动降噪效果号称较一代提升至 2 倍，重点针对空调与飞机引擎类低频噪声",
            "ANC 开启续航 35 小时，比一代多约 5 小时",
            "3 分钟快充可获得约 3 小时播放，充电效率为主要升级点之一",
            "改用触控按键替代实体键；黑、白、Agave 蓝绿三色；与杜比全景声 soundbar 生态联动增强"
        ],
        "why_important": "449 欧元定价反而低于一代的 499 欧元，头部 ANC 耳机开始用降价硬刚索尼 XM6 与 Bose，旗舰 ANC 价格带正在下移、中端产品空间被挤压。Tech Advisor IFA 现场确认三色与 35h 续航后该爆料可信度很高。对 TCL 耳机品类的判断：海外 ANC 机型定价窗口在收窄，与其跟随旗舰参数，不如把预算押在续航快充与生态互通上。",
        "terminal_relevance": "ANC 耳机 / 价格带下移 / 快充续航",
        "vendor": "Sonos", "model": "Ace Ultra",
        "sources": "Notebookcheck（billbil-kun 爆料） / Tech Advisor IFA 实测",
        "remark": "9 月 29 日正式发售；去重表内无 Sonos Ace 条目，非重复"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 7, True),
    ("显示/OLED", 14, True),
    ("折叠屏", 0, True),
    ("手写笔/触控", 1, True),
    ("散热/液冷", 3, True),
    ("电池/续航", 18, True),
    ("快充/无线充", 6, True),
    ("影像", 4, True),
    ("AI/NPU", 12, True),
    ("音频/扬声器", 10, True),
    ("5G/通信", 2, True),
    ("Wi-Fi/连接", 5, True),
    ("AR/VR显示", 3, True),
    ("材质/工艺", 9, True),
    ("可持续/模块化", 1, True),
    ("手柄/外设", 3, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {"rank": 1, "title": "联想 Yoga Tab Plus Gen 2", "dim": "平板电脑", "stars": 5, "key": "B级 / 13\" 4K 144Hz 1100nits / 12700mAh+68W / 849 欧元起 / 7 年系统更新"},
    {"rank": 2, "title": "联想 YOGA Pro 9n（RTX Spark）", "dim": "笔记本电脑", "stars": 5, "key": "B级 / 128GB 统一内存 / 本地 120B 模型 / 80W 塞进 16.7mm"},
    {"rank": 3, "title": "努比亚 NaviX Ultra（AI 智能体手机）", "dim": "手机", "stars": 4, "key": "B级 / MCP 端侧智能体范式 / 7100mAh / 工信部入网"},
    {"rank": 4, "title": "vivo V80 Lite 5G（马来西亚版）", "dim": "手机", "stars": 4, "key": "B级 / 10000mAh 第四代硅碳下探 331 美元 / 1400 循环 80%"},
    {"rank": 5, "title": "荣耀 MagicPad 4（国行预约）", "dim": "平板电脑", "stars": 4, "key": "B级 / 12.3\" 3K OLED 2400nits 165Hz / 骁龙 8 Gen 5 / 4.8mm（IT之家口径）"},
]
'''

src = open(TEMPLATE, encoding="utf-8").read()

# ① 只替换模板部分（此时尚未拼接 CHUNK），避免污染 CHUNK 内的卡片日期
src = src.replace("2026-08-26", "2026-09-07")
src = src.replace('WEEK = "周三"', 'WEEK = "周一"')
# 副标题补全：标注 8 类却只枚举 7 项的模板缺陷，补上 AI耳机·耳穿戴
src = src.replace(
    "采集口径：7类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑）",
    "采集口径：8类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑/AI耳机·耳穿戴）"
)
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
