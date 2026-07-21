import json
import requests


class BalanceSheetParser:

    def __init__(self, url):
        self.url = url

        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "fa-IR,fa;q=0.9,en;q=0.8",
        }

    def extract_datasource(self):

        response = requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        html = response.text

        marker = "var datasource ="

        start = html.find(marker)

        if start == -1:

            marker = "var datasource="

            start = html.find(marker)

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

        invisible_chars = [
            "\u200b",
            "\u200c",
            "\u200d",
            "\u200e",
            "\u200f",
            "\ufeff",
        ]

        for char in invisible_chars:

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

        text = " ".join(
            text.split()
        )

        return text.strip()

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

            return int(
                float(text)
            )

        except (
            ValueError,
            TypeError
        ):

            return 0

    def find_balance_sheet(
        self,
        sheets
    ):

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

            if title_fa in [
                "صورت وضعیت مالی",
                "صورت وضعيت مالي",
            ]:

                return sheet

            if title_en == "balance sheet":

                return sheet

        return None

    def get_balance_table(
        self,
        balance_sheet
    ):

        tables = balance_sheet.get(
            "tables",
            []
        )

        if not tables:

            return None

        return tables[0]

    def get_cell_value(
        self,
        cells,
        address
    ):

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

    def get_cell_text(
        self,
        cells,
        address
    ):

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

            print(
                "Balance sheet table not found"
            )

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

        # -------------------------------------------------
        # ستون B = جدیدترین دوره مالی
        #
        # آدرس‌های تأییدشده از ساختار JSON کدال:
        #
        # B22 = جمع دارایی‌ها
        # B35 = جمع حقوق مالکانه
        # B53 = جمع بدهی‌ها
        # B54 = جمع حقوق مالکانه و بدهی‌ها
        # -------------------------------------------------

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

        # -------------------------------------------------
        # متن ردیف‌ها برای کنترل
        # -------------------------------------------------

        assets_label = self.get_cell_text(
            cells,
            "A22"
        )

        equity_label = self.get_cell_text(
            cells,
            "A35"
        )

        liabilities_label = self.get_cell_text(
            cells,
            "A53"
        )

        total_label = self.get_cell_text(
            cells,
            "A54"
        )

        # -------------------------------------------------
        # کنترل تراز حسابداری
        # -------------------------------------------------

        equity_plus_liabilities = (
            equity
            +
            liabilities
        )

        balanced = (
            assets != 0
            and
            equity != 0
            and
            liabilities != 0
            and
            total != 0
            and
            assets == total
            and
            equity_plus_liabilities == total
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
            "Equity + Liabilities:",
            total
        )

        print(
            "Calculated Equity + Liabilities:",
            equity_plus_liabilities
        )

        print(
            "Balanced:",
            balanced
        )

        print()

        print(
            "Detected Labels:"
        )

        print(
            "A22:",
            assets_label
        )

        print(
            "A35:",
            equity_label
        )

        print(
            "A53:",
            liabilities_label
        )

        print(
            "A54:",
            total_label
        )

        return {
            "assets": assets,
            "equity": equity,
            "liabilities": liabilities,
            "total": total,
            "balanced": balanced
        }


if __name__ == "__main__":

    url = (
        "https://codal.ir/Reports/Decision.aspx?"
        "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"
        "&rt=0"
        "&let=6"
        "&ct=0"
        "&ft=-1"
        "&sheetId=0"
    )

    parser = BalanceSheetParser(
        url
    )

    result = parser.get_balance_data()

    print()

    print(
        result
    )