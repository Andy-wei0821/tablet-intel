# -*- coding: utf-8 -*-
"""生成 WB_2026-11-06_硬件看板.html —— 智能终端硬件情报日报
30 条（国内15 + 国际15），全部 URL 已 WebFetch 验证。
"""
import re

TODAY = "2026-11-06"
TODAY_INT = 20261106
BASE = r"E:/AI相关/预研究/202608/03_输出/"
OUT = BASE + "WB_2026-11-06_硬件看板.html"

DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

def skey(d):
    d = (d or "").strip()
    try:
        if len(d) == 10:
            return int(d.replace("-",""))
        if len(d) == 7:
            y,m = d.split("-"); return int(y)*10000 + int(m)*100 + 15
        if len(d) == 4:
            return int(d)*10000 + 901
    except Exception:
        pass
    return 0

STATUS_RANK = {"即将上市":0, "进行中":1, "已上市":2}

def norm_status(raw, date_str):
    s = (raw or "").strip()
    if any(k in s for k in ["即将","未上市","预售","曝光","官宣","定档","预热","预约","待发","预告","前瞻"]):
        base = "即将上市"
    elif "进行中" in s:
        base = "进行中"
    elif any(k in s for k in ["已上市","开售","发售","上架","现售","在售","上市","发布"]):
        base = "已上市"
    else:
        base = "即将上市"
    if base == "已上市" and skey(date_str) > TODAY_INT:
        base = "即将上市"
    return base

def cap_stars(g, s):
    s = int(s)
    return s if g == "A" else min(s, 4)

def clean(s):
    if isinstance(s, str):
        s = s.replace("{", "").replace("}", "")
        s = re.sub(r'^[①-⑩]\s*', '', s.strip())
        return s
    if isinstance(s, list):
        return [clean(x) for x in s]
    return s

