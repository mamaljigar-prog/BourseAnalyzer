import json
import requests


class BalanceSheetParser:


    def __init__(self, url):

        self.url = url

        self.headers = {

            "User-Agent":
            "Mozilla/5.0",

            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",

            "Accept-Language":
            "fa-IR,fa;q=0.9,en;q=0.8",

        }



    def extract_datasource(self):

        response = requests.get(

            self.url,

            headers=self.headers,

            timeout=30

        )


        response.raise_for_status()


        html = response.text


        markers = [

            "var datasource =",

            "var datasource="

        ]


        start = -1


        for marker in markers:

            start = html.find(marker)

            if start != -1:

                break



        if start == -1:

            raise ValueError(
                "Datasource not found"
            )



        json_start = html.find(

            "{",

            start

        )


        if json_start == -1:

            raise ValueError(
                "Datasource JSON not found"
            )



        decoder = json.JSONDecoder()


        datasource, _ = decoder.raw_decode(

            html[json_start:]

        )


        return datasource



    def extract_sheets(self):


        datasource = self.extract_datasource()


        return datasource.get(

            "sheets",

            []

        )



    def normalize(self, value):


        if value is None:

            return ""


        text = str(value)



        chars = [

            "\u200b",

            "\u200c",

            "\u200d",

            "\u200e",

            "\u200f",

            "\ufeff",

        ]


        for char in chars:

            text = text.replace(

                char,

                ""

            )



        text = text.replace(

            "ي",

            "ی"

        )


        text = text.replace(

            "ى",

            "ی"

        )


        text = text.replace(

            "ك",

            "ک"

        )


        text = text.replace(

            "ـ",

            ""

        )


        return "".join(

            text.split()

        ).strip()



    def parse_number(self, value):


        if value is None:

            return 0


        text = str(value).strip()


        if not text:

            return 0



        translation = str.maketrans(

            "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩",

            "01234567890123456789"

        )


        text = text.translate(

            translation

        )


        text = (

            text

            .replace(",", "")

            .replace("٬", "")

            .replace(" ", "")

        )



        try:

            return int(float(text))


        except:

            return 0



    def find_balance_sheet(self, sheets):


        print()

        print(
            "AVAILABLE SHEETS:"
        )


        for sheet in sheets:


            title = sheet.get(

                "title_Fa",

                ""

            )


            print(

                title

            )



        print()



        keywords = [

            "صورتوضعیتمالی",

            "ترازنامه",

            "وضعیتمالی",

            "balancesheet"

        ]



        for sheet in sheets:


            title_fa = self.normalize(

                sheet.get(

                    "title_Fa",

                    ""

                )

            )



            title_en = self.normalize(

                sheet.get(

                    "title_En",

                    ""

                )

            ).lower()



            for key in keywords:


                if key in title_fa:

                    return sheet



                if key in title_en:

                    return sheet



        return None



    def get_balance_table(self, balance_sheet):


        tables = balance_sheet.get(

            "tables",

            []

        )


        if not tables:

            return None


        return tables[0]



    def get_cell_value(self, cells, address):


        for cell in cells:


            if cell.get(

                "address"

            ) == address:


                return self.parse_number(

                    cell.get(

                        "value"

                    )

                )



        return 0



    def get_cell_text(self, cells, address):


        for cell in cells:


            if cell.get(

                "address"

            ) == address:


                return self.normalize(

                    cell.get(

                        "value",

                        ""

                    )

                )


        return ""



    def get_balance_data(self):


        sheets = self.extract_sheets()



        balance_sheet = self.find_balance_sheet(

            sheets

        )



        if balance_sheet is None:


            print(

                "Balance sheet not found"

            )


            return {

                "assets": 0,

                "equity": 0,

                "liabilities": 0,

                "total": 0,

                "balanced": False

            }



        table = self.get_balance_table(

            balance_sheet

        )



        if table is None:


            return {

                "assets": 0,

                "equity": 0,

                "liabilities": 0,

                "total": 0,

                "balanced": False

            }



        cells = table.get(

            "cells",

            []

        )



        assets = self.get_cell_value(

            cells,

            "B22"

        )


        equity = self.get_cell_value(

            cells,

            "B35"

        )


        liabilities = self.get_cell_value(

            cells,

            "B53"

        )


        total = self.get_cell_value(

            cells,

            "B54"

        )



        balanced = (

            assets != 0

            and

            equity + liabilities == total

            and

            assets == total

        )



        print()

        print(
            "Balance Sheet Data:"
        )


        print(
            "Assets:",
            assets
        )


        print(
            "Equity:",
            equity
        )


        print(
            "Liabilities:",
            liabilities
        )


        print(
            "Total:",
            total
        )


        print(
            "Balanced:",
            balanced
        )



        return {

            "assets": assets,

            "equity": equity,

            "liabilities": liabilities,

            "total": total,

            "balanced": balanced

        }



if __name__ == "__main__":


    pass