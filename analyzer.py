from valuation.valuation_model import calculate_valuation


class StockAnalyzer:

    def __init__(
        self,
        symbol,
        market_cap,
        sales,
        profit,
        assets,
        equity
    ):

        self.symbol = symbol
        self.market_cap = market_cap

        self.sales = sales
        self.profit = profit

        self.assets = assets
        self.equity = equity


    def report(self):

        result = calculate_valuation(
            market_cap=self.market_cap,
            forecast_sales=self.sales,
            forecast_profit=self.profit,
            equity=self.equity,
            assets=self.assets
        )

        return {

            "symbol": self.symbol,

            "market_value": self.market_cap,

            "forecast_sales": self.sales,

            "forecast_profit": self.profit,

            "PE": result["PE"],

            "PS": result["PS"],

            "PB": result["PB"],

            "PA": result["PA"]
        }