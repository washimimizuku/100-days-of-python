from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from selenium import webdriver
import time


IMMOSCOUT24_URL = "https://www.immoscout24.ch/en/real-estate/rent/city-zuerich?pt=2t&nrf=2"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeTCo0807OWP1hhNPIV0TIwZq7rf53pGlyPymSbZzMJSMoGQA/viewform?usp=sf_link"
CHROME_DRIVER_PATH = "vendors/chromedriver"


# Get Real Estate Properties listings
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "pt-PT,pt;q=0.9,en;q=0.8,en-US;q=0.7"
}

response = requests.get(url=IMMOSCOUT24_URL, headers=headers)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, "html.parser")

addresses = [address.text for address in soup.select("main div div div article a div div div address button span")]
prices = [link.text for link in soup.select("main div div div article a div div div h3 span")]
links = [f"https://www.immoscout24.ch/{link.get('href')}" for link in soup.select("main div div div article a")]

# Fill form
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
for i in range(len(addresses)):
    driver.get(FORM_URL)
    
    time.sleep(2)

    address_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(addresses[i])

    price_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(prices[i])

    link_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(links[i])

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()

    time.sleep(1)

driver.close()
