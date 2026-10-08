# -*- coding: utf-8 -*-
# WB_gen_2026-10-08.py — 每日硬件情报看板生成器
import html, datetime

TODAY = "2026-10-08"

# ---------------- 数据：国内 15 ----------------
cn = [
{"title":"小米平板9 Pro Max发布开售：13.3英寸大屏首发自研玄戒O3芯片，4299元起",
 "category":"平板","status":"已上市","date":"2026-09-08","source_level":"B","source_name":"泡泡网",
 "stars":4,"main_dim":"手写笔/触控","signal_type":"发布/开售","corroboration":2,
 "vendor":"小米 / 小米平板9 Pro Max",
 "key_params":"13.3英寸大屏、自研玄戒O3十核全大核AI处理器、最高16GB+1TB、10000mAh+120W闪充、首销赠M-Pencil Pro触控笔",
 "tech_features":["自研玄戒O3 AI处理器(GPU提升85%/功耗降64%)","M-Pencil Pro磁吸手写笔与PC级键盘","澎湃OS 4多窗口跨设备协同"],
 "why_important":"国产自研SoC+大屏生产力平板路线，对TCL平板/学习机在芯片自主与跨端协同上有直接对标意义",
 "related":"对标华为MatePad Pro、荣耀MagicPad 4的大屏生产力平板",
 "url":"https://www.pcpop.com/common/Article_677__4_7_1.htm",
 "source_detail":"泡泡网2026-09-07报道小米秋季旗舰发布会，多家媒体同步印证",
 "note":""},
{"title":"华为MatePad Air系列登场：12英寸OLED云晰柔光屏+麒麟T93B，4499元起",
 "category":"平板","status":"已上市","date":"2026-09-07","source_level":"B","source_name":"电脑之家PChome",
 "stars":4,"main_dim":"显示/OLED","signal_type":"发布","corroboration":2,
 "vendor":"华为 / 华为MatePad Air",
 "key_params":"12英寸OLED云晰柔光屏、2.8K+144Hz+2000nits、机身5.3mm/509g、麒麟T93B处理器、10100mAh+六扬声器",
 "tech_features":["首次从LCD升级至OLED柔光屏(抗反光护眼)","幻彩珠光工艺/509g超薄机身","M-Pencil Pro与磁吸键盘生态"],
 "why_important":"中端平板首次标配OLED柔光屏，提示TCL平板在护眼OLED与书写质感上的跟进方向",
 "related":"对标荣耀MagicPad 4、小米平板9 Pro Max",
 "url":"https://article.pchome.net/n2_46/s1/1.html",
 "source_detail":"电脑之家/泡泡网2026-09-07多文报道华为全场景发布会",
 "note":""},
{"title":"荣耀MagicPad 4开售：12.1英寸165Hz绿洲护眼屏+骁龙8s Gen4，3299元起",
 "category":"平板","status":"已上市","date":"2026-09-28","source_level":"B","source_name":"荣耀官网",
 "stars":4,"main_dim":"电池/快充","signal_type":"开售","corroboration":2,
 "vendor":"荣耀 / 荣耀MagicPad 4",
 "key_params":"12.1英寸3K 165Hz LCD、第四代骁龙8s、10100mAh、六扬声器、机身6.29mm/537g、3299元起",
 "tech_features":["荣耀绿洲护眼屏(165Hz/3000×1872/700nit/DCI-P3)","第四代骁龙8s旗舰芯片+立体散热系统","MagicOS 10 PC级多窗口+无边笔记+YOYO帮记"],
 "why_important":"大电池+高刷LCD的中端定价策略，对TCL平板性价比与续航定义有参考价值",
 "related":"对标小米平板9、华为MatePad Air",
 "url":"https://www.honor.com/cn/tablets/honor-magicpad-4",
 "source_detail":"荣耀官方产品页，2026-09-28开售",
 "note":""},
{"title":"iQOO Pad Ultra首款小平板10月5日开售：8.8英寸165Hz OLED+骁龙8超级至尊版",
 "category":"平板","status":"已上市","date":"2026-10-05","source_level":"C","source_name":"网易",
 "stars":3,"main_dim":"马达/触觉","signal_type":"开售","corroboration":2,
 "vendor":"vivo / iQOO Pad Ultra",
 "key_params":"8.8英寸OLED 2304×1440 165Hz、第六代骁龙8超级至尊版、9020mAh+66W、双X轴马达、多指500Hz采样",
 "tech_features":["五重风冷散热(风扇+双VC+铜块)","双X轴线性马达+对称双扬","自研电竞芯片Q4+PC模拟器"],
 "why_important":"小尺寸游戏平板的高刷OLED+主动散热+双马达方案，对TCL游戏平板/电竞终端的触觉与散热设计有参考",
 "related":"对标联想拯救者Y700、华为MatePad Mini 2",
 "url":"https://www.163.com/dy/article/L8BT6T670531G57O.html",
 "source_detail":"网易2026-10-04报道，结合iQOO官宣",
 "note":"核心芯片为第六代骁龙8超级至尊版(2nm)，具体以发售为准"},
{"title":"小米18 Pro系列发布：首发2nm骁龙至尊版+澎湃OS 4+百变背屏，5999元起",
 "category":"手机","status":"已上市","date":"2026-09-23","source_level":"B","source_name":"中国商报",
 "stars":4,"main_dim":"SoC/芯片","signal_type":"发布","corroboration":2,
 "vendor":"小米 / 小米18 Pro",
 "key_params":"首发第六代骁龙8至尊版(2nm)、Pro与Pro Max分别搭载至尊版/超级至尊版、5999元起、国补到手5499元",
 "tech_features":["2nm制程旗舰SoC性能能效双升","澎湃OS 4+百变背屏","徕卡双两亿像素主摄+长焦"],
 "why_important":"安卓阵营2nm旗舰芯片规模化落地，对TCL手机/平板SoC选型与端侧AI能力规划有方向性参考",
 "related":"对标OPPO Find X10、vivo X500、华为Mate 90",
 "url":"https://www.toutiao.com/article/7691134592144638498/",
 "source_detail":"中国商报2026-09-30国庆新机大战综述，多家媒体印证",
 "note":""},
{"title":"OPPO Find X10系列登场：哈苏超清原相机+增距镜套装，5499元起",
 "category":"手机","status":"已上市","date":"2026-09-22","source_level":"D","source_name":"今日头条/MBPhone",
 "stars":3,"main_dim":"摄像头","signal_type":"发布","corroboration":1,
 "vendor":"OPPO / OPPO Find X10",
 "key_params":"哈苏超清原相机、增距镜套装、Find X10起售价5499元/Pro Max 6799元、部分版本搭载天玑9600 Pro",
 "tech_features":["哈苏影像+增距镜远摄","天玑9600 Pro旗舰芯片","舞台/远摄影像场景强化"],
 "why_important":"影像旗舰以哈苏+增距镜强化远摄，对TCL手机/平板摄像模组与影像算法合作有参考",
 "related":"对标小米18 Pro、vivo X500",
 "url":"https://www.toutiao.com/article/7687463500880429607",
 "source_detail":"今日头条2026-09-20 MBPhone国产旗舰定档汇总",
 "note":""},
{"title":"华为WATCH 6系列亮相：全陶瓷机身+DeepSeek大模型腕上AI+高尿酸风险评估",
 "category":"智能手表","status":"已上市","date":"2026-09-07","source_level":"B","source_name":"央广网",
 "stars":4,"main_dim":"传感器","signal_type":"发布","corroboration":1,
 "vendor":"华为 / 华为WATCH 6",
 "key_params":"Pro陶瓷白首款全陶瓷表壳+18K金表冠、Pro屏3500nits、PPG光电容积脉搏波模组首发高尿酸风险评估、DeepSeek大模型小艺",
 "tech_features":["PPG光电容积脉搏波模组无创代谢筛查","DeepSeek大模型腕上AI管家(多轮对话/翻译)","42/43/46mm三表径+eSIM独立通话"],
 "why_important":"腕上大模型+代谢类慢病无创筛查，对TCL智能穿戴在健康传感器与端侧AI场景有前瞻参考",
 "related":"对标荣耀手表6 Pro、OPPO Watch S2、Apple Watch S12",
 "url":"https://www.cnr.cn/tech/techph/20260907/t20260907_527807158.shtml",
 "source_detail":"央广网2026-09-07华为HarmonyOS 7全场景发布会",
 "note":""},
{"title":"荣耀手表6 Pro上市：行业首发心脏停搏监测+双层OLED屏+无感血压2.0，1699元起",
 "category":"智能手表","status":"已上市","date":"2026-09-28","source_level":"B","source_name":"中关村在线",
 "stars":4,"main_dim":"生物识别","signal_type":"上市","corroboration":2,
 "vendor":"荣耀 / 荣耀手表6 Pro",
 "key_params":"行业首发心脏停搏监测、双层OLED屏、无感血压2.0+ECG心电+HRV、1699元起(国补1444元)",
 "tech_features":["灵瞳感知系统无感血压出值","心脏停搏监测+主动求救","北极星定位+全天候健康监测"],
 "why_important":"将心脏停搏等危急生物识别监测下放到1699元价位，对TCL手表的生物传感与急救功能定义有压力参考",
 "related":"对标华为WATCH 6、OPPO Watch S2",
 "url":"https://smartwear.zol.com.cn/more/2_1737.shtml",
 "source_detail":"中关村在线智能穿戴频道2026-09-28报道，证券时报同步印证",
 "note":""},
{"title":"雷鸟创新RayNeo iO智能眼镜IFA开售：33克+97%透光萤火虫纳米引擎+48小时续航",
 "category":"AR-VR眼镜","status":"已上市","date":"2026-09-04","source_level":"B","source_name":"雷科技/TechPowerUp",
 "stars":4,"main_dim":"结构/工艺","signal_type":"开售","corroboration":2,
 "vendor":"雷鸟创新 / RayNeo iO",
 "key_params":"整机仅33克、0.085cc单色绿色萤火虫纳米引擎、光学透过率97%、48小时超长续航、9月4日全球开售",
 "tech_features":["33g极致轻量全天候佩戴","萤火虫纳米引擎高透光光学","连续记忆主动式AI助理(脱离手机)"],
 "why_important":"超轻量+高透光全天候AI眼镜形态，对TCL在智能眼镜结构工艺与佩戴体验上有直接对标",
 "related":"对标Rokid乐奇、Meta Ray-Ban、XREAL",
 "url":"https://headlinesbriefing.com/zh-Hans/tech/techpowerup-news/rayneo-launches-io-smart-glasses-and-gt-cinema-series-9d06337f",
 "source_detail":"TechPowerUp/雷科技2026-09-04 IFA报道，Counterpoint市占数据印证",
 "note":""},
{"title":"PICO Space Pro头显发布：micro-OLED近4000PPI+双芯片架构对标Vision Pro",
 "category":"AR-VR眼镜","status":"即将上市","date":"2026-09-02","source_level":"B","source_name":"IT之家",
 "stars":5,"main_dim":"显示/OLED","signal_type":"发布","corroboration":2,
 "vendor":"PICO / PICO Space Pro",
 "key_params":"定制micro-OLED近4000PPI(平均40PPD/核心区>45PPD)、自研协处理器+旗舰SoC双芯片(性能达XR2 Gen2两倍)、分体式设计",
 "tech_features":["micro-OLED近4000PPI超高角分辨率","双芯片架构(感知+主处理)","PICO OS 6空间计算+多窗口锚定"],
 "why_important":"国产高端XR头显以近4000PPI micro-OLED+双芯片定义空间计算，对TCL显示面板与XR终端研发有强参考",
 "related":"对标苹果Vision Pro、Meta Quest 4",
 "url":"https://www.ithome.com/0/991/578.htm",
 "source_detail":"IT之家2026-08-19/09-02报道，映维网Nweon同步印证Project Swan规格",
 "note":"开售时间与国行价格待9月2日发布会后确认"},
{"title":"华为MateBook Pro S发布：798克全球最轻14英寸+3.1K柔性OLED灵盾防窥屏",
 "category":"笔记本电脑","status":"已上市","date":"2026-08-05","source_level":"B","source_name":"华为官网",
 "stars":4,"main_dim":"结构/工艺","signal_type":"发布","corroboration":2,
 "vendor":"华为 / 华为MateBook Pro S",
 "key_params":"798g/11.9mm镁锂合金机身、14.2英寸3.1K 120Hz柔性OLED灵盾防窥屏(1600nits)、自研麒麟XE90+鸿蒙、后置摄像头扫描",
 "tech_features":["镁锂合金+微绒单涂超轻工艺","业界首款柔性OLED灵盾防窥屏(一键防窥)","鸿蒙小艺AI+跨设备碰一碰协同"],
 "why_important":"超轻镁锂合金+防窥OLED+鸿蒙生态，对TCL笔记本在轻薄结构、护眼屏与跨端协同上有标杆参考",
 "related":"对标苹果MacBook Air、荣耀MagicBook Pro 14",
 "url":"https://consumer.huawei.com:8443/cn/harmonyos-computer/matebook-pro-s",
 "source_detail":"华为官网消费者业务页，2026-08-05全场景发布会",
 "note":""},
{"title":"联想Yoga Pro 9n发布：搭载RTX Spark可本地运行1200亿参数大模型",
 "category":"笔记本电脑","status":"即将上市","date":"2026-09-04","source_level":"B","source_name":"联想官网",
 "stars":4,"main_dim":"AI/NPU","signal_type":"发布","corroboration":1,
 "vendor":"联想 / 联想Yoga Pro 9n",
 "key_params":"搭载NVIDIA RTX Spark芯片、本地运行1200亿(千亿级)参数大模型、15.3英寸2.5K 165Hz OLED、16.7mm、80W TDP",
 "tech_features":["RTX Spark本地大模型算力(1 PFLOPS FP4)","128GB统一内存跑千亿参数模型","Lenovo X Power散热压入16.7mm机身"],
 "why_important":"AI PC将大模型本地化作为核心卖点，对TCL笔记本/平板的端侧AI算力规划有直接启示",
 "related":"对标华为MateBook Pro、苹果MacBook AI版",
 "url":"https://m.lenovo.com.cn/wiki/article-49351.html",
 "source_detail":"联想官网知识库2026-09-04 IFA报道(发布时间页标注2026-10-02)",
 "note":""},
{"title":"倍思Simple Mini4 Air磁吸无线充拆解：7mm极薄+7N吸力+Qi2 15W认证",
 "category":"无线充","status":"已上市","date":"2026-09-07","source_level":"C","source_name":"充电头网",
 "stars":3,"main_dim":"认证/合规","signal_type":"拆解","corroboration":1,
 "vendor":"倍思 / Baseus Simple Mini4 Air",
 "key_params":"厚度7.04mm、重量54.9g、磁吸7N超强吸力、Qi2认证15W无线快充、型号MC10MINI3、CE/FCC认证",
 "tech_features":["官方Qi2认证磁吸无线充","7mm极薄+7N磁力随贴随充","铝合金外壳+编织线缆"],
 "why_important":"Qi2认证磁吸无线充走向极薄化，对TCL配件在无线充电标准与磁吸结构设计有合规与设计参考",
 "related":"对标绿联MagFlow、安克MagGo、moto snap",
 "url":"https://www.toutiao.com/article/7682618581946761778",
 "source_detail":"充电头网2026-09-07拆解原文，今日头条转载",
 "note":""},
{"title":"Redmi小爱触屏音箱Pro发布开售：8英寸屏+4700mAh+超级小爱大模型，499元",
 "category":"智能音箱","status":"已上市","date":"2026-09-09","source_level":"D","source_name":"XiaomiDna",
 "stars":3,"main_dim":"AI/NPU","signal_type":"开售","corroboration":1,
 "vendor":"小米 / Redmi小爱触屏音箱Pro",
 "key_params":"8英寸触摸屏、4700mAh电池(4.5h续航)、9月3日发布9月9日开售499元、内置第三代超级小爱AI",
 "tech_features":["超级小爱大模型连续对话","8英寸触屏+4700mAh可移动续航","1600+实用技能+全屋智能联动"],
 "why_important":"带屏音箱融入大模型与可移动电池，对TCL带屏音箱/智能家居中控的AI交互有参考",
 "related":"对标小度智能屏、天猫精灵CC",
 "url":"https://xiaomidna.com/news/redmi-xiaoai-touchscreen-speaker-pro-came-with-upgraded-features",
 "source_detail":"XiaomiDna 2026-09-03报道Redmi小爱触屏音箱Pro",
 "note":""},
{"title":"OPPO Enco X4发布：安卓最强AI实时翻译(24语种)+丹拿同轴双单元，千元内首销",
 "category":"AI耳机·耳穿戴","status":"已上市","date":"2026-09-22","source_level":"B","source_name":"太平洋电脑网",
 "stars":4,"main_dim":"音频","signal_type":"首销","corroboration":2,
 "vendor":"OPPO / OPPO Enco X4",
 "key_params":"6nm旗舰芯片+AI实时翻译(24种语言)、第四代丹拿同轴双单元(11mm+6mm)+双DAC、LHDC Lossless、53h续航、首销千元内",
 "tech_features":["端侧AI实时翻译(耳内播放+App文字双保障)","丹拿同轴双单元+LHDC无损传输","6nm芯片+AI降噪算法(人声降噪提升250%)"],
 "why_important":"TWS耳机以端侧AI翻译+无损音频+6nm芯片定义千元档，对TCL耳机的AI音频与声学协同有强参考",
 "related":"对标华为FreeBuds、苹果AirPods翻译、小米Buds",
 "url":"https://g.pconline.com.cn/x/2182/21825488.html",
 "source_detail":"太平洋电脑网2026-09 OPPO Enco X4报道，IT168同步印证",
 "note":""},
]

