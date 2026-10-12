# -*- coding: utf-8 -*-
"""生成 WB_2026-10-12_硬件看板.html —— 智能终端硬件情报日报"""
import datetime

OUT = r"E:/AI相关/预研究/202608/03_输出/WB_2026-10-12_硬件看板.html"
TODAY = "2026-10-12"

# 16 技术维度（固定顺序）
DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

CATEGORY_ORDER = ["平板","手机","智能手表","AR-VR眼镜","笔记本电脑","无线充","智能音箱","AI耳机·耳穿戴"]

def skey(d):
    """日期排序键：越新越大"""
    d = d.strip()
    try:
        if len(d) == 10:
            return int(d.replace("-",""))
        if len(d) == 7:  # 2026-10
            y,m = d.split("-"); return int(y)*10000 + int(m)*100 + 15
        if len(d) == 4:  # 2026
            return int(d)*10000 + 901
    except Exception:
        pass
    return 0

STATUS_RANK = {"即将上市":0, "进行中":1, "已上市":2}

# 30 条情报（国内 15 + 国际 15），每条 14 字段 + 辅助字段
DATA = [
 # ===================== 国内 15 条 =====================
 {"region":"cn","title":"荣耀WIN平板官宣：8.4英寸240Hz OLED游戏小平板","category":"平板","main_dim":"显示/OLED",
  "dims":"显示/OLED|SoC/芯片|散热|电池/快充","status":"即将上市","stars":3,"grade":"D",
  "corroboration":"2（今日头条科技衍生、腾讯搜一搜同文）","signal_type":"曝光/预热",
  "key_params":"8.4±英寸2.5K+ OLED 240Hz、第五代骁龙8至尊版、10000mAh青海湖电池+66W、内置主动散热风扇",
  "tech_features":["8.4±英寸OLED 240Hz超高刷，居中单孔小直屏","第五代骁龙8至尊版（3nm、2+6全大核4.6GHz、Adreno840+18MB独显）","万毫安青海湖电池+66W有线、内置主动散热风扇+VC均热板、支持充电分离"],
  "why":"荣耀首次切入8英寸游戏小平板，与WIN手机组成电竞生态，把主动散热与万毫安带入小屏阵营。",
  "relevance":"代表国产小平板从影音向重载游戏性能转型，对SoC、散热、电池快充供应链有牵引。",
  "vendor":"荣耀/HONOR WIN平板","date":"2026-10","url":"https://www.toutiao.com/article/7692850956890849819/",
  "source_name":"今日头条(科技衍生)","source_detail":"科技衍生(D级)、腾讯搜一搜同文(E级)",
  "note":"具体分辨率/最终定价待10月发布会确认；工程参数以预热稿为准。"},

 {"region":"cn","title":"小米平板9 Pro预售：12.5英寸3.2K、第五代骁龙8、11000mAh","category":"平板","main_dim":"SoC/芯片",
  "dims":"SoC/芯片|显示/OLED|电池/快充|AI/NPU","status":"已上市","stars":4,"grade":"B",
  "corroboration":"3（IT之家、百度百科、CNMO）","signal_type":"发售",
  "key_params":"12.5英寸3.2K护眼屏、第五代骁龙8、11000mAh电池、HyperOS 4+超级小爱2.0、3799元起",
  "tech_features":["12.5英寸大屏兼顾生产力与便携，全系3.2K高清护眼屏","第五代骁龙8旗舰平台，11000mAh大电池支持14.5h短视频/20h会议","HyperOS 4+超级小爱2.0，AI办公套件、跨端任务执行、WPS for Pad等PC级应用"],
  "why":"小米平板数字系列首次在Pro版用上第五代骁龙8，11000mAh刷新安卓平板电池上限。",
  "relevance":"推动国产平板SoC与电池容量军备竞赛，AI办公生态向平板渗透。",
  "vendor":"小米/平板9 Pro","date":"2026-09-14","url":"https://www.toutiao.com/article/7685214266438025762",
  "source_name":"今日头条(IT之家)","source_detail":"IT之家(B级)、百度百科(D级)、CNMO(B级)",
  "note":""},

 {"region":"cn","title":"红魔游戏平板5 Pro：9.06英寸OLED 185Hz、骁龙8至尊版Gen5","category":"平板","main_dim":"显示/OLED",
  "dims":"显示/OLED|SoC/芯片|散热|电池/快充","status":"已上市","stars":4,"grade":"C",
  "corroboration":"3（太平洋电脑网、GSMchoice、life.tw）","signal_type":"发售",
  "key_params":"9.06英寸OLED 185Hz/300Hz触控、骁龙8至尊版Gen5(Adreno840)、8300mAh+80W、红芯R4、363g",
  "tech_features":["9.06英寸OLED 185Hz，1600nit局部峰值，SGS低蓝光护眼","骁龙8至尊版Gen5+红芯R4辅助芯片，主动散热风扇","8300mAh+80W有线、双USB-C、旁路充电、363g轻薄机身"],
  "why":"红魔将游戏手机主动散热与高刷OLED下放到小平板，定义电竞平板新形态。",
  "relevance":"强化国产游戏平板在SoC、散热、高刷OLED的差异化竞争。",
  "vendor":"努比亚/红魔游戏平板5 Pro","date":"2026-09","url":"https://product.pconline.com.cn/tabletpc/nubia/2844572_detail.html",
  "source_name":"太平洋电脑网","source_detail":"太平洋电脑网(C级)、GSMchoice(C级)、life.tw(B级)",
  "note":"国内具体发布日期以官方为准，参数页标注发布时间2026年。"},

 {"region":"cn","title":"台电T60 Mini开售：8.8英寸2.5K 90Hz、紫光展锐T7300、899元","category":"平板","main_dim":"显示/OLED",
  "dims":"显示/OLED|SoC/芯片|电池/快充|无线通信","status":"已上市","stars":4,"grade":"B",
  "corroboration":"2（IT之家/凤凰网、IT之家今日头条）","signal_type":"发售",
  "key_params":"8.8英寸2.5K(2560×1600)90Hz LCD、紫光展锐T7300八核、6000mAh+18W、899元",
  "tech_features":["8.8英寸2.5K 90Hz InCell全贴合，PPI 343，324g口袋机身","紫光展锐T7300八核(2.2GHz)，8+128GB、TF扩展","6000mAh+18W PD、双模4G双SIM、双频Wi-Fi 6/蓝牙5.4、北斗双频定位"],
  "why":"899元把2.5K高刷小屏平板打进千元内，国产化芯平板走量代表作。",
  "relevance":"展现国产入门平板在屏幕与通信(4G插卡)上的性价比打法。",
  "vendor":"台电/Teclast T60 Mini","date":"2026-09-20","url":"https://h5.ifeng.com/c/vivo/v002AgWbjWQBE9wsEe80fTfKuoUFHqKCOf4tn1vitOFrXY0__",
  "source_name":"凤凰网(IT之家)","source_detail":"IT之家(B级)、凤凰网(B级)、今日头条(IT之家,B级)",
  "note":""},

 {"region":"cn","title":"一加16定档10月12日：第六代骁龙8超级至尊版、9000mAh、185FPS","category":"手机","main_dim":"SoC/芯片",
  "dims":"SoC/芯片|显示/OLED|电池/快充|摄像头","status":"即将上市","stars":4,"grade":"B",
  "corroboration":"2（CNMO科技、Beebom）","signal_type":"新品发布",
  "key_params":"第六代骁龙8超级至尊版、第四代东方屏165Hz/185FPS、9000mAh+100W有线+50W无线、2亿主摄",
  "tech_features":["第六代骁龙8超级至尊版，安兔兔563万+，自研电竞三芯","第四代东方屏全局165Hz、游戏185FPS，2亿像素主摄","9000mAh冰川电池+100W有线+50W无线闪充，IP66/68/69、3D超声波指纹"],
  "why":"下半年性能旗舰标杆，把万级电池与185FPS游戏高刷带入主流旗舰。",
  "relevance":"牵引骁龙8EE6、高刷屏、百瓦有线+50W无线快充供应链。",
  "vendor":"一加/OnePlus 16","date":"2026-10-12","url":"https://www.toutiao.com/article/7694187656502051343",
  "source_name":"今日头条(CNMO科技)","source_detail":"CNMO科技(B级)、Beebom(B级)",
  "note":""},

 {"region":"cn","title":"红魔12 Pro+定档10月15日：屏下前摄、RGB水冷+风冷散热","category":"手机","main_dim":"散热",
  "dims":"散热|SoC/芯片|显示/OLED|电池/快充","status":"即将上市","stars":4,"grade":"B",
  "corroboration":"2（CNMO科技、快科技/网易）","signal_type":"新品发布",
  "key_params":"第六代骁龙8超级至尊版、第九代屏下全面屏0.96mm黑边、RGB水冷+风冷协同散热、8400mAh+120W+80W无线",
  "tech_features":["第九代屏下前摄，0.96mm极窄黑边，纯平镜头设计","RGB水冷+风冷协同散热系统，主打轻薄手感","第六代骁龙8超级至尊版，爆料8400mAh+120W有线+80W无线"],
  "why":"游戏手机在散热(水冷+风冷)与屏下摄像头形态上继续领跑。",
  "relevance":"推动主动散热、屏下摄像与高功率无线充电在手机端落地。",
  "vendor":"努比亚/红魔12 Pro+","date":"2026-10-15","url":"https://www.toutiao.com/article/7694187656502051343",
  "source_name":"今日头条(CNMO科技)","source_detail":"CNMO科技(B级)、快科技(B级)",
  "note":"电池容量(8400mAh)来自爆料，最终以发布会为准。"},

 {"region":"cn","title":"OPPO Watch X3开售：TC4钛合金+蓝宝石、16天续航、646mAh","category":"智能手表","main_dim":"结构/工艺",
  "dims":"结构/工艺|传感器|电池/快充|无线通信","status":"已上市","stars":3,"grade":"D",
  "corroboration":"1（科技衍生今日头条/腾讯搜一搜）","signal_type":"发售",
  "key_params":"1.5英寸LTPO OLED 466×466、TC4钛合金表圈/表体+蓝宝石镜、646mAh、长续航16天、7.5W磁吸、独立eSIM、5ATM/IP68/IP69",
  "tech_features":["TC4钛合金表圈与表体+蓝宝石水晶镜(莫氏8+)，11mm/70g","1.5英寸LTPO OLED，全局600nit/激发1500nit/运动3000nit，58类数据表盘","高精度健康传感器60秒体检14项+AI分析，646mAh长续航16天，7.5W磁吸、独立eSIM、5ATM/IP68/IP69"],
  "why":"OPPO旗舰手表走向钛合金+蓝宝石材质与长续航，强化健康运动定位。",
  "relevance":"带动智能手表钛合金结构、LTPO屏与eSIM独立通信供应链。",
  "vendor":"OPPO/Watch X3","date":"2026-10-12","url":"https://so.html5.qq.com/page/real/search_news?docid=70000021_3896acbbc9d75952",
  "source_name":"腾讯搜一搜(科技衍生)","source_detail":"科技衍生(D级)、腾讯搜一搜(E级)",
  "note":"单一信源，建议以OPPO官方页面二次印证价格与配色。"},

 {"region":"cn","title":"华为WATCH D3发布：腕部动态血压记录仪、二类医疗器械认证","category":"智能手表","main_dim":"传感器",
  "dims":"传感器|认证/合规|显示/OLED|电池/快充","status":"已上市","stars":4,"grade":"B",
  "corroboration":"2（泡泡网/网易、腾讯搜一搜同文）","signal_type":"发售",
  "key_params":"1.92英寸AMOLED、玄玑感知系统+腕带气囊、二类医疗器械+CE-MDR认证、540mAh、6天续航、11.3mm/40g、2988元",
  "tech_features":["业界首创轻扰动态血压(示波法微泵+PPG)，二类医疗器械+CE-MDR认证","玄玑感知系统+腕带气囊，微体检升级17项指标，新增高尿酸/冠心病风险评估","1.92英寸AMOLED 3000nit、540mAh常规6天/动态1天、11.3mm减薄15%、2988元起"],
  "why":"将医疗级动态血压监测带入消费手表，强化华为健康穿戴壁垒。",
  "relevance":"推动传感器(气囊/PPG)、医疗器械认证在智能手表落地。",
  "vendor":"华为/HUAWEI WATCH D3","date":"2026-10-01","url":"https://www.163.com/dy/article/L85ETVLD05128A8R.html",
  "source_name":"网易(泡泡网)","source_detail":"泡泡网(B级)、网易(D级)",
  "note":""},

 {"region":"cn","title":"Rokid第二代带显示AI眼镜定档10月27日：全功能AI+首秀数贸会","category":"AR-VR眼镜","main_dim":"AI/NPU",
  "dims":"AI/NPU|显示/OLED|摄像头|音频","status":"即将上市","stars":4,"grade":"B",
  "corroboration":"3（北京商报、上海证券报、VRAR星球）","signal_type":"新品发布(定档)",
  "key_params":"第二代带显示全功能AI眼镜，10月27日发布；延续拍摄/翻译/提词/导航/支付，性能更强续航更长佩戴更轻",
  "tech_features":["定位第二代带显示全功能AI眼镜，9月数贸会全球首秀","延续拍摄/翻译/提词/导航/支付核心能力并强化细分场景","发布会定档10月27日杭州，销售计划届时揭晓"],
  "why":"Rokid将带显示AI眼镜迭代，定义国内全功能AI眼镜产品范式。",
  "relevance":"牵引Micro-LED显示、端侧AI与轻量化眼镜供应链。",
  "vendor":"Rokid/乐奇第二代AI眼镜","date":"2026-10-27","url":"https://www.toutiao.com/article/7690826935064199721",
  "source_name":"今日头条(北京商报)","source_detail":"北京商报(B级)、上海证券报(B级)、VRAR星球(C级)",
  "note":"具体光学/芯片/重量参数待10月27日发布会公布。"},

 {"region":"cn","title":"极米MemoMind One登陆56家门店：Micro-LED光波导、无摄像头办公AI眼镜","category":"AR-VR眼镜","main_dim":"显示/OLED",
  "dims":"显示/OLED|AI/NPU|音频","status":"已上市","stars":3,"grade":"C",
  "corroboration":"1（OFweek可穿戴）","signal_type":"发售",
  "key_params":"Micro-LED光波导、摒弃摄像头设计、主打翻译/录音转写/提词/导航、国庆期间全国56家线下门店",
  "tech_features":["Micro-LED光波导方案，轻量化无摄像头更合规","主打翻译、录音转写、提词、导航等实用办公功能","国庆期间登陆全国56家线下门店，走办公场景渠道"],
  "why":"极米以无摄像头光波导方案切入办公AI眼镜，规避隐私监管风险。",
  "relevance":"代表国内AI眼镜'去摄像头+光波导'的合规化产品路线。",
  "vendor":"极米/MemoMind One","date":"2026-10","url":"https://wearable.ofweek.com/2026-10/ART-8440-5011-30706040.html",
  "source_name":"OFweek可穿戴设备网","source_detail":"OFweek可穿戴(C级)",
  "note":"具体重量/续航/芯片参数信源未披露。"},

 {"region":"cn","title":"雷神AI Master M7000移动工作站：锐龙AI Max+395、64GB驯服120B模型","category":"笔记本电脑","main_dim":"AI/NPU",
  "dims":"AI/NPU|SoC/芯片|散热|BMS/电源|显示/OLED","status":"已上市","stars":4,"grade":"B",
  "corroboration":"3（站长之家、AIbase、凤凰网/IT之家）","signal_type":"发售",
  "key_params":"AMD锐龙AI Max+395、64GB LPDDR5X+85GB AI SSD、本地跑120B MoE、16英寸2.5K 165Hz、99Wh、160W、19900元(国补)",
  "tech_features":["锐龙AI Max+395(50 TOPS XDNA2)，64GB内存+85GB SLC AI Cache","群联aiDaptiv+把SSD当显存延伸，本地部署GPT-OSS-120B","16英寸2.5K 165Hz 500nit、99Wh电池、2风扇3热管160W、OCuLink/2.5GbE"],
  "why":"首款把120B大模型塞进2.45kg背包的国产AI移动工作站，定义端侧算力新形态。",
  "relevance":"推动AI PC从云端回归本地，带动统一内存/AI SSD/BMS架构。",
  "vendor":"雷神/Thunderobot AI Master M7000","date":"2026-09-21","url":"https://www.chinaz.com/ainews/31197.shtml",
  "source_name":"站长之家","source_detail":"站长之家(B级)、AIbase(B级)、凤凰网/IT之家(B级)",
  "note":""},

 {"region":"cn","title":"荣耀MagicBook Pro 16极客版开卖：Ultra5 125H、3K 165Hz、补贴5099","category":"笔记本电脑","main_dim":"显示/OLED",
  "dims":"显示/OLED|SoC/芯片|电池/快充|音频","status":"已上市","stars":3,"grade":"C",
  "corroboration":"2（超能网今日头条、笔记本评测网）","signal_type":"发售",
  "key_params":"酷睿Ultra5 125H(14核18线程)、16英寸3K 165Hz IPS 100% DCI-P3、75Wh、1.79kg、六扬声器空间音频、补贴5099元起",
  "tech_features":["16英寸3K@165Hz IPS，10bit/500nit/100% DCI-P3、HDR400+莱茵护眼","酷睿Ultra5 125H 14核18线程，16+512GB，75Wh电池、Wi-Fi 6E","1.79kg/17.9mm，立体散热(3D复合热管+双百叶风扇)，六扬声器空间音频渲染"],
  "why":"荣耀把3K高刷与空间音频下放到5K价位的轻薄创作本。",
  "relevance":"反映国产轻薄本在高刷屏、空间音频与国补定价上的竞争。",
  "vendor":"荣耀/HONOR MagicBook Pro 16 极客版","date":"2026-09-29","url":"https://www.toutiao.com/article/7690784929147372073/",
  "source_name":"今日头条(超能网)","source_detail":"超能网(C级)、笔记本评测网(C级)",
  "note":""},

 {"region":"cn","title":"绿联新款二合一折叠无线充：25W Qi2.2磁吸、对标MagSafe Duo","category":"无线充","main_dim":"电池/快充",
  "dims":"电池/快充|结构/工艺","status":"已上市","stars":4,"grade":"B",
  "corroboration":"3（IT之家、快科技、9to5Toys）","signal_type":"新品发布",
  "key_params":"25W Qi2.2磁吸无线充、二合一折叠(手机+AirPods 5W)、折叠6.02×7.26×2.67cm、玻璃面板、59.99美元",
  "tech_features":["支持最新Qi2.2标准，最高25W磁吸无线充电","二合一折叠：主区手机+副区5W耳机，可作支架","折叠仅6.02×7.26×2.67cm，玻璃面板，过充/过压/短路/异物检测"],
  "why":"国内配件厂率先跟进Qi2.2，填补苹果MagSafe Duo退市后的二合一磁吸空档。",
  "relevance":"牵引国产无线充电配件向Qi2.2高功率磁吸升级。",
  "vendor":"绿联/UGREEN Qi2.2二合一折叠无线充","date":"2026-08-29","url":"https://www.toutiao.com/article/7679469407357125158",
  "source_name":"今日头条(IT之家)","source_detail":"IT之家(B级)、快科技(B级)、9to5Toys(B级)",
  "note":"首发面向美国市场，国行上市时间待确认。"},

 {"region":"cn","title":"天猫精灵X6：通义大模型AI音箱、双喇叭天空音架构","category":"智能音箱","main_dim":"音频",
  "dims":"音频|AI/NPU","status":"已上市","stars":3,"grade":"D",
  "corroboration":"2（什么值得买评测、未来精灵品牌资讯）","signal_type":"发售",
  "key_params":"通义千问大模型、10W高音+20W低音双喇叭天空音架构、Hi-Res认证、约300元档",
  "tech_features":["接入阿里通义大模型，支持多轮对话与跨内容源在线搜索","10W高音+20W低音双喇叭+1.1声道天空音架构，过Hi-Res","AliGenie 6.0系统，智能家居控制，300元内性价比定位"],
  "why":"阿里把大模型下沉到三百元档音箱，重定义入门AI音箱交互。",
  "relevance":"体现国产智能音箱从语音遥控器向AI助手的转型。",
  "vendor":"天猫精灵/Tmall Genie X6","date":"2026-09","url":"https://post.smzdm.com/p/azze58lp/",
  "source_name":"什么值得买","source_detail":"什么值得买(D级社区评测)、AIBase(B级品牌资讯)",
  "note":"评测稿见2026年初，2026年内密集上市；精确首发月份信源未明确。"},

 {"region":"cn","title":"韶音OpenFit 2 AI亮相云栖：Qwen大模型、会议纪要与实时翻译","category":"AI耳机·耳穿戴","main_dim":"音频",
  "dims":"音频|AI/NPU|传感器|无线通信","status":"已上市","stars":4,"grade":"B",
  "corroboration":"4（IT之家/新浪、钱江晚报、中国经济新闻网、GoodNav）","signal_type":"曝光/发售",
  "key_params":"Qwen大模型、长时录音+AI会议总结+实时翻译、1398元、IP55、9.4g、21×11mm单元、蓝牙5.4、48h续航、四麦克风",
  "tech_features":["Qwen大模型底座，长时录音/AI会议总结/多语种实时翻译，12行业热词调优+19套纪要模板","AI实验室：智能对话/日程待办/随口记/消息助手，双击唤醒耳边AI","21×11mm复合振膜+定向传音，IP55、9.4g、蓝牙5.4双设备、单耳11h/总48h、四麦克风降噪"],
  "why":"韶音首款AI耳机把端侧大模型会议转写/翻译带入开放式耳机，定义耳边AI生产力。",
  "relevance":"代表AI耳机与平板/手机协同的端侧音频AI方向，牵引麦克风阵列与低功耗AI。",
  "vendor":"韶音/Shokz OpenFit 2 AI","date":"2026-09-22","url":"https://finance.sina.cn/tech/2026-09-23/detail-inisunsp1433984.d.html?vt=4",
  "source_name":"新浪科技(IT之家)","source_detail":"IT之家(B级)、钱江晚报(B级)、中国经济新闻网(B级)、GoodNav(C级)",
  "note":"AI实验室功能后续通过固件推送。"},

 # ===================== 国际 15 条 =====================
 {"region":"intl","title":"Acer Iconia Tab 11 5G：10.95吋90Hz IPS + 5G + 2TB microSD 扩展","category":"平板","main_dim":"显示/OLED",
  "dims":"显示/OLED|无线通信|电池/快充","status":"已上市","stars":4,"grade":"B",
  "corroboration":"NotebookCheck(B)+Acer印度官网(A)双源印证","signal_type":"官方发布（印度上市）",
  "key_params":"10.95吋1920×1200 90Hz 450nits IPS、MediaTek 8755、8GB+128/256GB、5G通话、7400mAh+18W、最高2TB microSD，印度₹23,999起",
  "tech_features":["10.95英寸90Hz IPS面板，450尼特峰值亮度，金属机身8.2mm/500g","支持5G蜂窝通话+独立SIM/混合卡槽，最高2TB microSD扩展","7400mAh电池+18W充电，四扬声器、侧边指纹、Android 16"],
  "why":"在入门价位提供5G与超大本地存储扩展，反趋势保留microSD，适合离线数据终端场景。",
  "relevance":"海外中端安卓平板在 connectivity 与存储上的差异化打法，值得关注供应链成本结构。",
  "vendor":"Acer / Iconia Tab 11 5G","date":"2026-10-10","url":"https://www.notebookcheck.net/Acer-officially-launches-5G-tablet-with-up-to-2TB-expandable-storage.1420411.0.html",
  "source_name":"NotebookCheck","source_detail":"NotebookCheck 于2026-10-10报导，并引用Acer印度官网规格与定价",
  "note":"Acer印度官网为A级信源，提供参数与价格印证"},

 {"region":"intl","title":"Lenovo Yoga Tab Plus Gen 2：骁龙8 Elite + 13吋4K 144Hz + 7年更新","category":"平板","main_dim":"SoC/芯片",
  "dims":"SoC/芯片|显示/OLED|电池/快充|手写笔/触控","status":"已上市","stars":4,"grade":"B",
  "corroboration":"NotebookCheck(B)引用联想IFA发布与官方页面","signal_type":"IFA 2026发布 + 美国首降",
  "key_params":"13吋3840×2560 144Hz 1100nits Dolby Vision、骁龙8 Elite、12/16GB+256/512GB、12700mAh、Tab Pen Pro 2、Android17承诺7年更新，美国$799.99(降后)",
  "tech_features":["高通骁龙8 Elite旗舰SoC，13英寸4K 144Hz LCD，1100尼特HDR，100% DCI-P3，杜比视界","12700mAh大电池，6扬声器哈曼卡顿，标配Tab Pen Pro 2与磁吸键盘","出厂Android 17，承诺升级至Android 24并7年安全更新，支持Wi-Fi 7与8192级压感笔"],
  "why":"安卓平板首次在旗舰SoC+4K高刷屏上承诺iPhone级7年系统支持，冲击高端创作平板。",
  "relevance":"与Galaxy Tab S旗舰、iPad Pro形成高端安卓阵营对标，关注SoC/显示/长周期支持趋势。",
  "vendor":"Lenovo / Yoga Tab Plus Gen 2","date":"2026-09","url":"https://www.notebookcheck.net/Lenovo-s-flagship-Android-tablet-with-Snapdragon-8-Elite-and-4K-display-gets-a-200-discount.1414587.0.html",
  "source_name":"NotebookCheck","source_detail":"NotebookCheck 2026-10-03报导美国首降，并引用联想IFA 2026发布与官方规格页",
  "note":"同系Yoga Tab Gen 2(天玑9500s/11吋)为已被去重的相近型号，本条目仅取Plus Gen 2"},

 {"region":"intl","title":"Samsung Galaxy Tab A11：8.7吋90Hz + Helio G99 + 7年系统更新 印度上市","category":"平板","main_dim":"显示/OLED",
  "dims":"显示/OLED|电池/快充|认证/合规","status":"已上市","stars":3,"grade":"C",
  "corroboration":"Gizbot单源，附印度定价","signal_type":"媒体曝光（上市）",
  "key_params":"8.7吋1340×800 TFT 90Hz、Helio G99、最高8GB+128GB、5100mAh+15W、承诺7年OS更新，印度₹12,999起",
  "tech_features":["8.7英寸HD+ TFT 90Hz（前代60Hz），前置5MP/后置8MP，337g轻机身","MediaTek Helio G99，最高8GB RAM+128GB，microSD扩展至2TB","5100mAh+15W充电，Dolby双扬声器，One UI 7/Android 15，三星承诺7年系统更新"],
  "why":"三星将旗舰级7年系统更新下放到入门A系列，拉长低端平板生命周期。",
  "relevance":"入门平板软件支持周期拉长，影响以旧换新与二手残值策略。",
  "vendor":"Samsung / Galaxy Tab A11","date":"2026-10-09","url":"https://www.gizbot.com/amphtml/news/samsung-galaxy-tab-a11-launched-in-india-with-90hz-display-and-7-years-of-os-updates-119061.html",
  "source_name":"Gizbot","source_detail":"Gizbot 2026-10-09报导印度上市与完整定价",
  "note":"Tab A11+（11吋）已于2026年初上市，不在本窗口，故仅取A11"},

 {"region":"intl","title":"REDMI两款新平板现身EEC认证，预计10月前后登陆海外市场","category":"平板","main_dim":"认证/合规",
  "dims":"认证/合规|无线通信","status":"即将上市","stars":3,"grade":"C",
  "corroboration":"腾讯新闻(引CNMO/外媒)单源","signal_type":"EEC认证曝光",
  "key_params":"型号2610FRP38G与26104RPF2G于2026-09-11完成EEC注册（通知号KZ0000014997），REDMI为全球市场做准备，预计10月前后上市",
  "tech_features":["两款REDMI平板均由小米通讯注册于欧亚经济委员会(EEC)数据库","型号以\"2610\"开头，外媒推测2026年10月前后进入市场","认证页仅公布型号，未披露具体名称/规格/售价，市场定位待定"],
  "why":"REDMI平板加速出海，补全小米海外平板矩阵，后续或与POCO等渠道协同。",
  "relevance":"关注海外中端安卓平板供给增量，对供应链与渠道有指示意义。",
  "vendor":"Xiaomi REDMI / 两款未命名平板 (2610FRP38G, 26104RPF2G)","date":"2026-09-15","url":"https://news.qq.com/rain/a/20260915A07LMW00",
  "source_name":"腾讯新闻(引CNMO科技)","source_detail":"腾讯新闻2026-09-15刊发，引用外媒对EEC数据库的披露",
  "note":"为认证/出海信号，规格尚未公开，需后续上市稿印证"},

 {"region":"intl","title":"Sony Xperia 10 VIII： brighter 120Hz OLED + 立体声升级 + Gemini，10月全球开售","category":"手机","main_dim":"显示/OLED",
  "dims":"显示/OLED|音频|电池/快充|AI/NPU","status":"已上市","stars":5,"grade":"A",
  "corroboration":"Sony新加坡官网(A)+pcnmobile+kimovil多源印证","signal_type":"官方发布（上市）",
  "key_params":"6.1吋FHD+ 120Hz OLED（较前代亮约50%）、骁龙6 Gen3、8GB+128GB(可6GB虚拟)、5000mAh两天续航、IPX5/8+GG Victus2，S$799",
  "tech_features":["6.1英寸19.5:9 FHD+ OLED 120Hz，亮度较前代提升约50%并随环境自动调色","前置立体声扬声器音量+15%、低频+30%，保留3.5mm与LDAC/Hi-Res","集成Google Gemini、Circle to Search、Ask Photos，5000mAh支持两天续航"],
  "why":"索尼中端机坚持OLED+3.5mm+两年系统更新的长寿命策略，海外小屏细分市场标杆。",
  "relevance":"显示/音频/AI助手在主流机型的落地组合，对中端机规格基线有参考。",
  "vendor":"Sony / Xperia 10 VIII","date":"2026-10-06","url":"https://www.sony.com.sg/pressrelease?prName=sony-launches-xperia-10-viii-with-a-focus-on-improving-everyday-ease-of-use",
  "source_name":"Sony Singapore 官方新闻稿","source_detail":"Sony新加坡官网2026-10-06发布，含完整规格、定价与区域上市信息",
  "note":"pcnmobile/kimovil提供英版详细参数（50MP主摄+13MP超广、microSD 2TB）作为印证"},

 {"region":"intl","title":"Vivo V80：蔡司三摄 + 7200mAh + 144Hz OLED，中端影像机10/06发布","category":"手机","main_dim":"摄像头",
  "dims":"摄像头|显示/OLED|电池/快充|结构/工艺","status":"已上市","stars":3,"grade":"C",
  "corroboration":"AugustMan单源（含完整规格）","signal_type":"官方确认（10/06发布）",
  "key_params":"6.59吋OLED 144Hz 5000nits、骁龙7 Gen4、50MP主摄OIS+50MP长焦+8MP超广、50MP前摄、7200mAh+90W、IP68/69、6年更新",
  "tech_features":["蔡司光学三摄：50MP主摄(OIS)+50MP长焦+8MP超广，50MP前摄","6.59英寸OLED 144Hz，峰值亮度5000尼特，OriginOS 7(Android 17)","7200mAh BlueVolt电池+90W FlashCharge，IP68/IP69防护，最高6年系统升级"],
  "why":"中端机把蔡司影像+大电池+高亮高刷屏下放到主流价位，挤压同档竞品。",
  "relevance":"摄像头/显示/电池在中端机的堆料趋势，对影像与快充供应链有指示。",
  "vendor":"Vivo / V80","date":"2026-10-06","url":"https://www.augustman.com/my/gear/tech/upcoming-smartphones-in-october-2026-vivo-oneplus/",
  "source_name":"AugustMan","source_detail":"AugustMan 2026-10-08前瞻，列Vivo V80与OnePlus 16规格",
  "note":"与OnePlus 16同篇；V80定位中端影像，10月6日已发布"},

 {"region":"intl","title":"Garmin Enduro 4：1.4吋MIP+Power Sapphire太阳能，活动320h/智能90天超长续航","category":"智能手表","main_dim":"电池/快充",
  "dims":"电池/快充|BMS/电源|传感器|结构/工艺|显示/OLED","status":"已上市","stars":5,"grade":"A",
  "corroboration":"Garmin官网(A)+AndroidHeadlines+NotebookCheck印证","signal_type":"官方发布（上市）",
  "key_params":"1.4吋MIP 280×280+Power Sapphire太阳能、活动模式最高320h/智能模式90天（日光下）、64GB、ECG、10ATM、66g、钛圈，$899.99",
  "tech_features":["1.4英寸MIP屏+蓝宝石太阳能镜片，省电模式下日光充足可近乎无限续航","64GB存储、ECG、皮肤温度、SpO2传感器，100+运动模式，内置LED手电","51mm钛圈+玻纤聚合物壳仅66g，10ATM防水，Garmin Pay(NFC)，新增Garmin Epic多日活动记录"],
  "why":"将超长续航与旗舰传感器（ECG/温感/64GB）结合，定义超耐力智能表新基准。",
  "relevance":"电池/BMS/传感器/结构工艺集成度极高的标杆，供可穿戴功耗与材料参考。",
  "vendor":"Garmin / Enduro 4","date":"2026-10-09","url":"https://www.garmin.com/en-US/newsroom/press-release/outdoor/enduro-4-smartwatch-redefines-ultraperformance-with-extreme-battery-life-and-advanced-training-features/",
  "source_name":"Garmin 官方新闻室","source_detail":"Garmin 2026-10-06发布、10-09全球开售，PRNewswire分发；AndroidHeadlines/NotebookCheck跟进",
  "note":"较Enduro 3内存+50%、地图引擎+30%平移速度"},

 {"region":"intl","title":"Garmin Approach S72：双尺寸AMOLED高尔夫智能表，首搭扬声器/麦克风与挥杆指标","category":"智能手表","main_dim":"传感器",
  "dims":"传感器|显示/OLED|电池/快充|音频","status":"已上市","stars":5,"grade":"A",
  "corroboration":"Garmin官网(A)+AndroidHeadlines印证","signal_type":"官方发布（上市）",
  "key_params":"43/47mm AMOLED、实时心率+挥杆指标(手速/上杆/腕旋)、果岭读数、GPS关16天/球场20h、扬声器麦克风、$799.99起",
  "tech_features":["高尔夫生物数据：心率趋势回溯+挥杆指标（手速、上杆幅度、腕部旋转）","果岭读数（坡度方向/平均坡度%）、推杆分析、航拍图，需Garmin Golf会员","首次在Garmin高尔夫表加入扬声器与麦克风支持通话/语音指令，内置LED手电"],
  "why":"将专业高尔夫传感与健康穿戴融合，并补齐通话音频能力，拓展垂直运动可穿戴边界。",
  "relevance":"传感器(生物+运动学)+音频模组在垂直场景手表的集成范例。",
  "vendor":"Garmin / Approach S72","date":"2026-10-09","url":"https://www.garmin.com/en-US/newsroom/press-release/outdoor/meet-approach-s72-garmins-ultimate-golf-smartwatch/",
  "source_name":"Garmin 官方新闻室","source_detail":"Garmin 2026-10-06发布、10-09开售，PRNewswire分发",
  "note":"47mm版本建议零售$799.99，43mm同价；ECG与连续血氧也具备"},

 {"region":"intl","title":"Ray-Ban Meta Audio：无摄像头AI音频眼镜，43g/12h，Muse语音助手","category":"AR-VR眼镜","main_dim":"音频",
  "dims":"音频|AI/NPU|无线通信|结构/工艺","status":"即将上市","stars":4,"grade":"B",
  "corroboration":"TechTimes(B)+Smart Glasses Daily(C)印证","signal_type":"Meta Connect 2026发布",
  "key_params":"无摄像头、开放声场音频、Muse AI语音助手、43g、12h续航(充电盒+48h)、23种框型/镜片，$349，10/13发货",
  "tech_features":["彻底移除摄像头，仅保留开放声场音频+音乐/播客+通话，回应隐私争议","内置Muse AI语音助手，Ray-Ban Clubmaster/Burbank框型，处方镜片兼容","43g轻量、12小时续航（充电盒总计48小时），可调节鼻托与铰链"],
  "why":"智能眼镜从'摄像+AR'转向'无摄音频AI'形态，开辟隐私友好型可穿戴新品类。",
  "relevance":"音频+端侧AI助手在眼镜形态的产品化，对AI耳机/耳穿戴赛道有外溢启示。",
  "vendor":"Meta × Ray-Ban / Meta Audio","date":"2026-09-28","url":"https://www.techtimes.com/articles/328012/20260924/meta-vr-glasses-camera-free-audio-specs-keychain-ai-lead-connect-2026-haul.htm",
  "source_name":"TechTimes","source_detail":"TechTimes 2026-09-24 Connect报道；Smart Glasses Daily 2026-10-02补充发布日期与重量",
  "note":"与Meta VR Glasses(已去重)为不同产品线，本条仅取无摄音频款"},

 {"region":"intl","title":"Ray-Ban Meta Gen 3：12MP 3K摄像 + 六麦克风阵列 + 9h续航，Aviator新框型","category":"AR-VR眼镜","main_dim":"摄像头",
  "dims":"摄像头|音频|电池/快充|AI/NPU|无线通信","status":"已上市","stars":4,"grade":"B",
  "corroboration":"TechTimes(B)单篇覆盖Gen3/Display/Audio多型号","signal_type":"Meta Connect 2026发布",
  "key_params":"12MP 3K视频、六麦克风阵列(降噪>90%)、9h续航、专用AI按键、Dolby Atmos录音、$449起，新增Aviator/Zena框型",
  "tech_features":["12MP摄像头支持3K视频，六麦克风阵列宣称环境噪声抑制超90%","新增专用Meta AI按键，Dolby Atmos空间音频录音，全线摄像款支持","新增Ray-Ban Aviator与Zena猫眼框型，含Kylie Jenner/Lisa联名，续航8→9h"],
  "why":"主流摄像智能眼镜的代际升级，强化录音与AI入口，推动可穿戴影像标准化。",
  "relevance":"摄像头+阵列麦+端侧AI在眼镜形态的工程取舍，对手机/耳机传感有借鉴。",
  "vendor":"Meta × Ray-Ban / Meta Gen 3","date":"2026-09-23","url":"https://www.techtimes.com/articles/328012/20260924/meta-vr-glasses-camera-free-audio-specs-keychain-ai-lead-connect-2026-haul.htm",
  "source_name":"TechTimes","source_detail":"TechTimes 2026-09-24 Connect报道，覆盖Gen3/Display/Audio/Adventurer全系",
  "note":"同日Meta Display($799 HUD款)亦在文中，但本条聚焦Gen3摄像款"},

 {"region":"intl","title":"ASUS Vivobook 16 2026 Ryzen Edition：锐龙7 H260 + 2.5K 144Hz + 38 TOPS NPU","category":"笔记本电脑","main_dim":"AI/NPU",
  "dims":"AI/NPU|SoC/芯片|显示/OLED","status":"已上市","stars":3,"grade":"C",
  "corroboration":"PC Central单源（含完整规格）","signal_type":"媒体曝光（中国上市）",
  "key_params":"16吋2560×1600 144Hz 100%sRGB、锐龙7 H260(4nm,5.1GHz)、Radeon 780M、16GB LPDDR5、NPU 16 TOPS(系统38 TOPS)、5599元起",
  "tech_features":["AMD锐龙7 H260（8核16线程，4nm，5.1GHz），Radeon 780M iGPU 2.7GHz","NPU 16 TOPS，系统总AI算力38 TOPS，面向Copilot+本地推理","16英寸2.5K 144Hz 100%sRGB低蓝光屏，15.9mm/1.65kg，双USB-C+双USB-A+HDMI2.1"],
  "why":"主流价位笔电普及高刷屏与NPU，AI PC下沉至千元级市场。",
  "relevance":"AI/NPU与高刷显示在中端笔电的渗透，关注AMD平台AI PC成本曲线。",
  "vendor":"ASUS / Vivobook 16 2026 Ryzen Edition","date":"2026-10-07","url":"https://pccentral.net/asus-vibook-16-2026-ryzen-edition-launches-with-5-1ghz-chip-and-144hz-display-for-around-834",
  "source_name":"PC Central","source_detail":"PC Central 2026-10-07报导中国上市，含售价与完整规格",
  "note":"中国首发，国际版预计后续；同系Vivobook S14/S16骁龙版10月印度上市"},

 {"region":"intl","title":"ASUS Vivobook 14 Flip (TP3407AA)：360°翻转OLED + 酷睿Ultra7 49 TOPS NPU + 38h","category":"笔记本电脑","main_dim":"AI/NPU",
  "dims":"AI/NPU|显示/OLED|电池/快充|手写笔/触控","status":"已上市","stars":3,"grade":"C",
  "corroboration":"91mobiles单源（印度发布）","signal_type":"官方发布（印度）",
  "key_params":"14吋FHD+ ASUS OLED触控翻转、酷睿Ultra7 Series3 355(49 TOPS NPU)、最高38h、Thunderbolt4、TPM2.0、AI摄像头，₹179,990",
  "tech_features":["360°全金属翻转，FHD+ ASUS OLED触控屏，支持主动笔","英特尔酷睿Ultra7 Series3 355，NPU达49 TOPS，整机AI性能领先","最长38小时续航、Thunderbolt 4、microSD、TPM 2.0、带物理遮挡的AI摄像头"],
  "why":"翻转形态+高NPU算力+长续航，定义主流创作/学生AI本新基线。",
  "relevance":"AI/NPU笔电的形态(翻转/OLED)与续航整合趋势。",
  "vendor":"ASUS / Vivobook 14 Flip (TP3407AA)","date":"2026-09-16","url":"https://www.91mobiles.com/hub/asus-launches-new-vivobook-lineup-in-india/",
  "source_name":"91mobiles","source_detail":"91mobiles 2026-09-16报导ASUS印度Vivobook全系发布与定价",
  "note":"同发布还有Vivobook S14 Flip(骁龙X 45 TOPS)与Vivobook 16(锐龙7840HS 10 TOPS)"},

 {"region":"intl","title":"Belkin UltraCharge Pro Qi2 25W 三合一磁吸充电坞（WIZ040）","category":"无线充","main_dim":"电池/快充",
  "dims":"电池/快充|散热|认证/合规","status":"已上市","stars":3,"grade":"C",
  "corroboration":"techbizblogs(转Belkin日本发布)+WPC官方Qi2认证","signal_type":"配件发布（iPhone 18系列）",
  "key_params":"WPC官方Qi2 25W认证三合一坞，iPhone 0-50%约25分钟、Apple Watch S10 80%约30分钟，ChillBoost风扇降温最高7°C，₹18,173(免税)",
  "tech_features":["WPC官方Qi2 25W认证，可同时为iPhone/Apple Watch/AirPods充电","业界首搭散热风扇+ChillBoost™，降温最高7°C，缩短充电约4分钟","金属框架+软触材质，可调角度，Belkin SmartProtect安全系统"],
  "why":"Qi2 25W进入'带主动散热'阶段，反映高功率无线充的温控刚需。",
  "relevance":"无线充功率提升后的散热/认证趋势，对BMS与充电管理有参考。",
  "vendor":"Belkin / UltraCharge Pro Qi2 25W 3-in-1 Dock (WIZ040)","date":"2026-09","url":"https://techbizblogs.com/belkin-introduces-comprehensive-accessory-collection-for-iphone-18-pro-series/",
  "source_name":"Tech Biz Blogs (Belkin日本发布转引)","source_detail":"techbizblogs 2026-09-14刊发Belkin配件系列，含WIZ040规格；WPC官方Qi2认证为底",
  "note":"同系列还有UltraCharge Qi2 25W 10000mAh磁吸移动电源(BPD022)"},

 {"region":"intl","title":"Amazon 新Echo系列（Echo Dot Max / Echo Studio）全球开售，AZ3芯片+Alexa+","category":"智能音箱","main_dim":"AI/NPU",
  "dims":"AI/NPU|音频|传感器|无线通信","status":"已上市","stars":4,"grade":"A",
  "corroboration":"Amazon官方新闻室(A)+10月初全球开售信号(多家媒体)","signal_type":"官方发布 + 10月全球开售",
  "key_params":"自研AZ3/AZ3 Pro芯片、Omnisense传感(音频/超声/WiFi雷达/加速度)、Echo Dot Max约3倍低音、Echo Studio杜比全景声、内置Zigbee/Thread/Matter中枢",
  "tech_features":["自研AZ3( Echo Dot Max)/AZ3 Pro( Echo Studio)芯片，唤醒词识别+约50%、端侧AI处理","Omnisense传感平台：音频+超声+WiFi雷达+加速度，实现存在/运动/温度感知的主动智能家居","Echo Dot Max首次内置智能家庭中枢，支持Zigbee/Thread/Matter/BT；Echo Studio杜比全景声 compact机身"],
  "why":"智能音箱从'语音播放'升级为'端侧AI+环境感知中枢'，AZ3自研芯片是关键。",
  "relevance":"端侧NPU+多模传感在智能家居入口的集成，对标其他品牌的本地AI助手。",
  "vendor":"Amazon / Echo Dot Max · Echo Studio","date":"2026-10","url":"https://press.aboutamazon.com/in/2026/6/amazon-launches-echo-dot-max-and-echo-studio-featuring-premium-audio-and-new-modern-design",
  "source_name":"Amazon 全球新闻中心","source_detail":"Amazon 2026-05-27印度发布新闻室；10月初多市场(含Echo Show 8/11)开售为窗口内信号",
  "note":"印度首发为5月，本窗口信号为10月初四款新Echo全球范围开售；Echo Show 8/11含1300万摄像头与Omnisense"},

 {"region":"intl","title":"Sony LinkBuds Clip 鎏光金中国限定新色：耳夹式AI通话降噪真无线","category":"AI耳机·耳穿戴","main_dim":"音频",
  "dims":"音频|AI/NPU|电池/快充|无线通信","status":"已上市","stars":4,"grade":"C",
  "corroboration":"极客公园(C,10/09限定色)+Sony印度官方(A,产品AI规格)印证","signal_type":"官方新配色上市（窗口内）",
  "key_params":"耳夹开放式、AI-DNN降噪+骨声纹VPU、10mm单元、DSEE、360 Reality Audio、37h(9h+28h)、IPX4、蓝牙5.3多点，2026-10-09限定金上市",
  "tech_features":["基于AI的深度神经网络(DNN)降噪算法，双麦+新一代骨声纹VPU精准拾音，嘈杂环境通话清晰","耳夹开放式设计，三种聆听模式(标准/人声增强/漏音抑制)，10mm驱动单元+360临场音效","综合续航约37小时(单次9h)，充电3分钟用1小时，IPX4防水，蓝牙5.3多点，支持Gemini"],
  "why":"开放式耳夹形态+端侧AI通话降噪，代表AI耳机从入耳降噪转向'环境感知+清晰通话'。",
  "relevance":"音频(含AI耳机声学)维度标杆：DNN降噪+VPU骨传导+长续航的集成方案。",
  "vendor":"Sony / LinkBuds Clip（鎏光金限定色）","date":"2026-10-09","url":"https://www.geekpark.net/news/372177",
  "source_name":"极客公园 (GeekPark)","source_detail":"极客公园2026-10-09报导LinkBuds Clip鎏光金中国限定新色上市；AI声学规格与Sony印度官方7月发布稿一致",
  "note":"本条为限定色窗口内信号，AI声学参数引自Sony官方(A)产品发布"},
]

