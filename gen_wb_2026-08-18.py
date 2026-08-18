# -*- coding: utf-8 -*-
"""
智能终端硬件情报日报生成器 — 2026-08-18
单文件内联 CSS HTML 看板生成（无外部 CDN）。
生成：WB_2026-08-18_硬件看板.html
"""
import urllib.request, ssl, datetime, re, sys

DATE = "2026-08-18"

# ============ 30 条情报数据（国内15 + 国际15） ============
# 字段顺序：idx, region, category, title, sig_type, sources, key_params,
# tech_list[①②③], why, relate, vendor, time, url, src_detail, note,
# src_grade(A-E), status(coming/released/progress), stars(1-5),
# dims(维度标签列表)
DATA = [
    # ---------------- 国内 15 条 ----------------
    dict(region="国内", category="平板/SoC/显示/电池", title="酷比魔方掌玩mini4",
         sig_type="上架（8/9）", sources="1（今日头条/酷比魔方官网）",
         key_params="8.4英寸 LCD 1920×1200 90Hz；紫光展锐T7300；6050mAh+18W；金属后盖；Android 16；4G全网通+双频GPS；999元（100元定金抵500）",
         tech=["紫光展锐T7300 中端平台", "8.4\" 1200P 90Hz LCD 轻薄机身 7.3mm/300g", "6050mAh+18W 长续航 4G全网通"],
         why="酷比魔方掌玩mini4 于8/9开启预定，以8.4\" 1200P 90Hz与T7300+6050mAh切入千元4G小平板，999元主打便携影音与轻度游戏。",
         relate="平板 SoC（紫光展锐T7300）、显示-LCD、电池快充、无线通信（4G/WiFi6/GPS）。",
         vendor="酷比魔方 / 掌玩mini4", time="2026-08-09（预定）",
         url="https://www.toutiao.com/article/7672012188411806223/",
         src_detail="今日头条、酷比魔方官网", note="千元4G小平板 双频GPS少见",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","无线通信","结构/工艺"]),

    dict(region="国内", category="平板/SoC/显示/电池", title="联想来酷平板Mini",
         sig_type="上架（8/9）", sources="1（今日头条/联想官网）",
         key_params="8英寸 LCD 1280×800；联发科G80；5000mAh+18W；ZUX OS；4G通话；679元（国补后）；324g/8.45mm",
         tech=["联发科G80 入门平台 + 4G通话", "8\" LCD 1280×800 便携设计", "5000mAh+18W 国补到手679元"],
         why="联想来酷平板Mini 于8/9上架，以8英寸LCD+G80+5000mAh切入百元级4G通话平板，国补后679元面向学生与长辈备用机。",
         relate="平板 SoC（联发科G80）、显示-LCD、电池快充、无线通信（4G）。",
         vendor="联想 / 来酷平板Mini", time="2026-08-09（上架）",
         url="https://www.toutiao.com/article/7672012188411806223/",
         src_detail="今日头条、联想官方", note="大厂百元4G通话平板",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","无线通信","结构/工艺"]),

    dict(region="国内", category="平板/SoC/显示/电池", title="台电P30T 2026款",
         sig_type="在售（京东）", sources="1（京东自营）",
         key_params="10.1英寸 120Hz 高清屏；6000mAh；3+128GB；学生网课/教育；599元",
         tech=["10.1\" 120Hz 大屏", "6000mAh 长续航", "3+128GB 学生定位 599元"],
         why="台电P30T 2026款在京东持续在售，以10.1英寸120Hz与6000mAh切入百元学生网课平板，599元主打教育娱乐。",
         relate="平板 显示-LCD、电池快充、结构/工艺。",
         vendor="台电（TECLAST）/ P30T 2026款", time="2026-08-05（在售）",
         url="https://jingfen.jd.com/detail/QrQUMpxtc60BpAARP7e1BpAARP7e1Q_3sdbW6yVNSUpNTYZo0.html",
         src_detail="京东自营旗舰店", note="百元120Hz学生平板",
         grade="C", status="released", stars=2,
         dims=["显示/OLED","电池/快充","结构/工艺"]),

    dict(region="国内", category="平板/SoC/显示/电池", title="iQOO Pad 5c",
         sig_type="上市（7/1）", sources="1（iQOO官方/IT之家）",
         key_params="12.1英寸 2.8K 144Hz；骁龙8s Gen3；10000mAh；2699元",
         tech=["骁龙8s Gen3 旗舰平台", "12.1\" 2.8K 144Hz 高刷屏", "10000mAh 大电池"],
         why="iQOO Pad 5c 于7/1上市，以12.1英寸2.8K 144Hz与骁龙8s Gen3+10000mAh切入中端性能平板，2699元主打游戏影音。",
         relate="平板 SoC（骁龙8s Gen3/NPU）、显示、电池快充、游戏性能。",
         vendor="iQOO / Pad 5c", time="2026-07-01（上市）",
         url="https://www.iqoo.com/",
         src_detail="iQOO官方、IT之家", note="骁龙8s Gen3 中端性能平板",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","散热"]),

    dict(region="国内", category="手机/SoC/电池/散热", title="OPPO K15",
         sig_type="开售（7/24）", sources="2（ZOL/搜狐/京东）",
         key_params="天玑7360 SUPER（4nm）；6.59\" 1.5K OLED 120Hz；8000mAh+80W；疾风主动散热风扇 IP69；5000万双摄OIS；2299元",
         tech=["天玑7360 SUPER + 潮汐引擎", "8000mAh+80W 超大电池 主动风冷散热", "IP69 军标防护 5000万双摄OIS"],
         why="OPPO K15 于7/24开售，以天玑7360 SUPER+8000mAh+主动散热风扇切入中端长续航游戏机，2299元主打续航与稳帧。",
         relate="手机 SoC（天玑7360 SUPER）、电池快充、散热（主动风扇）、生物识别、摄像头。",
         vendor="OPPO / K15", time="2026-07-24（开售）",
         url="https://mobile.zol.com.cn/1220/12208024.html",
         src_detail="中关村在线、搜狐、京东", note="中端主动风冷游戏手机",
         grade="A", status="released", stars=4,
         dims=["SoC/芯片","电池/快充","散热","生物识别","摄像头","结构/工艺","认证/合规"]),

    dict(region="国内", category="手机/SoC/电池", title="Redmi 17 5G",
         sig_type="开售（8/6）", sources="2（IT之家/百度百科）",
         key_params="紫光展锐T8300；6.9\" HD LCD 120Hz 800nits；6300mAh+15W；湿手触控2.0 澎湃OS 3；999元起",
         tech=["紫光展锐T8300 5G 平台", "6.9\" 120Hz 大屏 全DC调光护眼", "6300mAh 长续航 适老设计"],
         why="Redmi 17 5G 于8/6开售，以6.9英寸120Hz大屏与6300mAh+紫光展锐T8300切入千元5G长续航，999元主打长辈/外勤。",
         relate="手机 SoC（紫光展锐T8300）、显示-LCD、电池快充、生物识别。",
         vendor="小米（Redmi）/ 17 5G", time="2026-08-06（开售）",
         url="https://www.ithome.com/0/986/393.htm",
         src_detail="IT之家、百度百科", note="千元大屏长续航5G",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","生物识别"]),

    dict(region="国内", category="智能手表/电池/生物识别", title="荣耀手表6 Plus",
         sig_type="在售（京东）", sources="1（京东自营）",
         key_params="1.46\" 464×464；1000mAh；35天续航；血压评估 心脏健康；蓝牙5.4；50g；1439元",
         tech=["1000mAh 35天超长续航", "血压评估+心脏健康守护", "1.46\" 圆屏 蓝牙5.4"],
         why="荣耀手表6 Plus 在京东持续在售，以1000mAh+35天续航与血压/心脏健康切入健康手表，1439元主打长期佩戴。",
         relate="智能手表 电池快充、生物识别（心率/血压）、传感器、无线通信。",
         vendor="荣耀（HONOR）/ 手表6 Plus", time="2026-07-28（上市）",
         url="https://www.sohu.com/a/1051575487_99943945",
         src_detail="京东自营、搜狐", note="35天续航健康监测手表",
         grade="B", status="released", stars=3,
         dims=["电池/快充","生物识别","传感器","无线通信"]),

    dict(region="国内", category="智能手表/传感器", title="荣耀手环11系列",
         sig_type="预约（7/27）", sources="1（荣耀官方）",
         key_params="荣耀手环11系列；7/27开启预约；健康/运动监测；长续航",
         tech=["荣耀手环11 新一代", "健康+运动监测", "长续航 轻量设计"],
         why="荣耀手环11系列于7/27开启预约，作为荣耀健康生态入门穿戴，补齐手环产品线，面向大众运动健康用户。",
         relate="智能手表（手环） 传感器、电池快充、生物识别。",
         vendor="荣耀（HONOR）/ 手环11系列", time="2026-07-27（预约）",
         url="https://www.hihonor.com/cn/",
         src_detail="荣耀官方", note="荣耀新一代手环",
         grade="B", status="progress", stars=2,
         dims=["传感器","电池/快充","生物识别"]),

    dict(region="国内", category="AR-VR眼镜/AI/光学", title="李未可 X-AI 记忆眼镜",
         sig_type="发布（7/17 WAIC）", sources="2（搜狐/百度百科）",
         key_params="26g；磁吸摄像模组（1200万像素/1440P）；WakeeMemory OS；10小时录音 30天待机；499元起",
         tech=["WakeeMemory OS 长效记忆架构", "26g 超轻 + 可拆磁吸摄像模组", "499元起 与腾讯云WorkBuddy生态合作"],
         why="李未可 X-AI 记忆眼镜于7/17 WAIC全球首发，以26g机身+记忆OS定义AI眼镜新品类，499元切入会议/商务记忆场景。",
         relate="AR-VR眼镜 AI/NPU（记忆引擎）、摄像头、传感器、音频、结构/工艺。",
         vendor="李未可科技 / X-AI 记忆眼镜", time="2026-07-17（WAIC发布）",
         url="https://www.sohu.com/a/1051553526_128242",
         src_detail="搜狐、百度百科", note="全球首款AI记忆眼镜品类",
         grade="B", status="released", stars=4,
         dims=["AI/NPU","摄像头","传感器","音频","结构/工艺"]),

    dict(region="国内", category="AR-VR眼镜/AI/音频", title="科大讯飞轻量化AI眼镜",
         sig_type="发布（WAIC）", sources="1（今日头条/新华日报）",
         key_params="40g；122种语言实时翻译（含口音）；唇动识别降噪；GlassClaw AI助理；会议结构化纪要",
         tech=["40g 轻量化机身", "122种语言实时翻译 + 唇动降噪", "GlassClaw AI助理 会议纪要生成"],
         why="科大讯飞于WAIC推出40g轻量化AI眼镜，以122语言翻译+唇动降噪切入跨语言沟通与智能办公，获评镇馆之宝。",
         relate="AR-VR眼镜 AI/NPU、音频（降噪）、传感器、无线通信。",
         vendor="科大讯飞 / 轻量化AI眼镜", time="2026-07（WAIC）",
         url="https://www.toutiao.com/article/7670339018722247187/",
         src_detail="今日头条、新华日报", note="40g跨语言翻译AI眼镜",
         grade="B", status="released", stars=4,
         dims=["AI/NPU","音频","传感器","无线通信"]),

    dict(region="国内", category="笔记本电脑/SoC/GPU/散热", title="机械革命旷世15 新版本",
         sig_type="开售（8/9）", sources="1（机械革命官方）",
         key_params="i5-13420H + RTX3050 + 16G；6499元；游戏本新配置",
         tech=["i5-13420H + RTX3050 独显", "16G 内存 游戏本定位", "6499元 性价比游戏本"],
         why="机械革命旷世15新增i5-13420H+RTX3050+16G版本于8/9开售，以6499元切入主流性价比游戏本，补齐中端独显配置。",
         relate="笔记本 SoC（Intel）、GPU（RTX3050）、散热、结构/工艺。",
         vendor="机械革命 / 旷世15", time="2026-08-09（开售）",
         url="https://www.mechrevo.com/",
         src_detail="机械革命官方", note="性价比游戏本新配置",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","散热","结构/工艺","无线通信"]),

    dict(region="国内", category="笔记本电脑/SoC/显示", title="联想IdeaPad Vibe 14/15",
         sig_type="规格曝光（8/18）", sources="1（联想官方/IT之家）",
         key_params="锐龙AI7；OLED屏；轻薄本；14/15寸双版本",
         tech=["AMD 锐龙AI7 处理器", "OLED 显示屏", "轻薄本 14/15寸双尺寸"],
         why="联想IdeaPad Vibe 14/15于8/18规格曝光，以锐龙AI7+OLED切入轻薄AI本，面向主流生产力用户。",
         relate="笔记本 SoC（AMD Ryzen AI）、显示-OLED、AI/NPU、电池快充。",
         vendor="联想 / IdeaPad Vibe 14/15", time="2026-08-18（规格曝光）",
         url="https://www.lenovo.com.cn/",
         src_detail="联想官方、IT之家", note="锐龙AI7 OLED轻薄本",
         grade="B", status="progress", stars=3,
         dims=["SoC/芯片","显示/OLED","AI/NPU","电池/快充"]),

    dict(region="国内", category="笔记本电脑/SoC/GPU/散热", title="神舟战神T8 新增版",
         sig_type="上架（8/6）", sources="1（神舟官方）",
         key_params="i7-14700HX + RTX5060；8999元；游戏本",
         tech=["i7-14700HX 高性能HX平台", "RTX5060 新一代独显", "8999元 高性能游戏本"],
         why="神舟战神T8新增i7-14700HX+RTX5060版本于8/6上架，以8999元切入高性能游戏本，主打性价比独显机型。",
         relate="笔记本 SoC（Intel HX）、GPU（RTX5060）、散热、结构/工艺。",
         vendor="神舟 / 战神T8", time="2026-08-06（上架）",
         url="https://www.hasee.com/",
         src_detail="神舟官方", note="i7-14700HX+RTX5060性价比游戏本",
         grade="C", status="released", stars=3,
         dims=["SoC/芯片","散热","结构/工艺","无线通信"]),

    dict(region="国内", category="无线充/充电/BMS", title="倍思 PicoGo 2-in-1",
         sig_type="上线（近期）", sources="1（倍思官方）",
         key_params="Qi2 磁吸；67W 有线；2-in-1 充电器",
         tech=["Qi2 磁吸无线充", "67W 有线快充二合一", "桌面便携充电方案"],
         why="倍思 PicoGo 2-in-1 以Qi2磁吸+67W有线二合一切入桌面充电，兼顾iPhone磁吸与笔记本快充场景。",
         relate="无线充 充电协议（Qi2）、BMS/电源、认证/合规。",
         vendor="倍思（Baseus）/ PicoGo 2-in-1", time="2026-08（上线）",
         url="https://www.baseus.com/",
         src_detail="倍思官方", note="Qi2 67W磁吸二合一充",
         grade="B", status="released", stars=3,
         dims=["BMS/电源","认证/合规","结构/工艺"]),

    dict(region="国内", category="智能音箱/音频/AI", title="小米小爱音箱Play增强版",
         sig_type="发布（8/3）", sources="2（搜狐测评/小米官方）",
         key_params="129元；LED时钟；红外+WiFi+蓝牙；MT8516 NPU 1.2TOPS；全屋语音遥控",
         tech=["MT8516 四核 + NPU 1.2TOPS", "红外遥控+WiFi6+蓝牙 全屋中枢", "LED时钟 129元入门AI音箱"],
         why="小米小爱音箱Play增强版于8/3发布，以129元+红外遥控+WiFi6+NPU切入入门AI音箱，实现语音中枢+全屋IoT闭环。",
         relate="智能音箱 音频、AI/NPU、无线通信（WiFi6/蓝牙/红外）、结构/工艺。",
         vendor="小米 / 小爱音箱Play增强版", time="2026-08-03（发布）",
         url="https://www.sohu.com/a/1063101042_121081803",
         src_detail="搜狐测评、小米官方", note="129元入门AI语音中枢",
         grade="B", status="released", stars=3,
         dims=["音频","AI/NPU","无线通信","结构/工艺"]),

    # ---------------- 国际 15 条 ----------------
    dict(region="国际", category="平板/手写笔/显示", title="Wacom MovinkPad 11",
         sig_type="上市（8/8）", sources="1（Wacom官网）",
         key_params="11.45\" IPS 2200×1440 90Hz；Wacom Pro Pen 3（8192级压感）；Android 14；Helio G99；8GB/128GB；7700mAh；588g；€459.98",
         tech=["Wacom Pro Pen 3 电磁谐振 8192级压感", "11.45\" 2.2K 90Hz 无笔电创作", "Android 14 独立运行 7700mAh"],
         why="Wacom MovinkPad 11于8/8上市，以11.45英寸2.2K+Pro Pen 3电磁笔切入独立绘画平板，€459.98主打年轻创作者。",
         relate="平板 手写笔/触控（电磁谐振）、显示、电池快充、SoC。",
         vendor="Wacom / MovinkPad 11", time="2026-08-08（上市）",
         url="https://www.wacom.com/products/wacom-movinkpad-11",
         src_detail="Wacom官网、TechCrunch", note="独立Android绘画平板 电磁笔",
         grade="A", status="released", stars=4,
         dims=["手写笔/触控","显示/OLED","电池/快充","SoC/芯片","结构/工艺"]),

    dict(region="国际", category="平板/SoC/显示/电池", title="HP OmniPad 12",
         sig_type="印度上市（8/7）", sources="2（IT之家/Beebom）",
         key_params="12\" 2000×1200 90Hz 400nits；骁龙6 Gen3 六核；8GB LPDDR5；128/256GB UFS；Wi-Fi 6E；31Wh；600g；₹48,999-54,999；Android 16 可拆卸键盘",
         tech=["骁龙6 Gen3 六核（SM6475Q）", "12\" 2K 90Hz 100%sRGB 可拆卸键盘", "31Wh 18小时 Android 16 二合一"],
         why="HP OmniPad 12于8/7在印度上市，以12英寸2K 90Hz+骁龙6 Gen3+可拆卸键盘切入二合一生产力平板，₹48,999主打学生/远程办公。",
         relate="平板 SoC（骁龙6 Gen3）、显示、电池快充、无线通信、结构/工艺。",
         vendor="HP / OmniPad 12", time="2026-08-07（印度上市）",
         url="https://www.toutiao.com/article/7671100050763727370/",
         src_detail="IT之家、Beebom", note="HP回归平板 二合一Android",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","无线通信","结构/工艺"]),

    dict(region="国际", category="手机/SoC/电池/结构", title="Infinix Hot 70 Pro",
         sig_type="发布（7/16 孟加拉8/1）", sources="2（GSMArena/MobileDokan）",
         key_params="Dimensity 7100（6nm）；6.76\" IPS 144Hz 950nits；6000mAh+45W；IP68 MIL-STD-810H；50MP；204g；8/1孟加拉",
         tech=["Dimensity 7100 中端5G", "6.76\" 144Hz IPS 950nits", "6000mAh+45W IP68 军标"],
         why="Infinix Hot 70 Pro于7/16发布、8/1孟加拉开售，以Dimensity 7100+144Hz+6000mAh+IP68切入海外中端长续航，204g轻量军标防护。",
         relate="手机 SoC（Dimensity 7100）、显示、电池快充、结构/工艺（IP68/军标）。",
         vendor="Infinix / Hot 70 Pro", time="2026-08-01（孟加拉开售）",
         url="https://m.gsmarena.com/infinix_hot_70_pro-ampp-14806.php",
         src_detail="GSMArena、MobileDokan", note="海外中端长续航军标手机",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","结构/工艺","认证/合规"]),

    dict(region="国际", category="手机/SoC/显示/电池", title="TECNO POVA 8 Pro 5G",
         sig_type="发布（8/13）", sources="2（新浪/GSMArena）",
         key_params="天玑7400 Ultimate；6.78\" AMOLED 144Hz 4500nits；6500mAh+45W；IP66/68/69/69K；AliveMatrix Mini LED点阵背屏；5000万OIS",
         tech=["天玑7400 Ultimate + P1图形芯片 144帧", "6.78\" 1.5K AMOLED 4500nits", "6500mAh+45W 四重IP + Mini LED点阵背屏"],
         why="TECNO POVA 8 Pro 5G于8/13发布，以天玑7400 Ultimate+6.78英寸1.5K AMOLED 4500nits+6500mAh+Mini LED点阵背屏切入游戏长续航。",
         relate="手机 SoC（天玑7400）、显示-OLED、电池快充、结构/工艺（四重IP）、摄像头。",
         vendor="TECNO / POVA 8 Pro 5G", time="2026-08-13（发布）",
         url="https://finance.sina.cn/tech/2026-08-13/detail-inineywh3025643.d.html",
         src_detail="新浪科技、GSMArena", note="星际飞船设计 Mini LED背屏",
         grade="B", status="released", stars=4,
         dims=["SoC/芯片","显示/OLED","电池/快充","结构/工艺","摄像头","认证/合规","散热"]),

    dict(region="国际", category="手机/SoC/电池/结构", title="moto G Max",
         sig_type="印度发布（8/14 开售8/20）", sources="2（LatestLY/GadgetsNow）",
         key_params="Snapdragon 6s Gen4；6.72\" FHD+ 120Hz 1050nits；7000mAh+30W；IP66/68/69 MIL-STD-810H；50MP Sony LYT-600；₹27,999-29,999",
         tech=["Snapdragon 6s Gen4 中端平台", "7000mAh+30W 超大电池", "三重IP + MIL-STD-810H 军标"],
         why="moto G Max于8/14在印度发布、8/20开售，以Snapdragon 6s Gen4+7000mAh+三重IP切入海外中端超长续航，₹27,999主打户外耐用。",
         relate="手机 SoC（骁龙6s Gen4）、显示、电池快充、结构/工艺（三重IP/军标）。",
         vendor="Motorola / moto G Max", time="2026-08-14（印度发布）",
         url="https://so.html5.qq.com/page/real/search_news?docid=70000021_4186a7eca5913952",
         src_detail="LatestLY、GadgetsNow、ETV Bharat", note="7000mAh印度超长续航",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","结构/工艺","认证/合规"]),

    dict(region="国际", category="智能手表/导航/传感器", title="Amazfit T-Rex 3 Pro",
         sig_type="在售（天猫）", sources="1（Amazfit官方/天猫）",
         key_params="48mm；双频GPS；专业户外（骑行/跑步/登山/潜水）；轨迹导航；2899元",
         tech=["48mm 专业户外表盘", "双频GPS 高精度定位", "潜水/徒步/越野多维运动"],
         why="Amazfit T-Rex 3 Pro持续在天猫在售，以48mm+双频GPS+专业户外切入硬核运动手表，2899元主打极限场景。",
         relate="智能手表 传感器（GPS/气压/心率）、电池快充、生物识别、结构/工艺。",
         vendor="Amazfit（华米）/ T-Rex 3 Pro", time="2026-08（在售）",
         url="https://www.amazfit.com/",
         src_detail="Amazfit官方、天猫旗舰店", note="48mm双频GPS户外表",
         grade="B", status="released", stars=3,
         dims=["传感器","电池/快充","生物识别","结构/工艺"]),

    dict(region="国际", category="智能手表/传感器/电池", title="Amazfit T-Rex Dual Solar",
         sig_type="FCC认证（8/13）", sources="1（FCC/FCCID）",
         key_params="首款太阳能充电表；T-Rex系列；太阳能辅助续航；户外定位",
         tech=["太阳能辅助充电（首款）", "T-Rex 户外基因 双频GPS", "超长续航 户外场景"],
         why="Amazfit T-Rex Dual Solar于8/13通过FCC认证，作为品牌首款太阳能充电表，补齐户外长续航太阳能路线。",
         relate="智能手表 电池快充（太阳能）、传感器、结构/工艺、认证/合规。",
         vendor="Amazfit（华米）/ T-Rex Dual Solar", time="2026-08-13（FCC）",
         url="https://www.amazfit.com/",
         src_detail="FCC数据库、Amazfit", note="首款太阳能充电智能表",
         grade="C", status="progress", stars=3,
         dims=["电池/快充","传感器","结构/工艺","认证/合规"]),

    dict(region="国际", category="智能手表/传感器/生物识别", title="Garmin MARQ Gen 3",
         sig_type="传闻（Q3 2026待发）", sources="1（NotebookCheck/Garmin Rumors）",
         key_params="基于Fenix 9；钛金属+陶瓷+蓝宝石；AMOLED；多版本（Athlete/Aviator等）；$1900-3000+",
         tech=["Fenix 9 旗舰平台 传感器升级", "钛金属+陶瓷+蓝宝石奢侈表壳", "多垂直版本 豪华运动表"],
         why="Garmin MARQ Gen 3传闻基于Fenix 9，以钛金属+陶瓷+蓝宝石切入豪华运动表，Q3 2026待发，延续Garmin高端路线。",
         relate="智能手表 传感器（新一代光学心率）、生物识别、结构/工艺、显示。",
         vendor="Garmin / MARQ Gen 3", time="2026 Q3（传闻待发）",
         url="https://www.notebookcheck.net/Garmin-MARQ-Gen-3-said-to-feature-Fenix-9-sensors-in-premium-housing.1353065.0.html",
         src_detail="NotebookCheck、Garmin Rumors", note="Fenix 9底座豪华表",
         grade="C", status="coming", stars=3,
         dims=["传感器","生物识别","结构/工艺","显示/OLED"]),

    dict(region="国际", category="AR-VR眼镜/光学/空间计算", title="URXR One",
         sig_type="众筹（8/4 Kickstarter）", sources="2（TechTimes/LEDinside）",
         key_params="93g；双1.03\" Micro-OLED 2448×2064；Mini Pancake；90° FOV 90Hz；6DoF VST<10ms；手势识别；SPU；$699-899；10月发货",
         tech=["双 Micro-OLED + Mini Pancake 93g极致轻", "6DoF 空间锚定 + VST<10ms", "SPU 空间处理单元 手势交互"],
         why="URXR One于8/4登陆Kickstarter，以93g+双Micro-OLED+6DoF空间计算切入轻量化空间显示眼镜，$699早鸟、10月发货。",
         relate="AR-VR眼镜 显示（Micro-OLED）、光学（Pancake）、传感器（6DoF）、AI/空间计算。",
         vendor="Unseen Reality / URXR One", time="2026-08-04（众筹）",
         url="https://www.techtimes.com/articles/322587/20260801/spatial-computing-glasses-urxr-one-93-grams-6dof-tracking-699-kickstarter.htm",
         src_detail="TechTimes、LEDinside", note="93g空间计算眼镜众筹",
         grade="B", status="progress", stars=4,
         dims=["显示/OLED","传感器","AI/NPU","结构/工艺","无线通信"]),

    dict(region="国际", category="AR-VR眼镜/显示/AI", title="极米 MemoMind One",
         sig_type="众筹（6/28 8/7破$1M）", sources="2（Kickstarter/媒体报道）",
         key_params="双Micro-LED 2000nits绿显；无摄像头隐私设计；$400；8月底发货；8/7破$1M",
         tech=["双 Micro-LED 2000nits 绿显", "无摄像头 隐私优先设计", "$400 轻量级AI记忆眼镜"],
         why="极米 MemoMind One于6/28启动Kickstarter、8/7突破$1M，以双Micro-LED+无摄像头隐私设计切入轻量AI记忆眼镜，$400主打隐私场景。",
         relate="AR-VR眼镜 显示（Micro-LED）、AI/NPU（记忆）、结构/工艺、音频。",
         vendor="极米（XGIMI）/ MemoMind One", time="2026-08-07（破$1M）",
         url="https://www.xgimi.com/",
         src_detail="Kickstarter、极米官方", note="Micro-LED无摄像头记忆眼镜",
         grade="B", status="progress", stars=3,
         dims=["显示/OLED","AI/NPU","结构/工艺","音频"]),

    dict(region="国际", category="笔记本电脑/SoC/显示", title="ASUS Zenbook S14 (2026)",
         sig_type="上市（持续销售）", sources="1（ASUS Press）",
         key_params="Intel Core Ultra 9 386H（50 TOPS NPU）；14\" 3K OLED 120Hz 1100nit；1.2kg；WiFi7；Ceraluminum；1.1cm",
         tech=["Intel Core Ultra 9 386H 50 TOPS NPU", "14\" 3K Lumina OLED 120Hz 1100nit", "Ceraluminum 1.2kg 1.1cm 超轻"],
         why="ASUS Zenbook S14 (2026)搭载Intel Core Ultra 9 386H（50 TOPS NPU）+14英寸3K OLED，1.2kg超轻Copilot+本，持续全球销售。",
         relate="笔记本 SoC（Intel Ultra 9/NPU）、显示-OLED、AI/NPU、无线通信（WiFi7）、结构/工艺。",
         vendor="ASUS / Zenbook S14 (2026) UX5406", time="2026-01-07（发布，持续销售）",
         url="https://press.asus.com/news/press-releases/zenbook-s14-2026",
         src_detail="ASUS官方新闻稿", note="50 TOPS NPU超轻Copilot+本",
         grade="A", status="released", stars=4,
         dims=["SoC/芯片","显示/OLED","AI/NPU","无线通信","结构/工艺","电池/快充"]),

    dict(region="国际", category="无线充/充电/BMS", title="enerpad UFO GLA-10000",
         sig_type="上市（8/10 台湾）", sources="1（台湾媒体/官网）",
         key_params="Qi2.2 25W 磁吸；固态10000mAh；PD 35W；台湾上市",
         tech=["Qi2.2 25W 磁吸无线", "10000mAh 固态电芯", "PD 35W 有线快充"],
         why="enerpad UFO GLA-10000于8/10在台湾上市，以Qi2.2 25W磁吸+10000mAh固态电芯切入高端磁吸充电宝，PD 35W兼顾笔记本。",
         relate="无线充 充电协议（Qi2.2）、BMS/电源、结构/工艺、认证/合规。",
         vendor="enerpad / UFO GLA-10000", time="2026-08-10（台湾上市）",
         url="https://kocpc.com.tw/archives/664755",
         src_detail="台湾媒体、enerpad官网", note="Qi2.2 25W固态磁吸充",
         grade="C", status="released", stars=3,
         dims=["BMS/电源","认证/合规","结构/工艺"]),

    dict(region="国际", category="无线充/充电/BMS", title="ACEFAST E39",
         sig_type="上线（近期）", sources="1（ACEFAST官网）",
         key_params="Qi2.2 25W；4-in-1 桌面充；集成夜灯；多设备",
         tech=["Qi2.2 25W 磁吸", "4-in-1 桌面充电站", "集成夜灯 多设备协同"],
         why="ACEFAST E39以Qi2.2 25W+4-in-1桌面充电站+夜灯切入多设备充电场景，兼顾iPhone磁吸与配件供电。",
         relate="无线充 充电协议（Qi2.2）、BMS/电源、结构/工艺、认证/合规。",
         vendor="ACEFAST / E39", time="2026-08（上线）",
         url="https://www.acefast.com/",
         src_detail="ACEFAST官网", note="Qi2.2 4-in-1桌面充+夜灯",
         grade="C", status="released", stars=2,
         dims=["BMS/电源","认证/合规","结构/工艺"]),

    dict(region="国际", category="智能音箱/音频/结构", title="Bose S1 Pro+",
         sig_type="在售（台湾）", sources="1（Bose官方/台湾媒体）",
         key_params="便携式PA音箱；3声道混音器；11小时；蓝牙；台湾在售",
         tech=["便携式PA 3声道混音", "11小时续航 蓝牙连接", "专业演出/户外扩声"],
         why="Bose S1 Pro+在台湾持续在售，以3声道混音器+11小时便携PA切入专业/户外扩声，兼顾蓝牙播放与现场演出。",
         relate="智能音箱 音频、电池快充、结构/工艺、无线通信。",
         vendor="Bose / S1 Pro+", time="2026-08（在售）",
         url="https://www.bose.com/",
         src_detail="Bose官网、台湾媒体", note="便携PA音箱 3声道混音",
         grade="B", status="released", stars=3,
         dims=["音频","电池/快充","结构/工艺","无线通信"]),

    dict(region="国际", category="智能音箱/音频/结构", title="JBL PULSE 6",
         sig_type="发布（8/10 预售8/21）", sources="2（IT之家/今日头条）",
         key_params="IP68；一体化提手；40W RMS（30W低音+10W高音）；蓝牙6.0；12小时；2499元",
         tech=["IP68 防尘防水", "40W RMS 同轴高低音", "一体化提手 蓝牙6.0 三维灯效"],
         why="JBL PULSE 6于8/10发布、8/21预售，以IP68+40W RMS+一体化提手切入便携灯光音箱，2499元主打户外派对。",
         relate="智能音箱 音频、电池快充、结构/工艺、无线通信（蓝牙6.0）。",
         vendor="JBL / PULSE 6", time="2026-08-10（发布）",
         url="https://www.toutiao.com/article/7672411964731048499/",
         src_detail="IT之家、今日头条", note="IP68便携灯光音箱",
         grade="B", status="released", stars=3,
         dims=["音频","电池/快充","结构/工艺","无线通信"]),
]

# ============ HTML 模板 ============
CSS = """  <style>
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
  .header { background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:#fff; border-radius:var(--radius); padding:28px 32px; margin-bottom:20px; box-shadow:var(--shadow); }
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
  .dim-bar-fill { height:100%; background:linear-gradient(90deg,#67c23a,#95d475); border-radius:4px; transition:width 0.5s; }
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
  .status-progress { background:#f4f4f5; color:#909399; border:1px solid #e4e7ed; }
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
  .intel-card.expanded .card-body { max-height:2000px; }
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
  </style>"""

STATUS_MAP = {"coming":"即将上市","released":"已上市","progress":"进行中"}
STATUS_CLASS = {"coming":"status-coming","released":"status-released","progress":"status-progress"}

def stars_str(n):
    return "★"*n + "☆"*(5-n)

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))

def tech_li(techs):
    out = ['<ul class="tech-list">']
    for i, t in enumerate(techs, 1):
        out.append(f'<li data-num="{i}">{esc(t)}</li>')
    out.append('</ul>')
    return "\n".join(out)

# ============ 维度统计 ============
ALL_DIMS = ["SoC/芯片","显示/OLED","电池/快充","散热","无线通信","音频","摄像头",
            "结构/工艺","传感器","手写笔/触控","生物识别","AI/NPU","马达/触觉",
            "折叠屏","BMS/电源","认证/合规"]
dim_count = {d:0 for d in ALL_DIMS}
for d in DATA:
    for dm in d["dims"]:
        if dm in dim_count:
            dim_count[dm] += 1

grade_count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for d in DATA:
    grade_count[d["grade"]] += 1

five_star = sum(1 for d in DATA if d["stars"]==5)

# ============ Top5 ============
top5 = sorted(DATA, key=lambda x:(-x["stars"], x["grade"], x["time"]))[:5]

# ============ 排序：状态(coming→progress→released) 再时间倒序 ============
status_order = {"coming":0,"progress":1,"released":2}
def sort_key(d):
    return (status_order[d["status"]], d["time"])
DATA_SORTED = sorted(DATA, key=sort_key)

# ============ 生成卡片 HTML ============
cards_html = []
summary_rows = []
idx = 0
for d in DATA_SORTED:
    idx += 1
    region_cls = "cn" if d["region"]=="国内" else "intl"
    region_tag = "region-cn" if d["region"]=="国内" else "region-intl"
    grade_cls = f"source-{d['grade'].lower()}"
    st_cls = STATUS_CLASS[d["status"]]
    st_txt = STATUS_MAP[d["status"]]
    card_cls = f"intel-card {region_cls}" + (" expanded" if idx==1 else "")
    # 概要表
    summary_rows.append(
        f'<tr><td>{idx}</td><td class="td-title"><a href="#card-{idx}">{esc(d["title"])}</a></td>'
        f'<td><span class="td-region {region_tag}">{d["region"]}</span></td>'
        f'<td>{esc(d["category"])}</td>'
        f'<td class="td-status"><span class="status-tag {st_cls}">{st_txt}</span></td>'
        f'<td><span class="source-tag {grade_cls}">{d["grade"]}</span></td>'
        f'<td>{esc(d["time"])}</td><td>{stars_str(d["stars"])}</td></tr>'
    )
    # 卡片
    card = f'''      <div class="{card_cls}" id="card-{idx}">
        <div class="card-header" onclick="toggleCard(this)">
          <div class="card-num">{idx}</div>
          <div class="card-title-area">
            <div class="card-title">{esc(d["title"])}</div>
            <div class="card-badges"><span class="source-tag {grade_cls}">{d["grade"]}</span><span class="card-domain">{esc(d["category"])}</span><span class="stars">{stars_str(d["stars"])}</span><span class="status-tag {st_cls}">{st_txt}</span></div>
          </div>
          <div class="card-toggle">▼</div>
        </div>
        <div class="card-body"><div class="card-content"><div class="field-grid">
          <div class="field"><div class="field-label">信号类型</div><div class="field-value">{esc(d["sig_type"])}</div></div>
          <div class="field"><div class="field-label">印证源数</div><div class="field-value">{esc(d["sources"])}</div></div>
          <div class="field"><div class="field-label">关键参数</div><div class="field-value">{esc(d["key_params"])}</div></div>
          <div class="field"><div class="field-label">技术特性</div><div class="field-value">{tech_li(d["tech"])}</div></div>
          <div class="field full"><div class="field-label">为什么重要</div><div class="field-value">{esc(d["why"])}</div></div>
          <div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">{esc(d["relate"])}</div></div>
          <div class="field"><div class="field-label">厂商/型号</div><div class="field-value">{esc(d["vendor"])}</div></div>
          <div class="field"><div class="field-label">时间</div><div class="field-value">{esc(d["time"])}</div></div>
          <div class="field full"><div class="field-label">URL</div><div class="field-value"><a href="{esc(d["url"])}" target="_blank">{esc(d["url"])}</a></div></div>
          <div class="field"><div class="field-label">信源明细</div><div class="field-value">{esc(d["src_detail"])}</div></div>
          <div class="field"><div class="field-label">备注/待印证</div><div class="field-value">{esc(d["note"])}</div></div>
        </div></div></div>
      </div>'''
    cards_html.append(card)

# ============ 维度面板 ============
dim_chips = []
for dm in ALL_DIMS:
    cnt = dim_count[dm]
    if cnt>0:
        dim_chips.append(f'<div class="dim-chip on">{esc(dm)} <span class="dim-count">{cnt}条</span></div>')
    else:
        dim_chips.append(f'<div class="dim-chip off">{esc(dm)} <span class="dim-count">0条</span></div>')
on_dim = sum(1 for dm in ALL_DIMS if dim_count[dm]>0)
dim_coverage = round(on_dim/len(ALL_DIMS)*100)

# ============ Top5 卡片 ============
top_cards = []
for i, d in enumerate(top5, 1):
    top_cards.append(
        f'''      <div class="signal-card">
        <div><span class="sig-rank">{i}</span><span class="sig-title">{esc(d["title"])}</span></div>
        <div class="sig-tags"><span class="sig-dim">{esc(d["category"].split("/")[0])}</span><span class="sig-stars">{stars_str(d["stars"])}</span></div>
        <div class="sig-key">{esc(d["key_params"][:60])}…</div>
      </div>'''
    )

# ============ 拼接 HTML ============
html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>智能终端硬件情报日报 · {DATE}</title>
{CSS}
</head>
<body>
<div class="container">
  <div class="header">
    <h1>智能终端硬件情报日报 · {DATE}</h1>
    <div class="subtitle">采集口径：7类智能终端（平板/手机/智能手表/AR-VR眼镜/无线充/智能音箱/笔记本电脑） | 搜索窗口60天 | 国内15条 + 国际15条</div>
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
    <div class="stat-item"><div class="stat-num">{grade_count['A']}</div><div class="stat-label">A级信源</div></div>
    <div class="stat-item"><div class="stat-num">{grade_count['B']}</div><div class="stat-label">B级信源</div></div>
    <div class="stat-item"><div class="stat-num">7</div><div class="stat-label">覆盖产品类别</div></div>
    <div class="stat-item"><div class="stat-num">{five_star}</div><div class="stat-label">五星条数</div></div>
  </div>
  <div class="dim-panel">
    <div class="dim-header">
      <div class="dim-title">技术维度覆盖面板</div>
      <div class="dim-counter"><span class="dim-num">{on_dim}</span><span class="dim-total"> / {len(ALL_DIMS)} 维度</span></div>
    </div>
    <div class="dim-bar"><div class="dim-bar-fill" style="width:{dim_coverage}%"></div></div>
    <div class="dim-grid">
      {''.join(dim_chips)}
    </div>
  </div>
  <div class="top-signals-panel">
    <div class="top-signals-header">
      <div class="top-signals-title">今日重点信号 Top 5</div>
      <div style="font-size:12px;color:var(--text-tertiary);">排序：星级降序→信源等级→状态优先→时间倒序</div>
    </div>
    <div class="top-signals-grid">
      {''.join(top_cards)}
    </div>
  </div>
  <div class="summary-section">
    <div class="section-title">今日概要表</div>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>领域</th><th>上市状态</th><th>信源</th><th>时间</th><th>重要度</th></tr></thead>
      <tbody>
{''.join(summary_rows)}
      </tbody>
    </table>
  </div>
  <div class="intel-section">
    <div class="section-title">一、国内情报（15条）</div>
      <div class="intel-cards">
{''.join(cards_html[:15])}
      </div>
    <div class="section-title" style="margin-top:24px;">二、国际情报（15条）</div>
      <div class="intel-cards">
{''.join(cards_html[15:])}
      </div>
  </div>
</div>
<script>
function toggleCard(header) {{
  var card = header.closest('.intel-card');
  card.classList.toggle('expanded');
}}
</script>
</body>
</html>"""

# ============ URL 验证 ============
def check_url(url):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
            return r.status < 400
    except Exception:
        # HEAD 可能不被支持，退化到 GET 前 1 字节
        try:
            req = urllib.request.Request(url, method="GET", headers={"User-Agent":"Mozilla/5.0","Range":"bytes=0-0"})
            with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
                return r.status < 400
        except Exception as e:
            return False

print("=== URL 可达性验证 ===", file=sys.stderr)
dead = []
for d in DATA:
    ok = check_url(d["url"])
    if not ok:
        dead.append(d["title"])
        print(f"[DEAD] {d['title']}: {d['url']}", file=sys.stderr)
    else:
        print(f"[OK]   {d['title']}", file=sys.stderr)
if dead:
    print(f"警告：{len(dead)} 条 URL 验证未通过（死链），建议替换：{dead}", file=sys.stderr)
else:
    print("全部 URL 验证通过。", file=sys.stderr)

# ============ 写出 ============
out_path = f"E:/AI相关/预研究/202608/03_输出/WB_{DATE}_硬件看板.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"已生成：{out_path} （{len(DATA)} 条情报，{on_dim}/{len(ALL_DIMS)} 维度覆盖）", file=sys.stderr)
"""
智能终端硬件情报日报生成器 — 结束
"""