# ---------------- 数据：国际 15 ----------------
intl = [
{"title":"Samsung Galaxy Tab S12 Ultra官宣：Dimensity 9500+14.6英寸Dynamic AMOLED 2X 1600nit，10/7上市",
 "category":"平板","status":"即将上市","date":"2026-10-07","source_level":"A","source_name":"Samsung官网",
 "stars":5,"main_dim":"SoC/芯片","signal_type":"官宣","corroboration":2,
 "vendor":"Samsung / Galaxy Tab S12 Ultra",
 "key_params":"MediaTek Dimensity 9500 + 14.6英寸Dynamic AMOLED 2X 2960×1848 120Hz 1600nit + 3D Vapor Chamber + IP68 + 11600mAh 45W",
 "tech_features":["Dimensity 9500 3nm处理器(NPU提速最高61%)","14.6英寸Dynamic AMOLED 2X 1600nit","S Pen+DeX+IP68装甲铝"],
 "why_important":"旗舰平板SoC/显示/散热/手写笔标杆，对TCL平板NPU与高亮OLED方案有直接对标价值",
 "related":"竞品对标 iPad Pro M5 / 小米平板9 Pro Max",
 "url":"https://samsung.com/us/tablets/galaxy-tab-s12/",
 "source_detail":"Samsung美国官网Galaxy Tab S12系列Coming Soon页面(10/7上市)",
 "note":""},
{"title":"Samsung Galaxy Tab S12+官宣：Dimensity 9500+12.6英寸Dynamic AMOLED 2X，10/7上市",
 "category":"平板","status":"即将上市","date":"2026-10-07","source_level":"A","source_name":"TechDaily/Samsung",
 "stars":5,"main_dim":"显示/OLED","signal_type":"官宣","corroboration":2,
 "vendor":"Samsung / Galaxy Tab S12+",
 "key_params":"Dimensity 9500 + 12.6英寸Dynamic AMOLED 2X 2800×1752 120Hz 1600nit + S Pen + IP68 + 10600mAh 45W",
 "tech_features":["Dynamic AMOLED 2X高刷大屏","Super Fast Charging 45W","轻薄机身+四扬声器+S Pen"],
 "why_important":"与Ultra同代中杯方案，提供不同尺寸/价格段OLED平板参考",
 "related":"竞品对标 iPad Air M4 / 荣耀Pad 20 Pro",
 "url":"https://techdaily.com.my/samsung-galaxy-tab-s12-series",
 "source_detail":"TechDaily 2026-10-01报道S12系列(10/7马来西亚上市)",
 "note":""},
{"title":"Lenovo Yoga Tab Gen 2发布：11.1英寸4K 144Hz屏+天玑9500s+11000mAh",
 "category":"平板","status":"已上市","date":"2026-09-15","source_level":"B","source_name":"NotebookCheck",
 "stars":4,"main_dim":"显示/OLED","signal_type":"发布","corroboration":2,
 "vendor":"Lenovo / Yoga Tab Gen 2",
 "key_params":"11.1英寸4K(3840×2560)144Hz LCD 1100nit Dolby Vision、天玑9500s、11000mAh/68W、Android 17+Qira AI、起价€649",
 "tech_features":["3:2 4K 144Hz高刷LCD","联发科天玑9500s旗舰平台","Lenovo Qira AI+免费Tab Pen Pro 2"],
 "why_important":"4K高刷+大电池+AI生态，对标旗舰安卓平板，对TCL平板显示与生产力方向有参考",
 "related":"对标三星Tab S12、小米Pad 8的旗舰安卓平板",
 "url":"https://www.notebookcheck.net/Lenovo-packs-a-4K-144-Hz-display-and-11-000-mAh-battery-into-a-compact-Android-tablet.1387258.0.html",
 "source_detail":"NotebookCheck基于IFA 2026展示报道，2026年9月起上市",
 "note":""},
{"title":"荣耀 Pad X9b Max国际版发布：13英寸120Hz LCD+骁龙6s Gen2+10100mAh，已海外上市",
 "category":"平板","status":"已上市","date":"2026-09-16","source_level":"A","source_name":"NotebookCheck",
 "stars":4,"main_dim":"显示/OLED","signal_type":"发布","corroboration":1,
 "vendor":"荣耀 Honor / Pad X9b Max",
 "key_params":"13英寸120Hz LCD(2500×1560)、骁龙6s 4G Gen2、10100mAh/45W、最高6GB+256GB、MagicOS 10(Android 16)",
 "tech_features":["13英寸120Hz LCD 700nit IMAX Enhanced认证","骁龙6s 4G Gen2+RAM Turbo虚拟12GB","10100mAh电池45W快充、四扬声器DTS:X Hi-Res"],
 "why_important":"大屏低价海外平板路线(13寸+万毫安+120Hz)对TCL海外平板产品定义与定价有参考价值",
 "related":"对标三星Galaxy Tab A系列、联想Tab海外中端机型",
 "url":"https://www.notebookcheck.net/Honor-launches-13-inch-Android-tablet-with-120Hz-display-and-Snapdragon-processor.1401171.0.html",
 "source_detail":"NotebookCheck 2026-09-16报道，荣耀国际版Pad X9b Max在中东/南美/东南亚上市",
 "note":""},
{"title":"Motorola Signature 27官宣：骁龙8 Elite Extreme Gen6+2亿像素潜望+索尼Lytia 910+B&O音频",
 "category":"手机","status":"即将上市","date":"2026-09-23","source_level":"B","source_name":"The Verge",
 "stars":4,"main_dim":"摄像头","signal_type":"官宣","corroboration":2,
 "vendor":"Motorola / Signature 27",
 "key_params":"骁龙8 Elite Extreme Gen6+2亿像素潜望长焦+5000万主摄(索尼Lytia 910 LOFIC)+B&O调音",
 "tech_features":["首发高通骁龙8 Elite Extreme Gen6","索尼LOFIC Lytia 910主摄，17档动态范围","2亿像素潜望式长焦+Bang&Olufsen音频"],
 "why_important":"旗舰影像传感器(LOFIC高动态)与厂商品牌音频合作模式值得关注",
 "related":"竞品对标 Galaxy S26 Ultra / 小米18 Pro",
 "url":"https://theverge.com/998844/motorola-signature-27-specs-snapdragon-8-elite-extreme-gen-6",
 "source_detail":"The Verge官宣报道，明确芯片、主摄传感器、长焦与B&O合作",
 "note":"完整规格/价格/日期待年底全球发布补充"},
{"title":"Apple iPhone 18 Pro发布：A20 Pro芯片+4800万可变光圈主摄+钛/铝机身",
 "category":"手机","status":"已上市","date":"2026-09-09","source_level":"A","source_name":"Apple Newsroom",
 "stars":5,"main_dim":"摄像头","signal_type":"发布","corroboration":2,
 "vendor":"Apple / iPhone 18 Pro",
 "key_params":"A20 Pro芯片; 6.3英寸120Hz超视网膜XDR OLED(2622×1206,3000nit); 4800万可变光圈主摄; 60W有线/15W无线; 钛金属+超瓷晶盾2",
 "tech_features":["A20 Pro新一代芯片+VC均热板","4800万像素融合主摄可变光圈","新一代Apple Intelligence/Siri AI"],
 "why_important":"TCL手机影像与旗舰SoC预研对标：可变光圈主摄与端侧AI是2026旗舰核心方向",
 "related":"对标三星Galaxy S26 Ultra、Pixel 11的旗舰影像方案",
 "url":"https://nr.apple.com/Dl1b9K0uH9",
 "source_detail":"Apple官方新闻稿，2026-09-09发布，9-12预售、9-18发售",
 "note":""},
{"title":"Samsung Galaxy Watch Ultra2发布：钛金属+IP69K+10ATM+首创40%快充",
 "category":"智能手表","status":"已上市","date":"2026-09-10","source_level":"A","source_name":"Samsung官网",
 "stars":5,"main_dim":"结构/工艺","signal_type":"官宣","corroboration":2,
 "vendor":"Samsung / Galaxy Watch Ultra2",
 "key_params":"钛金属表壳+IP69K+10ATM+EN13319+首搭Galaxy Watch 40%快充(30分钟)",
 "tech_features":["钛金属机身","IP69K+10ATM潜水级防护","首创手表40%快充(约30分钟)+双频GPS+蓝宝石玻璃"],
 "why_important":"高端运动手表防护与快充标杆，对TCL手表三防/充电策略参考",
 "related":"竞品对标 Garmin Enduro 4 / 华为WATCH Ultimate",
 "url":"https://samsung.com/ph/watches/galaxy-watch/galaxy-watch-ultra2-titanium-silver-lte-sm-l715fzsaxtc/buy",
 "source_detail":"Samsung菲律宾官网Galaxy Watch Ultra2购买页，列明材质、防护与快充",
 "note":""},
{"title":"Garmin fēnix 9 / fēnix 9 Pro发布：首款全钛表壳+1.5英寸3000nit AMOLED+inReach卫星",
 "category":"智能手表","status":"已上市","date":"2026-08-25","source_level":"A","source_name":"Garmin Newsroom",
 "stars":5,"main_dim":"传感器","signal_type":"发布","corroboration":2,
 "vendor":"Garmin / fēnix 9 / fēnix 9 Pro",
 "key_params":"全钛金属表壳(Pro)、1.5英寸3000nit AMOLED(466×466)、inReach卫星/LTE、64GB、51mm续航31天(太阳能57天)、$999.99/$1099.99起",
 "tech_features":["inReach卫星通讯+LTE独立通话/SOS","Garmin Epic多日活动串联","50%更多RAM+30%更快地图导航"],
 "why_important":"TCL手表户外与长续航方向：钛金属轻量化+卫星通讯+太阳能，旗舰运动表标杆",
 "related":"竞品对标 Apple Watch Ultra2、三星Galaxy Watch Ultra2",
 "url":"https://www.garmin.com/en-CA/blog/news/garmin-expands-its-flagship-performance-smartwatch-lineup-with-fenix9-and-fenix9-pro",
 "source_detail":"Garmin官方新闻稿2026-08-25，8-28开启订购",
 "note":""},
{"title":"Meta VR Glasses发布：100g分体式+骁龙Reality Elite+5K micro-OLED，Connect 2026",
 "category":"AR-VR眼镜","status":"即将上市","date":"2026-09-24","source_level":"B","source_name":"The Verge",
 "stars":5,"main_dim":"显示/OLED","signal_type":"发布","corroboration":2,
 "vendor":"Meta / VR Glasses",
 "key_params":"100g眼镜+口袋计算坞(骁龙Reality Elite/12GB/128GB)+5K micro-OLED 2412×2288/眼 120Hz+$1299",
 "tech_features":["分体式口袋计算坞(非头带)","单眼5K micro-OLED 120Hz IMAX Enhanced认证","重量仅100g(约Quest3 1/5)"],
 "why_important":"轻量化VR新形态与分体算力架构，对TCL XR/眼镜形态与散热取舍有强参考",
 "related":"竞品对标 Apple Vision Pro / XREAL Aura",
 "url":"https://theverge.com/tech/999517/meta-vr-glasses-connect-2026-hands-on",
 "source_detail":"The Verge Connect 2026上手报道+发布汇总，含重量、芯片、分辨率、价格",
 "note":"2027春季上市"},
{"title":"三星×谷歌 Android XR 智能眼镜过FCC认证：SM-O200J/Gentle Monster 与 SM-O200P/Warby Parker",
 "category":"AR-VR眼镜","status":"进行中","date":"2026-09-30","source_level":"A","source_name":"Android Authority",
 "stars":5,"main_dim":"AI/NPU","signal_type":"认证","corroboration":2,
 "vendor":"三星 Samsung / 型号 SM-O200J、SM-O200P",
 "key_params":"双型号SM-O200J(Gentle Monster)、SM-O200P(Warby Parker)，各4-5个变体，安卓XR+Gemini",
 "tech_features":["安卓XR平台+Gemini AI助手","与Gentle Monster/Warby Parker联名时尚镜框","FCC认证多变种(共9个型号)"],
 "why_important":"三星+谷歌安卓XR眼镜量产在即，是Meta Ray-Ban之外最重磅的AI眼镜竞品，对TCL智能眼镜/音频眼镜预研有对标意义",
 "related":"对标Meta Ray-Ban、Snap Specs；TCL可关注音频+AI眼镜路线",
 "url":"https://www.androidauthority.com/samsungs-smart-glasses-stop-by-fcc-3717548/",
 "source_detail":"Android Authority 2026-09-30，引用Droid Life发现的FCC文件",
 "note":"另有Smart Glasses Daily 2026-10-02跟进，预计年内发布"},
{"title":"Acer Swift Blade 14发布：799g碳纤维+英特尔Wildcat Lake+OLED可选",
 "category":"笔记本电脑","status":"即将上市","date":"2026-09-02","source_level":"B","source_name":"The Verge",
 "stars":4,"main_dim":"结构/工艺","signal_type":"发布","corroboration":1,
 "vendor":"Acer / Swift Blade 14",
 "key_params":"799g/12.95mm+碳纤维顶盖底盖+英特尔Wildcat Lake(最高Core7 350)+OLED可选",
 "tech_features":["碳纤维顶盖与底板实现799g轻量","0.51英寸(12.95mm)超薄","可选2880×1800/90Hz OLED 400nit"],
 "why_important":"轻薄本碳纤维工艺与低功耗x86平台，对TCL笔记本轻量化设计参考",
 "related":"竞品对标 MacBook Air / LG Gram",
 "url":"https://theverge.com/gadgets/987802/acer-swift-blade-14-air-16-laptop-ifa-price-specs",
 "source_detail":"The Verge IFA 2026报道，明确重量、材质、处理器与屏幕选项",
 "note":"12月北美上市，定价未公布"},
{"title":"联想 ThinkBook 14 Gen 9 发布骁龙X2 Plus版：50Wh电池+32GB LPDDR5x，10月上市$1299",
 "category":"笔记本电脑","status":"即将上市","date":"2026-09-03","source_level":"A","source_name":"NotebookCheck",
 "stars":4,"main_dim":"SoC/芯片","signal_type":"发布","corroboration":1,
 "vendor":"联想 Lenovo / ThinkBook 14 Gen 9 (Snapdragon X2 Plus)",
 "key_params":"骁龙X2 Plus(25W TDP)、最高32GB LPDDR5x-9523、1TB SSD(可扩展)、50Wh、14寸WUXGA、10月上市$1299",
 "tech_features":["高通骁龙X2 Plus ARM处理器(单核/多核/NPU提升)","50Wh电池较Intel版增大、双M.2 SSD槽","Wi-Fi 7、14寸WUXGA IPS 400nit、1.3kg"],
 "why_important":"骁龙X2 Plus进入主流商务本，ARM Copilot+ PC生态成熟信号，对TCL笔记本芯片选型与续航设计有参考",
 "related":"对标Surface Laptop、戴尔XPS ARM版；TCL笔记本可跟进X2平台",
 "url":"https://www.notebookcheck.net/New-Lenovo-ThinkBook-14-Gen-9-laptop-launches-with-bigger-battery-and-new-SoC.1387282.0.html",
 "source_detail":"NotebookCheck 2026-09-03 IFA 2026报道",
 "note":""},
{"title":"Motorola Moto Snap Qi2磁吸充电宝：25W Qi2+5000mAh，€39.99欧洲上市",
 "category":"无线充","status":"已上市","date":"2026-09-10","source_level":"B","source_name":"The Verge (IFA 2026)",
 "stars":4,"main_dim":"电池/快充","signal_type":"发布","corroboration":1,
 "vendor":"Motorola / Moto Snap Qi2",
 "key_params":"25W Qi2磁吸无线充+5000mAh+USB-C 20W+折叠支架+€39.99",
 "tech_features":["Qi2磁吸对齐25W无线输出","5000mAh电芯，USB-C有线20W","内置可折叠支架"],
 "why_important":"Qi2磁吸移动电源形态与25W功率趋势，对TCL无线充/配件规划参考",
 "related":"竞品对标 三星磁吸电池包 / 绿联折叠无线充",
 "url":"http://theverge.com/ifa-berlin/archives/2?t=1661663481186/archives/",
 "source_detail":"The Verge IFA 2026滚动报道明确Moto Snap Qi2 puck 25W与价格上市日",
 "note":"仅欧洲上市"},
{"title":"苹果 HomePod mini 2 曝光：代码泄露五配色，新芯片+Siri AI，预计10月发布",
 "category":"智能音箱","status":"进行中","date":"2026-09-25","source_level":"B","source_name":"Frandroid",
 "stars":4,"main_dim":"AI/NPU","signal_type":"曝光","corroboration":2,
 "vendor":"苹果 Apple / HomePod mini 2",
 "key_params":"球形织物外观不变、五配色(新增绿/粉/蓝)、新S系列芯片、Siri AI(Linwood)、预计2026-10发布",
 "tech_features":["新处理器支持Siri AI(Linwood)本地智能","五配色含三种全新色(绿/粉/蓝)","保留Thread/Matter智能家居、360度声场"],
 "why_important":"HomePod mini 2是苹果6年来首次小音箱更新，Siri AI+智能家居入口，对TCL智能音箱/AI音箱语音交互设计有对标价值",
 "related":"对标亚马逊Echo、谷歌Nest Audio；TCL音箱可强化AI语音",
 "url":"https://www.frandroid.com/marques/3261839_homepod-mini-2-une-fuite-confirme-cinq-coloris-dont-trois-inedits",
 "source_detail":"Frandroid 2026-09-25，引用MacRumors Aaron Perris在苹果代码中发现",
 "note":"苹果代码泄露，尚未官宣；预计2026年10月随Apple TV 4K等一同发布"},
{"title":"Samsung Galaxy Buds On发布：首款夹耳开放式耳机+Gemini Live+头控",
 "category":"AI耳机·耳穿戴","status":"即将上市","date":"2026-10-01","source_level":"B","source_name":"SamMobile",
 "stars":4,"main_dim":"AI/NPU","signal_type":"官宣","corroboration":2,
 "vendor":"Samsung / Galaxy Buds On",
 "key_params":"夹耳开放式不入耳; 骁龙S7 Gen1 Sound; 9.5h续航; Gemini Live+头控; 299,000韩元; 10-27韩国首发",
 "tech_features":["Gemini Live免唤醒对话","头部手势接听/拒接/查看通知","TwinBoost扬声器+漏音抑制+三麦骨传导通话降噪"],
 "why_important":"TCL耳机AI交互范式：把Gemini等大模型语音助手嵌入开放式耳机，头控免手操作",
 "related":"对标Bose Ultra Open、Sony LinkBuds Clip、华为FreeClip",
 "url":"https://www.sammobile.com/news/galaxy-buds-on-official-samsung-first-clip-on-earbuds/",
 "source_detail":"SamMobile 2026-10-01，同期EDAILY/Beebom报道，韩国10-27上市",
 "note":""},
]

