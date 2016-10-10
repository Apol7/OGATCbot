from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

productKeyword = 'Reversible Hooded'
supreme = 'http://www.supremenewyork.com/shop/all'
category = '/jackets'
desiredColor = "Black"

print(datetime.datetime.now())
driver = webdriver.Chrome()
driver.get(supreme + category)

specificproduct = driver.find_element_by_partial_link_text(productKeyword)
print(supreme + category + specificproduct.get_attribute("href"))
driver.get(specificproduct.get_attribute("href"))


specificProductColor = driver.find_element_by_css_selector('[data-style-name="Black"]')
print(supreme + category + specificProductColor.get_attribute("href"))
driver.get(specificProductColor.get_attribute("href"))


#elem.send_keys("level 12, right here")
#elem.send_keys(Keys.RETURN)
#time.sleep(2)

print(datetime.datetime.now())


