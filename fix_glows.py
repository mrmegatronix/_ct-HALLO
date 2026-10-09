with open('index.html', 'r') as f:
    content = f.read()

# 1. Update drawOwls
old_owls = """                ctx.ellipse(owl.x + 16, owl.y, 3, 4 * eyeScale, 0, 0, Math.PI*2);
                ctx.fill();
                ctx.shadowBlur = 0;"""
new_owls = """                ctx.ellipse(owl.x + 16, owl.y, 3, 4 * eyeScale, 0, 0, Math.PI*2);
                ctx.fill();
                ctx.shadowBlur = 0;
                
                ctx.strokeStyle = '#000';
                ctx.lineWidth = 1.5;
                ctx.stroke();"""
content = content.replace(old_owls, new_owls)

# 2. Add flickering candle glows for pumpkin and windows
old_moon = """            ctx.arc(mx, my, 400, 0, Math.PI*2);
            ctx.fill();
            ctx.globalCompositeOperation = 'source-over';"""
new_moon = """            ctx.arc(mx, my, 400, 0, Math.PI*2);
            ctx.fill();
            
            // Flicker effect for building lights
            let flicker = 0.7 + Math.random() * 0.3;

            // Jack-o'-lantern candle glow
            const jx = 960, jy = 430;
            const jGlow = ctx.createRadialGradient(jx, jy, 0, jx, jy, 150);
            jGlow.addColorStop(0, `rgba(255, 120, 0, ${flicker * 0.6})`);
            jGlow.addColorStop(1, 'rgba(255, 120, 0, 0)');
            ctx.fillStyle = jGlow;
            ctx.beginPath();
            ctx.arc(jx, jy, 150, 0, Math.PI*2);
            ctx.fill();

            // Left Windows candle glow
            const wlx = 400, wly = 560;
            const wlGlow = ctx.createRadialGradient(wlx, wly, 0, wlx, wly, 300);
            wlGlow.addColorStop(0, `rgba(255, 150, 20, ${flicker * 0.4})`);
            wlGlow.addColorStop(1, 'rgba(255, 150, 20, 0)');
            ctx.fillStyle = wlGlow;
            ctx.beginPath();
            ctx.ellipse(wlx, wly, 300, 100, 0, 0, Math.PI*2);
            ctx.fill();

            // Right Windows candle glow
            const wrx = 1315, wry = 560;
            const wrGlow = ctx.createRadialGradient(wrx, wry, 0, wrx, wry, 300);
            wrGlow.addColorStop(0, `rgba(255, 150, 20, ${flicker * 0.4})`);
            wrGlow.addColorStop(1, 'rgba(255, 150, 20, 0)');
            ctx.fillStyle = wrGlow;
            ctx.beginPath();
            ctx.ellipse(wrx, wry, 300, 100, 0, 0, Math.PI*2);
            ctx.fill();

            ctx.globalCompositeOperation = 'source-over';"""
content = content.replace(old_moon, new_moon)

with open('index.html', 'w') as f:
    f.write(content)

