import requests
import re


JS_URL = (
    "https://www.tsetmc.com/"
    "main.9d60e7997e683da143f0.js"
)


text = requests.get(
    JS_URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
).text


target = "GetInstrumentSearch"


index = text.find(target)


print("INDEX:", index)


if index != -1:

    start = max(
        0,
        index - 500
    )

    end = index + 800


    print(
        text[start:end]
    )

else:

    print(
        "NOT FOUND"
    )