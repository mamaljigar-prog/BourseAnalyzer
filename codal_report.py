import requests
import re
from io import BytesIO
import pandas as pd


class CodalReport:

    def __init__(self, url):
        self.url = url


    def get_html(self):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            self.url,
            headers=headers,
            timeout=60
        )

        print("Status:", response.status_code)

        response.encoding = "utf-8"

        return response.text



    def find_excel_link(self, html):

        # پیدا کردن لینک اکسل داخل صفحه کدال

        patterns = [

            r'https?://[^"\']+\.xlsx',

            r'ExcelUrl["\']?\s*[:=]\s*["\']([^"\']+)'

        ]


        for pattern in patterns:

            match = re.search(
                pattern,
                html,
                re.I
            )

            if match:

                url = match.group(1)

                print("Excel پیدا شد")

                return url


        print("Excel پیدا نشد")

        return None



    def download_excel(self, url):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }


        response = requests.get(
            url,
            headers=headers,
            timeout=60
        )


        print(
            "Excel status:",
            response.status_code
        )


        return BytesIO(
            response.content
        )



    def read_excel(self):

        html = self.get_html()


        excel_url = self.find_excel_link(
            html
        )


        if not excel_url:

            print(
                "گزارش اکسل مستقیم پیدا نشد"
            )

            return None



        try:

            file = self.download_excel(
                excel_url
            )


            xls = pd.ExcelFile(
                file
            )


            print("================")
            print("Sheet های گزارش")
            print("================")


            for sheet in xls.sheet_names:

                print("-", sheet)


            return xls.sheet_names


        except Exception as e:

            print(
                "خطا در خواندن اکسل:",
                e
            )

            return None