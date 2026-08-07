# -*- coding: utf-8 -*-
"""Fix remaining card status tag CSS class mismatches"""

filepath = "E:/AI相关/预研究/202608/03_输出/WB_2026-08-07_硬件看板.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Only fix card header status tags (not table cells which use td-status wrapper)
# Card tags pattern: <span class="status-tag status-XXX">TEXT</span>
# Table cells pattern: <td class="td-status"><span class="status-tag status-XXX">TEXT</span></td>

# Fix card tags that are NOT inside td-status (i.e. in card headers)
# We need to be careful not to touch table cells

# Strategy: fix all occurrences, then re-fix table cells to correct values
replacements = [
    ('<span class="status-tag status-coming">已上市</span>', '<span class="status-tag status-released">已上市</span>'),
    ('<span class="status-tag status-coming">已发布</span>', '<span class="status-tag status-released">已发布</span>'),
    ('<span class="status-tag status-coming">进行中</span>', '<span class="status-tag status-progress">进行中</span>'),
    ('<span class="status-tag status-notyet">即将上市</span>', '<span class="status-tag status-coming">即将上市</span>'),
]

for old, new in replacements:
    count = html.count(old)
    # Only replace if NOT inside td-status (table cells already correct)
    # We'll replace all, then fix table cells back
    html = html.replace(old, new)
    if count > 0:
        print(f"Fixed {count}x: {old[:50]}... -> {new[:50]}...")

# Now table cells might have been double-affected, let's verify
import re

# Count all status tags by location
table_tags = re.findall(r'<td class="td-status"><span class="status-tag (status-\w+)">(.*?)</span></td>', html)
card_tags = re.findall(r'class="card-badges">.*?<span class="status-tag (status-\w+)">(.*?)</span>', html, re.DOTALL)

# Actually, let's just count all occurrences
all_tags = re.findall(r'<span class="status-tag (status-\w+)">(.*?)</span>', html)
from collections import Counter
combos = Counter(all_tags)

print(f"\nTotal status tags: {len(all_tags)}")
for (cls, text), count in sorted(combos.items()):
    print(f"  {cls} + {text}: {count}")

# Verify correctness
expected = {
    ("status-released", "已上市"),
    ("status-released", "已发布"),
    ("status-coming", "即将上市"),
    ("status-progress", "进行中"),
}
errors = [(cls, text, count) for (cls, text), count in combos.items() if (cls, text) not in expected]
if errors:
    print(f"\n✗ Still {len(errors)} wrong combos:")
    for cls, text, count in errors:
        print(f"  {cls} + {text}: {count}")
else:
    print("\n✓ All status tag CSS classes correct!")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
print(f"\nFile saved: {len(html)} bytes")
