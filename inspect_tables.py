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


print("TABLE COUNT:", len(sheet["tables"]))


for i, table in enumerate(sheet["tables"]):

    print("================")
    print("TABLE:", i)
    print(table.keys())

    for k,v in table.items():
        print(
            "   ",
            k,
            type(v)
        )