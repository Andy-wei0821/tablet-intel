# -*- coding: utf-8 -*-
# Generator for WB_2026-09-29_硬件看板.html
# Single HTML, inline CSS, no CDN. 30 cards (CN15 + INTL15).
import datetime

DATE = "2026-09-29"
TITLE = "智能终端硬件情报日报 · " + DATE

DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

ITEMS = [
 # ---------- CN (1-15) ----------
 {"region":"国内","title":"荣耀平板 X10 Pro Max 开售：13 英寸 120Hz + 骁龙 6s + 10100mAh，2599 元","category":"平板","dim":"显示/OLED","status":"已上市","date":"2026-09","source_tier":"A","source_name":"荣耀商城","url":"https://www.honor.com/cn/shop/product/10086835939850.html?cid=899176","corroboration":1,"stars":4,"vendor":"荣耀 Honor","signal_type":"新品开售","key_params":"13 英寸 2500×1560 120Hz LCD；第二代骁龙 6s 4G；8+128GB；10100mAh+45W；MagicOS 10；618g/6.72mm；到手 1899 元（原价 2599）","tech_features":["13 英寸 120Hz LCD 护眼大屏","第二代骁龙 6s 4G 平台","10100mAh 青海湖电池+45W 超级快充","MagicOS 10（Android 16）","四扬声器杜比音效","莱茵低蓝光认证","微边全面屏 88% 屏占比"],"why_important":"荣耀中端大屏平板补齐 10000mAh 级续航，以 2599 元（到手 1899）切入教育/影音市场，对标同档国产平板。","terminal_link":"对标 TCL 平板 NXTPAPER 系列（护眼大屏/教育定位），作为 TCL 在 1000-3000 元档的竞品基准。","note":"去重表含 MagicPad 4/Pad X9b Max 等荣耀其他型号，本款 X10 Pro Max 不冲突。"},

 {"region":"国内","title":"联想小新平板 11 上市：11 英寸 2.5K 护眼屏 + 天玑 6300 + 手写笔套装，1299 元","category":"平板","dim":"手写笔/触控","status":"已上市","date":"2026-09-10","source_tier":"A","source_name":"联想官方商城","url":"https://m.lenovo.com.cn/wiki/product-doc-46425.html","corroboration":1,"stars":3,"vendor":"联想 Lenovo","signal_type":"新品开售","key_params":"11 英寸 2560×1600 2.5K；天玑 6300；8+128/256GB；7040mAh；金属机身 6.99mm/480g；四扬声器杜比；1299 元","tech_features":["11 英寸 2.5K 护眼屏","天玑 6300 处理器","7040mAh 长续航","四扬声器杜比全景声","AI 伴学/AI 字幕","金属机身+联想手写笔套装","莱茵 TUV 低蓝光"],"why_important":"千元级 AI 学习平板，主打护眼与 AI 伴学，覆盖学生群体，是国产中端平板走量机型。","terminal_link":"对标 TCL 入门护眼/学习平板，作为 TCL 在千元档平板的性价比竞品参照。","note":"去重表联想产品为 Yoga Tab/小新 Pro GT/拯救者 Y700，本款小新平板 11 不冲突。"},

 {"region":"国内","title":"荣耀 Pad 20 Pro 海外发布：12.1 英寸 3K 柔光屏 + 骁龙 8s Gen4 + 66W","category":"平板","dim":"SoC/芯片","status":"已上市","date":"2026-08-24","source_tier":"C","source_name":"TechNave 中文","url":"https://cn.technave.com/?p=351354","corroboration":1,"stars":3,"vendor":"荣耀 Honor","signal_type":"海外发布","key_params":"12.1 英寸 3K 屏；骁龙 8s Gen4；66W 快充；Paperlike 柔光屏；六扬声器；AI 生产力工具","tech_features":["12.1 英寸 3K 屏","骁龙 8s Gen4","66W 有线快充","抗反射 Paperlike 柔光屏","六扬声器","旗舰 AI 生产力工具"],"why_important":"荣耀 Pad 20 系列高配，柔光屏+66W 快充提升生产力属性，是海外中高端平板代表。","terminal_link":"对标 TCL 平板 NXTPAPER 柔光护眼技术在海外的规格对齐。","note":"与 Pad 20 同场发布，作为 Pro 版本单独计入；去重表无此型号。"},

 {"region":"国内","title":"荣耀 Pad 20 海外发布：12.1 英寸 3K + 骁龙 7 Gen3 + 六扬声器","category":"平板","dim":"SoC/芯片","status":"已上市","date":"2026-08-24","source_tier":"C","source_name":"TechNave 中文","url":"https://cn.technave.com/?p=351354","corroboration":1,"stars":3,"vendor":"荣耀 Honor","signal_type":"海外发布","key_params":"12.1 英寸 3K 屏；骁龙 7 Gen3；45W 快充；六扬声器；芯片级 AI 离焦护眼","tech_features":["12.1 英寸 3K 护眼大屏","骁龙 7 Gen3","六扬声器环绕音响","芯片级 AI 离焦护眼","晕动症缓解显示","继承 MagicPad 4 AI 工具"],"why_important":"荣耀海外中端平板主力，3K 屏+大电池组合主打影音娱乐，反映国产平板出海策略。","terminal_link":"对标 TCL 海外平板（如 TCL Tab 系列）在中端影音平板的规格与定价。","note":"海外（马来西亚）8/24 发布；去重表无 Pad 20，与 MagicPad 4/Pad X9b Max 不冲突。"},

 {"region":"国内","title":"iQOO 16 发布：第六代骁龙 8 超级至尊版(2nm) + 2K 165Hz + 8400mAh，9/29 开售","category":"手机","dim":"SoC/芯片","status":"已上市","date":"2026-09-29","source_tier":"B","source_name":"腾讯新闻/IT之家","url":"https://news.qq.com/rain/a/20260928A0BY0Q00","corroboration":2,"stars":5,"vendor":"vivo / iQOO","signal_type":"新品发布","key_params":"6.85 英寸 2K 165Hz 三星 M16 屏；第六代骁龙 8 超级至尊版(2nm)；8400mAh+100W 有线+40W 无线；50Mp 三摄含 3X 潜望；3D 超声指纹/IP68；自研 Q4 电竞芯","tech_features":["2nm 第六代骁龙 8 超级至尊版","2K 165Hz 三星 M16 珠峰屏(10000nit 局部)","8400mAh+100W 有线+40W 无线","自研 Q4 电竞芯片","50Mp 三摄含 3X 潜望长焦","3D 超声波指纹+IP68/IP69"],"why_important":"首批 2nm 旗舰之一，2K 165Hz 三星屏+8400mAh 大电池定义下半年性能旗舰标杆。","terminal_link":"对标 TCL 手机在 2nm 旗舰/高刷屏/大电池方向的产品规划参照。","note":"去重表行 61 为 iQOO Pad Ultra（平板），本款为 iQOO 16 手机，不冲突。"},

 {"region":"国内","title":"华为 Mate 90 系列样机到店：麒麟 9050 + 鸿蒙 7 + 全系直屏回归，即将发布","category":"手机","dim":"SoC/芯片","status":"即将上市","date":"2026-09-29","source_tier":"B","source_name":"新浪科技","url":"https://k.sina.com.cn/article_7879923512_1d5ae173806801h5ia.html","corroboration":1,"stars":4,"vendor":"华为 Huawei","signal_type":"样机到店/即将发布","key_params":"麒麟 9050/9050 Pro；HarmonyOS 7；全系直屏回归；6800mAh+100W 有线/80W 无线(Pro+)；红枫影像+3D 人脸；5G 回归","tech_features":["麒麟 9050/9050 Pro","首发鸿蒙 7 正式版","全系直屏回归设计","6800mAh 大电池+100W 有线/80W 无线","红枫影像系统+3D 人脸","5G 回归+卫星/隐私防窥屏"],"why_important":"华为下半年直板旗舰核心产品，麒麟 9050+鸿蒙 7+直屏回归，对标同代 iPhone 旗舰。","terminal_link":"对标 TCL 旗舰手机在自研芯片/鸿蒙竞品/影像方向的规划参照。","note":"去重表含 MatePad/MateBook/Mate XT2，无 Mate 90 手机，不冲突。"},

 {"region":"国内","title":"华为 WATCH GT 7 开售：1.32 英寸 3000nit AMOLED + 540mAh + 14 天续航，1588 元","category":"智能手表","dim":"传感器","status":"已上市","date":"2026-08","source_tier":"A","source_name":"华为商城 VMall","url":"https://www.vmall.com/product/comdetail/index.html?prdId=10086906049417","corroboration":1,"stars":4,"vendor":"华为 Huawei","signal_type":"新品开售","key_params":"1.32 英寸 AMOLED 3000nit；540mAh 14 天续航；血糖健康研究；蓝牙 6.0；5ATM+IP69；HarmonyOS 6.1；1588 元","tech_features":["1.32 英寸 3000nit AMOLED","540mAh 最长 14 天续航","血糖健康研究支持","蓝牙 6.0+全功能 NFC","5ATM+IP69 防水","HarmonyOS 6.1"],"why_important":"GT 系列长续航健康手表主力，3000nit 屏+血糖研究扩展健康监测边界。","terminal_link":"对标 TCL 智能手表/手环在长续航、健康监测（血糖/血氧）方向的竞品参照。","note":"去重表含 Ultimate 2/D3/手表 6 Pro，本款 GT 7 不冲突。"},

 {"region":"国内","title":"Amazfit T-Rex Dual Solar 发布：全球首款双面太阳能 AMOLED 表，25-34 天续航","category":"智能手表","dim":"电池/快充","status":"已上市","date":"2026-09-22","source_tier":"A","source_name":"Amazfit 官方","url":"https://uk.amazfit.com/blogs/news/amazfit-introduces-t-rex-dual-solar-the-first-amoled-smartwatch-with-dual-sided-solar-charging","corroboration":2,"stars":4,"vendor":"华米 Amazfit（Zepp Health）","signal_type":"新品发布","key_params":"双面太阳能 AMOLED；1.32 英寸 3000nit；660mAh 25-34 天；10ATM+50 米潜水；5 级钛合金+蓝宝石；649.90 英镑","tech_features":["全球首款双面太阳能 AMOLED 手表","前/后双太阳能面板延长续航","1.32 英寸 3000nit AMOLED","660mAh 25 天(太阳能可达 34 天)","5 级钛合金+蓝宝石镜面","10ATM+潜水+双频六星 GPS"],"why_important":"首次将 AMOLED 与双面太阳能结合，户外长续航手表技术里程碑，国产穿戴出海标杆。","terminal_link":"对标 TCL 户外/运动智能手表在续航、太阳能、坚固结构方向的竞品参照。","note":"去重表行 37 为华米 Cheetah 2 Ultra（越野跑表），本款 T-Rex Dual Solar 不冲突。"},

 {"region":"国内","title":"XREAL Aura 亮相：Android XR 空间计算眼镜，70° 光波导 + 指纹识别，秋季上市","category":"AR-VR眼镜","dim":"生物识别","status":"即将上市","date":"2026-09","source_tier":"A","source_name":"XREAL 官方","url":"https://www.xreal.com/aura","corroboration":2,"stars":4,"vendor":"XREAL（中国）","signal_type":"展会首发/预约","key_params":"Android XR 系统；骁龙 Reality Elite+X1S 双芯；70° 光学透视 FOV；95g；电致变色调光+指纹识别；Gemini 助手","tech_features":["Android XR 空间计算眼镜","骁龙 Reality Elite+XREAL X1S 双芯","70° 光学透视显示","95g 轻量化","电致变色调光+指纹识别","Gemini AI 助手+Google Play 生态"],"why_important":"首款面向消费者的 Android XR 眼镜形态，定义轻量空间计算新品类，国产 AR 出海旗舰。","terminal_link":"对标 TCL 在智能眼镜/AR 方向的布局与重量、FOV、AI 助手规格参照。","note":"去重表含雷鸟/Rokid/Meta 等，本款 XREAL Aura 不冲突。"},

 {"region":"国内","title":"千问 AI 眼镜 N1 系列亮相：骁龙 AR1 三芯 + 4K 录像 + 虹膜支付，10/13 开售","category":"AR-VR眼镜","dim":"AI/NPU","status":"即将上市","date":"2026-09-22","source_tier":"B","source_name":"快科技/站长之家","url":"https://www.chinaz.com/2026/0922/1778529.shtml","corroboration":2,"stars":4,"vendor":"阿里巴巴 千问","signal_type":"展会亮相","key_params":"骁龙 AR1+恒玄 BES2800+低功耗感知三芯；5000 万像素 4K 录像；N1 Pro 眼动追踪+虹膜支付；可换电不断电；心率/血氧/HRV 监测；10/13 现货","tech_features":["高通骁龙 AR1+恒玄 BES2800+低功耗感知芯片三芯方案","5000 万像素 4K 超清录像+多重防抖","N1 Pro 眼动追踪+虹膜支付","镜腿可换电设计(换电不断电)","N1 Pro 体征监测(心率/血氧/HRV/体温)","阿里系服务一句话调用"],"why_important":"阿里 Personal Agent 硬件入口，眼动+虹膜把交互与身份合一，定义无屏 AI 眼镜新形态。","terminal_link":"对标 TCL 在 AI 眼镜/可穿戴个人智能体方向的布局参照。","note":"去重表含 Meta/Rokid/雷鸟等，本款千问 N1 不冲突；10/13 发售，情报在窗口内。"},

 {"region":"国内","title":"机械革命翼龙 15 Air 2026 发布：锐龙 7 H449 + RTX5060 + 15.3 英寸 OLED，国补 9999","category":"笔记本电脑","dim":"散热","status":"已上市","date":"2026-08-30","source_tier":"B","source_name":"网易/IT之家","url":"https://c.m.163.com/news/a/L5JGMMMC0511B8LM.html","corroboration":2,"stars":4,"vendor":"机械革命（清华同方）","signal_type":"新品发布","key_params":"锐龙 7 H449 + RTX5060；15.3 英寸 2.5K 240Hz OLED；1.6kg/18.75mm；双风扇后出风 170W 双烤；99Wh 电池；国补 9999 元","tech_features":["锐龙 7 H449 处理器+RTX5060 独显","15.3 英寸 2.5K 240Hz OLED 电竞屏","1.6kg 轻薄机身","双风扇后出风 170W 双烤散热","99Wh 电池+100W PD","国补到手 9999 元"],"why_important":"轻薄游戏本把 OLED 高刷与 RTX5060 下探至万元内，国补拉高性价比。","terminal_link":"对标 TCL 游戏本/创作本在 OLED 屏、轻薄化、独显性价比方向的竞品参照。","note":"去重表含七彩虹/微星等游戏本，本款机械革命不冲突。"},

 {"region":"国内","title":"雷神 ZERO Air 15 小轻龙展出：RTX5060 + Ultra7 + 15.3 英寸 OLED，约 1.54kg","category":"笔记本电脑","dim":"结构/工艺","status":"已上市","date":"2026-09-20","source_tier":"B","source_name":"太平洋科技","url":"https://g.pconline.com.cn/x/2182/21829338.html","corroboration":1,"stars":3,"vendor":"雷神 Thunderobot","signal_type":"校园活动展出","key_params":"RTX5060 + Ultra7 356H；15.3 英寸 OLED；1.54kg；32GB DDR5+1TB；AI 加速","tech_features":["RTX5060 笔记本电脑 GPU","Ultra7 356H 处理器","15.3 英寸超竞 OLED 屏","约 1.54kg 轻量化","32GB DDR5+1TB PCIe4.0","AI 加速支持"],"why_important":"雷神轻薄高性能本，1.54kg+OLED 主打校园创作与轻游戏场景。","terminal_link":"对标 TCL 轻薄高性能本在重量、OLED 屏、AI 加速方向的竞品参照。","note":"去重表含机械革命/七彩虹等，本款雷神不冲突。"},

 {"region":"国内","title":"moto snap 无线充电器发布：Qi2.2 25W 磁吸 + 摩托私有 30W，39 欧元","category":"无线充","dim":"无线通信","status":"已上市","date":"2026-09-07","source_tier":"B","source_name":"充电头网","url":"https://www.chongdiantou.com/archives/1788766168168.html","corroboration":1,"stars":3,"vendor":"摩托罗拉 Motorola","signal_type":"IFA 发布","key_params":"Qi2.2 25W；摩托私有 30W；铝壳+1.5m 编织线；IPX2；39 欧元","tech_features":["Qi2.2 无线充电标准 25W","摩托罗拉私有协议最高 30W","铝合金轻薄圆形机身","自带 1.5 米编织 USB-C 线","过热/过充保护+零待机功耗","IPX2 防泼溅+磁吸支架可选"],"why_important":"摩托罗拉补齐 Qi2.2 磁吸配件，反映 Qi2.2 25W 在安卓旗舰的普及趋势。","terminal_link":"对标 TCL 磁吸无线充电配件在 Qi2.2/功率/价格方向的规划参照。","note":"去重表含倍思/贝尔金/mophie/安克等，本款 moto snap 不冲突。"},

 {"region":"国内","title":"小度智能音箱 Pro Max 上市：首款带屏小度音箱 + 超能小度大模型，9/28","category":"智能音箱","dim":"AI/NPU","status":"已上市","date":"2026-09-28","source_tier":"C","source_name":"百度百科（百度 AI Day 发布）","url":"https://baike.baidu.com/item/%E5%B0%8F%E5%BA%A6%E6%99%BA%E8%83%BD%E9%9F%B3%E7%AE%B1Pro%20Max/68945430","corroboration":1,"stars":3,"vendor":"百度 小度","signal_type":"新品发布","key_params":"小彩屏；超能小度大模型；3 英寸 12W 单元；温/湿度/光线传感器；9/28 上市；AI 大模型问答","tech_features":["首款带屏小度智能音箱(小彩屏)","超能小度 AI 大模型问答","3 英寸 12W 单元+倒相管设计","内置温湿度/光线亮度传感器联动家电","15 种方言+多意图识别+长期记忆","百度 AI Day 发布 9/28 上市"],"why_important":"小度首款带屏音箱，AI 大模型+环境感知推动智能家居主动服务。","terminal_link":"对标 TCL 智能音箱/屏在 AI 大模型、环境传感、智能家居联动方向的竞品参照。","note":"去重表含小爱/天猫精灵/华为 Sound 等，本款小度 Pro Max 不冲突。"},

 {"region":"国内","title":"华为 FreeBuds 7 悦彰耳机发布：第三代音频 AI 芯片 + 半入耳降噪，999 元","category":"AI耳机·耳穿戴","dim":"音频","status":"已上市","date":"2026-09-07","source_tier":"B","source_name":"中关村在线 ZOL","url":"https://dcdv.zol.com.cn/1244/12447787.html","corroboration":2,"stars":4,"vendor":"华为 Huawei","signal_type":"新品发布","key_params":"第三代音频 AI 芯片(双 DSP+NPU)；半入耳主动降噪；100dB 双向通话；10.8mm 单元；999 元；星闪音频","tech_features":["自研第三代音频 AI 芯片(双 DSP+NPU)","半入耳舒适降噪新标杆","100dB 双向静谧通话","10.8mm 高保真全频单元","星闪音频连接+4.6Mbps 无损","42 小时续航+IP55"],"why_important":"华为数字系列新一代，半入耳降噪与 AI 芯片算力翻倍，定义半入耳旗舰标准。","terminal_link":"对标 TCL 真无线耳机在降噪、AI 芯片、无损传输方向的竞品参照。","note":"去重表行 125 为 FreeBuds Neo（不同型号），本款 FreeBuds 7 不冲突。"},

 # ---------- INTL (16-30) ----------
 {"region":"国际","title":"OnePlus Pad 3 全球在售：13.2 英寸 3.4K + 骁龙 8 Elite + 12140mAh，80W","category":"平板","dim":"SoC/芯片","status":"已上市","date":"2026-09","source_tier":"A","source_name":"OnePlus 官网（阿联酋）","url":"https://www.oneplus.com/ae/oneplus-pad-3/specs","corroboration":3,"stars":5,"vendor":"OnePlus","signal_type":"全球在售旗舰","key_params":"13.2 英寸 3392×2400 3.4K 144Hz LTPS LCD；骁龙 8 Elite；12-16GB LPDDR5X；12140mAh+80W；5.97mm/675g；8 扬声器；Wi-Fi7","tech_features":["骁龙 8 Elite 旗舰平台(Oryon CPU)","3.4K 144Hz 12bit 色深大屏","12140mAh 泰坦电池+80W","8 扬声器四低音四高音","VC 均热板 34857mm² 散热","专属 AI 按键+Gemini","Wi-Fi 7+USB3.2 Gen1"],"why_important":"安卓平板性能天花板，骁龙 8 Elite 下放平板，对标 iPad Pro 级生产力，海外多市场同步发售。","terminal_link":"对标 TCL Tab A1 NXTPAPER（安卓平板线）在旗舰性能与创作场景的差距。","note":"不在去重表；与去重表 OnePlus 15(手机)、Redmagic Astra 2 等不同产品。"},

 {"region":"国际","title":"Alldocube iPlay 80 mini Turbo 发布：8.8 英寸 2.5K 120Hz + 天玑 7400，约 199 美元","category":"平板","dim":"显示/OLED","status":"已上市","date":"2026-08-13","source_tier":"B","source_name":"Gizmochina","url":"https://www.gizmochina.com/?p=748281","corroboration":2,"stars":4,"vendor":"ALLDOCUBE","signal_type":"新发布/全球首发（日本优先）","key_params":"8.8 英寸 2560×1600 2.5K 120Hz IPS；天玑 7400；8GB LPDDR5X+128GB；6500mAh+20W；295g/6.95mm；RGB 灯；4G LTE","tech_features":["8.8 寸 2.5K 120Hz 小平板","天玑 7400 中高性能 SoC","RGB 游戏风背盖","旁路充电控温","4G LTE 单卡","microSD 扩展 2TB","Widevine L1+双扬"],"why_important":"小屏游戏平板细分市场国际新品，日本全球首发，300g 内便携+高刷，填补便携游戏平板空白。","terminal_link":"对标 TCL Tab A1 NXTPAPER（小/中尺寸安卓平板）在便携游戏场景的差距。","note":"不在去重表；与去重表酷比魔方酷玩 Pad Pro2、Blackview Zeno6 Pro 等不同品牌。"},

 {"region":"国际","title":"TCL Tab A1 NXTPAPER 海外上市：11 英寸类纸护眼屏 + Helio G100，249.99 美元","category":"平板","dim":"结构/工艺","status":"已上市","date":"2026-09-11","source_tier":"B","source_name":"AndroidHeadlines","url":"https://www.androidheadlines.com/2026/09/tcl-tab-a1-nxtpaper-launch-budget-tablets.html","corroboration":2,"stars":4,"vendor":"TCL","signal_type":"新发布/海外上市","key_params":"11 英寸 2112×1320 90Hz IPS(NxtPaper 3A Crystal 类纸)；Helio G100；6+128GB；8000mAh+20W；6.2mm/426g；四扬 IP54；赠 T-Pen2+皮套 249.99 美元","tech_features":["NxtPaper 3A Crystal 类纸抗反射屏","纸张/墨色双护眼阅读模式","随附 T-Pen2 主动笔+保护壳","四立体声扬声器","IP54 防尘防泼溅","Android16+Gemini+Circle to Search","microSD 2TB"],"why_important":"TCL 自有海外平板主力型号，类纸护眼屏差异化切入阅读/学习场景，配件即送拉高性价比。","terminal_link":"TCL Tab A1 NXTPAPER（本家对标基准，与雷鸟平板协同）。","note":"不在去重表；与去重表 TCL Note A1 NXTPAPER（不同产品名）不冲突。"},

 {"region":"国际","title":"Acer Iconia X16 发布：16 英寸 OLED 安卓平板，双 USB-C 可作便携副屏，Q4 上市","category":"平板","dim":"显示/OLED","status":"即将上市","date":"2026-09-02","source_tier":"B","source_name":"Android Authority","url":"https://www.androidauthority.com/acer-iconia-x14-x16-tablet-launch-ifa-2026-3705429/","corroboration":2,"stars":4,"vendor":"Acer","signal_type":"IFA 2026 发布","key_params":"16 英寸 1920×1200 OLED 60Hz；Helio G80；6+128GB；8000mAh 10h；双 USB-C(一为视频输入)；内置支架；Android16；Q4 北美+EMEA","tech_features":["16 寸 OLED 大屏","双 USB-C 其中一口支持视频输入(可作便携副屏)","内置三脚架式支架","选配主动笔+键盘","四扬声器","microSD 2TB","Android16"],"why_important":"Acer 把大屏 OLED 安卓平板做成便携副屏形态，双 USB-C 视频输入是差异化卖点。","terminal_link":"对标 TCL Tab A1 NXTPAPER（大屏安卓平板）在副屏/生产力形态的差距。","note":"不在去重表；与去重表 Acer Iconia Duo D12 为不同产品（原 intomobile 源被 Cloudflare 拦截，已换 Android Authority）。"},

 {"region":"国际","title":"Samsung Galaxy S26 FE 海外发布：6.7 英寸 Dynamic AMOLED 2X + Exynos 2500 + 长焦","category":"手机","dim":"摄像头","status":"已上市","date":"2026-09-14","source_tier":"B","source_name":"Mobile Maniya","url":"https://mobilemaniya.com/samsung-galaxy-s26-fe-specs-review-price-in-india","corroboration":3,"stars":4,"vendor":"Samsung","signal_type":"新发布/海外上市","key_params":"6.7 英寸 FHD+ Dynamic AMOLED 2X 120Hz 1900nit；Exynos 2500(3nm)；8+256GB；50+12+8(3x OIS)；4900mAh 45W；One UI9 Android17；7 年更新；79999 卢比","tech_features":["Exynos 2500 3nm","Dynamic AMOLED 2X 1900nit","5000 万主摄+3 倍光变长焦","4900mAh+45W 有线+15W 无线","One UI9+Android17","7 年系统/安全更新","IP68"],"why_important":"三星 FE 走量机型，长焦+长更新周期+IP68，海外中端旗舰有力竞争者。","terminal_link":"对标 TCL 50 系列（手机）在长焦、系统更新周期方向的差距。","note":"不在去重表；与去重表 S26 Ultra/Z Flip8/Z Fold8/S25 系列等不同型号。"},

 {"region":"国际","title":"Poco X8 Power 海外发布：10000mAh 硅碳电池 + 100W，IP69K 四重防护","category":"手机","dim":"电池/快充","status":"已上市","date":"2026-09-04","source_tier":"B","source_name":"Gadgets 360","url":"https://gadgets360.com/poco-x8-power-137351","corroboration":4,"stars":4,"vendor":"POCO","signal_type":"新发布/海外上市","key_params":"6.83 英寸 1.5K 120Hz AMOLED 3500nit；骁龙 6 Gen5；8+128 起；10000mAh 100W+27W 反向；IP68/69/69K；35999 卢比","tech_features":["10000mAh 硅碳电池","100W 有线+27W 反向供电","骁龙 6 Gen5 印度首发","IP66/68/69/69K 多重防护","3500nit 12bit AMOLED","Gorilla Glass Victus2+SGS 五星抗摔","4 代 OS+6 年安全"],"why_important":"中端机电池容量破万毫安+百瓦快充，续航与耐用双拉满，重塑性价比标杆。","terminal_link":"对标 TCL 50 系列（手机）在电池容量、快充、防护认证方向的差距。","note":"不在去重表；intomobile 原文被 Cloudflare 拦截，已改用 Gadgets360 可达源。"},

 {"region":"国际","title":"Garmin Venu 4 发布：1.4 英寸 AMOLED + 12 天续航 + 腕上通话，549.99 美元","category":"智能手表","dim":"传感器","status":"已上市","date":"2026-09","source_tier":"A","source_name":"Garmin 美国官网","url":"https://garmin.com/en-US/p/1614061","corroboration":2,"stars":5,"vendor":"Garmin","signal_type":"新品上市","key_params":"45mm(另有 41mm)；1.4 英寸 AMOLED；12 天续航；LED 手电筒；内置扬声器+麦克风通话；549.99 美元；金属机身","tech_features":["1.4 寸 AMOLED 大屏","12 天智能续航","内置 LED 手电筒","扬声器+麦克风腕上通话","ECG/HRV/皮肤温度/Pulse Ox","80+ 运动+Garmin Coach","语音指令+WhatsApp"],"why_important":"Garmin 主流 AMOLED 健康手表迭代，加入通话与手电筒，直面 Apple Watch/三星对标。","terminal_link":"对标 TCL 运动手表（穿戴）在 AMOLED、健康传感、通话方向的差距。","note":"不在去重表；与去重表 Garmin Fenix9/Enduro4/Fenix E2 等为不同系列。"},

 {"region":"国际","title":"Redmi Watch 6 Lite 海外发布：1.5 英寸 1500nit AMOLED + 18 天续航，约 75 美元","category":"智能手表","dim":"显示/OLED","status":"已上市","date":"2026-08-24","source_tier":"B","source_name":"NotebookCheck","url":"https://www.notebookcheck.net/Xiaomi-releases-new-smartwatch-with-up-to-18-days-battery-life-and-1-500-nit-AMOLED-display.1377173.0.html","corroboration":2,"stars":4,"vendor":"小米 Redmi","signal_type":"海外发布","key_params":"1.96 英寸 410×502 1500nit AMOLED；470mAh；最长 18 天；5ATM；GPS；27.8g；波兰/欧元区/Amazon US，约 75 美元","tech_features":["1.5 英寸 1500nit AMOLED","470mAh 最长 18 天续航","5ATM 防水","GPS 定位","塑料金属涂层机身 27.8g","Android 8.0/iOS 14.0+"],"why_important":"小米海外入门智能表，1500nit AMOLED+18 天续航以约 75 美元切入全球走量市场。","terminal_link":"对标 TCL 智能手表/手环在海外入门价位的竞品参照。","note":"不在去重表；与去重表 小米手环 11（不同品类/型号）不冲突。"},

 {"region":"国际","title":"PICO Space Pro 延期至 Q4：双 4K Micro-OLED + 自研空间芯片，对标 Quest/Vision Pro","category":"AR-VR眼镜","dim":"显示/OLED","status":"进行中","date":"2026-08-24","source_tier":"B","source_name":"Spatial Insider","url":"https://spatialinsiders.com/stories/pico-space-pro-september-2-event","corroboration":2,"stars":4,"vendor":"PICO","signal_type":"发布延期","key_params":"双 4K Micro-OLED 4000PPI；自研空间芯片+主芯片(超 XR2 Gen2 2 倍)；端到端 12ms；PICO OS 6；Shared Space；Q4 2026","tech_features":["双 4K Micro-OLED 4000PPI","自研空间协处理器(延迟 12ms)","PICO OS 6 Shared Space","眼/手/指针/手柄多模态输入","Cloud Crystal 界面语言","原 9/2 揭幕延至 Q4","最高 40PPD 中心"],"why_important":"PICO 下一代旗舰头显，双 4K+自研芯片对标 Quest/Vision Pro，延期打磨 OS 值得跟踪。","terminal_link":"对标 TCL 雷鸟(RayNeo) AR 在 XR 头显方向的差距。","note":"不在去重表；与去重表 Meta Quest4、Vision Pro2 等不同品牌。"},

 {"region":"国际","title":"Even Realities G2 智能眼镜 IFA 亮相：双目 Micro-LED 波导 + 48 小时续航，599 美元","category":"AR-VR眼镜","dim":"显示/OLED","status":"已上市","date":"2026-09","source_tier":"C","source_name":"Basic Tutorials","url":"https://basic-tutorials.com/news/ifa-2026-even-realities-g2-camera-less-ai-smart-glasses-with-a-48-hour-battery-life","corroboration":1,"stars":3,"vendor":"Even Realities","signal_type":"IFA 2026 展出","key_params":"双目 Micro-LED 波导 640×350/眼 1200nit；36g；48h 续航；31 语言实时翻译；无摄像头；IP65；599 美元","tech_features":["双目 Micro-LED 波导显示 640×350/眼","1200nit 亮度","36g 镁钛轻量框架","48 小时续航","31 语言实时翻译+Conversate 转写","无摄像头隐私设计+四麦克风","IP65 防护"],"why_important":"无摄像头 AI 眼镜以 48 小时续航+实时翻译切入隐私敏感市场，代表轻量 AI 眼镜新路线。","terminal_link":"对标 TCL 在 AI 眼镜/可穿戴个人智能体方向的布局参照。","note":"不在去重表；原 WearableXP 综述页未含本产品，已换 Basic Tutorials 专文。"},

 {"region":"国际","title":"Acer Vero 16 发布：可维修/可升级 Panther Lake 笔记本，3K OLED，2026-12 上市","category":"笔记本电脑","dim":"AI/NPU","status":"即将上市","date":"2026-09-02","source_tier":"B","source_name":"NotebookCheck","url":"https://www.notebookcheck.net/Acer-unveils-repairable-Panther-Lake-laptop-with-3K-OLED-display-and-upgradeable-CPU.1385683.0.html","corroboration":2,"stars":4,"vendor":"Acer","signal_type":"IFA 2026 发布","key_params":"16 英寸 2880×1800 OLED 120Hz 100% DCI-P3；Intel Panther Lake 最高 Core Ultra X9 388H；最高 32GB LPDDR5X+512GB；71Wh；免工具维修；2026-12","tech_features":["可维修设计(免工具开盖)","电池+SSD 用户可换","CPU 可跨代升级","Panther Lake 最高 180 TOPS AI","3K OLED 120Hz","Wi-Fi7+BT5.6","双 TB4+双 USB-A+HDMI+SD"],"why_important":"主流厂商首款主打可升级/可维修的 Panther Lake 笔记本，可持续设计+高性能兼得。","terminal_link":"对标 TCL 笔记本（通用 PC）在可维修设计与端侧 AI 方向的差距。","note":"不在去重表；与去重表 ThinkPad X1 Carbon Gen14、华硕破晓 Air 等不同。"},

 {"region":"国际","title":"ASUS Zenbook 14 UX3480AA 国际发布：1100nit OLED + Panther Lake + 18 小时续航","category":"笔记本电脑","dim":"显示/OLED","status":"已上市","date":"2026-08-31","source_tier":"B","source_name":"NotebookCheck","url":"https://notebookcheck.net/Asus-releases-new-14-inch-laptop-internationally-with-1-100-nit-OLED-display-Intel-Panther-Lake-and-18-hours-battery-life.1383295.0.html","corroboration":2,"stars":4,"vendor":"ASUS","signal_type":"国际发布/发货","key_params":"14 英寸 2.8K OLED 120Hz 1100nit(HDR)；Panther Lake Core Ultra 5 325/7 355/9 386H；70Wh 18h；1.3kg；Ceraluminum；1299 英镑+","tech_features":["1100nit 峰值 HDR OLED","Panther Lake 三档 CPU","70Wh 官方 18 小时续航","1.3kg 轻量","Ceraluminum 防污涂层","欧洲已现货/英国 9 月下旬发货","Wi-Fi7"],"why_important":"Panther Lake 国际版轻薄本标杆，高亮 OLED+长续航，海外多市场价格已公布。","terminal_link":"对标 TCL 笔记本（通用轻薄本）在 OLED 屏与续航方向的差距。","note":"不在去重表；与去重表 ASUS Zenbook A14(骁龙 X2)为不同模具平台。"},

 {"region":"国际","title":"Anker MagGo 2 Pro 发布：Qi2.2 25W 磁吸 + SnapCool 主动风冷，109.99 美元","category":"无线充","dim":"电池/快充","status":"已上市","date":"2026-09-17","source_tier":"A","source_name":"Anker 官网/EIN Presswire","url":"https://www.einpresswire.com/article/943055584/anker-launches-maggo-2-pro-the-world-s-fastest-and-coolest-wireless-power-bank","corroboration":3,"stars":5,"vendor":"Anker","signal_type":"IFA 2026 发布/上市","key_params":"Qi2.2 25W 磁吸无线；SnapCool 主动风冷(背部<36℃)；10000mAh；45W 自充；智能屏；可调支架；型号 A110R；109.99 美元","tech_features":["Qi2.2 真 25W 无线(SGS A+ 最高评级)","SnapCool 主动风冷(背部<36℃)","10000mAh+45W 有线自充","智能屏显电量/温度/健康","0-80° 可调支架","ActiveShield5.0 千万次/日温控","四色"],"why_important":"全球首款获 SGS 最高评级的 25W 磁吸无线充，主动散热破解无线快充发热降速痛点。","terminal_link":"对标 TCL 充电配件（无线充）在 Qi2.2 与主动散热方向的规划参照。","note":"不在去重表；与去重表 安克快充护机三折叠风冷无线充(型号不同)不冲突；Anker SoundCore 为音箱不同类。"},

 {"region":"国际","title":"UGREEN Uliya 智能语音助理喇叭发布：四麦克风 + Matter 控制 + 本地 AI，99 美元","category":"智能音箱","dim":"AI/NPU","status":"即将上市","date":"2026-09","source_tier":"C","source_name":"BigGo 财经","url":"https://finance.biggo.com.tw/news/55965574-fa81-461a-ab0c-f63af4d37f0a","corroboration":2,"stars":3,"vendor":"UGREEN","signal_type":"IFA 2026 生态发布","key_params":"四麦克风阵列+三单元声学；Matter 控制；本地 AI 事件通知；99 美元(早鸟 69)；配 HomeAgent 生态","tech_features":["四麦克风远场拾音","三单元声学系统","Matter 兼容智能家居控制","本地 AI 通知(婴儿哭/包裹到达)","UGREEN HomeAgent 生态入口","IFA 2026 亮相","早鸟 69 美元"],"why_important":"UGREEN 从充电配件跨界本地 AI 智能家居，Uliya 是其语音入口，标志配件厂向上做平台。","terminal_link":"对标 TCL 智能音箱（对标智能音箱）在本地 AI 与 Matter 生态方向的差距。","note":"不在去重表；与去重表 Echo Dot Max/Echo Show11/Sonos Beam Ultra/HomePod3 等不同产品。"},

 {"region":"国际","title":"Timekettle W4 Plus AI 同传耳机发布：5.7g 耳塞 + 52 语言实时翻译，379 美元","category":"AI耳机·耳穿戴","dim":"音频","status":"已上市","date":"2026-09-06","source_tier":"B","source_name":"GismoLand","url":"https://gismoland.com/2026/09/05/timekettle-w4-plus-fifty-two-languages-inside-a-5-7-gram-earbud","corroboration":3,"stars":4,"vendor":"Timekettle（时空壶）","signal_type":"IFA 2026 发布/开售","key_params":"5.7g 半入耳；52 语言 106 口音 13 离线对；Babel OS 3.0；骨传导声纹传感器；3+12h；379 美元(订阅版 299)；9-6 开售","tech_features":["52 在线语言+106 口音","13 对离线翻译","Babel OS 3.0 语境翻译","骨传导声纹+双麦降噪(VoiceFocus)","AI 行业术语/会议摘要/口语教练","四种模式(面对面/收听/通话/多媒体)","5.7g 超轻半入耳"],"why_important":"把 52 语言实时同传塞进 5.7g 耳塞，跨境商务/旅行刚需，AI 耳穿戴标杆产品。","terminal_link":"对标 TCL 耳机（AI 耳穿戴）在实时翻译与轻量化方向的差距。","note":"不在去重表；与去重表 TOZO NC9 Pro/Plaud One/韶音 OpenFit2/网易有道 OpenPods/飞书×安克/Bose Ultra Open 等为不同品牌或已覆盖产品。"},
]