# ---------------- 维度统计 ----------------
DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺","传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]
dim_count = {d:0 for d in DIMS}
for it in cn+intl:
    dim_count[it["main_dim"]] += 1
covered = sum(1 for d in DIMS if dim_count[d] > 0)

def date_key(d):
    p = d.split("-")
    if len(p)==3: return int(p[0])*10000+int(p[1])*100+int(p[2])
    return int(p[0])*10000+int(p[1])*100

STATUS_RANK = {"即将上市":0,"进行中":1,"已上市":2}
def sort_key(it):
    return (STATUS_RANK[it["status"]], -date_key(it["date"]))

cn_sorted = sorted(cn, key=sort_key)
intl_sorted = sorted(intl, key=sort_key)
all_items = cn_sorted + intl_sorted

CIRCLED = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩"]
def stars(s): return "★"*s + "☆"*(5-s)
def esc(x): return html.escape(str(x), quote=True)

SRC_CLASS = {"A":"source-a","B":"source-b","C":"source-c","D":"source-d","E":"source-e"}
REG_CLASS = {"国内":"region-cn","国际":"region-intl"}

def status_tag(status):
    if status=="即将上市": return '<span class="status-tag status-coming">即将上市</span>'
    if status=="进行中": return '<span class="status-tag status-progress">进行中</span>'
    return ""

