# -*- coding: utf-8 -*-
"""Fix: add 上市状态 column to summary table + fix card status CSS classes"""

import re

filepath = "E:/AI相关/预研究/202608/03_输出/WB_2026-08-07_硬件看板.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# === 1. Add status-released and status-progress CSS classes ===
old_css = """  .status-coming { background:#ecf5ff; color:#409eff; border:1px solid #b3d8ff; }
  .status-notyet { background:#fdf6ec; color:#e6a23c; border:1px dashed #f5dab1; }"""

new_css = """  .status-coming { background:#ecf5ff; color:#409eff; border:1px solid #b3d8ff; }
  .status-released { background:#f0f9eb; color:#67c23a; border:1px solid #c2e7b0; }
  .status-progress { background:#f4f4f5; color:#909399; border:1px solid #e4e7ed; }"""

html = html.replace(old_css, new_css)

# === 2. Fix card status tags: normalize CSS classes ===
# Map: text -> correct CSS class
status_map = {
    "已上市": "status-released",
    "已发布": "status-released",
    "即将上市": "status-coming",
    "进行中": "status-progress",
}

# Fix all card header status tags
# Pattern: <span class="status-tag status-XXX">TEXT</span>
def fix_status_tag(match):
    text = match.group(2)
    css_class = status_map.get(text, "status-released")
    return f'<span class="status-tag {css_class}">{text}</span>'

html = re.sub(
    r'<span class="status-tag\s+\w+">(已上市|已发布|即将上市|进行中)</span>',
    fix_status_tag,
    html
)

# === 3. Add 上市状态 column to summary table ===
# Add header
old_header = '<thead><tr><th>#</th><th>标题</th><th>区域</th><th>领域</th><th>信源</th><th>时间</th><th>重要度</th></tr></thead>'
new_header = '<thead><tr><th>#</th><th>标题</th><th>区域</th><th>领域</th><th>上市状态</th><th>信源</th><th>时间</th><th>重要度</th></tr></thead>'
html = html.replace(old_header, new_header)

# Status data for all 30 items (matching summary table order)
statuses = [
    ("已上市", "released"),     # 1 红魔游戏平板5 Pro
    ("已上市", "released"),     # 2 华为MatePad Pro Max
    ("即将上市", "coming"),     # 3 小米18 CMIIT认证
    ("已上市", "released"),     # 4 iQOO 15T
    ("已上市", "released"),     # 5 vivo X Fold6
    ("即将上市", "coming"),     # 6 荣耀WIN Turbo
    ("即将上市", "coming"),     # 7 华为WATCH GT 7系列
    ("已上市", "released"),     # 8 华为WATCH GT Runner 2
    ("已上市", "released"),     # 9 雷鸟GT系列AR眼镜
    ("已上市", "released"),     # 10 雷鸟V4 AI拍摄眼镜
    ("已发布", "released"),     # 11 Qi2.2无线充电标准发布
    ("进行中", "progress"),     # 12 WPC Qi2.2认证521款
    ("已上市", "released"),     # 13 天猫精灵Sound Pro
    ("已上市", "released"),     # 14 小米小爱音箱Pro 2026款
    ("已上市", "released"),     # 15 联想小新Air 2026版
    ("已上市", "released"),     # 16 Motorola Moto Pad 70 Pro
    ("即将上市", "coming"),     # 17 Samsung Galaxy Z Fold 8
    ("即将上市", "coming"),     # 18 Samsung Galaxy Z Flip 8
    ("即将上市", "coming"),     # 19 Google Pixel 11系列
    ("已上市", "released"),     # 20 Motorola Razr 70 Ultra
    ("即将上市", "coming"),     # 21 Samsung Galaxy Watch Ultra2
    ("即将上市", "coming"),     # 22 Samsung Galaxy Watch9
    ("已上市", "released"),     # 23 Xiaomi Watch S5 46mm
    ("已上市", "released"),     # 24 XREAL AURA空间计算眼镜
    ("进行中", "progress"),     # 25 Qi2.2全球终端采纳
    ("已上市", "released"),     # 26 Google Home Speaker
    ("已上市", "released"),     # 27 Acer Swift Spin 14 AI
    ("已上市", "released"),     # 28 Acer Swift Air 14
    ("已上市", "released"),     # 29 Microsoft Surface Pro/Laptop 8
    ("已上市", "released"),     # 30 HP OmniBook X 16
]

# Insert status cell before 信源 cell in each row
# Pattern: ...<td>领域</td><td><span class="source-tag... → insert status cell
lines = html.split('\n')
new_lines = []
row_idx = 0

for line in lines:
    # Match summary table data rows (contain <td>N</td> at start)
    m = re.match(r'(\s*<tr><td>(\d+)</td><td class="td-title">.*?</td><td><span class="td-region.*?</td><td>.*?</td>)<td><span class="source-tag', line)
    if m and row_idx < len(statuses):
        prefix = m.group(1)
        status_text, status_class = statuses[row_idx]
        status_cell = f'<td><span class="status-tag status-{status_class}">{status_text}</span></td>'
        new_line = prefix + status_cell + '<td><span class="source-tag' + line[m.end():]
        new_lines.append(new_line)
        row_idx += 1
    else:
        new_lines.append(line)

html = '\n'.join(new_lines)

# Also add small CSS for summary table status tags
old_status_css = ".status-tag { display:inline-block; font-size:11px; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; margin-left:8px; }"
new_status_css = ".status-tag { display:inline-block; font-size:11px; font-weight:600; padding:2px 8px; border-radius:4px; white-space:nowrap; margin-left:8px; }"
# Add a smaller variant for table
table_status_css = "\n  .td-status .status-tag { margin-left:0; font-size:10px; padding:1px 6px; }"
# Wrap status cells in td-status class
html = html.replace('<td><span class="status-tag status-', '<td class="td-status"><span class="status-tag status-')
# Insert the CSS after status-tag definition
html = html.replace(old_status_css, new_status_css + table_status_css)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done! File size: {len(html)} bytes")
print(f"Status column added to {row_idx} rows")

# Verify
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
    
# Check header
if "<th>上市状态</th>" in content:
    print("✓ Header: 上市状态 column found")
else:
    print("✗ Header: 上市状态 column NOT found")

# Count status cells in table
status_count = content.count('class="td-status"')
print(f"✓ Status cells in table: {status_count}")

# Check CSS classes
for cls in ["status-released", "status-progress"]:
    if f".{cls}" in content:
        print(f"✓ CSS .{cls} defined")
    else:
        print(f"✗ CSS .{cls} NOT defined")

# Check card status tags
card_tags = re.findall(r'<span class="status-tag (status-\w+)">(已上市|已发布|即将上市|进行中)</span>', content)
print(f"\nCard status tags ({len(card_tags)} total):")
from collections import Counter
combos = Counter(card_tags)
for (cls, text), count in combos.items():
    print(f"  {cls} + {text}: {count}")
