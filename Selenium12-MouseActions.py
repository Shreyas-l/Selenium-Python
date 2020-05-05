from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(2)
 
driver.find_element_by_id("txtUsername").send_keys("Admin")
time.sleep(2)
 
driver.find_element_by_id("txtPassword").send_keys("admin123")
time.sleep(1)
 
driver.find_element_by_id("btnLogin").click()
time.sleep(2)
 
admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
usrMgmt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
 
actions = ActionChains(driver)
 
actions.move_to_element(admin).move_to_element(usrMgmt).move_to_element(users).click().perform() # Mouse Hover

driver.get("http://testautomationpractice.blogspot.com")

button = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

action = ActionChains(driver)

action.double_click(button).perform()   # Double Click

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

action = ActionChains(driver)

action.context_click(button).perform()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

sourceID = ["box1","box2","box3","box4","box5","box6","box7"]
targetID = ["box101","box102","box103","box104","box105","box106","box107"]

action = ActionChains(driver)

for i,j in zip(sourceID,targetID):
	s = driver.find_element_by_id(i)
	t = driver.find_element_by_id(j)
	time.sleep(1)
	action.drag_and_drop(s,t).perform()          # Drag & Drop    



time.sleep(5)
driver.quit()