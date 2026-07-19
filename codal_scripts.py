import requests
import re


url = input("لینک اصلی کدال: ")


html = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    },
    timeout=60
).text


print("Length:", len(html))


patterns = [
    "sheet",
    "Sheet",
    "sheetId",
    "SheetId",
    "Report",
    "GetSheet",
    "ajax",
    "WebMethod"
]


for p in patterns:
    print(
        p,
        html.find(p)
    )


print("\n--- اطراف sheet ---")


for m in re.finditer(
    "sheet",
    html,
    re.I
):
    print(
        html[m.start()-100:m.start()+200]
    )
    print("----------------")