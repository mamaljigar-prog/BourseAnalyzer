import requests
import re
import json


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


# پیدا کردن بخش cells

start = html.find('"cells":')


print("cells position:", start)


if start == -1:
    print("cells پیدا نشد")
    exit()


part = html[start:start+5000]


print(part)