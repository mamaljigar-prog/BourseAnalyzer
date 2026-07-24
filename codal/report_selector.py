from datetime import datetime
import re


class ReportSelector:

    def __init__(
        self,
        financial_reports,
        monthly_reports
    ):
        self.financial_reports = financial_reports or []
        self.monthly_reports = monthly_reports or []


    def normalize(self, text):

        if not text:
            return ""

        text = str(text)

        replacements = {
            "ÙŠ": "ی",
            "Ù‰": "ی",
            "Ùƒ": "ک",
            "ي": "ی",
            "ى": "ی",
            "ك": "ک",
            "\u200c": "",
            "\u200e": "",
            "\u200f": ""
        }

        for a, b in replacements.items():
            text = text.replace(a, b)

        return text.strip()



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
            "۹": "9"
        }

        for a, b in replacements.items():
            text = text.replace(a, b)

        return text



    def extract_date(self, title):

        title = self.normalize_digits(
            self.normalize(title)
        )

        matches = re.findall(
            r'140\d/\d{1,2}/\d{1,2}',
            title
        )

        if not matches:
            return datetime.min


        try:

            y, m, d = matches[-1].split("/")

            return datetime(
                int(y),
                int(m),
                int(d)
            )

        except Exception:

            return datetime.min



    def is_valid_financial_report(self, report):

        title = self.normalize(
            report.get("title", "")
        )

        if not title:
            return False


        invalid_words = [
            "ابطال شده",
            "باطل شده",
            "پیش نویس",
            "حذف شده"
        ]


        for word in invalid_words:

            if word in title:
                return False


        return True



    def is_annual(self, report):

        title = self.normalize(
            report.get("title", "")
        )


        patterns = [
            "سال مالی",
            "سالمالی",
            "سالانه",
            "صورت مالی سال",
            "صورتهای مالی سال",
            "صورت های مالی سال",
            "دوره منتهی به 140"
        ]


        for pattern in patterns:

            if pattern in title:
                return True


        return False



    def is_interim(self, report):

        title = self.normalize(
            report.get("title", "")
        )


        patterns = [
            "3 ماهه",
            "سه ماهه",
            "6 ماهه",
            "شش ماهه",
            "9 ماهه",
            "نه ماهه",
            "میاندوره",
            "میان دوره"
        ]


        for pattern in patterns:

            if pattern in title:
                return True


        return False



    def is_audited(self, report):

        title = self.normalize(
            report.get("title", "")
        )


        return (
            "حسابرسی شده" in title
            and
            "حسابرسی نشده" not in title
        )



    def latest_financial(self):

        reports = [

            r for r in self.financial_reports

            if self.is_valid_financial_report(r)

        ]


        if not reports:
            return None


        return max(
            reports,
            key=lambda r: self.extract_date(
                r.get("title", "")
            )
        )



    def latest_annual(self):

        annuals = [

            r for r in self.financial_reports

            if (
                self.is_valid_financial_report(r)
                and
                self.is_annual(r)
            )

        ]


        if not annuals:
            return None


        return max(
            annuals,
            key=lambda r: (
                self.is_audited(r),
                self.extract_date(
                    r.get("title", "")
                )
            )
        )



    def latest_interim(self):

        interims = [

            r for r in self.financial_reports

            if (
                self.is_valid_financial_report(r)
                and
                self.is_interim(r)
            )

        ]


        if not interims:
            return None


        return max(
            interims,
            key=lambda r: self.extract_date(
                r.get("title", "")
            )
        )



    def latest_complete_financial(self):

        annual = self.latest_annual()

        if annual:
            return annual

        return self.latest_financial()



    def latest_monthly(self):

        if not self.monthly_reports:
            return None


        valid_reports = [

            r for r in self.monthly_reports

            if self.is_valid_financial_report(r)

        ]


        if not valid_reports:
            return None


        return max(
            valid_reports,
            key=lambda r: self.extract_date(
                r.get("title", "")
            )
        )