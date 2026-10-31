# -*- coding: utf-8 -*-
"""生成 WB_2026-10-31_硬件看板.html —— 智能终端硬件情报日报
嵌入 30 条已核验情报（国内15 + 国际15），归一化、裁剪、渲染合规单 HTML。
"""
import re

TODAY = "2026-10-31"
TODAY_INT = 20261031
OUT = r"E:/AI相关/预研究/202608/03_输出/WB_2026-10-31_硬件看板.html"

DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头","结构/工艺",
        "传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉","折叠屏","BMS/电源","认证/合规"]

CATEGORY_ORDER = ["平板","手机","智能手表","AR-VR眼镜","笔记本电脑","无线充","智能音箱","AI耳机·耳穿戴"]

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

def to_ymd(s):
    s = (s or "").strip()
    try:
        if len(s) == 10:
            return int(s.replace("-",""))
        if len(s) == 7:
            y,m = s.split("-"); return int(y)*10000 + int(m)*100 + 15
    except Exception:
        pass
    return 0

STATUS_RANK = {"即将上市":0, "进行中":1, "已上市":2}

def norm_status(raw, date_str):
    s = (raw or "").strip()
    if any(k in s for k in ["即将","未上市","预售","曝光","官宣","定档","预热","预约","待发","公布","预告","前瞻"]):
        base = "即将上市"
    elif any(k in s for k in ["已上市","开售","发售","上架","现售","售卖","在售","上市","发布"]):
        base = "已上市"
    elif "进行中" in s:
        base = "进行中"
    else:
        base = "即将上市"
    if base == "已上市" and to_ymd(date_str) > TODAY_INT:
        base = "即将上市"
    return base

def cap_stars(g, s):
    s = int(s)
    return s if g == "A" else min(s, 4)

