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
