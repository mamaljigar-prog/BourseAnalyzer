import requests


class CodalAdapter:


    def __init__(self, symbol):

        self.symbol = symbol



    def get_reports(self):

        url = "https://search.codal.ir/api/search/v2/q"


        params = {

            "Symbol": self.symbol,

            "PageNumber": 1,

            "PageSize": 10

        }


        headers = {

            "User-Agent":
            "Mozilla/5.0"

        }


        try:

            response = requests.get(

                url,

                params=params,

                headers=headers,

                timeout=30

            )


            print(
                "Status:",
                response.status_code
            )


            data = response.json()


            return data



        except requests.exceptions.Timeout:

            print(
                "کدال پاسخ نداد (Timeout)"
            )

            return None



        except Exception as e:

            print(
                "خطا:",
                e
            )

            return None