# -*- coding: utf-8 -*-
"""Generate remaining HTML cards 12-15 (domestic) + cards 16-30 (international) and append to file."""

filepath = r"E:\AI相关\预研究\202608\03_输出\WB_tmp.html"

cn = ['①','②','③','④','⑤','⑥','⑦','⑧','⑨','⑩']

def card(seq, title, source, domain, stars, status, is_cn,
         sig, conf, params, techs, why, rel, vendor, time_val, url, url_text, src_det, notes):
    cls = "cn" if is_cn else "intl"
    sc = {"已上市":"status-released","即将上市":"status-coming","进行中":"status-coming"}.get(status,"status-coming")
    tl = "".join(f'<li data-num="{cn[i]}">{t}</li>' for i,t in enumerate(techs))
    return f"""
      <!-- Card {seq}: {title.split(" — ")[0]} -->
      <div class="intel-card {cls}" id="card-{seq}">
        <div class="card-header" onclick="toggleCard('card-{seq}')">
          <div class="card-num">{seq}</div>
          <div class="card-title-area">
            <div class="card-title">{title}</div>
            <div class="card-badges">
              <span class="source-tag source-{source.lower()}">{source}</span>
              <span class="card-domain">{domain}</span>
              <span class="stars">{stars}</span>
              <span class="status-tag {sc}">{status}</span>
            </div>
          </div>
          <span class="card-toggle">&#9660;</span>
        </div>
        <div class="card-body">
          <div class="card-content">
            <div class="field-grid">
              <div class="field"><div class="field-label">信号类型</div><div class="field-value">{sig}</div></div>
              <div class="field"><div class="field-label">印证源数</div><div class="field-value">{conf}</div></div>
              <div class="field full"><div class="field-label">关键参数</div><div class="field-value">{params}</div></div>
              <div class="field full"><div class="field-label">技术特性</div><div class="field-value"><ul class="tech-list">{tl}</ul></div></div>
              <div class="field full"><div class="field-label">为什么重要</div><div class="field-value">{why}</div></div>
              <div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">{rel}</div></div>
              <div class="field"><div class="field-label">厂商/型号</div><div class="field-value">{vendor}</div></div>
              <div class="field"><div class="field-label">时间</div><div class="field-value">{time_val}</div></div>
              <div class="field"><div class="field-label">URL</div><div class="field-value"><a href="{url}" target="_blank">{url_text}</a></div></div>
              <div class="field"><div class="field-label">信源明细</div><div class="field-value">{src_det}</div></div>
              <div class="field full"><div class="field-label">备注待印证</div><div class="field-value">{notes}</div></div>
            </div>
          </div>
        </div>
      </div>"""

# Card 12 remaining fields (complete from 智能终端关联点)
c12_rest = """              <div class="field full"><div class="field-label">智能终端关联点</div><div class="field-value">平板Qi2.2磁吸25W无线充2026Q2旗舰标配，千元机下半年下沉；磁吸线圈/主控芯片供应链成本下降</div></div>
              <div class="field"><div class="field-label">厂商/型号</div><div class="field-value">WPC联盟 / 多厂商</div></div>
              <div class="field"><div class="field-label">时间</div><div class="field-value">2026-01</div></div>
              <div class="field"><div class="field-label">URL</div><div class="field-value"><a href="https://www.wpc.org/qi2" target="_blank">WPC官方</a></div></div>
              <div class="field"><div class="field-label">信源明细</div><div class="field-value">WPC官方 (A级)、帕沃思 (B级)</div></div>
              <div class="field full"><div class="field-label">备注待印证</div><div class="field-value">平板Qi2.2支持清单待更新；25W磁吸实际发热控制方案需关注</div></div>
            </div>
          </div>
        </div>
      </div>
"""