# ---------- 清洗：去除花括号 ----------
def clean(s):
    if isinstance(s, str):
        return s.replace("{", "").replace("}", "")
    if isinstance(s, list):
        return [clean(x) for x in s]
    return s
for d in DATA:
    for k, v in list(d.items()):
        d[k] = clean(v)

# ---------- 维度计数 ----------
dim_count = {dm: 0 for dm in DIMS}
for d in DATA:
    parts = [p.strip() for p in d["dims"].split("|")]
    for p in parts:
        if p in dim_count:
            dim_count[p] += 1
covered = sum(1 for dm in DIMS if dim_count[dm] > 0)
grade_count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for d in DATA:
    grade_count[d["grade"]] += 1
five_star = sum(1 for d in DATA if d["stars"] == 5)

# ---------- 排序（区内按状态→时间倒序） ----------
def sort_key(d):
    return (STATUS_RANK.get(d["status"], 9), -skey(d["date"]))
cn = sorted([d for d in DATA if d["region"]=="cn"], key=sort_key)
intl = sorted([d for d in DATA if d["region"]=="intl"], key=sort_key)
ordered = cn + intl  # card-1..15 = cn, 16..30 = intl

# ---------- Top5 ----------
def top_sort(d):
    gr = {"A":0,"B":1,"C":2,"D":3,"E":4}[d["grade"]]
    return (-d["stars"], gr, STATUS_RANK.get(d["status"],9), -skey(d["date"]))
