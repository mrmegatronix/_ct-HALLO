import re

with open('index.html', 'r') as f:
    content = f.read()

old_messages = """        const messages = [
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

new_messages = """        const messages = [
            {
                color: "#ffaa00",
                size: "10vw",
                lines: [
                    ["JOIN", "US"],
                    ["FOR", "HALLOWEEN"]
                ]
            },
            {
                color: "#ff33ff",
                size: "6vw",
                lines: [
                    ["SPOOKTACULAR", "TRIVIA", "NIGHT,"],
                    ["WEDNESDAY,", "OCTOBER", "28TH"],
                    ["FROM", "7PM"]
                ]
            },
            {
                color: "#00ff33",
                size: "11vw",
                lines: [
                    ["BOOK", "NOW"],
                    ["IF", "YOU", "DARE"]
                ]
            },
            {
                color: "#33ccff",
                size: "9vw",
                lines: [
                    ["WE", "WOULDN'T"],
                    ["WANT", "YOU", "TO"],
                    ["GET", "A", "SCARE!"]
                ]
            }
        ];"""
content = content.replace(old_messages, new_messages)

old_logic = """            // Dynamically calculate font size in vw so the longest line fills exactly 95% of the screen width
            let maxLineLength = Math.max(...msg.lines.map(line => line.join(" ").length));
            let fontSizeVW = 95 / (maxLineLength * 0.45); // Creepster aspect ratio approximation
            fontSizeVW = Math.min(fontSizeVW, 22); // Cap vertical height
            h1.style.fontSize = fontSizeVW + 'vw';
            h1.style.letterSpacing = '2px';"""

new_logic = """            // Safely apply pre-calculated hardcoded viewport widths to prevent all clipping
            h1.style.fontSize = msg.size;
            h1.style.letterSpacing = '3px';"""
content = content.replace(old_logic, new_logic)

with open('index.html', 'w') as f:
    f.write(content)

