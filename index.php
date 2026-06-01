<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unkindness.ai — A Parliament of Opinions</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background-color: #050507;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        /* Nav */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
            background: linear-gradient(to bottom, rgba(5,5,7,0.9) 0%, transparent 100%);
        }
        
        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            letter-spacing: -0.03em;
            color: #fff;
            text-decoration: none;
        }
        
        .logo span {
            color: #666;
        }
        
        .nav-links a {
            color: #888;
            text-decoration: none;
            font-size: 0.9rem;
            margin-left: 30px;
            transition: color 0.2s;
        }
        
        .nav-links a:hover {
            color: #fff;
        }
        
        /* Hero */
        .hero {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px;
            position: relative;
        }
        
        .hero h1 {
            font-size: 4rem;
            font-weight: 700;
            letter-spacing: -0.04em;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #fff 0%, #999 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .hero p {
            font-size: 1.5rem;
            color: #666;
            margin-bottom: 40px;
            font-weight: 400;
        }
        
        .hero .tagline {
            font-size: 1rem;
            color: #444;
            max-width: 500px;
            line-height: 1.6;
        }
        
        /* Canvas container */
        #swarm-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            pointer-events: none;
        }
        
        .hero-content {
            position: relative;
            z-index: 10;
        }
        
        /* Features section */
        .features {
            position: relative;
            z-index: 10;
            padding: 100px 40px;
            background: linear-gradient(to top, rgba(5,5,7,1) 0%, rgba(5,5,7,0) 100%);
        }
        
        .features-grid {
            max-width: 1000px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
        }
        
        .feature {
            text-align: left;
        }
        
        .feature h3 {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 10px;
            color: #fff;
        }
        
        .feature p {
            font-size: 0.95rem;
            color: #666;
            line-height: 1.6;
        }
        
        .feature .icon {
            font-size: 1.5rem;
            margin-bottom: 15px;
            display: block;
        }
        
        /* Footer */
        footer {
            position: relative;
            z-index: 10;
            padding: 40px;
            text-align: center;
            color: #444;
            font-size: 0.85rem;
        }
        
        footer a {
            color: #666;
            text-decoration: none;
        }
        
        footer a:hover {
            color: #fff;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }
            .hero p {
                font-size: 1.1rem;
            }
            .features-grid {
                grid-template-columns: 1fr;
            }
            nav {
                padding: 15px 20px;
            }
        }
    </style>
