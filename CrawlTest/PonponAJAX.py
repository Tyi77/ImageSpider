#取得資料
import urllib.request as req
url="https://medium.com/_/graphql"

request = req.Request(url, headers={
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
    "Apollographql-Client-Name":"lite",
    "Apollographql-Client-Version":"main-20220421-171442-915c421cc8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)
#分析資料
import json
data = json.loads(data)
print(data)