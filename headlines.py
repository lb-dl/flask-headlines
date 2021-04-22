import configparser
import feedparser
import requests

from flask import Flask, render_template, request



app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'
             }

DEFAULTS = {'publication': 'bbc',
            'city': 'Dnipro, Ukraine'}


@app.route('/')
def home():
    # get customized headlines, based on user input or default
    publication = request.args.get('publication')
    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)
    # get customized weather based on user input or default
    city = request.args.get('city')
    print(f'city: {city}')
    if not city:
        city = DEFAULTS['city']
    weather = get_weather(city)
    return render_template("home.html", articles=articles, weather=weather)



def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS["publication"]
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']



def get_weather(query):
    api_key = get_api_key()
    url_api = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(query, api_key)
    data = requests.get(url_api)
    parsed = data.json()
    weather = None
    if parsed.get('weather'):
        weather = \
            {'description': parsed['weather'][0]['description'],
             'temperature': parsed['main']['temp'],
             'city': parsed['name'], 'country': parsed['sys']['country']}
    return weather



if __name__ == '__main__':
    app.run(port=5000, debug=True)
