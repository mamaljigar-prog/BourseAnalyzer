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



    def normalize(self,text):

        if not text:
            return ""

        text=str(text)

        for a,b in {

            "ي":"ی",
            "ى":"ی",
            "ك":"ک",
            "\u200c":"",
            "\u200e":"",
            "\u200f":""

        }.items():

            text=text.replace(a,b)

        return text



    def normalize_digits(self,text):

        for a,b in {

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

        }.items():

            text=text.replace(a,b)

        return text



    def extract_date(self,title):

        title=self.normalize_digits(title)

        matches=re.findall(
            r'140\d/\d{2}/\d{2}',
            title
        )


        if not matches:

            return datetime.min


        try:

            y,m,d=matches[-1].split("/")

            return datetime(
                int(y),
                int(m),
                int(d)
            )

        except:

            return datetime.min



    def score_report(self,report):

        title=self.normalize(

            report.get(
                "title",
                ""
            )

        )


        score=0


        # حذف توضیحات
        if "توضیحات" in title:

            return -1000



        # حذف تلفیقی
        if "تلفیقی" in title:

            score-=500



        # صورت مالی سالانه اولویت بالا
        if "صورتهای مالی" in title:

            score+=100


        if "سالمالی" in title or "سال مالی" in title:

            score+=100



        # حسابرسی شده بهتر است
        if "حسابرسیشده" in title:

            score+=50



        # میان دوره ای پایین تر
        if "میاندوره" in title:

            score-=50



        return score



    def latest_complete_financial(self):


        if not self.financial_reports:

            return None



        return sorted(

            self.financial_reports,

            key=lambda r:(

                self.score_report(r),

                self.extract_date(

                    r.get(
                        "title",
                        ""
                    )

                )

            ),

            reverse=True

        )[0]



    def latest_financial(self):


        return self.latest_complete_financial()



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