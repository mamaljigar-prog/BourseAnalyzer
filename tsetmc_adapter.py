from tsetmc import Tsetmc



class TsetmcAdapter:


    def __init__(self, symbol):

        self.symbol = symbol



    def get_stock_data(self):


        tsetmc = Tsetmc(self.symbol)


        data = tsetmc.get_data()



        result = {

            "symbol": data["symbol"],

            "company": data["company"],

            "shares": data["shares"],

            "market": data["market"],

            "last_price": data["last_price"],

            "closing_price": data["closing_price"]

        }



        result["market_value"] = (

            result["shares"]

            *

            result["closing_price"]

        )



        return result