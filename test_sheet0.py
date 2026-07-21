import requests
from bs4 import BeautifulSoup


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=0"


r = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    }
)


print(r.status_code)


soup = BeautifulSoup(
    r.text,
    "html.parser"
)


text = soup.get_text(
    " ",
    strip=True
)


print(
    "صورت وضعیت مالی" in text
)


print(
    "دارایی" in text
)


print(
    text[text.find("صورت وضعیت مالی"):text.find("صورت وضعیت مالی")+1000]
)