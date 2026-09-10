# -*- coding: utf-8 -*-
"""生成 WB_2026-09-10_硬件看板.html（智能终端硬件情报日报）"""
import re, subprocess

TPL = '_tmp_tpl.html'
OUT = 'WB_2026-09-10_硬件看板.html'
DATE = '2026-09-10'
WEEK = '周四'

# region: cn / intl
# st: coming / progress / released
C = [
 dict(region='cn', title='传音 TECNO Camon Slim 5G 发布：6.39mm 机身塞入 6000mAh', vendor='TECNO（传音）', model='Camon Slim 5G',
      domain='手机', st='coming', date='2026-09-08', lvl='C', stars=4,
      sig='新品发布', srcn='2 个印证源（IT之家、Notebookcheck）',
      url='https://www.ithome.com/0/999/710.htm', sname='IT之家',
      params='6.78 英寸 2644×1208 AMOLED 144Hz；天玑 7300e；8GB(+16GB 虚拟)+128/256GB；6000mAh 硅碳 +45W；6.39mm；50MP LYTIA 700C 1/1.56 英寸 OIS',
      tech=['6.39mm 机身塞入 6000mAh 硅碳电池', 'IP66/68/69/69K 与 MIL-STD-810H 四防', 'GPU 1080P 经 T1 芯片上采样至 1.5K', '1/11236 秒长焦快拍', '湿手油手触控 2.0'],
      why='6.39mm 做到 6000mAh 硅碳，是超薄与大电池并存的量产标杆，为平板轻薄化提供堆叠工程参照。',
      rel='硅碳负极让「超薄+大电池」从矛盾变为可量产方案。',
      detail='IT之家，2026-09-08，援引 NotebookCheck', remark='价格与各市场上时间未公布；第三枚后置镜头为装饰件',
      dims=['电池/续航','SoC/芯片','显示/OLED','影像','材质/工艺']),

 dict(region='cn', title='小度智能音箱 Pro Max 发布：三环境传感器 + 小彩屏', vendor='百度（小度）', model='小度智能音箱 Pro Max',
      domain='智能音箱', st='coming', date='2026-09-08', lvl='C', stars=4,
      sig='新品发布', srcn='1 个印证源',
      url='https://news.qq.com/rain/a/20260908A0AOD800', sname='IT之家（腾讯新闻）',
      params='3 英寸 12W 单元，倒相管 + 导音锥；内置温度、湿度、光线三传感器；搭载小彩屏；上市价 349 元，首销 299 元；9 月 28 日预售',
      tech=['小彩屏显示时间与表情', '温湿度与光线三传感器联动家电', '超能小度支持多轮对话、15 种方言、长期记忆', '3 英寸 12W 倒相管 + 导音锥', '首销 299 元'],
      why='299 元音箱加入三环境传感器与彩屏，把家庭智能中枢感知入口前移，TCL 需评估传感器与屏显在中控产品的配比。',
      rel='智能音箱正升级为带环境感知的家庭 AI 中枢。',
      detail='IT之家，2026-09-08', remark='与小度 AI 手表 Fit 同品牌但属不同产品线',
      dims=['AI/NPU','音频/扬声器','Wi-Fi/连接']),

 dict(region='cn', title='华为 WATCH 6 系列发布：2799 元起，首发高尿酸风险评估', vendor='华为', model='WATCH 6 系列',
      domain='智能手表', st='coming', date='2026-09-07', lvl='B', stars=5,
      sig='新品发布', srcn='2 个印证源（IT之家、华为全场景发布会）',
      url='https://www.ithome.com/0/999/359.htm', sname='IT之家',
      params='球面蓝宝石表镜；峰值亮度 3000nits、Pro 3500nits；42mm 38g/10.2mm 航空铝；Pro 43/46mm 纳米微晶陶瓷与钛合金；2799 元起；9 月 23 日开售',
      tech=['X-TAP 2.0 压感精度翻倍、指标 17→20 项', '联合协和首发高尿酸风险评估', 'Pro 首次全陶瓷表壳配 18K 金表冠', 'eSIM 独立通信 + 翻腕手势', '全能与省电双模 3 秒切换'],
      why='穿戴健康从心率血氧扩展到代谢无创评估，提示平板与穿戴的跨端健康数据协同新方向。',
      rel='穿戴正从运动记录转向「监测-洞察-养成」主动健康管理。',
      detail='IT之家，2026-09-07，华为全场景新品发布会', remark='电池容量与续航时长官方未披露，待印证',
      dims=['AI/NPU','显示/OLED','材质/工艺','5G/通信']),

 dict(region='cn', title='WiWU Qi2.2 三合一风冷磁吸无线充（25W 主动散热）', vendor='WiWU 为悟（深圳吉玛仕）', model='Qi2.2 三合一空间站风冷磁吸无线充',
      domain='无线充', st='coming', date='2026-08-19', lvl='B', stars=3,
      sig='认证/新品', srcn='1 个印证源',
      url='https://www.chongdiantou.com/archives/1787110837659.html', sname='充电头网',
      params='Qi2.2 认证：手机 25W、耳机 5W、手表 2.5W 三设备同充；立式桌面，面板横竖屏切换 + 约 36° 俯仰调节；内置智能温控风扇',
      tech=['手机端通过 Qi2.2 认证，磁吸 25W', '手表 2.5W + 耳机 5W 三设备同充', '内置智能温控风扇主动散热', '面板约 36° 俯仰 + 横竖屏切换', '触摸键切换指示灯与风扇'],
      why='25W 磁吸 + 主动风冷已下放到深圳中小品牌，说明该方案成本可控，TCL 平板若支持磁吸充电需同步预留散热位。',
      rel='三合一磁吸底座可平移为平板 + 耳机 + 手表的桌面一体充电站。',
      detail='充电头网，2026-08-19', remark='售价与正式上市时间未公布，9 月 19 日深圳充电嘉年华首秀',
      dims=['快充/无线充','散热/液冷']),

 dict(region='cn', title='汉王 N6 Pro 墨水屏录写本将售：8192 级压感 + 四麦转写', vendor='汉王科技', model='N6 Pro',
      domain='平板', st='coming', date='2026-08-05', lvl='C', stars=3,
      sig='新品预告', srcn='2 个印证源（IT之家、网易科技）',
      url='https://www.ithome.com/0/985/915.htm', sname='IT之家',
      params='6 英寸 300PPI 黑白墨水屏；8192 级压感手写；内置 8 核处理器；四麦克风阵列；CNC 金属中框三面窄边框；8 月 11 日 20:00 发售',
      tech=['6 英寸 300PPI 墨水屏', '8192 级压感数字笔', '四麦克风阵列支持语音转写与纪要', 'CNC 金属中框 + 三面窄边框', '取消电容触控减少误触'],
      why='墨水屏叠加 8192 级压感与四麦 AI 转写，把「读写记」合成随身形态，TCL 护眼类平板可借鉴其手写 + AI 记录栈。',
      rel='护眼显示、手写笔与 AI 会议记录正融合进单一随身终端。',
      detail='IT之家、网易科技，2026-08-05', remark='售价、SoC 型号与电池容量官方尚未公布',
      dims=['显示/OLED','手写笔/触控','AI/NPU','音频/扬声器']),

 dict(region='cn', title='TOZO AIVU 眼镜海外众筹：45g 光波导 + 端侧隐私识别', vendor='TOZO', model='AIVU',
      domain='AR-VR眼镜', st='progress', date='2026-07-21', lvl='D', stars=3,
      sig='众筹', srcn='1 个印证源',
      url='https://new.qq.com/rain/a/20260721A06R9300', sname='腾讯网《AI 眼镜日报》',
      params='整机 45g；树脂光波导镜片；本地隐私运算，拍摄画面仅用于实时 AI 识别、不存储不上传；集 AR 显示、音频播放与 AI 视觉识别于一体；Kickstarter 众筹',
      tech=['45g 树脂光波导轻量化', '端侧本地识别不上传', '拍摄仅用于实时 AI 识别', 'AR 显示 + 音频 + 视觉三合一', '主打日常潮流佩戴'],
      why='「不存储、只做端侧识别」是绕开拍摄隐私争议的产品路径，值得 TCL 眼镜定义在隐私合规上参考。',
      rel='隐私设计正成为 AI 眼镜能否日常佩戴的关键变量。',
      detail='腾讯网《AI 眼镜日报》，2026-07-21，引 XR 控', remark='众筹阶段，售价与量产时间未公布',
      dims=['AR/VR显示','AI/NPU','影像','材质/工艺']),

 dict(region='cn', title='华为 Pura X View 阔直板开售：6.39 英寸 16:9.5 + 7000mAh', vendor='华为', model='Pura X View',
      domain='手机', st='released', date='2026-09-09', lvl='B', stars=5,
      sig='开售', srcn='2 个印证源（IT之家、华为商城）',
      url='https://www.ithome.com/0/999/980.htm', sname='IT之家',
      params='6.39 英寸 2232×1320 OLED 直屏 16:9.5，120Hz/2160Hz PWM/6500nits 峰值；麒麟 9030S；7000mAh 硅负极 +66W 有线/50W 无线；6.68mm/201g；12+256GB 5999 元',
      tech=['四等边 1.05mm、屏占比 96.1%', '6400mm² VC 均热板', '7000mAh 硅负极电池', '2 亿像素 RYYB 主摄 + 潜望长焦', 'IP68/IP69 + 北斗卫星消息 + eSIM'],
      why='6.39 英寸 16:9.5 比例配 7000mAh 仍做到 201g，验证「阔直板」新形态，TCL 可评估该比例的屏幕开模与堆叠。',
      rel='新屏幕比例与硅负极电池正重塑轻薄大电池机型。',
      detail='IT之家，2026-09-09，华为商城/京东同步上架', remark='无',
      dims=['显示/OLED','SoC/芯片','电池/续航','快充/无线充','散热/液冷']),

 dict(region='cn', title='ThinkPad E16 酷睿 5 版开售：7299 元，全接口 + 护眼认证', vendor='联想', model='ThinkPad E16 2026',
      domain='笔记本电脑', st='released', date='2026-09-06', lvl='C', stars=3,
      sig='开售', srcn='2 个印证源（IT之家、京东商品页）',
      url='https://www.ithome.com/0/999/047.htm', sname='IT之家',
      params='16 英寸 1920×1200 60Hz 400nits IPS，Eyesafe 2.0 + AG 防眩光；酷睿 5 320（6 核 6 线程）；16GB+512GB；48Wh；1.71kg/17.05mm；7299 元',
      tech=['双雷电 4 + RJ45 + HDMI 2.1 全接口', '400nits AG 防眩光 + Eyesafe 2.0', '杜比全景声与哈曼音效', '48Wh 电池', '9 月 7 日 0 点开售'],
      why='7000 元档商务本仍以接口完整性与护眼认证为卖点，TCL 二合一与键盘生态可参考其接口与护眼标准组合。',
      rel='生产力设备的护眼认证与全接口仍是刚需。',
      detail='IT之家、京东商品页，2026-09-06', remark='48Wh 电池偏小，续航表现待实测印证',
      dims=['显示/OLED','SoC/芯片','Wi-Fi/连接']),

 dict(region='cn', title='加南 K2 AI 眼镜拆解：33.5g + 音频 SoC 与影像 ISP 双芯', vendor='加南科技（KANNAN）', model='K2（AGK201CN）',
      domain='AR-VR眼镜', st='released', date='2026-09-01', lvl='B', stars=3,
      sig='拆解/实测', srcn='2 个印证源（我爱音频网、搜狐）',
      url='https://www.toutiao.com/article/7680480110181122623/', sname='我爱音频网',
      params='实测整机 33.5g、镜框 25g；3200 万摄 4K30 + EIS 防抖；物奇微 WQ7036AX + 星宸 SSC309QL；64GB eMMC；150mAh；IP54；Wi-Fi6 + 蓝牙 5.4；日常续航 1.3~1.5 天',
      tech=['超轻尼龙镜框，镜框仅 25g', '物奇微音频 SoC + 星宸影像处理器双芯异构', '3200 万像素 4K30，EIS + AI 双防抖', '逆声波定向传音 + 3 麦 AI 降噪', '江波龙超小尺寸 64GB eMMC'],
      why='用音频 SoC + 独立影像 ISP 替代 AR1 方案，是一条更低成本的国产 AI 眼镜芯片路径，值得 TCL 做 BOM 对标。',
      rel='拍摄类 AI 眼镜是第一视角内容采集端，可与平板本地 AI 转写/归档联动。',
      detail='我爱音频网拆解稿，2026-09-01', remark='产品 6 月已发布，9 月 1 日为拆解稿；售价未公布',
      dims=['AR/VR显示','影像','SoC/芯片']),

 dict(region='cn', title='机械革命无界 14S 2026 开售：Intel 18A 平台 3899 元', vendor='机械革命（清华同方）', model='无界 14S 2026',
      domain='笔记本电脑', st='released', date='2026-08-27', lvl='C', stars=3,
      sig='开售', srcn='1 个印证源',
      url='https://news.qq.com/rain/a/20260827A087KE00', sname='IT之家（腾讯新闻）',
      params='14 英寸 1920×1200 60Hz 100% sRGB 全局 DC 调光雾面屏；酷睿 5 315（Intel 18A 工艺）；12GB+500GB；60Wh；约 1.1kg 银色金属机身；4199 元，首发 3899 元',
      tech=['Intel 18A 制程，功耗较前代降 64%', '60Wh 电池，24 小时本地视频续航', '1.3mm 键程键盘', '双全功能 USB-C 10Gbps + HDMI 2.1', 'Fn+X 三档性能切换 15/25/30W'],
      why='18A 平台把长续航轻薄本压到 3899 元，TCL 若评估低功耗 PC 平台需对标其能效与续航口径。',
      rel='新一代低功耗制程正把长续航轻薄本价格带下压。',
      detail='IT之家（腾讯新闻），2026-08-27', remark='部分地区国补后低至约 3314 元',
      dims=['SoC/芯片','电池/续航','显示/OLED']),

 dict(region='cn', title='步步高学习机 S10 上市：14.2 英寸类朗伯光刻护眼屏', vendor='步步高', model='学习机 S10',
      domain='平板', st='released', date='2026-08-27', lvl='D', stars=3,
      sig='开售', srcn='1 个印证源',
      url='https://www.ithome.com/0/994/893.htm', sname='IT之家（商家供稿）',
      params='14.2 英寸 2328×1600 120Hz 类朗伯光刻护眼屏；骁龙 6 Gen4；8GB；10000mAh；智慧升降双摄；无线磁吸手写笔；6999 元',
      tech=['光刻微纳结构 91% 透光、99% 漫反射', 'DtoF 坐姿与距离双监测', '10000mAh 大电池', '智慧升降双摄', '无线磁吸手写笔'],
      why='教育平板把纳米光刻护眼与 DtoF 坐姿检测做成核心卖点，TCL 学习平板应评估护眼光学加行为传感的组合。',
      rel='学习平板竞争焦点从参数转向护眼光学与用眼行为干预。',
      detail='IT之家（商家供稿），2026-08-27', remark='来源为商家推荐稿，参数需以步步高官方页复核',
      dims=['显示/OLED','手写笔/触控','电池/续航','影像']),

 dict(region='cn', title='台电 ArtPad 上架：13.2 英寸 2.2K 120Hz + 压感手写 1099 元', vendor='台电（Teclast）', model='ArtPad',
      domain='平板', st='released', date='2026-08-21', lvl='C', stars=3,
      sig='上架', srcn='1 个印证源',
      url='https://www.toutiao.com/article/7676388158245732910/', sname='IT之家（今日头条）',
      params='13.2 英寸 2.2K 120Hz 面板，支持 4096 级压感手写；紫光展锐 T7300；8GB+128GB；10000mAh，18W 有线充电；厚 7.5mm；1099 元',
      tech=['13.2 英寸 2.2K 120Hz 大屏', '4096 级压感手写', '10000mAh 大电池', '基于安卓 16 的 ArtOS', '星空灰配色'],
      why='1099 元把 13 英寸 120Hz 大屏与压感手写打包，说明大屏入门平板的价格地板继续下探，TCL 需跟进 BOM 与价位带。',
      rel='大屏入门平板的价格与手写能力同步下探。',
      detail='IT之家（今日头条），2026-08-21', remark='与台电 P50 同品牌但不同尺寸产品线；屏幕材质与亮度官方未公布',
      dims=['显示/OLED','手写笔/触控','电池/续航']),

 dict(region='cn', title='小度 AI 手表 Fit 开售：198 元接入文心大模型', vendor='百度（小度）', model='小度 AI 智能手表 Fit',
      domain='智能手表', st='released', date='2026-07-27', lvl='C', stars=3,
      sig='开售', srcn='2 个印证源（IT之家、IT168）',
      url='https://www.toutiao.com/article/7667191810216690218', sname='IT之家（今日头条）',
      params='1.95 英寸 320×386 IPS 弧面玻璃；8.8mm/42g；300mAh，常规 5 天、极限 7 天；100+ 运动模式；198 元，国补 159.8 元',
      tech=['接入文心大模型语音问答', 'AI 生成个性化表盘', '24 小时情绪/压力/心率/血氧监测', '100+ 运动模式', '金属质感中框与表冠'],
      why='200 元内把手表做成大模型语音入口，说明端侧 AI 助手成本门槛极低，TCL IoT 配件应评估大模型下沉路径。',
      rel='大模型能力正快速向百元级穿戴渗透。',
      detail='IT之家、IT168，2026-07-27', remark='是否支持 NFC 与离线支付未确认',
      dims=['AI/NPU','显示/OLED','电池/续航']),

 dict(region='cn', title='台电 2026 款 P50 平板上市：11 英寸 90Hz + 8000mAh 749 元', vendor='台电（Teclast）', model='P50 2026 款',
      domain='平板', st='released', date='2026-07-20', lvl='C', stars=3,
      sig='上市', srcn='1 个印证源',
      url='https://www.ithome.com/0/979/045.htm', sname='IT之家',
      params='11 英寸 1280×800 90Hz IPS LCD；紫光展锐 T7250；6GB LPDDR4 + 128GB；8000mAh；金属机身 8mm/525g；749 元',
      tech=['11 英寸 90Hz 入门高刷屏', '8000mAh 电池支持双 4G', '金属一体化机身 8mm/525g', '前置 5MP、后置 13MP', '出厂安卓 16'],
      why='749 元档下放 90Hz 与 8000mAh，入门平板配置底线被抬高，TCL 入门平板需重估刷新率与电池基线。',
      rel='千元以下平板正被 90Hz 高刷与大电池重新定义。',
      detail='IT之家，2026-07-20', remark='快充功率、扬声器与屏幕亮度官方未公布，待印证',
      dims=['显示/OLED','SoC/芯片','电池/续航']),

 dict(region='cn', title='Cleer 鹊桥开放式耳机上市：内嵌 AI 智能体 1199 元', vendor='Cleer', model='Bridge（鹊桥）',
      domain='AI耳机·耳穿戴', st='released', date='2026-07-16', lvl='C', stars=4,
      sig='上市', srcn='1 个印证源',
      url='https://www.toutiao.com/article/7663034066187207204', sname='IT之家（今日头条）',
      params='单耳 7.8g，IPX5；12mm 动圈单元；杜比音效 + Cleer DBE 5.0 动态低音；双源拾音通话架构；单耳 7 小时、综合 23 小时；1199 元',
      tech=['人体工学「鹊桥弧」设计', '内置 AI 智能体支持翻译与语音转写', '12mm 动圈 + 杜比音效', '双源拾音架构通话降噪', 'IPX5 防水'],
      why='开放式耳机内嵌 AI 智能体做实时翻译与转写，是耳穿戴 AI 化的落地样本，TCL 音频配件可评估端侧 AI 与开放式形态组合。',
      rel='开放式耳机正成为 AI 语音与翻译的高频入口。',
      detail='IT之家（今日头条），2026-07-16', remark='芯片型号与蓝牙版本官方未披露',
      dims=['音频/扬声器','AI/NPU']),

 # ---------------- 国际 ----------------
 dict(region='intl', title='苹果首款折叠屏 iPhone Duo 发布：1999 美元起', vendor='Apple', model='iPhone Duo',
      domain='手机', st='coming', date='2026-09-10', lvl='C', stars=5,
      sig='发布会', srcn='2 个印证源（太平洋科技、苹果官网）',
      url='https://news.pconline.com.cn/2181/21818082.html', sname='太平洋科技',
      params='7.6 英寸内屏 2670×1878（屏下前摄）+ 5.4 英寸外屏，均 3000nit；A20 Pro；自研 C2 基带；纯 eSIM；侧边指纹；256GB 起 1999 美元，国行 15999 元起',
      tech=['100+ 零件可变扭矩铰链', '大尺寸 VC 均热板，持续性能 +35%', '自研 C2 基带（速率 +50%、功耗 -15%）', '纯 eSIM 设计，取消实体卡槽', '48MP 主摄 + 48MP 融合式超广角'],
      why='苹果入场把折叠屏从「形态尝鲜」推向主流，铰链、UTG、散热与双电池叠构将成为平板/折叠品类共同技术底座。',
      rel='折叠形态的铰链与散热方案可直接迁移至折叠平板预研。',
      detail='太平洋科技，2026-09-10，苹果秋季发布会', remark='10 月 16 日预售、10 月 23 日发售；国行价格已公布',
      dims=['折叠屏','散热/液冷','SoC/芯片']),

 dict(region='intl', title='Blackview Xplore 6 三防机 IFA 首发：12000mAh + 增距镜', vendor='Blackview', model='Xplore 6',
      domain='手机', st='coming', date='2026-09-06', lvl='B', stars=4,
      sig='IFA 首发', srcn='1 个印证源',
      url='https://www.notebookcheck.net/This-rugged-phone-with-secondary-display-and-huge-battery-uses-a-tele-extender-for-10x-optical-zoom.1390927.0.html', sname='Notebookcheck',
      params='6.73 英寸 3200×1440 AMOLED 120Hz + 1.47 英寸背屏 368×194；天玑 9400+；18GB+1TB；12000mAh/120W 有线 + 80W 无线；428g/18.2mm；约 950 欧元',
      tech=['3.33x 外接增距镜把 3x 长焦变 10x 光变（等效 230mm）', '50MP OV50H 主摄 OIS', '背屏可作取景器与媒体控制', 'MIL-STD-810H / IP68 / IP69K', '3 年 Android 更新'],
      why='12000mAh 大电池 + 80W 无线充进入三防机，大电池与高功率无线充的堆叠/散热是平板可直接借鉴的工程样本。',
      rel='大电池 + 高功率无线充的热管理与机身厚度权衡。',
      detail='Notebookcheck，2026-09-06，IFA 2026 现场体验', remark='欧洲 9 月底开售，套装含增距镜；价格含耳机与充电座',
      dims=['电池/续航','快充/无线充','影像']),

 dict(region='intl', title='GOSIGHT P1 全彩 AR 眼镜：热插拔电池架构 + 69g', vendor='GOSIGHT', model='P1',
      domain='AR-VR眼镜', st='coming', date='2026-09-04', lvl='B', stars=4,
      sig='IFA 首发', srcn='1 个印证源（GLOBE NEWSWIRE 厂商稿）',
      url='https://www.tmcnet.com/news/2026/09/04/10440523.htm', sname='TMCnet（GLOBE NEWSWIRE）',
      params='双目 0.3 英寸全彩 Micro-OLED + 阵列波导；6 米等效 105 英寸虚拟屏，60Hz；约 69g；透光率 >85%；12MP 相机；内部桥接电池 + 可换外置电池',
      tech=['内桥接电池 + 可热插拔外置电池，换电不断电', '双目全彩 Micro-OLED + 阵列波导光学', '等效 6 米 105 英寸虚拟屏，60Hz 自动亮度', '透光率 >85%，抑制彩虹纹与外漏光', '硬件联动指示灯，被遮挡即停拍'],
      why='用「可换电不断电」解决全彩 AR 的续航中断，是把 AR 从演示推向连续可用的架构级解法，值得 TCL 跟踪其电池模块化思路。',
      rel='模块化供电可能成为 AR 眼镜连续佩戴的必要条件。',
      detail='GLOBE NEWSWIRE / TMCnet，2026-09-04，IFA Berlin 2026 首发', remark='众筹时间、最终规格与售价尚未公布；69g 为目标值',
      dims=['AR/VR显示','电池/续航','影像']),

 dict(region='intl', title='台电 T60 Mini 日本亮相：8.8 英寸 2.5K + 324g', vendor='Teclast（台电）', model='T60 Mini',
      domain='平板', st='coming', date='2026-09-02', lvl='C', stars=3,
      sig='海外上市预告', srcn='1 个印证源',
      url='https://tech.sina.cn/2026-09-02/detail-iniqmmyw1306473.d.html', sname='新浪科技（IT之家）',
      params='8.8 英寸 2560×1600 90Hz；紫光展锐 T7300 6nm 八核 2.2GHz，安兔兔超 65 万；8GB+128GB；6000mAh/18W PD；约 8mm/324g；Android 17',
      tech=['双卡双待 4G LTE', 'Wi-Fi 6 + 蓝牙 5.4', 'microSD 扩展', '13MP 后摄 / 5MP 前摄', '9 月日本上市'],
      why='8.8 英寸小尺寸平板在日本重新活跃，324g 轻量化 + LTE 是通勤与车载场景的差异化切口。',
      rel='小尺寸平板（8~9 英寸）在海外仍有明确需求窗口。',
      detail='新浪科技（IT之家），2026-09-02', remark='日本以外市场与价格未公布',
      dims=['显示/OLED','SoC/芯片','5G/通信']),

 dict(region='intl', title='Zens 折叠三合一磁吸无线充发布：Qi2.2 25W 附 65W 适配器', vendor='Zens（荷兰）', model='Fold Charger Pro 3',
      domain='无线充', st='coming', date='2026-09-01', lvl='A', stars=4,
      sig='官方发布', srcn='1 个印证源',
      url='https://zens.tech/blogs/news/zens-makes-25w-wireless-charging-more-flexible-with-new-foldable-chargers', sname='Zens 官方',
      params='Qi2.2 认证折叠三合一磁吸无线充：iPhone 最高 25W、Apple Watch 与 AirPods 各 5W；充电面可展开支持横竖屏；随附 65W USB-C PD 适配器；€129.99',
      tech=['Qi2.2 认证磁吸面，最高 25W', '手机 + 手表 + 耳机三设备同充', '折叠展开面，横竖屏可用', '随机附送 65W USB-C PD 适配器', '折叠后扁平收纳便于差旅'],
      why='国际品牌把「折叠 + 附送 65W 适配器」做成标准配置，磁吸无线充竞争点已从功率转向形态与配套完整度。',
      rel='平板若引入磁吸无线充，配件包应含足额适配器以兑现标称功率。',
      detail='Zens 官方新闻，2026-09-01，官网开启预订', remark='目前仅欧洲定价，其他市场时间未定',
      dims=['快充/无线充','材质/工艺']),

 dict(region='intl', title='viaim Rise AI 耳机 Indiegogo 众筹：AI Agent + 同轴双驱', vendor='viaim', model='Rise',
      domain='AI耳机·耳穿戴', st='progress', date='2026-09-07', lvl='C', stars=4,
      sig='众筹', srcn='1 个印证源（Indiegogo 项目页）',
      url='https://www.notebookcheck.net/viaim-Rise-earbuds-launch-on-Indiegogo-with-AI-agent-and-coaxial-dual-drivers.1392363.0.html', sname='Notebookcheck',
      params='11mm 低音 + 6mm 高音同轴双驱，20Hz-40kHz；SBC/AAC/LDAC；每耳 3 麦 + 1 骨传导 VPU，充电盒另含 3 麦阵列；IP55；259 美元早鸟（MSRP 399）',
      tech=['「听-想-做」AI Agent，可对接 ChatGPT/Claude/Gemini 生成草稿与任务', '盒内 3 麦阵列做环境拾音', '11 月 OTA：盒体 Type-C 直连 PC 当外置麦', '蓝牙 6.1 双设备多点', 'IFA 2026 Best in Audio 获奖'],
      why='把耳机从「转写工具」升级为「可执行动作的 AI Agent」，充电盒兼作 PC 麦克风是硬件形态的实用创新。',
      rel='音频配件的 AI 化正在从转写走向任务执行闭环。',
      detail='Notebookcheck，2026-09-07，IFA 2026 报道', remark='续航 6 小时（关 ANC）/总计 25 小时；支持 MagSafe 无线充',
      dims=['AI/NPU','音频/扬声器','电池/续航']),

 dict(region='intl', title='HP OmniBook 5 16 换装 Wildcat Lake：1100nit OLED 可选', vendor='HP', model='OmniBook 5 16',
      domain='笔记本电脑', st='released', date='2026-09-09', lvl='B', stars=3,
      sig='上市', srcn='1 个印证源（HP 美国官网）',
      url='https://www.notebookcheck.net/HP-releases-new-16-inch-laptop-with-1-100-nit-OLED-32-GB-RAM-and-Intel-Wildcat-Lake.1395010.0.html', sname='Notebookcheck',
      params='16 英寸可选 1800p 120Hz OLED（500nit SDR / 1100nit HDR）；Core 5 320 / Core 7 350；最高 32GB + 1TB PCIe Gen5；68Wh；1199.99 美元起，顶配 1959 美元',
      tech=['1100nit HDR OLED 选项', '可选蓝牙 6 + Wi-Fi 7 模块', 'PCIe Gen5 SSD', '32GB 内存仅绑定 Core 5 320', '三种配色'],
      why='同模具换更低阶平台做价差，是 SKU 分层与屏幕规格解耦的典型打法，可平移到平板产品线规划。',
      rel='同一 ID 下用 SoC/屏幕分级覆盖不同价格带。',
      detail='Notebookcheck，2026-09-09，HP 美国官网上架', remark='与 Panther Lake 版同模具，属同系列不同配置',
      dims=['显示/OLED','SoC/芯片','Wi-Fi/连接']),

 dict(region='intl', title='Huion Kamvas Pad 12 开售：EMR 无源笔 + 16384 压感 499 美元', vendor='Huion（绘王）', model='Kamvas Pad 12',
      domain='平板', st='released', date='2026-09-08', lvl='B', stars=4,
      sig='开售', srcn='2 个印证源（TechPowerUp、Huion 官网）',
      url='https://www.notebookcheck.net/New-premium-tablet-arrives-with-2-4K-display-and-impressive-pen-capabilities.1392302.0.html', sname='Notebookcheck',
      params='12.2 英寸全贴合 2400×1600 90Hz，350nit，99% sRGB；联发科 Genio 720 6nm；8GB+256GB；8000mAh；665g/7.8mm；499 美元',
      tech=['EMR 无源笔 PW600C 免充电', '16384 级压感 + 60° 倾斜识别', '5800 LPI、260 PPS 采样', '四扬声器', 'microSD 扩展'],
      why='EMR 无源笔 + 16384 压感下放到 499 美元 Android 平板，是无源电磁阵营对主动电容笔的正面挑战。',
      rel='TCL 平板若走教育/手写路线，需评估 EMR 与主动笔的成本与延迟取舍。',
      detail='Notebookcheck，2026-09-08，援引 TechPowerUp 与 Huion 官网', remark='无',
      dims=['手写笔/触控','显示/OLED','SoC/芯片']),

 dict(region='intl', title='Redmi Watch 6 Lite 欧洲开售：69 欧元配独立 GPS', vendor='Xiaomi', model='Redmi Watch 6 Lite',
      domain='智能手表', st='released', date='2026-09-08', lvl='B', stars=3,
      sig='开售', srcn='1 个印证源',
      url='https://www.notebookcheck.net/Redmi-Watch-6-Lite-launches-in-Europe-with-a-1-96-inch-AMOLED-display-and-18-day-battery-life.1393257.0.html', sname='Notebookcheck',
      params='1.96 英寸 AMOLED，峰值 1500nit；内置 GPS；150+ 运动模式；18 天续航（重度 6 天）；5ATM；欧元区 69 欧元 / 英国 59 英镑',
      tech=['1500nit 高亮 AMOLED', '独立 GNSS 定位', '蓝牙通话（Android/iOS）', '5ATM 防水', '黑/钢灰两色'],
      why='69 欧元档段已标配独立 GPS + 1500nit 屏，入门穿戴的屏幕亮度与定位基准被再次抬高。',
      rel='穿戴与平板在「户外可读亮度」上的屏幕规格趋同。',
      detail='Notebookcheck，2026-09-08', remark='此前已在波兰、东南亚等市场上架',
      dims=['显示/OLED','电池/续航']),

 dict(region='intl', title='Rogbid Model R3T 手表：190° 弹出摄像头 + 4G LTE 99.99 美元', vendor='Rogbid', model='Model R3T',
      domain='智能手表', st='released', date='2026-09-02', lvl='B', stars=3,
      sig='上市', srcn='1 个印证源（Rogbid 官方商店）',
      url='https://www.notebookcheck.net/Rogbid-Model-R3T-smartwatch-launches-with-a-pop-up-camera-and-4G-LTE-support.1385720.0.html', sname='Notebookcheck',
      params='1.6 英寸 480×480 AMOLED（Panda Glass）；Unisoc SL8541E；3GB+32GB；1100mAh；47mm 316 不锈钢 / IP67；99.99 美元',
      tech=['190° 旋转弹出摄像头', '独立 4G LTE 通话上网', '多系统 GNSS + 指南针', '红外遥控（5 米）', '支持第三方 App 安装'],
      why='百美元档实现「独立通信 + 摄像头」的完整形态，验证了超低成本穿戴 SoC + 小尺寸模组的可行性。',
      rel='独立 LTE 能力正在向 100 美元以下穿戴渗透。',
      detail='Notebookcheck，2026-09-02，Rogbid 官方商店同步上架', remark='摄像头像素官方未标注',
      dims=['5G/通信','材质/工艺','影像']),

 dict(region='intl', title='Rokid 乐奇 AI+AR 眼镜澳洲上市：49g 双目 Micro-LED 波导', vendor='Rokid', model='Rokid Glasses（乐奇 / RV101）',
      domain='AR-VR眼镜', st='released', date='2026-09-02', lvl='B', stars=4,
      sig='海外上市', srcn='2 个印证源（iTWire、Rokid 澳洲官网）',
      url='https://www.tomsguide.com/computing/smart-glasses/i-tried-rokids-ai-ar-glasses-for-a-month-and-the-general-bad-vibes-i-have-around-wearables-are-slowly-subsiding-but-i-cant-stop-worrying-about-my-personal-data', sname="Tom's Guide",
      params='49g；双目单色 Micro-LED 波导，约 30° FOV、最高 1500nit；骁龙 AR1 Gen 1 + 2GB/32GB；12MP IMX681（1680p 视频）；210mAh；AU$999',
      tech=['89 语实时翻译 + 实时字幕', '声控提词器（可跟语速滚动）', 'AR 导航（Google Maps 联动）', '磁吸处方镜片', '开放耳双扬 + 四麦阵列'],
      why='双 Micro-LED 波导把「信息提示 + 翻译字幕」做成日常可用形态，49g 是当前带显示眼镜的量产重量基准。',
      rel='Micro-LED + 波导是 AR 眼镜轻量化与户外可读性的主流组合。',
      detail="Tom's Guide，2026-09-02，一个月长测", remark='摄像与视频画质是主要短板；评测同时提出数据隐私担忧',
      dims=['AR/VR显示','AI/NPU','音频/扬声器']),

 dict(region='intl', title='索尼 ULT TOWER 7 派对音箱发布：420W + Auracast 百台串联', vendor='Sony', model='ULT TOWER 7',
      domain='智能音箱', st='coming', date='2026-09-02', lvl='A', stars=4,
      sig='官方发布', srcn='2 个印证源（索尼日本官方稿、ThePCEnthusiast）',
      url='https://www.sony.jp/CorporateCruise/Press/202609/26-0902', sname='索尼日本官方新闻稿',
      params='新开发 280mm 圆形低音单元 + 2 中音 + 4 高音；最大输出 420W；内置电池约 30 小时；IPX4（竖置）；约 22.8kg；日本 9 月 18 日上市，市场预估约 85000 日元',
      tech=['360° 派对音效', '音场最適化（按噪声/摆放/横竖置自动补正）', 'Party Chain 经 Auracast 最多无线串联 100 台', '新增 XLR/RCA/USB-C 输入', 'ULT1/ULT2/FLAT/LIVE 四种音效模式'],
      why='用 Auracast 做 100 台同步，把多设备低延迟组网的边界推到消费级；音场自动补正的思路可直接用于平板多扬声器校准。',
      rel='Auracast 广播音频将成为多设备同步音频的通用底座。',
      detail='索尼日本官方新闻稿，2026-09-02', remark='本体塑料约 20% 为再生塑料；同系列还有 Tower Max / Tower 5',
      dims=['音频/扬声器','Wi-Fi/连接','可持续/模块化']),

 dict(region='intl', title='努比亚 Pad Plus Wi-Fi 版日本上市：249 美元支持 Type-C 视频输出', vendor='Nubia（中兴）', model='Pad Plus（Wi-Fi）',
      domain='平板', st='released', date='2026-08-27', lvl='B', stars=3,
      sig='海外上市', srcn='2 个印证源（Notebookcheck 中文版）',
      url='https://www.notebookcheck.net/Nubia-launches-Android-tablet-for-249-with-12-inch-display-Widevine-L1-and-USB-C-video-output.1380263.0.html', sname='Notebookcheck',
      params='12 英寸 2000×1200 90Hz IPS；Unisoc T820（T9100）6nm；6GB+128GB；8000mAh/26W；550g/7.2mm；39800 日元（约 249 美元）',
      tech=['USB-C 支持视频输出', 'Widevine L1 认证', '四扬声器', '可选带触控板键盘 9800 日元', 'IPX2 防水'],
      why='249 美元档首次把「USB-C 视频输出」做成卖点，是平板外接显示器/投屏场景的低成本方案。',
      rel='入门平板用 Type-C 直连显示器补齐生产力短板。',
      detail='Notebookcheck，2026-08-27', remark='包装不含充电头',
      dims=['显示/OLED','SoC/芯片','电池/续航']),

 dict(region='intl', title='Infinix Xpad 30 Pro 海外上市：2.5K 90Hz + 2TB 扩展 227 美元', vendor='Infinix（传音）', model='Xpad 30 Pro',
      domain='平板', st='released', date='2026-08-23', lvl='B', stars=3,
      sig='海外上市', srcn='2 个印证源（Notebookcheck、GSMArena 规格库）',
      url='https://www.notebookcheck.net/Affordable-Infinix-tablet-launches-with-11-inch-display-and-2TB-storage-support.1376140.0.html', sname='Notebookcheck',
      params='11 英寸 1600×2560 90Hz IGZO，峰值 550nit；Helio G200 Ultimate；最高 8GB+256GB；8200mAh/18W；菲律宾 12/128GB 约 227 美元',
      tech=['2TB microSD 扩展', '旁路供电 + 游戏模式', '4G SIM 版本可选', '兼容 X Pencil 20 与 X KeyBoard 11', '桌面扩展模式'],
      why='200 美元档已配 2.5K 90Hz + 8200mAh + 手写笔键盘生态，TCL 入门平板需重估屏幕与配件捆绑策略。',
      rel='低价平板的「屏 + 笔 + 键盘」全套生产力组合正下探至 227 美元。',
      detail='Notebookcheck，2026-08-23', remark='国内未上市；各区域 8GB/12GB 内存说法不一',
      dims=['显示/OLED','SoC/芯片','手写笔/触控']),

 dict(region='intl', title='Acer Swift Edge 14 国际开售：990g 塞入 65Wh + 120Hz OLED', vendor='Acer', model='Swift Edge 14（2026）',
      domain='笔记本电脑', st='released', date='2026-08-21', lvl='B', stars=4,
      sig='国际开售', srcn='1 个印证源（Acer 官方商店）',
      url='https://www.notebookcheck.net/Acer-releases-new-lightweight-14-inch-laptop-internationally-with-120-Hz-OLED-Intel-Panther-Lake-and-32-GB-RAM.1374369.0.html', sname='Notebookcheck',
      params='14 英寸 1800p 120Hz OLED，500nit；Panther Lake Core Ultra 5 325 / Ultra 7 355；最高 32GB + 1TB；65Wh；990g；捷克/德国/香港/新马/瑞士/UAE 已上架',
      tech=['990g 14 英寸 OLED 机身', '120Hz 500nit OLED', '32GB 内存配置', '65Wh 电池', '顶配 €1439 / MYR 6999'],
      why='990g 内塞入 65Wh + 120Hz OLED，轻薄本的「重量—电池—屏幕」三角基准被刷新，直接对标大屏平板的便携性上限。',
      rel='轻薄本 1kg 门槛内的散热与续航方案可供高端平板参考。',
      detail='Notebookcheck，2026-08-21', remark='零售版本暂无 CES 上宣称的 Core Ultra 9 386H',
      dims=['显示/OLED','SoC/芯片','电池/续航']),
]

