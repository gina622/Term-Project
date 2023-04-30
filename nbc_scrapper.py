from bs4 import BeautifulSoup
from nytimes_scrapper import download_page

DOWNLOAD_URL = "https://www.nbcnews.com/business"

def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    news_list = soup.find('ul', attrs={'class' : 'styles_items__Ldw92'})
    news_content = news_list.find_all('li')
    news_dict = {}
    for content in news_content:
        box = content.find_all('div')[2]
        title = box.find('h2').text
        # print(title)
        link = box.find('a')['href']
        # print(link)
        news_dict[title] = link
    return news_dict

nbc_news = parse_html(download_page(DOWNLOAD_URL))

def main():
    print(parse_html(download_page(DOWNLOAD_URL)))

if __name__ == "__main__":
    main()