import re


class ReportPeriodDetector:

    def __init__(self, title=""):
        self.title = self.normalize(title)

    def normalize(self, text):

        if not text:
            return ""

        text = str(text)

        replacements = {
            "ÙŠ": "ی",
            "Ù‰": "ی",
            "Ùƒ": "ک",
            "\u200c": "",
            "\u200e": "",
            "\u200f": "",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

    def normalize_digits(self, text):

        if not text:
            return ""

        replacements = {
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
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

    def extract_dates(self, text):

        text = self.normalize_digits(text)

        return re.findall(
            r"140\d\s*/\s*(\d{1,2})\s*/\s*(\d{1,2})",
            text
        )

    def detect_fiscal_year_end(self):

        title = self.normalize_digits(self.title)

        patterns = [
            r"سال\s*مالی\s*منتهی\s*به\s*140\d/\d{1,2}/\d{1,2}",
            r"سال\s*مالی\s*منتهی\s*به",
            r"دوره\s*مالی\s*منتهی\s*به",
        ]

        for pattern in patterns:

            if re.search(pattern, title):

                dates = self.extract_dates(title)

                if dates:

                    month = int(dates[-1][0])

                    return month

        return None

    def detect(self):

        title = self.normalize_digits(self.title)

        # -------------------------
        # explicit period
        # -------------------------

        explicit_patterns = [

            (
                [
                    r"9\s*ماهه",
                    r"نه\s*ماهه",
                    r"دوره\s*9\s*ماهه",
                    r"صورت\s*مالی\s*9\s*ماهه",
                    r"میاندوره\s*9\s*ماهه",
                ],
                9,
                "9M",
                "9_month"
            ),

            (
                [
                    r"6\s*ماهه",
                    r"شش\s*ماهه",
                    r"دوره\s*6\s*ماهه",
                ],
                6,
                "6M",
                "6_month"
            ),

            (
                [
                    r"3\s*ماهه",
                    r"سه\s*ماهه",
                    r"دوره\s*3\s*ماهه",
                ],
                3,
                "3M",
                "3_month"
            ),

            (
                [
                    r"سال\s*مالی",
                    r"سالانه",
                    r"صورت\s*مالی\s*سالانه",
                ],
                12,
                "12M",
                "annual"
            )

        ]


        for patterns, months, label, period in explicit_patterns:

            for pattern in patterns:

                if re.search(pattern, title):

                    return {
                        "months": months,
                        "label": label,
                        "period": period,
                        "title": self.title
                    }


        # -------------------------
        # fiscal year based detection
        # -------------------------

        fiscal_end = self.detect_fiscal_year_end()

        dates = self.extract_dates(title)

        if dates:

            report_month = int(
                dates[-1][0]
            )


            if fiscal_end:

                # پایان سال مالی شرکت
                # مثلا پایان شهریور = ماه 6
                #
                # فاصله گزارش تا پایان سال مالی
                # برای تعیین دوره استفاده می‌شود

                diff = fiscal_end - report_month

                if diff < 0:
                    diff += 12


                period_months = 12 - diff


                if period_months in [3, 6, 9, 12]:

                    labels = {
                        3: ("3M", "3_month"),
                        6: ("6M", "6_month"),
                        9: ("9M", "9_month"),
                        12: ("12M", "annual"),
                    }

                    label, period = labels[period_months]

                    return {
                        "months": period_months,
                        "label": label,
                        "period": period,
                        "fiscal_year_end": fiscal_end,
                        "title": self.title
                    }


            # fallback calendar

            if report_month == 3:

                return {
                    "months": 3,
                    "label": "3M",
                    "period": "3_month",
                    "title": self.title
                }

            if report_month == 6:

                return {
                    "months": 6,
                    "label": "6M",
                    "period": "6_month",
                    "title": self.title
                }

            if report_month == 9:

                return {
                    "months": 9,
                    "label": "9M",
                    "period": "9_month",
                    "title": self.title
                }

            if report_month == 12:

                return {
                    "months": 12,
                    "label": "12M",
                    "period": "annual",
                    "title": self.title
                }


        return {
            "months": 12,
            "label": "12M",
            "period": "annual",
            "title": self.title
        }