import pandas as pd
import requests
import json
from io import StringIO


# آدرس گزارش ماهانه کدال
# فعلاً همان لینک گزارش را اینجا قرار می‌دهیم

url = "LINK_MONTHLY_CODAL"


print("دریافت گزارش ماهانه...")


response = requests.get(url)

print("Status:", response.status_code)


html = response.text


tables = pd.read_html(StringIO(html))


print("تعداد جدول‌ها:", len(tables))


sales_data = []


for i, df in enumerate(tables):

    text = df.to_string()


    # پیدا کردن جدول‌هایی که فروش دارند
    if "مبلغ فروش" in text or "فروش" in text:

        print()
        print("===================")
        print("جدول فروش پیدا شد:", i)
        print("===================")

        print(df.head())


        sales_data.append(
            df.to_dict()
        )



result = {

    "tables_found": len(sales_data),

    "sales_tables": sales_data

}



with open(
    "monthly_data.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=4
    )


print()
print("MONTHLY DATA SAVED")