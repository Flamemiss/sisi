# 任务7：API调用实践（AI大模型）

## 🎯 任务目标

学会调用国内AI大模型API（SiliconFlow、DeepSeek），实现AI对话功能。

---

## 📋 验收标准

| 序号 | 验收项目 | 具体要求 |
|------|----------|----------|
| 1 | 账号注册 | 注册SiliconFlow或DeepSeek账号 |
| 2 | 获取API Key | 成功获取API密钥 |
| 3 | 简单调用 | 发送请求并获得AI回复 |
| 4 | 多轮对话 | 实现连续对话功能 |
| 5 | 异常处理 | 能处理API调用失败情况 |

---

## 🛠️ 平台介绍

### SiliconFlow（硅基流动）

- 官网：https://siliconflow.cn/
- 特点：聚合多个模型，有免费额度
- 支持模型：Qwen、DeepSeek、GLM等

### DeepSeek（深度求索）

- 官网：https://www.deepseek.com/
- 特点：国产大模型，性价比高
- API文档：https://platform.deepseek.com/

---

## 📝 准备工作

### 步骤1：注册账号

1. 访问 https://cloud.siliconflow.cn/ 或 https://platform.deepseek.com/
2. 注册账号（支持手机号注册）
3. 完成实名认证（如需要）

### 步骤2：获取API Key

1. 登录后进入控制台
2. 找到"API Keys"或"密钥管理"
3. 创建新的API Key
4. **妥善保管，不要泄露！**

### 步骤3：安装依赖

```cmd
pip install openai requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

## 📝 练习任务

### 练习1：SiliconFlow调用

```python
# siliconflow_demo.py
"""
SiliconFlow API调用示例
文档：https://docs.siliconflow.cn/
"""
import requests
import json

# ⚠️ 替换为你的API Key
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
API_URL = "https://api.siliconflow.cn/v1/chat/completions"

def chat(message):
    """调用SiliconFlow API"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "Qwen/Qwen2.5-7B-Instruct",  # 免费模型
        "messages": [
            {"role": "user", "content": message}
        ],
        "max_tokens": 512
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"请求失败: {e}"

# 测试
if __name__ == "__main__":
    question = "用Python写一个计算1到100求和的代码"
    print(f"问: {question}")
    print(f"\n答: {chat(question)}")
```

### 练习2：DeepSeek调用

```python
# deepseek_demo.py
"""
DeepSeek API调用示例
文档：https://platform.deepseek.com/api-docs/
"""
from openai import OpenAI

# ⚠️ 替换为你的API Key
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"

# 创建客户端
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

def chat(message):
    """调用DeepSeek API"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": message}
            ],
            max_tokens=512
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"请求失败: {e}"

# 测试
if __name__ == "__main__":
    question = "请用简单的话解释什么是API"
    print(f"问: {question}")
    print(f"\n答: {chat(question)}")
```

### 练习3：多轮对话

```python
# multi_turn_chat.py
"""
多轮对话示例（以SiliconFlow为例）
"""
import requests

API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
API_URL = "https://api.siliconflow.cn/v1/chat/completions"

class ChatBot:
    def __init__(self):
        self.messages = []
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
    
    def chat(self, user_input):
        """发送消息并获取回复"""
        # 添加用户消息
        self.messages.append({"role": "user", "content": user_input})
        
        data = {
            "model": "Qwen/Qwen2.5-7B-Instruct",
            "messages": self.messages,
            "max_tokens": 512
        }
        
        try:
            response = requests.post(API_URL, headers=self.headers, json=data, timeout=30)
            response.raise_for_status()
            result = response.json()
            
            # 获取AI回复
            ai_message = result["choices"][0]["message"]["content"]
            
            # 添加AI回复到历史
            self.messages.append({"role": "assistant", "content": ai_message})
            
            return ai_message
        except Exception as e:
            return f"请求失败: {e}"
    
    def clear(self):
        """清空对话历史"""
        self.messages = []
        print("对话历史已清空")

def main():
    bot = ChatBot()
    print("=== AI对话助手 ===")
    print("输入 'quit' 退出，'clear' 清空历史\n")
    
    while True:
        user_input = input("你: ").strip()
        
        if not user_input:
            continue
        if user_input.lower() == 'quit':
            print("再见！")
            break
        if user_input.lower() == 'clear':
            bot.clear()
            continue
        
        response = bot.chat(user_input)
        print(f"\nAI: {response}\n")

if __name__ == "__main__":
    main()
```

### 练习4：带系统提示的对话

```python
# system_prompt_chat.py
"""
自定义AI角色（系统提示）
"""
import requests

API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
API_URL = "https://api.siliconflow.cn/v1/chat/completions"

def create_assistant(system_prompt):
    """创建自定义助手"""
    messages = [{"role": "system", "content": system_prompt}]
    
    def chat(user_input):
        messages.append({"role": "user", "content": user_input})
        
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "Qwen/Qwen2.5-7B-Instruct",
            "messages": messages,
            "max_tokens": 512
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=data, timeout=30)
            result = response.json()
            ai_message = result["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": ai_message})
            return ai_message
        except Exception as e:
            return f"错误: {e}"
    
    return chat

# 创建不同角色的助手
if __name__ == "__main__":
    # 创建英语老师
    english_teacher = create_assistant(
        "你是一位友善的英语老师，用中文回答学生问题，并给出英文例句。"
    )
    
    print("=== 英语老师助手 ===\n")
    print(english_teacher("怎么用英语表达'我很开心'？"))
    print()
    print(english_teacher("还有其他说法吗？"))
```

### 练习5：流式输出

```python
# stream_chat.py
"""
流式输出示例（逐字显示）
"""
import requests

API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
API_URL = "https://api.siliconflow.cn/v1/chat/completions"

def stream_chat(message):
    """流式调用API"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [{"role": "user", "content": message}],
        "max_tokens": 512,
        "stream": True  # 开启流式输出
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data, stream=True)
        
        print("AI: ", end="", flush=True)
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith("data: ") and line != "data: [DONE]":
                    import json
                    chunk = json.loads(line[6:])
                    if chunk["choices"][0]["delta"].get("content"):
                        print(chunk["choices"][0]["delta"]["content"], end="", flush=True)
        print()  # 换行
        
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    stream_chat("写一首关于春天的短诗")
```

---

## 🔒 安全提醒

### API Key安全

```python
# ❌ 错误做法：硬编码在代码中
API_KEY = "sk-xxxxx"

# ✅ 正确做法：使用环境变量
import os
API_KEY = os.getenv("SILICONFLOW_API_KEY")

# 或使用配置文件（不要提交到Git）
# config.py（添加到.gitignore）
# API_KEY = "sk-xxxxx"
```

### 设置环境变量（Windows）

```cmd
# 临时设置（仅当前窗口有效）
set SILICONFLOW_API_KEY=sk-xxxxx

# 永久设置（系统环境变量）
# 右键"此电脑" → 属性 → 高级系统设置 → 环境变量
```

---

## ✅ 自测清单

- [ ] 成功注册并获取API Key了吗？
- [ ] 能发送请求并收到AI回复吗？
- [ ] 理解 `messages` 列表的结构吗？
- [ ] 知道 `role` 有哪几种类型吗？（user/assistant/system）
- [ ] 知道如何安全保管API Key吗？

---

## 📚 推荐资源

- SiliconFlow文档：https://docs.siliconflow.cn/
- DeepSeek文档：https://platform.deepseek.com/api-docs/
- OpenAI API格式参考：https://platform.openai.com/docs/api-reference
