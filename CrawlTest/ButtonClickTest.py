from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get(f'https://unsplash.com/s/photos/apple')

# loadMore = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/div[3]/div[1]/button')
# if loadMore:
#     loadMore.click()

driver.find_element(By.CSS_SELECTOR, '.CwMIr.DQBsa.p1cWU.jpBZ0.AYOsT.Olora.I0aPD.dEcXu').click()

time.sleep(0.5)

for _ in range(4):
    driver.execute_script('window.scrollBy(0, 2500);')
    time.sleep(0.3)

results = driver.find_elements(By.CSS_SELECTOR, 'a.rEAWd .MorZF img.YVj9w')

print(len(results))

driver.close()

# url = results[].get_attribute('src')

# print(url)

# driver.get(url)

# image = driver.find_element(By.TAG_NAME, 'img')

# with open('./imageTest.jpg', 'wb') as file:
#     file.write(image.screenshot_as_png)