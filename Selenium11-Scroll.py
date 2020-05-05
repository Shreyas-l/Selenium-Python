from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")


driver.execute_script("window.scrollBy(0,1000)","") # Aproach 1

i=0													# Aproach 2		
j=1
while j!=1000:
	driver.execute_script("window.scrollBy(" + str(i) + "," + str(j) + ")","")
	i=j
	j+=1
	time.sleep(0.2)


flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")  # Approach 3

driver.execute_script("arguments[0].scrollIntoView();",flag)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") # Approachm 4

time.sleep(10)
driver.quit()