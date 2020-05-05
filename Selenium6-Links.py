from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://newtours.demoaut.com")

anchors = driver.find_elements_by_tag_name("a")
print("Number of Links present : ",len(anchors))

for link in anchors:
	print(link.text)  # Printing all the Links

driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[8]/td/table/tbody/tr/td[2]/font/a").click()
time.sleep(2)

ele = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/a")
if not ele.is_displayed():
	time.sleep(5)
else:
	ele.click()

time.sleep(1)

driver.find_element_by_link_text("Register here").click()
time.sleep(1)

while True:
	driver.back()
	time.sleep(1)
	driver.forward()
	time.sleep(1)

driver.quit()