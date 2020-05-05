from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("https://www.selenium.dev/selenium/docs/api/java/")

driver.switch_to_frame("packageListFrame") # 1st Frame

links = driver.find_elements_by_tag_name("a")

for link in links:
	print(link.text)

driver.find_element_by_xpath("/html/body/div[2]/ul/li[6]/a").click()

driver.switch_to_default_content() # Always switch to default content before switching to next frame

driver.switch_to_frame("packageFrame") # 2nd Frame

links1 = driver.find_elements_by_tag_name("a")

for link in links1:
	print(link.text)

driver.find_element_by_xpath("/html/body/div/ul/li[3]/a").click()

driver.switch_to_default_content()

driver.switch_to_frame("classFrame") #3rd Frame
time.sleep(2)

links2 = driver.find_elements_by_tag_name("a")

for link in links2:
	print(link.text)

driver.find_element_by_xpath("//*[@id='t2']/span[1]/a").click()