DIMS = ['SoC/芯片','显示/OLED','折叠屏','手写笔/触控','散热/液冷','电池/续航','快充/无线充','影像',
        'AI/NPU','音频/扬声器','5G/通信','Wi-Fi/连接','AR/VR显示','材质/工艺','可持续/模块化','手柄/外设']
STATUS_TXT = {'coming': '即将上市', 'progress': '进行中', 'released': '已上市'}
STATUS_CLS = {'coming': 'status-coming', 'progress': 'status-progress', 'released': 'status-released'}
STATUS_ORD = {'coming': 0, 'progress': 1, 'released': 2}
LVL_ORD = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


def stars_html(n):
    return '★' * n + '☆' * (5 - n)


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;').replace("'", '&#x27;'))


# ---------- 排序：区域内按状态分组，同状态时间倒序 ----------
def sort_key(c):
    d = c['date']
    day = int(d[8:10]) if len(d) >= 10 else 1
    return (STATUS_ORD[c['st']], -day)


cn = sorted([c for c in C if c['region'] == 'cn'], key=sort_key)
intl = sorted([c for c in C if c['region'] == 'intl'], key=sort_key)
ordered = cn + intl
for i, c in enumerate(ordered, 1):
    c['num'] = i

assert len(cn) == 15 and len(intl) == 15, (len(cn), len(intl))

