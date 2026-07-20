import requests


class TSETMCAdapter:

    def __init__(self):
        self.base_url = "https://cdn.tsetmc.com/api"


    def get_closing_price(self, ins_code):

        url = (
            f"{self.base_url}/ClosingPrice/"
            f"GetClosingPriceInfo/{ins_code}"
        )

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        data = response.json()

        return data



    def get_instrument_info(self, ins_code):

        url = (
            f"{self.base_url}/Instrument/"
            f"GetInstrumentInfo/{ins_code}"
        )

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        return response.json()