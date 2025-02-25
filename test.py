from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
visited = set()
start_url = 'https://loigiaihay.com/soan-bai-buoc-vao-doi-sgk-ngu-van-12-tap-2-ket-noi-tri-thuc-a161956.html'
to_crawl = [start_url]
articles_crawled = 0
max_articles = 10
while to_crawl and articles_crawled < max_articles:
    url = to_crawl.pop(0)
    if url in visited:
        continue
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        print(response.text)
    except requests.RequestException as e:
            print(f"Lỗi khi crawl {url}: {e}")