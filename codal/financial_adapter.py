import json
import requests


class CodalProfitLossParser:

    CURRENT_COLUMN_CODE = 2
    COMPARABLE_COLUMN_CODE = 3
    ANNUAL_COLUMN_CODE = 5

    def __init__(self, url):

        self.url = url

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

    # =========================================================
    # EXTRACT SHEETS
    # =========================================================

    def extract_sheets(self):

        response = requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        text = response.text

        marker = '"sheets":'

        start = text.find(
            marker
        )

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
                "Invalid sheets JSON"
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

    # =========================================================
    # NORMALIZE TEXT
    # =========================================================

    def normalize(
        self,
        value
    ):

        if value is None:

            return ""

        text = str(
            value
        )

        # -----------------------------------------------------
        # Common Codal mojibake repair
        # -----------------------------------------------------

        for _ in range(3):

            if (
                "Ø" not in text
                and
                "Ù" not in text
                and
                "Û" not in text
                and
                "Ã" not in text
                and
                "â" not in text
                and
                "Ú" not in text
            ):

                break

            try:

                repaired = (
                    text
                    .encode(
                        "latin1"
                    )
                    .decode(
                        "utf-8"
                    )
                )

                if repaired == text:

                    break

                text = repaired

            except (
                UnicodeEncodeError,
                UnicodeDecodeError
            ):

                break

        # -----------------------------------------------------
        # Explicit common mojibake replacements
        # -----------------------------------------------------

        replacements = {

            "Ø¯Ø±Ø¢Ù…Ø¯Ù‡Ø§ÛŒ":
                "درآمدهای",

            "Ø¯Ø±Ø¢Ù…Ø¯Ù‡Ø§ÙŠ":
                "درآمدهای",

            "Ø¯Ø±Ø¢Ù…Ø¯Ù‡Ø§":
                "درآمدها",

            "Ø¯Ø±Ø¢Ù…Ø¯":
                "درآمد",

            "Ø³ÙˆØ¯":
                "سود",

            "Ø²ÛŒØ§Ù†":
                "زیان",

            "Ø²ÛŒØ§Ù†":
                "زیان",

            "Ø®Ø§Ù„Øµ":
                "خالص",

            "Ù†Ø§Ø®Ø§Ù„Øµ":
                "ناخالص",

            "Ø¹Ù…Ù„ÛŒØ§ØªÛŒ":
                "عملیاتی",

            "Ø¹Ù…Ù„ÛŒØ§ØªÛŒ":
                "عملیاتی",

            "ØºÛŒØ±Ø¹Ù…Ù„ÛŒØ§ØªÛŒ":
                "غیرعملیاتی",

            "ØºÛŒØ±Ø¹Ù…Ù„ÛŒØ§ØªÛŒ":
                "غیرعملیاتی",

            "Ø³Ø§ÛŒØ±":
                "سایر",

            "Ø³Ø±Ù…Ø§ÛŒÙ‡":
                "سرمایه",

            "Ú¯Ø°Ø§Ø±ÛŒ":
                "گذاری",

            "ØµÙˆØ±Øª":
                "صورت",

            "Ùˆ":
                "و",

            "Ù‡Ø²ÛŒÙ†Ù‡":
                "هزینه",

            "Ù‡Ø§":
                "ها",

            "ÙØ±ÙˆØ´":
                "فروش",

            "ÙŠ":
                "ی",

            "Ùƒ":
                "ک",

            "ÛŒ":
                "ی",

            "Ú©":
                "ک"

        }

        for old, new in replacements.items():

            text = text.replace(
                old,
                new
            )

        # -----------------------------------------------------
        # Persian / Arabic character normalization
        # -----------------------------------------------------

        character_replacements = {

            "ي": "ی",

            "ى": "ی",

            "ك": "ک",

            "ۀ": "ه",

            "ة": "ه",

            "ؤ": "و",

            "إ": "ا",

            "أ": "ا",

            "ٱ": "ا",

            "ـ": "",

            "\u200c": "",

            "\u200e": "",

            "\u200f": "",

            "\ufeff": ""

        }

        for old, new in (
            character_replacements.items()
        ):

            text = text.replace(
                old,
                new
            )

        return (
            text
            .strip()
        )

    # =========================================================
    # NORMALIZE COMPARISON TEXT
    # =========================================================

    def normalized_compact(
        self,
        value
    ):

        text = self.normalize(
            value
        )

        return (
            text
            .replace(
                " ",
                ""
            )
            .replace(
                "\t",
                ""
            )
            .replace(
                "\n",
                ""
            )
            .replace(
                "(",
                ""
            )
            .replace(
                ")",
                ""
            )
            .replace(
                "‌",
                ""
            )
        )

    # =========================================================
    # PARSE NUMBER
    # =========================================================

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

        # Persian digits
        persian_digits = str.maketrans(

            "۰۱۲۳۴۵۶۷۸۹",

            "0123456789"

        )

        text = text.translate(
            persian_digits
        )

        # Arabic digits
        arabic_digits = str.maketrans(

            "٠١٢٣٤٥٦٧٨٩",

            "0123456789"

        )

        text = text.translate(
            arabic_digits
        )

        # Mojibake digits
        mojibake_digits = {

            "Û°": "0",
            "Û±": "1",
            "Û²": "2",
            "Û³": "3",
            "Û´": "4",
            "Ûµ": "5",
            "Û¶": "6",
            "Û·": "7",
            "Û¸": "8",
            "Û¹": "9"

        }

        for old, new in (
            mojibake_digits.items()
        ):

            text = text.replace(
                old,
                new
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
            .replace(
                "−",
                "-"
            )
            .replace(
                "–",
                "-"
            )
            .replace(
                "—",
                "-"
            )
        )

        # Parentheses mean negative
        if (
            text.startswith("(")
            and
            text.endswith(")")
        ):

            text = (
                "-"
                +
                text[1:-1]
            )

        try:

            return int(
                float(
                    text
                )
            )

        except (
            ValueError,
            TypeError
        ):

            return 0

    # =========================================================
    # FIND INCOME STATEMENT SHEET
    # =========================================================

    def find_income_statement_sheet(
        self
    ):

        sheets = (
            self.extract_sheets()
        )

        best_sheet = None
        best_score = 0

        for sheet in sheets:

            title = self.normalize(

                sheet.get(
                    "title_Fa",
                    ""
                )

            )

            compact = (
                self.normalized_compact(
                    title
                )
            )

            score = 0

            if (
                "صورتسودوزیان" in compact
            ):

                score += 10

            if (
                "سودوزیان" in compact
            ):

                score += 10

            if (
                "صورتسود" in compact
            ):

                score += 5

            if (
                "سود" in compact
            ):

                score += 2

            if (
                "زیان" in compact
            ):

                score += 2

            if score > best_score:

                best_score = score

                best_sheet = sheet

        return best_sheet

    # =========================================================
    # GET CELLS
    # =========================================================

    def get_cells(
        self
    ):

        sheet = (
            self.find_income_statement_sheet()
        )

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

        # Prefer table containing the most cells
        table = max(
            tables,
            key=lambda x: len(
                x.get(
                    "cells",
                    []
                )
            )
        )

        return table.get(
            "cells",
            []
        )

    # =========================================================
    # FIND ROW
    # =========================================================

    def find_row(
        self,
        cells,
        keywords
    ):

        normalized_keywords = [

            self.normalized_compact(
                keyword
            )

            for keyword in keywords

        ]

        # -----------------------------------------------------
        # First pass: exact / strong match
        # -----------------------------------------------------

        for cell in cells:

            title = self.normalized_compact(

                cell.get(
                    "value",
                    ""
                )

            )

            if not title:

                continue

            for keyword in (
                normalized_keywords
            ):

                if (
                    keyword
                    and
                    keyword in title
                ):

                    return cell.get(
                        "rowCode"
                    )

        return None

    # =========================================================
    # FIND ROW BY PRIORITY
    # =========================================================

    def find_row_by_priority(
        self,
        cells,
        keyword_groups
    ):

        for group in keyword_groups:

            row_code = (
                self.find_row(
                    cells,
                    group
                )
            )

            if row_code is not None:

                return row_code

        return None

    # =========================================================
    # GET RAW ROW VALUES
    # =========================================================

    def get_row_values(
        self,
        cells,
        row_code
    ):

        result = []

        if row_code is None:

            return result

        for cell in cells:

            if (
                cell.get(
                    "rowCode"
                )
                !=
                row_code
            ):

                continue

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

    # =========================================================
    # EXTRACT CONCEPT
    # =========================================================

    def extract_concept(
        self,
        cells,
        keywords
    ):

        row_code = (
            self.find_row(
                cells,
                keywords
            )
        )

        if row_code is None:

            return []

        return (
            self.get_row_values(
                cells,
                row_code
            )
        )

    # =========================================================
    # EXTRACT CONCEPT WITH PRIORITY
    # =========================================================

    def extract_concept_priority(
        self,
        cells,
        keyword_groups
    ):

        row_code = (
            self.find_row_by_priority(
                cells,
                keyword_groups
            )
        )

        if row_code is None:

            return []

        return (
            self.get_row_values(
                cells,
                row_code
            )
        )

    # =========================================================
    # FIND COLUMN VALUE
    # =========================================================

    def find_column_value(
        self,
        rows,
        column_code
    ):

        for row in rows:

            if (
                row.get(
                    "columnCode"
                )
                ==
                column_code
            ):

                return row

        return None

    # =========================================================
    # BUILD PERIOD DATA
    # =========================================================

    def build_period_data(
        self,
        rows,
        column_code
    ):

        row = (
            self.find_column_value(
                rows,
                column_code
            )
        )

        if row is None:

            return {

                "available":
                    False,

                "value":
                    None,

                "report_period_end":
                    None,

                "fiscal_year_end":
                    None

            }

        return {

            "available":
                True,

            "value":
                row.get(
                    "value",
                    0
                ),

            "report_period_end":
                row.get(
                    "period"
                ),

            "fiscal_year_end":
                row.get(
                    "year"
                )

        }

    # =========================================================
    # BUILD CANONICAL CONCEPT
    # =========================================================

    def build_canonical_concept(
        self,
        rows
    ):

        return {

            "current_period":

                self.build_period_data(

                    rows,

                    self.CURRENT_COLUMN_CODE

                ),

            "comparable_period":

                self.build_period_data(

                    rows,

                    self.COMPARABLE_COLUMN_CODE

                ),

            "annual":

                self.build_period_data(

                    rows,

                    self.ANNUAL_COLUMN_CODE

                ),

            "raw_rows":

                rows

        }

    # =========================================================
    # DEBUG ROW MATCH
    # =========================================================

    def debug_concept(
        self,
        name,
        rows
    ):

        print()

        print(
            "DEBUG CONCEPT:",
            name
        )

        if not rows:

            print(
                "  NOT FOUND"
            )

            return

        for row in rows:

            print(

                "  ROW:",
                row.get(
                    "address"
                ),
                "| COLUMN:",
                row.get(
                    "columnCode"
                ),
                "| VALUE:",
                row.get(
                    "value"
                ),
                "| PERIOD:",
                row.get(
                    "period"
                ),
                "| YEAR:",
                row.get(
                    "year"
                )

            )

    # =========================================================
    # FINANCIAL DATA
    # =========================================================

    def get_financial_data(
        self
    ):

        cells = (
            self.get_cells()
        )

        # =====================================================
        # SALES
        # =====================================================

        sales_rows = (
            self.extract_concept_priority(

                cells,

                [

                    [

                        "درآمدهای عملیاتی"

                    ],

                    [

                        "درآمدهاي عملیاتی"

                    ],

                    [

                        "فروش"

                    ],

                    [

                        "درآمد عملیاتی"

                    ],

                    [

                        "درآمدهای عملیاتی"

                    ]

                ]

            )
        )

        # =====================================================
        # GROSS PROFIT
        # =====================================================

        gross_profit_rows = (
            self.extract_concept_priority(

                cells,

                [

                    [

                        "سود (زیان) ناخالص"

                    ],

                    [

                        "سود(زیان) ناخالص"

                    ],

                    [

                        "سود ناخالص"

                    ],

                    [

                        "سود ناخالص"

                    ],

                    [

                        "سود (زیان) ناخالص"

                    ]

                ]

            )
        )

        # =====================================================
        # OPERATING PROFIT
        # =====================================================

        operating_profit_rows = (
            self.extract_concept_priority(

                cells,

                [

                    [

                        "سود (زیان) عملیاتی"

                    ],

                    [

                        "سود(زیان) عملیاتی"

                    ],

                    [

                        "سود عملیاتی"

                    ],

                    [

                        "زیان عملیاتی"

                    ]

                ]

            )
        )

        # =====================================================
        # NON OPERATING INCOME
        # =====================================================

        non_operating_rows = (
            self.extract_concept_priority(

                cells,

                [

                    [

                        "سایر درآمدها و هزینه های غیرعملیاتی"

                    ],

                    [

                        "سایر درآمدها و هزینه‌های غیرعملیاتی"

                    ],

                    [

                        "سایر درآمدها و هزینه های غیر عملیاتی"

                    ],

                    [

                        "درآمدهای غیرعملیاتی"

                    ],

                    [

                        "درآمد غیرعملیاتی"

                    ],

                    [

                        "سایر درآمدها"

                    ],

                    [

                        "درآمد سرمایه گذاری"

                    ],

                    [

                        "درآمد سرمایه‌گذاری"

                    ]

                ]

            )
        )

        # =====================================================
        # NET PROFIT
        # =====================================================

        net_profit_rows = (
            self.extract_concept_priority(

                cells,

                [

                    [

                        "سود (زیان) خالص"

                    ],

                    [

                        "سود(زیان) خالص"

                    ],

                    [

                        "سود خالص"

                    ],

                    [

                        "زیان خالص"

                    ]

                ]

            )
        )

        # =====================================================
        # DEBUG
        # =====================================================

        self.debug_concept(
            "SALES",
            sales_rows
        )

        self.debug_concept(
            "GROSS PROFIT",
            gross_profit_rows
        )

        self.debug_concept(
            "OPERATING PROFIT",
            operating_profit_rows
        )

        self.debug_concept(
            "NON OPERATING INCOME",
            non_operating_rows
        )

        self.debug_concept(
            "NET PROFIT",
            net_profit_rows
        )

        # =====================================================
        # CANONICAL DATA
        # =====================================================

        canonical_data = {

            "sales":

                self.build_canonical_concept(

                    sales_rows

                ),

            "gross_profit":

                self.build_canonical_concept(

                    gross_profit_rows

                ),

            "operating_profit":

                self.build_canonical_concept(

                    operating_profit_rows

                ),

            "non_operating_income":

                self.build_canonical_concept(

                    non_operating_rows

                ),

            "net_profit":

                self.build_canonical_concept(

                    net_profit_rows

                )

        }

        return canonical_data


if __name__ == "__main__":

    url = (

        "https://codal.ir/Reports/Decision.aspx?"

        "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"

        "&rt=0&let=6&ct=0&ft=-1&sheetId=1"

    )

    parser = CodalProfitLossParser(
        url
    )

    result = (
        parser.get_financial_data()
    )

    print(

        json.dumps(

            result,

            ensure_ascii=False,

            indent=4

        )

    )