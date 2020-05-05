from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory" : "/Users/shreyas_rl/Desktop/git/Selenium-Python"})

driver = webdriver.Chrome("/Users/shreyas_rl/Desktop/git/Selenium-Python/chromedriver",chrome_options=chromeOptions)

driver.get("http://testautomationpractice.blogspot.com")
time.sleep(5)

driver.switch_to_frame(0)

file = driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("/Users/shreyas_rl/Desktop/git/Selenium-Python/TestSEPrac9.pdf")

time.sleep(5)

driver.get("http://demo.automationtesting.in/FileDownload.html")
time.sleep(2)

driver.find_element_by_id("textbox").send_keys("Hello I'm Shreyas")

driver.find_element_by_id("createTxt").click()
time.sleep(1)

driver.find_element_by_id("link-to-download").click()

driver.find_element_by_id("pdfbox").send_keys("Hello I'm Shreyas")

driver.find_element_by_id("createPdf").click()
time.sleep(1)

driver.find_element_by_id("pdf-link-to-download").click()


time.sleep(5)
driver.quit()