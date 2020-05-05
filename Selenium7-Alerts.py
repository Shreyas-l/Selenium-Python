from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

alertEle = driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button")

while True:
	alertEle.click()

	time.sleep(1)

	driver.switch_to_alert().accept()

	time.sleep(1)

	alertEle.click()

	time.sleep(1)

	driver.switch_to_alert().dismiss()

