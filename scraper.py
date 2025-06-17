import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_dantri():
    # URL của trang Dân trí
    url = "https://dantri.com.vn/"
    
    try:
        # Gửi request đến trang web
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        # Kiểm tra status code
        if response.status_code == 200:
            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Lấy các bài viết mới nhất
            articles = []
            news_items = soup.find_all('article', class_='article-item')
            
            for item in news_items[:10]:  # Lấy 10 bài viết đầu tiên
                try:
                    title = item.find('h3', class_='article-title').text.strip()
                    link = item.find('a')['href']
                    if not link.startswith('http'):
                        link = 'https://dantri.com.vn' + link
                    
                    articles.append({
                        'title': title,
                        'link': link,
                        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                except Exception as e:
                    print(f"Lỗi khi xử lý bài viết: {str(e)}")
                    continue
            
            # Lưu kết quả vào file JSON
            with open('dantri_news.json', 'w', encoding='utf-8') as f:
                json.dump(articles, f, ensure_ascii=False, indent=4)
            
            return articles
            
        else:
            print(f"Lỗi khi truy cập trang web. Status code: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")
        return None

if __name__ == "__main__":
    print("Đang cào dữ liệu từ Dân trí...")
    results = scrape_dantri()
    if results:
        print(f"Đã cào thành công {len(results)} bài viết")
        print("Dữ liệu đã được lưu vào file dantri_news.json") 