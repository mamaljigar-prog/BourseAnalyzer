import requests
import re
import json
from io import BytesIO
import pandas as pd


class CodalReport:

    def __init__(self, url):
        self.url = url

    def get_html(self):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(
            self.url,
            headers=headers,
            timeout=60
        )

        print("Status:", r.status_code)

        r.encoding = "utf-8"

        return r.text


    def find_excel_link(self, html):

        patterns = [
            r'https?://[^"\']+\.xlsx',
            r'ExcelUrl.{0,200}?["\'](.*?)["\']'
        ]

        for p in patterns:

            result = re.search(
                p,
                html,
                re.I
            )

            if result:

                print("Excel پیدا شد")

                return result.group(1)


        print("Excel پیدا نشد")

        return None



    def download_excel(self, excel_url):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(
            excel_url,
            headers=headers,
            timeout=60
        )

        print(
            "Excel status:",
            r.status_code
        )


        return BytesIO(
            r.content
        )



    def read_excel(self):

        html = self.get_html()

        excel_url = self.find_excel_link(
            html
        )


        if not excel_url:

            print(
                "گزارش Excel ندارد"
            )

            return None


        excel = self.download_excel(
            excel_url
        )


        try:

            xls = pd.ExcelFile(
                excel
            )


            print("================")
            print("Sheet های گزارش")
            print("================")


            for s in xls.sheet_names:

                print("-", s)


            return xls.sheet_names


        except Exception as e:

            print(
                "خطا در خواندن Excel:",
                e
            )

            return None