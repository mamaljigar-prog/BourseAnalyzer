import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from codal_table import CodalTableParser


url = input("لینک کدال: ")


parser = CodalTableParser(url)


tables = parser.extract_tables()


table4 = tables[4]


print("================")
print("TABLE 4 ROWS")
print("================")


for i,row in enumerate(table4["rows"]):

    text = " | ".join(row)

    if len(text) > 0:

        print(
            i,
            text[:300]
        )