# market_data/symbol_resolver.py

import requests
from urllib.parse import quote


class SymbolResolver:
    """
    پیدا کردن اطلاعات نماد از TSETMC
    """

    BASE_URL = "https://www.tsetmc.com"


    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "User-Agent": "Mozilla/5.0",

            "Accept": "application/json,text/plain,*/*",

            "Referer": "https://www.tsetmc.com/"

        })


    def search(self, symbol):

        encoded_symbol = quote(
            symbol
        )

        url = (

            self.BASE_URL +

            "/api/Instrument/"
            "GetInstrumentSearch/" +

            encoded_symbol

        )


        response = self.session.get(

            url,

            timeout=10

        )


        result = {

            "status_code":
                response.status_code,

            "content_type":
                response.headers.get(
                    "Content-Type"
                ),

            "symbol":
                symbol,

            "url":
                url

        }


        try:

            result["data"] = response.json()


        except Exception:

            result["raw"] = response.text[:500]


        return result



if __name__ == "__main__":

    resolver = SymbolResolver()

    print(
        resolver.search("شپنا")
    )