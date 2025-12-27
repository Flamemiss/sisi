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
