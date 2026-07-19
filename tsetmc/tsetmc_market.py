class TsetmcMarket:

    def __init__(
        self,
        symbol,
        price,
        shares
    ):
        self.symbol = symbol
        self.price = price
        self.shares = shares


    def market_cap(self):

        # ارزش بازار به میلیارد تومان
        return round(
            (self.price * self.shares) / 10_000_000_000,
            2
        )


    def report(self):

        return {

            "symbol": self.symbol,

            "price": self.price,

            "shares": self.shares,

            "market_cap": self.market_cap()

        }