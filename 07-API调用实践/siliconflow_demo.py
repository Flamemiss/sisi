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
