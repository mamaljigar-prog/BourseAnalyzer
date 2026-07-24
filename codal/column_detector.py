import re
from datetime import datetime


class ColumnDetector:

    """
    Detects financial report columns by their semantic meaning.

    IMPORTANT:
    This class must NOT assume that the current period is always
    column B, C, or any fixed Excel column.

    It tries to identify:
        - current period
        - previous comparable period
        - previous fiscal year
        - percentage / change columns

    The detector works with row metadata returned by Codal parsers.
    """

    def __init__(self, rows=None):

        self.rows = rows or []



    # ==========================================================
    # TEXT NORMALIZATION
    # ==========================================================

    def normalize(self, value):

        if value is None:
            return ""

        text = str(value)

        replacements = {

            "\u200c": "",
            "\u200e": "",
            "\u200f": "",
            "\u00a0": " ",

            "ي": "ی",
            "ى": "ی",
            "ك": "ک",

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
            "۹": "9"

        }

        for old, new in replacements.items():

            text = text.replace(
                old,
                new
            )

        return " ".join(
            text.split()
        ).strip()



    # ==========================================================
    # COLUMN LETTER / NUMBER
    # ==========================================================

    def column_number_to_letter(
        self,
        number
    ):

        try:

            number = int(number)

        except (
            ValueError,
            TypeError
        ):

            return None


        if number <= 0:

            return None


        result = ""


        while number > 0:

            number, remainder = divmod(

                number - 1,

                26

            )

            result = (

                chr(
                    65 + remainder
                )

                +

                result

            )


        return result



    def extract_column_number(
        self,
        row
    ):

        if not isinstance(
            row,
            dict
        ):

            return None


        # ----------------------------------
        # Direct column code
        # ----------------------------------

        if row.get(
            "columnCode"
        ) is not None:

            try:

                return int(
                    row.get(
                        "columnCode"
                    )
                )

            except (
                ValueError,
                TypeError
            ):

                pass


        # ----------------------------------
        # Address
        # Example: B4
        # ----------------------------------

        address = row.get(

            "address",

            ""

        )


        if address:

            match = re.match(

                r"^([A-Za-z]+)",

                str(
                    address
                )

            )


            if match:

                letters = (
                    match.group(
                        1
                    ).upper()
                )


                number = 0


                for char in letters:

                    number = (

                        number * 26

                        +

                        ord(
                            char
                        )

                        -

                        64

                    )


                return number


        return None



    # ==========================================================
    # EXTRACT TEXT
    # ==========================================================

    def extract_text(
        self,
        row
    ):

        if not isinstance(
            row,
            dict
        ):

            return ""


        possible_fields = [

            "title",
            "Title",
            "text",
            "Text",
            "name",
            "Name",
            "header",
            "Header",
            "label",
            "Label",
            "description",
            "Description",
            "value"

        ]


        for field in possible_fields:

            value = row.get(
                field
            )


            if value is not None:

                text = self.normalize(
                    value
                )


                if text:

                    return text


        return ""



    # ==========================================================
    # HEADER CLASSIFICATION
    # ==========================================================

    def classify_header(
        self,
        text
    ):

        text = self.normalize(
            text
        )


        if not text:

            return "unknown"


        # ----------------------------------
        # Current period
        # ----------------------------------

        current_keywords = [

            "دوره جاری",
            "دوره فعلی",
            "سال جاری",
            "سال مالی جاری",
            "جاری",
            "current period",
            "current"

        ]


        for keyword in current_keywords:

            if keyword in text:

                return "current"


        # ----------------------------------
        # Previous comparable period
        # ----------------------------------

        previous_keywords = [

            "دوره مشابه سال قبل",
            "دوره مشابه",
            "مشابه سال قبل",
            "مشابه دوره قبل",
            "دوره قبل",
            "سال قبل",
            "سال مالی قبل",
            "previous period",
            "previous"

        ]


        for keyword in previous_keywords:

            if keyword in text:

                return "previous_comparable"


        # ----------------------------------
        # Change / percentage
        # ----------------------------------

        change_keywords = [

            "درصد تغییر",
            "درصد رشد",
            "تغییرات",
            "رشد",
            "درصد",

            "%",

            "change",
            "growth"

        ]


        for keyword in change_keywords:

            if keyword in text:

                return "change"


        # ----------------------------------
        # Fiscal year
        # ----------------------------------

        fiscal_keywords = [

            "سال مالی",
            "سال مالی قبل",
            "سال گذشته",
            "fiscal year"

        ]


        for keyword in fiscal_keywords:

            if keyword in text:

                return "fiscal_year"


        return "unknown"



    # ==========================================================
    # DATE DETECTION
    # ==========================================================

    def extract_date(
        self,
        text
    ):

        text = self.normalize(
            text
        )


        if not text:

            return None


        patterns = [

            r"(14\d{2})[\/\-](\d{1,2})[\/\-](\d{1,2})",

            r"(14\d{2})(\d{2})(\d{2})"

        ]


        for pattern in patterns:

            matches = re.findall(

                pattern,

                text

            )


            if not matches:

                continue


            for match in matches:

                try:

                    year = int(
                        match[0]
                    )

                    month = int(
                        match[1]
                    )

                    day = int(
                        match[2]
                    )


                    if (

                        1300 <= year <= 1500

                        and

                        1 <= month <= 12

                        and

                        1 <= day <= 31

                    ):

                        return (

                            year,

                            month,

                            day

                        )

                except:

                    continue


        return None



    # ==========================================================
    # FIND HEADER ROWS
    # ==========================================================

    def find_header_rows(
        self
    ):

        result = []


        for row in self.rows:

            text = self.extract_text(
                row
            )


            if not text:

                continue


            category = self.classify_header(
                text
            )


            date = self.extract_date(
                text
            )


            if (

                category != "unknown"

                or

                date is not None

            ):

                result.append({

                    "row":
                        row,

                    "text":
                        text,

                    "category":
                        category,

                    "date":
                        date,

                    "column":
                        self.extract_column_number(
                            row
                        )

                })


        return result



    # ==========================================================
    # DETECT COLUMNS
    # ==========================================================

    def detect(
        self
    ):

        headers = self.find_header_rows()


        result = {

            "current": None,

            "previous_comparable": None,

            "previous_fiscal_year": None,

            "change": None,

            "columns": {},

            "confidence": "low",

            "method": None

        }


        # ======================================================
        # METHOD 1
        # Explicit semantic header
        # ======================================================

        for item in headers:

            column = item.get(
                "column"
            )


            if not column:

                continue


            category = item.get(
                "category"
            )


            if category == "current":

                result["current"] = column

                result["columns"][

                    column

                ] = "current"


            elif category == "previous_comparable":

                result["previous_comparable"] = column

                result["columns"][

                    column

                ] = "previous_comparable"


            elif category == "change":

                result["change"] = column

                result["columns"][

                    column

                ] = "change"


        if (

            result["current"] is not None

            or

            result["previous_comparable"] is not None

        ):

            result["confidence"] = "high"

            result["method"] = (

                "semantic_header"

            )

            return result



        # ======================================================
        # METHOD 2
        # Date-based detection
        # ======================================================

        dated_columns = []


        for item in headers:

            column = item.get(
                "column"
            )


            date = item.get(
                "date"
            )


            if (

                column is not None

                and

                date is not None

            ):

                dated_columns.append({

                    "column":
                        column,

                    "date":
                        date

                })


        if dated_columns:

            dated_columns.sort(

                key=lambda x:

                x["date"],

                reverse=True

            )


            result["current"] = (

                dated_columns[0][

                    "column"

                ]

            )


            result["columns"][

                dated_columns[0]["column"]

            ] = "current"


            if len(
                dated_columns
            ) > 1:

                result["previous_comparable"] = (

                    dated_columns[1][

                        "column"

                    ]

                )


                result["columns"][

                    dated_columns[1]["column"]

                ] = "previous_comparable"


            result["confidence"] = "medium"

            result["method"] = (

                "date_order"

            )

            return result



        # ======================================================
        # METHOD 3
        # No safe inference
        # ======================================================

        result["confidence"] = "low"

        result["method"] = (

            "undetermined"

        )


        return result



    # ==========================================================
    # CONVENIENCE METHODS
    # ==========================================================

    def current_column(
        self
    ):

        return self.detect().get(
            "current"
        )



    def previous_column(
        self
    ):

        return self.detect().get(

            "previous_comparable"

        )



    def is_reliable(
        self
    ):

        result = self.detect()


        return (

            result.get(
                "current"
            ) is not None

            and

            result.get(
                "confidence"
            )

            in [

                "high",

                "medium"

            ]

        )