class Company:

    def __init__(
        self,
        symbol,
        name,
        sales,
        net_profit,
        assets,
        equity
    ):

        self.symbol = symbol
        self.name = name

        self.sales = sales
        self.net_profit = net_profit

        self.assets = assets
        self.equity = equity


    def net_margin(self):

        if self.sales == 0:
            return 0

        return round(
            (self.net_profit / self.sales) * 100,
            2
        )


    def report(self):

        return {

            "symbol": self.symbol,

            "name": self.name,

            "sales": self.sales,

            "net_profit": self.net_profit,

            "assets": self.assets,

            "equity": self.equity,

            "net_margin": self.net_margin()

        }