CSS = '''  <style>
  :root {
    --bg: #f5f7fa; --card-bg: #fff; --border: #e4e7ed;
    --text: #303133; --text-secondary: #606266; --text-tertiary: #909399;
    --primary: #409eff; --success: #67c23a; --warning: #e6a23c; --danger: #f56c6c; --info: #909399;
    --tag-a: #67c23a; --tag-b: #409eff; --tag-c: #e6a23c; --tag-d: #f56c6c; --tag-e: #aa55ff;
    --shadow: 0 2px 12px rgba(0,0,0,0.06); --shadow-hover: 0 4px 20px rgba(0,0,0,0.1); --radius: 10px;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--text); line-height:1.6; padding:20px; }
  .container { max-width:1200px; margin:0 auto; }
  .header { background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:#fff; border-radius:var(--radius); padding:28px 32px; margin-bottom: 20px; box-shadow:var(--shadow); }
  .header h1 { font-size:24px; margin-bottom:8px; }
  .header .subtitle { font-size:14px; opacity:0.9; }
  .header .meta { display:flex; gap:12px; margin-top:14px; flex-wrap:wrap; }
  .meta-badge { background:rgba(255,255,255,0.2); border:1px solid rgba(255,255,255,0.3); border-radius:20px; padding:4px 14px; font-size:13px; }
  .stats-bar { display:flex; gap:16px; margin-bottom:24px; flex-wrap:wrap; }
  .stat-item { background:var(--card-bg); border-radius:var(--radius); padding:14px 20px; box-shadow:var(--shadow); flex:1; min-width:140px; text-align:center; }
  .stat-num { font-size:22px; font-weight:700; color:var(--primary); }
  .stat-label { font-size:12px; color:var(--text-tertiary); margin-top:4px; }
  .dim-panel { background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }
  .dim-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }
  .dim-title { font-size:16px; font-weight:700; display:flex; align-items:center; gap:8px; }
  .dim-title::before { content:''; width:4px; height:18px; background:var(--success); border-radius:2px; }
  .dim-counter { font-size:14px; color:var(--text-secondary); }
  .dim-counter .dim-num { font-size:18px; font-weight:600; color:var(--success); }
  .dim-counter .dim-total { color:var(--text-tertiary); }
  .dim-bar { width:100%; height:8px; background:#f0f2f5; border-radius:4px; margin-bottom:16px; overflow:hidden; }
  .dim-bar-fill { height:100%; background:linear-gradient(90deg,#67c23a,#95d475); border-radius: 4px; transition:width 0.5s; }
  .dim-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
  .dim-chip { padding:8px 12px; border-radius:8px; font-size:13px; font-weight:500; display:flex; justify-content:space-between; align-items:center; }
  .dim-chip.on { background:#f0f9eb; border:1px solid #c2e7b0; color:#67c23a; }
  .dim-chip.off { background:#f5f7fa; border:1px solid #e4e7ed; color:#c0c4cc; }
  .dim-chip .dim-count { font-size:11px; opacity:0.7; font-weight:400; }
  .summary-section { background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }
  .section-title { font-size:16px; font-weight:700; margin-bottom:14px; display:flex; align-items:center; gap:8px; }
  .section-title::before { content:''; width:4px; height:18px; background:var(--primary); border-radius:2px; }
  table { width:100%; border-collapse:collapse; font-size:13px; }
  thead th { background:#f0f2f5; padding:10px 12px; text-align:left; font-weight:600; color:var(--text-secondary); border-bottom:2px solid var(--border); white-space:nowrap; }
  tbody td { padding:10px 12px; border-bottom:1px solid var(--border); vertical-align:top; }
  tbody tr:hover { background:#f5f7fa; }
  tbody tr:last-child td { border-bottom:none; }
  .td-title { font-weight:600; color:var(--text); }
  .td-region { font-size:12px; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; }
  .region-cn { background:#ecf5ff; color:#409eff; }
  .region-intl { background:#fdf6ec; color:#e6a23c; }
  .source-tag { display:inline-block; font-size:12px; font-weight:700; padding:2px 10px; border-radius:12px; white-space:nowrap; }
  .source-a { background:#f0f9eb; color:var(--tag-a); border:1px solid #c2e7b0; }
  .source-b { background:#ecf5ff; color:var(--tag-b); border:1px solid #b3d8ff; }
  .source-c { background:#fdf6ec; color:var(--tag-c); border:1px solid #f5dab1; }
  .source-d { background:#fef0f0; color:var(--tag-d); border:1px solid #fbc4c4; }
  .source-e { background:#f3f0ff; color:var(--tag-e); border:1px solid #d3c2ff; }
  .status-tag { display:inline-block; font-size:11px; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; margin-left:8px; }
  .td-status .status-tag { margin-left:0; font-size:10px; padding:1px 6px; }
  .status-coming { background:#ecf5ff; color:#409eff; border:1px solid #b3d8ff; }
  .status-released { background:#f0f9eb; color:#67c23a; border:1px solid #c2e7b0; }
  .status-progress { background:#ecf5ff; color:#409eff; border:1px solid #b3d8ff; }
  .intel-section { margin-bottom:24px; }
  .intel-cards { display:grid; grid-template-columns:1fr; gap:16px; }
  .intel-card { background:var(--card-bg); border-radius:var(--radius); box-shadow:var(--shadow); overflow:hidden; transition:box-shadow 0.3s; border-left:4px solid var(--primary); }
  .intel-card.cn { border-left-color:var(--tag-b); }
  .intel-card.intl { border-left-color:var(--tag-c); }
  .intel-card:hover { box-shadow:var(--shadow-hover); }
  .card-header { padding:16px 20px; cursor:pointer; display:flex; align-items:flex-start; gap:12px; user-select:none; }
  .card-num { flex-shrink:0; width:28px; height:28px; border-radius:50%; background:#f0f2f5; color:var(--text-secondary); font-size:13px; font-weight:700; display:flex; align-items:center; justify-content:center; margin-top:2px; }
  .intel-card.cn .card-num { background:#ecf5ff; color:var(--tag-b); }
  .intel-card.intl .card-num { background:#fdf6ec; color:var(--tag-c); }
  .card-title-area { flex:1; }
  .card-title { font-size:15px; font-weight:600; color:var(--text); margin-bottom:6px; }
  .card-badges { display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
  .card-badges .stars { font-size:12px; color:var(--warning); letter-spacing:1px; }
  .card-domain { font-size:12px; color:var(--text-tertiary); background:#f5f7fa; padding:2px 8px; border-radius:4px; }
  .card-toggle { flex-shrink:0; color:var(--text-tertiary); font-size:14px; transition:transform 0.3s; margin-top:4px; }
  .intel-card.expanded .card-toggle { transform:rotate(180deg); }
  .card-body { max-height:0; overflow:hidden; transition:max-height 0.4s ease; }
  .intel-card.expanded .card-body { max-height:3000px; }
  .card-content { padding:0 20px 18px 20px; border-top:1px solid var(--border); padding-top:16px; }
  .field-grid { display:grid; grid-template-columns:1fr 1fr; gap:12px 20px; }
  .field { display:flex; flex-direction:column; gap:4px; }
  .field.full { grid-column:1 / -1; }
  .field-label { font-size:12px; font-weight:600; color:var(--text-tertiary); letter-spacing:0.5px; }
  .field-value { font-size:13px; color:var(--text-secondary); line-height:1.7; }
  .field-value a { color:var(--primary); text-decoration:none; word-break:break-all; }
  .field-value a:hover { text-decoration:underline; }
  .field-value .tech-list { padding-left:0; list-style:none; }
  .field-value .tech-list li { padding:2px 0; padding-left:18px; position:relative; }
  .field-value .tech-list li::before { content:attr(data-num); position:absolute; left:0; font-weight:700; color:var(--primary); }
  @media (max-width:768px) { .field-grid { grid-template-columns:1fr; } .dim-grid { grid-template-columns:repeat(2,1fr); } table { font-size:12px; } thead th,tbody td { padding:8px 6px; } }
  html { scroll-behavior: smooth; }
  .td-title a { color: inherit; text-decoration: none; }
  .td-title a:hover { color: var(--primary); text-decoration: underline; }
  .top-signals-panel { background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }
  .top-signals-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }
  .top-signals-title { font-size:16px; font-weight:700; display:flex; align-items:center; gap:8px; }
  .top-signals-title::before { content:''; width:4px; height:18px; background:var(--warning); border-radius:2px; }
  .top-signals-grid { display:grid; grid-template-columns:repeat(5,1fr); gap:12px; }
  .signal-card { background:linear-gradient(135deg,#f5f7fa,#fafafa); border-radius:8px; padding:12px 14px; border-left:3px solid var(--success); transition:box-shadow 0.3s; }
  .signal-card:hover { box-shadow:var(--shadow-hover); }
  .signal-card .sig-rank { display:inline-block; font-size:11px; font-weight:700; color:#fff; background:var(--success); border-radius:50%; width:18px; height:18px; text-align:center; line-height:18px; margin-right:6px; }
  .signal-card .sig-title { font-size:13px; font-weight:600; color:var(--text); line-height:1.4; }
  .signal-card .sig-tags { display:flex; gap:4px; flex-wrap:wrap; margin-bottom:4px; margin-top:6px; }
  .signal-card .sig-dim { font-size:11px; background:#f0f9eb; color:#67c23a; border-radius:4px; padding:1px 6px; }
  .signal-card .sig-stars { font-size:12px; color:#e6a23c; }
  .signal-card .sig-key { font-size:11px; color:var(--text-secondary); line-height:1.5; margin-top:4px; }
  </style>'''

