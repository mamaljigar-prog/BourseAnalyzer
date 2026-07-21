import requests


url = "https://codal.ir/js/html.script.js"


text = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text


print(text[:2000])