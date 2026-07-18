from valuation import (
    market_cap_toman,
    forward_pe,
    forward_ps,
    future_value_by_pe
)



class StockAnalyzer:


    def __init__(
        self,
        symbol,
        price,
        shares,
        sales_forecast,
        profit_forecast,
        assets,
        equity
    ):

        self.symbol = symbol
        self.price = price
        self.shares = shares
        self.sales_forecast = sales_forecast
        self.profit_forecast = profit_forecast

        # اطلاعات ترازنامه
        self.assets = assets
        self.equity = equity



    def market_value(self):

        return market_cap_toman(
            self.price,
            self.shares
        )



    def pe_forward(self):

        return forward_pe(
            self.market_value(),
            self.profit_forecast
        )



    def ps_forward(self):

        return forward_ps(
            self.market_value(),
            self.sales_forecast
        )



    def pb(self):

        if self.equity == 0:
            return 0

        return self.market_value() / self.equity



    def pa(self):

        if self.assets == 0:
            return 0

        return self.market_value() / self.assets



    def future_market_value(self):

        return future_value_by_pe(
            self.profit_forecast,
            7
        )



    def upside(self):

        return (
            (self.future_market_value() - self.market_value())
            /
            self.market_value()
        ) * 100



    def get_report_data(self):

        return {

            "symbol": self.symbol,

            "market_value": self.market_value(),

            "sales": self.sales_forecast,

            "profit": self.profit_forecast,

            "pe": self.pe_forward(),

            "ps": self.ps_forward(),

            "pb": self.pb(),

            "pa": self.pa(),

            "future_value": self.future_market_value(),

            "upside": self.upside()

        }