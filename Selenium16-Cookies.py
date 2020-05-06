from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver")

#driver.get("https://www.amazon.com")

driver.get("http://122.200.19.29/mrg")


cookies = driver.get_cookies()  # Capture all Cookies

print(len(cookies))
print(cookies)  # List of Dictionary Objects


driver.delete_all_cookies()


# Add New Cookie to the Browser
cookie = {'name':'MyCookie','value':'1234567'}   # Cookie Name cant contain spaces
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

time.sleep(2)

# Delete a Cookie
driver.delete_cookie('MyCookie')

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)



time.sleep(5)
driver.quit()