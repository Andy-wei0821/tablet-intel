import re

with open('WB_2026-08-07_硬件看板.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all card comment positions
card_positions = []
for m in re.finditer(r'      <!-- Card (\d+) -->', content):
    card_positions.append((int(m.group(1)), m.start(), m.end()))

print(f"Found {len(card_positions)} card comments")

# Extract card blocks (from comment start to next comment start or section end)
card_blocks = {}
for i, (num, start, comment_end) in enumerate(card_positions):
    if i + 1 < len(card_positions):
        block_end = card_positions[i+1][1]
    else:
        # Last card - find closing </div></div>
        remaining = content[comment_end:]
        close_match = re.search(r'    </div>\n  </div>', remaining)
        if close_match:
            block_end = comment_end + close_match.start()
        else:
            block_end = len(content)
    
    block_text = content[start:block_end]
    card_blocks[num] = block_text
    print(f"  Card {num}: {len(block_text)} chars")

# New order: old card numbers in new sequence
# Domestic: 1,2,4,3,5 (swap 3 and 4)
# International: 7,6,9,8,10 (reorder)
new_order = [1, 2, 4, 3, 5, 7, 6, 9, 8, 10]

# Build new blocks with updated numbers
new_blocks = []
for new_pos, old_num in enumerate(new_order, 1):
    block = card_blocks[old_num]
    old_s = str(old_num)
    new_s = str(new_pos)
    
    # Update comment
    block = block.replace(f"<!-- Card {old_s} -->", f"<!-- Card {new_s} -->", 1)
    # Update card-num div
    block = block.replace(f'card-num">{old_s}', f'card-num">{new_s}', 1)
    
    new_blocks.append(block)

# Find the gap between domestic and international sections
# Gap = text between end of card 5 block and start of card 6 comment
gap_start = None
gap_end = None
for i, (num, start, comment_end) in enumerate(card_positions):
    if num == 5 and i+1 < len(card_positions):
        gap_start = card_positions[i+1][1]  # start of next comment (but this is wrong - need end of card 5 block)
        break

# Actually, gap is between the end of the last domestic card block and the start of first international card block
# Card 5 block ends where Card 6 comment starts
# But there are section closing/opening divs in between

# Find the section boundary
# The text between card 5's block end and card 6's comment start
for i, (num, start, comment_end) in enumerate(card_positions):
    if num == 5:
        # End of card 5 block = start of next card (6) comment
        gap_start = card_positions[i+1][1] if i+1 < len(card_positions) else None
        break
for i, (num, start, comment_end) in enumerate(card_positions):
    if num == 6:
        gap_end = start
        break

if gap_start and gap_end:
    gap_text = content[gap_start:gap_end]
    print(f"Gap text length: {len(gap_text)}")
else:
    gap_text = ""
    print("WARNING: No gap found")

# Reconstruct
first_start = card_positions[0][1]
last_comment_end = None
for i, (num, start, comment_end) in enumerate(card_positions):
    if num == 10:
        remaining = content[comment_end:]
        close_match = re.search(r'    </div>\n  </div>', remaining)
        if close_match:
            last_comment_end = comment_end + close_match.start()
        break

before = content[:first_start]
after = content[last_comment_end:]

cn_new = "".join(new_blocks[:5])
intl_new = "".join(new_blocks[5:])

new_content = before + cn_new + gap_text + intl_new + after

with open('WB_2026-08-07_硬件看板.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! Cards reordered.")

# Verify
with open('WB_2026-08-07_硬件看板.html', 'r', encoding='utf-8') as f:
    verify = f.read()

for m in re.finditer(r'<!-- Card (\d+) -->', verify):
    num = int(m.group(1))
    title_m = re.search(r'card-title">(.{0,60})', verify[m.end():])
    if title_m:
        print(f"  Card {num}: {title_m.group(1)[:50]}...")
