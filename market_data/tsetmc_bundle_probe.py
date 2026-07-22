import requests
import re


JS_URL = "https://www.tsetmc.com/main.9d60e7997e683da143f0.js"


r = requests.get(
    JS_URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
)


print("STATUS:", r.status_code)

print("LENGTH:", len(r.text))


patterns = [

    r'\/api\/[^"\']+',
    r'https?://[^"\']+',
    r'[^"\']*Market[^"\']*',
    r'[^"\']*Instrument[^"\']*',
    r'[^"\']*Symbol[^"\']*'

]


for pattern in patterns:

    print("\nPATTERN:", pattern)

    matches = re.findall(
        pattern,
        r.text
    )

    for item in matches[:30]:

        print(item)