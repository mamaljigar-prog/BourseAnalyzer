import requests
import pandas as pd
from io import BytesIO


excel_url = "https://excel.codal.ir/service/Excel/GetAll/OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d/0"


headers = {
    "User-Agent": "Mozilla/5.0"
}


r = requests.get(
    excel_url,
    headers=headers,
    timeout=60
)


print("Status:", r.status_code)
print("Size:", len(r.content))


file = BytesIO(r.content)


xls = pd.ExcelFile(file)


print("\nSheet ها:")
for s in xls.sheet_names:
    print(s)


for s in xls.sheet_names:

    print("\n===================")
    print("Sheet:", s)

    df = pd.read_excel(
        file,
        sheet_name=s,
        header=None
    )

    print(df.head(10))