import requests
from bs4 import BeautifulSoup
import os
import concurrent.futures
import functools
import time

# 獲取一個圖片
def getImage(url, index, keyword):
    img = requests.get(url)

    with open(f'./images/{keyword}/{keyword}{str(index+1)}.jpg', 'wb') as file:
        file.write(img.content)

# 透過輸入的item，爬特定的keyword資料
def spider(item):  # item : 元素為[str key, int count]的雙重陣列
    keyword = item[0]
    count = item[1]

    # 看images資料夾中是否有相對應的資料夾
    if not os.path.exists(f'./images/{keyword}'):
        os.mkdir(f'./images/{keyword}')

    # 取得網頁的資料
    response = requests.get(f'https://unsplash.com/s/photos/{keyword}')

    # 用BeautifulSoup去解析HTML檔
    soup = BeautifulSoup(response.text, 'lxml')

    # 用select去找到所要的圖片集合
    results = soup.select('a.rEAWd .MorZF img.YVj9w', limit=count)

    # 預備每一個圖片的url以便之後的下載
    imageLinks = [result.get('src') for result in results]

    # 針對每一個item爬圖片下來：運用multiThreading的方式爬
    with concurrent.futures.ThreadPoolExecutor(max_workers=60) as executor:
        executor.map(functools.partial(getImage, keyword = keyword), imageLinks, range(count))

    time.sleep(2)



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