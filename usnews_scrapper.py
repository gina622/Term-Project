from bs4 import BeautifulSoup
import requests
# from nytimes_scrapper import download_page

DOWNLOAD_URL = "https://www.usnews.com/news/business"

def download_page(url):
    headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
    "cache-control": "max-age=0",
    "dnt": "1",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    }
    response = requests.get(url, headers=headers, timeout=30)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    news_list = soup.find_all('div', attrs={"class" : "story"})
    news_dict = {}
    for news in news_list:
        title = news.find('h3').text
        link = news.find('a', attrs = {'class' : 'Anchor-byh49a-0 dKVMQA'})['href']
        news_dict[title] = link
    return news_dict

us_news = parse_html(download_page(DOWNLOAD_URL))

def main():
    print(parse_html(download_page(DOWNLOAD_URL)))

if __name__ == "__main__":
    main()