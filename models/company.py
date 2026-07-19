class Company:

    def __init__(
        self,
        name,
        symbol=None,
        sales=0,
        operating_profit=0,
        net_profit=0,
        assets=0,
        equity=0,
        market_cap=0
    ):

        self.name = name
        self.symbol = symbol

        self.sales = sales
        self.operating_profit = operating_profit
        self.net_profit = net_profit

        self.assets = assets
        self.equity = equity

        self.market_cap = market_cap


    def net_margin(self):

        if self.sales == 0:
            return 0

        return round(
            (self.net_profit / self.sales) * 100,
            2
        )


    def operating_margin(self):

        if self.sales == 0:
            return 0

        return round(
            (self.operating_profit / self.sales) * 100,
            2
        )


    def show(self):

        print("==============================")
        print("COMPANY REPORT")
        print("==============================")

        print("Name:", self.name)
        print("Symbol:", self.symbol)

        print("------------------------------")

        print("Sales:", self.sales)
        print("Operating Profit:", self.operating_profit)
        print("Net Profit:", self.net_profit)

        print("------------------------------")

        print("Assets:", self.assets)
        print("Equity:", self.equity)
        print("Market Cap:", self.market_cap)

        print("------------------------------")

        print("Net Margin:", self.net_margin(), "%")
        print("Operating Margin:", self.operating_margin(), "%")

        print("==============================")


    def __str__(self):

        return (
            f"{self.name} ({self.symbol})\n"
            f"Sales: {self.sales}\n"
            f"Net Profit: {self.net_profit}"
        )