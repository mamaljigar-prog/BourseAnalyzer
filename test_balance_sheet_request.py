import requests


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"


data = {
    "ctl00$ddlTable": "0"
}


r = requests.post(
    url,
    data=data,
    headers={
        "User-Agent":"Mozilla/5.0"
    }
)


print(r.status_code)

print(
    "دارایی" in r.text
)

print(
    "صورت وضعیت مالی" in r.text
)


open(
    "balance_result.html",
    "w",
    encoding="utf-8"
).write(r.text)