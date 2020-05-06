from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://newtours.demoaut.com")

driver.save_screenshot("/Users/shreyas_rl/Desktop/git/Selenium-Python/SS/homepage.png")


driver.quit()