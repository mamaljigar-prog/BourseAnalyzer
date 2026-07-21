import re
import json


html = open("sheet0.html", encoding="utf-8").read()


match = re.search(
    r'var datasource = (\{.*?\});',
    html,
    re.DOTALL
)

data = json.loads(match.group(1))


cells = data["sheets"][0]["tables"][0]["cells"]


print("CELL COUNT:", len(cells))


for i, cell in enumerate(cells[:30]):
    print("================")
    print("CELL", i)
    print(cell)