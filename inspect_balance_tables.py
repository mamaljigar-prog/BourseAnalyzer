import requests
from bs4 import BeautifulSoup


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"


html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text


soup = BeautifulSoup(
    html,
    "html.parser"
)


tables = soup.find_all("table")


for i, table in enumerate(tables):

    text = table.get_text(
        " ",
        strip=True
    )

    if (
        "دارایی" in text
        or
        "حقوق مالکانه" in text
        or
        "بدهی" in text
    ):

        print("================")
        print("TABLE", i)
        print(text[:1000])