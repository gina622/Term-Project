from flask import Flask, render_template, request
from nytimes_scrapper import times_news
from theonion_scrapper import theonion_news
from nbc_scrapper import nbc_news
from ap_scrapper import ap_news
from cnbc_scrapper import cnbc_news
from bostonglobe_scrapper import bostonglobe_news
from usnews_scrapper import us_news

app = Flask(__name__)

@app.route('/')
def news():
    return render_template("index.html", times_news = times_news, theonion_news = theonion_news, nbc_news = nbc_news, ap_news = ap_news, cnbc_news = cnbc_news, bostonglobe_news = bostonglobe_news, us_news = us_news)

@app.route('/newsource', methods = ["POST", "GET"])
def get_source():
    if request.method == "POST":
        source = request.form.get("source")
    return render_template(f'{source}.html', times_news = times_news, theonion_news = theonion_news, nbc_news = nbc_news, ap_news = ap_news, cnbc_news = cnbc_news, bostonglobe_news = bostonglobe_news, us_news = us_news)


if __name__ == "__main__":
    app.run(debug=True)