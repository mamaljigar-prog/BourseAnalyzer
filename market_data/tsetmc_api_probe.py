# market_data/tsetmc_api_probe.py

import requests


class TsetmcApiProbe:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json,text/plain,*/*",
            "Referer": "https://www.tsetmc.com/"

        })


    def test_urls(self):

        urls = [

            "https://www.tsetmc.com/api/MarketWatch/GetMarketWatch",

            "https://www.tsetmc.com/api/instrument/GetInstrument",

            "https://www.tsetmc.com/api/Instrument/GetInstrument",

            "https://www.tsetmc.com/api/Symbol/GetSymbols",

            "https://www.tsetmc.com/api/Market/GetMarketWatch"

        ]


        results = []


        for url in urls:

            try:

                response = self.session.get(

                    url,

                    timeout=10

                )


                results.append({

                    "url": url,

                    "status_code":
                        response.status_code,

                    "content_type":
                        response.headers.get(
                            "Content-Type"
                        ),

                    "length":
                        len(response.text),

                    "preview":
                        response.text[:100]

                })


            except Exception as e:

                results.append({

                    "url": url,

                    "error":
                        str(e)

                })


        return results



if __name__ == "__main__":

    probe = TsetmcApiProbe()


    for item in probe.test_urls():

        print("\n")

        print(item)