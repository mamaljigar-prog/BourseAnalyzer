import requests
from bs4 import BeautifulSoup


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=0"


r = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
)


soup = BeautifulSoup(
    r.text,
    "html.parser"
)


tables = soup.find_all("table")


print("TABLE COUNT:", len(tables))


for i, table in enumerate(tables):

    txt = table.get_text(
        " ",
        strip=True
    )

    print("================")
    print("TABLE", i)
    print(txt[:500])