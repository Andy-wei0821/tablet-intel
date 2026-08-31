#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 WB_2026-08-31_硬件看板.html
做法：读取 gen_wb_2026-08-26.py 模板，先替换模板内 日期/周几/类别数(7→8)，
     再注入 CARDS/DIMS/TOP5，exec 生成。
     注意：先替换 src 再拼接 CHUNK，避免全局 replace 污染 CHUNK 内的卡片日期。
"""
import os

TEMPLATE = r"E:\AI相关\预研究\202608\03_输出\gen_wb_2026-08-26.py"

CHUNK = r'''CARDS = [
    # ========== 国内 15 条 ==========
    {
        "region": "cn", "status": "released",
        "title": "联想 ThinkTab 11S 平板",
        "stars": 4, "source": "B", "date": "2026-08-31", "domain": "平板",
        "url": "https://www.163.com/dy/article/L5L4U0SE0511B8LM.html",
        "url_label": "IT之家",
        "signal_type": "开售",
        "confirm_count": "2 个印证源",
        "key_params": "11 英寸 2.5K LCD 90Hz 屏（2560×1600 / 276 PPI / 500nits）+ 天玑 6300 + 8GB+128GB + 7040mAh，一体式金属机身 7mm/485g，首发价 1799 元",
        "tech_features": [
            "11 英寸 2560×1600 LCD 屏，276 PPI、90Hz 刷新率、500nits 亮度，前置 800 万 + 后置 1300 万像素摄像头",
            "联发科天玑 6300 处理器，8GB LPDDR4X + 128GB UFS 2.2，内置 7040mAh 电池并支持 PD 3.0（随机附赠 20W 充电适配器）",
            "一体式金属背壳，厚约 7mm、重约 485g，配备 4 扬声器系统并支持杜比全景声",
            "搭载基于安卓 16 的 ZUX OS，支持电脑模式/分屏/浮窗多任务，超级互联 2.0 打通联想电脑与联想手机，接口含 MicroSD、USB-C 2.0、3.5mm 与 POGO Pin 磁吸键盘触点"
        ],
        "why_important": "ThinkTab 11S 把金属一体机身做到 7mm/485g 并落在 1799 元价位，是千元商用平板结构件与整机成本控制的现成参照。其 ZUX OS 的电脑模式/分屏/浮窗与跨端互联，说明千元档平板已从「影音壳子」转向生产力入口，TCL 平板在系统侧的多任务与跨端能力需要同步对齐。",
        "terminal_relevance": "与平板生态协同",
        "vendor": "联想 Lenovo", "model": "ThinkTab 11S",
        "sources": "IT之家",
        "remark": "8 月 31 日 10:00 首发，首发价 1799 元，部分地区国补后到手价低至 1529.15 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "作业帮学习机 Z100",
        "stars": 4, "source": "B", "date": "2026-08-17", "domain": "平板",
        "url": "https://www.toutiao.com/article/7674848827643363850",
        "url_label": "环球网",
        "signal_type": "首发",
        "confirm_count": "3 个印证源",
        "key_params": "14.7 英寸 OXIDE 类纸护眼巨幕屏 + AI 双屏三摄，自研教育行业首个大模型 + 百亿学情数据，31 亿题库 / 770 万真题试卷，覆盖全国 369 个地级市",
        "tech_features": [
            "14.7 英寸 OXIDE 超广角类纸护眼巨幕屏，获五大机构 11 项护眼认证",
            "搭载 AI 双屏三摄，可对作业/试卷拍照后自动识别错题并生成学情诊断报告",
            "自研教育行业首个大模型 + 百亿学情大数据，支持「随时问」「AI 超级精准学」（错因诊断—错因定位—错因清零）「AI 王牌密训」",
            "本地化首创市级「本地学练考」专区，含本地考点课/精准练/易错题/真题卷/备考五大体系，精细化覆盖全国 369 个地级市"
        ],
        "why_important": "学习机是当前国内少数仍在增长的大屏安卓平板品类，14.7 英寸 OXIDE 大屏 + 11 项护眼认证代表该品类对面板的最新要求。AI 双摄拍题链路（拍照→诊断→计划）也是大屏平板差异化最成熟的一条软件路径，值得 TCL 平板在教育与护眼两条线上直接对标。",
        "terminal_relevance": "大屏护眼面板与平板教育生态",
        "vendor": "作业帮 Zuoyebang", "model": "Z100",
        "sources": "环球网",
        "remark": "8 月 17 日「AI 超级老师」发布会同场亮相，正式进军高端市场，售价尚未公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "台电 ArtPad 13.2 英寸平板",
        "stars": 3, "source": "B", "date": "2026-08-21", "domain": "平板",
        "url": "https://www.toutiao.com/article/7676388158245732910",
        "url_label": "IT之家",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "13.2 英寸 2.2K 120Hz IPS（2240×1600、7:5）+ 紫光展锐 T7300 + 8GB+128GB + 10000mAh/18W，7.5mm/约 728g，1099 元",
        "tech_features": [
            "13.2 英寸 2240×1600 IPS 屏，7:5 比例，支持 120Hz 自适应刷新率与最高 240Hz 触控采样率",
            "支持 4096 级压感手写，可作为绘画与笔记输入",
            "紫光展锐 T7300 处理器 + 8GB RAM + 128GB 存储，支持 microSD/TF 卡扩展（官方全球站标称最高 2TB）",
            "内置 10000mAh 电池支持 18W 有线充电，配立体声双扬声器、Wi-Fi 6 与 4G 全网通，预装基于安卓 16 的 ArtOS"
        ],
        "why_important": "用入门级 SoC 换取 13.2 英寸 120Hz 大屏 + 10000mAh 电池，是低价大屏平板最典型的 BOM 取舍模型。该价位段已经能给到 2.2K/120Hz/4096 级压感，说明大尺寸高刷面板与主动笔方案的成本门槛已明显下移，TCL 平板在 1000–1500 元档需要对位。",
        "terminal_relevance": "大屏低成本平板 BOM 与压感笔方案",
        "vendor": "台电 Teclast", "model": "ArtPad（13.2 英寸）",
        "sources": "IT之家",
        "remark": "8 月 21 日京东上架，星空灰单配色，8GB+128GB 版本 1099 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "学而思学习机 T6 系列（TCL 华星定制屏）",
        "stars": 5, "source": "B", "date": "2026-07-09", "domain": "平板",
        "url": "https://article.pchome.net/info/14421.html",
        "url_label": "PChome",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "TCL 华星联合定制 APEX 自然光护眼屏（13.9 英寸 3000×2000 / 261 PPI，T6 Max 为 15 英寸 3220×2280 / 264 PPI），内置 12000mAh，标准版首发价 6899 元",
        "tech_features": [
            "全系搭载与 TCL 华星联合定制的 APEX 自然光护眼屏，采用自然圆偏振、宽光谱光学调校与双重漫反射设计，获全球首个 SGS 高自然光相似度认证及 10 项护眼认证",
            "T6 Max 配 15 英寸 3220×2280 屏（264 PPI），T6 标准版与国际版配 13.9 英寸 3000×2000 屏（261 PPI）",
            "内置 12000mAh 电池，采用自研双摄像头架构，分别捕捉学生面部学习状态与纸面作答细节",
            "AI 家教支持拍照诊断与学习规划，依据作业或试卷自动生成学情诊断报告与学习计划并同步家长端；T6 Max 新增「小思屏」交互，支持落座唤醒与动态表情互动"
        ],
        "why_important": "这是本批情报中与 TCL 关联度最高的一条：TCL 华星的 APEX 自然光护眼屏已进入学而思旗舰学习机并拿到全球首个 SGS 高自然光相似度认证，说明集团面板资源已在头部教育硬件上完成商业化验证。对 TCL 平板事业部而言，这既是可直接复用的护眼屏资产，也是「自有面板 + 整机」垂直整合的现成样板。",
        "terminal_relevance": "TCL 华星面板与平板整机的垂直整合",
        "vendor": "学而思 TAL", "model": "T6 系列（标准版 / 国际版 / T6 Max）",
        "sources": "PChome",
        "remark": "6 月 30 日发布、7 月 9 日全渠道开售；标准版首发价 6899 元、国际版 8699 元、T6 Max 11999 元"
    },
    {
        "region": "cn", "status": "coming",
        "title": "OPPO Find X10 系列（全球首发天工屏）",
        "stars": 5, "source": "C", "date": "2026-08-26", "domain": "手机",
        "url": "https://baike.baidu.com/item/OPPO%20Find%20X10%20%E7%B3%BB%E5%88%97/68622108",
        "url_label": "百度百科",
        "signal_type": "官宣",
        "confirm_count": "3 个印证源",
        "key_params": "台积电 2nm 天玑 9600 Pro（2+3+3 三丛集，主频逼近 5GHz）+ 全球首发天工屏 + 2 亿像素主摄/2 亿像素潜望长焦，电池目标超 8000mAh，支持 80W 有线快充",
        "tech_features": [
            "搭载台积电 2nm 工艺天玑 9600 Pro，2+3+3 三丛集架构，主频逼近 5GHz，支持 LPDDR6 内存与 UFS 5.0 闪存，集成 NGP 神经加速器",
            "全球首发新一代「天工屏」，搭载自研屏幕双产线技术，RGB 三色发光材料全部换新，支持 BT.2020 色域，并在硬件层面将有益深红光占比提升至 5.5%",
            "全系回归直屏方案，提供 1.5K 与 2K 规格，Pro/Pro Max 支持 LTPO 与高刷新率，全系支持 IP68 与 IP69 防尘防水",
            "影像为 2 亿像素 1/1.3 英寸主摄 + 2 亿像素潜望长焦 + 多光谱镜头；预装 ColorOS 17，Pro 版搭载 3D 超声波屏下指纹"
        ],
        "why_important": "2nm 移动平台 + 自研屏幕双产线是下半年旗舰 SoC 与 OLED 供应链最关键的两个变量，两者都会直接传导到旗舰平板。天工屏把「有益深红光占比 5.5%」作为护眼卖点量化，也为平板护眼屏提供了可复制的指标化叙事。",
        "terminal_relevance": "2nm SoC 与自研 OLED 产线可迁移至旗舰平板",
        "vendor": "OPPO 广东欧珀移动通信", "model": "Find X10 / Pro / Pro Max",
        "sources": "百度百科",
        "remark": "预计 2026 年 9 月中下旬发布，Find X10 Ultra 确认延期至明年初；8 月 26 日天工屏在厦门天马发布会上亮相"
    },
    {
        "region": "cn", "status": "coming",
        "title": "荣耀 Magic9 系列",
        "stars": 4, "source": "C", "date": "2026-08-29", "domain": "手机",
        "url": "https://new.qq.com/rain/a/20260829A071BD00",
        "url_label": "腾讯新闻",
        "signal_type": "官宣",
        "confirm_count": "2 个印证源",
        "key_params": "首批搭载台积电 N2P 2nm 骁龙 8 Elite Gen6，标配 100W 快充头，共三款机型（含带风扇性能旗舰），官宣 9 月 28 日发布并开启预约",
        "tech_features": [
            "首批搭载台积电 N2P 2nm 工艺骁龙 8 Elite Gen6 芯片，为荣耀首款 2nm 旗舰",
            "两款新机疑似入网（内部代号 Twinkle），标配 100W 快充充电器",
            "系列共三款机型，其中包含一款内置风扇的主动散热性能旗舰",
            "8 月 29 日官宣 9 月 28 日发布并同步开启预约，与 2nm 平台首批产能节奏绑定"
        ],
        "why_important": "荣耀把主动散热风扇带进直板旗舰，意味着 2nm 平台在峰值功耗上仍需结构性散热方案补位。这一路径对 TCL 平板的高性能 SKU 很有参考价值——平板有更大腔体，主动散热的引入门槛反而比手机更低。",
        "terminal_relevance": "主动散热架构可迁移至平板高性能 SKU",
        "vendor": "荣耀 HONOR", "model": "Magic9 系列",
        "sources": "腾讯新闻",
        "remark": "定档 9 月 28 日发布；部分配置仍为入网与博主爆料，最终以发布会为准"
    },
    {
        "region": "cn", "status": "released",
        "title": "小天才电话手表 Z12 少年版",
        "stars": 4, "source": "B", "date": "2026-08-05", "domain": "智能手表",
        "url": "https://www.toutiao.com/article/7670441661273326095",
        "url_label": "IT之家",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "高通骁龙 W5 旗舰穿戴芯片（4nm）+ 2GB+64GB，1.78 英寸柔性 AMOLED，3200 万像素 OIS 后摄 + 2000 万像素超感光前摄，2699 元起",
        "tech_features": [
            "搭载高通骁龙 W5 旗舰穿戴芯片（4nm 制程），配备 2GB 运行内存与 64GB 存储",
            "1.78 英寸柔性 AMOLED 屏，应用纳米级 AR 抗反射膜工艺，反射率较前代降低 75%",
            "后置 3200 万像素 OIS 光学防抖主摄 + 前置 2000 万像素超感光摄像头，右侧星环旋钮支持旋转变焦、音量调节与界面导航",
            "全球首款搭载 GSR 皮肤电传感器的儿童手表，结合 PPG 心率识别多种身心状态；楼层定位 5.0 配智能开环天线、独立定位芯片与高精度气压计"
        ],
        "why_important": "儿童手表在 4nm 穿戴平台、3200 万像素 OIS 微型影像模组与 GSR 皮电传感器上的堆料，远超主流成人智能手表。这条「小体积 + 重传感 + 强影像」的路径，对平板的副屏化配件、儿童平板 SKU 都有直接借鉴意义。",
        "terminal_relevance": "穿戴端生物传感与低功耗平台参考",
        "vendor": "小天才（步步高教育电子）", "model": "Z12 少年版",
        "sources": "IT之家",
        "remark": "8 月 5 日发布，2699 元起，搭载全新青春系统 5.0，内置 23 种运动模式"
    },
    {
        "region": "cn", "status": "coming",
        "title": "华为 WATCH 6 系列",
        "stars": 3, "source": "C", "date": "2026-08-30", "domain": "智能手表",
        "url": "https://www.163.com/dy/article/L5JVBH540512ER4R.html",
        "url_label": "网易号",
        "signal_type": "官宣",
        "confirm_count": "2 个印证源",
        "key_params": "9 月 2 日德国慕尼黑「Chase the Wild」全球首发（国内尚未发布），圆形金属表盘 + X-TAP 多感知传感器回归，定位智能健康 + AI 运动分析",
        "tech_features": [
            "延续圆形表盘 + 金属表壳 + 数字表冠 + 物理快捷键布局，官方主打「Slim in Style」，表带衔接处更收敛以降低佩戴体积感",
            "右侧 HUAWEI X-TAP 多感知传感器回归，两处接触区较 WATCH 5 明显扩大，支持指尖血氧测量与一键健康概览",
            "官方明确将带来更全面的健康管理与 AI 驱动的更广泛运动场景分析",
            "与 WATCH GT 7 系列形成人群分工：GT 7 主打户外与长续航，WATCH 6 主打智能、健康与 AI，并时隔一年重返欧洲市场"
        ],
        "why_important": "华为把腕上传感从「功能堆叠」切换到「佩戴体验 + 传感精度」优先，X-TAP 接触面积扩大是精度优先于外观的明确信号。这类端侧健康 AI 的能力边界，决定了平板在健康/教育场景中能承接多少协同算力。",
        "terminal_relevance": "穿戴生物传感与端侧 AI 健康算法",
        "vendor": "华为 Huawei", "model": "WATCH 6 系列",
        "sources": "网易号",
        "remark": "9 月 2 日慕尼黑全球首发，国内发布时间未定；屏幕尺寸、处理器、电池容量等详细参数待发布会公布"
    },
    {
        "region": "cn", "status": "coming",
        "title": "PICO Space Pro（Project Swan）",
        "stars": 5, "source": "B", "date": "2026-08-19", "domain": "AR-VR眼镜",
        "url": "https://new.qq.com/rain/a/20260820A0CWWQ00",
        "url_label": "腾讯新闻",
        "signal_type": "官宣",
        "confirm_count": "3 个印证源",
        "key_params": "定制 Micro-OLED 近 4000 PPI（平均 40 PPD、中心峰值 45 PPD）+ 双芯片架构（自研 XR 芯片 + 旗舰主处理器）+ 分体式约 100g 头显本体，感知延迟 12ms",
        "tech_features": [
            "定制 Micro-OLED 微显示屏，像素密度近 4000 PPI，平均角分辨率 40 PPD、视野中心区域最高 45 PPD（对比 Apple Vision Pro 约 34 PPD、Meta Quest 3 约 25 PPD）",
            "双芯片协同架构：PICO 全链路自研 XR 芯片负责空间感知、图像处理与传感器数据融合，将感知延迟压缩至 12ms；主处理器 CPU/GPU 性能为前代平台的两倍",
            "分体式轻量化设计，将计算与供电模块外置，头显本体重量压缩至约 100g，配人体工学编织头带与额头缓冲结构",
            "首发 PICO OS 6 系统与 PICO Spatial Engine 空间引擎，统一渲染架构支持 2D 应用、3D 空间应用与全景沉浸式内容在三维空间内并行运行"
        ],
        "why_important": "PICO 用「自研 XR 协处理器 + 分体式外置算力」同时解性能、重量、散热三个死结，是国产 XR 目前最完整的一套工程答案。45 PPD 超过 Vision Pro 意味着国产近眼显示供应链已具备对标海外的能力，这条供应链同样服务 AR 眼镜与未来平板的光学创新。",
        "terminal_relevance": "分体式计算架构与近眼显示供应链",
        "vendor": "PICO（字节跳动）", "model": "Space Pro（Project Swan）",
        "sources": "腾讯新闻",
        "remark": "8 月 19 日官宣 9 月 2 日发布会；8 月 24 日官方公告发布调整，新品推迟至 2026 年第四季度，理由为首发版本要落地一处新软件能力"
    },
    {
        "region": "cn", "status": "coming",
        "title": "雷鸟 GT / GT Max 影院级 AR 眼镜",
        "stars": 4, "source": "C", "date": "2026-08-21", "domain": "AR-VR眼镜",
        "url": "https://new.qq.com/rain/a/20260821A0BW8D00",
        "url_label": "腾讯新闻",
        "signal_type": "首发",
        "confirm_count": "2 个印证源",
        "key_params": "Peacock 光学引擎 3.0 Max + 第 5.5 代 Tandem MicroOLED，GT Max 提供 59° 视场角与 227/267/307 英寸三档缩放，GT 68g / GT Max 78g，全球定价 299 / 399 美元",
        "tech_features": [
            "双芯片架构：Vision 4000 显示芯片 + Zone 360 3DoF 芯片，硬件级 3DoF 追踪支持 Steady、Pinned、Follow 三种观看模式",
            "Peacock 光学引擎 3.0 Max + 第 5.5 代 Tandem MicroOLED，GT Max 提供 59° 视场角，可动态缩放虚拟屏幕至 227/267/307 英寸",
            "搭配雷鸟 Pocket TV Pro 成为全球首套支持原生杜比视界播放、并具备实时 AI SDR 转 HDR 功能的 AR 眼镜系统",
            "GT 重 68g、GT Max 重 78g，配 B&O 调音赛道式四扬声器，升级 6 磁路设计使低频灵敏度提升 5dB，支持头部追踪空间音频与 Whisper Mode"
        ],
        "why_important": "雷鸟把 Tandem MicroOLED + 双显示芯片下探到 299 美元价位，并首次把杜比视界与实时 AI SDR→HDR 做成系统级能力。观影型 AR 眼镜与平板在「私人巨幕」场景上直接竞争，这条产品线的规格—价格曲线是 TCL 平板影音定位必须跟踪的替代威胁。",
        "terminal_relevance": "近眼显示模组与 Tandem OLED 供应链",
        "vendor": "雷鸟创新 RayNeo", "model": "GT / GT Max",
        "sources": "腾讯新闻",
        "remark": "8 月 21 日发布，官方零售 2026 年 9 月 4 日启动（官网与亚马逊）；两款均支持官方定制处方镜片插片"
    },
    {
        "region": "cn", "status": "released",
        "title": "华为 MateBook Fold 非凡大师（新款）",
        "stars": 5, "source": "B", "date": "2026-08-28", "domain": "笔记本",
        "url": "https://www.ithome.com/0/995/486.htm",
        "url_label": "IT之家",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "18 英寸双层 OLED 折叠屏（3.3K / 1600nits / 92% 屏占比），折叠后为 13 英寸形态、1.16kg、平展薄至 7.3mm，40μm UTG 柔性玻璃，国补到手价 23499 元",
        "tech_features": [
            "18 英寸双层 OLED 折叠巨幕，3.3K 分辨率、1600nits 峰值亮度、92% 屏占比，10Hz–90Hz LTPO 自适应刷新，AR 镀膜使反射率低至 2.5%，配 1440Hz 高频 PWM 调光",
            "业界首次实现 40μm 超薄 UTG 柔性玻璃量产，抗冲击能力提升 90%、抗弯曲形变提升 10 倍、抗挤压提升 30%，可承受 50 万次手写笔点击；玄武水滴铰链采用锆基液态金属主轴",
            "折叠后为 13 英寸轻薄本形态，整机 1.16kg、平展薄至 7.3mm；双层 OLED 架构实现 30% 能效优化与 3 倍屏幕寿命提升",
            "首次在鸿蒙折叠电脑中加入原生手写能力，HUAWEI M-Pen 3 支持提笔即写、全局批注、小艺圈选与远场空鼠翻页"
        ],
        "why_important": "18 英寸折叠屏 + 原生手写笔 + 专业软件深度适配，正在侵蚀「大屏平板 + 键盘」的生产力腹地。40μm UTG 量产与双层 OLED 能效/寿命数据，是 TCL 平板在评估折叠或超大屏形态时最需要的一手工程指标。",
        "terminal_relevance": "折叠屏形态与平板大屏生产力的边界",
        "vendor": "华为 Huawei", "model": "MateBook Fold 非凡大师（新款）",
        "sources": "IT之家",
        "remark": "随 8 月 28 日鸿蒙电脑新品阵容全面开售同步开放国补，最低到手价 23499 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "机械革命 无界 14S 2026 轻薄本",
        "stars": 3, "source": "B", "date": "2026-08-27", "domain": "笔记本",
        "url": "https://tech.ifeng.com/c/8vvpZXbqKc2",
        "url_label": "凤凰网科技",
        "signal_type": "开售",
        "confirm_count": "2 个印证源",
        "key_params": "英特尔 18A 制程「Wildcat Lake」酷睿 5 315，12GB + 500GB，14 英寸 1920×1200 60Hz 100% sRGB 雾面屏，1.1kg / 60Wh，定价 4199 元、首发 3899 元",
        "tech_features": [
            "基于 Intel 18A 制程工艺「Wildcat Lake」酷睿 5 315，官方称相比前代图像编辑性能 +48%、网页浏览性能 +45%、功耗 -64%",
            "12GB RAM + 500GB SSD 组合，支持至高 30W 性能释放",
            "14 英寸 1920×1200 60Hz 雾面屏，覆盖 100% sRGB 高色域并支持全局 DC 调光；银色金属机身约 1.1kg，键盘 1.3mm 键程",
            "内置 60Wh 电池，官方标称本地视频播放 24+ 小时、综合办公 21+ 小时；接口含 2 个全功能 USB-C 10Gbps、2 个 USB-A 5Gbps、HDMI 2.1 与 3.5mm 音频口"
        ],
        "why_important": "这是 Intel 18A 首批落地的消费终端之一，-64% 功耗与 21+ 小时办公续航是检验新制程能效的真实样本。该平台若下放到平板或二合一形态，将直接改变 ARM/Windows 平板的续航竞争格局，需要提前做功耗与散热预研。",
        "terminal_relevance": "低功耗平台与续航设计参考",
        "vendor": "机械革命 MECHREVO", "model": "无界 14S 2026",
        "sources": "凤凰网科技",
        "remark": "8 月 27 日 10:00 京东开售，定价 4199 元、首发价 3899 元，部分地区国补后低至 3314.15 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "绿联二合一折叠无线充电器（Qi2.2 25W）",
        "stars": 3, "source": "B", "date": "2026-08-29", "domain": "无线充",
        "url": "https://news.mydrivers.com/1/1147/1147398.htm",
        "url_label": "快科技",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "Qi2.2 25W 磁吸主充板 + 5W 副充板，折叠后仅 6.02×7.26×2.67 厘米，建议搭配 45W 以上适配器，售价 59.99 美元",
        "tech_features": [
            "支持 25W Qi2.2 无线充电标准，内置磁吸模组，兼容 iPhone 系列及其他 Qi2 设备；第二块充电板输出功率为 5W，适用于 AirPods / AirPods Pro",
            "采用类 MagSafe Duo 的二合一折叠结构，折叠后尺寸仅 6.02×7.26×2.67 厘米，可握于掌中或收入口袋",
            "折叠形态下可作为手机支架使用，充电板正面采用玻璃材质兼顾美观与耐用",
            "内置过充保护、过压保护、短路保护与异物检测等多重安全机制，官方建议搭配 45W 以上电源适配器以保证稳定输出"
        ],
        "why_important": "Qi2.2 25W 正从桌面支架形态向折叠便携形态下沉，意味着 25W 级磁吸的线圈、磁组与温控方案已经可以做进 2.67 厘米厚度。平板若要引入磁吸充电或磁吸配件生态，这条体积—功率—散热的平衡点是必须参考的基线。",
        "terminal_relevance": "可迁移至平板磁吸充电与配件生态",
        "vendor": "绿联 UGREEN", "model": "二合一折叠无线充电器（25W Qi2.2）",
        "sources": "快科技",
        "remark": "8 月底在美国市场推出，售价 59.99 美元；中国大陆定价与上架时间尚未公布"
    },
    {
        "region": "cn", "status": "released",
        "title": "漫步者 K200 便携 K 歌音箱",
        "stars": 3, "source": "B", "date": "2026-08-28", "domain": "智能音箱",
        "url": "https://www.toutiao.com/article/7678969244368814626/",
        "url_label": "IT之家",
        "signal_type": "开售",
        "confirm_count": "2 个印证源",
        "key_params": "28W 连续不失真功率 / 56W 峰值，22mm 丝绢膜球顶高音 + 53×93mm 跑道型长冲程中低音，标配无线双麦克风，2×2600mAh 续航 17.5 小时，799 元",
        "tech_features": [
            "28W 连续不失真功率、峰值 56W，声学配置为 22mm 丝绢膜球顶高音单元 + 53×93mm 跑道型长冲程中低音单元",
            "标配无线双麦克风，每只麦克风支持独立音量与音效调节以适配不同声线，并提供专属收纳盒",
            "内置 2 节 2600mAh 锂电池，最长续航 17.5 小时；蓝牙 6.0 可同时连接两台设备，支持蓝牙、USB 声卡、TF 卡多种输入方式",
            "搭载 32 位高精度 DSP 音频处理芯片，提供 5+N 种音乐音效与 8 种 K 歌音效，兼容全民 K 歌、唱吧、酷狗、网易云、QQ 音乐等主流应用"
        ],
        "why_important": "便携音箱正从单纯外放转向「DSP 音效 + 双麦 K 歌」的场景化硬件，799 元价位即标配无线双麦与多模输入。这类设备是平板影音/客厅 K 歌场景最直接的音频外延，TCL 平板在家庭娱乐配件上的空白值得关注。",
        "terminal_relevance": "平板外接音频与家庭影音 K 歌场景",
        "vendor": "漫步者 Edifier", "model": "K200",
        "sources": "IT之家",
        "remark": "8 月 28 日推出，8 月 31 日 20:00 开售，售价 799 元"
    },
    {
        "region": "cn", "status": "released",
        "title": "1MORE 万魔 AiClip S52 耳夹式 AI 耳机",
        "stars": 4, "source": "B", "date": "2026-08-13", "domain": "AI耳机·耳穿戴",
        "url": "https://news.yesky.com/hotnews/439/366439.shtml",
        "url_label": "天极网",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "11mm 动圈 + Hi-Res 无线金标 + LDAC，0.5mm 动钛 C 桥舒适豆 2.0 结构，深度接入五大主流大模型，单次 10 小时 / 综合 45 小时，IPX5，原价 698 元",
        "tech_features": [
            "采用 0.5mm 动钛 C 桥 + 黄金四点支撑的「舒适豆 2.0」架构，实现耳廓与耳背双重支撑，解决球状耳夹单点硌耳与耳背磨肤痛点",
            "搭载 11mm 超大动圈单元，获国际 Hi-Res 无线金标认证并支持 LDAC 无损解码",
            "深度接入 DeepSeek、字节豆包、腾讯混元、通义千问、文心一言五大模型；支持会议录音转写、17 种以上语言互译与拍照问答",
            "蓝牙 6.0 支持手机/电脑双设备无缝切换，四麦协同降噪 + 360° 抗风噪算法，单次续航 10 小时、综合 45 小时，IPX5 级防水抗汗"
        ],
        "why_important": "开放式耳夹已经把「多模型 AI 会议助手」做成标配能力（转写、脑图、同传），端侧 AI 交互正从手机向耳端迁移。平板作为会议与生产力主设备，需要考虑与这类耳穿戴 AI 外设的协同接口与多设备切换体验。",
        "terminal_relevance": "与平板会议/生产力场景的 AI 外设协同",
        "vendor": "万魔 1MORE", "model": "AiClip S52",
        "sources": "天极网",
        "remark": "8 月 13 日与 AERO Q32、SonoFlow Max HQ60 同场上市，原价 698 元、到手价 628.2 元、国补价 533.97 元"
    },

    # ========== 国际 15 条 ==========
    {
        "region": "intl", "status": "released",
        "title": "OnePlus Pad 4",
        "stars": 5, "source": "B", "date": "2026-07", "domain": "平板",
        "url": "https://www.notebookcheck.net/Really-fast-tablet-giant-that-lasts-for-days-OnePlus-Pad-4-Review.1349991.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "13.2 英寸 3392×2400 144Hz IPS 平板，骁龙 8 Elite Gen 5 + 12GB/256GB，13380mAh 电池 + 80W 快充，5.9mm / 672g，八扬声器",
        "tech_features": [
            "13.2 英寸 14:10 IPS 屏，3392×2400 分辨率（315 PPI）、144Hz 刷新率、540Hz 触控采样率、支持 Dolby Vision",
            "骁龙 8 Elite Gen 5（2×4.6GHz Oryon Gen 3 大核 + 6×3.6GHz 性能核）+ Adreno 840，配 12GB 内存与 256GB UFS 4.1",
            "13380mAh 电池 + 80W 有线快充，机身厚 5.9mm、重 672g，无风扇被动散热",
            "八扬声器系统 + 机身背部 3 个 Pogo pin 直连键盘盖，Wi-Fi 7 与蓝牙 6.0"
        ],
        "why_important": "13.2 英寸 + 13380mAh 却压到 5.9mm/672g，说明大电池与超薄机身可通过堆叠与结构件复用同时达成，值得 TCL 大屏平板做厚度/续航对标。背部 Pogo pin 直连键盘盖在时延与供电上优于蓝牙键盘，可作为二合一配件架构参考。",
        "terminal_relevance": "大屏平板：续航/厚度/扬声器/键盘触点架构",
        "vendor": "一加 OnePlus", "model": "OnePlus Pad 4",
        "sources": "Notebookcheck",
        "remark": "欧洲 €799（亚马逊 €699.90）；全球版约 $609（12+256）；无 IP 防护等级"
    },
    {
        "region": "intl", "status": "released",
        "title": "Nubia Pad Plus (Wi-Fi)",
        "stars": 3, "source": "B", "date": "2026-08-27", "domain": "平板",
        "url": "https://www.notebookcheck.net/Nubia-launches-Android-tablet-for-249-with-12-inch-display-Widevine-L1-and-USB-C-video-output.1380263.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "首发",
        "confirm_count": "2 个印证源",
        "key_params": "12 英寸 2000×1200 90Hz IPS，Unisoc T820（6nm），6GB + 128GB，8000mAh / 26W，四扬声器，JPY 39,800（约 $249）日本上市",
        "tech_features": [
            "12 英寸 IPS 屏，2000×1200 分辨率、90Hz 刷新率",
            "Unisoc T820（6nm 八核 CPU + Mali-G57 MC4），6GB 内存 + 128GB 存储",
            "8000mAh 电池 + 26W 有线快充，标称 7.6 小时视频播放 / 9.5 小时网页浏览（包装不含充电器）",
            "四扬声器 + Widevine L1 + USB-C 支持视频输出；机身 281×177×7.2mm、约 550g，IPX2"
        ],
        "why_important": "$249 价位把 12 英寸大屏、四扬声器与 USB-C 视频输出（可投外显）下放，是低成本大屏平板的配置基准线。USB-C 视频输出对教育/会议投屏是低成本差异化点，平板端值得预埋。",
        "terminal_relevance": "入门大屏平板：BOM 基线 / 投屏能力 / 扬声器配置",
        "vendor": "努比亚 Nubia（中兴）", "model": "Nubia Pad Plus (Wi-Fi)",
        "sources": "Notebookcheck",
        "remark": "日本 JPY 39,800；触控键盘套 JPY 9,800，套装限量 JPY 42,800"
    },
    {
        "region": "intl", "status": "released",
        "title": "Tecno MegaPad SE 2",
        "stars": 2, "source": "B", "date": "2026-08-30", "domain": "平板",
        "url": "https://www.notebookcheck.net/Tecno-officially-launches-tablet-with-2K-display-and-LTE-connectivity.1382974.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "9.7 英寸 2048×1280 90Hz LCD，Helio G88，4GB + 256GB，7000mAh / 18W，4G LTE，PHP 13,499（约 $217）菲律宾开售",
        "tech_features": [
            "9.7 英寸 LCD，2048×1280 分辨率、90Hz 刷新率、550nits 峰值亮度",
            "联发科 Helio G88（八核最高 2.0GHz + Mali-G52 MC2），4GB 内存 + 最高 256GB 存储",
            "microSD 扩展最高 2TB，配 7000mAh 电池与 18W USB-C 充电",
            "机身 7.9mm 厚、约 387g，单 nano-SIM 支持 4G LTE，双频 Wi-Fi + 双扬声器"
        ],
        "why_important": "9.7 英寸 + 387g + 4G LTE 的紧凑组合，是新兴市场「可通话小尺寸平板」的典型规格包。2TB microSD 扩展在入门平板上仍是刚需卖点，TCL 海外低价线需注意保留卡槽而非只推云存储。",
        "terminal_relevance": "小尺寸平板：新兴市场形态 / 存储扩展 / 蜂窝连接",
        "vendor": "传音 Tecno", "model": "MegaPad SE 2",
        "sources": "Notebookcheck",
        "remark": "菲律宾 PHP 13,499（4GB+256GB）；三色：Deep Gray / Sandy Titanium / Iris Purple"
    },
    {
        "region": "intl", "status": "released",
        "title": "Honor Pad X9 Max",
        "stars": 3, "source": "B", "date": "2026-07-23", "domain": "平板",
        "url": "https://www.gadgets360.com/tablets/news/honor-pad-x9-max-price-launch-specifications-features-11809450",
        "url_label": "Gadgets 360",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "13 英寸 2500×1560 120Hz LCD，骁龙 6s Gen 2，最高 6GB + 256GB，10100mAh / 45W，四扬声器 IMAX Enhanced，£349.99 起",
        "tech_features": [
            "13 英寸 2.5K（2500×1560）LCD，120Hz 刷新率、700nits 峰值、228 PPI、88% 屏占比、10.7 亿色",
            "骁龙 6s Gen 2 八核（4 性能核 + 4 能效核，峰值 2.9GHz），最高 6GB + 256GB（可扩展至 2TB）",
            "10100mAh 电池 + 45W 有线快充，标称 16 小时视频播放 / 13 小时阅读 / 最长 90 天待机",
            "TÜV 莱茵类纸屏认证（宣称消除 98% 环境光、降低 35% 闪烁）+ 低蓝光与无频闪认证；四扬声器支持 IMAX Enhanced"
        ],
        "why_important": "13 英寸 120Hz + 10100mAh + 45W 构成的大屏长续航组合，是 TCL 大屏平板最直接的规格对照物。把「护眼」做成可量化认证指标（98% 环境光消除、35% 闪烁降低），说明类纸屏的竞争已进入认证与参数化阶段，NXTPAPER 产品线需跟进话术与第三方背书。",
        "terminal_relevance": "大屏平板：护眼显示认证 / 长续航 / 海外定价带",
        "vendor": "荣耀 Honor", "model": "Honor Pad X9 Max",
        "sources": "Gadgets 360",
        "remark": "4GB+128GB £349.99 / 6GB+256GB £449.99；英国等部分海外市场官网在售"
    },
    {
        "region": "intl", "status": "released",
        "title": "Motorola Edge 70 Max",
        "stars": 5, "source": "B", "date": "2026-07-15", "domain": "手机",
        "url": "https://www.thehindu.com/sci-tech/technology/gadgets/motorola-edge-70-max-launched-in-india/article71224516.ece/amp",
        "url_label": "The Hindu",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "6.8 英寸 QHD+ LTPO AMOLED 144Hz（峰值 7000nits），骁龙 8 Gen 5，7100mAh 硅碳电池，90W 有线 + 25W Qi2 磁吸无线，₹54,999",
        "tech_features": [
            "6.8 英寸 QHD+（1440×3168）LTPO AMOLED，1–144Hz 自适应、峰值亮度 7000nits、10bit、HDR10+、康宁大猩猩玻璃 7i",
            "7100mAh 硅碳负极电池，90W 有线 TurboPower + 25W Qi2 磁吸无线 + 5W 反向有线，标称 58 小时续航",
            "5500mm² 均热板散热；221g / 8.29mm，IP68 + IP69 与 MIL-STD-810H 军规认证",
            "骁龙 8 Gen 5（2 颗 3.8GHz 超大核 + 6 颗 3.3GHz 性能核）+ 12GB LPDDR5X + 256GB UFS 4.1，Wi-Fi 7 / 蓝牙 6"
        ],
        "why_important": "7100mAh 硅碳电芯 + 90W 有线 + 25W Qi2 磁吸无线共存，是高能量密度电池与无线充兼容的一次完整工程验证，对 TCL 平板引入硅碳电芯与磁吸生态有直接参考价值。Qi2 磁吸在手机端普及后，平板端磁吸配件与对位充电的兼容性需提前规划。",
        "terminal_relevance": "平板：硅碳电池 / 磁吸无线充 / 均热板散热面积",
        "vendor": "摩托罗拉 Motorola（联想）", "model": "Motorola Edge 70 Max",
        "sources": "The Hindu",
        "remark": "印度 7/15 发布、7/20 开售；8GB+256GB ₹54,999、12GB+256GB ₹59,999"
    },
    {
        "region": "intl", "status": "released",
        "title": "Nothing Phone (4b)",
        "stars": 3, "source": "B", "date": "2026-07-17", "domain": "手机",
        "url": "https://www.gsmarena.com/newsdetail.php3?idNews=73609&c=10003",
        "url_label": "GSMArena",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "6.77 英寸 1080p+ OLED 120Hz（峰值 2000nits），骁龙 6 Gen 4，5200mAh / 33W，Glyph Bar 五灯条，€330 / £300",
        "tech_features": [
            "6.77 英寸 1080p+ OLED，120Hz、户外模式 1200nits / 峰值 2000nits，龙迹 Pro 玻璃",
            "骁龙 6 Gen 4 + LPDDR4X + UFS 2.2，全球多数市场 8GB/128GB；印度版电池加大到 6000mAh",
            "5200mAh 电池 + 33W 有线 + 7.5W 反向有线，标称 22 小时连续视频播放",
            "背部 Glyph Bar 由 4 颗白光 + 1 颗红光 LED 组成，可自定义用于计时器与录制指示；IP64、屏下光学指纹、蓝牙 6.0"
        ],
        "why_important": "以 5200mAh + 33W 做出「Nothing 续航最长的机型」，说明中端机续航竞争已从堆容量转向 SoC 能效与系统调度，平板同样可走这条路。Glyph Bar 用 5 颗 LED 承担通知/计时/录制指示，是极低成本的「光交互」硬件方案，平板可参考用于充电与状态提示。",
        "terminal_relevance": "终端：LED 状态交互 / 续航调度 / 中端 BOM 成本压力",
        "vendor": "Nothing", "model": "Nothing Phone (4b)",
        "sources": "GSMArena",
        "remark": "7/7 发布、7/17 零售；€330 / £300 / ₹34,999；3 年系统更新 + 6 年安全更新"
    },
    {
        "region": "intl", "status": "released",
        "title": "Casio G-Shock GBX-H5600KI-5",
        "stars": 3, "source": "B", "date": "2026-08-28", "domain": "智能手表",
        "url": "https://www.notebookcheck.net/Casio-s-new-heart-rate-sensor-equipped-G-Shock-launches-in-more-markets.1381012.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "上市",
        "confirm_count": "3 个印证源",
        "key_params": "光学心率 + 三轴加速度计 G-Shock 冲浪签名款，Polar 算法，200m 防水 + 太阳能，$370 / €329，8 月登陆德/荷/西等多国",
        "tech_features": [
            "光学心率传感器 + 三轴加速度计，训练分析跑 Polar 算法，覆盖心肺负荷、睡眠恢复、配速/距离/步幅",
            "MIP LCD 屏；碳纤维增强树脂表背，比上一代心率款减重约 18g",
            "连续心率记录最长 35 小时；200m 防水 + 太阳能充电 + 矿物玻璃",
            "机身 51.1×44.5×17.3mm、重 47g；生物基树脂表壳表带，薰衣草色点缀用气相沉积"
        ],
        "why_important": "碳纤维增强树脂表背在保持 200m 防水前提下减重 18g，是穿戴产品「结构件材料换重量」的可量化案例，可直接迁移到平板后盖与支架设计。心率 + 三轴加速度 + 第三方 Polar 算法的分工，说明运动算法可外购而不必全栈自研。",
        "terminal_relevance": "穿戴与终端：结构减重材料 / 传感器选型 / 算法外购模式",
        "vendor": "卡西欧 Casio", "model": "G-Shock GBX-H5600KI-5",
        "sources": "Notebookcheck",
        "remark": "德/荷/西 €329；美国 $370；日本以外市场预计 9 月铺货"
    },
    {
        "region": "intl", "status": "released",
        "title": "Whoop 5.0 Meridian 钛金属表带",
        "stars": 2, "source": "B", "date": "2026-08-27", "domain": "智能手表",
        "url": "https://www.notebookcheck.net/Whoop-5-0-Meridian-launches-with-titanium-build-but-surprising-drawback.1380336.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "上市",
        "confirm_count": "2 个印证源",
        "key_params": "Whoop 5.0 专用 100% 钛金属米兰尼斯表带，$149，8 月 27 日官网开售（主机与订阅另购）",
        "tech_features": [
            "表带 100% 钛金属编织，PVD 工艺实现玫瑰金 / 金色 / 哑光黑，另有银色，共 4 色",
            "磁吸卡扣可无级调节，适配无屏健康追踪器 Whoop 5.0",
            "单独售价 $149；主机需另购，入门订阅 $199/年、进阶订阅 $359/年",
            "金属编织层会屏蔽电磁感应，给主机无线充电前必须先把表带拆下"
        ],
        "why_important": "一条表带做出 $149 的溢价，说明可穿戴的「材质升级/珠宝化」是高毛利路径。金属编织表带与电感式无线充电物理冲突，是金属化外观与无线充共存的反面案例——平板若做金属机身 + 无线充电，需提前规避整块金属遮蔽线圈。",
        "terminal_relevance": "穿戴配件：材质溢价 / 无线充与金属件冲突 / 订阅制",
        "vendor": "Whoop", "model": "Whoop 5.0 Meridian Band",
        "sources": "Notebookcheck",
        "remark": "$149 仅表带；Whoop 5.0 主机另售（$239 起），必须绑定订阅才能使用"
    },
    {
        "region": "intl", "status": "released",
        "title": "Even Realities G2 显示智能眼镜",
        "stars": 5, "source": "C", "date": "2026-08-06", "domain": "AR-VR眼镜",
        "url": "https://www.cool3c.com/article/250495",
        "url_label": "Cool3c",
        "signal_type": "开售",
        "confirm_count": "4 个印证源",
        "key_params": "36g 双目 Micro-LED + 光波导全彩显示眼镜，无摄像头无外放，1200nits、透光率 98%，台湾 8 月 6 日开售 NT$19,990",
        "tech_features": [
            "整机含镜片约 36g，镁合金镜框 + 钛金属镜脚，圆框/方框两款、灰/棕/绿三色",
            "双目 Micro-LED + 光波导显示，透光率 98%、最大亮度 1200nits，可随环境自动调节",
            "完全无摄像头、无外放扬声器，仅内建 4 组麦克风；IP65、蓝牙 5.4",
            "单次充电约 2 天，充电盒可再充约 7 次、合计约 2 周；支持 35 种语言双向实时翻译；可配 Even R1 智能戒指手势操控"
        ],
        "why_important": "36g 做到双目全彩波导显示，靠的是「砍掉摄像头与外放」的极端功能取舍，说明全彩 AR 眼镜的轻量化首先要做减法，对 TCL AR 眼镜的重量预算分配是最直接的参考。眼镜 + 戒指的手势交互闭环，为「显示终端 + 低功耗控制器」双设备架构提供了现成范式。",
        "terminal_relevance": "AR 眼镜：Micro-LED 波导 / 整机减重策略 / 双设备交互架构",
        "vendor": "Even Realities", "model": "Even G2（配 Even R1 智能戒指）",
        "sources": "Cool3c",
        "remark": "7/15 发布、7/30 台湾开放预购、8/6 正式开卖；眼镜 NT$19,990，R1 戒指 NT$7,990"
    },
    {
        "region": "intl", "status": "released",
        "title": "Rollme View Series（AuraView / ProView）",
        "stars": 2, "source": "B", "date": "2026-08-19", "domain": "AR-VR眼镜",
        "url": "https://www.notebookcheck.net/Rollme-launches-new-99-99-smart-camera-glasses-with-AI-live-translation-and-a-Sony-12MP-camera.1372554.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "首发",
        "confirm_count": "2 个印证源",
        "key_params": "$99.99 AI 拍摄眼镜，索尼 12MP 摄像头 + EIS，双芯片架构驱动端侧 AI 与实时翻译，280mAh，8 月 19 日上市",
        "tech_features": [
            "索尼 12MP 摄像头 + 电子防抖（EIS），按下快门后 0.6 秒完成拍摄",
            "双芯片架构驱动 AI 助手、视觉识别（物体/地标）与书本/印刷文本翻译，另有独立口语实时翻译模式",
            "双独立扬声器 + 高灵敏度麦克风与通话降噪，280mAh 电池",
            "TR90 镜框：AuraView 为金属半框 + 棕色调镜片，ProView 为全框并附深色墨镜与透明两副镜片"
        ],
        "why_important": "$99.99 把 12MP 索尼传感器 + 双芯片 + 实时翻译压进眼镜，说明 AI 眼镜的硬件成本门槛已降到百美元级，TCL 若切入需按此成本线反推设计。相比 2025 年 AirView 的 $79.99，一年涨价 25%，直接反映存储与芯片涨价对可穿戴 BOM 的挤压。",
        "terminal_relevance": "AI 眼镜：百美元成本线 / 双芯片架构 / BOM 涨价压力",
        "vendor": "Rollme", "model": "Rollme View Series：AuraView / ProView",
        "sources": "Notebookcheck",
        "remark": "$99.99 两款同价，Rollme 官方商店发售；未公布重量、视频规格与机内存储容量"
    },
    {
        "region": "intl", "status": "released",
        "title": "HP Omen Max 16（AMD 版）",
        "stars": 4, "source": "A", "date": "2026-08", "domain": "笔记本",
        "url": "https://www.hp.com/gb-en/shop/products/laptops/omen-max-gaming-laptop-16-ak0000na-bn8c9ea-abu",
        "url_label": "HP 官方（英国）",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "16 英寸 WQXGA 240Hz IPS，Ryzen AI 9 HX 375 + RTX 5080 16GB，Unleashed 模式 250W TPP，£2,499（原价 £2,800）",
        "tech_features": [
            "AMD Ryzen AI 9 HX 375（12 核 / 24 线程，最高 5.1GHz，内置 NPU）+ RTX 5080 笔记本版 16GB GDDR7",
            "16 英寸 WQXGA（2560×1600）IPS，60–240Hz 可变刷新、3ms 响应、500nits、100% sRGB，支持 DC 调光",
            "Unleashed 模式整机总功耗 250W（CPU 75W + GPU 175W）；OMEN Tempest Cooling Pro 采用均热板 + CPU/GPU 双涂 Cryo 液态金属 + IR 热传感器",
            "83Wh 六芯电池，30 分钟充至 50%；32GB DDR5-5600 + 1TB PCIe Gen4；MediaTek Wi-Fi 7 + 蓝牙 5.4"
        ],
        "why_important": "CPU/GPU 双涂液态金属 + 均热板 + IR 热传感器，是 250W TPP 长期稳定释放的关键，对 TCL 高性能平板的散热设计（尤其非对称热源布局）有直接参考价值。83Wh + 30 分钟充至 50% 说明大功耗设备仍可用快充把续航短板补回来。",
        "terminal_relevance": "高性能平板：液态金属散热 / 功耗分配 / 快充补位",
        "vendor": "惠普 HP", "model": "OMEN MAX 16-ak0000na",
        "sources": "HP 英国官网",
        "remark": "英国 £2,499（原价 £2,800）；美国 MSRP $3,699，促销价 $2,199.99；重约 2.72kg"
    },
    {
        "region": "intl", "status": "released",
        "title": "Razer Blade 18 (2026)",
        "stars": 5, "source": "A", "date": "2026-08", "domain": "笔记本",
        "url": "https://www.razer.com/gaming-laptops/razer-blade-18",
        "url_label": "Razer 官方",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "18 英寸双模屏（UHD+ 240Hz / FHD+ 440Hz），Ultra 9 290HX Plus + RTX 5090 175W，最高 128GB DDR5-6400，$3,499 起",
        "tech_features": [
            "全球首款 18 英寸双模屏：UHD+ 3840×2400@240Hz 与 FHD+ 1920×1200@440Hz 一键切换，600nits（SDR）、100% DCI-P3、Calman 认证",
            "Intel Core Ultra 9 290HX Plus（24 核 / 24 线程，最高 5.5GHz，NPU 13 TOPS）+ RTX 5090 笔记本版（24GB VRAM、175W TGP）",
            "散热为均热板 + 三风扇 + 热罩导流结构，整机 280W TPP，散热鳍片厚仅 0.05mm",
            "最高 128GB DDR5-6400 双通道，双 M.2 可扩展至 8TB（Gen4）；Thunderbolt 5 达 120Gbps"
        ],
        "why_important": "同一块屏用「分辨率/刷新率可切换」同时覆盖创作与电竞，是显示规格与功耗按场景动态分配的思路，平板可借鉴做「高刷模式 / 高分辨率模式」的用户可选档位。280W TPP 下用 0.05mm 超薄鳍片 + 三风扇，说明高功率轻薄化要靠鳍片密度而非单纯加大风扇。",
        "terminal_relevance": "平板：双模显示策略 / 高密度散热鳍片 / 高速扩展接口",
        "vendor": "雷蛇 Razer", "model": "Razer Blade 18（RZ09-0582 系列）",
        "sources": "Razer 官方",
        "remark": "美/英已上市，$3,499.99 / £3,299.99 起，顶配 128GB 版 $6,999.99 仅美国"
    },
    {
        "region": "intl", "status": "released",
        "title": "Twelve South Valet / Valet Small",
        "stars": 3, "source": "B", "date": "2026-07-30", "domain": "无线充",
        "url": "https://www.notebookcheck.net/Twelve-South-Qi2-wireless-charging-pad-with-Nappa-leather-comes-in-two-sizes.1353944.0.html",
        "url_label": "Notebookcheck",
        "signal_type": "上市",
        "confirm_count": "4 个印证源",
        "key_params": "Qi2 25W 磁吸无线充电托盘（Nappa 皮革台面 + 锌合金加重底座），$179 / $129，7 月 30 日官方开售",
        "tech_features": [
            "Qi2 磁吸无线充电最高 25W，另有一路 USB-C 输出最高 19W 可为耳机等设备补电",
            "Nappa 皮革台面 + 锌合金加重底座（内置理线结构），外框可拆换，黑 / 米 / 棕三色",
            "两种尺寸：标准款深约 19cm，Valet Small 深约 10.8cm",
            "标配 1.5m USB-C 线与电源适配器；Small 款可同时为 3 台设备补电"
        ],
        "why_important": "Qi2 25W 已下放到「家居收纳托盘」形态，说明磁吸无线充正从数码配件转向家居产品，平板磁吸充电配件的形态可以更生活化而不必做成支架。25W 磁吸 + 19W USB-C 双路输出，值得评估平板磁吸底座的功率分配策略。",
        "terminal_relevance": "平板配件：Qi2 磁吸生态 / 多设备功率分配 / 家居化形态",
        "vendor": "Twelve South", "model": "Valet / Valet Small",
        "sources": "Notebookcheck",
        "remark": "美国 $179 / $129；英国 £179.99 / £129.99，欧洲 €189.99 / €139.99"
    },
    {
        "region": "intl", "status": "released",
        "title": "soundcore Rave 3S",
        "stars": 3, "source": "C", "date": "2026-08-07", "domain": "智能音箱",
        "url": "https://newsbytes.ph/2026/08/07/soundcore-rave-3s-uses-ai-to-turn-songs-into-karaoke-tracks/",
        "url_label": "Newsbytes.PH",
        "signal_type": "上市",
        "confirm_count": "5 个印证源",
        "key_params": "200W 便携派对音箱，AI 人声消除把任意流媒体歌曲变伴奏，随机附 2 支无线麦克风，PHP 19,995，8 月菲律宾上市",
        "tech_features": [
            "200W 输出，由 3 个全频单元 + 1 个 6.5 英寸独立低音单元构成",
            "AI Vocal Removal 实时剥离流媒体歌曲原唱人声生成伴奏，无需另找卡拉 OK 版本",
            "随机附 2 支无线麦克风；支持自定义 EQ、人声增强与混响；另有独立麦克风与吉他输入、AUX-IN",
            "节拍同步 LED 灯效；IPX4 防泼水；单次充电续航最长 12 小时"
        ],
        "why_important": "把端侧 AI 音源分离（人声消除）做成音箱主卖点，说明端侧小模型在音频设备上已有成熟落地场景，TCL 平板与音箱可评估类似的本地 AI 音频功能。随附无线麦克风 + 乐器输入的「一机多场景」打包，是提升客单价的配件组合策略。",
        "terminal_relevance": "智能音箱 / 平板音频：端侧 AI 音频 / 多场景配件打包",
        "vendor": "声阔 soundcore（安克 Anker）", "model": "soundcore Rave 3S",
        "sources": "Newsbytes.PH",
        "remark": "菲律宾 PHP 19,995，官网及 Lazada / Shopee / TikTok Shop 发售"
    },
    {
        "region": "intl", "status": "released",
        "title": "POVA AI Buds Pro",
        "stars": 4, "source": "C", "date": "2026-08-22", "domain": "AI耳机·耳穿戴",
        "url": "https://gadgets.beebom.com/news/pova-ai-buds-pro-launched-in-india-key-specs-price-sale-date",
        "url_label": "Beebom Gadgets",
        "signal_type": "开售",
        "confirm_count": "4 个印证源",
        "key_params": "48dB 混合主动降噪 TWS，8 麦克风 + VPU，机内 4 小时录音，78 语种 AI 翻译，40 小时续航，₹14,999",
        "tech_features": [
            "混合主动降噪最深 48dB，配 8 麦克风阵列 + 独立 VPU 语音拾取单元",
            "充电盒内置红色 Quick Note 实体键，可脱离手机直接启动录音并存于耳机机内，容量达 4 小时，事后与 App 同步",
            "AI 实时语音转写 + 自动生成会议摘要、行动项与待办清单；AI 翻译支持 78 种语言；支持双设备无缝切换",
            "总续航 40 小时，支持 LHDC 高解析音频，耳机盒兼用 USB-C 与 Qi 无线充电，IP55 防尘防水"
        ],
        "why_important": "把录音 / 转写 / 摘要做成耳机本体的独立闭环（机内 4 小时存储 + 盒上实体键），意味着 AI 录音硬件正从手机剥离成独立节点，TCL 平板可作为这些 AI 穿戴的记录与整理中枢。48dB ANC + 8 麦克风 + VPU 是当前 TWS 的硬件上限配置，可作为音频配件能力基线。",
        "terminal_relevance": "平板 + AI 穿戴协同：本地录音 / 端侧转写摘要 / 多语种翻译",
        "vendor": "POVA（传音 Tecno）", "model": "POVA AI Buds Pro",
        "sources": "Beebom Gadgets",
        "remark": "8/14 发布、8/22 开售；₹14,999，银行优惠后 ₹12,499"
    },
]

# ── 技术维度面板（16 维）──
DIMS = [
    ("SoC/芯片", 18, True),
    ("显示/OLED", 16, True),
    ("折叠屏", 1, True),
    ("手写笔/触控", 2, True),
    ("散热/液冷", 4, True),
    ("电池/续航", 17, True),
    ("快充/无线充", 12, True),
    ("影像", 5, True),
    ("AI/NPU", 12, True),
    ("音频/扬声器", 10, True),
    ("5G/通信", 3, True),
    ("Wi-Fi/连接", 6, True),
    ("AR/VR显示", 3, True),
    ("材质/工艺", 9, True),
    ("可持续/模块化", 2, True),
    ("手柄/外设", 2, True),
]

# ── Top5 重点信号 ──
TOP5 = [
    {"rank": 1, "title": "学而思学习机 T6 系列", "dim": "平板电脑", "stars": 5, "key": "B级 / TCL华星APEX自然光护眼屏 / SGS认证 / 12000mAh"},
    {"rank": 2, "title": "华为 MateBook Fold 非凡大师", "dim": "折叠屏", "stars": 5, "key": "B级 / 18英寸双层OLED / 40μm UTG / 1.16kg"},
    {"rank": 3, "title": "OnePlus Pad 4", "dim": "平板电脑", "stars": 5, "key": "B级 / 13.2英寸144Hz / 13380mAh / 5.9mm·672g"},
    {"rank": 4, "title": "PICO Space Pro", "dim": "AR/VR", "stars": 5, "key": "B级 / 近4000PPI Micro-OLED / 45PPD / 分体式100g"},
    {"rank": 5, "title": "Motorola Edge 70 Max", "dim": "手机", "stars": 5, "key": "B级 / 7100mAh硅碳 / 90W+25W Qi2 / 7000nits"},
]
'''

src = open(TEMPLATE, encoding="utf-8").read()

# ① 只替换模板部分（此时尚未拼接 CHUNK），避免污染 CHUNK 内的卡片日期
src = src.replace("2026-08-26", "2026-08-31")
src = src.replace('WEEK = "周三"', 'WEEK = "周一"')
src = src.replace("采集口径：7类智能终端", "采集口径：8类智能终端")
src = src.replace('<div class="stat-num">7</div>', '<div class="stat-num">8</div>')

# ③ 排序键兜底：部分卡片日期只到月（如 "2026-07"），取"日"切片为空会 int('') 报错
src = src.replace(
    '-int(c["date"][:4]), -int(c["date"][5:7]), -int(c["date"][8:10])',
    '-int(c["date"][:4]), -int(c["date"][5:7]), -int(c["date"][8:10] or "1")'
)

# ② 再注入 CARDS/DIMS/TOP5
start = src.index("CARDS = [")
end = src.index("# ── 排序：状态优先")
new_src = src[:start] + CHUNK + "\n" + src[end:]

exec(new_src)
print("DONE")
