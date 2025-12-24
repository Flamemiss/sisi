# 任务10：综合项目 - AI聊天机器人

## 🎯 任务目标

综合运用所学知识，制作一个完整的AI聊天机器人应用。

---

## 📋 验收标准

| 序号 | 验收项目 | 具体要求 |
|------|----------|----------|
| 1 | 项目结构 | 代码文件组织合理 |
| 2 | AI对话 | 调用API实现智能对话 |
| 3 | 用户界面 | 有可视化聊天界面（网页或命令行） |
| 4 | 对话历史 | 支持多轮对话，记住上下文 |
| 5 | 特色功能 | 至少1个特色功能（如角色扮演） |
| 6 | 项目文档 | 完整的README说明 |
| 7 | 版本管理 | 使用Git管理代码 |

---

## 🏗️ 项目结构

```
ai-chatbot/
├── README.md           # 项目说明
├── requirements.txt    # 依赖列表
├── config.py           # 配置文件（API Key）
├── main.py            # 主程序入口
├── chatbot.py         # 聊天机器人核心
├── web/               # 网页版（可选）
│   ├── index.html
│   ├── style.css
│   └── script.js
└── .gitignore         # Git忽略文件
```

---

## 📝 实现步骤

### 第一步：创建项目文件夹

```cmd
mkdir ai-chatbot
cd ai-chatbot
git init
```

### 第二步：创建配置文件

**config.py**（添加到.gitignore，不要提交）：

```python
# config.py
# API配置

# SiliconFlow
SILICONFLOW_API_KEY = "sk-your-api-key-here"
SILICONFLOW_BASE_URL = "https://api.siliconflow.cn/v1"
SILICONFLOW_MODEL = "Qwen/Qwen2.5-7B-Instruct"

# 或 DeepSeek
DEEPSEEK_API_KEY = "sk-your-api-key-here"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"

# 选择使用的平台
USE_PLATFORM = "siliconflow"  # 或 "deepseek"
```

### 第三步：核心聊天模块

**chatbot.py**：

```python
"""
聊天机器人核心模块
"""
import requests
from config import *

class ChatBot:
    """AI聊天机器人"""
    
    def __init__(self, system_prompt=None):
        """初始化机器人"""
        self.messages = []
        
        # 根据配置选择平台
        if USE_PLATFORM == "siliconflow":
            self.api_key = SILICONFLOW_API_KEY
            self.base_url = SILICONFLOW_BASE_URL
            self.model = SILICONFLOW_MODEL
        else:
            self.api_key = DEEPSEEK_API_KEY
            self.base_url = DEEPSEEK_BASE_URL
            self.model = DEEPSEEK_MODEL
        
        # 设置系统提示词
        if system_prompt:
            self.messages.append({
                "role": "system",
                "content": system_prompt
            })
    
    def chat(self, user_message):
        """发送消息并获取回复"""
        # 添加用户消息
        self.messages.append({
            "role": "user",
            "content": user_message
        })
        
        # 构建请求
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": self.messages,
            "max_tokens": 1024,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            ai_message = result["choices"][0]["message"]["content"]
            
            # 保存AI回复到历史
            self.messages.append({
                "role": "assistant",
                "content": ai_message
            })
            
            return ai_message
            
        except requests.exceptions.Timeout:
            return "请求超时，请重试"
        except requests.exceptions.RequestException as e:
            return f"请求失败: {e}"
        except Exception as e:
            return f"发生错误: {e}"
    
    def clear_history(self):
        """清空对话历史"""
        # 保留系统提示
        system_msgs = [m for m in self.messages if m["role"] == "system"]
        self.messages = system_msgs
    
    def get_history(self):
        """获取对话历史"""
        return self.messages.copy()
    
    def set_system_prompt(self, prompt):
        """设置新的系统提示"""
        # 移除旧的系统提示
        self.messages = [m for m in self.messages if m["role"] != "system"]
        # 添加新的系统提示
        self.messages.insert(0, {"role": "system", "content": prompt})


# 预设角色
ROLES = {
    "default": "你是一个有帮助的AI助手，用中文回答问题。",
    "teacher": "你是一位耐心的编程老师，用简单易懂的方式解释技术概念，多举例子。",
    "translator": "你是一位专业的中英翻译，将用户输入的中文翻译成英文，英文翻译成中文。",
    "writer": "你是一位创意写作助手，擅长写故事、诗歌和各种文案。",
    "coder": "你是一位资深程序员，帮助用户写代码、调试和解释代码。"
}
```

