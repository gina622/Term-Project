import requests
from bs4 import BeautifulSoup 

DOWNLOAD_URL = "https://www.nytimes.com/section/business"

def download_page(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    news_list = soup.find('ol', attrs={"aria-live" : "off"})
    news_content = news_list.find_all('li')
    news_dict = {}
    for content in news_content:
        title = content.find('h2')
        link = "https://www.nytimes.com" + content.find('a')['href']
        news_dict[title.text] = link
    return news_dict
    # news_headings = news_list.find_all('h2')
    # news_link = news_list.find('a')['href']
    # news_dict = {}
    # for heading in news_headings:
    #     news_dict['title'] = heading
    return times_news

times_news = parse_html(download_page(DOWNLOAD_URL)) # This is a list of NYTimes article titles

# def index(req):
#     return render(req, 'index.html', {'times_news': times_news})

def main():
    print(parse_html(download_page(DOWNLOAD_URL)))

if __name__ == "__main__":
    main()