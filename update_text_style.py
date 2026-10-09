import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add webkit text stroke and line-height to h1 CSS
css_h1_old = """        h1 {
            font-size: 100px;
            letter-spacing: 10px;
            color: #fff;
            margin: 0;
            text-transform: uppercase;
            text-shadow: 0 0 50px rgba(255,100,0,0.8), 0 5px 15px #000;
            white-space: normal;
        }"""
css_h1_new = """        h1 {
            font-size: 150px;
            letter-spacing: 5px;
            color: #fff;
            margin: 0;
            text-transform: uppercase;
            white-space: normal;
            line-height: 1.1;
            -webkit-text-stroke: 4px #000;
        }"""
content = content.replace(css_h1_old, css_h1_new)

# 2. Update JS styling in runTextCycle
old_js_style = """            const h1 = document.querySelector('.content h1');
            h1.style.color = '#ffffff';
            h1.style.textShadow = `0 0 40px rgba(255, 255, 255, 0.8), 0 5px 15px #000`;
            h1.style.fontSize = msg.lines.length > 2 ? '65px' : '85px';
            h1.style.letterSpacing = '5px';"""
new_js_style = """            const h1 = document.querySelector('.content h1');
            h1.style.color = '#ffffff';
            // Bright white glow + solid black drop shadow to pop against the background
            h1.style.textShadow = `0 0 30px #fff, 0 10px 20px #000, 0 0 10px #000`;
            h1.style.fontSize = msg.lines.length > 2 ? '110px' : '180px';
            h1.style.letterSpacing = '5px';"""
content = content.replace(old_js_style, new_js_style)

# 3. Increase text-line margin slightly for bigger fonts
content = content.replace("margin-bottom: 5px;", "margin-bottom: 10px;")

with open('index.html', 'w') as f:
    f.write(content)

