import requests
from bs4 import BeautifulSoup


url = "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=QxYX7A2pkntVRzKRJzUFvg%3d%3d&rt=0&let=58&ct=0&ft=-1"


headers = {
    "User-Agent": "Mozilla/5.0"
}


r = requests.get(
    url,
    headers=headers,
    timeout=60
)


soup = BeautifulSoup(
    r.text,
    "html.parser"
)


tables = soup.find_all("table")


print("تعداد جدول ها:", len(tables))


for i, table in enumerate(tables):

    txt = table.get_text(
        " ",
        strip=True
    )

    if "محصول" in txt or "فروش" in txt or "مقدار" in txt:

        print("====================")
        print("TABLE:", i)
        print("====================")

        print(
            txt[:3000]
        )