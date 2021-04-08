import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_EMAIL = os.environ.get('LINKEDIN_EMAIL')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD')
MY_PHONE = os.environ.get('MY_PHONE')
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=106693272&keywords=software%20engineering%20manager&location=Switzerland"
CHROME_DRIVER_PATH = "vendors/chromedriver"


driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(LINKEDIN_URL)

time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(LINKEDIN_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(LINKEDIN_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
remember_me_button = driver.find_element_by_class_name("btn__primary--large")
remember_me_button.click()

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(MY_PHONE)
        
        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
            print("Application submitted.")

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

