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

            "ÙŠ": "ÛŒ",
            "Ù‰": "ÛŒ",
            "Ùƒ": "Ú©",
            "\u200c": "",
            "\u200e": "",
            "\u200f": ""

        }

        for a, b in replacements.items():

            text = text.replace(a, b)


        return text



    def normalize_digits(self, text):

        if not text:

            return ""


        replacements = {

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

            text = text.replace(a, b)


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

            y, m, d = matches[-1].split("/")


            return datetime(

                int(y),

                int(m),

                int(d)

            )


        except:

            return datetime.min



    def is_annual(self, report):


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



    def is_interim(self, report):


        title = self.normalize(

            report.get(

                "title",

                ""

            )

        )


        return (

            "میاندوره" in title

            or

            "میان دوره" in title

            or

            "دوره ۳ ماهه" in title

            or

            "دوره ۶ ماهه" in title

            or

            "دوره ۹ ماهه" in title

        )



    def is_audited(self, report):


        title = self.normalize(

            report.get(

                "title",

                ""

            )

        )


        return (

            "حسابرسی شده" in title

            and

            "نشده" not in title

        )



    def latest_annual(self):


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



    def latest_interim(self):


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



    def latest_financial(self):


        return self.latest_annual()



    def latest_complete_financial(self):


        return self.latest_annual()



    def latest_monthly(self):


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