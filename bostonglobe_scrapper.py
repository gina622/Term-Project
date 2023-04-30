from bs4 import BeautifulSoup
from nytimes_scrapper import download_page

DOWNLOAD_URL = "https://www.bostonglobe.com/business/"



def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    news_list = soup.find_all('div', attrs={"class" : "section_feed_item | no-padding font_primary"})
    news_dict = {}
    for news in news_list:
        title = news.find('h4').text
        link = "https://www.bostonglobe.com" + news.find('a', attrs={"class" : "color_main"})['href']
        news_dict[title] = link
    # print(link.prettify())
    return news_dict

bostonglobe_news = parse_html(download_page(DOWNLOAD_URL))

def main():
    print(parse_html(download_page(DOWNLOAD_URL)))

if __name__ == "__main__":
    main()