top5 = sorted(DATA, key=top_sort)[:5]

# ---------- HTML 渲染 ----------
def stars(n):
    return "★" * n

def status_tag(status):
    if status == "即将上市":
        return '<span class="status-tag status-coming">即将上市</span>'
    if status == "进行中":
        return '<span class="status-tag status-progress">进行中</span>'
    return ""  # 已上市 不显示标签

def region_tag(region):
    if region == "cn":
        return '<span class="td-region region-cn">国内</span>'
    return '<span class="td-region region-intl">国际</span>'

def source_tag(g):
    return '<span class="source-tag source-%s">%s</span>' % (g.lower(), g)

def card_html(d, idx, expanded):
    n = idx
    cls = "intel-card %s%s" % (d["region"], " expanded" if expanded else "")
    tf = "".join('<li data-num="%s">%s</li>' % (chr(0x2460+i), t) for i, t in enumerate(d["tech_features"]))
    status_badge = ('<span class="status-tag status-coming">即将上市</span>' if d["status"]=="即将上市"
                   else '<span class="status-tag status-progress">进行中</span>' if d["status"]=="进行中" else "")
    return '''<!-- Card %(n)d: %(title)s -->
      <div class="%(cls)s" id="card-%(n)d">
        <div class="card-header" onclick="toggleCard('card-%(n)d')">
          <div class="card-num">%(n)d</div>
          <div class="card-title-area">
            <div class="card-title">%(title)s</div>
            <div class="card-badges">
              %(stag)s
              <span class="card-domain">%(domain)s</span>
              <span class="stars">%(stars)s</span>
              %(sbadge)s
            </div>
          </div>
          <span class="card-toggle">▼</span>
        </div>
        <div class="card-body">
          <div class="card-content">
            <div class="field-grid">
              <div class="field"><div class="field-label">信号类型</div><div class="field-value">%(stype)s</div></div>
              <div class="field"><div class="field-label">印证源数</div><div class="field-value">%(corr)s</div></div>
              <div class="field full"><div class="field-label">关键参数</div><div class="field-value">%(kp)s</div></div>
              <div class="field full"><div class="field-label">技术特性</div><div class="field-value"><ul class="tech-list">%(tf)s</ul></div></div>
              <div class="field full"><div class="field-label">为什么重要</div><div class="field-value">%(why)s</div></div>
              <div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">%(rel)s</div></div>
              <div class="field"><div class="field-label">厂商/型号</div><div class="field-value">%(vendor)s</div></div>
              <div class="field"><div class="field-label">时间</div><div class="field-value">%(date)s</div></div>
              <div class="field"><div class="field-label">URL</div><div class="field-value"><a href="%(url)s" target="_blank">%(sname)s</a></div></div>
              <div class="field"><div class="field-label">信源明细</div><div class="field-value">%(sdetail)s</div></div>
              <div class="field full"><div class="field-label">备注待印证</div><div class="field-value">%(note)s</div></div>
            </div>
          </div>
        </div>
      </div>''' % {
        "n": n, "cls": cls, "title": d["title"], "stag": source_tag(d["grade"]),
        "domain": d["dims"].replace("|","/"), "stars": stars(d["stars"]), "sbadge": status_badge,
        "stype": d["signal_type"], "corr": d["corroboration"], "kp": d["key_params"],
        "tf": tf, "why": d["why"], "rel": d["relevance"], "vendor": d["vendor"],
        "date": d["date"], "url": d["url"], "sname": d["source_name"],
        "sdetail": d["source_detail"], "note": d["note"]
    }

