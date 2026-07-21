import requests

url = "https://codal.ir/Reports/Decision.aspx"

params = {
    "LetterSerial": "OOObOOOaNGDL045HqC0wNGueH5Hw==",
    "rt": "0",
    "let": "6",
    "ct": "0",
    "ft": "-1"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(
    url,
    params=params,
    headers=headers
)

print(r.status_code)
print("صورت وضعیت مالی" in r.text)

open("sheet.html","w",encoding="utf-8").write(r.text)