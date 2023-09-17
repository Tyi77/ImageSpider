from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import concurrent.futures
import time

# 獲取一個圖片
def getImage(url, index, keyword, driver):
    driver.get(url)

    with open(f'./images/{keyword}/{keyword}{str(index+1)}.jpg', 'wb') as file:
        file.write(driver.find_element(By.TAG_NAME, 'img').screenshot_as_png)


# 透過輸入的item，爬特定的keyword資料
def spider(item):  # item : 元素為[str key, int count]的雙重陣列
    keyword = item[0]
    count = item[1]

    # 看images資料夾中是否有相對應的資料夾
    if not os.path.exists(f'./images/{keyword}'):
        os.mkdir(f'./images/{keyword}')

    driver = webdriver.Chrome()  # 開一個webdriver instance

    # 取得網頁頁面
    driver.get(f'https://unsplash.com/s/photos/{keyword}')

    # 點擊button : Load more photos
    driver.find_element(By.CSS_SELECTOR, '.CwMIr.DQBsa.p1cWU.jpBZ0.AYOsT.Olora.I0aPD.dEcXu').click()
    time.sleep(1)  # 要等瀏覽器處理button點擊

    # Scroll the page
    times = ((count - 40) // 20) + 1
    for _ in range(times):
        driver.execute_script('window.scrollBy(0, 2400);')
        time.sleep(0.3)

    # 正式開始找取資料
    results = driver.find_elements(By.CSS_SELECTOR, 'a.rEAWd .MorZF img.YVj9w')

    # 將指定數量的url從results list放到imageLinks中
    imageLinks=[]
    for id in range(count):
        imageLinks.append(results[id].get_attribute('src'))

    # 針對每一個item爬圖片下來 : 運用for迴圈的方式爬
    for index, link in enumerate(imageLinks):
        getImage(link, index, keyword, driver)

    driver.close()



# 輸入資料
inputItems = input("Please enter the keyword and the number of the photos (e.g. apple: 2, car sign: 12, banana: 7): ")

# 資料前處理
inputItems = [item.strip() for item in inputItems.split(',')]
inputItems = [item.split(':') for item in inputItems]
inputItems = [[item[0], int(item[1])] for item in inputItems]

# 確認是否有總資料夾
if not os.path.exists('./images'):
    os.mkdir('./images')

# 開始爬蟲
startTime = time.time()  # 開始計時
# 用 multiThreading爬每一個item
with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
    executor.map(spider, inputItems)
endTime = time.time()  # 結束計時

# 印出執行時間
print(f'執行時間{endTime - startTime}秒')