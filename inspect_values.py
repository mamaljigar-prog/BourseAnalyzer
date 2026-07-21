import json
import re

html = open("sheet0.html", encoding="utf-8").read()

m = re.search(
    r'var datasource = (.*?);',
    html,
    re.S
)

data = json.loads(m.group(1))

sheet = data["sheets"][0]

table = sheet["tables"][0]

for cell in table["cells"]:
    if cell["value"] not in ["", None]:
        print(
            cell["address"],
            "|",
            cell["value"]
        )