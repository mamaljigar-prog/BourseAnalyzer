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

            "PageSize": 50

        }


        response = requests.get(

            url,

            params=params,

            headers=self.headers,

            timeout=30

        )


        print(
            "Codal Status:",
            response.status_code
        )


        return response.json()



    def find_financial_reports(self):

        data = self.search_reports()


        reports = data.get(
            "Letters",
            []
        )


        result = []


        for report in reports:


            title = report.get(
                "Title",
                ""
            )


            if (
                "صورت‌های مالی" in title
                or
                "صورت های مالی" in title
                or
                "اطلاعات و صورت‌های مالی" in title
            ):


                result.append({

                    "type": "financial",

                    "title": title,

                    "url": report.get("Url")

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


            title = report.get(
                "Title",
                ""
            )


            if "گزارش فعالیت ماهانه" in title:


                result.append({

                    "type": "monthly",

                    "title": title,

                    "url": report.get("Url")

                })


        return result





if __name__ == "__main__":


    adapter = CodalAdapter(
        "خراسان"
    )


    print("================ مالی ================")


    for r in adapter.find_financial_reports():

        print(r["title"])



    print("================ ماهانه ================")


    for r in adapter.find_monthly_reports():

        print(r["title"])