def card_html(it, idx, region):
    cid = "card-%d" % idx
    exp = " expanded" if idx==1 else ""
    cls = "intel-card cn"+exp if region=="国内" else "intel-card intl"+exp
    badges = '<span class="source-tag %s">%s</span><span class="sig-dim" style="background:#f0f9eb;color:#67c23a;border-radius:4px;padding:1px 6px;font-size:11px;">%s</span><span class="stars">%s</span>%s' % (
        SRC_CLASS[it["source_level"]], it["source_level"], esc(it["main_dim"]), stars(it["stars"]), status_tag(it["status"]))
    tech = "".join('<li data-num="%s">%s</li>' % (CIRCLED[i], esc(t)) for i,t in enumerate(it["tech_features"]))
    url_a = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(it["url"]), esc(it["url"]))
    fields = []
    fields.append(('<div class="field"><div class="field-label">信号类型</div><div class="field-value">%s</div></div>' % esc(it["signal_type"])))
    fields.append(('<div class="field"><div class="field-label">印证源数</div><div class="field-value">%d 个独立信源</div></div>' % it["corroboration"]))
    fields.append(('<div class="field"><div class="field-label">主技术维度</div><div class="field-value">%s</div></div>' % esc(it["main_dim"])))
    fields.append(('<div class="field"><div class="field-label">区域</div><div class="field-value">%s</div></div>' % esc(region)))
    fields.append(('<div class="field"><div class="field-label">厂商/型号</div><div class="field-value">%s</div></div>' % esc(it["vendor"])))
    fields.append(('<div class="field"><div class="field-label">时间</div><div class="field-value">%s</div></div>' % esc(it["date"])))
    fields.append(('<div class="field"><div class="field-label">信源等级</div><div class="field-value">%s 级 — %s</div></div>' % (it["source_level"], esc(it["source_name"]))))
    fields.append(('<div class="field"><div class="field-label">信源明细</div><div class="field-value">%s</div></div>' % esc(it["source_detail"])))
    fields.append(('<div class="field full"><div class="field-label">关键参数</div><div class="field-value">%s</div></div>' % esc(it["key_params"])))
    fields.append(('<div class="field full"><div class="field-label">技术特性</div><div class="field-value"><ul class="tech-list">%s</ul></div></div>' % tech))
    fields.append(('<div class="field full"><div class="field-label">为什么重要</div><div class="field-value">%s</div></div>' % esc(it["why_important"])))
    fields.append(('<div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">%s</div></div>' % esc(it["related"])))
    fields.append(('<div class="field full"><div class="field-label">来源 URL</div><div class="field-value">%s</div></div>' % url_a))
    fields.append(('<div class="field full"><div class="field-label">备注待印证</div><div class="field-value">%s</div></div>' % esc(it["note"] if it["note"] else "—")))
    return '      <div class="%s" id="%s">\n        <div class="card-header" onclick="toggleCard(\'%s\')">\n          <div class="card-num">%d</div>\n          <div class="card-title-area">\n            <div class="card-title">%s</div>\n            <div class="card-badges">%s</div>\n          </div>\n          <div class="card-toggle">▼</div>\n        </div>\n        <div class="card-body"><div class="card-content">\n          <div class="field-grid">\n          %s\n          </div>\n        </div></div>\n      </div>' % (cls, cid, cid, idx, esc(it["title"]), badges, "".join(fields))

