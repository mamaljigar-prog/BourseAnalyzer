import re
import json


html = open("sheet0.html", encoding="utf-8").read()


match = re.search(
    r'var datasource = (\{.*?\});',
    html,
    re.DOTALL
)

data = json.loads(match.group(1))


sheet = data["sheets"][0]

print(sheet.keys())

print("================")

for key, value in sheet.items():
    print("KEY:", key, "TYPE:", type(value))