### 第四步：命令行版主程序

**main.py**：

```python
"""
AI聊天机器人 - 命令行版
"""
from chatbot import ChatBot, ROLES

def print_help():
    """打印帮助信息"""
    print("""
命令说明：
  /help     - 显示帮助
  /clear    - 清空对话历史
  /role     - 切换角色
  /history  - 查看对话历史
  /quit     - 退出程序
""")

def print_roles():
    """打印可用角色"""
    print("\n可用角色：")
    for name, desc in ROLES.items():
        print(f"  {name}: {desc[:30]}...")
    print()

def main():
    print("="*50)
    print("      🤖 AI聊天机器人")
    print("="*50)
    print("输入 /help 查看命令，/quit 退出\n")
    
    # 创建机器人
    bot = ChatBot(ROLES["default"])
    current_role = "default"
    
    while True:
        try:
            user_input = input("你: ").strip()
        except KeyboardInterrupt:
            print("\n再见！")
            break
        
        if not user_input:
            continue
        
        # 处理命令
        if user_input.startswith('/'):
            cmd = user_input.lower()
            
            if cmd == '/quit' or cmd == '/exit':
                print("再见！")
                break
            
            elif cmd == '/help':
                print_help()
            
            elif cmd == '/clear':
                bot.clear_history()
                print("对话历史已清空\n")
            
            elif cmd == '/role':
                print_roles()
                role_name = input("选择角色: ").strip()
                if role_name in ROLES:
                    bot.set_system_prompt(ROLES[role_name])
                    bot.clear_history()
                    current_role = role_name
                    print(f"已切换到角色: {role_name}\n")
                else:
                    print("角色不存在\n")
            
            elif cmd == '/history':
                history = bot.get_history()
                print("\n对话历史：")
                for msg in history:
                    role = msg["role"]
                    content = msg["content"][:50] + "..." if len(msg["content"]) > 50 else msg["content"]
                    print(f"  [{role}]: {content}")
                print()
            
            else:
                print("未知命令，输入 /help 查看帮助\n")
            
            continue
        
        # 发送消息
        print("AI: ", end="", flush=True)
        response = bot.chat(user_input)
        print(response)
        print()

if __name__ == "__main__":
    main()
```

### 第五步：网页版（可选进阶）

