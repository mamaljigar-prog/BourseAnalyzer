import json
import requests


class CodalProfitLossParser:

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

        response.raise_for_status()

        text = response.text

        marker = '"sheets":'

        start = text.find(marker)

        if start == -1:
            raise ValueError("Sheets not found")

        start += len(marker)

        while start < len(text) and text[start] != "[":
            start += 1

        if start >= len(text):
            raise ValueError("Sheets array not found")


        count = 0
        end = None

        for i in range(start, len(text)):

            if text[i] == "[":
                count += 1

            elif text[i] == "]":
                count -= 1

            if count == 0:
                end = i + 1
                break


        if end is None:
            raise ValueError("Invalid sheets JSON")


        return json.loads(
            text[start:end]
        )


    def normalize(self, value):

        if value is None:
            return ""

        return (
            str(value)
            .replace("\u200c", "")
            .replace("\u200e", "")
            .replace("\u200f", "")
            .replace("ي", "ی")
            .replace("ك", "ک")
            .strip()
        )


    def parse_number(self, value):

        if value is None:
            return 0

        text = str(value).strip()

        if text == "":
            return 0


        translation = str.maketrans(
            "۰۱۲۳۴۵۶۷۸۹",
            "0123456789"
        )

        text = text.translate(
            translation
        )


        text = (
            text
            .replace(",", "")
            .replace(" ", "")
        )


        try:
            return int(float(text))

        except:

            return 0



    def find_income_statement_sheet(self):

        sheets = self.extract_sheets()

        for sheet in sheets:

            title = self.normalize(
                sheet.get(
                    "title_Fa",
                    ""
                )
            )

            if (
                "صورت سود" in title
                or
                "سود و زیان" in title
            ):

                return sheet


        return None



    def get_cells(self):

        sheet = self.find_income_statement_sheet()

        if sheet is None:

            raise ValueError(
                "Income statement not found"
            )


        tables = sheet.get(
            "tables",
            []
        )

        if not tables:

            raise ValueError(
                "Tables not found"
            )


        return tables[0].get(
            "cells",
            []
        )



    def find_row(self, cells, keywords):

        keywords = [
            self.normalize(x)
            for x in keywords
        ]


        for cell in cells:

            if cell.get("columnCode") != 1:
                continue


            title = self.normalize(
                cell.get(
                    "value",
                    ""
                )
            )


            for key in keywords:

                if key in title:

                    return cell.get(
                        "rowCode"
                    )


        return None



    def get_row_values(self, cells, row_code):

        result = []


        for cell in cells:

            if cell.get(
                "rowCode"
            ) == row_code:


                result.append(
                    {
                        "address": cell.get(
                            "address"
                        ),

                        "columnCode": cell.get(
                            "columnCode"
                        ),

                        "value": self.parse_number(
                            cell.get(
                                "value"
                            )
                        ),

                        "year": cell.get(
                            "yearEndToDate"
                        ),

                        "period": cell.get(
                            "periodEndToDate"
                        )
                    }
                )


        return result



    def extract_concept(self, cells, keywords):

        row = self.find_row(
            cells,
            keywords
        )


        if row is None:
            return []


        return self.get_row_values(
            cells,
            row
        )



    def get_financial_data(self):

        cells = self.get_cells()


        return {

            "sales":
                self.extract_concept(
                    cells,
                    [
                        "درآمدهای عملیاتی",
                        "درآمدهاي عملياتي"
                    ]
                ),


            "gross_profit":
                self.extract_concept(
                    cells,
                    [
                        "سود(زیان) ناخالص",
                        "سود(زيان) ناخالص"
                    ]
                ),


            "operating_profit":
                self.extract_concept(
                    cells,
                    [
                        "سود(زیان) عملیاتی",
                        "سود(زيان) عملياتى"
                    ]
                ),


            "non_operating_income":
                self.extract_concept(
                    cells,
                    [
                        "سایر درآمدها و هزینه های غیرعملیاتی",
                        "ساير درآمدها و هزينه هاي غيرعملياتي"
                    ]
                ),


            "net_profit":
                self.extract_concept(
                    cells,
                    [
                        "سود(زیان) خالص",
                        "سود(زيان) خالص"
                    ]
                )

        }



if __name__ == "__main__":


    url = (
        "https://codal.ir/Reports/Decision.aspx?"
        "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"
        "&rt=0&let=6&ct=0&ft=-1&sheetId=1"
    )


    parser = CodalProfitLossParser(
        url
    )


    result = parser.get_financial_data()


    print(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=4
        )
    )