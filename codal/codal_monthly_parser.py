import requests
import json


class CodalMonthlyParser:


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


        start = text.find('"sheets":')


        if start == -1:
            return None


        start += len('"sheets":')


        while text[start] != '[':
            start += 1


        count = 0


        for i in range(start, len(text)):

            if text[i] == '[':
                count += 1


            elif text[i] == ']':
                count -= 1


            if count == 0:

                end = i + 1
                break



        return json.loads(
            text[start:end]
        )




    def find_monthly_sheet(self):

        sheets = self.extract_sheets()


        if not sheets:
            return None


        for sheet in sheets:

            title = sheet.get(
                "title_Fa",
                ""
            )


            print(
                "SHEET:",
                title
            )


        return sheets




    def get_monthly_data(self):

        sheets = self.find_monthly_sheet()


        if not sheets:
            return None


        result = []


        for sheet in sheets:


            tables = sheet.get(
                "tables",
                []
            )


            for table in tables:


                cells = table.get(
                    "cells",
                    []
                )


                for cell in cells:


                    value = cell.get(
                        "value"
                    )


                    if value and (
                        "فروش" in str(value)
                        or
                        "درآمد" in str(value)
                    ):


                        result.append({

                            "address": cell.get("address"),

                            "value": value

                        })


        return result





if __name__ == "__main__":


    url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=QxYX7A2pkntVRzKRJzUFvg%3d%3d&rt=0&let=58&ct=0&ft=-1"


    parser = CodalMonthlyParser(
        url
    )


    data = parser.get_monthly_data()


    print("================")

    print(data)