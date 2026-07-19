import requests
from bs4 import BeautifulSoup
import re


url = input("لینک کدال: ")


r = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    },
    timeout=60
)


html = r.text


print("طول HTML:", len(html))


ids = re.findall(
    r"sheetId[=|']+(\d+)",
    html
)


print("Sheet ID ها:")
print(
    set(ids)
)


# پیدا کردن متن اطراف sheetId

for match in re.finditer(
    "sheetId",
    html
):

    start = max(
        0,
        match.start()-100
    )

    end = match.start()+150

    print(
        html[start:end]
    )
