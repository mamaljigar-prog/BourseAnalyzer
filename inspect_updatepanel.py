import requests
from bs4 import BeautifulSoup


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=0"


html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text


start = html.find('id="ctl00_cphBody_UpdatePanel1"')

part = html[start:start+50000]


soup = BeautifulSoup(part, "html.parser")

tables = soup.find_all("table")

print("TABLES:", len(tables))


for i,t in enumerate(tables):
    txt=t.get_text(" ",strip=True)
    print("================")
    print(i, txt[:300])