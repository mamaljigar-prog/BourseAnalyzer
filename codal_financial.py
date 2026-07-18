import requests
import pandas as pd
from io import BytesIO
import time


class CodalFinancialAdapter:

    def __init__(self, symbol):

        self.symbol = symbol


    def get_letters(self):

        url = (
            "https://search.codal.ir/api/search/v2/q"
        )

        params = {
            "Symbol": self.symbol,
            "PageNumber": 1,
            "Length": 50
        }


        for attempt in range(3):

            try:

                response = requests.get(
                    url,
                    params=params,
                    timeout=30,
                    headers={
                        "User-Agent":
                        "Mozilla/5.0"
                    }
                )


                if response.status_code != 200:

                    print(
                        "کدال پاسخ نامعتبر داد:",
                        response.status_code
                    )

                    time.sleep(2)
                    continue


                return response.json()


            except Exception as e:

                print(
                    f"خطا در ارتباط کدال - تلاش {attempt+1}/3"
                )

                time.sleep(3)


        return None



    def find_annual_report(self):

        data = self.get_letters()


        if not data:

            return None


        letters = data.get(
            "Letters",
            []
        )


        for item in letters:


            title = item.get(
                "Title",
                ""
            )


            if (
                "صورت‌های مالی" in title
                and
                "سالانه" in title
            ):

                return item



        return None




    def download_excel(self, report):


        excel_url = report.get(
            "ExcelUrl"
        )


        if not excel_url:

            print(
                "این گزارش فایل اکسل ندارد"
            )

            return None



        try:

            response = requests.get(
                excel_url,
                timeout=60,
                headers={
                    "User-Agent":
                    "Mozilla/5.0"
                }
            )


            if response.status_code != 200:

                print(
                    "خطا در دانلود اکسل:",
                    response.status_code
                )

                return None



            return BytesIO(
                response.content
            )


        except Exception as e:

            print(
                "خطا در دریافت فایل اکسل:",
                e
            )

            return None




    def read_excel(self):


        report = self.find_annual_report()


        if not report:

            print(
                "گزارش سالانه پیدا نشد"
            )

            return None



        print("----------------")
        print(
            "گزارش پیدا شد:"
        )

        print(
            report.get("Title")
        )

        print(
            "تاریخ انتشار:",
            report.get("PublishDateTime")
        )

        print("----------------")



        excel = self.download_excel(
            report
        )


        if not excel:

            return None



        try:

            xls = pd.ExcelFile(
                excel
            )


            print(
                "Sheet ها:"
            )


            for sheet in xls.sheet_names:

                print(
                    "-",
                    sheet
                )


            return xls.sheet_names



        except Exception as e:

            print(
                "خطا در خواندن اکسل:",
                e
            )

            return None