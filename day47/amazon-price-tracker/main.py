from bs4 import BeautifulSoup
import os
import requests
from requests_html import HTMLSession
import smtplib
from dotenv import load_dotenv

load_dotenv()


TARGET_PRODUCT_PAGE="https://www.amazon.com/Nikon-D610-FX-Format-Digital-Camera/dp/B00FOTF8M2/ref=sr_1_2?dchild=1&keywords=nikon&qid=1617797977&sr=8-2"
BUY_PRICE = 900

EMAIL_SERVER = os.environ.get('EMAIL_SERVER')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
MY_EMAIL = os.environ.get('MY_EMAIL')

session = HTMLSession()
response = session.get(TARGET_PRODUCT_PAGE)
response.html.render()
html = response.html.html

soup = BeautifulSoup(html, "html.parser")
price = soup.find(name="span", id="priceblock_ourprice").getText()
price = float(price.replace('$', '').replace(',', ''))

title = soup.find(id="productTitle").get_text().strip()

if price < BUY_PRICE:
    message = f"{title} is now ${price}"

    with smtplib.SMTP(EMAIL_SERVER, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_USER, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_USER,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{TARGET_PRODUCT_PAGE}"
        )