def summary_row(n, d):
    return ('<tr><td>%d</td><td class="td-title"><a href="#card-%d">%s</a></td><td>%s</td>'
            '<td>%s</td><td class="td-status">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>') % (
        n, n, d["title"], region_tag(d["region"]), d["dims"].replace("|","/"),
        status_tag(d["status"]), source_tag(d["grade"]), d["date"], stars(d["stars"]))

# 维度面板
dim_chips = ""
for dm in DIMS:
    c = dim_count[dm]
    onoff = "on" if c > 0 else "off"
    dim_chips += '<div class="dim-chip %s">%s <span class="dim-count">%d条</span></div>' % (onoff, dm, c)

# Top5 面板
top_cards = ""
for i, d in enumerate(top5, 1):
    top_cards += '''      <div class="signal-card">
        <div><span class="sig-rank">%d</span><span class="sig-title">%s</span></div>
        <div class="sig-tags"><span class="sig-dim">%s</span><span class="sig-stars">%s</span></div>
        <div class="sig-key">%s</div>
      </div>''' % (i, d["title"], d["main_dim"], stars(d["stars"]), d["key_params"][:60])

# 卡片区
cn_cards = "\n".join(card_html(d, i+1, i==0) for i, d in enumerate(cn))
intl_cards = "\n".join(card_html(d, len(cn)+i+1, False) for i, d in enumerate(intl))
summary_rows = "\n".join(summary_row(i+1, d) for i, d in enumerate(ordered))