# ---------- helpers ----------
STATUS_RANK = {"即将上市":0, "进行中":1, "已上市":2}
STATUS_CLASS = {"即将上市":"status-coming", "进行中":"status-progress", "已上市":"status-released"}
CIRCLED = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩"]

def star_str(n):
    return "★"*n + "☆"*(5-n)

def sort_key(it):
    return (STATUS_RANK[it["status"]], -int(it["date"].replace("-","")))

cn = sorted([it for it in ITEMS if it["region"]=="国内"], key=sort_key)
intl = sorted([it for it in ITEMS if it["region"]=="国际"], key=sort_key)
ordered = cn + intl

dim_count = {d:0 for d in DIMS}
for it in ITEMS:
    if it["dim"] in dim_count:
        dim_count[it["dim"]] += 1
covered = sum(1 for d in DIMS if dim_count[d] > 0)

tier_count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for it in ITEMS:
    tier_count[it["source_tier"]] += 1
five_star = sum(1 for it in ITEMS if it["stars"]==5)

def field(label, value, full=False):
    cls = "field full" if full else "field"
    return f'          <div class="{cls}"><div class="field-label">{label}</div><div class="field-value">{value}</div></div>'

def render_card(idx, it):
    badges = (f'<span class="source-tag source-{it["source_tier"].lower()}">{it["source_tier"]}</span>'
              f'<span class="sig-dim" style="background:#f0f9eb;color:#67c23a;border-radius:4px;padding:1px 6px;font-size:11px;">{it["dim"]}</span>'
              f'<span class="stars">{"★"*it["stars"]}{"☆"*(5-it["stars"])}</span>')
    if it["status"] != "已上市":
        badges += f'<span class="status-tag {STATUS_CLASS[it["status"]]}">{it["status"]}</span>'
    else:
        badges += f'<span class="status-tag" style="background:#f0f9eb;color:#67c23a;border:1px solid #c2e7b0;">已上市</span>'
    tech_li = "".join(f'<li data-num="{CIRCLED[i]}">{t}</li>' for i,t in enumerate(it["tech_features"]))
    fields = (
        field("信号类型", it["signal_type"]) +
        field("印证源数", f'{it["corroboration"]} 个独立信源') +
        field("主技术维度", it["dim"]) +
        field("区域", it["region"]) +
        field("厂商/型号", it["vendor"]) +
        field("时间", it["date"]) +
        field("信源等级", f'{it["source_tier"]} 级 — {it["source_name"]}') +
        field("信源明细", it["source_name"]) +
        field("关键参数", it["key_params"], full=True) +
        field("技术特性", f'<ul class="tech-list">{tech_li}</ul>', full=True) +
        field("为什么重要", it["why_important"], full=True) +
        field("智能终端关联点", it["terminal_link"], full=True) +
        field("来源 URL", f'<a href="{it["url"]}" target="_blank" rel="noopener">{it["url"]}</a>', full=True) +
        field("备注待印证", it["note"], full=True)
    )
    expanded = " expanded" if idx == 1 else ""
    return f'''      <div class="intel-card {('cn' if it['region']=='国内' else 'intl')}{expanded}" id="card-{idx}">
        <div class="card-header" onclick="toggleCard('card-{idx}')">
          <div class="card-num">{idx}</div>
          <div class="card-title-area">
            <div class="card-title">{it['title']}</div>
            <div class="card-badges">{badges}</div>
          </div>
          <div class="card-toggle">▼</div>
        </div>
        <div class="card-body"><div class="card-content">
          <div class="field-grid">
{fields}
          </div>
        </div></div>
      </div>'''

