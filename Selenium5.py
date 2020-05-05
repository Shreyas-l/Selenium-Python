from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("http://localhost/bioData.php")

#print(driver.page_source)

#Find No. of InputBoxes

no_ib = driver.find_elements_by_class_name("text_field")
print(len(no_ib))

driver.find_element_by_id("fname").send_keys("Abc")
time.sleep(1)
driver.find_element_by_id("lname").send_keys("Xyz")
time.sleep(1)
driver.find_element_by_id("addr").send_keys("A huvi hidv dhv ihi uvhid uvh iusdvih iu dvi is i his hhu fehfivbc")
time.sleep(1)

status = driver.find_element_by_id("male").is_selected()
print(status)
driver.find_element_by_id("male").click()
statusS = status = driver.find_element_by_id("male").is_selected()
print(statusS)
time.sleep(1)

driver.find_element_by_id("vehicle2").click()
time.sleep(1)
driver.find_element_by_id("vehicle3").click()
time.sleep(1)

options = driver.find_elements_by_tag_name("option")
print(len(options))

for option in options:
	print(option.text)   # Display all dropdown options

driver.find_element_by_css_selector("option[value=eve]").click()



time.sleep(5)
driver.quit()