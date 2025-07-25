import requests
from bs4 import BeautifulSoup

def search_articles(keyword: str):
    url = f"https://search.naver.com/search.naver?query={keyword}&where=news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for item in soup.select(".news_area"):
        title_elem = item.select_one(".news_tit")
        if title_elem:
            results.append({
                "title": title_elem.get_text(),
                "url": title_elem['href']
            })
    return results
