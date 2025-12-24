# 任务6：Python爬虫入门

## 🎯 任务目标

学会用Python获取网页数据，并提取有用信息保存下来。

---

## 📋 验收标准

| 序号 | 验收项目 | 具体要求 |
|------|----------|----------|
| 1 | 库安装 | 成功安装 requests 和 beautifulsoup4 |
| 2 | 获取网页 | 用requests获取网页HTML内容 |
| 3 | 解析HTML | 用BeautifulSoup提取标题、链接 |
| 4 | 数据保存 | 将爬取数据保存为文件 |
| 5 | 异常处理 | 能处理网络错误情况 |

---

## ⚠️ 重要提醒

**爬虫道德与法律**：

1. 遵守网站的 `robots.txt` 规则
2. 控制爬取频率，不要给服务器造成压力
3. 仅用于学习目的，不爬取敏感信息
4. 部分网站禁止爬虫，请遵守网站规定

---

## 🛠️ 环境准备

```cmd
pip install requests beautifulsoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

## 📝 练习任务

### 练习1：获取网页内容

```python
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
```

### 练习2：添加请求头

某些网站会检测请求来源，需要添加请求头模拟浏览器：

```python
# fetch_with_headers.py
import requests

url = "https://www.baidu.com"

# 模拟浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
print(f"状态码: {response.status_code}")
```

### 练习3：解析HTML

```python
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
```

### 练习4：爬取天气信息

```python
# weather_crawler.py
import requests
from bs4 import BeautifulSoup

def get_weather():
    """爬取天气信息（示例用中国天气网）"""
    
    # 北京天气页面
    url = "http://www.weather.com.cn/weather1d/101010100.shtml"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 尝试获取天气信息
        print("=== 天气页面爬取成功 ===")
        print(f"页面标题: {soup.title.string}")
        
        # 注意：实际网页结构可能变化，需要根据实际情况调整选择器
        
    except requests.RequestException as e:
        print(f"请求失败: {e}")

if __name__ == "__main__":
    get_weather()
```

### 练习5：爬取并保存数据

```python
# save_data.py
import requests
from bs4 import BeautifulSoup
import json
import csv

def crawl_and_save():
    """爬取数据并保存为多种格式"""
    
    # 示例：爬取一个简单页面
    url = "https://www.example.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取数据
        data = {
            "title": soup.title.string if soup.title else "无标题",
            "url": url,
            "paragraphs": [p.get_text().strip() for p in soup.find_all('p')]
        }
        
        # 保存为JSON
        with open('result.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("已保存到 result.json")
        
        # 保存为文本
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(f"标题: {data['title']}\n")
            f.write(f"网址: {data['url']}\n")
            f.write("\n段落内容:\n")
            for i, p in enumerate(data['paragraphs'], 1):
                f.write(f"{i}. {p}\n")
        print("已保存到 result.txt")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    crawl_and_save()
```

### 练习6：完整爬虫模板

```python
# crawler_template.py
"""
通用爬虫模板
"""
import requests
from bs4 import BeautifulSoup
import time
import json

class SimpleCrawler:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        self.session = requests.Session()
    
    def fetch(self, url):
        """获取网页内容"""
        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()  # 检查HTTP错误
            response.encoding = response.apparent_encoding  # 自动检测编码
            return response.text
        except requests.RequestException as e:
            print(f"请求失败 [{url}]: {e}")
            return None
    
    def parse(self, html):
        """解析HTML（子类重写此方法）"""
        soup = BeautifulSoup(html, 'html.parser')
        return {
            "title": soup.title.string if soup.title else None,
            "links": [a.get('href') for a in soup.find_all('a', href=True)]
        }
    
    def save(self, data, filename):
        """保存数据"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已保存到 {filename}")
    
    def run(self, url):
        """运行爬虫"""
        print(f"正在爬取: {url}")
        html = self.fetch(url)
        if html:
            data = self.parse(html)
            self.save(data, 'output.json')
            return data
        return None

# 使用示例
if __name__ == "__main__":
    crawler = SimpleCrawler()
    result = crawler.run("https://www.example.com")
    if result:
        print(f"爬取成功！获取到 {len(result.get('links', []))} 个链接")
```

---

## 🔧 常用方法速查

### Requests

| 方法 | 作用 |
|------|------|
| `requests.get(url)` | GET请求 |
| `response.text` | 获取文本内容 |
| `response.json()` | 解析JSON |
| `response.status_code` | 状态码 |

### BeautifulSoup

| 方法 | 作用 |
|------|------|
| `soup.find('tag')` | 找第一个标签 |
| `soup.find_all('tag')` | 找所有标签 |
| `soup.select('css选择器')` | CSS选择器 |
| `tag.get_text()` | 获取文本 |
| `tag.get('属性')` | 获取属性值 |

---

## ✅ 自测清单

- [ ] 知道 `requests.get()` 如何发送请求吗？
- [ ] 知道为什么要添加 User-Agent 请求头吗？
- [ ] 能用 BeautifulSoup 提取网页标题吗？
- [ ] 知道 `find()` 和 `find_all()` 的区别吗？
- [ ] 能把爬取的数据保存到文件吗？

---

## 📚 推荐资源

- Requests文档：https://docs.python-requests.org/zh_CN/latest/
- BeautifulSoup文档：https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
- 崔庆才爬虫教程：https://cuiqingcai.com/
