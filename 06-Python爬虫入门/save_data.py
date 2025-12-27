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
