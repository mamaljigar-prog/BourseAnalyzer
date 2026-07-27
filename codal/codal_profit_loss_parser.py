import json
import re
import requests


class CodalProfitLossParser:

    CURRENT_COLUMN_CODE = 2
    COMPARABLE_COLUMN_CODE = 5
    ANNUAL_COLUMN_CODE = 1

    def __init__(
        self,
        url,
        current_column_code=None,
        comparable_column_code=None,
        annual_column_code=None
    ):

        self.url = url

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/150.0.0.0 Safari/537.36"
            )
        }

        if current_column_code is not None:
            self.CURRENT_COLUMN_CODE = current_column_code

        if comparable_column_code is not None:
            self.COMPARABLE_COLUMN_CODE = comparable_column_code

        if annual_column_code is not None:
            self.ANNUAL_COLUMN_CODE = annual_column_code

        self._response_text = None
        self._sheets = None
        self._income_statement_sheet = None
        self._cells = None

    # =========================================================
    # HTTP
    # =========================================================

    def fetch_text(self):

        if self._response_text is not None:
            return self._response_text

        response = requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        response.encoding = response.apparent_encoding or "utf-8"

        self._response_text = response.text

        return self._response_text

    # =========================================================
    # TEXT NORMALIZATION
    # =========================================================

    def normalize(
        self,
        value
    ):

        if value is None:
            return ""

        text = str(value)

        # -----------------------------------------------------
        # Common mojibake repair
        # -----------------------------------------------------

        replacements = {

            "Ã™Å ": "ÛŒ",
            "Ã™Æ’": "Ú©",
            "Ã›Å’": "ÛŒ",
            "ÃšÂ©": "Ú©",

            "ÙŠ": "ÛŒ",
            "Ùƒ": "Ú©",

            "â€Œ": "\u200c",
            "â€Ž": "\u200e",
            "â€Ž": "\u200e",
            "â€Ž": "\u200e",

            "ي": "ی",
            "ى": "ی",
            "ك": "ک",

            "ۀ": "ه",
            "ة": "ه",

            "ؤ": "و",
            "إ": "ا",
            "أ": "ا",

            "\u200c": "",
            "\u200e": "",
            "\u200f": ""

        }

        for old, new in replacements.items():

            text = text.replace(
                old,
                new
            )

        # -----------------------------------------------------
        # Attempt generic mojibake repair
        # -----------------------------------------------------

        if (
            "Ã" in text
            or
            "Â" in text
            or
            "Ø" in text
            or
            "Ù" in text
        ):

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

                if repaired != text:

                    text = repaired

            except (
                UnicodeEncodeError,
                UnicodeDecodeError
            ):

                pass

        return (
            text
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
            .replace(
                " ",
                ""
            )
            .replace(
                "\t",
                ""
            )
            .replace(
                "\r",
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
            .strip()
        )

    # =========================================================
    # COMPACT NORMALIZATION
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
                "\r",
                ""
            )
            .replace(
                "\n",
                ""
            )
            .replace(
                "‌",
                ""
            )
            .replace(
                "ۀ",
                "ه"
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

        # -----------------------------------------------------
        # Persian / Arabic digits
        # -----------------------------------------------------

        digit_translation = str.maketrans(

            "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩",

            "01234567890123456789"

        )

        text = text.translate(
            digit_translation
        )

        # -----------------------------------------------------
        # Mojibake digit patterns
        # -----------------------------------------------------

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
            "Û¹": "9",

            "Ã›Â°": "0",
            "Ã›Â±": "1",
            "Ã›Â²": "2",
            "Ã›Â³": "3",
            "Ã›Â´": "4",
            "Ã›Âµ": "5",
            "Ã›Â¶": "6",
            "Ã›Â·": "7",
            "Ã›Â¸": "8",
            "Ã›Â¹": "9"

        }

        for old, new in (
            mojibake_digits.items()
        ):

            text = text.replace(
                old,
                new
            )

        # -----------------------------------------------------
        # Negative signs
        # -----------------------------------------------------

        text = (
            text
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
            .replace(
                "âˆ’",
                "-"
            )
            .replace(
                "â€“",
                "-"
            )
            .replace(
                "â€”",
                "-"
            )
        )

        # -----------------------------------------------------
        # Parentheses negative values
        # -----------------------------------------------------

        negative = (

            text.startswith("(")

            and

            text.endswith(")")

        )

        if negative:

            text = text[1:-1]

        # -----------------------------------------------------
        # Remove separators
        # -----------------------------------------------------

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
                "\u00a0",
                ""
            )
        )

        # -----------------------------------------------------
        # Extract numeric part
        # -----------------------------------------------------

        match = re.search(

            r"-?\d+(?:\.\d+)?",

            text

        )

        if not match:

            return 0

        number_text = match.group(
            0
        )

        try:

            number = int(
                float(
                    number_text
                )
            )

            if negative:

                number = -abs(
                    number
                )

            return number

        except (
            ValueError,
            TypeError
        ):

            return 0

    # =========================================================
    # EXTRACT SHEETS
    # =========================================================

    def extract_sheets(
        self
    ):

        if self._sheets is not None:

            return self._sheets

        text = self.fetch_text()

        # -----------------------------------------------------
        # Primary marker
        # -----------------------------------------------------

        markers = [

            '"sheets":',

            '"sheets" :',

            "'sheets':",

            "'sheets' :"

        ]

        start = -1

        marker_used = None

        for marker in markers:

            start = text.find(
                marker
            )

            if start != -1:

                marker_used = marker

                break

        if start == -1:

            # -------------------------------------------------
            # Alternative: JSON embedded in script
            # -------------------------------------------------

            match = re.search(

                r'"sheets"\s*:\s*\[',

                text

            )

            if match:

                start = match.start()

                marker_used = (
                    '"sheets":'
                )

        if start == -1:

            raise ValueError(
                "Sheets not found"
            )

        start += len(
            marker_used
        )

        # -----------------------------------------------------
        # Find opening bracket
        # -----------------------------------------------------

        while (

            start < len(text)

            and

            text[start] != "["

        ):

            start += 1

        if start >= len(text):

            raise ValueError(
                "Invalid sheets JSON"
            )

        # -----------------------------------------------------
        # Balanced JSON array extraction
        # -----------------------------------------------------

        depth = 0
        end = None

        in_string = False
        escaped = False

        for index in range(

            start,

            len(text)

        ):

            char = text[index]

            if in_string:

                if escaped:

                    escaped = False

                elif char == "\\":

                    escaped = True

                elif char == '"':

                    in_string = False

                continue

            if char == '"':

                in_string = True

                continue

            if char == "[":

                depth += 1

            elif char == "]":

                depth -= 1

                if depth == 0:

                    end = index + 1

                    break

        if end is None:

            raise ValueError(
                "Invalid sheets JSON"
            )

        raw_json = text[
            start:end
        ]

        try:

            self._sheets = json.loads(
                raw_json
            )

        except json.JSONDecodeError:

            # -------------------------------------------------
            # Try repairing common malformed content
            # -------------------------------------------------

            try:

                self._sheets = json.loads(

                    raw_json
                    .replace(
                        "\ufeff",
                        ""
                    )

                )

            except json.JSONDecodeError as exc:

                raise ValueError(

                    "Invalid sheets JSON"

                ) from exc

        return self._sheets

    # =========================================================
    # FIND INCOME STATEMENT SHEET
    # =========================================================

    def find_income_statement_sheet(
        self
    ):

        if self._income_statement_sheet is not None:

            return self._income_statement_sheet

        sheets = self.extract_sheets()

        best_sheet = None
        best_score = 0

        for sheet in sheets:

            title = self.normalize(

                sheet.get(
                    "title_Fa",
                    ""
                )

            )

            title_en = self.normalize(

                sheet.get(
                    "title",
                    ""
                )

            )

            compact = (
                self.normalized_compact(
                    title
                )
            )

            compact_en = (
                self.normalized_compact(
                    title_en
                )
            )

            score = 0

            # -------------------------------------------------
            # Persian mojibake / Persian
            # -------------------------------------------------

            income_keywords = [

                "صورتسودوزیان",

                "صورتسودوزیانجامع",

                "سودوزیان",

                "سودوزیانجامع",

                "صورتسود",

                "سودو‌زیان",

                "سود",

                "زیان"

            ]

            for keyword in income_keywords:

                normalized_keyword = (
                    self.normalized_compact(
                        keyword
                    )
                )

                if (
                    normalized_keyword
                    and
                    normalized_keyword in compact
                ):

                    if (
                        "صورتسودوزیان"
                        in normalized_keyword
                    ):

                        score += 20

                    elif (
                        "سودوزیان"
                        in normalized_keyword
                    ):

                        score += 15

                    elif (
                        "صورتسود"
                        in normalized_keyword
                    ):

                        score += 10

                    else:

                        score += 2

            # -------------------------------------------------
            # English title fallback
            # -------------------------------------------------

            english_keywords = [

                "incomestatement",

                "profitandloss",

                "profitloss",

                "statementofprofit",

                "statementofincome"

            ]

            for keyword in english_keywords:

                if (
                    keyword
                    in compact_en
                ):

                    score += 20

            # -------------------------------------------------
            # Sheet content scoring
            # -------------------------------------------------

            tables = sheet.get(
                "tables",
                []
            )

            cell_count = 0

            sample_text = ""

            for table in tables:

                cells = table.get(
                    "cells",
                    []
                )

                cell_count += len(
                    cells
                )

                for cell in cells[:100]:

                    sample_text += " "

                    sample_text += self.normalize(

                        cell.get(
                            "value",
                            ""
                        )

                    )

            sample_compact = (
                self.normalized_compact(
                    sample_text
                )
            )

            financial_keywords = [

                "درآمد",

                "فروش",

                "بهایتمامشده",

                "سودناخالص",

                "سودعملیاتی",

                "سودخالص",

                "سودوزیان",

                "هزینه"

            ]

            for keyword in financial_keywords:

                if (
                    self.normalized_compact(
                        keyword
                    )
                    in
                    sample_compact
                ):

                    score += 2

            # -------------------------------------------------
            # Prefer sheets with meaningful tables
            # -------------------------------------------------

            if cell_count > 20:

                score += 2

            if cell_count > 100:

                score += 2

            # -------------------------------------------------
            # Keep best match
            # -------------------------------------------------

            if score > best_score:

                best_score = score

                best_sheet = sheet

        self._income_statement_sheet = (
            best_sheet
        )

        return best_sheet

    # =========================================================
    # GET CELLS
    # =========================================================

    def get_cells(
        self
    ):

        if self._cells is not None:

            return self._cells

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

        # -----------------------------------------------------
        # Select table with maximum meaningful cells
        # -----------------------------------------------------

        table = max(

            tables,

            key=lambda item: len(

                item.get(
                    "cells",
                    []
                )

            )

        )

        self._cells = table.get(
            "cells",
            []
        )

        return self._cells

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

        normalized_keywords = [

            keyword

            for keyword in normalized_keywords

            if keyword

        ]

        # -----------------------------------------------------
        # First pass: exact strong match
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
                    title
                    ==
                    keyword
                ):

                    return cell.get(
                        "rowCode"
                    )

        # -----------------------------------------------------
        # Second pass: contains
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
                    in
                    title
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
    # DEBUG CONCEPT
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
                        "Ø¯Ø±Ø¢Ù…Ø¯Ù‡Ø§ÛŒ Ø¹Ù…Ù„ÛŒØ§ØªÛŒ"
                    ],

                    [
                        "Ø¯Ø±Ø¢Ù…Ø¯Ù‡Ø§ÙŠ Ø¹Ù…Ù„ÛŒØ§ØªÙŠ"
                    ],

                    [
                        "درآمدهای عملیاتی"
                    ],

                    [
                        "درآمدهای عملیاتی"
                    ],

                    [
                        "فروش"
                    ],

                    [
                        "ØÙØ±ÙˆØ´"
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
                        "Ø³ÙˆØ¯ (Ø²ÛŒØ§Ù†) Ù†Ø§Ø®Ø§Ù„Øµ"
                    ],

                    [
                        "Ø³ÙˆØ¯(Ø²ÛŒØ§Ù†) Ù†Ø§Ø®Ø§Ù„Øµ"
                    ],

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
                        "زیان ناخالص"
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
                        "Ø³ÙˆØ¯ (Ø²ÛŒØ§Ù†) Ø¹Ù…Ù„ÛŒØ§ØªÛŒ"
                    ],

                    [
                        "Ø³ÙˆØ¯(Ø²ÛŒØ§Ù†) Ø¹Ù…Ù„ÛŒØ§ØªÛŒ"
                    ],

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
                        "Ø³Ø§ÛŒØ± Ø¯Ø±Ø¢Ù…Ø¯Ù‡Ø§ Ùˆ Ù‡Ø²ÛŒÙ†Ù‡ Ù‡Ø§ÛŒ ØºÛŒØ±Ø¹Ù…Ù„ÛŒØ§ØªÛŒ"
                    ],

                    [
                        "Ø³Ø§ÛŒØ± Ø¯Ø±Ø¢Ù…Ø¯Ù‡Ø§ Ùˆ Ù‡Ø²ÛŒÙ†Ù‡â€ŒÙ‡Ø§ÛŒ ØºÛŒØ±Ø¹Ù…Ù„ÛŒØ§ØªÛŒ"
                    ],

                    [
                        "سایر درآمدها و هزینه های غیرعملیاتی"
                    ],

                    [
                        "سایر درآمدها و هزینه‌های غیرعملیاتی"
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
                        "Ø³ÙˆØ¯ (Ø²ÛŒØ§Ù†) Ø®Ø§Ù„Øµ"
                    ],

                    [
                        "Ø³ÙˆØ¯(Ø²ÛŒØ§Ù†) Ø®Ø§Ù„Øµ"
                    ],

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


# =============================================================
# STANDALONE TEST
# =============================================================

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