import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "vendors/chromedriver"
WEB_PAGE="https://en.wikipedia.org/wiki/Main_Page"


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(WEB_PAGE)

article_count = driver.find_element_by_css_selector("#articlecount a")
article_count.click()

for handle in driver.window_handles:
    driver.switch_to_window(handle)

time.sleep(1)

main_page = driver.find_element_by_link_text("Main page")
main_page.click()

time.sleep(1)

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


driver.close()
