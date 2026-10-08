import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Brighten background
content = content.replace("background-position: center;", "background-position: center;\n            filter: brightness(1.25);")

# 2. Fix h1 css
content = content.replace("white-space: nowrap;", "white-space: normal;\n        }\n        \n        .text-line {\n            display: block;\n            margin-bottom: 5px;")
content = content.replace("margin: 0 15px;", "margin: 0 0.15em;")

# 3. Replace messages array
old_messages = """        const messages = [
            ["JOIN", "US", "FOR", "HALLOWEEN"],
            ["SPOOKTACULAR", "TRIVIA", "NIGHT,", "WEDNESDAY", "28TH", "FROM", "7PM"],
            ["BOOK", "NOW", "IF", "YOU", "DARE"],
            ["WE", "WOULDN'T", "WANT", "YOU", "TO", "GET", "A", "SCARE!"]
        ];"""
new_messages = """        const messages = [
            {
                color: "#ffaa00",
                lines: [
                    ["JOIN", "US"],
                    ["FOR", "HALLOWEEN"]
                ]
            },
            {
                color: "#ff33ff",
                lines: [
                    ["SPOOKTACULAR", "TRIVIA", "NIGHT,"],
                    ["WEDNESDAY", "28TH"],
                    ["FROM", "7PM"]
                ]
            },
            {
                color: "#00ff33",
                lines: [
                    ["BOOK", "NOW"],
                    ["IF", "YOU", "DARE"]
                ]
            },
            {
                color: "#33ccff",
                lines: [
                    ["WE", "WOULDN'T"],
                    ["WANT", "YOU", "TO"],
                    ["GET", "A", "SCARE!"]
                ]
            }
        ];"""
content = content.replace(old_messages, new_messages)

# 4. Replace runTextCycle
old_runTextCycle = """        function runTextCycle() {
            let words = messages[currentMessageIndex];
            totalWords = words.length;
            revealedWords = 0;
            isTextCycleActive = true;
            
            let charCount = words.join(" ").length;
            let fontSize = charCount > 40 ? 40 : (charCount > 25 ? 60 : 100);
            const h1 = document.querySelector('.content h1');
            h1.style.fontSize = fontSize + 'px';
            
            let html = '';
            for(let i=0; i<totalWords; i++) {
                html += `<span id="word${i}">${words[i]}</span>`;
            }
            h1.innerHTML = html;"""

new_runTextCycle = """        function runTextCycle() {
            let msg = messages[currentMessageIndex];
            totalWords = msg.lines.reduce((acc, line) => acc + line.length, 0);
            revealedWords = 0;
            isTextCycleActive = true;
            
            const h1 = document.querySelector('.content h1');
            h1.style.color = msg.color;
            h1.style.textShadow = `0 0 50px ${msg.color}, 0 5px 15px #000`;
            h1.style.fontSize = msg.lines.length > 2 ? '65px' : '85px';
            
            let html = '';
            let wordIdx = 0;
            msg.lines.forEach(line => {
                html += `<div class="text-line">`;
                line.forEach(word => {
                    html += `<span id="word${wordIdx}">${word}</span>`;
                    wordIdx++;
                });
                html += `</div>`;
            });
            h1.innerHTML = html;"""
content = content.replace(old_runTextCycle, new_runTextCycle)

# 5. Load SVG Monster Images and remove cryptids logic
monster_loading = """        // Witch Image Loading
        const witchImg = new Image();
        witchImg.src = 'witch.png';
        
        let witch = {
            x: -200, y: 300,
            speed: 2.0, scale: 0.6
        };"""

new_monster_loading = """        // Witch Image Loading
        const witchImg = new Image();
        witchImg.src = 'witch.png';
        let witch = { x: -200, y: 300, speed: 2.0, scale: 0.6 };

        // Load Professional Monster SVGs
        const monsterImages = [];
        ['ghost.svg', 'reaper.svg', 'skeleton.svg', 'vampire.svg', 'werewolf.svg', 'zombie.svg'].forEach(src => {
            let img = new Image();
            img.src = src;
            monsterImages.push(img);
        });"""
content = content.replace(monster_loading, new_monster_loading)

# 6. Remove Window Cryptids and update walking monsters
start_idx = content.find("        // Window Cryptids")
end_idx = content.find("        // Spawn & Draw Cats")

if start_idx != -1 and end_idx != -1:
    new_monsters_code = """        // Spawn & Draw Walking Monsters using high-res SVGs
            if (Math.random() < 0.015 && monsterImages.length > 0) {
                monsters.push({
                    img: monsterImages[Math.floor(Math.random() * monsterImages.length)],
                    x: Math.random() < 0.5 ? -100 : 2020,
                    y: 800 + Math.random() * 250,
                    targetX: 850 + Math.random() * 200,
                    targetY: 600,
                    speed: 0.8 + Math.random() * 1.0,
                    frame: 0
                });
            }

            monsters.sort((a,b) => a.y - b.y).forEach((m, i) => {
                m.frame += 0.1;
                let dx = m.targetX - m.x;
                let dy = m.targetY - m.y;
                let dist = Math.sqrt(dx*dx + dy*dy);
                
                if (dist < 10) { monsters.splice(i, 1); return; }
                
                m.x += (dx/dist) * m.speed;
                m.y += (dy/dist) * m.speed;
                
                let scale = 0.5 + ((m.y - 600) / 450) * 0.8;
                
                ctx.save();
                ctx.translate(m.x, m.y);
                ctx.scale(dx > 0 ? scale : -scale, scale); 
                
                if (m.img.complete && m.img.width > 0) {
                    let bob = Math.sin(m.frame) * 4;
                    ctx.drawImage(m.img, -40, -80 + bob, 80, 80);
                }
                ctx.restore();
            });

"""
    content = content[:start_idx] + new_monsters_code + content[end_idx:]

with open('index.html', 'w') as f:
    f.write(content)