DATA = [
# ================= 国内 =================
{
 "region":"cn","category":"平板",
 "title":"iPad mini 8 国行11月6日开售：8.5英寸OLED加2nm A20 Pro，5499元起仍锁60Hz",
 "status":"已上市","date":"2026-11-06","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|结构/工艺",
 "grade":"A","stars":5,"signal_type":"开售","corroboration":2,
 "key_params":"8.5英寸OLED，峰值亮度1200尼特、对比度2000000:1；A20 Pro（2nm工艺），12GB内存；机身5.4mm、约255g；IP67防尘防水；128GB版5499元起（国补后约4999元）；Wi-Fi 7；取消底部扬声器开孔改用屏幕发声；刷新率维持60Hz无ProMotion",
 "tech_features":["OLED首次下放到mini尺寸iPad，改用屏下发声提升机身密闭性并首次支持IP67","A20 Pro每个GPU核心内置神经网络加速器，蜂窝版首用自研C2基带","配Apple N1无线芯片，支持蓝牙6与Thread家庭网络"],
 "why_important":"安卓小尺寸平板已普遍上高刷的背景下，苹果把顶级2nm算力与60Hz屏放在同一台机器上，规格错配成为行业讨论焦点；同时OLED、自研基带、自研无线芯片三件套在小尺寸形态首发，等于给小尺寸终端立了新的硬件组合范式。",
 "relevance":"8.5英寸OLED加旗舰SoC是安卓小平板最直接的规格锚点；60Hz争议反证高刷已是国产平板的差异化标配，产品定义时应避免算力与屏幕错配；屏下发声与IP67的堆叠方案值得借鉴。",
 "vendor":"苹果 iPad mini 8（A20 Pro）",
 "url":"https://www.apple.com.cn/ipad-mini/",
 "source_name":"Apple 中国官网",
 "source_detail":"Apple 中国官网 iPad mini 产品页（规格与5499元起定价）；快科技 2026-11-05 报道11月6日首销与60Hz争议互相印证",
 "note":"11-01期已覆盖该产品的全球发布，本条为国行开售与定价落地；屏下发声、C2基带、12GB内存为国行页面新增口径"
},
{
 "region":"cn","category":"平板",
 "title":"荣耀WIN平板开售：8.4英寸240Hz OLED加10000mAh，国补后3699元起",
 "status":"已上市","date":"2026-11-01","main_dim":"散热","dims":"散热|显示/OLED|SoC/芯片",
 "grade":"B","stars":3,"signal_type":"开售","corroboration":2,
 "key_params":"8.4英寸OLED，240Hz刷新率、峰值亮度6000尼特、10.7亿色；第五代骁龙8至尊版（3nm，超大核4.6GHz，Adreno 840 18MB独立显存）；东风涡轮风扇15000rpm加双VC同步风冷；10000mAh、66W快充、27W反向充电；480Hz多指触控、5000Hz瞬时触控；12GB+256GB 4499元、16GB+512GB 5199元，国补后3699元起",
 "tech_features":["风扇与机身一体化设计，PC级双出风口加导热铜翅片、双层VC均热板","240Hz OLED为当前小尺寸平板最高刷新率档位","支持PC游戏模拟器，幻影引擎已适配40多款高帧游戏"],
 "why_important":"把小尺寸平板做成带主动风冷的游戏机，是平板品类从影音办公向高性能游戏细分的一次明确分叉；万级电池加240Hz屏的组合，也把小平板的电源与散热预算推到接近游戏本的水平。",
 "relevance":"8.4英寸机身内塞风扇加双VC的堆叠方式是小平板散热设计的极限样本；240Hz OLED与480Hz触控的配套关系，可作为游戏平板触控链路的设计基线。",
 "vendor":"荣耀/WIN 平板",
 "url":"https://www.163.com/dy/article/LALUL56U0511BE1V.html",
 "source_name":"网易（转三易生活）",
 "source_detail":"三易生活 2026-11-01 报道正式开售与国补价；荣耀俱乐部 2026-11-02 抢先购公告与官方产品页印证配置",
 "note":"10-31期已覆盖该产品发布，本条为开售与国补价格落地，属进展非重复；风扇转速与噪音的实际表现待真机实测"
},
{
 "region":"cn","category":"平板",
 "title":"TCL 联合巴诺书店推 NOOK 联名版 Tab A1 NXTPAPER：11英寸类纸屏，11月19日发售",
 "status":"即将上市","date":"2026-11-06","main_dim":"显示/OLED","dims":"显示/OLED|结构/工艺|电池/快充",
 "grade":"B","stars":3,"signal_type":"发布","corroboration":2,
 "key_params":"11英寸2.1K NXTPAPER防眩光类纸屏（标准/彩纸/墨纸三模式）；联发科Helio G100；6GB+128GB，microSD可扩至2TB；8000mAh；四扬声器；IP54；249.99美元；随附T-Pen 2手写笔与保护套；即日起预购，11月19日经650家巴诺门店及线上发售",
 "tech_features":["NXTPAPER类纸屏三模式一键切换，Max Ink模式可省电并屏蔽通知","预装NOOK应用，打通有声书、漫画、杂志内容生态","硬件与连锁书店渠道绑定，用线下网络触达阅读人群"],
 "why_important":"硬件厂商与内容渠道联名，是中低端平板跳出参数同质化的一条现实路径；类纸屏加内容预装的组合直接对标墨水屏阅读器，等于用LCD成本抢电子书市场。",
 "relevance":"类纸显示路线与墨水屏形成替代竞争，对护眼终端选型有参考；渠道联名与内容绑定的模式可复制到教育、阅读等垂直场景终端。",
 "vendor":"TCL/Tab A1 NXTPAPER 巴诺联名版",
 "url":"https://news.qq.com/rain/a/20261106A03FW800",
 "source_name":"腾讯新闻（转IT时代网）",
 "source_detail":"腾讯新闻 2026-11-06 报道联名版预购与规格；Good e-Reader、Android Authority 2026-11-05 报道交叉印证",
 "note":"与11-03期覆盖的TCL Note A1为不同型号（Note A1为记事本形态）；原版Tab A1今年9月已在美上市，本条为NOOK联名新SKU"
},
{
 "region":"cn","category":"平板",
 "title":"宏碁暗影骑士G710插卡小平板降价上市：8.8英寸165Hz加天玑8300，国补后2549元",
 "status":"已上市","date":"2026-11-06","main_dim":"无线通信","dims":"无线通信|显示/OLED|电池/快充",
 "grade":"D","stars":2,"signal_type":"开售","corroboration":1,
 "key_params":"8.8英寸LCD，1880×3008分辨率，最高165Hz；天玑8300；6200mAh加30W充电；实体SIM卡槽支持5G通话；约355g、厚7.5mm；8GB+256GB起，预约价4099元直降至国补后2549元；双USB-C接口与线性马达",
 "tech_features":["实体SIM卡槽支持5G网络与通话，小平板兼作大屏手机","8.8英寸便携尺寸配165Hz高刷，双USB-C支持边充边接外设","线性马达与双扬声器补齐影音游戏体验"],
 "why_important":"5G插卡小平板仍是稀缺品类，从预约价4099元直落至国补后2549元，反映8英寸级平板细分市场竞争加剧、定价体系正在重构。",
 "relevance":"插卡通话能力从手机向小平板下探，为8英寸游戏平板与通信融合产品的定价与射频选型提供价格锚点。",
 "vendor":"宏碁/暗影骑士 G710",
 "url":"https://www.163.com/dy/article/LB0SL9GR0511RFLI.html",
 "source_name":"网易号 刘奔跑（自媒体）",
 "source_detail":"网易号自媒体 2026-11-06 报道上市降价与配置，参数未与官方页核对",
 "note":"D级自媒体单一信源，价格与国补口径待官方渠道印证；文中对比的酷比魔方掌玩mini4 Ultra为4月已上市产品，不与本条混淆"
},
{
 "region":"cn","category":"手机",
 "title":"荣耀Magic9 Pro Max首次走出内地：阿莱联名双2亿影像，香港10999港元起",
 "status":"已上市","date":"2026-11-05","main_dim":"摄像头","dims":"摄像头|SoC/芯片|电池/快充",
 "grade":"B","stars":4,"signal_type":"发布","corroboration":2,
 "key_params":"2亿像素主摄1/1.28英寸f/1.57加OIS；2亿像素潜望长焦1/1.4英寸f/2.6支持3.5倍光学；自研影像芯片驭光H1；第六代骁龙8至尊版；8000mAh配100W有线加80W无线；香港12GB+512GB售10999港元",
 "tech_features":["与ARRI阿莱联合调校的电影级双2亿影像系统","自研驭光H1强化动态范围与实时HDR处理","8000mAh大电池加100W有线、80W无线双快充"],
 "why_important":"荣耀旗舰首次在内地以外市场开卖并创当地旗舰订单纪录，国产旗舰高端化出海明显提速；电影厂牌联名影像正在成为万元档机型的新差异化范式。",
 "relevance":"阿莱联名影像链路与大电池双快充组合，为国产影像旗舰的产品定义与万元档定价提供参照；也提示影像差异化正从硬件规格转向调校体系与品牌授权。",
 "vendor":"荣耀/Magic9 Pro Max",
 "url":"https://www.163.com/dy/article/LAV3URL10511CPVM.html",
 "source_name":"网易（转快科技）",
 "source_detail":"快科技 2026-11-05 报道香港发布与完整规格；荣耀全球CMO关海涛微博战报印证订单纪录",
 "note":"该系列9月28日已在内地发布（未进入本系列看板），本条为香港市场首发事件；国行与港版在频段与卫星通信上或有差异，待官方口径"
},
{
 "region":"cn","category":"手机",
 "title":"摩托罗拉Signature 27发布：全球首款双层OLED手机，峰值亮度12000尼特、1899欧元起",
 "status":"即将上市","date":"2026-11-06","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|散热",
 "grade":"B","stars":4,"signal_type":"发布","corroboration":2,
 "key_params":"6.78英寸1.5K Extreme AMOLED Duo双层OLED，峰值亮度12000尼特；第六代骁龙8至尊版（2nm）；索尼Lytia 910 5000万主摄加2亿像素潜望长焦（100倍AI超级变焦）；B&O调音；7000mAh配90W有线加50W无线；227g、厚7.99mm；1899欧元起，11月16日欧洲与中东开售；承诺7代安卓大版本更新",
 "tech_features":["双层OLED两发光层分担电场，亮度翻倍同时延长寿命","ArcticMesh散热系统，均热板面积较上代增40%","出厂预装安卓17，为首款官方支持GrapheneOS的非Pixel机型"],
 "why_important":"双层OLED在旗舰手机规模落地，验证该技术在亮度、寿命、能效三角上的工程平衡，为国产旗舰的屏幕路线提供了单层之外的新选项；7年更新承诺也在拉长旗舰的生命周期口径。",
 "relevance":"双层OLED与单层方案的取舍直接影响旗舰屏幕选型与BOM；7000mAh塞进7.99mm机身的堆叠方案，是影像旗舰做轻薄大电池的参考样本。",
 "vendor":"摩托罗拉/Signature 27",
 "url":"https://mobile.zol.com.cn/1269/12694813.html",
 "source_name":"中关村在线",
 "source_detail":"中关村在线 2026-11-06 报道发布与完整规格；快科技、网易科技同日报道印证；GrapheneOS 官方9月确认支持该机型",
 "note":"11-02期仅覆盖定档信息，本条为正式发布；首发为欧洲与中东，国行发售计划官方未公布，是否预装GrapheneOS亦未确认"
},
{
 "region":"cn","category":"智能手表",
 "title":"华为WATCH Air曝光：商标信息指向超薄新品类，预计11月内发布",
 "status":"即将上市","date":"2026-11-05","main_dim":"结构/工艺","dims":"结构/工艺|传感器",
 "grade":"B","stars":2,"signal_type":"曝光","corroboration":1,
 "key_params":"依据华为近期商标注册信息推断，定位超薄智能手表，预计11月内发布；屏幕、传感器与电池规格官方均未公布；可参照在售WATCH FIT 4 Pro的9.3mm厚度与30.4g重量作为对照基线",
 "tech_features":["Air命名延续华为轻薄产品线逻辑，或与FIT系列形成定位梯队","商标先行注册符合华为新品发布惯例","超薄定位对表壳材料与传感器堆叠提出更高要求"],
 "why_important":"华为在Ultimate、GT、WATCH数字与FIT四条线之外再开Air轻薄线，说明头部厂商仍在按形态与人群细分穿戴矩阵，超薄正在成为独立卖点而非附属属性。",
 "relevance":"若落地，超薄定位将牵动表壳材料（钛/铝合金）、电池能量密度与传感器堆叠方案的选择，可作为穿戴产品线补位与竞品定位的观察样本。",
 "vendor":"华为/WATCH Air（未发布）",
 "url":"https://www.163.com/dy/article/LAVNRUCD051191D6.html",
 "source_name":"网易（转CNMO科技）",
 "source_detail":"CNMO科技 2026-11-05 报道数码博主依据商标注册信息的推测，单一信源",
 "note":"属商标推断类爆料，非官方确认，规格与发布时间均待印证；与已覆盖的WATCH 6系列、WATCH D3、手表Fit 6均非同一产品"
},

{
 "region":"cn","category":"智能手表",
 "title":"辰显光电展出全球首款1.85英寸TFT基Micro-LED透明手表：息屏可见机械机芯",
 "status":"进行中","date":"2026-11-04","main_dim":"显示/OLED","dims":"显示/OLED|结构/工艺",
 "grade":"D","stars":2,"signal_type":"展出/技术首秀","corroboration":1,
 "key_params":"1.85英寸TFT基Micro-LED透明显示屏；息屏状态高透过率，可直接看到表内机械机芯；在机械表基础上叠加轻智能能力；2026世界显示产业创新发展大会（11月4日成都）现场展出；量产时间与价格未公布",
 "tech_features":["TFT基Micro-LED做透明显示，兼顾机械表质感与轻智能功能","息屏高透过率解决了透明屏在腕上的观感矛盾","与京东方、天马等面板厂同场展出，属面板端技术展示"],
 "why_important":"透明Micro-LED从展台走向腕上形态，意味着智能手表的外观光学路线可能出现第三种选择（除圆形AMOLED与电子纸之外）；面板厂主导而非整机厂主导，说明上游正在为穿戴品类寻找新卖点。",
 "relevance":"若量产成本可控，透明Micro-LED会改变手表表壳结构、透光路径与电池布置方式；对高端机械表联名款与轻智能产品定义均有参考价值。",
 "vendor":"辰显光电/1.85英寸透明Micro-LED手表",
 "url":"https://www.sohu.com/a/1097165839_355475",
 "source_name":"搜狐网（2026世界显示产业创新发展大会报道）",
 "source_detail":"搜狐 2026-11-04 大会现场报道，引述辰显光电总经理黄秀颀介绍；属展会展示口径",
 "note":"普通媒体单一信源，且为展会展品而非量产商品，参数仅有尺寸与透过率定性描述；量产时间、良率与成本均未公布，按技术信号收录"
},
{
 "region":"cn","category":"AR-VR眼镜",
 "title":"影目发布INMO Future：双目1080P全彩波导加主动散热，一体式空间计算5499元起",
 "status":"已上市","date":"2026-11-04","main_dim":"显示/OLED","dims":"显示/OLED|散热|AI/NPU",
 "grade":"C","stars":4,"signal_type":"发布","corroboration":3,
 "key_params":"双目1080P全彩阵列光波导，视场角36度，入眼亮度最高800尼特（较上代提升33%）；主动散热使重负载温度稳定低于42摄氏度；SLAM加6DoF，厘米级（10cm以内）定位，3秒内完成多平面检测；基于安卓14的空间AIOS；标准价6999元、发布价5999元、现场到手价5499元",
 "tech_features":["一体式独立计算，不依赖手机或主机，本身即完整空间计算设备","空间地图可持久化，重戴后厘米级重定位，内容锚定留在原处","支持无线串流PC与主机画面、多窗口移动办公与三维协同评审"],
 "why_important":"一体式全彩AI眼镜的显示分辨率从行业普遍的约500×380跃升到双目1080P，同时把主动散热压进眼镜形态，标志一体式空间计算眼镜完成工程化落地；厂商同步设立3000万元内容基金，品类生态开始配套。",
 "relevance":"阵列光波导加主动散热的堆叠方案为AI眼镜硬件设计提供新范式；空间锚定与持久化地图意味着眼镜从显示配件走向独立计算终端，直接影响下一代终端形态判断。",
 "vendor":"影目科技/INMO Future",
 "url":"https://www.cqn.com.cn/cj/content/2026-11/04/content_9179545.htm",
 "source_name":"中国质量新闻网",
 "source_detail":"中国质量新闻网 2026-11-04 发布会报道；艾邦AR/VR网、中国商报网、上海静安同日报道，参数一致",
 "note":"芯片仅表述为高通骁龙高性能空间处理芯片，具体型号官方未点名；价格为三档口径（6999/5999/5499），以发布价5999元为准"
},
{
 "region":"cn","category":"AR-VR眼镜",
 "title":"三星Android XR眼镜定档11月12日预购：骁龙AR1 Gen1无屏方案，Gentle Monster联名镜框",
 "status":"即将上市","date":"2026-11-05","main_dim":"SoC/芯片","dims":"SoC/芯片|AI/NPU|结构/工艺",
 "grade":"B","stars":4,"signal_type":"发布","corroboration":3,
 "key_params":"11月12日开启预购，12月起发货；骁龙AR1 Gen1平台；无内嵌显示屏的音频优先方案；单次续航9小时，充电盒可再满充7次；11款镜框、覆盖两个FCC ID；内置摄像头并配录制指示灯；首发美国与韩国",
 "tech_features":["Gemini智能体驱动导航、实时翻译与视觉问答","录制指示灯加遮挡即停拍的隐私机制","同时兼容安卓与iPhone双生态，扩大潜在用户盘"],
 "why_important":"首款Android XR消费级眼镜进入销售环节，大厂定价与时尚品牌联名将共同定义AI眼镜的主流价位带与日常佩戴审美；无屏音频优先路线也明确了与AR显示路线的分野。",
 "relevance":"对国产AI眼镜出海定价与无屏音频方案的产品定义有直接参照；Gemini智能体的交互设计为国内大模型眼镜的功能规划提供对标样本。",
 "vendor":"三星/Intelligent Eyewear（Android XR）",
 "url":"https://www.androidauthority.com/samsung-smart-glasses-pre-orders-3732159/",
 "source_name":"Android Authority",
 "source_detail":"Android Authority 2026-11-05 确认预购日期；Warby Parker 财报电话会（SEC文件）、Android Central 交叉印证",
 "note":"11-01期仅覆盖定档12月中旬，本条为预购日期与镜框细节落地；价格未公布，中国大陆不在首波名单"
},
{
 "region":"cn","category":"笔记本电脑",
 "title":"机械革命旷世16开售：酷睿5 205H加RTX 3050，140W散热下探国补5099元",
 "status":"已上市","date":"2026-11-05","main_dim":"散热","dims":"散热|SoC/芯片|显示/OLED",
 "grade":"B","stars":3,"signal_type":"开售","corroboration":1,
 "key_params":"16英寸LCD雾面屏1920×1200、165Hz、400尼特、全sRGB；酷睿5 205H加RTX 3050 4GB（显卡95W满血）；五热管双风扇四出风口，整机140W散热；60Wh电池、约2.2kg；预留内存插槽与M.2位；首发5999元，国补后5099.15元",
 "tech_features":["140W整机散热在5千元档支撑满血显卡释放","预留内存与硬盘位，可自主升级","Wi-Fi 6E加蓝牙5.4、RGB背光键盘"],
 "why_important":"入门游戏本把140W散热规格下放到国补5千元档，说明国补周期内游戏本价格带整体下移、入门机型散热普遍加码，中端本的散热预算被进一步压缩。",
 "relevance":"可作为5千元价位游戏本的散热规格基线与165Hz雾面屏配置基准；对中端轻薄本如何在有限厚度内做散热取舍有反向参考。",
 "vendor":"机械革命/旷世16",
 "url":"https://www.163.com/dy/article/LAV3C73H0511B8LM.html",
 "source_name":"网易（转IT之家）",
 "source_detail":"IT之家 2026-11-05 报道开售与完整规格，单一信源",
 "note":"价格含国补，短期随大促波动；与11-01期联想来酷Pro 16为同价位竞品但不是同一产品"
},
{
 "region":"cn","category":"笔记本电脑",
 "title":"触控版MacBook Pro国行11月6日发售：双层串联OLED加M5 Max，16英寸减重320g",
 "status":"已上市","date":"2026-11-05","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|结构/工艺",
 "grade":"B","stars":4,"signal_type":"开售","corroboration":2,
 "key_params":"16.3英寸PROLED XDR双层串联OLED，HDR与SDR峰值亮度均2000尼特、10-120Hz自适应；M5 Max 18核CPU加32核GPU，最高128GB统一内存；16英寸约1.82kg，较前代减重320g；续航最长24小时；10月30日预购、11月6日国行发售",
 "tech_features":["Mac产品线首次引入触控屏，铰链重新设计以保证点按稳定","双层串联OLED在笔电端首次商用，亮度与寿命同步提升","灵动岛与发光logo时隔十年回归，六扬声器低音下潜增强约五成"],
 "why_important":"触控进Mac终结了长达十年的产品路线争论；双层串联OLED在笔电商用会拉动高端创作本的显示升级周期，与国产RTX Spark AI本形成屏幕与算力两端的对标。",
 "relevance":"双层串联OLED的亮度、寿命与功耗表现，是国产高端创作本屏幕选型的直接参照；触控化趋势将影响Windows笔电的铰链工艺与交互定义。",
 "vendor":"苹果/MacBook Pro（触控版，M5 Pro/Max）",
 "url":"https://www.163.com/dy/article/LB0NB89C0511B8LM.html",
 "source_name":"网易（转IT之家）",
 "source_detail":"IT之家 2026-11-05 实拍上手报道；快科技等媒体发布信息相互印证",
 "note":"11-01期已覆盖该产品发布，本条为上手实测与国行发售落地，新增M5 Max核心数、减重320g等口径"
},
{
 "region":"cn","category":"无线充",
 "title":"绿联MagFlow Qi2.2 Slim海外上市：10000mAh磁吸25W无线加45W有线，79.99美元",
 "status":"已上市","date":"2026-11-05","main_dim":"电池/快充","dims":"电池/快充|认证/合规|BMS/电源",
 "grade":"B","stars":3,"signal_type":"发布","corroboration":2,
 "key_params":"10000mAh；厚13.9mm、重215g；Qi2.2无线最高25W，30分钟可将iPhone 18 Pro充至42%；内置USB-C编织线支持45W有线（PD 3.0/PPS/QC 4.0）；自充最高30W约2小时满；1个USB-C口最多同充3台设备；79.99美元，暗樱桃配色",
 "tech_features":["内置线缆兼作提绳，省掉随身线材","低电流模式可为手环、手表等小配件安全充电","以配色跟进iPhone 18 Pro机身色，走外观配套策略"],
 "why_important":"国产配件厂在Qi2.2 25W档位以79.99美元定价，同时压住苹果MagSafe外接电池与安克MagGo的价格带，说明无线充电配件正从参数竞争转向外观与生态配套竞争。",
 "relevance":"Qi2.2的25W无线加45W有线的功率分配，是磁吸移动电源电源管理（BMS）设计的现实样本；内置线缆与低电流模式是配件差异化的低成本切入点。",
 "vendor":"绿联（UGREEN）/MagFlow Qi2.2 Slim 10000mAh",
 "url":"https://www.163.com/dy/article/LB055SER0511B8LM.html",
 "source_name":"网易（转IT之家）",
 "source_detail":"IT之家 2026-11-05 报道海外上市与定价；HitechReports 同日报道印证美国亚马逊已开售",
 "note":"为9月已发布MagFlow Qi2.2的暗樱桃配色新增SKU，硬件规格未变；与10-31期AUKEY、11-04期安克MagGo 2 Pro非同一产品"
},
{
 "region":"cn","category":"智能音箱",
 "title":"Nothing CMF牛奶盒音箱国行开售：Speaker S 449元、M 849元，前盖可拆换可3D打印",
 "status":"已上市","date":"2026-11-05","main_dim":"音频","dims":"音频|结构/工艺|无线通信",
 "grade":"B","stars":3,"signal_type":"开售","corroboration":1,
 "key_params":"Speaker S：45mm全频单元10W RMS加双被动辐射器；Speaker M：70mm低音加16mm高音，35W RMS密闭箱体；均IP68防尘防水；蓝牙6.0加NFC碰触配对；50音量开Ultra Bass续航18小时；USB-C兼充电与无损音频传输；449元与849元",
 "tech_features":["前面板与旋钮可拆换，官方提供3D设计文件供自行打印配件","USB-C口同时承担充电与无损音频输入","NFC轻触配对与双设备同时连接"],
 "why_important":"可拆可换的模块化外观把消费电子DIY文化带进音频品类；蓝牙6.0与IP68在449元价位形成规格下探，给国产蓝牙音箱的差异化提供了外部参照。",
 "relevance":"模块化外壳与配件生态思路可被国产音箱直接借鉴；蓝牙6.0加NFC的交互组合，可作为IoT音频终端的连接基线。",
 "vendor":"Nothing/CMF Speaker S、Speaker M（国行）",
 "url":"https://www.163.com/dy/article/LB0998L00511B8LM.html",
 "source_name":"网易（转IT之家）",
 "source_detail":"IT之家 2026-11-05 报道国行开售、定价与声学规格，单一信源",
 "note":"11-02期已覆盖该产品海外首发，本条为国行开售与完整声学参数，属进展非重复"
},
{
 "region":"cn","category":"AI耳机·耳穿戴",
 "title":"摩托罗拉Moto Buds 2 Ultra发布：Bose降噪加楼氏动铁双单元，Qi2充电盒承载AI翻译",
 "status":"已上市","date":"2026-11-05","main_dim":"音频","dims":"音频|无线通信|电池/快充",
 "grade":"B","stars":3,"signal_type":"发布","corroboration":1,
 "key_params":"11mm动圈加Knowles楼氏动铁双单元；Bose QuietControl主动降噪与SoundDesign调音；蓝牙6.0，支持SBC/AAC/LHDC 4/LHDC 5；单次续航8小时、含盒37小时；充电盒支持Qi2无线充；每耳三麦克风加语音拾取单元；199欧元",
 "tech_features":["Bose声学IP授权上车，降噪与调音由Bose提供","Qi2充电盒同时承担AI实时翻译功能承载","三麦加骨导式语音拾取的呼叫降噪链路"],
 "why_important":"借第三方声学IP授权加智能化充电盒切入中高端降噪耳机，说明TWS的差异化路径正在从自研声学转向品牌授权与配件功能扩展。",
 "relevance":"Qi2充电盒承载AI翻译的方案，为国产TWS的外设智能化提供参考；蓝牙6.0加LHDC 5的组合正在成为旗舰耳机新的连接基线。",
 "vendor":"摩托罗拉/Moto Buds 2 Ultra",
 "url":"https://www.163.com/dy/article/LB0NVNDJ0511B8LM.html",
 "source_name":"网易（转IT之家）",
 "source_detail":"IT之家 2026-11-05 报道与Moto Watch 2 Fit 同场发布，规格来自官方发布信息",
 "note":"全球发布产品，国行发售计划官方未公布；AI实时翻译的语种数量与是否订阅收费未公布，待印证"
},
# ================= 国际 =================
{
 "region":"intl","category":"平板",
 "title":"联想Idea Tab Pro Gen 2马来西亚上市：13英寸3.5K加10200mAh，首搭Lenovo Qira",
 "status":"已上市","date":"2026-11-03","main_dim":"AI/NPU","dims":"AI/NPU|显示/OLED|电池/快充",
 "grade":"B","stars":4,"signal_type":"开售","corroboration":2,
 "key_params":"13英寸3.5K PureSight Pro（Dolby Vision，可选防眩光雾面版）；骁龙8s Gen 4；6.20mm厚、不足600g；10200mAh加45W快充；四JBL扬声器加Dolby Atmos；8GB+256GB起，RM2899起；11月3日起在马来西亚联想专卖店开售",
 "tech_features":["首款搭载Lenovo Qira的平板，Qira功能2026年稍后上线","Smart Key一键唤起Lenovo Smart AI Input，用自然语言生成文本与翻译","Smarter Reader加AI Notes构成完整学习闭环，课堂实时转录"],
 "why_important":"把AI学习工作流做成硬件级快捷键加系统级智能体，是平板从娱乐设备转向教育生产力工具的具体落地方式；13英寸3.5K加10200mAh的配置在RM2899价位，把大屏高分辨率与长续航同时下放。",
 "relevance":"6.2mm机身塞进10200mAh的堆叠方案，对轻薄平板的电池布局有直接参考；Qira这类系统级智能体的入口设计，是平板AI功能定义的重要观察点。",
 "vendor":"联想/Idea Tab Pro Gen 2",
 "url":"https://tech.rockstarmedia.com.my/news/lenovo-yoga-tab-gen-2",
 "source_name":"Tech Rockstar Media（马来西亚）",
 "source_detail":"Tech Rockstar Media 2026-11-03 报道五款平板马来上市与Idea Tab Pro Gen 2完整规格；GadgetMTech、东方日报同日报道印证",
 "note":"与11-03期覆盖的Yoga Tab Plus/Gen 2为同场发布的不同型号；本条聚焦Idea Tab Pro Gen 2的教育AI定位与Qira首搭"
},
{
 "region":"intl","category":"平板",
 "title":"联想Legion Tab第五代马来西亚开售：8.8英寸3K 165Hz加Coldfront Vapor，RM3399起",
 "status":"已上市","date":"2026-11-03","main_dim":"散热","dims":"散热|显示/OLED|SoC/芯片",
 "grade":"B","stars":4,"signal_type":"开售","corroboration":2,
 "key_params":"8.8英寸3K屏、165Hz、典型亮度600尼特；骁龙8 Elite Gen 5；最高16GB LPDDR5X 10667Mbps加512GB；9000mAh加68W充电；Legion Coldfront Vapor散热效率较上代提升32%；360g；双USB-C支持边充边接外设；RM3399起",
 "tech_features":["Coldfront Vapor均热方案效率提升32%，为8.8英寸机身做高负载准备","双USB-C口可同时充电与接外设，游戏场景实用","Lenovo AI Engine+按场景增强游戏音效、抑制语音通话噪声并调整触控灵敏度"],
 "why_important":"8.8英寸3K 165Hz加旗舰SoC的组合，把小尺寸平板彻底做成游戏终端；360g配9000mAh的能重比，是当前小尺寸高性能平板的工程上限样本。",
 "relevance":"8.8英寸机身内做均热板加双USB-C的布局，对国产小尺寸游戏平板的散热与接口设计有直接参考；10667Mbps LPDDR5X的带宽配置也提示内存规格正在成为游戏平板卖点。",
 "vendor":"联想/Legion Tab（8.8英寸，第五代）",
 "url":"https://gadgetmtech.com/lenovo-launches-new-tablet-line-up-in-malaysia",
 "source_name":"GadgetMTech",
 "source_detail":"GadgetMTech 2026-11-03 报道马来西亚五款平板上市与Legion Tab Gen 5完整规格；Tech Rockstar Media、东方日报同日报道印证",
 "note":"与同场发布的Idea Tab Pro Gen 2为不同型号，本条聚焦游戏定位；RM3399为8.8英寸版的起售价"
},
{
 "region":"intl","category":"平板",
 "title":"TCL TAB A1 Plus NXTPAPER登陆澳洲：12.2英寸2.4K类纸屏加10000mAh，599澳元",
 "status":"已上市","date":"2026-11-04","main_dim":"显示/OLED","dims":"显示/OLED|手写笔/触控|电池/快充",
 "grade":"B","stars":3,"signal_type":"开售","corroboration":1,
 "key_params":"TAB A1 Plus：12.2英寸2.4K NXTPAPER，骁龙4 Gen 2，6GB+256GB，10000mAh，599澳元；TAB A1：11英寸2.1K，Helio G100，6GB+128GB，8000mAh，449澳元；均随附翻盖保护壳与T-Pen 2手写笔；经JB Hi-Fi等澳洲主流零售渠道铺货",
 "tech_features":["NXTPAPER Key实体键一键切换三种显示模式，Max Ink模式省电并静音通知","3A Crystal Shield玻璃三层涂层：防眩、防反射、防指纹","金属一体成型机身，手写笔标配降低使用门槛"],
 "why_important":"TCL在澳洲一次性铺开Note A1、TAB A1、TAB A1 Plus三款类纸屏设备，形成完整价格带覆盖，是类纸显示技术从单品走向规模化出货的标志性动作。",
 "relevance":"验证防眩光类纸屏在中端平板的量产成本与渠道接受度，为类纸方案的配置取舍与出海定价提供对照样本。",
 "vendor":"TCL/TAB A1 NXTPAPER、TAB A1 Plus NXTPAPER",
 "url":"https://eftm.com/2026/11/paper-like-browsing-tcl-debuts-nxtpaper-smartphone-and-tablet-lineup-across-australia-282975",
 "source_name":"EFTM（澳大利亚）",
 "source_detail":"EFTM 2026-11-04 报道TCL NXTPAPER手机与平板全系澳洲上市，单一信源",
 "note":"与11-06同期的巴诺联名版为不同市场SKU（澳洲标准版对美国NOOK联名版）；与11-03期TCL Note A1非同一型号"
},
{
 "region":"intl","category":"平板",
 "title":"华为MatePad Air港版11月5日开售：5.3mm机身加12英寸144Hz OLED柔光屏，6288港元",
 "status":"已上市","date":"2026-11-05","main_dim":"显示/OLED","dims":"显示/OLED|结构/工艺|手写笔/触控",
 "grade":"B","stars":3,"signal_type":"开售","corroboration":2,
 "key_params":"12英寸2.8K 144Hz OLED PaperMatte柔光屏，峰值亮度1200尼特；厚5.3mm、重约509g（柔光屏版520g）；10100mAh加66W快充，30分钟充至42%；星闪极速互联；3D立体散热架构加高导热六方石墨烯；8GB+256GB售6288港元，随机附送智能磁吸键盘，首卖赠M-Pencil Pro",
 "tech_features":["纳米级微蚀刻加抗反射纳米涂层，强光下抑制眩光","星闪技术提升手写笔与键盘连接稳定性并降低时延","港版预装PC级WPS Office与升级版HUAWEI Notes"],
 "why_important":"5.3mm机身与柔光OLED的组合，代表生产力平板向电子书级阅读体验融合的方向；港版直接预装PC级办公套件并捆绑键盘手写笔，说明华为在海外市场用整套生产力方案而非单机打差异化。",
 "relevance":"柔光屏加星闪外设互联是国产平板差异化的成熟样板，对手写笔连接方案选型与办公平板的产品定义有直接参考。",
 "vendor":"华为/MatePad Air（2026）港版",
 "url":"https://www.mobilemagazinehk.com/2026/11/2026-11-huawei-matepad-air-hk-launch.html",
 "source_name":"Mobile Magazine（香港）",
 "source_detail":"Mobile Magazine 2026-11-05 报道港版开售、定价与完整规格；ePrice香港 2026-10-28 发布会预告交叉印证",
 "note":"11-01期覆盖的是内地版实测，本条为港版开售与定价，属市场进展；港版捆绑策略与内地不同，不能直接套用"
},
{
 "region":"intl","category":"手机",
 "title":"华为nova 16s香港首销：7000mAh加100W快充，3888港元起主打轻薄人像",
 "status":"已上市","date":"2026-11-05","main_dim":"电池/快充","dims":"电池/快充|摄像头|SoC/芯片",
 "grade":"A","stars":4,"signal_type":"开售","corroboration":2,
 "key_params":"7000mAh电池配100W有线快充；1.5K OLED直屏；麒麟平台；nova 16s售3888港元、nova 16s Pro售5188港元；11月5日17时起香港首销",
 "tech_features":["7000mAh大电池塞进轻薄人像定位机身","100W快充为nova系列海外最高规格","AI构图与夜景人像算法强化年轻市场卖点"],
 "why_important":"nova是华为海外走量主力线，7000mAh加100W在轻薄中端机里规格激进，直接压向海外中端市场；香港首销定价透露华为海外中端价格带策略已回到有竞争力的区间。",
 "relevance":"高密度电池在中端机的普及节奏与100W快充下沉，是终端电源设计的关键信号；海外定价可作为中端竞品基准。",
 "vendor":"华为/nova 16s、nova 16s Pro",
 "url":"https://consumer.huawei.com/hk/offer/huawei-Terms-and-Conditions",
 "source_name":"华为香港官网（首销活动条款）",
 "source_detail":"华为香港官网 2026-11-05 首销条款页列明nova 16s HK$3888、Pro HK$5188与首销时间；ePrice香港 2026-10-28 发布会预告交叉印证",
 "note":"官网条款页为活动页而非产品规格页，规格部分来自发布会口径；与11-04期内地发布为同一产品不同市场，属进展"
},
{
 "region":"intl","category":"手机",
 "title":"iQOO 16海外发布在即：或首发骁龙8 Elite Extreme Gen 6，8500mAh瞄准印度",
 "status":"即将上市","date":"2026-11-02","main_dim":"SoC/芯片","dims":"SoC/芯片|电池/快充|显示/OLED",
 "grade":"B","stars":3,"signal_type":"曝光","corroboration":2,
 "key_params":"6.85英寸AMOLED；骁龙8 Elite Extreme Gen 6；12GB+256GB；8500mAh电池；5000万三摄加3200万前摄；11月内全球与印度发布",
 "tech_features":["首批搭载高通新一代旗舰平台的量产终端之一","8500mAh大电池配旗舰性能调校","已在印度移动大会现场提前亮相预热"],
 "why_important":"作为新一代骁龙旗舰平台的首批海外落地机型之一，其印度定价会牵动2026年底至2027年初性能机的价格带；8500mAh也把小尺寸旗舰的电池门槛继续抬高。",
 "relevance":"新平台海外首发节奏与8500mAh电池方案，是SoC与电源供应链的重要观察点；对国产旗舰的海外版本配置裁剪有参考。",
 "vendor":"iQOO/iQOO 16",
 "url":"https://www.deccanherald.com/technology/november-2026-iqoo-16-xiaomi-18-pro-motorola-signature-27-vivo-x500-and-more-phones-coming-this-month-4204199",
 "source_name":"Deccan Herald（印度）",
 "source_detail":"Deccan Herald 2026-11-02 十一月新机盘点报道iQOO 16海外发布计划；My Mobile India 同期报道交叉印证",
 "note":"属发布前曝光，海外版芯片型号与国行可能不同，规格待官方确认；与11-01期国行开售为同一产品的不同市场进展"
},
{
 "region":"intl","category":"智能手表",
 "title":"Garmin fenix 9 / 9 Pro发布：AMOLED亮度翻倍、存储升至64GB，Pro首用钛合金表壳",
 "status":"已上市","date":"2026-11-03","main_dim":"显示/OLED","dims":"显示/OLED|传感器|电池/快充",
 "grade":"B","stars":4,"signal_type":"发布","corroboration":2,
 "key_params":"AMOLED屏亮度较上代翻倍，9 Pro的51mm款为1.5英寸（fenix系列最大）；存储翻倍至64GB；43/47/51mm三尺寸，43mm续航10天、51mm最长29天（Pro 31天）；太阳能版最长57天；9 Pro首次采用钛合金表壳并加入绿光手电；新加坡S$1389起、9 Pro S$1489起",
 "tech_features":["新增Stamina Zones与Stamina Curves两套体力指标，五档强度区间可视化","地图引擎更新，平移速度提升约30%并加入透视视图","Garmin Epic 把多日运动记录编成可分享故事；inReach版支持卫星天气与位置共享"],
 "why_important":"fenix系列首次把AMOLED亮度翻倍与64GB存储同时给出，并让Pro版用上钛合金，说明专业户外表在向消费级屏幕体验靠拢；同时保留太阳能与inReach两条续航/通信分支，产品线分层更清晰。",
 "relevance":"亮度翻倍与钛合金表壳的组合，是高端运动表材质与显示升级的参考路径；Stamina类体力模型提示运动手表正从记录转向训练决策。",
 "vendor":"Garmin/fenix 9、fenix 9 Pro",
 "url":"https://www.hardwarezone.com.sg/mobile/wearables/garmin-fenix-9-fenix-9-pro-release-pricing-smartwatch",
 "source_name":"HardwareZone（新加坡）",
 "source_detail":"HardwareZone 2026-11-03 报道发布、规格与新加坡定价；澳洲金融评论 2026-11-03 fenix 9 Pro 评测交叉印证",
 "note":"与10-31期Garmin Enduro 4、Approach S72，11-01期MARQ Gen 3，11-03期Venu 4 均非同一型号；内存容量官方未披露"
},
{
 "region":"intl","category":"智能手表",
 "title":"华为WATCH GT 7系列台湾开卖：钛合金加3000尼特屏，Pro支持ECG与40米自由潜水",
 "status":"已上市","date":"2026-10-01","main_dim":"显示/OLED","dims":"显示/OLED|传感器|电池/快充",
 "grade":"B","stars":3,"signal_type":"开售","corroboration":2,
 "key_params":"GT 7 Pro：航天级钛合金表体加纳米微晶陶瓷表圈、1.47英寸蓝宝石镜面（峰值3000尼特）、ECG心电分析、40米自由潜水模式、轻度使用最长21天；GT 7 Pro售17990新台币、GT 7售12990新台币；首销赠FreeBuds Neo",
 "tech_features":["钛合金加微晶陶瓷材质下放到GT系列旗舰","ECG心电与情绪记录等进阶健康管理","110种以上运动模式，含高尔夫球场地图与坡度校正配速"],
 "why_important":"GT系列是华为穿戴的出货基石，GT 7 Pro把钛合金表体、ECG与专业潜水能力打包进主流价位，说明长续航运动手表的配置天花板仍在整体上移。",
 "relevance":"长续航户外手表的传感堆料与材质升级路径，对运动手表产品线的成本分层与传感器选型有直接参考。",
 "vendor":"华为/WATCH GT 7、WATCH GT 7 Pro",
 "url":"https://news.m.pchome.com.tw/expense/leho/20261001/index-79079598555813356013.html",
 "source_name":"PChome新闻（台湾）",
 "source_detail":"PChome新闻 2026-10-01 报道GT 7系列在台开卖与定价；NOVA资讯广场同期报道交叉印证",
 "note":"与11-04期WATCH 6系列非同一产品线；上市已超一个月，按60天窗口收录其台湾市场价格与配置策略"
},
{
 "region":"intl","category":"AR-VR眼镜",
 "title":"Nothing预告首款AI原生设备：12月发布无屏硬件，同步曝光音频与摄像头两款智能眼镜",
 "status":"即将上市","date":"2026-11-05","main_dim":"音频","dims":"音频|AI/NPU|结构/工艺",
 "grade":"B","stars":4,"signal_type":"曝光","corroboration":2,
 "key_params":"首款AI原生产品定于12月发布，无屏幕、非软件应用；据Roland Quandt爆料将推两款智能眼镜：音频版（音乐/通话/语音助手，光致变色镜片）与摄像头版（支持ChatGPT与翻译）；AI任务经手机与云端处理，不配AR显示",
 "tech_features":["明确不做AR显示，走无屏音频优先的轻算力路线","光致变色镜片可自动调节透光","摄像头版直连ChatGPT与实时翻译"],
 "why_important":"设计驱动型品牌入局无屏AI眼镜，意味着这条赛道的品牌阵营继续扩容；明确把算力放在手机与云端，等于公开押注与Meta音频眼镜同一技术路线。",
 "relevance":"无屏AI眼镜的光致变色镜片与云侧AI分工架构，是2026-2027年耳穿戴与眼镜融合形态的关键参考。",
 "vendor":"Nothing/首款AI原生设备及智能眼镜",
 "url":"https://www.163.com/dy/article/LAV8P13H0511B8LM.html",
 "source_name":"IT之家（网易转载）",
 "source_detail":"IT之家 2026-11-05 报道裴宇预告与Roland Quandt眼镜爆料；彭博社此前报道交叉印证",
 "note":"眼镜部分仍属爆料，发布形态与售价未定；Nothing现有产品线仅Ear系列耳机在去重清单内，眼镜与AI原生设备均为全新品类"
},
{
 "region":"intl","category":"AR-VR眼镜",
 "title":"Raven Prism眼镜式Linux计算机开放预售：全彩波导等效16英寸屏，热插拔电池可换模块",
 "status":"即将上市","date":"2026-11-05","main_dim":"显示/OLED","dims":"显示/OLED|电池/快充|AI/NPU",
 "grade":"C","stars":2,"signal_type":"发布","corroboration":2,
 "key_params":"独立Linux计算机（RavenOS）；全彩硅基液晶波导，等效一臂距离16英寸屏；四核64位ARM；49美元可退订金；2027年1月向早期用户发货；美国制造",
 "tech_features":["Raven Wings磁吸热插拔电池，换电不丢系统状态并预留AI加速器与蜂窝模块位","眼控数据本地处理加物理摄像头遮盖的隐私设计","开放系统底层访问与自有应用商店"],
 "why_important":"把完整Linux计算机装进眼镜并主打模块化供电，是AR之外个人计算眼镜的另一条路线；换电不断系统状态的设计，正面回应了穿戴设备续航与任务连续性的矛盾。",
 "relevance":"热插拔电池与本地AI隐私方案，为XR与穿戴终端的电源架构与安全设计提供新思路；模块化思路对配件生态规划有参考。",
 "vendor":"Raven Resonance/Raven Prism",
 "url":"https://m.10jqka.com.cn/20261105/c681491192.shtml",
 "source_name":"同花顺财经（转映维网Nweon）",
 "source_detail":"映维网 Nweon 2026-11-05 报道Raven Prism开放预售，同花顺财经转载",
 "note":"初创厂商、产品仍在预售阶段（2027年1月发货），量产与良率风险高；规格为厂商自述口径，售价未公布"
},
{
 "region":"intl","category":"笔记本电脑",
 "title":"宏碁Aspire X 16海外上架：首发酷睿Ultra X9 388H加2.8K 120Hz OLED，84Wh续航24小时",
 "status":"已上市","date":"2026-11-03","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|电池/快充",
 "grade":"B","stars":4,"signal_type":"开售","corroboration":2,
 "key_params":"16英寸2.8K OLED，SDR峰值500尼特、120Hz、100% DCI-P3；酷睿Ultra X9 388H（Panther Lake，Intel 18A）加Arc B390核显；16GB+512GB；84Wh电池最长24小时；约1.6kg，机身354.7×250.4×10.02-15.9mm",
 "tech_features":["Panther Lake平台酷睿Ultra X9 388H的首发机型之一","2.8K 120Hz OLED高刷高色域大屏下放到主流价位","84Wh电池在1.6kg机身实现标称24小时续航"],
 "why_important":"Panther Lake在主流消费本的落地样本，OLED高刷屏加大电池下探到主流价位，反映Intel 18A新平台在轻薄大屏本上的能效兑现程度。",
 "relevance":"Ultra X9 388H的能效表现与Arc B390核显规格，是2027年消费本平台选型的先行指标；84Wh配1.6kg的电源密度可作为轻薄本设计基线。",
 "vendor":"宏碁/Aspire X 16",
 "url":"https://m.ithome.com/html/1021837.htm",
 "source_name":"IT之家",
 "source_detail":"IT之家 2026-11-03 报道宏碁海外上架Aspire X 16；网易科技同日转载交叉印证",
 "note":"更高配SKU（32GB+2TB、Ultra 5 338H/X7 358H）尚未上架；与11-02期Swift Air 14、11-03期非凡Go Air均非同型号"
},
{
 "region":"intl","category":"笔记本电脑",
 "title":"微软Windows AI PC四级路线图曝光：8GB仅够入门，128GB才算能本地跑模型",
 "status":"进行中","date":"2026-11-04","main_dim":"AI/NPU","dims":"AI/NPU|SoC/芯片",
 "grade":"C","stars":3,"signal_type":"供应链/路线图泄露","corroboration":2,
 "key_params":"Tier 0：8GB内存起步，配Wildcat Lake酷睿300/400、锐龙100/200、骁龙X/X Plus，仅做基础本地AI；Tier 1：16-64GB，符合Copilot+，含Panther Lake酷睿Ultra 300、锐龙AI 400、骁龙X2 Plus/Elite；Tier 2：128GB起，本地构建运行模型，含RTX Spark；Tier 3：工作站级，Crescent Island单卡160-512GB显存",
 "tech_features":["按内存容量、AI算力与本地模型能力做四层分级，首次给出明确内存门槛","下一代平台被点名：Nova Lake、锐龙AI 500 Medusa Point、骁龙Next","Tier 2/3 把RTX Spark与DGX Station列为参考硬件"],
 "why_important":"微软把AI PC从营销概念拆成可量化的内存与算力分层，Tier 1的16GB门槛会直接影响整机厂的标配内存决策，也可能重新定义中低端机型的AI功能边界。",
 "relevance":"内存分级的硬门槛直接关系笔记本BOM（16GB成为AI PC入场券），是2027年平台与内存配置规划的重要输入；对端侧模型部署的算力预算同样有约束意义。",
 "vendor":"微软（Windows 混合智能路线图）",
 "url":"https://www.163.com/dy/article/LASRTHFD0511CPVM.html",
 "source_name":"网易（转快科技）",
 "source_detail":"快科技 2026-11-04 报道泄露PPT内容；Windows Central、cnBeta 同期报道同一份路线图，属两个独立媒体印证同一信源",
 "note":"源自泄露的PPT照片（爆料者HXL），微软未官方确认，平台代号与门槛均可能调整，按路线图信号而非发布信息收录"
},
{
 "region":"intl","category":"无线充",
 "title":"Peak Design首发充电线：号称全球首款Qi2.3认证磁吸充电宝，5000mAh接电可跑25W",
 "status":"已上市","date":"2026-11-03","main_dim":"认证/合规","dims":"认证/合规|电池/快充|结构/工艺",
 "grade":"A","stars":4,"signal_type":"发布","corroboration":2,
 "key_params":"Wireless Kickstand Travel Battery：5000mAh铝合金磁吸充电宝，99.95美元；接USB电源时Qi2.3无线25W，纯电池模式15W；Wireless Charging Station 2-in-1：双25W Qi2.2同时输出（需75W适配器），99.95美元；Dual Slim 65W GaN充电器64.95美元；11月3日开订",
 "tech_features":["厂商口径为全球首款Qi2.3认证无线充电器，小容量电芯实现25W无线","充电宝内置折叠支架，阳极氧化铝外壳","双pad无线座支持双设备同功率充电，另附USB-C口可充第三台"],
 "why_important":"Qi2.3新标准的首个消费级产品落地，5000mAh小体积做到25W无线，代表无线充电在功率、体积、散热三者间的新工程水位；高端摄影配件品牌切入充电市场，说明Qi2生态开始出现溢价竞争。",
 "relevance":"Qi2.2/2.3的功率档位推进节奏，直接决定下一代手机无线充电的配件设计上限；小容量高功率方案对电芯与散热选型有参考价值。",
 "vendor":"Peak Design/Wireless Kickstand Travel Battery 等",
 "url":"https://www.theverge.com/tech/1024484/peak-design-wireless-travel-battery-charging-charger-station-qi",
 "source_name":"The Verge",
 "source_detail":"The Verge 2026-11-03 报道Peak Design充电配件线发布与定价；Engadget、9to5Google 同期报道交叉印证",
 "note":"Qi2.3为厂商自称的首款认证，WPC官方认证清单未在报道中列出，待核实；与10-31期Belkin、11-03期Anker Prime均非同一产品"
},
{
 "region":"intl","category":"智能音箱",
 "title":"谷歌Home Speaker假日季首次降价：99.99降至79.99美元，Gemini Live仍需订阅解锁",
 "status":"已上市","date":"2026-11-02","main_dim":"音频","dims":"音频|AI/NPU|无线通信",
 "grade":"B","stars":3,"signal_type":"促销/商业模式","corroboration":2,
 "key_params":"2026年6月27日上市的Google Home Speaker原价99.99美元，11月2日至12月2日促销价79.99美元；360度音频、三远场麦克风加硬件静音开关；内置Matter中枢与Thread边界路由器；四色可选",
 "tech_features":["阔别六年更新的谷歌智能音箱新品首次降价","Matter加Thread双协议家庭中枢，配Gemini for Home","Gemini Live连续对话需订阅Home Premium，硬件让利软件收费"],
 "why_important":"谷歌用20美元让利在假日季抢AI音箱入口，却把核心AI能力锁进年费订阅，说明AI音箱正在走向硬件微利、软件收费的商业模式分化；与亚马逊Echo新品线的价格战将决定家庭AI入口份额。",
 "relevance":"音箱端侧AI算力配置与订阅制的绑定关系，是智能音频终端定义的前瞻信号；Matter/Thread双栈已成为家庭中枢的准入门槛。",
 "vendor":"谷歌/Google Home Speaker（2026）",
 "url":"https://9to5toys.com/2026/11/02/google-home-speaker-best-price-nest/",
 "source_name":"9to5Toys",
 "source_detail":"9to5Toys 2026-11-02 报道Best Buy首次现金折扣；9to5Google 同期报道Gemini Live订阅拆解",
 "note":"属渠道促销信息，非产品发布；与10-31期Amazon Echo 2026新品线为不同厂商产品"
},
{
 "region":"intl","category":"AI耳机·耳穿戴",
 "title":"三星Galaxy Buds On登陆美国：229美元11月6日开售，C形耳夹加S7 Gen1平台",
 "status":"已上市","date":"2026-11-06","main_dim":"音频","dims":"音频|SoC/芯片|结构/工艺",
 "grade":"B","stars":4,"signal_type":"开售","corroboration":2,
 "key_params":"C形耳夹开放式设计；高通Snapdragon S7 Gen1音频平台加Class-D功放；11.3mm级TwinBoost双低音单元；三麦克风加骨传导拾音；单次续航9.5小时、含盒38小时；IP54；美国229美元（韩国10月27日以29.9万韩元首发）",
 "tech_features":["三星首款耳夹式开放形态耳机，主打环境感知与佩戴安全","音频泄漏抑制技术降低外漏，双低音单元补开放结构的低频短板","头部手势控制、Bixby语音备忘检索与Gemini Live等Galaxy AI交互上耳"],
 "why_important":"229美元直接对标索尼LinkBuds Clip，把耳夹式开放耳机从细分品类推向大厂主战场；AI语音交互上耳意味着全天佩戴入口之争从手表蔓延到耳穿戴。",
 "relevance":"耳夹结构的声学补强方案（双低音加骨传导拾音）与S7 Gen1的端侧AI能力，是下一代开放式耳机的硬件基准。",
 "vendor":"三星/Galaxy Buds On",
 "url":"https://www.neoteo.com/en/galaxy-buds-on-launch-us-date-price-and-rollout",
 "source_name":"NeoTeo",
 "source_detail":"NeoTeo 报道美国11月6日上市与229美元定价；SamMobile 韩国10月27日首发与欧洲2027年初计划交叉印证",
 "note":"正文与美国上市日期一致，未发现与其他产品混淆；欧洲上市时间官方口径为2027年初，待确认"
},
]

