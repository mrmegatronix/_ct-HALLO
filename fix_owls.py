with open('index.html', 'r') as f:
    content = f.read()

old_draw_owls = """        function drawOwls(ctx) {
            owls.forEach(owl => {
                owl.timer += 0.5;
                let eyeScale = 1;
                // Blink closed randomly
                if (owl.timer > 100) {
                    if (owl.timer < 105) eyeScale = 0.1;
                    else owl.timer = 0;
                }
                
                ctx.fillStyle = '#ffaa00';
                ctx.shadowColor = '#ffaa00';
                ctx.shadowBlur = 15;
                ctx.beginPath();
                ctx.ellipse(owl.x, owl.y, 3, 4 * eyeScale, 0, 0, Math.PI*2);
                ctx.ellipse(owl.x + 16, owl.y, 3, 4 * eyeScale, 0, 0, Math.PI*2);
                ctx.fill();
                ctx.shadowBlur = 0;
                
                ctx.strokeStyle = '#000';
                ctx.lineWidth = 1.5;
                ctx.stroke();
            });
        }"""

new_draw_owls = """        function drawOwls(ctx) {
            owls.forEach(owl => {
                owl.timer += 0.5;
                let eyeScale = 1;
                // Blink closed randomly
                if (owl.timer > 100) {
                    if (owl.timer < 105) eyeScale = 0.1;
                    else owl.timer = 0;
                }
                
                ctx.fillStyle = '#ffaa00';
                ctx.strokeStyle = 'rgba(0,0,0,0.8)';
                ctx.lineWidth = 2;
                
                // Left eye (Almond/Alien shaped, tilted inward)
                ctx.save();
                ctx.translate(owl.x, owl.y);
                ctx.rotate(0.35); 
                ctx.beginPath();
                ctx.moveTo(-6, 0);
                ctx.quadraticCurveTo(0, -5 * eyeScale, 6, 0);
                ctx.quadraticCurveTo(0, 5 * eyeScale, -6, 0);
                ctx.shadowColor = '#ffaa00';
                ctx.shadowBlur = 15;
                ctx.fill();
                ctx.shadowBlur = 0;
                ctx.stroke();
                ctx.restore();

                // Right eye
                ctx.save();
                ctx.translate(owl.x + 18, owl.y);
                ctx.rotate(-0.35); 
                ctx.beginPath();
                ctx.moveTo(-6, 0);
                ctx.quadraticCurveTo(0, -5 * eyeScale, 6, 0);
                ctx.quadraticCurveTo(0, 5 * eyeScale, -6, 0);
                ctx.shadowColor = '#ffaa00';
                ctx.shadowBlur = 15;
                ctx.fill();
                ctx.shadowBlur = 0;
                ctx.stroke();
                ctx.restore();
            });
        }"""

content = content.replace(old_draw_owls, new_draw_owls)

with open('index.html', 'w') as f:
    f.write(content)

