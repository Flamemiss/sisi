# fetch_page.py
import requests

# 目标网址（百度为例）
url = "https://www.baidu.com"

# 发送请求
response = requests.get(url)

# 查看状态码（200表示成功）
print(f"状态码: {response.status_code}")

# 查看网页内容（前500字符）
print(f"\n网页内容预览:\n{response.text[:500]}")