def norm_region(r):
    r = (r or "").strip().lower()
    if r in ("国内", "cn", "china"):
        return "cn"
    if r in ("国际", "intl", "international", "global"):
        return "intl"
    return r

for d in DATA:
    d["region"] = norm_region(d.get("region",""))

assert len(DATA) == 30, "count=%d" % len(DATA)

for d in DATA:
    for k, v in list(d.items()):
        d[k] = clean(v)
    d["status"] = norm_status(d.get("status",""), d.get("date",""))
    d["stars"] = cap_stars(d["grade"], d["stars"])

dim_count = {dm: 0 for dm in DIMS}
for d in DATA:
    for p in [p.strip() for p in d["dims"].split("|")]:
        if p in dim_count:
            dim_count[p] += 1
covered = sum(1 for dm in DIMS if dim_count[dm] > 0)
grade_count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for d in DATA:
    grade_count[d["grade"]] += 1
five_star = sum(1 for d in DATA if d["stars"] == 5)
cn_n = sum(1 for d in DATA if d["region"]=="cn")
intl_n = sum(1 for d in DATA if d["region"]=="intl")

def sort_key(d):
    return (STATUS_RANK.get(d["status"], 9), -skey(d["date"]))
cn = sorted([d for d in DATA if d["region"]=="cn"], key=sort_key)
intl = sorted([d for d in DATA if d["region"]=="intl"], key=sort_key)
ordered = cn + intl

