import requests
import time


class TsetmcClient:
    """
    ارتباط با API بازار TSETMC

    قوانین پروژه:
    - P/E سایت TSETMC استفاده نمی‌شود.
    - فقط داده خام بازار دریافت می‌شود.
    - محاسبات مالی داخل BourseAnalyzer انجام می‌شود.
    """

    BASE_URL = "https://cdn.tsetmc.com"


    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "User-Agent":
                "Mozilla/5.0",

            "Accept":
                "application/json, text/plain, */*",

            "Referer":
                "https://www.tsetmc.com/"

        })


    def _get(self, endpoint):

        url = self.BASE_URL + endpoint


        last_error = None


        for attempt in range(3):

            try:

                response = self.session.get(
                    url,
                    timeout=15
                )


                if response.status_code == 200:

                    return response.json()


                else:

                    last_error = (
                        f"HTTP {response.status_code}"
                    )


            except Exception as e:

                last_error = str(e)


            print(
                f"API retry {attempt + 1}/3 : {url}"
            )


            time.sleep(2)



        raise Exception(
            f"TSETMC API failed: {url} | {last_error}"
        )



    def search_symbol(self, symbol):

        endpoint = (
            "/api/Instrument/GetInstrumentSearch/"
            + symbol
        )

        data = self._get(endpoint)


        results = (
            data
            .get("instrumentSearch", [])
        )


        for item in results:

            if item.get("lVal18AFC") == symbol:

                return item


        return None



    def get_instrument_info(self, ins_code):

        endpoint = (
            "/api/Instrument/GetInstrumentInfo/"
            + str(ins_code)
        )

        return self._get(endpoint)



    def get_closing_price(self, ins_code):

        endpoint = (
            "/api/ClosingPrice/GetClosingPriceInfo/"
            + str(ins_code)
        )

        return self._get(endpoint)



    def get_market_snapshot(self, ins_code):

        info = self.get_instrument_info(
            ins_code
        )


        price = self.get_closing_price(
            ins_code
        )


        instrument = (
            info
            .get("instrumentInfo", {})
        )


        closing = (
            price
            .get("closingPriceInfo", {})
        )


        return {

            "ins_code":
                ins_code,


            "symbol":
                instrument.get(
                    "lVal18AFC"
                ),


            "name":
                instrument.get(
                    "lVal30"
                ),


            "shares":
                instrument.get(
                    "zTitad"
                ),


            "last_price":
                closing.get(
                    "pDrCotVal"
                ),


            "closing_price":
                closing.get(
                    "pClosing"
                ),


            "industry":
                instrument
                .get("sector", {})
                .get("lSecVal")

        }



if __name__ == "__main__":


    client = TsetmcClient()


    result = client.search_symbol(
        "شپنا"
    )


    print(result)