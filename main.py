from flask import Blueprint
from __init__ import db
import configparser
import datetime
import feedparser
import requests
from flask_login import login_required, current_user

from flask import make_response, render_template, request

main = Blueprint('main', __name__)


RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'
             }

DEFAULTS = {'publication': 'bbc',
            'city': 'Dnipro, Ukraine',
            'currency_from': 'UAH',
            'currency_to': 'USD'}

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"
CURRENCY_URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


@main.route('/')
def home():
    # get customized headlines, based on user input or default
    publication = get_value_with_fallback("publication")
    articles = get_news(publication)
    # get customized weather based on user input or default
    city = get_value_with_fallback("city")
    weather = get_weather(city)
    # get customized currency based on user input or default
    currency_from = get_value_with_fallback("currency_from")
    currency_to = get_value_with_fallback("currency_to")
    rate = get_rate(currency_to)
    response = make_response(render_template("home.html", articles=articles,
                                             weather=weather, currency_to=currency_to,
                                             currency_from=currency_from, rate=rate))
    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie("publication", publication, expires=expires)
    response.set_cookie("city", city, expires=expires)
    response.set_cookie("currency_to", currency_to, expires=expires)
    return response


def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return DEFAULTS[key]


def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS["publication"]
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed["entries"]


def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openweathermap"]["api"]


def get_weather(query):
    api_key = get_api_key()
    url_api = WEATHER_URL.format(query, api_key)
    data = requests.get(url_api)
    parsed = data.json()
    weather = None
    if parsed.get("weather"):
        weather = \
            {"description": parsed["weather"][0]["description"],
             "temperature": parsed["main"]["temp"],
             "city": parsed["name"], "country": parsed["sys"]["country"]}
    return weather


def get_rate(to):
    data = requests.get(CURRENCY_URL)
    parsed = data.json()
    for row in parsed:
        if row["ccy"] == to:
            buy = row["buy"]
            sell = row["sale"]

            return f'{buy}/{sell}'


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
