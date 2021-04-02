import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
OPENWEATHER_API_ENDPOINT = os.environ.get('OPENWEATHER_API_ENDPOINT')

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

MY_LATITUDE = os.environ.get('MY_LATITUDE')
MY_LONGITUDE = os.environ.get('MY_LONGITUDE')
MY_PHONE = os.environ.get('MY_PHONE')

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "exclude": "current,minutely,daily",
    "appid": OPENWEATHER_API_KEY,
}

response = requests.get(OPENWEATHER_API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12] # Next 12 hours

will_rain = False
for hour_data in weather_slice:
    condition_code = int(hour_data['weather'][0]['id'])
    print(hour_data['weather'])
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("It's going to rain today. Remember to bring an ☔️.")
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
                     body="It's going to rain today. Remember to bring an ☔️.",
                     from_=TWILIO_PHONE_NUMBER,
                     to=MY_PHONE
                 )
    print(message.status)
else:
    print("It's not going to rain today. Remeber to bring your 😎.'")
