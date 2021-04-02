import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()


MY_LATITUDE = os.environ.get('MY_LATITUDE')
MY_LONGITUDE = os.environ.get('MY_LONGITUDE')

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
