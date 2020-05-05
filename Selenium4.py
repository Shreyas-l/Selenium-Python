from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com")

driver.find_element_by_xpath("//*[@id='tab-flight-tab-hp']").click()

driver.find_element_by_xpath("//*[@id='flight-type-roundtrip-label-hp-flight']").click()

driver.find_element_by_xpath("//*[@id='flight-origin-hp-flight']").send_keys("SFO")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='flight-destination-hp-flight']").send_keys("NYC")
time.sleep(2)

driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("06/20/2020")
time.sleep(2)
driver.find_element_by_id("flight-returning-hp-flight").click()

count=0
while count!=10:
	driver.find_element_by_id("flight-returning-hp-flight").send_keys(Keys.BACKSPACE)
	count+=1

driver.find_element_by_id("flight-returning-hp-flight").send_keys("06/27/202")

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

wait = WebDriverWait(driver,10)

element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stops']/div/div[3]/div/label"))) # Explicit Wait

element.click()

time.sleep(3)

driver.quit()