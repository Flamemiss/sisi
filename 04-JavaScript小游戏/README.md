# 任务4：JavaScript网页小游戏

## 🎯 任务目标

学会JavaScript基础，制作一个可以在浏览器运行的小游戏。

---

## 📋 验收标准

| 序号 | 验收项目 | 具体要求 |
|------|----------|----------|
| 1 | 游戏界面 | 网页显示游戏区域 |
| 2 | 用户交互 | 能响应键盘或鼠标操作 |
| 3 | 游戏逻辑 | 有基本的游戏规则 |
| 4 | 分数显示 | 显示当前得分 |
| 5 | 游戏结束 | 有胜负判定或结束提示 |
| 6 | 重新开始 | 可以重新开始游戏 |

---

## 📝 练习任务

### 项目：猜数字游戏

创建文件 `guess.html`：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>猜数字游戏</title>
    <style>
        body {
            font-family: "Microsoft YaHei", sans-serif;
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
            text-align: center;
        }
        
        .game-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            border-radius: 20px;
            color: white;
        }
        
        h1 {
            margin-bottom: 10px;
        }
        
        input {
            width: 100px;
            padding: 15px;
            font-size: 24px;
            text-align: center;
            border: none;
            border-radius: 10px;
            margin: 20px 0;
        }
        
        button {
            padding: 15px 30px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin: 5px;
        }
        
        .btn-primary {
            background: #ffd700;
            color: #333;
        }
        
        .btn-secondary {
            background: rgba(255,255,255,0.2);
            color: white;
        }
        
        button:hover {
            transform: scale(1.05);
        }
        
        .message {
            font-size: 20px;
            margin: 20px 0;
            min-height: 30px;
        }
        
        .history {
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="game-box">
        <h1>🎮 猜数字游戏</h1>
        <p>我想了一个1-100之间的数字，猜猜是多少？</p>
        
        <input type="number" id="guessInput" min="1" max="100" placeholder="?">
        
        <div>
            <button class="btn-primary" onclick="checkGuess()">猜一猜</button>
            <button class="btn-secondary" onclick="resetGame()">重新开始</button>
        </div>
        
        <div class="message" id="message"></div>
        
        <div class="history">
            <p>已猜次数: <span id="attempts">0</span></p>
            <p>猜过的数: <span id="history">-</span></p>
        </div>
    </div>

    <script>
        // 游戏变量
        let secretNumber;
        let attempts;
        let guessHistory;
        
        // 初始化游戏
        function initGame() {
            secretNumber = Math.floor(Math.random() * 100) + 1;
            attempts = 0;
            guessHistory = [];
            document.getElementById('message').textContent = '';
            document.getElementById('attempts').textContent = '0';
            document.getElementById('history').textContent = '-';
            document.getElementById('guessInput').value = '';
            document.getElementById('guessInput').disabled = false;
        }
        
        // 检查猜测
        function checkGuess() {
            const input = document.getElementById('guessInput');
            const guess = parseInt(input.value);
            
            // 验证输入
            if (isNaN(guess) || guess < 1 || guess > 100) {
                showMessage('请输入1-100之间的数字！', '#ffd700');
                return;
            }
            
            // 记录猜测
            attempts++;
            guessHistory.push(guess);
            document.getElementById('attempts').textContent = attempts;
            document.getElementById('history').textContent = guessHistory.join(', ');
            
            // 判断结果
            if (guess === secretNumber) {
                showMessage(`🎉 恭喜！答案就是 ${secretNumber}！用了 ${attempts} 次`, '#00ff00');
                input.disabled = true;
            } else if (guess < secretNumber) {
                showMessage('📈 太小了，再大一点！', '#ffd700');
            } else {
                showMessage('📉 太大了，再小一点！', '#ffd700');
            }
            
            input.value = '';
            input.focus();
        }
        
        // 显示消息
        function showMessage(text, color) {
            const msg = document.getElementById('message');
            msg.textContent = text;
            msg.style.color = color;
        }
        
        // 重新开始
        function resetGame() {
            initGame();
            showMessage('新游戏开始！', 'white');
        }
        
        // 回车键提交
        document.getElementById('guessInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                checkGuess();
            }
        });
        
        // 启动游戏
        initGame();
    </script>
