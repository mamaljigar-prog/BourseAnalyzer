import requests
import re


url = (
    "https://www.tsetmc.com/"
    "main.9d60e7997e683da143f0.js"
)


text = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
).text


patterns = [
    r'function _L\([^)]*\)',
    r'_L=\([^)]*\)=>',
    r'Instrument.{0,200}'
]


for p in patterns:

    print("\nPATTERN:", p)

    result = re.findall(
        p,
        text
    )

    for item in result[:5]:
        print(item)