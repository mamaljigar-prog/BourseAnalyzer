import requests
import pandas as pd
from io import BytesIO


class CodalFinancial:

    def __init__(self, reports):
        self.reports = reports


    def find_financial_report(self):

        for r in self.reports:

            title = r["Title"]

            if "صورت‌های مالی" in title and "سال مالی" in title:

                if r["ExcelUrl"]:
                    print("گزارش مالی پیدا شد")
                    print(title)
                    return r

        return None



    def download_excel(self, excel_url):

        print("دانلود اکسل:")
        print(excel_url)

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            excel_url,
            headers=headers,
            timeout=60
        )

        print("Status:", response.status_code)

        if response.status_code != 200:
            return None


        return BytesIO(response.content)



    def parse_income_statement(self, excel):

        try:

            sheets = pd.ExcelFile(excel)

            print("Sheet ها:")
            print(sheets.sheet_names)


            for sheet in sheets.sheet_names:

                if "سود" in sheet or "زیان" in sheet:

                    print("Sheet انتخاب شد:",sheet)

                    df = pd.read_excel(
                        excel,
                        sheet_name=sheet,
                        header=None
                    )


                    print(df.head(20))


                    return df


        except Exception as e:

            print(e)


        return None