# ---------- 统计 ----------
dim_count = {d: 0 for d in DIMS}
for c in C:
    for d in c['dims']:
        dim_count[d] += 1
lvl_count = {k: 0 for k in 'ABCDE'}
for c in C:
    lvl_count[c['lvl']] += 1
five = sum(1 for c in C if c['stars'] == 5)
liton = sum(1 for d in DIMS if dim_count[d] > 0)

# ---------- Top5：A级优先→星级降序→状态优先→时间倒序 ----------
def top_key(c):
    d = c['date']
    day = int(d[8:10]) if len(d) >= 10 else 1
    return (LVL_ORD[c['lvl']], -c['stars'], STATUS_ORD[c['st']], -day)


top5 = sorted(C, key=top_key)[:5]

# ---------- 读模板 ----------
s = open(TPL, encoding='utf-8').read()
head = s[:s.find('<div class="dim-panel">')]
tail = s[s.find('<script'):]

# ---------- 拼装 ----------
parts = [head]
parts.append('  <div class="dim-panel">\n')
parts.append('    <div class="dim-header">\n')
parts.append('      <div class="dim-title">技术维度覆盖面板</div>\n')
parts.append('      <div class="dim-counter"><span class="dim-num">%d</span><span class="dim-total"> / 16 维度</span></div>\n' % liton)
parts.append('    </div>\n')
parts.append('    <div class="dim-bar"><div class="dim-bar-fill" style="width:%d%%"></div></div>\n' % round(liton * 100 / 16))
parts.append('    <div class="dim-grid">\n')
for d in DIMS:
    n = dim_count[d]
    cls = 'dim-chip on' if n else 'dim-chip off'
    parts.append('      <div class="%s">%s <span class="dim-count">%d条</span></div>\n' % (cls, d, n))