</body>
</html>
```

---

### 进阶项目：贪吃蛇游戏

创建文件 `snake.html`：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>贪吃蛇游戏</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #1a1a2e;
            font-family: "Microsoft YaHei", sans-serif;
        }
        
        .game-container {
            text-align: center;
        }
        
        h1 {
            color: #00ff88;
            margin-bottom: 10px;
        }
        
        .info {
            color: white;
            margin-bottom: 10px;
        }
        
        canvas {
            border: 3px solid #00ff88;
            border-radius: 10px;
        }
        
        .controls {
            margin-top: 15px;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🐍 贪吃蛇</h1>
        <div class="info">
            得分: <span id="score">0</span> | 最高分: <span id="highScore">0</span>
        </div>
        <canvas id="gameCanvas" width="400" height="400"></canvas>
        <div class="controls">
            方向键或 WASD 控制移动 | 空格键暂停/继续
        </div>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        const gridSize = 20;
        const gridCount = canvas.width / gridSize;
        
        let snake, food, direction, score, highScore, gameLoop, isPaused;
        
        function initGame() {
            snake = [{ x: 10, y: 10 }];
            direction = { x: 1, y: 0 };
            score = 0;
            isPaused = false;
            highScore = localStorage.getItem('snakeHighScore') || 0;
            document.getElementById('highScore').textContent = highScore;
            updateScore();
            spawnFood();
            
            if (gameLoop) clearInterval(gameLoop);
            gameLoop = setInterval(update, 100);
        }
        
        function spawnFood() {
            food = {
                x: Math.floor(Math.random() * gridCount),
                y: Math.floor(Math.random() * gridCount)
            };
            // 确保食物不在蛇身上
            for (let part of snake) {
                if (part.x === food.x && part.y === food.y) {
                    spawnFood();
                    break;
                }
            }
        }
        
        function update() {
            if (isPaused) return;
            
            // 移动蛇头
            const head = {
                x: snake[0].x + direction.x,
                y: snake[0].y + direction.y
            };
            
            // 检查碰撞
            if (head.x < 0 || head.x >= gridCount || 
                head.y < 0 || head.y >= gridCount ||
                snake.some(part => part.x === head.x && part.y === head.y)) {
                gameOver();
                return;
            }
            
            snake.unshift(head);
            
            // 吃到食物
            if (head.x === food.x && head.y === food.y) {
                score += 10;
                updateScore();
                spawnFood();
            } else {
                snake.pop();
            }
            
            draw();
        }
        
        function draw() {
            // 清空画布
            ctx.fillStyle = '#1a1a2e';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 画网格
            ctx.strokeStyle = '#2a2a4e';
            for (let i = 0; i <= gridCount; i++) {
                ctx.beginPath();
                ctx.moveTo(i * gridSize, 0);
                ctx.lineTo(i * gridSize, canvas.height);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(0, i * gridSize);
                ctx.lineTo(canvas.width, i * gridSize);
                ctx.stroke();
            }
            
            // 画蛇
            snake.forEach((part, index) => {
                ctx.fillStyle = index === 0 ? '#00ff88' : '#00cc66';
                ctx.fillRect(part.x * gridSize + 1, part.y * gridSize + 1, 
                           gridSize - 2, gridSize - 2);
            });
            
            // 画食物
            ctx.fillStyle = '#ff6b6b';
            ctx.beginPath();
            ctx.arc(food.x * gridSize + gridSize/2, 
                   food.y * gridSize + gridSize/2, 
                   gridSize/2 - 2, 0, Math.PI * 2);
            ctx.fill();
        }
        
        function updateScore() {
            document.getElementById('score').textContent = score;
        }
        
        function gameOver() {
            clearInterval(gameLoop);
            if (score > highScore) {
                highScore = score;
                localStorage.setItem('snakeHighScore', highScore);
                document.getElementById('highScore').textContent = highScore;
            }
            
            ctx.fillStyle = 'rgba(0,0,0,0.7)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#ff6b6b';
            ctx.font = '30px Microsoft YaHei';
            ctx.textAlign = 'center';
            ctx.fillText('游戏结束!', canvas.width/2, canvas.height/2 - 20);
            ctx.fillStyle = 'white';
            ctx.font = '20px Microsoft YaHei';
            ctx.fillText(`得分: ${score}`, canvas.width/2, canvas.height/2 + 20);
            ctx.fillText('按空格键重新开始', canvas.width/2, canvas.height/2 + 50);
        }
        
        // 键盘控制
        document.addEventListener('keydown', (e) => {
            if (e.code === 'Space') {
                if (!gameLoop || gameLoop._cleared) {
                    initGame();
                } else {
                    isPaused = !isPaused;
                }
                return;
            }
            
            const keyMap = {
                'ArrowUp': { x: 0, y: -1 }, 'KeyW': { x: 0, y: -1 },
                'ArrowDown': { x: 0, y: 1 }, 'KeyS': { x: 0, y: 1 },
                'ArrowLeft': { x: -1, y: 0 }, 'KeyA': { x: -1, y: 0 },
                'ArrowRight': { x: 1, y: 0 }, 'KeyD': { x: 1, y: 0 }
            };
            
            const newDir = keyMap[e.code];
            if (newDir && (newDir.x !== -direction.x || newDir.y !== -direction.y)) {
                direction = newDir;
            }
        });
        
        initGame();
    </script>
</body>
</html>
```

---

## 🔧 JavaScript基础语法速查

| 语法 | 说明 | 示例 |
|------|------|------|
| 变量 | 声明变量 | `let name = "张三";` |
| 函数 | 定义函数 | `function add(a, b) { return a + b; }` |
| 条件 | if判断 | `if (x > 0) { ... }` |
| 循环 | for循环 | `for (let i = 0; i < 10; i++) { ... }` |
| 事件 | 点击事件 | `onclick="myFunction()"` |
| DOM | 获取元素 | `document.getElementById('id')` |

---

## ✅ 自测清单

- [ ] 能让按钮点击后执行函数吗？
- [ ] 知道如何用 `document.getElementById()` 获取元素吗？
- [ ] 知道如何修改元素的文字内容吗？
- [ ] 能用 `addEventListener` 监听键盘事件吗？
- [ ] 理解 `setInterval()` 的作用吗？

---

## 📚 推荐资源

- MDN JavaScript教程：https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript
- 现代JavaScript教程：https://zh.javascript.info/
