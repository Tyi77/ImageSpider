# 3.取得個別外資、投信、自營的資料
# 取得網頁response
# import requests
# import cfscrape
# import cloudscraper
# from bs4 import BeautifulSoup
# from requests.structures import CaseInsensitiveDict

# url = "https://www.wantgoo.com/stock/1342"
# token = cfscrape.get_tokens(url)

# url = "https://www.wantgoo.com/stock/1342/three-trend-for-30days"
# scraper = cfscrape.create_scraper()
# resp = scraper.get(url)

# resp = requests.get(url)  # 用get獲取response資料

# scraper = cloudscraper.create_scraper(interpreter='nodejs')
# resp = scraper.get(url)

# print(resp.status_code)

# root = BeautifulSoup(resp.text, "html.parser")
# print(root)  # qq被cloudflare擋下來了
# 分析response資料




# driverpath = 'C:\E\chromedriver_win32\chromedriver.exe'
# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import unittest, time, re

# class UntitledTestCase(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path=driverpath)
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://www.google.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
    
#     def test_untitled_test_case(self):
#         driver = self.driver
#         # driver.get("https://www.wantgoo.com/stock/1342")
#         driver.get("https://www.wantgoo.com/stock/1342/three-trend-for-30days")
    
#     def is_element_present(self, how, what):
#         try: self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e: return False
#         return True
    
#     def is_alert_present(self):
#         try: self.driver.switch_to_alert()
#         except NoAlertPresentException as e: return False
#         return True
    
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally: self.accept_next_alert = True
    
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)

# if __name__ == "__main__":
#     # unittest.main()
#     unittest.main()





# from selenium import webdriver
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")

# driverpath = 'C:\E\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(driverpath)

# driver.get('https://www.wantgoo.com/stock/1342/three-trend-for-30days/')

# print(driver.page_source)

# driver.quit()



import requests
import json

#用session記錄此次使用的cookie
rs = requests.session()
#post傳資料
response = rs.get("https://www.wantgoo.com", headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
})
print(response.status_code)
#再get一次PTT八卦版首頁
response = rs.get("https://www.wantgoo.com/stock/1342/three-trend-for-30days")
print(response.status_code)

# links = root.find_all("div", class_="title") # 文章標題
# for link in links:
#     print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白