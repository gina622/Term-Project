from bs4 import BeautifulSoup
from nytimes_scrapper import download_page

DOWNLOAD_URL = "https://www.cnbc.com/business/"


def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    news_list = soup.find('div', attrs={"class" : "PageBuilder-col-9"})
    articles = news_list.find_all('div', attrs={"data-test" : "Card"})
    news_dict = {}
    for article in articles:
        box = article.find('div', attrs={"class" : "Card-textContent"})
        # print(box)
        if box != None:
            content = box.find('div', attrs={"class" : "Card-titleContainer"})
        title = content.text
        link = content.find('a')['href']
        news_dict[title] = link
    return news_dict

cnbc_news = parse_html(download_page(DOWNLOAD_URL))

def main():
    print(parse_html(download_page(DOWNLOAD_URL)))

if __name__ == "__main__":
    main()