</head>
<body>
    <canvas id="swarm-canvas"></canvas>
    
    <nav>
        <a href="https://github.com/bdebruin/unkindness.ai" class="logo">unkindness<span>.ai</span></a>
        <div class="nav-links">
            <a href="https://github.com/bdebruin/unkindness.ai">GitHub</a>
            <a href="#features">Docs</a>
        </div>
    </nav>
    
    <section class="hero">
        <div class="hero-content">
            <h1>Unkindness.ai</h1>
            <p>A parliament of opinions.</p>
            <p class="tagline">Swarm intelligence simulation framework for modeling emergent behaviors in distributed agent systems.</p>
        </div>
    </section>
    
    <section class="features" id="features">
        <div class="features-grid">
            <div class="feature">
                <span class="icon">🐦</span>
                <h3>BaseRaven Agents</h3>
                <p>Autonomous agents with position, velocity, perception, memory, and communication. Each raven is an individual with its own beliefs and behaviors.</p>
            </div>
            <div class="feature">
                <span class="icon">🦅</span>
                <h3>Flocking Behavior</h3>
                <p>Reynolds-style boids simulation with separation, alignment, and cohesion. Watch emergent coordination arise from simple rules.</p>
            </div>
            <div class="feature">
                <span class="icon">🧠</span>
                <h3>Consensus Engine</h3>
                <p>Distributed decision making through opinion propagation. Ravens share and align beliefs through local communication.</p>
            </div>
            <div class="feature">
                <span class="icon">📊</span>
                <h3>Metrics & Visualization</h3>
                <p>Track population, energy, communication patterns, and state transitions. ASCII and JSON output for integration.</p>
            </div>
            <div class="feature">
                <span class="icon">🌍</span>
                <h3>Environment Simulation</h3>
                <p>Boundaries, resources, obstacles, and global data. Rich environments that shape agent behavior.</p>
            </div>
            <div class="feature">
                <span class="icon">⚡</span>
                <h3>Python Native</h3>
                <p>Built in Python with type hints throughout. Easy to extend, easy to integrate, easy to understand.</p>
            </div>
        </div>
    </section>
    
    <footer>
        <p><a href="https://github.com/bdebruin/unkindness.ai">View on GitHub</a> · MIT License</p>
    </footer>
    
    <script>
        // Simple flocking simulation on canvas
        const canvas = document.getElementById('swarm-canvas');
        const ctx = canvas.getContext('2d');
        
        let width, height;
        let ravens = [];
        const NUM_RAVENS = 80;
        
        // Resize handler
        function resize() {
            width = window.innerWidth;
            height = window.innerHeight;
            canvas.width = width;
            canvas.height = height;
        }
        
        window.addEventListener('resize', resize);
        resize();
        
        // Raven class
        class Raven {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 2;
                this.vy = (Math.random() - 0.5) * 2;
                this.history = [];
            }
            
            update(ravens) {
                // Separation
                let sx = 0, sy = 0;
                // Alignment  
                let ax = 0, ay = 0;
                // Cohesion
                let cx = 0, cy = 0;
                let count = 0;
                
                for (let other of ravens) {
                    if (other === this) continue;
                    let dx = this.x - other.x;
                    let dy = this.y - other.y;
                    let dist = Math.sqrt(dx*dx + dy*dy);
                    
                    if (dist < 80) {
                        sx -= dx / dist;
                        sy -= dy / dist;
                    }
                    if (dist < 150) {
                        ax += other.vx;
                        ay += other.vy;
                        cx += other.x;
                        cy += other.y;
                        count++;
                    }
                }
                
                if (count > 0) {
                    ax /= count;
                    ay /= count;
                    cx = cx/count - this.x;
                    cy = cy/count - this.y;
                }
                
                // Combine forces
                this.vx += sx * 0.05 + ax * 0.02 + cx * 0.01;
                this.vy += sy * 0.05 + ay * 0.02 + cy * 0.01;
                
                // Limit speed
                let speed = Math.sqrt(this.vx*this.vx + this.vy*this.vy);
                if (speed > 3) {
                    this.vx = (this.vx / speed) * 3;
                    this.vy = (this.vy / speed) * 3;
                }
                
                // Move
                this.x += this.vx;
                this.y += this.vy;
                
                // Wrap edges
                if (this.x < 0) this.x = width;
                if (this.x > width) this.x = 0;
                if (this.y < 0) this.y = height;
                if (this.y > height) this.y = 0;
                
                // Track history for trail
                this.history.push({x: this.x, y: this.y});
                if (this.history.length > 8) this.history.shift();
            }
            
            draw(ctx) {
                // Draw trail
                if (this.history.length > 1) {
                    ctx.beginPath();
                    ctx.moveTo(this.history[0].x, this.history[0].y);
                    for (let i = 1; i < this.history.length; i++) {
                        ctx.lineTo(this.history[i].x, this.history[i].y);
                    }
                    ctx.strokeStyle = 'rgba(255,255,255,0.1)';
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
                
                // Draw raven
                let angle = Math.atan2(this.vy, this.vx);
                ctx.save();
                ctx.translate(this.x, this.y);
                ctx.rotate(angle);
                
                ctx.beginPath();
                ctx.moveTo(8, 0);
                ctx.lineTo(-5, -4);
                ctx.lineTo(-3, 0);
                ctx.lineTo(-5, 4);
                ctx.closePath();
                
                ctx.fillStyle = 'rgba(255,255,255,0.6)';
                ctx.fill();
                
                ctx.restore();
            }
        }
        
        // Initialize ravens
        for (let i = 0; i < NUM_RAVENS; i++) {
            ravens.push(new Raven());
        }
        
        // Animation loop
        function animate() {
            ctx.fillStyle = 'rgba(5, 5, 7, 0.15)';
            ctx.fillRect(0, 0, width, height);
            
            for (let raven of ravens) {
                raven.update(ravens);
                raven.draw(ctx);
            }
            
            requestAnimationFrame(animate);
        }
        
        animate();
    </script>
</body>
</html>