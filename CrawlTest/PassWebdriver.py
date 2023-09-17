from selenium import webdriver

def func1():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    return driver

def func2(driver):
    driver.get('https://netspeak.org/')
    return driver.title

if __name__ == '__main__':
    driver = func1()
    title = func2(driver)
    print(title)
    driver.quit()