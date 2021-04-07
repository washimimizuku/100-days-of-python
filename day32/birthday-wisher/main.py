import datetime as dt
import os
import pandas
import random
import smtplib
from dotenv import load_dotenv

load_dotenv()


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
BIRTHDAYS_FILE = os.path.join(LOCATION, "birthdays.csv")
TEMPLATES_FILES = [
    os.path.join(LOCATION, "letter_templates/letter_1.txt"),
    os.path.join(LOCATION, "letter_templates/letter_2.txt"),
    os.path.join(LOCATION, "letter_templates/letter_3.txt")
]

EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv(BIRTHDAYS_FILE)
birthdays = {(row.month, row.day): row for (index, row) in data.iterrows() }

if today in birthdays:
    person = birthdays[today]
    template = random.choice(TEMPLATES_FILES)
    with open(template) as file:
        template_text = file.read()
    template_text = template_text.replace("[NAME]", person["name"])

    with smtplib.SMTP(EMAIL_SERVER) as connection:
        connection.starttls()
        connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_USER,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday!\n\n{template_text}"
        )
