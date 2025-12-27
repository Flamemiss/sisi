# fetch_with_headers.py
import requests

url = "https://www.baidu.com"

# 模拟浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
print(f"状态码: {response.status_code}")
