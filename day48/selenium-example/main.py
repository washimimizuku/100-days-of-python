from selenium import webdriver

CHROME_DRIVER_PATH = "vendors/chromedriver"
TARGET_PRODUCT_PAGE="https://www.amazon.com/Nikon-D610-FX-Format-Digital-Camera/dp/B00FOTF8M2/ref=sr_1_2?dchild=1&keywords=nikon&qid=1617797977&sr=8-2"


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(TARGET_PRODUCT_PAGE)

# By ID
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

# By name (for form fields)
search_field = driver.find_element_by_name("field-keywords")
print(search_field.tag_name)
print(search_field.get_attribute("name"))

# By class name
logo = driver.find_element_by_class_name("nav-logo-link")
print(logo.size)

# By CSS Selector
link = driver.find_element_by_css_selector(".a-list-item a")
print(link.text)
print(link.get_attribute('href'))

# By Xpath
link2 = driver.find_element_by_xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[4]')
print(link2.text)

# Plural 'elements' allow to get lists, applies to all above
links = driver.find_elements_by_css_selector(".a-list-item a")
for link in links:
    print(link.text)

driver.close() # driver.quit() would quit the browser
