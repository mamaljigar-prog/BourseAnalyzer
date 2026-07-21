import requests
from bs4 import BeautifulSoup


url = "https://codal.ir/Reports/Attachment.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"


html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text


soup = BeautifulSoup(
    html,
    "html.parser"
)


for tag in soup.find_all(["input","a","button"]):

    print(
        tag.name,
        "name=", tag.get("name"),
        "id=", tag.get("id"),
        "value=", tag.get("value"),
        "href=", tag.get("href"),
        "text=", tag.get_text(" ",strip=True)
    )