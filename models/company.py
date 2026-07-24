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
        non_operating_income=0,
        industry="",
        period_months=12
    ):


        self.name = name

        self.symbol = symbol

        self.industry = industry


        # Financial Data

        self.sales = sales

        self.operating_profit = operating_profit

        self.net_profit = net_profit


        self.non_operating_income = (
            non_operating_income
        )


        # Balance Sheet

        self.assets = assets

        self.equity = equity


        # Market Data

        self.market_cap = market_cap


        # Report Period

        self.period_months = (
            period_months
        )