from datetime import datetime
import re


class ReportSelector:

    def __init__(self, financial_reports, monthly_reports):

        self.financial_reports = financial_reports or []
        self.monthly_reports = monthly_reports or []


    def normalize_digits(self, text):

        if not text:
            return ""

        digits = {
            "۰":"0",
            "۱":"1",
            "۲":"2",
            "۳":"3",
            "۴":"4",
            "۵":"5",
            "۶":"6",
            "۷":"7",
            "۸":"8",
            "۹":"9"
        }

        for a,b in digits.items():
            text = text.replace(a,b)

        return text



    def extract_date(self, title):

        title = self.normalize_digits(title)

        matches = re.findall(
            r'140\d/\d{2}/\d{2}',
            title
        )


        if not matches:
            return datetime.min


        try:

            y,m,d = matches[-1].split("/")

            return datetime(
                int(y),
                int(m),
                int(d)
            )

        except:

            return datetime.min



    def is_revision(self, title):

        if not title:
            return False

        return (
            "اصلاحیه" in title
        )



    def sort_key(self, report):

        title = report.get(
            "title",
            ""
        )

        return (

            self.extract_date(title),

            self.is_revision(title)

        )



    def latest(self, reports):

        if not reports:
            return None


        return sorted(
            reports,
            key=self.sort_key,
            reverse=True
        )[0]



    def latest_financial(self):

        return self.latest(
            self.financial_reports
        )



    def latest_monthly(self):

        return self.latest(
            self.monthly_reports
        )



    def summary(self):

        return {

            "latest_financial":
                self.latest_financial(),

            "latest_monthly":
                self.latest_monthly(),

            "financial_count":
                len(self.financial_reports),

            "monthly_count":
                len(self.monthly_reports)

        }