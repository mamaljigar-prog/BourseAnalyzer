from codal_monthly import CodalMonthly
import json


url = "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=QxYX7A2pkntVRzKRJzUFvg%3d%3d&rt=0&let=58&ct=0&ft=-1"


codal = CodalMonthly(url)


data = codal.show_monthly_sales()



with open(
    "monthly_sales.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=4
    )


print(
    "monthly_sales.json ساخته شد"
)