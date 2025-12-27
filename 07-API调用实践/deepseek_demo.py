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
