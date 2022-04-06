import os
import requests
import smtplib
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


MY_LATITUDE = os.environ.get('MY_LATITUDE')
MY_LONGITUDE = os.environ.get('MY_LONGITUDE')

EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
MY_EMAIL = os.environ.get('MY_EMAIL')


def is_iss_visible():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LATITUDE -5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE -5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if is_iss_visible() and is_night():
        with smtplib.SMTP(EMAIL_SERVER) as connection:
            connection.starttls()
            connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_USER,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky!")
