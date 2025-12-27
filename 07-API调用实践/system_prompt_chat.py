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
