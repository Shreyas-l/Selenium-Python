from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://newtours.demoaut.com")

userNameEle = driver.find_element_by_name("userName")

print(userNameEle.is_displayed())  # Returns True/False based on element status
print(userNameEle.is_enabled())

userPassEle = driver.find_element_by_name("password")

print(userPassEle.is_displayed())  # Returns True/False based on element status
print(userPassEle.is_enabled())

userNameEle.send_keys("mercury")
userPassEle.send_keys("mercury")

driver.find_element_by_name("login").click()

roundTripRadioEle = driver.find_element_by_css_selector("input[value=roundtrip]")
print(roundTripRadioEle.is_selected() )

oneWayRadioEle = driver.find_element_by_css_selector("input[value=oneway]")
print(oneWayRadioEle.is_selected() )

time.sleep(5)
#driver.quit()