parts.append('    </div>\n  </div>\n')

parts.append('  <div class="top-signals-panel">\n')
parts.append('    <div class="top-signals-header">\n')
parts.append('      <div class="top-signals-title">今日重点信号 Top 5</div>\n')
parts.append('      <div style="font-size:12px;color:var(--text-tertiary);">排序：A级优先→星级降序→状态优先→时间倒序</div>\n')
parts.append('    </div>\n    <div class="top-signals-grid">\n')
for i, c in enumerate(top5, 1):
    parts.append('      <div class="signal-card">\n')
    parts.append('        <div><span class="sig-rank">%d</span><span class="sig-title">%s</span></div>\n' % (i, esc(c['title'])))
    parts.append('        <div class="sig-tags"><span class="sig-dim">%s</span><span class="sig-stars">%s</span></div>\n' % (c['domain'], stars_html(c['stars'])))
    parts.append('        <div class="sig-key">%s级 / %s</div>\n' % (c['lvl'], esc(c['params'][:110])))
    parts.append('      </div>\n')
parts.append('    </div>\n  </div>\n')

parts.append('  <div class="summary-section">\n    <div class="section-title">情报摘要表</div>\n')
parts.append('    <table>\n      <thead><tr><th>#</th><th>标题</th><th>区域</th><th>类别</th><th>信源</th><th>状态</th><th>时间</th></tr></thead>\n      <tbody>\n')
for c in ordered:
    reg = '国内' if c['region'] == 'cn' else '国际'
    regcls = 'region-cn' if c['region'] == 'cn' else 'region-intl'
    parts.append('      <tr>\n        <td>%d</td>\n' % c['num'])
    parts.append('        <td class="td-title"><a href="#card-%d">%s</a></td>\n' % (c['num'], esc(c['title'])))
    parts.append('        <td><span class="td-region %s">%s</span></td>\n' % (regcls, reg))
    parts.append('        <td>%s</td>\n' % c['domain'])
    parts.append('        <td><span class="source-tag source-%s">%s</span></td>\n' % (c['lvl'].lower(), c['lvl']))
    parts.append('        <td class="td-status"><span class="status-tag %s">%s</span></td>\n' % (STATUS_CLS[c['st']], STATUS_TXT[c['st']]))
    parts.append('        <td>%s</td>\n      </tr>\n' % c['date'])
