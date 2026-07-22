import requests
import re


JS_URL = "https://www.tsetmc.com/main.9d60e7997e683da143f0.js"


def main():

    r = requests.get(
        JS_URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    print("STATUS:", r.status_code)

    js = r.text

    index = js.find("_L:")

    print("INDEX:", index)

    if index == -1:
        print("NOT FOUND")
        return


    start = max(0, index - 1000)
    end = index + 3000

    print(
        js[start:end]
    )


if __name__ == "__main__":
    main()