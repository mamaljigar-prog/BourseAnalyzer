import requests


JS_URL = "https://www.tsetmc.com/main.9d60e7997e683da143f0.js"


js = requests.get(
    JS_URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
).text


start = js.find(
    "const a="
)

print("INDEX:", start)


if start != -1:
    print(
        js[start:start+2000]
    )

else:
    print(
        "const a not found"
    )


# چند مورد اطراف module 3546
module = js.find("3546:")

print("\nMODULE AREA")

print(
    js[module:module+8000]
)