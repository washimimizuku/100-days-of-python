import os
import requests
import smtplib
import time
from datetime import datetime


MY_LAT = 47.402210 # Dietikon latitude
MY_LONG = 8.392733 # Dietikon longitude

EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def is_iss_visible():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
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
                from_addr=my_email,
                to_addr=my_email,
                msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky!")

