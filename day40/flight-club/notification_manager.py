import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

MY_PHONE = os.environ.get('MY_PHONE')


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_SERVER) as connection:
            connection.starttls()
            connection.login(EMAIL_USER, EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=EMAIL_USER,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )