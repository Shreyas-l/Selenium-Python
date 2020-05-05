from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

caps = DesiredCapabilities.CHROME
caps['goog: loggingPrefs'] = {'performance': 'ALL'}
#driver = webdriver.Chrome(desired_capabilities=caps)

driver = webdriver.Chrome(executable_path="/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver",desired_capabilities=caps)

driver.get("https://fcrit.ac.in")

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/a[8]/button").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/div[3]/div/a").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[2]/form/center[1]/input[1]").send_keys("101730")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/form/center[1]/input[2]").send_keys("101730")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/form/center[2]/input").click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[4]/a").click()
time.sleep(2)

driver.get("https://sp.fcrit.ac.in/studentportal/student_attendance.php")

for request in driver.requests:
    if request.response:
        print(
        	
            request.path,
            request.response.status_code,
            request.response.headers['Content-Type']
        )

"""def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response

browser_log = driver.get_log('performance') 
events = [process_browser_log_entry(entry) for entry in browser_log]
events = [event for event in events if 'Network.response' in event['method']]"""

print(driver.current_url)
print(driver.page_source)

time.sleep(20)
driver.quit()