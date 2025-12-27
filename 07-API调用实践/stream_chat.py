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