def render_summary_row(idx, it):
    region_cls = "region-cn" if it["region"]=="国内" else "region-intl"
    region_txt = "国内" if it["region"]=="国内" else "国际"
    if it["status"] != "已上市":
        st = f'<span class="status-tag {STATUS_CLASS[it["status"]]}">{it["status"]}</span>'
    else:
        st = f'<span class="status-tag" style="background:#f0f9eb;color:#67c23a;border:1px solid #c2e7b0;">已上市</span>'
    return f'''      <tr>
        <td>{idx}</td>
        <td class="td-title"><a href="#card-{idx}">{it['title']}</a></td>
        <td><span class="td-region {region_cls}">{region_txt}</span></td>
        <td>{it['category']}</td>
        <td><span class="source-tag source-{it['source_tier'].lower()}">{it['source_tier']}</span></td>
        <td class="td-status">{st}</td>
        <td>{it['date']}</td>
        <td><span class="stars">{"★"*it['stars']}{"☆"*(5-it['stars'])}</span></td>
      </tr>'''

def dim_chip(d):
    n = dim_count[d]
    if n > 0:
        return f'<div class="dim-chip on">{d} <span class="dim-count">{n}条</span></div>'
    return f'<div class="dim-chip off">{d} <span class="dim-count">0条</span></div>'
