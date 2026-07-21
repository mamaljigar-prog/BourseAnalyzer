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
            raise ValueError(
                "Sheets not found"
            )

        start += len(marker)

        while (
            start < len(text)
            and text[start] != "["
        ):
            start += 1

        if start >= len(text):

            raise ValueError(
                "Sheets array not found"
            )

        count = 0
        end = None

        for i in range(
            start,
            len(text)
        ):

            if text[i] == "[":
                count += 1

            elif text[i] == "]":
                count -= 1

            if count == 0:

                end = i + 1

                break

        if end is None:

            raise ValueError(
                "Invalid sheets JSON"
            )

        return json.loads(
            text[start:end]
        )

    def normalize(self, value):

        if value is None:
            return ""

        return (
            str(value)
            .replace(
                "\u200c",
                ""
            )
            .replace(
                "\u200e",
                ""
            )
            .replace(
                "\u200f",
                ""
            )
            .strip()
        )

    def find_sheet(
        self,
        title
    ):

        sheets = self.extract_sheets()

        target = self.normalize(
            title
        )

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

            if (
                title_fa == target
                or
                title_en == target.lower()
            ):

                return sheet

        return None

    def parse_number(
        self,
        value
    ):

        if value is None:
            return 0

        text = str(
            value
        ).strip()

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
            .replace(
                ",",
                ""
            )
            .replace(
                "٬",
                ""
            )
            .replace(
                " ",
                ""
            )
        )

        try:

            return int(
                float(text)
            )

        except (
            ValueError,
            TypeError
        ):

            return 0

    def find_row(
        self,
        cells,
        labels
    ):

        normalized_labels = {
            self.normalize(
                label
            )
            for label in labels
        }

        for cell in cells:

            if cell.get(
                "columnCode"
            ) != 1:

                continue

            value = self.normalize(
                cell.get(
                    "value",
                    ""
                )
            )

            if value in normalized_labels:

                return cell.get(
                    "rowCode"
                )

        return None

    def get_row_cells(
        self,
        cells,
        row_code
    ):

        if row_code is None:

            return []

        result = []

        for cell in cells:

            if (
                cell.get(
                    "rowCode"
                )
                ==
                row_code
            ):

                result.append(
                    {
                        "address":
                            cell.get(
                                "address"
                            ),

                        "columnCode":
                            cell.get(
                                "columnCode"
                            ),

                        "value":
                            self.parse_number(
                                cell.get(
                                    "value"
                                )
                            ),

                        "year":
                            cell.get(
                                "yearEndToDate"
                            ),

                        "period":
                            cell.get(
                                "periodEndToDate"
                            )
                    }
                )

        return result

    def find_row_value(
        self,
        cells,
        labels
    ):

        row_code = self.find_row(
            cells,
            labels
        )

        return self.get_row_cells(
            cells,
            row_code
        )

    def get_financial_data(
        self
    ):

        sheet = self.find_sheet(
            "صورت سود و زیان"
        )

        if sheet is None:

            print(
                "Income Statement not found"
            )

            return {
                "sales": [],
                "gross_profit": [],
                "operating_profit": [],
                "net_profit": []
            }

        tables = sheet.get(
            "tables",
            []
        )

        if not tables:

            print(
                "Income Statement table not found"
            )

            return {
                "sales": [],
                "gross_profit": [],
                "operating_profit": [],
                "net_profit": []
            }

        cells = tables[0].get(
            "cells",
            []
        )

        data = {

            "sales":
                self.find_row_value(
                    cells,
                    {
                        "درآمدهای عملیاتی",
                        "درآمدهاي عملياتي"
                    }
                ),

            "gross_profit":
                self.find_row_value(
                    cells,
                    {
                        "سود(زیان) ناخالص",
                        "سود(زيان) ناخالص"
                    }
                ),

            "operating_profit":
                self.find_row_value(
                    cells,
                    {
                        "سود(زیان) عملیاتی",
                        "سود(زيان) عملياتي"
                    }
                ),

            "net_profit":
                self.find_row_value(
                    cells,
                    {
                        "سود(زیان) خالص",
                        "سود(زيان) خالص"
                    }
                )

        }

        return data


if __name__ == "__main__":

    url = (
        "https://codal.ir/Reports/Decision.aspx?"
        "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"
        "&rt=0"
        "&let=6"
        "&ct=0"
        "&ft=-1"
        "&sheetId=1"
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