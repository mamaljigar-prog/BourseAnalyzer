import re
import json


html = open("sheet0.html", encoding="utf-8").read()


match = re.search(
    r'var datasource = (\{.*?\});',
    html,
    re.DOTALL
)


print("FOUND:", bool(match))


data = json.loads(match.group(1))


print(data.keys())


print("SHEETS:")
for s in data["sheets"]:
    print(
        s.get("code"),
        s.get("title_Fa")
    )