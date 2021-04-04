import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWSAPI_API_KEY = os.environ.get('NEWSAPI_API_KEY')
TIME_SERIES_DAILY = "Time Series (Daily)"

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
MY_PHONE = os.environ.get('MY_PHONE')

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,
}
stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
stock_data_list = [value for (key, value) in stock_data[TIME_SERIES_DAILY].items()]
day_before_yesterday_closing_price = float(stock_data_list[1]["4. close"])
yesterday_closing_price = float(stock_data_list[0]["4. close"])

price_difference = yesterday_closing_price - day_before_yesterday_closing_price
price_difference_absolute = abs(price_difference)
price_difference_percentage = price_difference_absolute / yesterday_closing_price * 100

if price_difference_percentage > 0.1:
    # Get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWSAPI_API_KEY,
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    recent_news = news_data["articles"][:3]
    
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    up_down_symbol = "🔺"
    if price_difference < 0:
        up_down_symbol = "🔻"

    formatted_articles = [f"{STOCK}: {up_down_symbol}{round(price_difference_percentage, 2)}%\nHeadline: {article['title']}\Brief: {article['description']}" for article in recent_news]
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE
        )