# Top5 排序：星级降序→信源等级升序(A<B<C<D<E)→状态优先(即将上市>进行中>已上市)→时间倒序
SRC_RANK = {"A":0,"B":1,"C":2,"D":3,"E":4}
def top_key(it):
    return (-it["stars"], SRC_RANK[it["source_level"]], STATUS_RANK[it["status"]], -date_key(it["date"]))
top5 = sorted(cn+intl, key=top_key)[:5]

def top_html():
    out=[]
    for i,t in enumerate(top5,1):
        out.append('            <div class="signal-card">\n        <div><span class="sig-rank">%d</span><span class="sig-title">%s</span></div>\n        <div class="sig-tags"><span class="sig-dim">%s</span><span class="sig-stars">%s</span></div>\n        <div class="sig-key">%s级 / %s</div>\n      </div>' % (i, esc(t["title"]), esc(t["main_dim"]), stars(t["stars"]), t["source_level"], esc(t["key_params"])))
    return "\n".join(out)

def summary_rows():
    out=[]
    for i,it in enumerate(all_items,1):
        region = "国内" if i<=len(cn_sorted) else "国际"
        st = status_tag(it["status"])
        st_cell = '<td class="td-status">%s</td>' % (st if st else '<span style="color:#c0c4cc;">已上市</span>')
        out.append('            <tr>\n        <td>%d</td>\n        <td class="td-title"><a href="#card-%d">%s</a></td>\n        <td><span class="td-region %s">%s</span></td>\n        <td>%s</td>\n        <td><span class="source-tag %s">%s</span></td>\n        %s\n        <td>%s</td>\n        <td><span class="stars">%s</span></td>\n      </tr>' % (
            i, i, esc(it["title"]), REG_CLASS[region], region, esc(it["category"]), SRC_CLASS[it["source_level"]], it["source_level"], st_cell, esc(it["date"]), stars(it["stars"])))
    return "\n".join(out)

