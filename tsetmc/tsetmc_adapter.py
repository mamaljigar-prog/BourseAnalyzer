import requests


class TSETMCAdapter:


    def __init__(self):

        self.base_url = (
            "https://cdn.tsetmc.com/api"
        )

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }



    def request_json(
        self,
        url
    ):

        response = requests.get(
            url,
            headers=self.headers,
            timeout=15
        )

        response.raise_for_status()

        return response.json()



    def get_closing_price(
        self,
        ins_code
    ):

        url = (
            f"{self.base_url}/ClosingPrice/"
            f"GetClosingPriceInfo/{ins_code}"
        )

        return self.request_json(url)



    def get_instrument_info(
        self,
        ins_code
    ):

        url = (
            f"{self.base_url}/Instrument/"
            f"GetInstrumentInfo/{ins_code}"
        )

        return self.request_json(url)



    def get_company_name(
        self,
        info
    ):

        if not isinstance(info, dict):
            return None


        data = info.get(
            "instrumentInfo",
            info
        )


        if not isinstance(data, dict):
            return None



        name = data.get(
            "lVal30"
        )


        if name:

            return name.strip()



        return data.get(
            "lVal18AFC"
        )