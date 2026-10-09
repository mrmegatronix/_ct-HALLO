import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update JS logic
old_js = """            const h1 = document.querySelector('.content h1');
            h1.style.color = '#ffffff';
            h1.style.textShadow = `0 0 40px rgba(255, 255, 255, 0.8), 0 5px 15px #000`;
            h1.style.fontSize = msg.lines.length > 2 ? '65px' : '85px';"""

new_js = """            const h1 = document.querySelector('.content h1');
            h1.style.color = '#ffffff';
            h1.style.textShadow = `0 0 30px #fff, 0 10px 20px #000, 0 0 10px #000`;
            
            // Dynamically calculate font size in vw so the longest line fills exactly 95% of the screen width
            let maxLineLength = Math.max(...msg.lines.map(line => line.join(" ").length));
            let fontSizeVW = 95 / (maxLineLength * 0.45); // Creepster aspect ratio approximation
            fontSizeVW = Math.min(fontSizeVW, 22); // Cap vertical height
            h1.style.fontSize = fontSizeVW + 'vw';
            h1.style.letterSpacing = '2px';"""

content = content.replace(old_js, new_js)

# 2. Update CSS
old_css = """        h1 {
            font-size: 100px;
            letter-spacing: 10px;
            color: #fff;
            margin: 0;
            text-transform: uppercase;
            text-shadow: 0 0 50px rgba(255,100,0,0.8), 0 5px 15px #000;
            white-space: normal;
        }"""
new_css = """        h1 {
            font-size: 150px;
            letter-spacing: 2px;
            color: #fff;
            margin: 0;
            text-transform: uppercase;
            white-space: normal;
            line-height: 1.0;
            -webkit-text-stroke: 4px #000;
        }"""
content = content.replace(old_css, new_css)

content = content.replace("margin-bottom: 5px;", "margin-bottom: 2vh;")

with open('index.html', 'w') as f:
    f.write(content)

