import requests


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=0"


html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text


print("LEN:", len(html))


for word in [
    "tbl",
    "Grid",
    "Data",
    "sheetId",
    "0",
    "ReportViewer",
    "asmx",
    "ashx"
]:

    print(
        word,
        html.find(word)
    )


open(
    "sheet0.html",
    "w",
    encoding="utf-8"
).write(html)