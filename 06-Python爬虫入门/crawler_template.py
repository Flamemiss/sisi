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
