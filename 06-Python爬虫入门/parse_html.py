# parse_html.py
from bs4 import BeautifulSoup
import requests

url = "https://www.baidu.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

# 创建BeautifulSoup对象
soup = BeautifulSoup(response.text, 'html.parser')

# 获取页面标题
title = soup.title.string
print(f"页面标题: {title}")

# 获取所有链接
print("\n页面中的链接:")
for link in soup.find_all('a')[:10]:  # 只取前10个
    href = link.get('href')
    text = link.get_text().strip()
    if href and text:
        print(f"  {text}: {href}")
