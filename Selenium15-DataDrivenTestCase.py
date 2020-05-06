import XLUtils as xlu
from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://newtours.demoaut.com")

path = "data3.xlsx"

rows = xlu.getRowCount(path,'Sheet1')
cols = xlu.getColCount(path,'Sheet1')

print(rows,cols)

def ddt(userName,userPass):

	driver.find_element_by_name("userName").send_keys(userName)
	driver.find_element_by_name("password").send_keys(userPass)
	driver.find_element_by_name("login").click()
	if driver.title == "Find a Flight: Mercury Tours:":
		print("Test Case Passed!")
		xlu.writeDataIntoFile(path,'Sheet1',r,3,'Test Passed')
	else:
		print("Test Case Failed!")
		xlu.writeDataIntoFile(path,'Sheet1',r,3,'Test Failed')

	driver.find_element_by_link_text("Home").click()


for r in range(2,rows+1):
	userName = xlu.readFileData(path,'Sheet1',r,1)
	userPass = xlu.readFileData(path,'Sheet1',r,2)

	result = ddt(userName,userPass)


time.sleep(5)
driver.quit()