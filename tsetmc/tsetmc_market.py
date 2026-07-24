class MarketData:


    def __init__(self, closing_data, instrument_data):

        self.closing_data = closing_data["closingPriceInfo"]
        self.instrument_data = instrument_data["instrumentInfo"]



    def price(self):

        # قیمت پایانی سهم
        return self.closing_data["pClosing"]



    def shares(self):

        return self.instrument_data["zTitad"]



    def market_cap(self):

        price = self.price()
        shares = self.shares()


        value = (
            price *
            shares
        )


        # ریال به تومان و میلیارد تومان

        return round(
            value / 10 / 1_000_000_000,
            2
        )



    def report(self):

        return {

            "symbol":
            self.instrument_data["lVal18AFC"],

            "price":
            self.price(),

            "shares":
            self.shares(),

            "market_cap":
            self.market_cap()

        }