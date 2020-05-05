from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

time.sleep(2)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()  

print(driver.current_window_handle)  # CDwindow-878BDB222285FB83E5ADF035C5EAEC8A  Parent Window

handles = driver.window_handles  # Returns Handle Values of All Open Windows

for handle in handles:
	driver.switch_to.window(handle)
	print(driver.title)
	if driver.title == "Sakinalium | Home":
		driver.close() # Close current window


time.sleep(5)
driver.quit()