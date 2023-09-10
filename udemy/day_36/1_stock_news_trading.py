import datetime
import requests
import math
import os
from twilio.rest import Client

ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_KEY = os.environ.get("ALPHAVANTAGE_KEY")
FUNCTION_NAME = "TIME_SERIES_DAILY"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

NUMBER_FROM = os.environ.get("NUMBER_FROM")
NUMBER_TO = os.environ.get("NUMBER_TO")

alphavantage_param = {
    "function": FUNCTION_NAME,
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_KEY
}

response = requests.get(url=ALPHAVANTAGE_ENDPOINT, params=alphavantage_param)
response.raise_for_status()
daily_stock_data = response.json()['Time Series (Daily)']

# yesterday_closing_price = stock_data
yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
two_days_ago = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")

yesterday_price = float(daily_stock_data[yesterday]["4. close"])
two_days_ago_price = float(daily_stock_data[two_days_ago]["4. close"])

final_statistic = ""
final_value = 0
final_percent = 0

if yesterday_price == two_days_ago_price:
    final_statistic = "🟰"
    final_value = round(yesterday_price, 4)
elif yesterday_price > two_days_ago_price:
    final_statistic = "🔺"
    final_value = round(yesterday_price - two_days_ago_price, 4)
    final_percent = round(final_value / yesterday_price * 100, 2)
elif yesterday_price < two_days_ago_price:
    final_statistic = "🔻"
    final_value = math.fabs(round(yesterday_price - two_days_ago_price, 4))
    final_percent = math.fabs(round(final_value / yesterday_price * 100, 2))

if abs(final_percent) > 1:  # Change to 5
    newsapi_param = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    newsapi_response = requests.get(url=NEWS_API_ENDPOINT, params=newsapi_param)
    newsapi_response.raise_for_status()
    newsapi_data = newsapi_response.json()

    news_list = []
    for i in range(3):
        obj = {
            "author": newsapi_data["articles"][i]["author"],
            "title": newsapi_data["articles"][i]["title"],
            "description": newsapi_data["articles"][i]["description"],
            "content": newsapi_data["articles"][i]["content"],
        }
        news_list.append(obj)

    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for news in news_list:
        string_message = (f"{STOCK}: {final_statistic} {final_percent}\n"
                          f"Headline: {news['title']}\n"
                          f"Brief: {news['description']}\n")

        sms = twilio_client.messages.create(
            body=string_message,
            from_=NUMBER_FROM,
            to=NUMBER_TO)
        print(sms.sid)
