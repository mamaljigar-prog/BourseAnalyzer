import requests


session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://codal.ir/"
}


page_url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=%2baNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=0"


r1 = session.get(
    page_url,
    headers=headers
)

print("PAGE:", r1.status_code)
print("COOKIES:", session.cookies)


excel_url = "http://excel.codal.ir//service/excel/?letterSerial=%2baNGDL045HqC0wNGueH5Hw%3d%3d&sheetId=0&languageId=0"


r2 = session.get(
    excel_url,
    headers=headers
)


print("EXCEL:", r2.status_code)
print("TYPE:", r2.headers.get("Content-Type"))
print("SIZE:", len(r2.content))


open("balance.xlsx","wb").write(r2.content)