import requests
from bs4 import BeautifulSoup


url = "https://codal.ir/Reports/Attachment.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"


session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0"
}


r = session.get(
    url,
    headers=headers
)


soup = BeautifulSoup(
    r.text,
    "html.parser"
)


data = {}

for item in soup.find_all("input"):

    name = item.get("name")

    value = item.get("value","")

    if name:
        data[name] = value


print("FIELDS:")
for x in data.keys():
    print(x)


r2 = session.post(
    url,
    headers=headers,
    data=data
)


print("================")
print("STATUS", r2.status_code)
print("LEN", len(r2.text))


for a in BeautifulSoup(r2.text,"html.parser").find_all("a"):

    print(
        a.get_text(" ",strip=True),
        a.get("href")
    )