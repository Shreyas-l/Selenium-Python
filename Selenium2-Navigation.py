from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://newtours.demoaut.com")

print(driver.title)

driver.get("https://www.apple.com/")

print(driver.title)

while True:
	driver.back()

	print(driver.title)

	time.sleep(5)

	driver.forward()

	print(driver.title)

	time.sleep(5)