dim_html = "".join(dim_chip(d) for d in DIMS)
pct = round(covered/16*100)

def top_key(it):
    return (-it["stars"], 0 if it["source_tier"]=="A" else 1, STATUS_RANK[it["status"]], -int(it["date"].replace("-","")))
top5 = sorted(ITEMS, key=top_key)[:5]

top_cards = ""
for i, it in enumerate(top5, 1):
    top_cards += f'''      <div class="signal-card">
        <div><span class="sig-rank">{i}</span><span class="sig-title">{it['title']}</span></div>
        <div class="sig-tags"><span class="sig-dim">{it['category']}</span><span class="sig-stars">{"★"*it['stars']}{"☆"*(5-it['stars'])}</span></div>
        <div class="sig-key">{it['source_tier']}级 / {it['key_params']}</div>
      </div>'''

summary_rows = "".join(render_summary_row(i+1, it) for i, it in enumerate(ordered))
cards_html = "".join(render_card(i+1, it) for i, it in enumerate(ordered))
cn_cards = "".join(render_card(i+1, it) for i, it in enumerate(cn))
intl_cards = "".join(render_card(15+i+1, it) for i, it in enumerate(intl))

HTML = f'''<!DOCTYPE html>
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
  .status-progress {{ background:#ecf5ff; color:#409eff; border:1px solid #b3d8ff; }}
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
    <div class="stat-item"><div class="stat-num">{tier_count['A']}</div><div class="stat-label">A级信源</div></div>
    <div class="stat-item"><div class="stat-num">{tier_count['B']}</div><div class="stat-label">B级信源</div></div>
    <div class="stat-item"><div class="stat-num">8</div><div class="stat-label">覆盖产品类别</div></div>
    <div class="stat-item"><div class="stat-num">{five_star}</div><div class="stat-label">五星条数</div></div>
  </div>
  <div class="dim-panel">
    <div class="dim-header">
      <div class="dim-title">技术维度覆盖面板</div>
      <div class="dim-counter"><span class="dim-num">{covered}</span><span class="dim-total"> / 16 维度</span></div>
    </div>
    <div class="dim-bar"><div class="dim-bar-fill" style="width:{pct}%"></div></div>
    <div class="dim-grid">
      {dim_html}
    </div>
  </div>
  <div class="top-signals-panel">
    <div class="top-signals-header">
      <div class="top-signals-title">今日重点信号 Top 5</div>
      <div style="font-size:12px;color:var(--text-tertiary);">排序：星级降序→A级优先→状态优先→时间倒序</div>
    </div>
    <div class="top-signals-grid">
      {top_cards}
    </div>
  </div>
  <div class="summary-section">
    <div class="section-title">情报摘要表</div>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>类别</th><th>信源</th><th>状态</th><th>时间</th><th>重要度</th></tr></thead>
      <tbody>
      {summary_rows}
      </tbody>
    </table>
  </div>
  <div class="intel-section">
    <div class="section-title">一、国内情报（15条）</div>
    <div class="intel-cards">
{cn_cards}
    </div>
  </div>
  <div class="intel-section">
    <div class="section-title">二、国际情报（15条）</div>
    <div class="intel-cards">
{intl_cards}
    </div>
  </div>
</div>
<script>
function toggleCard(id) {{
  var el = document.getElementById(id);
  if (el.classList.contains('expanded')) el.classList.remove('expanded');
  else el.classList.add('expanded');
}}
</script>
</body>
</html>'''

out = f"E:/AI相关/预研究/202608/03_输出/WB_{DATE}_硬件看板.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print("written:", out, "bytes:", len(HTML.encode('utf-8')))
print("covered dims:", covered, "/16  pct:", pct)
print("tier A/B/C/D/E:", tier_count)
print("5-star:", five_star)
print("cn dates:", [it['date'] for it in cn])
print("intl dates:", [it['date'] for it in intl])
print("cn categories:", {c: sum(1 for it in cn if it['category']==c) for c in ['平板','手机','智能手表','AR-VR眼镜','笔记本电脑','无线充','智能音箱','AI耳机·耳穿戴']})
print("intl categories:", {c: sum(1 for it in intl if it['category']==c) for c in ['平板','手机','智能手表','AR-VR眼镜','笔记本电脑','无线充','智能音箱','AI耳机·耳穿戴']})
