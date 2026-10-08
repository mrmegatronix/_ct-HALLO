with open('index.html', 'r') as f:
    lines = f.readlines()

new_lines = []
in_bad_block = False
bad_block = []

for line in lines:
    if line.strip() == "// Spawn & Draw Walking Monsters using high-res SVGs":
        in_bad_block = True
    
    if in_bad_block:
        bad_block.append(line)
        if line.strip() == "// Draw Distant and Foreground Bats":
            in_bad_block = False
            # remove the last line from bad_block, append it to new_lines later
            bad_block.pop()
            new_lines.append(line) # keep the bats line where it belongs
    else:
        new_lines.append(line)

# Now inject bad_block inside render(), specifically before // Draw Distant and Foreground Bats
final_lines = []
for line in new_lines:
    if line.strip() == "// Draw Distant and Foreground Bats":
        final_lines.extend(bad_block)
        final_lines.append(line)
    else:
        final_lines.append(line)

with open('index.html', 'w') as f:
    f.writelines(final_lines)

