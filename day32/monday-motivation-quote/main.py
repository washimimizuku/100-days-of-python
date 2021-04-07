import datetime as dt
import os
import random
import smtplib
from dotenv import load_dotenv

load_dotenv()


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
QUOTES_FILE = os.path.join(LOCATION, "quotes.txt")

EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
MY_EMAIL = os.environ.get('MY_EMAIL')


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open(QUOTES_FILE) as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP(EMAIL_SERVER) as connection:
        connection.starttls()
        connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_USER,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}")
