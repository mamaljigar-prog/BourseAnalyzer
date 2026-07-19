import requests
import pandas as pd
from io import StringIO


url = "https://excel.codal.ir/service/Excel/GetAll/OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d/0"


headers = {
    "User-Agent": "Mozilla/5.0"
}


r = requests.get(
    url,
    headers=headers,
    timeout=60
)


print("Status:", r.status_code)


html = r.text


print("Length:", len(html))


tables = pd.read_html(StringIO(html))


print("تعداد جدول‌ها:", len(tables))


for i, df in enumerate(tables):

    print("\n====================")
    print("Table:", i)

    print(df.head(10))