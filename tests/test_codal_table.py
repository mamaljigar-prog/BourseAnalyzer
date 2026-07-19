import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from codal_table import CodalTableParser



url = input(
    "لینک کدال: "
)


parser = CodalTableParser(
    url
)


data = parser.find_financial_tables()


print("\n================")
print("نتیجه تشخیص جدول‌ها")
print("================")


for key,value in data.items():

    if value:

        print(
            key,
            "=> TABLE",
            value["index"]
        )

    else:

        print(
            key,
            "=> پیدا نشد"
        )