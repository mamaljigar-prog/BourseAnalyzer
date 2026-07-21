import re


html = open("sheet0.html", encoding="utf-8").read()


matches = re.findall(
    r'https?://excel\.codal\.ir[^"\']+',
    html
)


print("COUNT:", len(matches))

for m in matches:
    print("----------")
    print(m)