# Cards 13-15 (domestic)
c13 = card(13, "天猫精灵Sound Pro — 2.1声道60W+Hi-Res认证智能音箱", "B", "智能音箱/音频", "&#9733;&#9733;&#9733;", "已上市", True,
    "新品发布", "2+（天猫精灵官网、数码评测）",
    "2.1声道独立低音炮 | 60W总功率 | Hi-Res Audio认证 | 液态硅胶低音炮振膜 | Wi-Fi 6+蓝牙5.4 | FLAC/Hi-Res本地播放",
    ["2.1声道设计（独立低音炮+左右声道分离）","60W总输出功率（20W×2+20W低音）","Hi-Res Audio Wireless认证","液态硅胶低音炮振膜（低频下潜至35Hz）","Wi-Fi 6+蓝牙5.4双连接","支持FLAC/WAV/Hi-Res本地无损播放"],
    "智能音箱从语音助手向高品质音频终端演进，SoC音频解码能力成为差异化焦点。",
    "平板与智能音箱的音频协同（多设备音频共享）、SoC音频DSP共享设计思路、液态硅胶振膜材料方案",
    "天猫精灵 / Sound Pro", "2026-06", "https://www.tmallgenie.com", "天猫精灵官网",
    "天猫精灵官网 (B级)、数码评测媒体 (B级)", "具体SoC型号未公布；实际低频表现需对比HomePod")

c14 = card(14, "小米小爱音箱Pro 2026款 — 端侧AI推理+UWB空间感知全屋中枢", "B", "智能音箱/AI-NPU/无线通信", "&#9733;&#9733;&#9733;&#9733;", "已上市", True,
    "新品发布", "2+（小米官网、小米社区）",
    "端侧AI推理 | 自研音频SoC | UWB空间感知 | Matter协议中枢 | 立体声配对 | 6MIC远场阵列",
    ["端侧AI推理引擎（本地运行大模型，离线可用）","自研音频处理SoC（DSP+NPU集成）","UWB空间感知定位（设备自动发现与空间位置感知）","Matter协议智能家居中枢","多设备音频无缝接力（UWB触发）","远场麦克风阵列（6mic）"],
    "智能音箱成为全屋智能中枢，端侧AI降低云依赖，UWB空间感知是新趋势。",
    "平板与音箱的UWB联动设计、端侧AI推理SoC架构参考、Matter协议集成",
    "小米 / 小爱音箱Pro 2026款", "2026-Q2", "https://www.mi.com", "小米官网",
    "小米官网 (A级)、小米社区 (B级)", "端侧AI模型参数量和推理延迟未详细公布")

c15 = card(15, "联想小新Air 2026版 — Core Series 3 NPU 40TOPS+14寸OLED+1.2kg轻薄本", "A", "笔记本/SoC/NPU/显示-OLED", "&#9733;&#9733;&#9733;&#9733;", "已上市", True,
    "新品发布", "2+（联想官网、中关村在线）",
    "Intel Core Series 3(NPU 40 TOPS) | 14英寸2.8K OLED | 1.2kg | Copilot+ PC认证 | 70Wh电池 | 雷电4",
    ["Intel Core Series 3处理器（NPU 40 TOPS，Copilot+ PC认证）","14英寸2.8K OLED屏（100% DCI-P3）","1.2kg超轻机身（镁铝合金）","70Wh电池（15小时续航）","雷电4接口","LPDDR5X内存"],
    "AI PC普及加速，NPU 40 TOPS成为入门门槛，OLED+轻薄化是趋势。",
    "平板与笔记本的SoC NPU共享架构、OLED面板供应链、轻薄结构设计参考",
    "联想 / 小新Air 2026版", "2026-05-29", "https://www.lenovo.com.cn", "联想官网",
    "联想官网 (A级)、中关村在线 (B级)", "Core Series 3 NPU实际性能跑分待验证")

# Close domestic section + open international section
section_close_open = """
    </div>
  </div>

  <!-- International Intelligence -->
  <div class="intel-section">
    <div class="section-title">二、国际情报（15条）</div>
    <div class="intel-cards">
"""

# Cards 16-19
c16 = card(16, "Motorola Moto Pad 70 Pro — Dimensity 8400+12.1寸144Hz+120W快充", "B", "平板/SoC/电池-快充", "&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "2+（gizmochina、phonearena）",
    "联发科Dimensity 8400 | 12.1英寸144Hz LCD | 120W有线快充 | 10000mAh | JBL调音四扬声器",
    ["联发科Dimensity 8400 SoC（台积电4nm）","12.1英寸144Hz LCD（2800x1752）","120W有线快充（0-100%约35分钟）","10000mAh大电池","JBL调音四扬声器","USB 3.2 Gen1"],
    "国际市场平板SoC多元化，联发科在平板领域扩大份额，120W快充+10000mAh组合。",
    "平板SoC选型参考（联发科Dimensity在平板上的性能/功耗表现）、120W快充方案、大电池设计",
    "Motorola / Moto Pad 70 Pro", "2026-06-27", "https://www.gizmochina.com", "gizmochina",
    "gizmochina (B级)、phonearena (B级)", "Dimensity 8400在平板上的散热表现需实测")

