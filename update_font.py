import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update font link
content = content.replace("family=Cinzel:wght@700", "family=Creepster")

# 2. Update CSS font-family
content = content.replace("font-family: 'Cinzel', serif;", "font-family: 'Creepster', cursive;")

# 3. Update JS text coloring
old_color_code = """            const h1 = document.querySelector('.content h1');
            h1.style.color = msg.color;
            h1.style.textShadow = `0 0 50px ${msg.color}, 0 5px 15px #000`;"""
new_color_code = """            const h1 = document.querySelector('.content h1');
            h1.style.color = '#ffffff';
            h1.style.textShadow = `0 0 40px rgba(255, 255, 255, 0.8), 0 5px 15px #000`;"""
content = content.replace(old_color_code, new_color_code)

with open('index.html', 'w') as f:
    f.write(content)

