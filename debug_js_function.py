import requests
import re


base = "https://codal.ir"


for js in [
    "/js/html.script.js",
    "/js/Common.js"
]:

    print("================")
    print(js)

    url = base + js

    r = requests.get(
        url,
        headers={"User-Agent":"Mozilla/5.0"}
    )

    print("STATUS:", r.status_code)

    text = r.text

    pos = text.find("changeSheet")

    print("POSITION:", pos)

    if pos != -1:
        print(
            text[pos-300:pos+500]
        )