c17 = card(17, "Samsung Galaxy Z Fold 8 — 骁龙8 Elite Gen5+钛金属铰链+7.4寸折叠屏", "A", "手机/折叠屏/SoC/结构-工艺", "&#9733;&#9733;&#9733;&#9733;&#9733;", "即将上市", False,
    "即将上市", "3+（Samsung官网、GSMArena、AndroidAuthority）",
    "骁龙8 Elite Gen5 | 7.4英寸内折主屏+6.4英寸外屏 | 钛金属铰链 | 4400mAh | 25W+Qi2 | 200MP主摄",
    ["骁龙8 Elite Gen5（3nm）","7.4英寸QXGA+内折主屏（120Hz LTPO）","6.4英寸外屏","钛金属铰链（Armor Aluminum框架）","4400mAh电池+25W有线+Qi2无线","200MP主摄+12MP超广+10MP长焦"],
    "折叠屏旗舰SoC/铰链/电池方案对标参考，钛金属铰链是结构工艺新趋势。",
    "折叠屏平板的铰链结构设计、SoC选型、电池方案、钛金属工艺",
    "Samsung / Galaxy Z Fold 8", "2026-07-22", "https://www.samsung.com", "Samsung官网",
    "Samsung官网 (A级)、GSMArena (A级)、AndroidAuthority (B级)", "具体定价和发售日期待官宣")

c18 = card(18, "Samsung Galaxy Z Flip 8 — 骁龙8 Elite Gen5+3.2寸外屏竖折+钛金属", "A", "手机/折叠屏/SoC/结构-工艺", "&#9733;&#9733;&#9733;&#9733;", "即将上市", False,
    "即将上市", "3+（Samsung官网、GSMArena、AndroidAuthority）",
    "骁龙8 Elite Gen5 | 3.2英寸外屏 | 6.8英寸内折主屏 | 钛金属铰链 | 3700mAh | 25W+Qi2 | 50MP双摄",
    ["骁龙8 Elite Gen5（3nm）","3.2英寸Super AMOLED外屏","6.8英寸内折主屏","钛金属铰链","3700mAh电池+25W有线+Qi2无线","50MP主摄+12MP超广"],
    "竖折形态差异化，外屏面积持续扩大，钛金属铰链工艺下沉。",
    "折叠屏面板技术、铰链工艺、小体积散热方案",
    "Samsung / Galaxy Z Flip 8", "2026-07-22", "https://www.samsung.com", "Samsung官网",
    "Samsung官网 (A级)、GSMArena (A级)、AndroidAuthority (B级)", "外屏交互APP生态待完善")

c19 = card(19, "Google Pixel 11系列 — Tensor G6自研芯片+Gemini AI端侧+7年更新", "A", "手机/SoC/AI-NPU", "&#9733;&#9733;&#9733;&#9733;&#9733;", "即将上市", False,
    "即将上市", "3+（Google Store、9to5Google、AndroidPolice）",
    "Tensor G6自研芯片 | NPU算力提升 | Gemini AI端侧推理 | 7年系统更新 | 改进相机AI处理 | Titan M3安全芯片",
    ["Google Tensor G6自研芯片（TSMC 3nm）","NPU算力显著提升","Gemini AI端侧推理（离线可用）","7年Android系统更新承诺","改进相机AI处理（计算摄影）","Titan M3安全芯片"],
    "Google自研SoC+端侧AI生态对平板AI芯片选型有重要参考价值。",
    "平板SoC AI/NPU方案参考、端侧大模型部署架构、Tensor芯片自研路径",
    "Google / Pixel 11系列", "2026-08-12", "https://store.google.com", "Google Store",
    "Google Store (A级)、9to5Google (B级)、AndroidPolice (B级)", "Tensor G6具体NPU TOPS数值待官宣")

