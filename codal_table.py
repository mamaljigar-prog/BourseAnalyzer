import requests
from bs4 import BeautifulSoup


class CodalTableParser:

    def __init__(self, url):
        self.url = url


    def get_html(self):

        response = requests.get(
            self.url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=60
        )

        print("Status:", response.status_code)

        response.encoding = "utf-8"

        return response.text



    def extract_tables(self):

        html = self.get_html()

        soup = BeautifulSoup(
            html,
            "html.parser"
        )


        tables = soup.find_all(
            "table"
        )


        print(
            "تعداد جدول:",
            len(tables)
        )


        results = []


        for index, table in enumerate(tables):

            text = table.get_text(
                " ",
                strip=True
            )


            if not text:
                continue


            print("----------------")
            print(
                "TABLE",
                index
            )

            print(
                text[:200]
            )


            rows = []


            for tr in table.find_all("tr"):

                cells = []

                for cell in tr.find_all(
                    ["td", "th"]
                ):

                    value = cell.get_text(
                        " ",
                        strip=True
                    )

                    if value:
                        cells.append(value)


                if cells:
                    rows.append(cells)


            results.append(
                {
                    "index": index,
                    "text": text,
                    "rows": rows
                }
            )


        return results



    def find_financial_tables(self):

        tables = self.extract_tables()


        financial = {
            "income_statement": None,
            "balance_sheet": None,
            "cash_flow": None,
            "sales": None
        }


        for table in tables:

            text = table["text"]


            # سود و زیان

            if (
                "سود خالص" in text
                or
                "سود (زیان)" in text
                or
                "درآمدهای عملیاتی" in text
            ):

                financial["income_statement"] = table



            # ترازنامه

            if (
                "جمع دارایی‌ها" in text
                or
                "جمع دارايي" in text
                or
                "حقوق مالکانه" in text
            ):

                financial["balance_sheet"] = table



            # جریان وجوه نقد

            if (
                "جریان وجوه نقد" in text
                or
                "فعالیت‌های عملیاتی" in text
            ):

                financial["cash_flow"] = table



            # فروش

            if (
                "فروش" in text
                or
                "مقدار فروش" in text
                or
                "مبلغ فروش" in text
            ):

                financial["sales"] = table



        return financial