**web/index.html**：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI聊天机器人</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            font-family: "Microsoft YaHei", sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .chat-container {
            width: 100%;
            max-width: 600px;
            height: 80vh;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        
        .chat-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
        }
        
        .chat-header h1 { font-size: 1.5em; }
        
        .chat-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
        }
        
        .message {
            margin-bottom: 15px;
            display: flex;
        }
        
        .message.user { justify-content: flex-end; }
        .message.ai { justify-content: flex-start; }
        
        .message-content {
            max-width: 80%;
            padding: 12px 18px;
            border-radius: 18px;
            line-height: 1.5;
        }
        
        .user .message-content {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-bottom-right-radius: 4px;
        }
        
        .ai .message-content {
            background: #f0f0f0;
            color: #333;
            border-bottom-left-radius: 4px;
        }
        
        .chat-input {
            display: flex;
            padding: 15px;
            background: #f8f8f8;
            border-top: 1px solid #eee;
        }
        
        .chat-input input {
            flex: 1;
            padding: 15px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .chat-input button {
            margin-left: 10px;
            padding: 15px 25px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
        }
        
        .chat-input button:hover { opacity: 0.9; }
        .chat-input button:disabled { opacity: 0.5; }
        
        .typing {
            display: none;
            padding: 10px 20px;
            color: #888;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h1>🤖 AI聊天机器人</h1>
            <p>有什么可以帮你的？</p>
        </div>
        
        <div class="chat-messages" id="messages">
            <div class="message ai">
                <div class="message-content">
                    你好！我是AI助手，请问有什么可以帮你的？
                </div>
            </div>
        </div>
        
        <div class="typing" id="typing">AI正在思考...</div>
        
        <div class="chat-input">
            <input type="text" id="input" placeholder="输入消息..." 
                   onkeypress="if(event.key==='Enter') sendMessage()">
            <button onclick="sendMessage()" id="sendBtn">发送</button>
        </div>
    </div>

    <script>
        // 注意：网页版需要后端服务支持
        // 这里只是前端示例，实际需要配合Flask/FastAPI后端
        
        const messages = [];
        
        function addMessage(content, isUser) {
            const messagesDiv = document.getElementById('messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'ai'}`;
            messageDiv.innerHTML = `<div class="message-content">${content}</div>`;
            messagesDiv.appendChild(messageDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
        
        async function sendMessage() {
            const input = document.getElementById('input');
            const message = input.value.trim();
            
            if (!message) return;
            
            // 显示用户消息
            addMessage(message, true);
            input.value = '';
            
            // 显示思考中
            document.getElementById('typing').style.display = 'block';
            document.getElementById('sendBtn').disabled = true;
            
            // TODO: 调用后端API
            // 这里模拟API响应
            setTimeout(() => {
                document.getElementById('typing').style.display = 'none';
                document.getElementById('sendBtn').disabled = false;
                addMessage('这是AI的回复（需要配置后端API）', false);
            }, 1000);
        }
    </script>
</body>
</html>
```

### 第六步：依赖文件

**requirements.txt**：

```
requests>=2.28.0
```

### 第七步：Git忽略文件

**.gitignore**：

```
# API配置（包含密钥）
config.py

# Python
__pycache__/
*.pyc
.env

# IDE
.vscode/
.idea/
```

### 第八步：项目README

**README.md**：

```markdown
# 🤖 AI聊天机器人

一个基于国产大模型API的智能聊天机器人。

## 功能特性

- ✅ 多轮对话，记住上下文
- ✅ 多种角色切换（助手/老师/翻译/程序员）
- ✅ 命令行交互界面
- 🚧 网页版界面（开发中）

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API

复制 `config.example.py` 为 `config.py`，填入你的API Key：

```python
SILICONFLOW_API_KEY = "你的API Key"
```

### 3. 运行程序

```bash
python main.py
```

## 使用说明

| 命令 | 功能 |
|------|------|
| `/help` | 显示帮助 |
| `/role` | 切换角色 |
| `/clear` | 清空对话 |
| `/quit` | 退出程序 |

## 项目结构

```
ai-chatbot/
├── main.py         # 主程序
├── chatbot.py      # 核心模块
├── config.py       # 配置文件
└── requirements.txt
```

## 技术栈

- Python 3.8+
- Requests
- SiliconFlow / DeepSeek API

## 作者

你的名字

## 许可证

MIT License
```

---

## ✅ 验收检查

完成项目后，确认以下内容：

- [ ] 程序能正常运行
- [ ] 能与AI进行多轮对话
- [ ] 能切换不同角色
- [ ] 使用Git进行版本管理
- [ ] README文档完整
- [ ] 代码结构清晰

---

## 🚀 进阶挑战

如果你想继续提升，可以尝试：

1. **网页版**：用Flask/FastAPI搭建后端
2. **语音对话**：添加语音识别和合成
3. **知识库**：接入本地文档进行问答
4. **多模态**：支持图片理解
5. **部署上线**：部署到服务器让别人使用

---

## 📚 相关资源

- Flask快速入门：https://flask.palletsprojects.com/
- FastAPI教程：https://fastapi.tiangolo.com/zh/
- Gradio（快速搭建AI界面）：https://gradio.app/
