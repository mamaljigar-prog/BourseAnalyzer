import requests
import re


url = "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=QxYX7A2pkntVRzKRJzUFvg%3d%3d&rt=0&let=58&ct=0&ft=-1"


headers = {
    "User-Agent": "Mozilla/5.0"
}


r = requests.get(
    url,
    headers=headers,
    timeout=60
)


html = r.text


print("Status:", r.status_code)


patterns = [
    "محصول",
    "فروش",
    "مقدار",
    "Production",
    "Sales",
    "Report",
    "table",
    "cells"
]


for p in patterns:

    print(
        p,
        ":",
        html.find(p)
    )


print("----------------")


# اطراف کلمه محصول را نشان بده

pos = html.find("محصول")


if pos != -1:

    print(
        html[pos-500:pos+1000]
    )

else:

    print("محصول پیدا نشد")