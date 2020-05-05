from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://localhost/table.php")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))   # Edited xpath of first tr

print("nRows = ",rows)

col = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print("nCols = ",col)

print("Month" + "     " + "Earnings" + "     " + "Savings")

for r in range(2,rows+1):
	for c in range(1,col+1):
		ele = driver.find_element_by_xpath("/html/body/table/tbody/tr" + str([r]) + "/td" + str([c]))
		print(ele.text,end = "     ")
	print()

time.sleep(5)
driver.quit()