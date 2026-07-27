import requests


class CodalAdapter:

    def __init__(self, symbol):

        self.symbol = symbol

        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json, text/plain, */*"
        }

        self._search_reports_cache = None


    # =========================
    # Search Codal Reports
    # =========================

    def search_reports(self):

        if self._search_reports_cache is not None:

            return self._search_reports_cache


        url = (
            "https://search.codal.ir/api/search/v2/q"
        )


        params = {

            "Symbol":
                self.symbol,

            "PageNumber":
                1,

            "PageSize":
                200,

            "Category":
                1

        }


        response = requests.get(

            url,

            params=params,

            headers=self.headers,

            timeout=30

        )


        response.raise_for_status()


        data = response.json()


        if not isinstance(data, dict):

            raise ValueError(
                "Invalid Codal search response"
            )


        self._search_reports_cache = data


        return data


    # =========================
    # Normalize Persian Text
    # =========================

    def normalize(self, text):

        if text is None:

            return ""


        text = str(text)


        replacements = {

            "ي": "ی",
            "ى": "ی",
            "ك": "ک",
            "ۀ": "ه",
            "ة": "ه",
            "ؤ": "و",
            "إ": "ا",
            "أ": "ا",
            "آ": "ا",

            "\u200c": "",
            "\u200e": "",
            "\u200f": "",
            "\ufeff": "",

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
            "٩": "9"

        }


        for old, new in replacements.items():

            text = text.replace(
                old,
                new
            )


        text = (

            text

            .replace(
                "\u00a0",
                " "
            )

            .replace(
                "\t",
                " "
            )

        )


        text = " ".join(
            text.split()
        )


        return text.strip()


    # =========================
    # Compact Text
    # =========================

    def compact(self, text):

        text = self.normalize(
            text
        )


        return (

            text

            .replace(
                " ",
                ""
            )

            .replace(
                "-",
                ""
            )

            .replace(
                "_",
                ""
            )

        )


    # =========================
    # Get Letters
    # =========================

    def get_letters(self):

        data = self.search_reports()


        letters = data.get(
            "Letters",
            []
        )


        if not isinstance(
            letters,
            list
        ):

            return []


        return letters


    # =========================
    # Is Annual Financial Report
    # =========================

    def is_annual_financial_report(
        self,
        title
    ):

        normalized = self.normalize(
            title
        )


        compact = self.compact(
            title
        )


        # Standard form

        if (

            "صورتهای مالی" in normalized

            and

            "سال مالی" in normalized

        ):

            return True


        # With normal space

        if (

            "صورت های مالی" in normalized

            and

            "سال مالی" in normalized

        ):

            return True


        # Compact fallback

        if (

            "صورتهای مالی" in compact

            and

            "سالمالی" in compact

        ):

            return True


        return False


    # =========================
    # Is Interim Financial Report
    # =========================

    def is_interim_financial_report(
        self,
        title
    ):

        normalized = self.normalize(
            title
        )


        compact = self.compact(
            title
        )


        has_financial_statement = (

            "صورتهای مالی" in normalized

            or

            "صورت های مالی" in normalized

            or

            "اطلاعات و صورت" in normalized

            or

            "صورتهای مالی" in compact

        )


        has_interim_period = (

            "میاندورهای" in normalized

            or

            "میان دوره ای" in normalized

            or

            "میان‌دوره‌ای" in normalized

            or

            "میاندوره" in normalized

            or

            "میاندورهای" in compact

            or

            "میاندوره" in compact

        )


        return (

            has_financial_statement

            and

            has_interim_period

        )


    # =========================
    # Is Financial Report
    # =========================

    def is_financial_report(
        self,
        title
    ):

        return (

            self.is_annual_financial_report(
                title
            )

            or

            self.is_interim_financial_report(
                title
            )

        )


    # =========================
    # Is Monthly Report
    # =========================

    def is_monthly_report(
        self,
        title
    ):

        normalized = self.normalize(
            title
        )


        compact = self.compact(
            title
        )


        if (

            "گزارش فعالیت ماهانه" in normalized

            or

            "گزارش فعالیت ماهیانه" in normalized

        ):

            return True


        if (

            "گزارشفعالیتماهانه" in compact

            or

            "گزارشفعالیتماهیانه" in compact

        ):

            return True


        return False


    # =========================
    # Find Financial Reports
    # =========================

    def find_financial_reports(self):

        reports = self.get_letters()


        result = []


        for report in reports:

            title = self.normalize(

                report.get(
                    "Title",
                    ""
                )

            )


            if self.is_financial_report(
                title
            ):

                result.append({

                    "type":
                        "financial",

                    "title":
                        title,

                    "url":
                        report.get(
                            "Url"
                        ),

                    "raw":
                        report

                })


        return result


    # =========================
    # Find Monthly Reports
    # =========================

    def find_monthly_reports(self):

        reports = self.get_letters()


        result = []


        for report in reports:

            title = self.normalize(

                report.get(
                    "Title",
                    ""
                )

            )


            if self.is_monthly_report(
                title
            ):

                result.append({

                    "type":
                        "monthly",

                    "title":
                        title,

                    "url":
                        report.get(
                            "Url"
                        ),

                    "raw":
                        report

                })


        return result


    # =========================
    # Debug Titles
    # =========================

    def debug_titles(self):

        reports = self.get_letters()


        result = []


        for index, report in enumerate(
            reports
        ):

            title = report.get(
                "Title",
                ""
            )


            result.append({

                "index":
                    index,

                "title":
                    title,

                "normalized":
                    self.normalize(
                        title
                    ),

                "annual":
                    self.is_annual_financial_report(
                        title
                    ),

                "interim":
                    self.is_interim_financial_report(
                        title
                    ),

                "financial":
                    self.is_financial_report(
                        title
                    ),

                "monthly":
                    self.is_monthly_report(
                        title
                    )

            })


        return result