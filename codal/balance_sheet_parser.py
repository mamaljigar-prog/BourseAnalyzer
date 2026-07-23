import json
import requests

from financial.balance_sheet_mapper import BalanceSheetMapper


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
            "ÙŠ",
            "ÛŒ"
        )

        text = text.replace(
            "Ùƒ",
            "Ú©"
        )


        return "".join(
            text.split()
        ).strip()




    def find_balance_sheet(self, sheets):


        print()
        print(
            "AVAILABLE SHEETS:"
        )


        for sheet in sheets:

            print(
                sheet.get(
                    "title_Fa",
                    ""
                )
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




    def get_balance_data(self):


        sheets = self.extract_sheets()


        balance_sheet = self.find_balance_sheet(
            sheets
        )



        if balance_sheet is None:

            return {

                "assets": 0,
                "equity": 0,
                "liabilities": 0,
                "non_controlling_interest": 0,
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
                "non_controlling_interest": 0,
                "total": 0,
                "balanced": False

            }




        cells = table.get(
            "cells",
            []
        )



        result = BalanceSheetMapper(
            cells
        ).map()



        balanced = (

            result.assets > 0

            and

            result.assets ==
            result.liabilities
            +
            result.equity
            +
            result.non_controlling_interest

        )



        print()

        print(
            "Balance Sheet Data:"
        )


        print(
            "Assets:",
            result.assets
        )


        print(
            "Equity:",
            result.equity
        )


        print(
            "Liabilities:",
            result.liabilities
        )


        print(
            "Non Controlling Interest:",
            result.non_controlling_interest
        )


        print(
            "Balanced:",
            balanced
        )



        return {

            "assets":
                result.assets,


            "equity":
                result.equity,


            "liabilities":
                result.liabilities,


            "non_controlling_interest":
                result.non_controlling_interest,


            "total":
                result.assets,


            "balanced":
                balanced

        }



if __name__ == "__main__":

    pass