# Cards 20-22
c20 = card(20, "Motorola Razr 70 Ultra — 骁龙8 Elite+4寸外屏竖折+钛金属铰链", "B", "手机/折叠屏/SoC/结构-工艺", "&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "2+（Motorola官网、GSMArena）",
    "骁龙8 Elite | 4英寸pOLED外屏 | 7.1英寸内折主屏 | 钛金属铰链 | 4200mAh | 45W快充",
    ["骁龙8 Elite（3nm）","4英寸pOLED外屏（更大比例覆盖）","7.1英寸内折主屏","钛金属铰链","4200mAh电池+45W有线快充","50MP主摄+13MP超广"],
    "竖折外屏面积持续扩大趋势，钛金属铰链工艺普及。",
    "折叠屏铰链/面板技术、小尺寸设备散热方案、pOLED面板供应链",
    "Motorola / Razr 70 Ultra", "2026-07", "https://www.motorola.com", "Motorola官网",
    "Motorola官网 (A级)、GSMArena (B级)", "具体发售地区和定价待确认")

c21 = card(21, "Samsung Galaxy Watch Ultra2 — 骁龙Wear Elite 3nm+钛金属+590mAh+LTE", "A", "智能手表/SoC/电池/传感器", "&#9733;&#9733;&#9733;&#9733;&#9733;", "即将上市", False,
    "即将上市", "3+（Samsung官网、GSMArena、AndroidAuthority）",
    "骁龙Wear Elite 3nm | 钛金属表壳(Grade 4) | 590mAh | LTE/eSIM | 10ATM+IP69 | 双频GPS | ECG+血压+体温",
    ["骁龙Wear Elite 3nm平台（三星弃用Exynos转向高通）","钛金属表壳（Grade 4钛合金）","590mAh大电池","LTE/eSIM独立通信","10ATM+IP69防水","双频GPS（L1+L5）","ECG心电+血压+体温传感器"],
    "智能手表SoC从Exynos转向高通3nm，能效比突破，续航有望显著提升。",
    "智能手表SoC/电池/传感器方案对平板配件设计、健康生态的参考",
    "Samsung / Galaxy Watch Ultra2", "2026-07-22", "https://www.samsung.com", "Samsung官网",
    "Samsung官网 (A级)、GSMArena (A级)、AndroidAuthority (B级)", "骁龙Wear Elite实际续航和发热表现待实测")

c22 = card(22, "Samsung Galaxy Watch9 — 骁龙Wear Elite 3nm+双频GPS+BIA身体成分", "A", "智能手表/SoC/传感器/生物识别", "&#9733;&#9733;&#9733;&#9733;", "即将上市", False,
    "即将上市", "3+（Samsung官网、GSMArena、AndroidAuthority）",
    "骁龙Wear Elite 3nm | 铝/不锈钢表壳 | 双频GPS | BIA身体成分 | ECG+血压 | 40/44mm双尺寸",
    ["骁龙Wear Elite 3nm平台","铝/不锈钢表壳可选","双频GPS（L1+L5）","BIA身体成分分析","ECG心电+血压监测","40/44mm双尺寸","睡眠监测+压力分析"],
    "智能手表健康传感器持续迭代，SoC平台统一为高通3nm。",
    "传感器方案（BIA/ECG/血压）对平板配件/健康生态的参考、SoC统一化",
    "Samsung / Galaxy Watch9", "2026-07-22", "https://www.samsung.com", "Samsung官网",
    "Samsung官网 (A级)、GSMArena (A级)、AndroidAuthority (B级)", "BIA身体成分测量精度需临床验证")

# Cards 23-26
c23 = card(23, "Xiaomi Watch S5 46mm — 骁龙Wear+蓝宝石玻璃+14天续航", "B", "智能手表/SoC/电池/结构-工艺", "&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "2+（小米官网、gizmochina）",
    "骁龙Wear平台 | 蓝宝石玻璃表镜 | 14天续航 | 双频GPS | 150+运动模式 | 5ATM | AMOLED 466x466",
    ["骁龙Wear平台","蓝宝石玻璃表镜（莫氏9级硬度）","14天超长续航（节能模式）","双频GPS（L1+L5）","150+运动模式","5ATM防水","AMOLED屏（466x466）"],
    "智能手表续航突破14天，低功耗SoC+系统优化是趋势。",
    "低功耗SoC方案、蓝宝石玻璃面板供应链、AMOLED显示方案",
    "Xiaomi / Watch S5 46mm", "2026-05-29", "https://www.mi.com", "小米官网",
    "小米官网 (A级)、gizmochina (B级)", "14天续航为节能模式，日常使用续航待实测")