def dim_chips():
    out=[]
    for d in DIMS:
        c = dim_count[d]
        if c>0:
            out.append('<div class="dim-chip on">%s <span class="dim-count">%d条</span></div>' % (esc(d), c))
        else:
            out.append('<div class="dim-chip off">%s <span class="dim-count">0条</span></div>' % esc(d))
    return "\n      ".join(out)

A = sum(1 for it in cn+intl if it["source_level"]=="A")
B = sum(1 for it in cn+intl if it["source_level"]=="B")
C = sum(1 for it in cn+intl if it["source_level"]=="C")
D = sum(1 for it in cn+intl if it["source_level"]=="D")
five = sum(1 for it in cn+intl if it["stars"]==5)
cats = len(set(it["category"] for it in cn+intl))

html_doc = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>智能终端硬件情报日报 · %s</title>
%s
</head>
<body>
<div class="container">
  <div class="header">
    <h1>智能终端硬件情报日报 · %s</h1>
    <div class="subtitle">采集口径：8类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑/AI耳机·耳穿戴） | 搜索窗口60天 | 国内15条 + 国际15条</div>
    <div class="meta">
      <span class="meta-badge">总情报 30条</span>
      <span class="meta-badge">国内 15条</span>
      <span class="meta-badge">国际 15条</span>
      <span class="meta-badge">信源 A-E级</span>
      <span class="meta-badge">搜索窗口 60天</span>
    </div>
  </div>
  <div class="stats-bar">
    <div class="stat-item"><div class="stat-num">30</div><div class="stat-label">总情报数</div></div>
    <div class="stat-item"><div class="stat-num">%d</div><div class="stat-label">A级信源</div></div>
    <div class="stat-item"><div class="stat-num">%d</div><div class="stat-label">B级信源</div></div>
    <div class="stat-item"><div class="stat-num">%d</div><div class="stat-label">覆盖产品类别</div></div>
    <div class="stat-item"><div class="stat-num">%d</div><div class="stat-label">五星条数</div></div>
  </div>
  <div class="dim-panel">
    <div class="dim-header">
      <div class="dim-title">技术维度覆盖面板</div>
      <div class="dim-counter"><span class="dim-num">%d</span><span class="dim-total"> / 16 维度</span></div>
    </div>
    <div class="dim-bar"><div class="dim-bar-fill" style="width:%d%%"></div></div>
    <div class="dim-grid">
      %s
    </div>
  </div>
  <div class="top-signals-panel">
    <div class="top-signals-header">
      <div class="top-signals-title">今日重点信号 Top 5</div>
      <div style="font-size:12px;color:var(--text-tertiary);">排序：星级降序→A级优先→状态优先→时间倒序</div>
    </div>
    <div class="top-signals-grid">
