import requests
import json


class BalanceSheetParser:

    def __init__(self, url):

        self.url = url

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }


    def extract_sheets(self):

        response = requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )

        text = response.text


        # پیدا کردن داده JSON گزارش
        markers = [
            '"sheets":',
            'var sheets =',
            '"sheet":'
        ]

        start = -1

        for m in markers:

            start = text.find(m)

            if start != -1:
                start += len(m)
                break


        if start == -1:

            return []


        while start < len(text) and text[start] != '[':

            start += 1


        if start >= len(text):

            return []


        count = 0
        end = None


        for i in range(start, len(text)):

            if text[i] == '[':

                count += 1


            elif text[i] == ']':
                
                count -= 1


            if count == 0:

                end = i + 1
                break



        if not end:

            return []


        try:

            return json.loads(
                text[start:end]
            )

        except Exception:

            return []



    def get_balance_data(self):


        sheets = self.extract_sheets()


        assets = 0
        equity = 0



        for sheet in sheets:


            title = sheet.get(
                "title_Fa",
                ""
            )


            if "صورت وضعیت مالی" not in title:

                continue



            for table in sheet.get(
                "tables",
                []
            ):


                cells = table.get(
                    "cells",
                    []
                )



                for cell in cells:


                    value = str(
                        cell.get(
                            "value",
                            ""
                        )
                    )



                    if "جمع دارایی" in value:


                        row = cell.get(
                            "rowCode"
                        )


                        for c in cells:


                            if (
                                c.get("rowCode") == row
                                and c.get("address","").startswith("B")
                            ):

                                try:

                                    assets = int(
                                        c.get("value")
                                    )

                                except:

                                    pass




                    if (
                        "حقوق مالکانه" in value
                        or
                        "حقوق مالکین" in value
                    ):


                        row = cell.get(
                            "rowCode"
                        )


                        for c in cells:


                            if (
                                c.get("rowCode") == row
                                and c.get("address","").startswith("B")
                            ):

                                try:

                                    equity = int(
                                        c.get("value")
                                    )

                                except:

                                    pass



        return {

            "assets": assets,

            "equity": equity

        }



if __name__ == "__main__":


    print("Balance Sheet Parser Test")