from datetime import datetime
import re


class ReportSelector:

    def __init__(
        self,
        financial_reports,
        monthly_reports
    ):

        self.financial_reports = (
            financial_reports or []
        )

        self.monthly_reports = (
            monthly_reports or []
        )

    # =========================
    # Text Normalization
    # =========================

    def normalize(self, text):

        if not text:

            return ""

        text = str(text)

        replacements = {

            "ÙŠ": "ی",
            "Ù‰": "ی",
            "Ùƒ": "ک",
            "ÛŒ": "ی",
            "Ú©": "ک",

            "\u200c": "",
            "\u200e": "",
            "\u200f": ""

        }

        for a, b in replacements.items():

            text = text.replace(
                a,
                b
            )

        return text

    # =========================
    # Digit Normalization
    # =========================

    def normalize_digits(self, text):

        if not text:

            return ""

        text = str(text)

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

        for a, b in replacements.items():

            text = text.replace(
                a,
                b
            )

        return text

    # =========================
    # Extract Date
    # =========================

    def extract_date(
        self,
        title
    ):

        title = self.normalize_digits(
            title
        )

        matches = re.findall(

            r'14\d{2}/\d{1,2}/\d{1,2}',

            title

        )

        if not matches:

            return datetime.min

        try:

            y, m, d = (
                matches[-1]
                .split("/")
            )

            return datetime(

                int(y),

                int(m),

                int(d)

            )

        except Exception:

            return datetime.min

    # =========================
    # Extract Persian Date
    # =========================

    def extract_persian_date(
        self,
        title
    ):

        title = self.normalize_digits(
            title
        )

        matches = re.findall(

            r'(14\d{2})/(\d{1,2})/(\d{1,2})',

            title

        )

        if not matches:

            return None

        try:

            year, month, day = (
                matches[-1]
            )

            return {

                "year":
                    int(year),

                "month":
                    int(month),

                "day":
                    int(day)

            }

        except Exception:

            return None

    # =========================
    # Extract Period Months
    # =========================

    def extract_period_months(
        self,
        report
    ):

        if not report:

            return None

        title = self.normalize(

            report.get(

                "title",

                ""

            )

        )

        title = self.normalize_digits(
            title
        )

        # 3 ماهه

        if (

            "دوره 3 ماهه" in title

            or

            "دوره ۳ ماهه" in title

        ):

            return 3

        # 6 ماهه

        if (

            "دوره 6 ماهه" in title

            or

            "دوره ۶ ماهه" in title

        ):

            return 6

        # 9 ماهه

        if (

            "دوره 9 ماهه" in title

            or

            "دوره ۹ ماهه" in title

        ):

            return 9

        # Annual

        if (

            "سال مالی" in title

            or

            "سالمالی" in title

        ):

            return 12

        return None

    # =========================
    # Annual Report
    # =========================

    def is_annual(
        self,
        report
    ):

        title = self.normalize(

            report.get(

                "title",

                ""

            )

        )

        return (

            "سال مالی" in title

            or

            "سالمالی" in title

        )

    # =========================
    # Interim Report
    # =========================

    def is_interim(
        self,
        report
    ):

        title = self.normalize(

            report.get(

                "title",

                ""

            )

        )

        normalized = self.normalize_digits(
            title
        )

        return (

            "میاندوره" in normalized

            or

            "میان دوره" in normalized

            or

            "دوره 3 ماهه" in normalized

            or

            "دوره 6 ماهه" in normalized

            or

            "دوره 9 ماهه" in normalized

        )

    # =========================
    # Audited
    # =========================

    def is_audited(
        self,
        report
    ):

        title = self.normalize(

            report.get(

                "title",

                ""

            )

        )

        return (

            "حسابرسی شده" in title

            and

            "حسابرسی نشده" not in title

        )

    # =========================
    # Report Year
    # =========================

    def report_year(
        self,
        report
    ):

        date = self.extract_persian_date(

            report.get(

                "title",

                ""

            )

        )

        if not date:

            return None

        return date["year"]

    # =========================
    # Latest Annual
    # =========================

    def latest_annual(
        self
    ):

        annuals = [

            r

            for r in self.financial_reports

            if self.is_annual(r)

        ]

        if not annuals:

            return None

        return sorted(

            annuals,

            key=lambda r: (

                self.extract_date(

                    r.get(

                        "title",

                        ""

                    )

                ),

                self.is_audited(r)

            ),

            reverse=True

        )[0]

    # =========================
    # Latest Interim
    # =========================

    def latest_interim(
        self
    ):

        interims = [

            r

            for r in self.financial_reports

            if self.is_interim(r)

        ]

        if not interims:

            return None

        return sorted(

            interims,

            key=lambda r:

            self.extract_date(

                r.get(

                    "title",

                    ""

                )

            ),

            reverse=True

        )[0]

    # =========================
    # Latest Financial
    # =========================

    def latest_financial(
        self
    ):

        # مهم:
        # جدیدترین گزارش معتبر مالی را انتخاب می‌کنیم.
        #
        # بنابراین اگر جدیدترین گزارش 3M باشد،
        # همان 3M انتخاب می‌شود.
        #
        # اگر 6M باشد، 6M انتخاب می‌شود.
        #
        # اگر 9M باشد، 9M انتخاب می‌شود.
        #
        # گزارش سالانه فقط زمانی انتخاب می‌شود
        # که جدیدترین گزارش مالی سالانه باشد.

        if not self.financial_reports:

            return None

        valid_reports = [

            r

            for r in self.financial_reports

            if self.is_annual(r)
            or
            self.is_interim(r)

        ]

        if not valid_reports:

            return None

        return sorted(

            valid_reports,

            key=lambda r:

            self.extract_date(

                r.get(

                    "title",

                    ""

                )

            ),

            reverse=True

        )[0]

    # =========================
    # Latest Complete Financial
    # =========================

    def latest_complete_financial(
        self
    ):

        return self.latest_financial()

    # =========================
    # Find Comparable Period
    # =========================

    def find_comparable_period(
        self,
        current_report
    ):

        if not current_report:

            return None

        current_date = (
            self.extract_persian_date(

                current_report.get(

                    "title",

                    ""

                )

            )
        )

        if not current_date:

            return None

        current_year = (
            current_date["year"]
        )

        current_month = (
            current_date["month"]
        )

        current_period_months = (

            self.extract_period_months(

                current_report

            )

        )

        if current_period_months is None:

            return None

        target_year = (

            current_year - 1

        )

        candidates = []

        for report in self.financial_reports:

            if report is current_report:

                continue

            report_date = (
                self.extract_persian_date(

                    report.get(

                        "title",

                        ""

                    )

                )
            )

            if not report_date:

                continue

            if (

                report_date["year"]

                !=

                target_year

            ):

                continue

            report_period_months = (

                self.extract_period_months(

                    report

                )

            )

            if (

                report_period_months

                !=

                current_period_months

            ):

                continue

            # ماه پایان دوره نیز باید یکسان باشد.

            if (

                report_date["month"]

                !=

                current_month

            ):

                continue

            candidates.append(
                report
            )

        if not candidates:

            return None

        # اگر چند گزارش برای یک دوره وجود داشت،
        # گزارش حسابرسی‌شده اولویت دارد.

        return sorted(

            candidates,

            key=lambda r: (

                self.is_audited(r),

                self.extract_date(

                    r.get(

                        "title",

                        ""

                    )

                )

            ),

            reverse=True

        )[0]

    # =========================
    # Latest Monthly
    # =========================

    def latest_monthly(
        self
    ):

        if not self.monthly_reports:

            return None

        return sorted(

            self.monthly_reports,

            key=lambda r:

            self.extract_date(

                r.get(

                    "title",

                    ""

                )

            ),

            reverse=True

        )[0]