%s
    </div>
  </div>
  <div class="summary-section">
    <div class="section-title">情报摘要表</div>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>类别</th><th>信源</th><th>状态</th><th>时间</th><th>重要度</th></tr></thead>
      <tbody>
%s
      </tbody>
    </table>
  </div>
  <div class="intel-section">
    <div class="section-title">一、国内情报（15条）</div>
    <div class="intel-cards">
%s
    </div>
  </div>
  <div class="intel-section">
    <div class="section-title">二、国际情报（15条）</div>
    <div class="intel-cards">
%s
    </div>
  </div>
</div>
<script>
function toggleCard(id) {
  var el = document.getElementById(id);
  if (el.classList.contains('expanded')) el.classList.remove('expanded');
  else el.classList.add('expanded');
}
</script>
</body>
</html>''' % (TODAY, CSS, TODAY, A, B, cats, five, covered, int(round(covered/16*100)), dim_chips(), top_html(), summary_rows(),
       "\n".join(card_html(it,i,"国内") for i,it in enumerate(cn_sorted,1)),
       "\n".join(card_html(it,i,"国际") for i,it in enumerate(intl_sorted,len(cn_sorted)+1)))

out_path = "E:/AI相关/预研究/202608/03_输出/WB_%s_硬件看板.html" % TODAY
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_doc)
print("OK written:", out_path)
print("A=%d B=%d C=%d D=%d 5star=%d cats=%d dim_cov=%d/16" % (A,B,C,D,five,cats,covered))
print("CN status order:", [it["status"] for it in cn_sorted])
print("INTL status order:", [it["status"] for it in intl_sorted])
