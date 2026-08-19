# -*- coding: utf-8 -*-
"""
智能终端硬件情报日报生成器 — 2026-08-19
单文件内联 CSS HTML 看板生成（无外部 CDN）。
生成：WB_2026-08-19_硬件看板.html
"""
import urllib.request, ssl, datetime, re, sys

DATE = "2026-08-19"

# ============ 30 条情报数据（国内15 + 国际15） ============
# 字段顺序：idx, region, category, title, sig_type, sources, key_params,
# tech_list[①②③], why, relate, vendor, time, url, src_detail, note,
# src_grade(A-E), status(coming/released/progress), stars(1-5),
# dims(维度标签列表)
DATA = [
    # ---------------- 国内 15 条 ----------------
    dict(region="国内", category="平板/SoC/显示/电池", title="荣耀平板20 Pro",
         sig_type="配置公布（8/18）", sources="2（手机中国/荣耀官方）",
         key_params="12.1英寸 3K 165Hz；骁龙8s Gen4；10100mAh；MagicOS 10；Paperlike类纸屏；马来8/24发布",
         tech=["骁龙8s Gen4 旗舰平台", "12.1\" 3K 165Hz 类纸护眼屏", "10100mAh 大电池 + MagicOS 10"],
         why="荣耀平板20 Pro于8/18公布配置，以12.1英寸3K 165Hz与骁龙8s Gen4+10100mAh切入高端生产力平板，马来8/24发布对标国际版。",
         relate="平板 SoC（骁龙8s Gen4）、显示（3K类纸屏）、电池快充、手写笔/触控、结构/工艺。",
         vendor="荣耀（HONOR）/ 平板20 Pro", time="2026-08-18（配置公布）",
         url="https://www.hihonor.com/cn/",
         src_detail="手机中国、荣耀官方", note="荣耀高端平板 Pro 系列",
         grade="A", status="coming", stars=4,
         dims=["SoC/芯片","显示/OLED","电池/快充","手写笔/触控","结构/工艺"]),

    dict(region="国内", category="平板/SoC/显示/电池/通信", title="华为MatePad Mini",
         sig_type="全球发布（8/17）", sources="2（gadgets360/京东）",
         key_params="8.8英寸 OLED 2560×1600 120Hz；麒麟平台 HarmonyOS 5.1；5G独立通话+卫星短信；6400mAh+66W；3999元",
         tech=["8.8\" OLED 柔性屏 120Hz 1800nits", "麒麟芯 HarmonyOS 5.1 5G通话+卫星短信", "6400mAh+66W 旗舰小平板"],
         why="华为MatePad Mini于8/17全球发布，以8.8英寸OLED+5G独立通话+卫星短信切入旗舰通信小平板，补齐便携创作与户外应急场景。",
         relate="平板 SoC（麒麟）、显示-OLED、电池快充、无线通信（5G/卫星短信）、结构/工艺。",
         vendor="华为（HUAWEI）/ MatePad Mini", time="2026-08-17（全球发布）",
         url="https://consumer.huawei.com/cn/",
         src_detail="Gadgets360、京东", note="8.8寸通信小平板 卫星短信",
         grade="A", status="released", stars=4,
         dims=["SoC/芯片","显示/OLED","电池/快充","无线通信","结构/工艺","手写笔/触控"]),

    dict(region="国内", category="平板/SoC/显示/电池", title="荣耀平板GT2 Pro",
         sig_type="在售（京东）", sources="1（京东自营）",
         key_params="12.5英寸 165Hz 3K护眼电竞屏；满血骁龙8 Gen3；10100mAh；66W；2499元",
         tech=["满血骁龙8 Gen3 旗舰平台", "12.5\" 165Hz 3K 护眼电竞屏", "10100mAh+66W 66W快充"],
         why="荣耀平板GT2 Pro在京东持续在售，以12.5英寸3K 165Hz与满血骁龙8 Gen3+10100mAh切入高性能电竞/生产力平板，2499元主打性价比。",
         relate="平板 SoC（骁龙8 Gen3）、显示（3K高刷）、电池快充、散热、结构/工艺。",
         vendor="荣耀（HONOR）/ 平板GT2 Pro", time="2026-08（在售）",
         url="https://www.hihonor.com/cn/",
         src_detail="京东自营旗舰店", note="12.5寸3K电竞生产力平板",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","散热","结构/工艺","手写笔/触控"]),

    dict(region="国内", category="平板/显示/电池", title="真我平板 X",
         sig_type="上架（8/7 即将上市）", sources="1（ZOL/realme官方）",
         key_params="11英寸；realme UI 3.0 for Pad；1299-1599元；学生/轻办公定位",
         tech=["11\" 大屏 realme UI 3.0 for Pad", "1299-1599元 百元级平板", "轻办公/网课/影音定位"],
         why="真我平板 X于8/7上架，以11英寸与realme UI 3.0 for Pad切入千元级平板，1299元起面向学生与轻办公用户。",
         relate="平板 显示-LCD、电池快充、结构/工艺、无线通信。",
         vendor="realme（真我）/ 平板 X", time="2026-08-07（上架）",
         url="https://www.realme.com/cn/",
         src_detail="中关村在线、realme官方", note="千元级 realme UI 平板",
         grade="C", status="coming", stars=3,
         dims=["显示/OLED","电池/快充","结构/工艺","无线通信"]),

    dict(region="国内", category="手机/SoC/电池/生物识别", title="REDMI M100",
         sig_type="开售（8/18）", sources="2（小米官方/IT之家）",
         key_params="骁龙4 Gen5；6.9\" LCD 120Hz；7900mAh；1799元；国民长续航机",
         tech=["骁龙4 Gen5 5G 平台", "6.9\" 120Hz 大屏 长续航", "7900mAh 超大电池 1799元"],
         why="REDMI M100于8/18开售，以骁龙4 Gen5+7900mAh+6.9英寸120Hz切入千元5G长续航，1799元主打实用与耐用。",
         relate="手机 SoC（骁龙4 Gen5）、显示-LCD、电池快充、生物识别、无线通信。",
         vendor="小米（Redmi）/ M100", time="2026-08-18（开售）",
         url="https://www.mi.com/",
         src_detail="小米官方、IT之家", note="千元7900mAh长续航机",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","生物识别","无线通信"]),

    dict(region="国内", category="手机/SoC/电池/散热", title="荣耀WIN RT2",
         sig_type="预热（预计10-12月）", sources="1（荣耀官方/数码博主）",
         key_params="骁龙8 Elite Gen5；11000mAh；100W；Windows二合一平板手机形态",
         tech=["骁龙8 Elite Gen5 旗舰平台", "11000mAh+100W 超大电池", "Windows 二合一 平板手机形态"],
         why="荣耀WIN RT2预热，以骁龙8 Elite Gen5+11000mAh+100W定义Windows二合一大电池终端设备，预计10-12月登场。",
         relate="手机/平板 SoC（骁龙8 Elite Gen5）、电池快充、散热、结构/工艺、无线通信。",
         vendor="荣耀（HONOR）/ WIN RT2", time="2026-10（预计）",
         url="https://www.hihonor.com/cn/",
         src_detail="荣耀官方、数码博主", note="Windows二合一 11000mAh",
         grade="B", status="coming", stars=4,
         dims=["SoC/芯片","电池/快充","散热","结构/工艺","无线通信"]),

    dict(region="国内", category="智能手表/电池/生物识别", title="荣耀手表5 Pro eSIM版",
         sig_type="在售（京东）", sources="1（京东自营）",
         key_params="eSIM独立通信；10天续航；AI跑步算法；1.5\"圆屏；纳米陶瓷；1799元",
         tech=["eSIM 独立通信 脱离手机", "10天续航 + AI跑步算法", "1.5\" 圆屏 纳米陶瓷机身"],
         why="荣耀手表5 Pro eSIM版在售，以eSIM独立通信+10天续航+AI跑步算法切入独立穿戴，1799元主打运动与健康。",
         relate="智能手表 电池快充、生物识别（心率/血氧）、传感器、无线通信（eSIM）、马达/触觉（振动反馈）。",
         vendor="荣耀（HONOR）/ 手表5 Pro eSIM", time="2026-08（在售）",
         url="https://www.hihonor.com/cn/",
         src_detail="京东自营、荣耀官方", note="eSIM独立通信运动表",
         grade="B", status="released", stars=4,
         dims=["电池/快充","生物识别","传感器","无线通信","马达/触觉","结构/工艺"]),

    dict(region="国内", category="智能手表/传感器/显示", title="华为WATCH GT 6 Pro",
         sig_type="在售（京东）", sources="1（京东自营）",
         key_params="钛合金表壳；3000nit；21天续航；ECG；双频GNSS；IP69+5ATM；2488元",
         tech=["钛合金表壳 + 3000nit 高亮屏", "21天续航 + ECG 心电", "双频GNSS + IP69/5ATM 防护"],
         why="华为WATCH GT 6 Pro在售，以钛合金+3000nit+21天续航+ECG+双频GNSS切入高端运动健康表，2488元主打专业监测。",
         relate="智能手表 传感器（心率/血氧/ECG）、电池快充、生物识别、显示-OLED、结构/工艺、认证/合规。",
         vendor="华为（HUAWEI）/ WATCH GT 6 Pro", time="2026-08（在售）",
         url="https://consumer.huawei.com/cn/watches/",
         src_detail="京东自营、华为官方", note="钛合金 ECG 双频GNSS",
         grade="A", status="released", stars=4,
         dims=["传感器","电池/快充","生物识别","显示/OLED","结构/工艺","认证/合规"]),

    dict(region="国内", category="AR-VR眼镜/AI/音频", title="李未可Lawaken City AI智能眼镜",
         sig_type="发布（近期）", sources="1（李未可官方）",
         key_params="38g；128语种实时翻译；离线翻译；AI录音；5天待机；IP54",
         tech=["38g 超轻机身", "128语种实时翻译 + 离线翻译", "AI录音 5天待机 IP54"],
         why="李未可Lawaken City AI智能眼镜以38g机身+128语种实时/离线翻译+AI录音切入跨语言沟通与商务记忆，轻量化差异化。",
         relate="AR-VR眼镜 AI/NPU（翻译/记忆）、音频、传感器、结构/工艺、无线通信。",
         vendor="李未可科技 / Lawaken City", time="2026-08（发布）",
         url="https://www.liweike.com/",
         src_detail="李未可官方", note="38g跨语言AI眼镜",
         grade="B", status="released", stars=4,
         dims=["AI/NPU","音频","传感器","结构/工艺","无线通信"]),

    dict(region="国内", category="AR-VR眼镜/AI/摄像头", title="夸克AI眼镜G1 / 千问AI眼镜",
         sig_type="发布（近期）", sources="1（阿里/夸克官方）",
         key_params="高通AR1+恒玄BES2800；1200万像素摄像头；40g；9小时续航；1999元起",
         tech=["高通AR1 + 恒玄BES2800 双芯", "1200万像素摄像头 + 40g 轻量", "9小时续航 阿里千问大模型"],
         why="夸克AI眼镜G1（千问AI眼镜）以高通AR1+恒玄BES2800+1200万摄+40g切入AI拍摄/问答眼镜，1999元起主打通勤与记录。",
         relate="AR-VR眼镜 AI/NPU（千问大模型）、摄像头、音频、传感器、结构/工艺、无线通信。",
         vendor="阿里巴巴（夸克）/ AI眼镜G1", time="2026-08（发布）",
         url="https://www.quark.cn/",
         src_detail="阿里官方、夸克", note="阿里千问双芯AI眼镜",
         grade="B", status="released", stars=4,
         dims=["AI/NPU","摄像头","音频","传感器","结构/工艺","无线通信"]),

    dict(region="国内", category="笔记本电脑/SoC/显示/散热", title="机械革命无界14 2026",
         sig_type="在售（官方）", sources="1（机械革命官方）",
         key_params="轻薄全能本；2026款；2.8K高刷屏；主流独显；性价比定位",
         tech=["2026款 轻薄全能平台", "2.8K 高刷护眼屏", "主流独显 + 高效散热"],
         why="机械革命无界14 2026以轻薄全能本定位切入主流市场，2.8K屏+独显兼顾办公与轻度创作，延续高性价比路线。",
         relate="笔记本 SoC、显示-OLED、散热、结构/工艺、无线通信。",
         vendor="机械革命 / 无界14 2026", time="2026-08（在售）",
         url="https://www.mechrevo.com/",
         src_detail="机械革命官方", note="轻薄全能本 2026款",
         grade="C", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","散热","结构/工艺","无线通信"]),

    dict(region="国内", category="笔记本电脑/SoC/GPU/散热", title="神舟战神T9 2026",
         sig_type="在售（官方）", sources="1（神舟官方）",
         key_params="游戏本；i7-14700HX + RTX5060；16英寸 2.5K；8999元",
         tech=["i7-14700HX 高性能HX平台", "RTX5060 新一代独显", "16\" 2.5K 高刷电竞屏"],
         why="神舟战神T9 2026以i7-14700HX+RTX5060+16英寸2.5K切入高性能游戏本，8999元主打性价比独显机型。",
         relate="笔记本 SoC（Intel HX）、GPU（RTX5060）、散热、结构/工艺。",
         vendor="神舟 / 战神T9 2026", time="2026-08（在售）",
         url="https://www.hasee.com/",
         src_detail="神舟官方", note="i7-14700HX+RTX5060游戏本",
         grade="C", status="released", stars=3,
         dims=["SoC/芯片","散热","结构/工艺","显示/OLED"]),

    dict(region="国内", category="笔记本电脑/SoC/显示/电池", title="联想昭阳悦Air14",
         sig_type="在售（官方）", sources="1（联想官方）",
         key_params="轻薄商务本；2026款；长续航；全金属机身",
         tech=["2026款 轻薄商务平台", "长续航 全金属机身", "轻量化便携设计"],
         why="联想昭阳悦Air14以2026款轻薄商务本定位切入政企办公，长续航+全金属机身兼顾移动生产力。",
         relate="笔记本 SoC、显示、电池快充、结构/工艺、无线通信。",
         vendor="联想 / 昭阳悦Air14", time="2026-08（在售）",
         url="https://www.lenovo.com.cn/",
         src_detail="联想官方", note="轻薄商务本 2026款",
         grade="C", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","结构/工艺","无线通信"]),

    dict(region="国内", category="无线充/充电/BMS", title="倍思MagPro",
         sig_type="在售（官方）", sources="1（倍思官方）",
         key_params="Qi2 磁吸无线充；MagSafe兼容；便携磁吸；多设备",
         tech=["Qi2 磁吸无线充", "MagSafe 生态兼容", "便携磁吸 多设备充电"],
         why="倍思MagPro以Qi2磁吸+MagSafe兼容切入磁吸无线充，兼顾iPhone磁吸与多设备便携充电场景。",
         relate="无线充 充电协议（Qi2）、BMS/电源、结构/工艺、认证/合规。",
         vendor="倍思（Baseus）/ MagPro", time="2026-08（在售）",
         url="https://www.baseus.com/",
         src_detail="倍思官方", note="Qi2磁吸无线充",
         grade="B", status="released", stars=3,
         dims=["BMS/电源","认证/合规","结构/工艺","无线通信"]),

    dict(region="国内", category="智能音箱/音频/AI", title="华为 AI 音箱 2e",
         sig_type="上架（8/17）", sources="1（华为官方/京东）",
         key_params="85颗LED灯阵；小艺助手；鸿蒙超级终端；智能家居中控",
         tech=["85颗LED灯阵 氛围交互", "小艺助手 AI 语音", "鸿蒙超级终端 全屋中控"],
         why="华为AI音箱2e于8/17上架，以85颗LED灯阵+小艺助手+鸿蒙超级终端切入入门智能中控音箱，强化全屋IoT联动。",
         relate="智能音箱 音频、AI/NPU（小艺）、无线通信（鸿蒙超级终端）、结构/工艺。",
         vendor="华为（HUAWEI）/ AI 音箱 2e", time="2026-08-17（上架）",
         url="https://consumer.huawei.com/cn/audio/speakers/",
         src_detail="华为官方、京东", note="85颗LED灯阵 鸿蒙中控",
         grade="B", status="released", stars=3,
         dims=["音频","AI/NPU","无线通信","结构/工艺"]),

    # ---------------- 国际 15 条 ----------------
    dict(region="国际", category="平板/SoC/显示/电池", title="Honor Pad 20 Pro",
         sig_type="发布预告（马来 8/24）", sources="1（荣耀国际/马来西亚）",
         key_params="12.1英寸 3K；骁龙8s Gen4；10100mAh；66W；Paperlike屏；马来8/24发布",
         tech=["骁龙8s Gen4 旗舰平台", "12.1\" 3K Paperlike 类纸屏", "10100mAh+66W 大电池"],
         why="Honor Pad 20 Pro将于8/24在马来西亚发布，以12.1英寸3K Paperlike屏+骁龙8s Gen4+10100mAh切入东南亚高端平板，与国行配置对齐。",
         relate="平板 SoC（骁龙8s Gen4）、显示（3K类纸）、电池快充、手写笔/触控、结构/工艺。",
         vendor="HONOR（国际）/ Pad 20 Pro", time="2026-08-24（马来发布）",
         url="https://www.hihonor.com/global/",
         src_detail="荣耀国际、马来西亚官网", note="东南亚高端平板 Pro",
         grade="A", status="coming", stars=4,
         dims=["SoC/芯片","显示/OLED","电池/快充","手写笔/触控","结构/工艺"]),

    dict(region="国际", category="平板/SoC/显示/电池", title="Blackview Link 5",
         sig_type="日本发布（8/14）", sources="1（Blackview官方/日本媒体）",
         key_params="11英寸 HD IPS；Android 17；Allwinner A537；8300mAh；18W；约22999日元",
         tech=["Android 17 新系统", "11\" HD IPS 护眼屏", "8300mAh 长续航 入门定位"],
         why="Blackview Link 5于8/14在日本发布，以11英寸Android 17+8300mAh切入海外入门平板，22999日元主打长续航与护眼。",
         relate="平板 SoC（Allwinner A537）、显示-LCD、电池快充、结构/工艺、无线通信。",
         vendor="Blackview / Link 5", time="2026-08-14（日本发布）",
         url="https://www.blackview.hk/products/item/link-5",
         src_detail="Blackview官方、日本媒体", note="Android 17 入门长续航平板",
         grade="C", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","结构/工艺","无线通信"]),

    dict(region="国际", category="手机/SoC/显示/电池", title="Motorola Edge 70 Ultra",
         sig_type="预热（8月）", sources="1（Motorola官方）",
         key_params="旗舰定位；大电池；高刷曲面屏；影像旗舰；北美/全球",
         tech=["旗舰 SoC 平台", "高刷曲面屏 影像旗舰", "大电池 长续航"],
         why="Motorola Edge 70 Ultra于8月预热，以旗舰影像+大电池+高刷曲面屏切入北美/全球高端，对标安卓旗舰阵营。",
         relate="手机 SoC、显示-OLED、电池快充、摄像头、结构/工艺、无线通信。",
         vendor="Motorola / Edge 70 Ultra", time="2026-08（预热）",
         url="https://www.motorola.com/",
         src_detail="Motorola官方", note="海外旗舰影像机",
         grade="B", status="coming", stars=4,
         dims=["SoC/芯片","显示/OLED","电池/快充","摄像头","结构/工艺","无线通信"]),

    dict(region="国际", category="手机/SoC/显示/电池", title="Redmi Note 17 Pro Max 全球版",
         sig_type="全球发布（近期）", sources="1（小米国际/GSMArena）",
         key_params="大电池长续航；高刷屏；影像升级；全球市场",
         tech=["大电池 长续航平台", "高刷 AMOLED 屏", "影像系统升级"],
         why="Redmi Note 17 Pro Max全球版发布，以长续航+高刷屏+影像升级切入全球中端，延续Note系列走量定位。",
         relate="手机 SoC、显示-OLED、电池快充、摄像头、无线通信。",
         vendor="Xiaomi（Redmi）/ Note 17 Pro Max", time="2026-08（全球发布）",
         url="https://www.mi.com/global/",
         src_detail="小米国际、GSMArena", note="全球中端长续航机",
         grade="B", status="released", stars=3,
         dims=["SoC/芯片","显示/OLED","电池/快充","摄像头","无线通信"]),

    dict(region="国际", category="智能戒指/传感器/电池", title="Oura Ring 5",
         sig_type="韩国发布（8/18）", sources="1（Oura官方/韩媒）",
         key_params="较前代小40%；7天续航；健康/睡眠监测；智能戒指形态",
         tech=["较前代小40% 更轻佩戴", "7天续航 健康监测", "睡眠/心率/体温传感"],
         why="Oura Ring 5于8/18在韩国发布，以较前代小40%+7天续航切入智能戒指健康赛道，主打无感长期佩戴监测。",
         relate="智能戒指 传感器（心率/体温/睡眠）、电池快充、生物识别、结构/工艺。",
         vendor="Oura / Ring 5", time="2026-08-18（韩国发布）",
         url="https://ouraring.com/",
         src_detail="Oura官方、韩国媒体", note="更小更轻智能戒指",
         grade="B", status="released", stars=4,
         dims=["传感器","电池/快充","生物识别","结构/工艺"]),

    dict(region="国际", category="智能手表/传感器/电池", title="Amazfit Balance 3",
         sig_type="在售（官方）", sources="1（Amazfit官方）",
         key_params="全天候健康；双频GPS；长续航；AMOLED；Zepp OS",
         tech=["双频GPS 高精度定位", "AMOLED 全天候健康表", "Zepp OS 长续航"],
         why="Amazfit Balance 3在售，以双频GPS+AMOLED+长续航切入全能健康手表，延续Balalnce系列平衡定位。",
         relate="智能手表 传感器（GPS/心率/血氧）、电池快充、生物识别、显示-OLED、无线通信。",
         vendor="Amazfit（华米）/ Balance 3", time="2026-08（在售）",
         url="https://www.amazfit.com/",
         src_detail="Amazfit官方", note="全能健康平衡表",
         grade="B", status="released", stars=3,
         dims=["传感器","电池/快充","生物识别","显示/OLED","无线通信"]),

    dict(region="国际", category="智能手表/传感器/结构", title="Amazfit Cheetah 2 Ultra",
         sig_type="上市（5月 全球）", sources="1（Amazfit官方/JD）",
         key_params="1.5\" AMOLED 蓝宝石；5级钛合金；双频GPS；30天续航；780mAh；64GB；¥4299",
         tech=["5级钛合金+蓝宝石镜面", "1.5\" AMOLED 3000nit 双频GPS", "780mAh 30天续航 越野跑专攻"],
         why="Amazfit Cheetah 2 Ultra上市，以5级钛合金+蓝宝石+双频GPS+30天续航切入专业越野跑表，¥4299主打高端运动。",
         relate="智能手表 传感器（双频GPS/光学心率）、电池快充、生物识别、显示-OLED、结构/工艺、认证/合规。",
         vendor="Amazfit（华米）/ Cheetah 2 Ultra", time="2026-05（上市）",
         url="https://www.amazfit.com/",
         src_detail="Amazfit官方、京东", note="钛合金越野跑表 双频GPS",
         grade="B", status="released", stars=4,
         dims=["传感器","电池/快充","生物识别","显示/OLED","结构/工艺","认证/合规"]),

    dict(region="国际", category="AR-VR头显/显示/光学", title="Pimax Dream Air SE",
         sig_type="开放预购（8月）", sources="1（Pimax官方）",
         key_params="micro-OLED PC VR；轻量化；8月清预购；$899起",
         tech=["micro-OLED 高清PC VR", "轻量化机身 舒适佩戴", "$899起 消费级PC VR"],
         why="Pimax Dream Air SE于8月开放预购，以micro-OLED+轻量化切入消费级PC VR，899美元起降低高端VR门槛。",
         relate="AR-VR头显 显示（micro-OLED）、结构/工艺、传感器、音频。",
         vendor="Pimax / Dream Air SE", time="2026-08（开放预购）",
         url="https://www.pimax.com/",
         src_detail="Pimax官方", note="micro-OLED消费级PC VR",
         grade="B", status="coming", stars=4,
         dims=["显示/OLED","结构/工艺","传感器","音频"]),

    dict(region="国际", category="AR-VR头显/无线/散热", title="Valve Steam Frame",
         sig_type="认证通过（FCC 7/29）", sources="1（FCC/Valve）",
         key_params="无线PC VR；2026夏；FCC 7/29过审；$899-1199；Steam生态",
         tech=["无线 PC VR 低延迟", "Steam 生态直连", "FCC 过审 2026夏上市"],
         why="Valve Steam Frame于7/29通过FCC认证，以无线PC VR+Steam生态切入高端无线头显，$899-1199预计2026夏上市。",
         relate="AR-VR头显 显示、结构/工艺、无线通信（无线VR）、散热。",
         vendor="Valve / Steam Frame", time="2026-07（FCC）",
         url="https://store.steampowered.com/",
         src_detail="FCC数据库、Valve", note="Valve无线PC VR头显",
         grade="C", status="coming", stars=4,
         dims=["显示/OLED","结构/工艺","无线通信","散热"]),

    dict(region="国际", category="笔记本电脑/SoC/显示/GPU", title="ThinkPad P1 Gen 9",
         sig_type="在售（官方）", sources="1（Lenovo官方）",
         key_params="移动工作站；RTX专业显卡；高色域屏；ISV认证",
         tech=["移动工作站 标压平台", "RTX 专业显卡 ISV认证", "高色域高亮屏"],
         why="ThinkPad P1 Gen 9在售，以移动工作站+RTX专业显卡+ISV认证切入设计与工程生产力，延续P系列专业定位。",
         relate="笔记本 SoC、GPU（RTX专业卡）、显示-OLED、散热、结构/工艺。",
         vendor="Lenovo / ThinkPad P1 Gen 9", time="2026-08（在售）",
         url="https://www.lenovo.com/",
         src_detail="Lenovo官方", note="移动工作站 专业显卡",
         grade="A", status="released", stars=4,
         dims=["SoC/芯片","显示/OLED","散热","结构/工艺","无线通信"]),

    dict(region="国际", category="笔记本电脑/SoC/显示/散热", title="ROG Zephyrus Duo 2026",
         sig_type="在售（官方）", sources="1（ASUS ROG官方）",
         key_params="双屏游戏本；旗舰CPU+GPU；副屏拓展；液金散热",
         tech=["双屏 副屏拓展生产力", "旗舰 CPU+GPU 组合", "液金散热 高负载稳定"],
         why="ROG Zephyrus Duo 2026以双屏+旗舰CPU/GPU+液金散热切入高端双屏游戏本，兼顾游戏与创作多任务。",
         relate="笔记本 SoC、显示-OLED（双屏）、散热、结构/工艺、无线通信。",
         vendor="ASUS ROG / Zephyrus Duo 2026", time="2026-08（在售）",
         url="https://rog.asus.com/",
         src_detail="ASUS ROG官方", note="双屏旗舰游戏本",
         grade="A", status="released", stars=4,
         dims=["SoC/芯片","显示/OLED","散热","结构/工艺","无线通信"]),

    dict(region="国际", category="无线充/充电/BMS", title="Belkin UltraCharge Pro Qi2",
         sig_type="在售（官方）", sources="1（Belkin官方）",
         key_params="Qi2 25W 磁吸；USB-C；多设备；MFM兼容",
         tech=["Qi2 25W 磁吸无线", "USB-C 多设备充电", "MFM/Qi2 认证兼容"],
         why="Belkin UltraCharge Pro Qi2以25W磁吸+USB-C多设备切入高端磁吸充电，MFM/Qi2认证兼顾iPhone与安卓。",
         relate="无线充 充电协议（Qi2）、BMS/电源、结构/工艺、认证/合规。",
         vendor="Belkin / UltraCharge Pro Qi2", time="2026-08（在售）",
         url="https://www.belkin.com/",
         src_detail="Belkin官方", note="Qi2 25W磁吸充",
         grade="B", status="released", stars=3,
         dims=["BMS/电源","认证/合规","结构/工艺"]),

    dict(region="国际", category="无线充/充电/BMS", title="AUKEY MagFusion",
         sig_type="在售（官方）", sources="1（AUKEY官方）",
         key_params="Qi2 磁吸；MagSafe兼容；便携；多功率档",
         tech=["Qi2 磁吸无线充", "MagSafe 生态兼容", "便携 多功率档"],
         why="AUKEY MagFusion以Qi2磁吸+MagSafe兼容切入便携磁吸充电，多功率档兼顾手机与配件。",
         relate="无线充 充电协议（Qi2）、BMS/电源、结构/工艺、认证/合规。",
         vendor="AUKEY / MagFusion", time="2026-08（在售）",
         url="https://www.aukey.com/",
         src_detail="AUKEY官方", note="Qi2磁吸便携充",
         grade="B", status="released", stars=3,
         dims=["BMS/电源","认证/合规","结构/工艺"]),

    dict(region="国际", category="智能音箱/音频/结构", title="Marshall Acton IV",
         sig_type="在售（官方）", sources="1（Marshall官方）",
         key_params="家用蓝牙音箱；经典复古设计；动态低音；蓝牙5.x",
         tech=["经典复古木质箱体", "动态低音增强", "蓝牙无线播放"],
         why="Marshall Acton IV在售，以经典复古设计+动态低音切入家用蓝牙音箱，兼顾颜值与听感。",
         relate="智能音箱 音频、结构/工艺、无线通信（蓝牙）。",
         vendor="Marshall / Acton IV", time="2026-08（在售）",
         url="https://www.marshallheadphones.com/",
         src_detail="Marshall官方", note="复古家用蓝牙音箱",
         grade="B", status="released", stars=3,
         dims=["音频","结构/工艺","无线通信"]),

    dict(region="国际", category="智能音箱/音频/结构", title="LG xboom Mini",
         sig_type="上市（2026 lineup）", sources="1（LG官方）",
         key_params="1.75\" 低音单元；AI Sound；IP67；10小时；Magic Strap挂绳；220g",
         tech=["1.75\" 低音 + 被动辐射器", "AI Sound 自适应调音", "IP67 防护 + 10h 续航 + 挂绳"],
         why="LG xboom Mini于2026阵容上市，以1.75英寸低音+AI Sound+IP67+10小时切入超便携音箱，220g配挂绳主打随身。",
         relate="智能音箱 音频、结构/工艺（IP67军规）、电池快充、无线通信。",
         vendor="LG / xboom Mini", time="2026-08（上市）",
         url="https://www.lg.com/uk/speakers/portable-speakers/",
         src_detail="LG官方", note="超便携 IP67 AI音箱",
         grade="B", status="released", stars=3,
         dims=["音频","结构/工艺","电池/快充","无线通信"]),
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
