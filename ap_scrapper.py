from bs4 import BeautifulSoup
from nytimes_scrapper import download_page

DOWNLOAD_URL = "https://apnews.com/hub/business"


def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    news_list = soup.find('article', attrs={"data-tb-region" : "Feed Card"})
    articles = news_list.find_all('div', attrs={"data-key" : "feed-card-wire-story-with-image"})
    news_dict = {}
    for article in articles:
        box = article.find('div')
        title = box.find('h2').text
        link = "https://apnews.com" + box.find('a')['href']
        news_dict[title] = link
    return news_dict

ap_news = parse_html(download_page(DOWNLOAD_URL))

def main():
    print(parse_html(download_page(DOWNLOAD_URL)))

if __name__ == "__main__":
    main()