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
