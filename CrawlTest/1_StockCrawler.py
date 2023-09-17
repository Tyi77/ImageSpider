# 1. 從主要網頁獲取資料
# 取得網頁response
import requests
from requests.structures import CaseInsensitiveDict

url = "https://www.wantgoo.com/my/stocklist/instantquotation"

headers = CaseInsensitiveDict()
headers["authority"] = "www.wantgoo.com"
headers["accept"] = "application/json, text/plain, */*"
headers["accept-language"] = "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7"
headers["content-type"] = "application/json;charset=UTF-8"
headers["cookie"] = "BID=B8AF4072-5496-4E2E-9DD1-AC99BE51F4B2; client_fingerprint=0f2a7d2d5caee87ea92dfadcc4866256b5c4e28e7f18629ba21714da5ee7219b; _gid=GA1.2.601728353.1650454791; _gcl_au=1.1.915998842.1650454791; hblid=CswkRelaQ0ezXOW73h7B70H06ArbQaj6; _okdetect=%7B%22token%22%3A%2216504547926300%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D; olfsk=olfsk11049540666441904; _ok=8391-691-10-7433; popup=showed; _hjSessionUser_827061=eyJpZCI6IjI2ZmM5YzQ0LWVlNzYtNWEyMi1iNjA4LWM4MDAyNWI5NTUxNiIsImNyZWF0ZWQiOjE2NTA0NTQ3OTM0MzAsImV4aXN0aW5nIjp0cnVlfQ==; BrowserMode=Web; 1; _smt_uid=626109ea.1b94b120; wcsid=KujTUHxymC3RUN153h7B70HCaDb06mAA; _okbk=cd4%3Dtrue%2Ccd5%3Daway%2Cvi5%3D0%2Cvi4%3D1650604087128%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _hjSession_827061=eyJpZCI6IjRhZGZjMmY5LTQ3NjItNDYyNS1iOTM1LTM5YjYxZjlmNzY0ZiIsImNyZWF0ZWQiOjE2NTA2Mzg2ODYyMDgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=0; member_id=357759; user_name=z07135414@gmail.com; _gat_UA-6993262-2=1; _gat_gtag_UA_6993262_2=1; authorizedKey=w%2b0XOB%2fkEVJJdCrGkemg1XOkjCjGstZu; UserName=w%2b0XOB%2fkEVJJdCrGkemg1XOkjCjGstZu; NickName=asdfasdf; UserAccount=z07135414%40gmail.com; UnReadMailCount=1; Member_No=357759; IsLogin=True; urls=m.wantgoo.com; img=https%3a%2f%2fwww.wantgoo.com%2fimage%2fdisplaydefault1.png; Email=z07135414%40gmail.com; AdState=Show; MemberLevel=Normal; idUserName=z07135414%40gmail.com; __cf_bm=BE76EfhEYxfGVMF3MffTOw.bzV4OtKO79hSiQNMEGAA-1650649168-0-AR/a85q+lZG21TxodrDyExE/3/USXvWAUjcXoSr4GHwDrsEVA9ErfrEoUJIY/jggjviiKBuQOJTseVSLgsVxqfm4XWkbD6JQuKR57tIjeKQpzNnxIX6CGclP+oiyKpOtZA==; _ga=GA1.2.845747024.1650454791; _oklv=1650649176296%2CKujTUHxymC3RUN153h7B70HCaDb06mAA; _ga_FCVGHSWXEQ=GS1.1.1650646779.12.1.1650649176.0"
headers["origin"] = "https://www.wantgoo.com"
headers["referer"] = "https://www.wantgoo.com/my/stocklist"
headers["sec-ch-ua"] = '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = '"Windows"'
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "same-origin"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"

data = '{"stockNos":"1342|6443|4904|0000"}'

resp = requests.post(url, headers=headers, data=data)  # 用post獲取response資料

# 分析response資料
import json
from pprint import pprint
data = json.loads(resp.text)
pprint(data[0])