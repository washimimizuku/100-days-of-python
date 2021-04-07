import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

CHROME_DRIVER_PATH = "vendors/chromedriver"
WEB_PAGE="http://secure-retreat-92358.herokuapp.com/"
MY_EMAIL = os.environ.get("MY_EMAIL")

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(WEB_PAGE)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Nuno")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Barreto")
email = driver.find_element_by_name("email")
email.send_keys(MY_EMAIL)

submit_button = driver.find_element_by_css_selector("button.btn")
submit_button.click()


driver.close()