# ---------- 30 条已核验情报（region 标识 + 归一化字段）----------
DATA = [
 # ===================== 国内 15 条 =====================
 {"region":"cn","title":"荣耀 WIN 平板发布：8.4英寸2.3K 240Hz OLED+骁龙8 Elite Gen5+万级电池","category":"平板","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|电池/快充|散热","status":"已上市","stars":4,"grade":"B","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"8.4英寸2.3K 240Hz OLED电竞屏、骁龙8 Elite Gen5、10000mAh电池、东风涡轮主动散热风扇、国补到手3699元起","tech_features":["首发8.4英寸240Hz OLED电竞屏，局部峰值6000nit","搭载骁龙8 Elite Gen5旗舰平台","内置东风涡轮主动散热系统带高转速风扇","10000mAh大电池+66W快充","极客中心2.0开放性能自定义"],"why_important":"240Hz高刷小尺寸OLED平板直接对标iPad mini与拯救者平板，主动风冷+万级电池把游戏平板性能释放拉满，对TCL平板产品定义（高刷OLED、散热、续航）有强参考价值。荣耀WIN生态补全手机+游戏本+平板+耳机闭环。","relevance":"手机|笔记本电脑|AI耳机·耳穿戴","vendor":"荣耀 WIN 平板","date":"2026-10-21","url":"https://www.ithome.com/1/012/409.htm","source_name":"IT之家","source_detail":"IT之家 2026-10-13 报道，援引荣耀WIN电竞宇宙嘉年华官宣及10月13日技术沟通会","note":"正式售价与完整评测待补充"},
 {"region":"cn","title":"台电 M60 平板上市：12英寸2K屏+紫光展锐T7250，899元","category":"平板","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|电池/快充","status":"已上市","stars":3,"grade":"B","signal_type":"新品发布","corroboration":"1（单源）","key_params":"12英寸2000×1200 IPS LCD、紫光展锐T7250、6GB+128GB、8000mAh、4G通信、899元（国补755.65元）","tech_features":["12英寸2K IPS LCD面板","紫光展锐T7250八核处理器","8000mAh电池+4G通信","6GB+128GB存储可扩展","定价899元，国补后755.65元"],"why_important":"国产千元级大屏平板继续走国产芯+大电池+低价路线，紫光展锐T7250在入门平板渗透加速，对TCL入门平板成本结构与芯片选型有参考价值。","relevance":"手机","vendor":"台电 M60","date":"2026-10-05","url":"https://www.ithome.com/1/009/842.htm","source_name":"IT之家","source_detail":"IT之家 2026-10-05 报道，援引京东上架信息","note":"定位入门影音学习，性能偏入门"},
 {"region":"cn","title":"NECPC 发布 LAVIE Tab T12N/T8：天玑6400+12.1英寸2.5K屏","category":"平板","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|电池/快充|手写笔/触控","status":"已上市","stars":3,"grade":"B","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"T12N:12.1英寸2560×1600 90Hz LCD、天玑6400、8GB+256GB、10200mAh、530g，配键盘套与数位笔；T8:8.7英寸","tech_features":["T12N配12.1英寸2.5K 90Hz LCD","天玑6400 / 曦力G85双平台","T12N内置10200mAh大电池","配套键盘保护套+数位手写笔","10月27日随3款笔记本同步发布"],"why_important":"NEC/联想合资品牌以中屏2.5K+万级电池+手写笔键盘组合切入办公平板，佐证安卓平板向大屏+长续航+生产力配件演进，对TCL平板配件生态有借鉴。","relevance":"笔记本电脑|手写笔/触控","vendor":"NECPC LAVIE Tab T12N / T8","date":"2026-10-27","url":"https://news.qq.com/rain/a/20261027A0CXRZ00","source_name":"腾讯新闻（IT之家）","source_detail":"腾讯新闻 2026-10-27 转载IT之家，NECPC发布会","note":"国内行货渠道与定价待确认"},
 {"region":"cn","title":"联想小新 10.1 彩墨柔光版上架：护眼LCD+曦力G300","category":"平板","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|电池/快充|AI/NPU","status":"已上市","stars":3,"grade":"C","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"10.1英寸2136×1280 120Hz AG防眩LCD、联发科曦力G300、6/8GB+128GB、7060mAh、Android 17，1799元","tech_features":["10.1英寸120Hz防眩光LCD，获TÜV四项护眼认证","联发科曦力G300处理器","内置天骄学堂：AI口语教练/拍照讲题/涂鸦生图","7060mAh电池+3.5mm接口","提供趣学套装（保护壳+手写笔）"],"why_important":"学生平板以护眼认证+AI学习工具+家长管控为差异化而非堆性能，折射教育平板细分趋势；TCL若做学习平板可参考其护眼与AI辅导卖点组合。","relevance":"AI耳机·耳穿戴","vendor":"联想 小新 10.1 彩墨柔光版","date":"2026-10-23","url":"https://einkcn.com/html/product_6adc6a5d8b2f25993.html","source_name":"einkCN","source_detail":"einkCN 2026-10-24 报道，援引腾讯新闻，联想10月23日上架","note":"彩墨为显示模式而非电子纸；性能偏入门"},
 {"region":"cn","title":"REDMI K100 发布：骁龙8至尊版+独显D2+10000mAh硅碳电池","category":"手机","main_dim":"电池/快充","dims":"电池/快充|SoC/芯片|显示/OLED|无线通信","status":"即将上市","stars":4,"grade":"B","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"6.83英寸165Hz直屏、骁龙8至尊版+游戏独显D2、10000mAh小米金沙江电池（硅碳）、100W有线快充、Bose双扬、IP68","tech_features":["小米旗下首款电池破万手机，10000mAh硅碳电池","骁龙8至尊版+游戏独显D2双芯","6.83英寸165Hz直屏，3500nit峰值","100W有线+27W反充+旁路充电","Bose调音双扬+IP68+超声波指纹"],"why_important":"万级电池+硅碳负极成为2026下半年性能机标配，直接拉高续航基线；REDMI以双芯+超大电池在3000元档对标iQOO/一加，对TCL手机续航与快充定义有强对标意义。","relevance":"平板|笔记本电脑","vendor":"REDMI K100","date":"2026-10-27","url":"https://news.qq.com/rain/a/20261026A048IB00","source_name":"腾讯新闻（CNMO）","source_detail":"腾讯新闻 2026-10-26 报道，REDMI官宣10月27日发布","note":"最终售价10月27日揭晓，10月31日首销"},
 {"region":"cn","title":"iQOO Neo12 发布：2K 185Hz超冠屏+骁龙8E5+自研Q3芯片","category":"手机","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|散热|电池/快充|马达/触觉","status":"已上市","stars":5,"grade":"A","signal_type":"新品发布","corroboration":"3（多源印证）","key_params":"2K 185Hz超冠屏（天空之镜pTSF材料）、第五代骁龙8至尊版+自研电竞芯片Q3、冰穹风冷、9000mAh+100W，国补3149元起","tech_features":["联合清华/维信诺定制天空之镜pTSF发光材料2K 185Hz屏","第五代骁龙8至尊版+自研Q3电竞芯片（渲染/光追/AI三核）","冰穹风冷系统：59叶风扇+8200mm² 3D VC，降温7.2℃","9000mAh蓝海电池+100W快充","适配50+游戏原生185FPS、10款光追"],"why_important":"国产国屏之光2K 185Hz与自研电竞芯片Q3定义新一代游戏手机标杆，主动风冷+高亮高刷直屏对TCL游戏手机/平板的屏幕与散热路线有直接竞品对标价值；新华网报道增强可信度。","relevance":"平板|AI耳机·耳穿戴","vendor":"iQOO Neo 12","date":"2026-10-28","url":"https://www.news.cn/tech/20261029/d86e8f72f48b4943b344273c974a6929/c.html","source_name":"新华网","source_detail":"新华网 2026-10-29 报道，iQOO 10月28日发布会","note":"与iQOO Pad Pro同日发布，形成电竞双旗舰"},
 {"region":"cn","title":"华为 WATCH D3 发布：腕部动态血压记录仪，11.3mm","category":"智能手表","main_dim":"传感器","dims":"传感器|显示/OLED|生物识别|电池/快充","status":"已上市","stars":5,"grade":"B","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"腕部动态血压记录仪（中/欧双医疗器械认证）、11.3mm厚（减薄15%）、1.92英寸3000nit屏、一键微体检17项、2988元起","tech_features":["获中国二类医疗器械+欧盟CE MDR双认证","Hybrid融合测压：PPG无感监测+气囊示波法校准","整机11.3mm，较上代减薄15%","1.92英寸3000nit屏，一键微体检17项指标","运动前后血压模式+家庭空间健康关怀"],"why_important":"华为把专业血压监测做到消费级手表且获双医疗认证，证明健康传感（无创血压）是智能手表高端化核心赛道；对TCL手表产品定义（医疗级传感、轻薄化）提供明确对标与合规参考。","relevance":"手机","vendor":"华为 WATCH D3","date":"2026-10-01","url":"https://news.qq.com/rain/a/20261001A097AJ00","source_name":"腾讯新闻（闪电新闻）","source_detail":"腾讯新闻 2026-10-01 报道，华为Mate90系列及全场景发布会","note":"血压为辅助监测，非替代医疗设备"},
 {"region":"cn","title":"荣耀手表 6 Pro 开售：双层OLED+18天续航+CGM控糖","category":"智能手表","main_dim":"电池/快充","dims":"电池/快充|显示/OLED|传感器|生物识别","status":"已上市","stars":3,"grade":"C","signal_type":"新品发布","corroboration":"1（单源）","key_params":"1.5英寸双层OLED（466×466，5500nit）、最长18天续航（500mAh）、无感血压2.0+CGM控糖助手","tech_features":["1.5英寸双层OLED，峰值5500nit","最长18天续航，500mAh电池","无感血压2.0+AI数据解读","CGM控糖助手个性化建议","荣耀北极星定位+湿手触控"],"why_important":"长续航+双层OLED+健康传感（血压/控糖）是国产手表主流打法，荣耀以青海湖电池延续续航优势；TCL手表可参考长续航+健康AI解读组合与双层OLED提亮路线。","relevance":"手机","vendor":"荣耀 手表 6 Pro","date":"2026-10-08","url":"https://www.toutiao.com/article/7693971320849170984","source_name":"今日头条（智能穿戴测评）","source_detail":"今日头条 2026-10-08 报道，荣耀手表6 Pro开售","note":"价格未明确，定位中高端"},
 {"region":"cn","title":"雷鸟 GT Max bilibili限定版发布：78g巨幕AR眼镜","category":"AR-VR眼镜","main_dim":"显示/OLED","dims":"显示/OLED|音频|传感器|结构/工艺","status":"已上市","stars":4,"grade":"B","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"78g、等效267英寸巨幕、FOV 59°、孔雀光学引擎3.0 Max+独立画质芯片Vision4000、1200nit、120Hz、B&O四扬声器、2294元","tech_features":["78g轻量化，等效267英寸虚拟大屏","FOV 59°，孔雀光学引擎3.0 Max+Vision4000画质芯片","峰值1200nit、120Hz、3840Hz高频PWM","原生3DoF空间悬停","B&O联调四扬声器空间音频"],"why_important":"雷鸟以轻量化+独立画质芯片+大牌声学联名巩固影视巨幕AR眼镜优势，并借电竞IP（BLG）做圈层营销；对TCL AR/XR产品定义（轻量化、光学引擎、内容生态联名）有参考。","relevance":"手机|智能音箱","vendor":"雷鸟 RayNeo GT Max bilibili限定版","date":"2026-10-23","url":"https://www.163.com/dy/article/L9U2ML3A0511B8LM.html","source_name":"网易（IT之家）","source_detail":"网易 2026-10-23 转载IT之家，雷鸟创新×bilibili发布","note":"为S16赛事联名限定版，常规版GT Max同期在售"},
 {"region":"cn","title":"Rokid Glasses 2 发布：骁龙AR1+平台带显示AI眼镜","category":"AR-VR眼镜","main_dim":"AI/NPU","dims":"AI/NPU|显示/OLED|传感器|结构/工艺","status":"已上市","stars":5,"grade":"B","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"第一代骁龙AR1+平台+恒玄BES2800BP双芯片、Android/RTOS双系统、彩虹纹降60%/反射率降70%、起售价3699元","tech_features":["搭载第一代骁龙AR1+与恒玄BES2800BP双芯片","耦入光栅镀膜+超低反，彩虹纹降60%、反射率降70%","光机体积较上代减30%，柔性镜腿更大鼻托","AAC扬声器+杜比认证音效","2026上半年Rokid占全球带显示AI/AR眼镜41%份额"],"why_important":"Rokid以光学效率提升+双芯片架构+自然交互定义带显示AI眼镜新形态，并占全球带显示AI眼镜四成份额；对TCL布局AI眼镜（显示光学、端侧AI、Agent生态）是重要竞品与技术对标对象。","relevance":"手机|AI耳机·耳穿戴","vendor":"Rokid Glasses 2","date":"2026-10-27","url":"https://www.stdaily.com/web/gdxw/2026-10/28/content_604275.html","source_name":"科技日报","source_detail":"科技日报 2026-10-28 报道，乐奇Rokid Jungle 2026发布会","note":"同步发布全彩Rokid Color与交互戒指Rokid Ring"},
 {"region":"cn","title":"REDMI Book 14 2027 发布：72Wh电池+2.8K 120Hz+AI小爱","category":"笔记本电脑","main_dim":"电池/快充","dims":"电池/快充|显示/OLED|AI/NPU|无线通信","status":"即将上市","stars":4,"grade":"B","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"14英寸2.8K 120Hz屏、第三代英特尔酷睿（18A）、72Wh电池（20.2h续航）、LPDDR5X、超级小爱2.0，国补5779元起","tech_features":["第三代英特尔酷睿18A平台+LPDDR5X","72Wh大电池，实测办公续航20.2小时","14英寸2.8K 120Hz屏，100% sRGB","超级小爱2.0（MiMo大模型）：PPT生成/摘要/跨设备协同","双USB-A+双USB-C+HDMI，1.28kg"],"why_important":"REDMI把72Wh大电池与端侧AI助手下放到主流轻薄本，并强化手机-平板-电脑三端协同；对TCL笔记本的续航基线、AI PC交互与跨端生态构建是直接竞品参考。","relevance":"手机|平板","vendor":"REDMI Book 14 2027","date":"2026-10-27","url":"https://nb.zol.com.cn/1265/12659176.html","source_name":"中关村在线","source_detail":"中关村在线 2026-10-28 报道，REDMI 10月27日发布会","note":"16英寸版同步提供，11月3日发售"},
 {"region":"cn","title":"荣耀 MagicBook 14 2026 款：酷睿Ultra NPU+3K屏+140W","category":"笔记本电脑","main_dim":"AI/NPU","dims":"AI/NPU|显示/OLED|电池/快充|结构/工艺","status":"已上市","stars":3,"grade":"B","signal_type":"新品发布","corroboration":"1（单源）","key_params":"英特尔酷睿Ultra（集成NPU）、14英寸3K高刷护眼屏、100% DCI-P3、1.39kg/15.8mm、12小时续航、140W超级快充，到手6969元","tech_features":["全新酷睿Ultra集成NPU，本地大模型运行","14英寸3K高刷护眼屏，100% DCI-P3","轻至1.39kg、薄至15.8mm金属机身","140W超级快充，续航约12小时","AI算力跃升，智能办公加速"],"why_important":"荣耀以酷睿Ultra NPU本地AI+高色域轻薄+140W快充卡位AI轻薄本，与华为/小米形成国产AI PC trio；对TCL笔记本的NPU本地AI卖点与快充规格有对标参考。","relevance":"手机|平板","vendor":"荣耀 MagicBook 14 2026","date":"2026-10-22","url":"https://nb.zol.com.cn/1263/12633212_all.html","source_name":"中关村在线","source_detail":"中关村在线 2026-10-22 报道，荣耀MagicBook 14 2026款AI轻薄本","note":"报道侧重促销价，完整评测待补充"},
 {"region":"cn","title":"AUKEY MC319B 发布：Qi2.2 25W三合一磁吸折叠无线充","category":"无线充","main_dim":"BMS/电源","dims":"BMS/电源|无线通信|结构/工艺|认证/合规","status":"即将上市","stars":3,"grade":"C","signal_type":"新品发布","corroboration":"1（单源）","key_params":"Qi2.2（Qi2 25W）标准、三合一（手机15/25W+耳机5W+手表2.5W）、折叠17.5mm、240g、铝合金机身、预购约¥845","tech_features":["最新Qi2.2标准，手机最高25W无线快充","三合一：iPhone+AirPods+Apple Watch同充","折叠设计收合仅17.5mm，重240g","铝合金机身+强力磁吸精准对位","附收纳包与1.5m 60W C-C线，2年保固"],"why_important":"Qi2.2 25W三合一磁吸无线充成为2026配件升级主线（倍思/绿联/傲基集体上新），25W无线快充+折叠便携是桌面/出行新标准；对TCL周边配件（无线充）的产品规划与功率规格有对标价值。","relevance":"手机|AI耳机·耳穿戴","vendor":"AUKEY 傲基 MC 319B","date":"2026-10-06","url":"https://www.witsper.com/en/products/aukey-mc319b","source_name":"WitsPer（AUKEY渠道）","source_detail":"WitsPer智選家 2026-10-06 上架AUKEY MC319B预购页","note":"台港渠道预购，大陆行货与定价待确认；竞品倍思/绿联同规格已布局"},
 {"region":"cn","title":"小米智能音箱 Pro 大促：首搭超级小爱大模型+三曲库","category":"智能音箱","main_dim":"AI/NPU","dims":"AI/NPU|音频|无线通信|认证/合规","status":"已上市","stars":3,"grade":"B","signal_type":"行业动态","corroboration":"1（单源）","key_params":"内置超级小爱大模型、支持小米/QQ音乐/网易云三大曲库、织物机身+氛围灯带、远场拾音、全屋智能中控","tech_features":["首款搭载超级小爱大模型的小米音箱","打通小米/QQ音乐/网易云三大曲库","织物包裹+顶部氛围灯带，大单元低音","远场拾音优化，全屋智能中控","语音问答/写文案/做规划"],"why_important":"智能音箱从音箱转向大模型家庭中枢，超级小爱把语音助手升级为本地+云端AI代理；对TCL智能音箱/家居中控的AI化与多曲库生态整合有参考。","relevance":"手机|平板","vendor":"小米 智能音箱 Pro","date":"2026-10-19","url":"https://finance.sina.com.cn/tech/discovery/2026-10-19/doc-inivueuh0880665.shtml","source_name":"新浪科技（快科技）","source_detail":"新浪科技 2026-10-19 转载快科技，小米智能音箱Pro大促","note":"报道聚焦新人音乐会员福利活动"},
 {"region":"cn","title":"国家中试基地发布AI耳机方案：端侧听觉模型+昇腾适配+eSIM，做成可复用基座","category":"AI耳机·耳穿戴","main_dim":"AI/NPU","dims":"AI/NPU|音频|无线通信|认证/合规","status":"进行中","stars":4,"grade":"B","signal_type":"行业动态（方案/平台发布）","corroboration":"2（多源印证）","key_params":"端侧听觉模型+端云协同；能力覆盖多模态感知/自适应助听/健康监测/会议转写/实时翻译；支持昇腾等国产芯片适配与eSIM集成；可赋能耳机、AR眼镜、机器人；2026-10-22 深圳发布","tech_features":["构建端侧听觉模型，打造端云协同体系并配套数据闭环调优","支持昇腾等国产化芯片适配与eSIM集成，可脱离手机独立联网","能力覆盖多模态感知、自适应助听、健康监测、会议转写与实时翻译","面向厂商提供一体化基座服务，新品开发周期从数月压缩至1-2周","依托源自中科院声学所的声智科技团队攻坚复杂声学环境","同一听觉栈可复用至耳机、AR眼镜、机器人等11类终端"],"why_important":"国家级中试平台把AI耳机拆成「端侧听觉模型+国产芯片+eSIM」的可复用基座，中小品牌乃至整机厂可跳过从0搭算法与声学链路，直接比拼结构、佩戴与成本。对TCL耳机/耳穿戴的自研vs外采决策，以及AI眼镜、桌面机器人复用同一听觉栈，都有直接路径参考。","relevance":"手机|平板|AR-VR眼镜","vendor":"国家人工智能应用中试基地（消费领域移动终端方向）","date":"2026-10-22","url":"https://www.ccidcom.com/xinwenku/20261026/1QOQtE53zPbCSSFrm1d1gvf2bqe8w.html","source_name":"通信产业网","source_detail":"通信产业网 2026-10-26 报道「百场万企」AI终端专场（深圳，10/22）；东方财富/广州日报 10-27 同步报道","note":"方案的具体模型规模、功耗与BOM未公开，需向基地索取技术白皮书；由中国联通承建，下设芯片应用开发/昇腾生态适配/开源鸿蒙适配等五大中心"},
 # ===================== 国际 15 条 =====================
 {"region":"intl","title":"Samsung Galaxy S26 FE","category":"手机","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|摄像头|电池/快充|无线通信","status":"已上市","stars":4,"grade":"A","signal_type":"官方发布","corroboration":"2（多源印证）","key_params":"Exynos 2500, 6.7英寸 120Hz AMOLED 1900nit, 50MP主摄+8MP 3x长焦, 4900mAh, 45W/15W无线, One UI 9, 7年更新","tech_features":["Galaxy AI: Now Brief/Now Nudge, My FanCam","Super Steady Horizontal Lock, Photo Assist","Gemini Omni, Circle to Search, Gemini Live","Exynos 2500 (3nm) 旗舰芯片","7年系统更新承诺"],"why_important":"S26系列首款预装One UI 9的机型，把旗舰AI与长焦影像下放到FE价位($699)，7年更新承诺重塑中端价值，对TCL中端手机的长期维护策略有参考。","relevance":"智能手机","vendor":"Samsung","date":"2026-09-04","url":"https://news.samsung.com/za/samsung-unveils-galaxy-s26-fe-one-ui-9-advanced-camera-ai-and-galaxy-ai-from-day-one","source_name":"Samsung Newsroom (South Africa)","source_detail":"官方发布稿，含完整规格表与AI功能说明","note":"8/27发布，9/4南非等地上市，10/5全球渠道铺货，属60天窗口内上市"},
 {"region":"intl","title":"Samsung Galaxy Tab S12 Ultra","category":"平板","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|电池/快充|手写笔/触控","status":"已上市","stars":5,"grade":"A","signal_type":"官方发布","corroboration":"2（多源印证）","key_params":"14.6英寸 Dynamic AMOLED 2X 120Hz, 天玑9500, 11600mAh, IP68, S Pen, One UI 9, 7年更新","tech_features":["三星最薄(5.1mm)最强Galaxy Tab","NPU较S11 Ultra快61%","IP68+Photoshop预装打造移动创作旗舰","4声道空间音频; 3D均热板","Vision Booster, S Pen随附"],"why_important":"三星最薄最强Galaxy Tab，NPU较S11 Ultra快61%，IP68+Photoshop预装打造移动创作旗舰，对TCL高端平板的显示/算力/生产力组合有直接竞品对标。","relevance":"平板电脑","vendor":"Samsung","date":"2026-10-01","url":"https://www.samsung.com/nz/news/local//samsung-introduces-galaxy-tab-s12-series-the-ultimate-productivity-powerhouse-built-for-growth","source_name":"Samsung Newsroom (New Zealand)","source_detail":"官方发布稿，含完整规格与上市信息(10/21新西兰上市)","note":"10/1发布、10/7美国开售、10/21新西兰上市"},
 {"region":"intl","title":"Samsung Galaxy Tab S12+","category":"平板","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|电池/快充|手写笔/触控","status":"已上市","stars":3,"grade":"A","signal_type":"官方发布","corroboration":"2（多源印证）","key_params":"12.6英寸 Dynamic AMOLED 2X 120Hz, 天玑9500, 10600mAh, IP68, S Pen, microSD可扩展至2TB","tech_features":["120Hz AMOLED, 随附S Pen与microSD扩展","Galaxy AI多窗口/DeX","Vision Booster; 4声道空间音频","较上代更窄边框","直面iPad Air，性价比生产力平板"],"why_important":"以更低价格提供120Hz AMOLED、随附S Pen与microSD扩展，直面iPad Air，性价比生产力平板，对TCL平板的规格与定价策略有参考。","relevance":"平板电脑","vendor":"Samsung","date":"2026-10-02","url":"https://www.samsung.com/hk_en/news/product/samsung-introduces-galaxy-tab-s12-series-the-ultimate-productivity-powerhouse-built-for-growth/","source_name":"Samsung Newsroom (Hong Kong)","source_detail":"官方发布稿，含S12+规格(美区10/7上市, $1199.99起)","note":"与Ultra同代发布，主攻稍低价位生产力市场"},
 {"region":"intl","title":"REDMAGIC Astra 2 游戏平板发表","category":"平板","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|散热|电池/快充","status":"已上市","stars":4,"grade":"B","signal_type":"新品发布","corroboration":"2（多源印证）","key_params":"9.06英寸 OLED 185Hz, Snapdragon 8 Elite Gen 5, 16GB+512GB, 8300mAh, 双USB-C, $749","tech_features":["9.06英寸OLED 185Hz电竞屏","Snapdragon 8 Elite Gen 5 + AquaCore Cooling 2.0散热","8300mAh电池，双USB-C","支持PC游戏模拟与Moonlight串流","金属机身+可自定义灯效，起价$749"],"why_important":"红魔把185Hz OLED电竞屏与主动散热游戏平板推向全球市场，对TCL游戏平板的高刷OLED与散热路线有直接竞品对标价值。","relevance":"平板电脑","vendor":"REDMAGIC (nubia)","date":"2026-10-06","url":"https://life.tw/article/redmagic-astra-2-%E9%81%8A%E6%88%B2%E5%B9%B3%E6%9D%BF%E7%99%BC%E8%A1%A8-%E6%90%AD%E8%BC%89%E9%A0%82%E7%B4%9A%E6%99%B6%E7%89%87-3171045","source_name":"LIFE生活網（商傳媒）","source_detail":"LIFE生活網 2026-10-06 报道，REDMAGIC Astra 2 發表","note":"10月5日发表，全球定价$749，标配不含充电器"},
 {"region":"intl","title":"华为 MatePad Pro 12 (2026) 登陆欧洲：4.7mm/454g + PaperMatte OLED，€1,099起","category":"平板","main_dim":"显示/OLED","dims":"显示/OLED|SoC/芯片|电池/快充|结构/工艺|手写笔/触控","status":"已上市","stars":3,"grade":"C","signal_type":"上市/海外扩展","corroboration":"1（单源）","key_params":"12英寸PaperMatte OLED 3036×1952、峰值1600nit、麒麟T93（8核）、4.7mm/454g、66W有线+40W反向、视频13.7小时、€1,099起","tech_features":["12英寸PaperMatte纳米蚀刻OLED，3036×1952、峰值1600nit","整机4.7mm/454g，较上代更薄更轻","麒麟T93八核平台，官方称较上代T92显著提升","66W有线快充，并支持最高40W USB-C反向给手机充电","10/13德国开卖，官网赠M-Pencil Pro（截至11/17），键盘套另加€200"],"why_important":"华为把柔光OLED（PaperMatte）与4.7mm/454g的轻薄堆叠同时做到12英寸旗舰，并直接以€1,099进欧洲正面对标iPad Air；对TCL平板的显示贴合方案（防眩涂层 vs 传统AG膜）、中框与电池堆叠厚度分配是可直接量化的对标样本。麒麟T93也说明国产SoC在中高端平板仍在按代迭代。","relevance":"平板电脑|笔记本电脑","vendor":"华为 MatePad Pro 12 (2026)","date":"2026-10-13","url":"https://www.gsmgotech.com/2026/10/huawei-matepad-pro-12-2026-goes-global.html","source_name":"GSM GoTech","source_detail":"GSM GoTech 2026-10-13 报道，华为德国官网与柏林旗舰店当日开售；国行版本2026年8月已发布","note":"单源报道（中小垂直媒体），欧洲定价€1,099可查但国行差价大；麒麟T93具体制程未公开"},
 {"region":"intl","title":"Garmin Enduro 4","category":"智能手表","main_dim":"传感器","dims":"传感器|结构/工艺|电池/快充","status":"已上市","stars":4,"grade":"A","signal_type":"官方发布","corroboration":"2（多源印证）","key_params":"51mm, MIP太阳能, 320小时GPS续航, 10ATM, LED手电, 钛金属, 全彩地图","tech_features":["活动电量模式; 全彩地图+3D立体检视","进阶体力/耐力指标","Garmin Epic 92天训练故事","多频GNSS","钛金属圈+蓝宝石镜面"],"why_important":"超长耐力运动旗舰，太阳能+320h续航+全彩地图重新定义超马/越野场景，10/19上市，对TCL运动健康手表的续航与传感器路线有参考。","relevance":"智能手表","vendor":"Garmin","date":"2026-10-07","url":"https://www.garmin.com.tw/news/newscenter/news-2026-oct-approach-s72-enduro-4","source_name":"Garmin Newsroom (Taiwan)","source_detail":"官方发布稿，含Enduro 4与Approach S72完整规格，10/19上市","note":"与Approach S72同场10/7发布"},
 {"region":"intl","title":"Garmin Approach S72","category":"智能手表","main_dim":"传感器","dims":"传感器|显示/OLED|结构/工艺","status":"已上市","stars":3,"grade":"A","signal_type":"官方发布","corroboration":"2（多源印证）","key_params":"43/47mm, AMOLED, 高尔夫生理数据, 挥杆指标, 练习场模式, 果岭坡度判读","tech_features":["赛后心率波动复盘","挥杆手部速度/上杆幅度/手腕旋转","练习场自动追踪","Garmin Golf会员果岭坡度/推杆分析","钛金属圈+蓝宝石镜面"],"why_important":"面向高尔夫年轻化趋势(20岁以下球员增76%)的旗舰腕表，量化挥杆与果岭决策，对TCL手表垂直场景深耕有启发。","relevance":"智能手表","vendor":"Garmin","date":"2026-10-07","url":"https://www.garmin.com.tw/news/newscenter/news-2026-oct-approach-s72-enduro-4","source_name":"Garmin Newsroom (Taiwan)","source_detail":"官方发布稿，10/19台湾上市","note":"与Enduro 4同场发布，主攻高尔夫垂直场景"},
 {"region":"intl","title":"Meta Ray-Ban Display 登陆欧洲（德国电信开售）","category":"AR-VR眼镜","main_dim":"显示/OLED","dims":"显示/OLED|AI/NPU|摄像头|传感器|音频","status":"已上市","stars":4,"grade":"B","signal_type":"官方上市/扩展","corroboration":"2（多源印证）","key_params":"$799(含Neural Band), 600×600彩显, 12MP/3x, 神经腕带手势控制, 德国电信10/13起德国发售","tech_features":["镜内Meta AI视觉回答; 实时字幕/翻译","免提视频通话; 导航叠加","神经腕带细微手势控制","本地相册3D化","开放式耳机+6麦克风"],"why_important":"首款面向大众的彩色显示AI眼镜，神经腕带交互+欧盟扩区，定义头显之外的最强可穿戴AI入口，对TCL AI眼镜（显示光学、端侧AI）是重要竞品对标。","relevance":"AI耳机·耳穿戴","vendor":"Meta (Ray-Ban)","date":"2026-10-13","url":"https://www.vrtuoluo.cn/546163.html","source_name":"VR陀螺（编译）","source_detail":"VR陀螺 2026-10-14 编译，德国电信10/13起德国发售Meta Ray-Ban Display","note":"美国早前上市，本次以欧盟扩展计入近15天窗口"},
 {"region":"intl","title":"Ray-Ban Meta Gen 3","category":"AR-VR眼镜","main_dim":"AI/NPU","dims":"AI/NPU|音频|摄像头|传感器","status":"已上市","stars":4,"grade":"B","signal_type":"官方上市","corroboration":"2（多源印证）","key_params":"$449, AI相机眼镜, Meta AI, 免提步行导航, Spatial Audio, 9/23美国开售","tech_features":["Meta AI拍照/录像/通话/音乐","新增免提步行导航与Spatial Audio","第三方应用(如Naver Map)首发","Mandarin支持","100+镜框可选"],"why_important":"销量第一的AI眼镜主力迭代，9/23上市后成最主流AI可穿戴，验证无屏AI眼镜市场主流地位，对TCL无屏AI音频/眼镜路线有参考。","relevance":"AI耳机·耳穿戴","vendor":"Meta (Ray-Ban)","date":"2026-09-23","url":"https://www.metaversewatcher.io/best-smart-glasses-2026","source_name":"MetaverseWatcher","source_detail":"2026智能眼镜选购指南，含Gen 3售价$449、9/23开售与软件更新","note":"属60天窗口内；与Ray-Ban Display形成Meta显示/无显示双线"},
 {"region":"intl","title":"ASUS ProArt P16/P14（RTX Spark）美国开售：最高128GB统一内存+1 PFLOPS本地AI","category":"笔记本电脑","main_dim":"AI/NPU","dims":"AI/NPU|显示/OLED|结构/工艺|散热|电池/快充","status":"已上市","stars":4,"grade":"A","signal_type":"官方上市","corroboration":"2（多源印证）","key_params":"RTX Spark N1X（20核Grace CPU+最高6144核Blackwell GPU+第五代Tensor Core FP4）、最高1 PFLOPS、最高128GB LPDDR5X统一内存、2TB SSD、16英寸4K 120Hz OLED 1600nit、99.9Wh+140W、P16 $2,799.99起","tech_features":["NVIDIA RTX Spark超级芯片：20核Grace CPU+最高6144核Blackwell RTX GPU","最高128GB LPDDR5X统一内存，NVLink-C2C互联消除CPU/GPU数据搬运","最高1 PFLOPS（FP4）算力，可本地跑LLM/VLM、LoRA微调与Agent工作流","16英寸4K(3840×2400) Lumina Pro OLED，120Hz/1600nit，VESA DisplayHDR True Black 1000","99.9Wh电池+140W Type-C适配器，机身12.9mm/1.77kg","预装MuseTree（FLUX/WAN）、StoryCube，并原生支持ComfyUI与Hermes Agent"],"why_important":"RTX Spark把Grace CPU与Blackwell GPU做成统一内存的单一超芯，128GB让本地跑120B级模型成为可交付形态，ASUS官方更给出「5-10个月可摊平云端token成本」的TCO口径——这是AI PC从「NPU跑小模型」转向「本地跑大模型」的分水岭。对TCL笔记本/AI终端的算力路线选择（NPU vs 统一内存SoC）与散热、供电设计（140W）是直接前瞻样本。","relevance":"笔记本电脑|平板电脑|AI/NPU","vendor":"ASUS ProArt P16 / P14（H7607BA / H7407BA）","date":"2026-10-16","url":"https://www.asus.com/us/news/proart-rtxspark-buynow/","source_name":"ASUS 官方新闻室（美国）","source_detail":"ASUS 美国官方新闻稿 2026-10-16：ProArt P16/P14 已在 ASUS Store 与 Best Buy 开售，P16 MSRP $2,799.99起、P14 $2,599.99起","note":"128GB版本仅在ASUS Store有货，Best Buy最高64GB；Micro Center预计2026Q4初到店，起价随配置浮动"},
 {"region":"intl","title":"Dell XPS 16 Creator Edition (RTX Spark)","category":"笔记本电脑","main_dim":"AI/NPU","dims":"AI/NPU|显示/OLED|结构/工艺","status":"即将上市","stars":5,"grade":"A","signal_type":"官方预购","corroboration":"2（多源印证）","key_params":"RTX Spark最高128GB统一内存, 3.2K Tandem OLED, 0.7英寸机身, $3799.99, 10/16出货","tech_features":["本地运行大型LLM/微调/推理(无需云)","CUDA全栈; DLSS/光追游戏","GitHub Copilot/Claude Code/ComfyUI/Cursor原生","出厂校色Pantone","0.7英寸机身塞入128GB统一内存"],"why_important":"XPS首款RTX Spark机型，0.7英寸机身塞入128GB统一内存与工作站级创作/AI能力，重新定义轻薄创作本，对TCL高端创作本有标杆意义。","relevance":"笔记本电脑","vendor":"Dell","date":"2026-10-07","url":"https://www.dell.com/en-us/blog/dell-xps-16-creator-edition-where-nvidia-rtx-spark-meets-premium-design","source_name":"Dell 官方博客","source_detail":"官方产品博客，含RTX Spark规格、显示、端口、价格与Best Buy预购链接","note":"10/7 Best Buy 开启预售，$3799.99起；戴尔官方博客未给出确切出货日，10/16 为渠道侧说法"},
 {"region":"intl","title":"Belkin Qi2.2 25W ChillBoost 无线充电器","category":"无线充","main_dim":"BMS/电源","dims":"BMS/电源|无线通信|散热|认证/合规","status":"已上市","stars":4,"grade":"A","signal_type":"官方上市","corroboration":"2（多源印证）","key_params":"Qi2.2 25W, ChillBoost主动/被动散热, 0-50%约25分钟, 兼容Qi2磁吸机型","tech_features":["解决25W无线充电发热降速","智能温控+优化线圈","保护电池健康","磁吸对齐满速25W","首批通过Qi2.2 25W认证"],"why_important":"Belkin首批通过Qi2.2 25W认证充电器，主动散热让高速无线充稳定不降速，标志Qi2 25W生态落地，对TCL周边配件（无线充）功率规格有对标价值。","relevance":"手机","vendor":"Belkin","date":"2026-10-01","url":"https://www.belkin.com/hk/en/company/blog/25w-qi2-wireless-charging-cooling-technology","source_name":"Belkin 官方博客","source_detail":"官方技术博客说明ChillBoost与Qi2 25W产品线，Magnetic Charger已开售","note":"2026年Qi2.2 25W生态首发产品，年内持续铺货"},
 {"region":"intl","title":"Amazon Echo 2026 新品线 (Echo Dot / Studio / Show 16 等)","category":"智能音箱","main_dim":"AI/NPU","dims":"AI/NPU|音频|无线通信|传感器","status":"已上市","stars":4,"grade":"B","signal_type":"官方发布","corroboration":"2（多源印证）","key_params":"Echo Dot首搭AZ3端侧AI芯片与Matter/Thread中枢; Echo Studio加摄像头; Echo Show 16配16英寸屏; Alexa+","tech_features":["AZ3端侧AI加速(语音识别/降噪)","Omnisense温感与人存在检测","Alexa Home Map全屋可视化","屏上生成购物比较卡","Fire TV集成"],"why_important":"亚马逊秋季密集发布5款Alexa+设备，Echo Dot首次内置智能中枢与自研AZ3芯片，巩固全屋智能入口，对TCL智能音箱/家居中控的AI化有参考。","relevance":"智能音箱","vendor":"Amazon","date":"2026-10-29","url":"https://www.androidcentral.com/accessories/smart-home/amazons-latest-suite-of-alexa-powered-echo-devices-includes-a-digital-photo-frame","source_name":"Android Central","source_detail":"报道Amazon 10/29发布四款Echo+Alexa相框，含定价与规格","note":"落在近7天窗口；以Echo Dot(中枢+AZ3)为代表性单品"},
 {"region":"intl","title":"Nothing Ear (3)","category":"AI耳机·耳穿戴","main_dim":"AI/NPU","dims":"AI/NPU|音频|生物识别|认证/合规","status":"已上市","stars":4,"grade":"A","signal_type":"官方上市","corroboration":"2（多源印证）","key_params":"12mm动圈, 实时ANC, Static空间音频, Super Mic, Essential Space+ChatGPT, 55mAh/38h, IP54","tech_features":["AI驱动环境降噪(2000万小时真实音频训练)","Essential Space语音笔记自动转写","配对Nothing手机唤醒ChatGPT","动态低音增强","0.35mm金属天线"],"why_important":"Nothing旗舰真无线首次把端侧ChatGPT与Essential Space深度整合，定义会思考的耳机，强化AI可穿戴阵营，对TCL耳机的端侧AI路线有对标价值。","relevance":"AI耳机·耳穿戴","vendor":"Nothing","date":"2026-10-01","url":"https://nothing.tech/products/ear-3","source_name":"Nothing 官方产品页","source_detail":"官方规格页含驱动/ANC/空间音频/Super Mic/电池与AI功能","note":"Nothing为英国品牌(非中国)，符合国际/全球市场要求"},
 {"region":"intl","title":"Samsung Galaxy A18 & A08","category":"手机","main_dim":"显示/OLED","dims":"显示/OLED|摄像头|AI/NPU|电池/快充|生物识别","status":"已上市","stars":3,"grade":"A","signal_type":"官方发布","corroboration":"2（多源印证）","key_params":"6.7英寸 FHD+ Super AMOLED, Helio G99+, 50MP三摄, IP64, 6年系统更新, Circle to Search + Gemini/Perplexity AI","tech_features":["6.7英寸FHD+ Super AMOLED (A18)","Helio G99+ 6nm, LPDDR5","Circle to Search + Gemini/Perplexity AI agents","IP64防尘防溅, Knox Vault","6代系统更新+6年安全更新"],"why_important":"Galaxy A18/A08把Super AMOLED、6年系统支持与端侧AI agents下放到预算档，抬升TCL在新兴市场平价手机需达到的基线。","relevance":"智能手机","vendor":"Samsung","date":"2026-10-05","url":"https://www.samsung.com/nz/news/local/samsung-elevates-the-everyday-smartphone-experience-with-the-new-galaxy-a18-and-galaxy-a08","source_name":"Samsung Newsroom (New Zealand)","source_detail":"Samsung官方，2026-10-05 unveil；A08 10/16起售，A18 11/27上市","note":"A18 11/27上市、A08已在售；以系列发布计入"},
]

# ---------- 归一化 ----------
def clean(s):
    if isinstance(s, str):
        s = s.replace("{", "").replace("}", "")
        s = re.sub(r'^[①-⑩]\s*', '', s.strip())
    if isinstance(s, list):
        return [clean(x) for x in s]
    return s

for d in DATA:
    for k, v in list(d.items()):
        d[k] = clean(v)
    d["status"] = norm_status(d["status"], d["date"])
    d["stars"] = cap_stars(d["grade"], d["stars"])

assert len(DATA) == 30, "count=%d" % len(DATA)

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
cn_n = sum(1 for d in DATA if d["region"]=="cn")
intl_n = sum(1 for d in DATA if d["region"]=="intl")

# ---------- 排序（区内按状态→时间倒序） ----------
def sort_key(d):
    return (STATUS_RANK.get(d["status"], 9), -skey(d["date"]))
cn = sorted([d for d in DATA if d["region"]=="cn"], key=sort_key)
intl = sorted([d for d in DATA if d["region"]=="intl"], key=sort_key)
ordered = cn + intl

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
print("covered dims:", covered, "/16")
print("A/B/C/D/E:", grade_count)
print("five_star:", five_star)
print("cn:", cn_n, "intl:", intl_n)
print("top5:", [d["title"][:24] for d in top5])
from collections import Counter
for rg in ("cn","intl"):
    c=Counter(d["category"] for d in DATA if d["region"]==rg)
    print(rg, dict(c), "total", sum(c.values()))
print("status:", dict(Counter(d["status"] for d in DATA)))