c24 = card(24, "XREAL AURA — Android XR+Gemini AI+骁龙Reality Elite空间计算平台", "A", "AR-VR/显示-OLED/AI-NPU/SoC", "&#9733;&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "3+（XREAL官网、AndroidAuthority、TechCrunch）",
    "Android XR OS | Gemini AI集成 | 骁龙Reality Elite | 双目Micro-OLED 1080p | 手势+眼动追踪 | SLAM 6DoF | 光波导镜片",
    ["Android XR操作系统（Google专为空间计算设计）","Google Gemini AI深度集成","骁龙Reality Elite空间计算平台","手势追踪+眼动追踪","SLAM空间定位（6DoF）","双目Micro-OLED显示（1080p per eye）","光波导镜片"],
    "AR眼镜进入空间计算时代，自研OS+AI+专用SoC三合一，行业标志性产品。",
    "AR/VR显示技术（Micro-OLED+光波导）、空间计算SoC、手势/眼动交互方案",
    "XREAL / AURA", "2026-06-17", "https://www.xreal.com", "XREAL官网",
    "XREAL官网 (A级)、AndroidAuthority (B级)、TechCrunch (B级)", "光波导镜片量产良率和成本影响定价；续航表现待实测")

c25 = card(25, "Qi2.2全球终端采纳 — iPhone/Galaxy/Pixel三大阵营原生支持25W磁吸", "A", "无线充/无线通信", "&#9733;&#9733;&#9733;&#9733;", "进行中", False,
    "产业动态", "3+（WPC官方、Apple/Samsung/Google官网）",
    "25W磁吸 | iPhone 16/17系列 | Galaxy S26 Ultra | Pixel 10 Pro XL | 2026Q2旗舰标配 | 配件全品类覆盖",
    ["Qi2.2标准25W磁吸无线充电","iPhone 16/17系列原生支持（MagSafe兼容）","Samsung Galaxy S26 Ultra支持","Google Pixel 10 Pro XL支持","配件厂商全品类覆盖（Belkin/Anker/绿联/倍思）","2026Q2旗舰标配趋势"],
    "无线充电标准全球统一，磁吸25W成为新基准，产业拐点已至。",
    "平板Qi2.2磁吸25W无线充方案、磁吸线圈/主控芯片供应链",
    "WPC联盟 / Apple-Samsung-Google", "2026-01", "https://www.wpc.org/qi2", "WPC官方",
    "WPC官方 (A级)、Apple/Samsung/Google官网 (A级)", "平板Qi2.2支持清单待更新")

c26 = card(26, "Google Home Speaker — 端侧NPU运行Gemini Nano+100ms本地推理", "A", "智能音箱/AI-NPU/无线通信", "&#9733;&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "3+（Google Store、The Verge、9to5Google）",
    "端侧NPU | Gemini Nano推理 | <100ms响应 | Wi-Fi 6E | Matter中枢 | 立体声配对 | 远场麦克风阵列",
    ["端侧NPU运行Gemini Nano模型","<100ms本地推理响应（无需云端）","Wi-Fi 6E连接","Matter协议智能家居中枢","立体声配对（两台组成立体声）","远场麦克风阵列","环境感知传感器"],
    "智能音箱从云端AI向端侧AI转型，NPU成为标配，<100ms响应是突破。",
    "端侧NPU方案对平板AI推理的参考、音频SoC架构、Matter协议",
    "Google / Home Speaker", "2026-06-25", "https://store.google.com", "Google Store",
    "Google Store (A级)、The Verge (A级)、9to5Google (B级)", "端侧NPU具体型号和TOPS数值未公布")

# Cards 27-30
c27 = card(27, "Acer Swift Spin 14 AI — Core Series 3 NPU 40TOPS+360度翻转OLED", "B", "笔记本/SoC/NPU/显示-OLED", "&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "2+（Acer官网、LaptopMag）",
    "Intel Core Series 3(NPU 40 TOPS) | 14英寸OLED触控(2.8K) | 360度翻转 | Copilot+ PC | 雷电4 | 22小时续航",
    ["Intel Core Series 3处理器（NPU 40 TOPS）","14英寸OLED触控屏（2.8K）","360度翻转铰链（平板/笔记本二合一）","Copilot+ PC认证","雷电4接口","22小时续航"],
    "翻转本+AI NPU组合，笔记本/平板二合一形态持续演进。",
    "翻转形态参考（平板/笔记本二合一铰链设计）、NPU方案、OLED触控面板",
    "Acer / Swift Spin 14 AI", "2026-05-28", "https://www.acer.com", "Acer官网",
    "Acer官网 (A级)、LaptopMag (B级)", "360度翻转铰链耐久性需长期验证")

