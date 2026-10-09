with open('index.html', 'r') as f:
    content = f.read()

# Remove SVG loading
load_svg = """        // Load Professional Monster SVGs
        const monsterImages = [];
        ['ghost.svg', 'reaper.svg', 'skeleton.svg', 'vampire.svg', 'werewolf.svg', 'zombie.svg'].forEach(src => {
            let img = new Image();
            img.src = src;
            monsterImages.push(img);
        });"""
content = content.replace(load_svg, "")

# Remove Draw Cats function
start_cat_func = content.find("        function drawCat(ctx, frame) {")
end_cat_func = content.find("        function render() {")
if start_cat_func != -1 and end_cat_func != -1:
    content = content[:start_cat_func] + content[end_cat_func:]

# Remove Cats array
content = content.replace("        // Cats\n        let cats = [];", "")

# Remove Monsters array
content = content.replace("        // Walking Monsters\n        let monsters = [];", "")

# Remove Spawn & Draw Monsters from render loop
start_monsters = content.find("            // Spawn & Draw Walking Monsters using high-res SVGs")
end_monsters = content.find("            // Spawn & Draw Cats")
if start_monsters != -1 and end_monsters != -1:
    content = content[:start_monsters] + content[end_monsters:]

# Remove Spawn & Draw Cats from render loop
start_cats_draw = content.find("            // Spawn & Draw Cats")
end_cats_draw = content.find("            // Draw Distant and Foreground Bats")
if start_cats_draw != -1 and end_cats_draw != -1:
    content = content[:start_cats_draw] + content[end_cats_draw:]

with open('index.html', 'w') as f:
    f.write(content)