parts.append('      </tbody>\n    </table>\n  </div>\n')

for reg, label, items in (('cn', '国内情报（15 条）', cn), ('intl', '国际情报（15 条）', intl)):
    parts.append('  <div class="intel-section">\n')
    parts.append('    <div class="section-title">%s</div>\n' % label)
    parts.append('    <div class="intel-cards">\n')
    for c in items:
        n = c['num']
        exp = ' expanded' if n == 1 else ''
        parts.append('      <div class="intel-card %s%s" id="card-%d">\n' % (c['region'], exp, n))
        parts.append('        <div class="card-header" onclick="toggleCard(this)">\n')
        parts.append('          <div class="card-num">%d</div>\n' % n)
        parts.append('          <div class="card-title-area">\n')
        parts.append('            <div class="card-title">%s</div>\n' % esc(c['title']))
        parts.append('            <div class="card-badges">\n')
        parts.append('              <span class="stars">%s</span>\n' % stars_html(c['stars']))
        parts.append('              <span class="source-tag source-%s">%s</span>\n' % (c['lvl'].lower(), c['lvl']))
        parts.append('              <span class="status-tag %s">%s</span>\n' % (STATUS_CLS[c['st']], STATUS_TXT[c['st']]))
        parts.append('              <span class="card-domain">%s</span>\n' % c['domain'])
        parts.append('            </div>\n          </div>\n')
        parts.append('          <div class="card-toggle">▼</div>\n        </div>\n')
        parts.append('        <div class="card-body">\n')
        parts.append('          <div class="card-content">\n            <div class="field-grid">\n')
        parts.append('              <div class="field"><div class="field-label">信号类型</div><div class="field-value">%s</div></div>\n' % esc(c['sig']))
        parts.append('              <div class="field"><div class="field-label">印证源数</div><div class="field-value">%s</div></div>\n' % esc(c['srcn']))
        parts.append('              <div class="field full"><div class="field-label">关键参数</div><div class="field-value">%s</div></div>\n' % esc(c['params']))
        parts.append('              <div class="field full"><div class="field-label">技术特性</div><div class="field-value"><ul class="tech-list">\n')
        for j, t in enumerate(c['tech'], 1):
            parts.append('        <li data-num="%d">%s</li>\n' % (j, esc(t)))
        parts.append('      </ul></div></div>\n')
        parts.append('              <div class="field full"><div class="field-label">为什么重要</div><div class="field-value">%s</div></div>\n' % esc(c['why']))
        parts.append('              <div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">%s</div></div>\n' % esc(c['rel']))
        parts.append('              <div class="field"><div class="field-label">厂商</div><div class="field-value">%s</div></div>\n' % esc(c['vendor']))
        parts.append('              <div class="field"><div class="field-label">型号</div><div class="field-value">%s</div></div>\n' % esc(c['model']))
        parts.append('              <div class="field"><div class="field-label">时间</div><div class="field-value">%s</div></div>\n' % c['date'])
        parts.append('              <div class="field"><div class="field-label">来源URL</div><div class="field-value"><a href="%s" target="_blank">%s</a></div></div>\n' % (c['url'], esc(c['sname'])))
        parts.append('              <div class="field full"><div class="field-label">信源明细</div><div class="field-value">%s</div></div>\n' % esc(c['detail']))
        parts.append('              <div class="field full"><div class="field-label">备注/待印证</div><div class="field-value">%s</div></div>\n' % esc(c['remark']))
        parts.append('            </div>\n          </div>\n        </div>\n      </div>\n')
    parts.append('    </div>\n  </div>\n')