stat_a = grade_count["A"]; stat_b = grade_count["B"]

HTML = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>智能终端硬件情报日报 · %(TODAY)s</title>
<style>
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
  .header { background:linear-gradient(135deg,#667eea 0%%,#764ba2 100%%); color:#fff; border-radius:var(--radius); padding:28px 32px; margin-bottom:20px; box-shadow:var(--shadow); }
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
  .dim-bar { width:100%%; height:8px; background:#f0f2f5; border-radius:4px; margin-bottom:16px; overflow:hidden; }
  .dim-bar-fill { height:100%%; background:linear-gradient(90deg,#67c23a,#95d475); border-radius:4px; transition:width 0.5s; }
  .dim-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
  .dim-chip { padding:8px 12px; border-radius:8px; font-size:13px; font-weight:500; display:flex; justify-content:space-between; align-items:center; }
  .dim-chip.on { background:#f0f9eb; border:1px solid #c2e7b0; color:#67c23a; }
  .dim-chip.off { background:#f5f7fa; border:1px solid #e4e7ed; color:#c0c4cc; }
  .dim-chip .dim-count { font-size:11px; opacity:0.7; font-weight:400; }
  .summary-section { background:var(--card-bg); border-radius:var(--radius); padding:20px 24px; margin-bottom:24px; box-shadow:var(--shadow); }
  .section-title { font-size:16px; font-weight:700; margin-bottom:14px; display:flex; align-items:center; gap:8px; }
  .section-title::before { content:''; width:4px; height:18px; background:var(--primary); border-radius:2px; }
  table { width:100%%; border-collapse:collapse; font-size:13px; }
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
  .status-progress { background:#f4f4f5; color:#909399; border:1px solid #e4e7ed; }
  .intel-section { margin-bottom:24px; }
  .intel-cards { display:grid; grid-template-columns:1fr; gap:16px; }
  .intel-card { background:var(--card-bg); border-radius:var(--radius); box-shadow:var(--shadow); overflow:hidden; transition:box-shadow 0.3s; border-left:4px solid var(--primary); }
  .intel-card.cn { border-left-color:var(--tag-b); }
  .intel-card.intl { border-left-color:var(--tag-c); }
  .intel-card:hover { box-shadow:var(--shadow-hover); }
  .card-header { padding:16px 20px; cursor:pointer; display:flex; align-items:flex-start; gap:12px; user-select:none; }
  .card-num { flex-shrink:0; width:28px; height:28px; border-radius:50%%; background:#f0f2f5; color:var(--text-secondary); font-size:13px; font-weight:700; display:flex; align-items:center; justify-content:center; margin-top:2px; }
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
  .signal-card .sig-rank { display:inline-block; font-size:11px; font-weight:700; color:#fff; background:var(--success); border-radius:50%%; width:18px; height:18px; text-align:center; line-height:18px; margin-right:6px; }
  .signal-card .sig-title { font-size:13px; font-weight:600; color:var(--text); line-height:1.4; }
  .signal-card .sig-tags { display:flex; gap:4px; flex-wrap:wrap; margin-bottom:4px; margin-top:6px; }
  .signal-card .sig-dim { font-size:11px; background:#f0f9eb; color:#67c23a; border-radius:4px; padding:1px 6px; }
  .signal-card .sig-stars { font-size:12px; color:#e6a23c; }
  .signal-card .sig-key { font-size:11px; color:var(--text-secondary); line-height:1.5; margin-top:4px; }
</style>
</head>
<body>
<div class="container">

  <!-- Header -->
  <div class="header">
    <h1>智能终端硬件情报日报 · %(TODAY)s</h1>
    <div class="subtitle">采集口径：8类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑/AI耳机·耳穿戴） | 搜索窗口60天 | 国内15条 + 国际15条</div>
    <div class="meta">
      <span class="meta-badge">总情报 30条</span>
      <span class="meta-badge">国内 15条</span>
      <span class="meta-badge">国际 15条</span>
      <span class="meta-badge">信源 A-E级</span>
      <span class="meta-badge">搜索窗口 60天</span>
    </div>
  </div>

  <!-- Stats Bar -->
  <div class="stats-bar">
    <div class="stat-item"><div class="stat-num">30</div><div class="stat-label">总情报数</div></div>
    <div class="stat-item"><div class="stat-num">%(A)d</div><div class="stat-label">A级信源</div></div>
    <div class="stat-item"><div class="stat-num">%(B)d</div><div class="stat-label">B级信源</div></div>
    <div class="stat-item"><div class="stat-num">8</div><div class="stat-label">覆盖产品类别</div></div>
    <div class="stat-item"><div class="stat-num">%(FS)d</div><div class="stat-label">五星条数</div></div>
  </div>

  <!-- Dimension Coverage Panel -->
  <div class="dim-panel">
    <div class="dim-header">
      <div class="dim-title">技术维度覆盖面板</div>
      <div class="dim-counter"><span class="dim-num">%(COV)d</span><span class="dim-total"> / 16 维度</span></div>
    </div>
    <div class="dim-bar"><div class="dim-bar-fill" style="width:%(PCT).2f%%"></div></div>
    <div class="dim-grid">
      %(DIMCHIPS)s
    </div>
  </div>

  <!-- Top 5 Key Signals -->
  <div class="top-signals-panel">
    <div class="top-signals-header">
      <div class="top-signals-title">今日重点信号 Top 5</div>
      <div style="font-size:12px;color:var(--text-tertiary);">排序：星级降序→信源等级→状态优先→时间倒序</div>
    </div>
    <div class="top-signals-grid">
      %(TOPCARDS)s
    </div>
  </div>

  <!-- Summary Table -->
  <div class="summary-section">
    <div class="section-title">今日概要表</div>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>领域</th><th>上市状态</th><th>信源</th><th>时间</th><th>重要度</th></tr></thead>
      <tbody>
%(SUMMARY)s
      </tbody>
    </table>
  </div>

  <!-- Domestic Intelligence -->
  <div class="intel-section">
    <div class="section-title">一、国内情报（15条）</div>
      <div class="intel-cards">
%(CN)s
      </div>
  </div>

  <!-- International Intelligence -->
  <div class="intel-section">
    <div class="section-title">二、国际情报（15条）</div>
      <div class="intel-cards">
%(INTL)s
      </div>
  </div>

</div>
<script>
function toggleCard(id) {
  var el = document.getElementById(id);
  if (el.classList.contains('expanded')) { el.classList.remove('expanded'); }
  else { el.classList.add('expanded'); }
}
</script>
</body>
</html>''' % {
    "TODAY": TODAY, "A": stat_a, "B": stat_b, "FS": five_star, "COV": covered,
    "PCT": covered/16.0*100, "DIMCHIPS": dim_chips, "TOPCARDS": top_cards,
    "SUMMARY": summary_rows, "CN": cn_cards, "INTL": intl_cards
}

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print("written:", OUT)
print("covered dims:", covered, "/16")
print("A/B/C/D/E:", grade_count)
print("five_star:", five_star)
print("cn:", len(cn), "intl:", len(intl))
print("top5:", [d["title"][:20] for d in top5])
