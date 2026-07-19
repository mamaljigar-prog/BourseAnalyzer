import requests
import re


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=1"


r = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    },
    timeout=30
)


text = r.text


keywords = [
    "sheet",
    "Sheet",
    "getSheet",
    "Report",
    "Excel",
    "table",
    "Table",
    "Data"
]


for k in keywords:

    print("\n==========", k, "==========")


    result = re.findall(
        r".{0,100}" + k + r".{0,150}",
        text
    )


    for item in result[:10]:

        print(item)