parts.append(tail)
html = ''.join(parts)

# ---------- 头部日期/统计替换 ----------
html = re.sub(r'智能终端硬件情报日报 · \d{4}-\d{2}-\d{2}（?(周[一二三四五六日])?）?',
              '智能终端硬件情报日报 · %s（%s）' % (DATE, WEEK), html)
html = html.replace('<span class="meta-badge">信源 A-E级</span>', '<span class="meta-badge">信源 A-E级</span>')
m = re.search(r'(<div class="stat-item"><div class="stat-num">)(\d+)(</div><div class="stat-label">A级信源</div>)', html)
html = html[:m.start(2)] + str(lvl_count['A']) + html[m.end(2):]
m = re.search(r'(<div class="stat-item"><div class="stat-num">)(\d+)(</div><div class="stat-label">B级信源</div>)', html)
html = html[:m.start(2)] + str(lvl_count['B']) + html[m.end(2):]
m = re.search(r'(<div class="stat-item"><div class="stat-num">)(\d+)(</div><div class="stat-label">五星条数</div>)', html)
html = html[:m.start(2)] + str(five) + html[m.end(2):]

open(OUT, 'w', encoding='utf-8').write(html)
print('OK', OUT, len(html), 'bytes | A%d B%d C%d D%d E%d | 五星%d | 维度%d/16 | 国内%d 国际%d'
      % (lvl_count['A'], lvl_count['B'], lvl_count['C'], lvl_count['D'], lvl_count['E'], five, liton, len(cn), len(intl)))
