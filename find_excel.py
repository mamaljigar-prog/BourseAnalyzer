import requests
import re


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"


r = requests.get(
    url,
    headers={
        "User-Agent":"Mozilla/5.0"
    },
    timeout=60
)


html = r.text


# پیدا کردن لینک های اکسل

patterns = [
    r'href="([^"]*xls[^"]*)"',
    r'src="([^"]*xls[^"]*)"',
    r'([^"\']+\.xlsx)',
    r'([^"\']+\.xls)'
]


for p in patterns:

    result = re.findall(
        p,
        html,
        re.I
    )

    if result:

        print("FOUND:")
        for x in result:
            print(x)