def top_sort(d):
    gr = {"A":0,"B":1,"C":2,"D":3,"E":4}[d["grade"]]
    return (-d["stars"], gr, STATUS_RANK.get(d["status"],9), -skey(d["date"]))
top5 = sorted(DATA, key=top_sort)[:5]

def stars(n):
    return "★" * n

def status_tag(status):
    if status == "即将上市":
        return '<span class="status-tag status-coming">即将上市</span>'
    if status == "进行中":
        return '<span class="status-tag status-progress">进行中</span>'
    return ""

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
        "tf": tf, "why": d["why_important"], "rel": d["relevance"], "vendor": d["vendor"],
        "date": d["date"], "url": d["url"], "sname": d["source_name"],
        "sdetail": d["source_detail"], "note": d["note"]
    }

def summary_row(n, d):
    return ('<tr><td>%d</td><td class="td-title"><a href="#card-%d">%s</a></td><td>%s</td>'
            '<td>%s</td><td class="td-status">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>') % (
        n, n, d["title"], region_tag(d["region"]), d["dims"].replace("|","/"),
        status_tag(d["status"]), source_tag(d["grade"]), d["date"], stars(d["stars"]))

dim_chips = ""
for dm in DIMS:
    c = dim_count[dm]
    onoff = "on" if c > 0 else "off"
    dim_chips += '<div class="dim-chip %s">%s <span class="dim-count">%d条</span></div>' % (onoff, dm, c)

top_cards = ""
for i, d in enumerate(top5, 1):
    top_cards += '''      <div class="signal-card">
        <div><span class="sig-rank">%d</span><span class="sig-title">%s</span></div>
        <div class="sig-tags"><span class="sig-dim">%s</span><span class="sig-stars">%s</span></div>
        <div class="sig-key">%s</div>
      </div>''' % (i, d["title"], d["main_dim"], stars(d["stars"]), d["key_params"][:60])

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
print("covered dims:", covered, "/16  missing:", [dm for dm in DIMS if dim_count[dm]==0])
print("A/B/C/D/E:", grade_count)
print("five_star:", five_star)
print("cn:", cn_n, "intl:", intl_n)
print("top5:", [d["title"][:22] for d in top5])
from collections import Counter
print("cn cats:", Counter(d["category"] for d in cn))
print("intl cats:", Counter(d["category"] for d in intl))
print("cn status:", [(d["status"], d["date"]) for d in cn])
print("intl status:", [(d["status"], d["date"]) for d in intl])
