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

        # صورت سود و زیان
        self.sales = sales
        self.operating_profit = operating_profit
        self.net_profit = net_profit

        # وضعیت مالی
        self.assets = assets
        self.equity = equity

        # بازار
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

        print("نام شرکت:", self.name)
        print("نماد:", self.symbol)

        print("------------------------------")

        print("فروش عملیاتی:", self.sales)
        print("سود عملیاتی:", self.operating_profit)
        print("سود خالص:", self.net_profit)

        print("------------------------------")

        print("جمع دارایی‌ها:", self.assets)
        print("حقوق مالکانه:", self.equity)
        print("ارزش بازار:", self.market_cap)

        print("------------------------------")

        print("حاشیه سود خالص:", self.net_margin(), "%")
        print("حاشیه سود عملیاتی:", self.operating_margin(), "%")

        print("==============================")


    def __str__(self):

        return f"""
Company: {self.name}
Symbol: {self.symbol}

Sales: {self.sales}
Operating Profit: {self.operating_profit}
Net Profit: {self.net_profit}

Assets: {self.assets}
Equity: {self.equity}
Market Cap: {self.market_cap}

Net Margin: {self.net_margin()} %
Operating Margin: {self.operating_margin()} %
"""