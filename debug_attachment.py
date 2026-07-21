import requests
from bs4 import BeautifulSoup


url = "https://codal.ir/Reports/Attachment.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw=="


r = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
)


print("STATUS:", r.status_code)
print("LENGTH:", len(r.text))


soup = BeautifulSoup(
    r.text,
    "html.parser"
)


for a in soup.find_all("a"):

    href = a.get("href")

    text = a.get_text(
        " ",
        strip=True
    )

    if href:

        print(
            text,
            "---->",
            href
        )