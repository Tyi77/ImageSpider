from pprint import pprint
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driverpath = 'C:\E\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driverpath)

driver.get("https://www.google.com")

pprint(driver.page_source)

# element = driver.find_element_by_class_name("gLFyf.gsfi")
# element.send_keys("Selenium Python")

# time.sleep(5)
# element.clear()

# button = driver.find_element_by_class_name("gNO89b")
# button.click()

# element = driver.find_element(By.NAME, "btnI")
# print(element.get_attribute('value'))

driver.close()