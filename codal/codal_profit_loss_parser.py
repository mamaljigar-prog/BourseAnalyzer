import json
import re
import requests


class CodalProfitLossParser:

    def __init__(self, url):
        self.url = url

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

        self._sheets = None
        self._cells = None
        self._column_mapping = None

        self._period_months = None

        self._current_date = None
        self._previous_comparable_date = None
        self._annual_previous_date = None

    # =========================================================
    # HTTP / SHEET EXTRACTION
    # =========================================================

    def extract_sheets(self):

        if self._sheets is not None:
            return self._sheets

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

        try:
            self._sheets = json.loads(
                text[start:end]
            )

        except json.JSONDecodeError as exc:
            raise ValueError(
                "Could not decode sheets JSON"
            ) from exc

        return self._sheets

    # =========================================================
    # TEXT NORMALIZATION
    # =========================================================

    def normalize(self, value):

        if value is None:
            return ""

        text = str(value)

        replacements = {
            "\u200c": "",
            "\u200e": "",
            "\u200f": "",
            "‌": "",

            "ي": "ی",
            "ى": "ی",
            "ك": "ک",
            "ة": "ه",
            "ۀ": "ه",
            "ؤ": "و",

            "إ": "ا",
            "أ": "ا",
            "آ": "ا",

            "٪": "%",

            "٠": "0",
            "١": "1",
            "٢": "2",
            "٣": "3",
            "٤": "4",
            "٥": "5",
            "٦": "6",
            "٧": "7",
            "٨": "8",
            "٩": "9",

            "۰": "0",
            "۱": "1",
            "۲": "2",
            "۳": "3",
            "۴": "4",
            "۵": "5",
            "۶": "6",
            "۷": "7",
            "۸": "8",
            "۹": "9",

            "ÙŠ": "ی",
            "Ù‰": "ی",
            "Ùƒ": "ک",

            "â€Œ": "",

            "Ã™Å ": "ی",
            "Ã™Æ’": "ک"
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    # =========================================================
    # NUMBER PARSER
    # =========================================================

    def parse_number(self, value):

        if value is None:
            return 0

        if isinstance(value, bool):
            return int(value)

        if isinstance(value, (int, float)):

            try:
                return int(value)

            except (ValueError, TypeError):
                return 0

        text = str(value).strip()

        if not text:
            return 0

        text = self.normalize(text)

        text = (
            text
            .replace(",", "")
            .replace("٬", "")
            .replace(" ", "")
            .replace("%", "")
        )

        negative = False

        if text.startswith("(") and text.endswith(")"):

            negative = True
            text = text[1:-1]

        if text.startswith("-"):

            negative = True
            text = text[1:]

        text = re.sub(
            r"[^0-9.]+",
            "",
            text
        )

        if not text:
            return 0

        try:

            number = int(float(text))

            if negative:
                number = -number

            return number

        except (ValueError, TypeError):
            return 0

    # =========================================================
    # SHEET FINDER
    # =========================================================

    def find_income_statement_sheet(self):

        sheets = self.extract_sheets()

        candidates = []

        for sheet in sheets:

            title = self.normalize(
                sheet.get(
                    "title_Fa",
                    ""
                )
            )

            if not title:
                continue

            normalized_title = title.replace(
                " ",
                ""
            )

            score = 0

            if (
                "صورتسودوزیان" in normalized_title
                or
                "صورتسودوزیانجامع" in normalized_title
            ):
                score += 100

            if (
                "درآمدهایعملیاتی" in normalized_title
                or
                "درآمدها" in normalized_title
            ):
                score += 20

            if (
                "سود" in normalized_title
                or
                "زیان" in normalized_title
            ):
                score += 20

            if score > 0:

                candidates.append(
                    (
                        score,
                        sheet
                    )
                )

        if not candidates:
            return None

        candidates.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return candidates[0][1]

    # =========================================================
    # CELL EXTRACTION
    # =========================================================

    def get_cells(self):

        if self._cells is not None:
            return self._cells

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

        cells = tables[0].get(
            "cells",
            []
        )

        if not cells:
            raise ValueError(
                "Income statement cells not found"
            )

        self._cells = cells

        return self._cells

    # =========================================================
    # ROW LABEL DETECTION
    # =========================================================

    def get_row_labels(self, cells):

        rows = {}

        for cell in cells:

            row_code = cell.get(
                "rowCode"
            )

            column_code = cell.get(
                "columnCode"
            )

            if row_code is None:
                continue

            if column_code != 1:
                continue

            title = self.normalize(
                cell.get(
                    "value",
                    ""
                )
            )

            if not title:
                continue

            rows[row_code] = title

        return rows

    # =========================================================
    # DEBUG ROWS
    # =========================================================

    def debug_rows(self, cells):

        print()
        print("==============================")
        print("DEBUG PROFIT LOSS ROWS")
        print("==============================")

        rows = self.get_row_labels(cells)

        for row_code, title in rows.items():

            print(
                "ROW:",
                row_code,
                "| TITLE:",
                title
            )

        print("==============================")
        print()

    # =========================================================
    # HEADER DETECTION
    # =========================================================

    def _is_change_header(self, text):

        normalized = self.normalize(text)

        compact = normalized.replace(
            " ",
            ""
        )

        return (
            "درصدتغییر" in compact
            or
            "تغییردرصدی" in compact
            or
            "درصدتغییرات" in compact
        )

    def _is_current_header(self, text):

        normalized = self.normalize(text)

        compact = normalized.replace(
            " ",
            ""
        )

        if "تجدیدارائه" in compact:
            return False

        if "دورهمنتهیبه" in compact:
            return True

        return False

    def _is_restatement_header(self, text):

        normalized = self.normalize(text)

        compact = normalized.replace(
            " ",
            ""
        )

        return (
            "تجدیدارائهشده" in compact
            or
            "تجدیدارائه" in compact
        )

    # =========================================================
    # DATE EXTRACTION
    # =========================================================

    def _extract_date_from_header(self, text):

        if text is None:
            return None

        normalized = self.normalize(text)

        normalized = re.sub(
            r"\s+",
            "",
            normalized
        )

        match = re.search(
            r"(1[34]\d{2})[\/\-](\d{1,2})[\/\-](\d{1,2})",
            normalized
        )

        if not match:
            return None

        return (
            int(match.group(1)),
            int(match.group(2)),
            int(match.group(3))
        )

    # =========================================================
    # HEADER TEXTS
    # =========================================================

    def _find_header_texts(self, cells):

        header_values = {}

        for cell in cells:

            column_code = cell.get(
                "columnCode"
            )

            if column_code is None:
                continue

            value = cell.get(
                "value"
            )

            if value is None:
                continue

            text = self.normalize(value)

            if not text:
                continue

            has_date = (
                self._extract_date_from_header(text)
                is not None
            )

            is_change = (
                self._is_change_header(text)
            )

            is_current = (
                self._is_current_header(text)
            )

            is_restatement = (
                self._is_restatement_header(text)
            )

            if not (
                has_date
                or
                is_change
                or
                is_current
                or
                is_restatement
            ):
                continue

            if column_code not in header_values:
                header_values[column_code] = []

            header_values[column_code].append(
                text
            )

        return header_values

    # =========================================================
    # PERIOD MONTH CALCULATION
    # =========================================================

    def calculate_period_months(self, date):

        if not date:
            return None

        year, month, day = date

        if month <= 3:
            return 3

        if month <= 6:
            return 6

        if month <= 9:
            return 9

        return 12

    # =========================================================
    # COLUMN MAPPING
    # =========================================================

    def detect_column_mapping(self, cells):

        if self._column_mapping is not None:
            return self._column_mapping

        header_values = self._find_header_texts(
            cells
        )

        mapping = {}

        current_candidates = []
        restated_candidates = []
        change_columns = []

        for column_code, values in header_values.items():

            joined = " | ".join(values)

            role = "unknown"
            header_type = "unknown"

            date = None

            for value in values:

                extracted_date = (
                    self._extract_date_from_header(
                        value
                    )
                )

                if extracted_date is not None:

                    date = extracted_date
                    break

            if self._is_change_header(joined):

                role = "change"
                header_type = "percentage_change"

                change_columns.append(
                    column_code
                )

            elif self._is_current_header(joined):

                role = "current"
                header_type = "current_period"

                if date:

                    current_candidates.append(
                        {
                            "column_code": column_code,
                            "date": date
                        }
                    )

            elif self._is_restatement_header(joined):

                role = "restated"
                header_type = "restated_period"

                if date:

                    restated_candidates.append(
                        {
                            "column_code": column_code,
                            "date": date
                        }
                    )

            elif date:

                role = "unknown"
                header_type = "date_period"

            mapping[column_code] = {
                "column_code": column_code,
                "role": role,
                "header_type": header_type,
                "headers": values,
                "joined_header": joined,
                "date": date
            }

        # =====================================================
        # CURRENT PERIOD
        # =====================================================

        current_date = None
        current_column = None

        if current_candidates:

            current_candidates.sort(
                key=lambda item: item["date"]
            )

            selected_current = (
                current_candidates[-1]
            )

            current_column = (
                selected_current["column_code"]
            )

            current_date = (
                selected_current["date"]
            )

            self._current_date = current_date

            self._period_months = (
                self.calculate_period_months(
                    current_date
                )
            )

            mapping[current_column][
                "role"
            ] = "current"

            mapping[current_column][
                "header_type"
            ] = "current_period"

        # =====================================================
        # RESTATED CLASSIFICATION
        # =====================================================

        if current_date:

            current_year = current_date[0]
            current_month = current_date[1]

            comparable_candidates = []
            annual_candidates = []

            for item in restated_candidates:

                column_code = item[
                    "column_code"
                ]

                date = item[
                    "date"
                ]

                year = date[0]
                month = date[1]

                if (
                    year == current_year - 1
                    and
                    month == current_month
                ):

                    comparable_candidates.append(
                        item
                    )

                    mapping[column_code][
                        "role"
                    ] = "previous"

                    mapping[column_code][
                        "header_type"
                    ] = "previous_comparable"

                elif (
                    year == current_year - 1
                    and
                    month >= 10
                ):

                    annual_candidates.append(
                        item
                    )

                    mapping[column_code][
                        "role"
                    ] = "annual"

                    mapping[column_code][
                        "header_type"
                    ] = "annual_previous_full_year"

                else:

                    mapping[column_code][
                        "role"
                    ] = "restated"

                    mapping[column_code][
                        "header_type"
                    ] = "restated_period"

            # =================================================
            # PREVIOUS COMPARABLE
            # =================================================

            if comparable_candidates:

                comparable_candidates.sort(
                    key=lambda item: item["date"]
                )

                selected_previous = (
                    comparable_candidates[-1]
                )

                previous_column = (
                    selected_previous[
                        "column_code"
                    ]
                )

                self._previous_comparable_date = (
                    selected_previous[
                        "date"
                    ]
                )

                mapping[previous_column][
                    "role"
                ] = "previous"

                mapping[previous_column][
                    "header_type"
                ] = "previous_comparable"

            # =================================================
            # ANNUAL PREVIOUS
            # =================================================

            if annual_candidates:

                annual_candidates.sort(
                    key=lambda item: item["date"]
                )

                selected_annual = (
                    annual_candidates[-1]
                )

                annual_column = (
                    selected_annual[
                        "column_code"
                    ]
                )

                self._annual_previous_date = (
                    selected_annual[
                        "date"
                    ]
                )

                mapping[annual_column][
                    "role"
                ] = "annual"

                mapping[annual_column][
                    "header_type"
                ] = "annual_previous_full_year"

        # =====================================================
        # CHANGE COLUMNS
        # =====================================================

        for column_code in change_columns:

            mapping[column_code][
                "role"
            ] = "change"

            mapping[column_code][
                "header_type"
            ] = "percentage_change"

        self._column_mapping = mapping

        return mapping

    # =========================================================
    # DEBUG COLUMN MAPPING
    # =========================================================

    def debug_column_mapping(self, cells):

        mapping = self.detect_column_mapping(
            cells
        )

        print()
        print("DEBUG COLUMN MAPPING")
        print("---------------------")

        for column_code in sorted(
            mapping.keys()
        ):

            item = mapping[column_code]

            print(
                "COLUMN:",
                column_code,
                "| ROLE:",
                item.get("role"),
                "| TYPE:",
                item.get("header_type"),
                "| DATE:",
                item.get("date"),
                "| HEADERS:",
                item.get("headers")
            )

        print("---------------------")
        print()

        print(
            "CURRENT DATE:",
            self._current_date
        )

        print(
            "PREVIOUS COMPARABLE DATE:",
            self._previous_comparable_date
        )

        print(
            "ANNUAL PREVIOUS DATE:",
            self._annual_previous_date
        )

        print(
            "DETECTED PERIOD MONTHS:",
            self._period_months
        )

        print()

    # =========================================================
    # ROW FINDER
    # =========================================================

    def find_row(self, cells, keywords):

        normalized_keywords = [
            self.normalize(keyword)
            for keyword in keywords
        ]

        normalized_keywords = [
            keyword.replace(" ", "")
            for keyword in normalized_keywords
            if keyword
        ]

        best_match = None
        best_score = -1

        for cell in cells:

            if cell.get("columnCode") != 1:
                continue

            title = self.normalize(
                cell.get(
                    "value",
                    ""
                )
            )

            if not title:
                continue

            compact_title = title.replace(
                " ",
                ""
            )

            for keyword in normalized_keywords:

                if not keyword:
                    continue

                compact_keyword = keyword.replace(
                    " ",
                    ""
                )

                if (
                    compact_title
                    ==
                    compact_keyword
                ):

                    return cell.get(
                        "rowCode"
                    )

                if (
                    compact_keyword
                    in
                    compact_title
                ):

                    score = len(
                        compact_keyword
                    )

                    if score > best_score:

                        best_score = score

                        best_match = cell.get(
                            "rowCode"
                        )

        return best_match

    # =========================================================
    # ROW VALUE EXTRACTION
    # =========================================================

    def get_row_values(
        self,
        cells,
        row_code,
        debug=True
    ):

        result = []

        for cell in cells:

            if (
                cell.get("rowCode")
                !=
                row_code
            ):
                continue

            column_code = cell.get(
                "columnCode"
            )

            value = cell.get(
                "value"
            )

            result.append(
                {
                    "address": cell.get(
                        "address"
                    ),
                    "columnCode": column_code,
                    "value": self.parse_number(
                        value
                    )
                }
            )

        if debug:

            print()
            print(
                "DEBUG ROW VALUE",
                row_code
            )

            for item in result:
                print(item)

            print()

        return result

    # =========================================================
    # CONCEPT EXTRACTION
    # =========================================================

    def extract_concept(
        self,
        cells,
        keywords
    ):

        row = self.find_row(
            cells,
            keywords
        )

        if row is None:

            return {
                "row_code": None,
                "values": [],
                "semantic": {}
            }

        values = self.get_row_values(
            cells,
            row,
            debug=False
        )

        semantic = self.map_row_semantically(
            values
        )

        return {
            "row_code": row,
            "values": values,
            "semantic": semantic
        }

    # =========================================================
    # SEMANTIC ROW MAPPING
    # =========================================================

    def map_row_semantically(self, values):

        mapping = self.detect_column_mapping(
            self._cells
        )

        semantic = {
            "current": 0,
            "previous": 0,
            "annual": 0,
            "change": 0
        }

        for item in values:

            column_code = item.get(
                "columnCode"
            )

            value = item.get(
                "value",
                0
            )

            column_info = mapping.get(
                column_code
            )

            if not column_info:
                continue

            role = column_info.get(
                "role"
            )

            if role == "current":

                semantic[
                    "current"
                ] = value

            elif role == "previous":

                semantic[
                    "previous"
                ] = value

            elif role == "annual":

                semantic[
                    "annual"
                ] = value

            elif role == "change":

                semantic[
                    "change"
                ] = value

        # =====================================================
        # ANNUAL FALLBACK
        # =====================================================

        has_real_annual = any(
            column_info.get("role")
            == "annual"
            for column_info in mapping.values()
        )

        if (
            not has_real_annual
            and
            semantic["annual"] == 0
            and
            semantic["current"] != 0
            and
            semantic["previous"] == 0
        ):

            semantic[
                "annual"
            ] = semantic[
                "current"
            ]

        return semantic

    # =========================================================
    # FINANCIAL DATA
    # =========================================================

    def get_financial_data(self):

        cells = self.get_cells()

        self.debug_rows(
            cells
        )

        self.debug_column_mapping(
            cells
        )

        # =====================================================
        # SALES
        # =====================================================

        sales = self.extract_concept(
            cells,
            [
                "درآمدهای عملیاتی",
                "درآمدهای عملياتي",
                "فروش",
                "درآمد عملیاتی"
            ]
        )

        # =====================================================
        # GROSS PROFIT
        # =====================================================

        gross_profit = self.extract_concept(
            cells,
            [
                "سود ناخالص",
                "سود(زیان) ناخالص",
                "سود (زیان) ناخالص"
            ]
        )

        # =====================================================
        # OPERATING PROFIT
        # =====================================================

        operating_profit = self.extract_concept(
            cells,
            [
                "سود عملیاتی",
                "سود(زیان) عملیاتی",
                "سود (زیان) عملیاتی",
                "سود(زیان) عملياتى"
            ]
        )

        # =====================================================
        # NON OPERATING INCOME
        # =====================================================

        non_operating_income = self.extract_concept(
            cells,
            [
                "سایر درآمدها و هزینه های غیرعملیاتی",
                "سایر درآمدها و هزینه های غیر عملیاتی",
                "درآمدها و هزینه های غیرعملیاتی",
                "غیرعملیاتی",
                "غیر عملیاتی"
            ]
        )

        # =====================================================
        # NET PROFIT
        # =====================================================

        net_profit = self.extract_concept(
            cells,
            [
                "سود خالص",
                "سود(زیان) خالص",
                "سود (زیان) خالص"
            ]
        )

        # =====================================================
        # RESULT
        # =====================================================

        result = {

            "sales":
                sales.get(
                    "values",
                    []
                ),

            "gross_profit":
                gross_profit.get(
                    "values",
                    []
                ),

            "operating_profit":
                operating_profit.get(
                    "values",
                    []
                ),

            "non_operating_income":
                non_operating_income.get(
                    "values",
                    []
                ),

            "net_profit":
                net_profit.get(
                    "values",
                    []
                ),

            "semantic": {

                "sales":
                    sales.get(
                        "semantic",
                        {}
                    ),

                "gross_profit":
                    gross_profit.get(
                        "semantic",
                        {}
                    ),

                "operating_profit":
                    operating_profit.get(
                        "semantic",
                        {}
                    ),

                "non_operating_income":
                    non_operating_income.get(
                        "semantic",
                        {}
                    ),

                "net_profit":
                    net_profit.get(
                        "semantic",
                        {}
                    )
            },

            "period_months":
                self._period_months
        }

        # =====================================================
        # DEBUG
        # =====================================================

        print()
        print(
            "DEBUG SEMANTIC FINANCIAL DATA"
        )

        print(
            "------------------------------"
        )

        for concept_name in [
            "sales",
            "gross_profit",
            "operating_profit",
            "non_operating_income",
            "net_profit"
        ]:

            concept = result[
                "semantic"
            ].get(
                concept_name,
                {}
            )

            print(
                concept_name + ":",
                concept.get(
                    "current",
                    0
                ),
                "| Previous Comparable:",
                concept.get(
                    "previous",
                    0
                ),
                "| Annual Previous Full Year:",
                concept.get(
                    "annual",
                    0
                ),
                "| Change:",
                concept.get(
                    "change",
                    0
                )
            )

        print()

        print(
            "Current Date:",
            self._current_date
        )

        print(
            "Previous Comparable Date:",
            self._previous_comparable_date
        )

        print(
            "Annual Previous Date:",
            self._annual_previous_date
        )

        print(
            "Period Months:",
            result[
                "period_months"
            ]
        )

        print(
            "------------------------------"
        )

        print()

        return result

    # =========================================================
    # PUBLIC PERIOD MONTHS
    # =========================================================

    def get_period_months(self):

        if self._period_months is not None:
            return self._period_months

        cells = self.get_cells()

        self.detect_column_mapping(
            cells
        )

        return self._period_months

    # =========================================================
    # PUBLIC COLUMN MAPPING
    # =========================================================

    def get_column_mapping(self):

        cells = self.get_cells()

        return self.detect_column_mapping(
            cells
        )