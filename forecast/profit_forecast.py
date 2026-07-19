class ProfitForecast:

    def __init__(
        self,
        sales,
        net_profit,
        months_passed=12
    ):
        self.sales = sales
        self.net_profit = net_profit
        self.months_passed = months_passed


    def forecast_sales(self):

        if self.months_passed == 0:
            return 0

        return round(
            (self.sales / self.months_passed) * 12,
            2
        )


    def net_margin(self):

        if self.sales == 0:
            return 0

        return round(
            (self.net_profit / self.sales) * 100,
            2
        )


    def forecast_net_profit(self):

        return round(
            self.forecast_sales()
            *
            self.net_margin()
            /
            100,
            2
        )


    def report(self):

        return {

            "current_sales": self.sales,

            "forecast_sales": self.forecast_sales(),

            "current_profit": self.net_profit,

            "forecast_profit": self.forecast_net_profit(),

            "net_margin": self.net_margin()

        }