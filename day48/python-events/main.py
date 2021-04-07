from selenium import webdriver
from pprint import pprint

CHROME_DRIVER_PATH = "vendors/chromedriver"
WEB_PAGE="https://www.python.org/"


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(WEB_PAGE)

events_raw = driver.find_elements_by_css_selector("div.event-widget div.shrubbery ul li")
events = [{"date": event.text.split("\n")[0], "name": event.text.split("\n")[1]} for event in events_raw]
pprint(events)

driver.close()
