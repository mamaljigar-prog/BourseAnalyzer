import requests


url = "https://excel.codal.ir/service/excel/?letterSerial=%2BaNGDL045HqC0wNGueH5Hw%3D%3D&sheetId=0&languageId=0"


r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)


print("STATUS:", r.status_code)
print("TYPE:", r.headers.get("Content-Type"))
print("SIZE:", len(r.content))


open("balance.xlsx", "wb").write(r.content)