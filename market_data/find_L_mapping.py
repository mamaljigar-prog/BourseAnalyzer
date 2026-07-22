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


for keyword in [
    "_L",
    "Instrument:",
    "MarketData:",
    "ClosingPrice:",
    "api/"
]:

    print("\n================")
    print(keyword)

    indexes = [
        m.start()
        for m in re.finditer(
            re.escape(keyword),
            text
        )
    ]

    print("COUNT:", len(indexes))


    for i in indexes[:5]:

        print("\n---")

        print(
            text[
                max(0, i-300):
                i+500
            ]
        )