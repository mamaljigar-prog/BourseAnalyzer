import requests
from bs4 import BeautifulSoup


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"


r = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    },
    timeout=60
)


soup = BeautifulSoup(
    r.text,
    "html.parser"
)


for a in soup.find_all("a"):

    text = a.get_text(
        strip=True
    )

    href = a.get(
        "href"
    )

    if text:

        print(
            text,
            " --> ",
            href
        )