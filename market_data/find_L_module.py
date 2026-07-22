import requests


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


target = "3546:"

index = text.find(target)


print("INDEX:", index)


if index != -1:

    print(
        text[
            index:index+3000
        ]
    )

else:

    print("MODULE NOT FOUND")