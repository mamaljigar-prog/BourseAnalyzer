class Company:


    def __init__(
        self,
        name,
        symbol,
        sales,
        operating_profit,
        net_profit,
        assets,
        equity,
        market_cap,
        non_operating_income=0
    ):

        self.name = name

        self.symbol = symbol

        self.sales = sales

        self.operating_profit = operating_profit

        self.net_profit = net_profit

        self.non_operating_income = (
            non_operating_income
        )

        self.assets = assets

        self.equity = equity

        self.market_cap = market_cap