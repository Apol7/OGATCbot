from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

import time
import datetime
import contextlib
import sys
#import sys.argv


productKeyword = 'Astronaut'
supreme = 'http://www.supremenewyork.com/shop/all'
category = '/jackets'
desiredColor = "Black"
desiredSize = "Medium"
billingNameGiven = "Alex Dude"
emailGiven = "a@gmail.com"
telephoneGiven = "12345678910"
addressGiven = "bla"
zipGiven = "94062"
cityGiven = "Communist Heaven"
stateGiven = "CA"
countryGiven = "USA"
cardType = "Visa"
cardNumber = "1111111111111111"
cardMonth = "05"
cardYear = "2019"
cardCSV = "111"

print(datetime.datetime.now())
driver = webdriver.Chrome()
driver.get(supreme)

goButton = raw_input("Type y and hit enter if you are ready for SUPREME")
print("you entered y") ,goButton

driver.get(supreme + category)

def finditem():
    try:
        specificproduct = driver.find_element_by_partial_link_text(productKeyword)
    except:
        print("could not find" + productKeyword)
        driver.get(supreme + category)
        finditem()

finditem()

print(supreme + category + specificproduct.get_attribute("href"))
driver.get(specificproduct.get_attribute("href"))

specificProductColor = driver.find_element_by_css_selector('[data-style-name=' + desiredColor + ']')
print(supreme + category + specificProductColor.get_attribute("href"))
driver.get(specificProductColor.get_attribute("href"))

selectSize = Select(driver.find_element_by_id("size"))
selectSize.select_by_visible_text(desiredSize)

driver.find_element_by_name('commit').click()
time.sleep(.3)
driver.get('http://www.supremenewyork.com/checkout')

billingNameField = driver.find_element_by_id('order_billing_name')
billingNameField.send_keys(billingNameGiven)

emailField = driver.find_element_by_id('order_email')
emailField.send_keys(emailGiven)

telephoneField = driver.find_element_by_id('order_tel')
telephoneField.send_keys(telephoneGiven)

addressField = driver.find_element_by_id('bo')
addressField.send_keys(addressGiven)

zipField = driver.find_element_by_id('order_billing_zip')
zipField.send_keys(zipGiven)

cityField = driver.find_element_by_id('order_billing_city')
cityField.send_keys(cityGiven)

selectState = Select(driver.find_element_by_id('order_billing_state'))
selectState.select_by_visible_text(stateGiven)

selectCountry = Select(driver.find_element_by_id('order_billing_country'))
selectCountry.select_by_visible_text(countryGiven)

select = Select(driver.find_element_by_id("credit_card_type"))
select.select_by_visible_text(cardType)

cardNumberField = driver.find_element_by_id("cnb")
cardNumberField.send_keys(cardNumber)

select = Select(driver.find_element_by_id("credit_card_month"))
select.select_by_visible_text(cardMonth)

select = Select(driver.find_element_by_id("credit_card_year"))
select.select_by_visible_text(cardYear)

cardCSVField = driver.find_element_by_id("vval")
cardCSVField.send_keys(cardCSV)

time.sleep(.1)
driver.find_element_by_id("order_terms").click()
time.sleep(.1)
driver.find_element_by_name("commit").click()

#elem.send_keys("level 12, right here")
#elem.send_keys(Keys.RETURN)
#time.sleep(2)


print(datetime.datetime.now())