c28 = card(28, "Acer Swift Air 14 — Core Series 3+1kg以下超轻+OLED+Copilot+ PC", "B", "笔记本/SoC/NPU/显示-OLED/结构-工艺", "&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "2+（Acer官网、LaptopMag）",
    "Intel Core Series 3(NPU 40 TOPS) | 14英寸OLED(2.8K) | <1kg(镁锂合金) | Copilot+ PC | 15小时续航 | 雷电4",
    ["Intel Core Series 3处理器（NPU 40 TOPS）","14英寸OLED屏（2.8K）","<1kg超轻机身（镁锂合金）","Copilot+ PC认证","15小时续航","雷电4接口"],
    "AI PC极致轻薄化，<1kg+NPU成为新标准。",
    "超轻结构设计参考（镁锂合金）、OLED面板供应链、NPU方案",
    "Acer / Swift Air 14", "2026-05-28", "https://www.acer.com", "Acer官网",
    "Acer官网 (A级)、LaptopMag (B级)", "<1kg散热方案对性能释放的影响需实测")

c29 = card(29, "Microsoft Surface Pro 8 & Laptop 8 — Snapdragon X2 Elite NPU 80TOPS+OLED", "A", "笔记本/SoC/AI-NPU/显示-OLED", "&#9733;&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "3+（Microsoft官网、The Verge、Engadget）",
    "Snapdragon X2 Elite(NPU 80 TOPS) | 13英寸OLED | Copilot+ PC | 可拆卸键盘(Pro) | 雷电4 | 16GB+ | ARM架构Windows",
    ["Snapdragon X2 Elite（NPU 80 TOPS）","13英寸OLED（Pro可拆卸键盘形态）","Copilot+ PC认证","可拆卸键盘（Surface Pro）","雷电4/USB-C","16GB+内存","ARM架构Windows"],
    "Snapdragon X2 Elite NPU 80 TOPS定义AI PC性能天花板。",
    "平板/笔记本二合一SoC方案、ARM架构Windows生态、OLED面板",
    "Microsoft / Surface Pro 8 & Laptop 8", "2026-06-17", "https://www.microsoft.com", "Microsoft官网",
    "Microsoft官网 (A级)、The Verge (A级)、Engadget (B级)", "ARM架构Windows兼容性和x86模拟性能待验证")

c30 = card(30, "HP OmniBook X 16 — Snapdragon X2 Elite NPU 80TOPS+16寸2.8K OLED", "A", "笔记本/SoC/AI-NPU/显示-OLED", "&#9733;&#9733;&#9733;&#9733;&#9733;", "已上市", False,
    "新品发布", "2+（HP官网、LaptopMag）",
    "Snapdragon X2 Elite(NPU 80 TOPS) | 16英寸2.8K OLED | Copilot+ PC | 32GB可选 | 雷电4 | 21小时续航 | HP AI Companion",
    ["Snapdragon X2 Elite（NPU 80 TOPS）","16英寸2.8K OLED屏","Copilot+ PC认证","32GB内存可选","雷电4接口","21小时续航","HP AI Companion软件"],
    "AI PC大屏化+高性能NPU，80 TOPS成为旗舰标准。",
    "ARM架构SoC方案、大屏OLED面板、NPU算力对标",
    "HP / OmniBook X 16", "2026-07-30", "https://www.hp.com", "HP官网",
    "HP官网 (A级)、LaptopMag (B级)", "21小时续航为视频播放场景，实际办公续航待测试")

# Close tags
closing = """
    </div>
  </div>

</div>

<script>
function toggleCard(id) {
  var el = document.getElementById(id);
  if (el) el.classList.toggle('expanded');
}
</script>
</body>
</html>
"""

# Assemble all remaining content
remaining = c12_rest + c13 + c14 + c15 + section_close_open + c16 + c17 + c18 + c19 + c20 + c21 + c22 + c23 + c24 + c25 + c26 + c27 + c28 + c29 + c30 + closing

# Append to file
with open(filepath, 'a', encoding='utf-8') as f:
    f.write(remaining)

# Verify
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")
print(f"File size: {len(''.join(lines))} bytes")
print(f"Last line: {lines[-1].strip() if lines else 'EMPTY'}")
# Check for card count
card_count = sum(1 for l in lines if 'class="intel-card' in l)
print(f"Card count: {card_count}")
