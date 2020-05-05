from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)  # TItle of Page
print(driver.current_url)

#print(driver.page_source) # HTML of Page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

#driver.close() # Closes only Parent Window

driver.quit()  #Closes all Windows
