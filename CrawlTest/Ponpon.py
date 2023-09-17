#取得資料
import urllib.request as req
url="https://www.wantgoo.com/my/stocklist"

request = req.Request(url, headers={
    "user_name":"ttoommy0713@gmail.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)
#分析資料
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
print(root.title.string)