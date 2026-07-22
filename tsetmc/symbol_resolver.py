import requests


class SymbolResolver:


    def __init__(self):

        self.base_url = (
            "https://cdn.tsetmc.com/api"
        )

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }



    def find_ins_code(
        self,
        symbol
    ):


        url = (
            f"{self.base_url}/Instrument/"
            "GetInstrumentSearch/"
            f"{symbol}"
        )


        response = requests.get(

            url,

            headers=self.headers,

            timeout=15

        )


        response.raise_for_status()


        data = response.json()



        if isinstance(data, dict):

            items = (

                data.get("instrumentSearch")

                or

                data.get("instrumentSearchList")

                or

                []

            )


        else:

            items = data



        for item in items:


            name = (

                item.get("lVal18AFC")

                or

                item.get("symbol")

                or

                ""

            )


            if name == symbol:


                return (

                    item.get(
                        "insCode"
                    )

                    or

                    item.get(
                        "inscode"
                    )

                )



        return None