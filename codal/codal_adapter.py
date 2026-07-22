import requests



class CodalAdapter:


    def __init__(self, symbol):

        self.symbol = symbol

        self.headers = {

            "User-Agent": "Mozilla/5.0"

        }



    def search_reports(self):


        url = "https://search.codal.ir/api/search/v2/q"


        params = {

            "Symbol": self.symbol,

            "PageNumber": 1,

            "PageSize": 200,

            "Category": 1

        }


        response = requests.get(

            url,

            params=params,

            headers=self.headers,

            timeout=30

        )


        response.raise_for_status()


        return response.json()



    def normalize(self, text):

        if not text:

            return ""


        return (

            str(text)

            .replace("\u200c", "")

            .replace("\u200e", "")

            .replace("\u200f", "")

            .strip()

        )



    def find_financial_reports(self):


        data = self.search_reports()


        reports = data.get(

            "Letters",

            []

        )


        result = []



        for report in reports:


            title = self.normalize(

                report.get(

                    "Title",

                    ""

                )

            )


            if (

                "صورت" in title

                and

                "مالی" in title

            ):


                result.append({

                    "type":

                    "financial",


                    "title":

                    title,


                    "url":

                    report.get(

                        "Url"

                    )

                })


        return result



    def find_monthly_reports(self):


        data = self.search_reports()


        reports = data.get(

            "Letters",

            []

        )


        result = []



        for report in reports:


            title = self.normalize(

                report.get(

                    "Title",

                    ""

                )

            )


            if (

                "گزارش فعالیت ماهانه" in title

            ):


                result.append({

                    "type":

                    "monthly",


                    "title":

                    title,


                    "url":

                    report.get(

                        "Url"

                    )

                })


        return result