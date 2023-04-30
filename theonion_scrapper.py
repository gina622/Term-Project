from bs4 import BeautifulSoup
from nytimes_scrapper import download_page

DOWNLOAD_URL = "https://www.theonion.com/tag/business"


def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    news_list = soup.find('div', attrs={"class" : "sc-17uq8ex-0 fakHlO"})
    articles = news_list.find_all('article')
    news_dict = {}
    for article in articles:
        box = article.find('div', attrs={'class' : 'sc-cw4lnv-13 hHSpAQ'})
        text = box.find('div', attrs = {'class' : 'sc-cw4lnv-10 blRKje'})
        title_div = text.find('div', attrs = {'class' : 'sc-cw4lnv-5 dYIPCV'})
        link = title_div.find('a')['href']
        news_dict[title_div.text] = link
    return news_dict


theonion_news = parse_html(download_page(DOWNLOAD_URL))


def main():
    print(parse_html(download_page(DOWNLOAD_URL)))

if __name__ == "__main__":
    main()