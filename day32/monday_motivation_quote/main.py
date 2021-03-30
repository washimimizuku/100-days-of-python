import datetime as dt
import os
import random
import smtplib


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
QUOTES_FILE = os.path.join(LOCATION, "quotes.txt")

EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


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
        from_addr=my_email,
        to_addr="someone@example.com",
        msg=f"Subject:Monday Motivation\n\n{quote}}")
