class FinalAnalyzer:

    def __init__(
        self,
        company,
        forecast_sales,
        forecast_profit,
        profit_quality,
        valuation
    ):

        self.company = company
        self.forecast_sales = forecast_sales
        self.forecast_profit = forecast_profit
        self.profit_quality = profit_quality
        self.valuation = valuation


    def growth_rate(self, current, forecast):

        if current == 0:
            return 0

        return round(
            ((forecast - current) / current) * 100,
            2
        )


    def debt_to_equity(self):

        if self.company.equity == 0:
            return 0

        liabilities = (
            self.company.assets -
            self.company.equity
        )

        return round(
            liabilities / self.company.equity,
            2
        )


    def balance_status(self):

        ratio = self.debt_to_equity()

        if ratio < 1:

            return "Healthy"

        elif ratio < 2:

            return "Moderate"

        else:

            return "High debt"


    def generate(self):

        return {

            "company": self.company.name,

            "symbol": self.company.symbol,


            "performance": {

                "current_sales":
                    self.company.sales,

                "forecast_sales":
                    round(
                        self.forecast_sales
                    ),

                "sales_growth":
                    self.growth_rate(
                        self.company.sales,
                        self.forecast_sales
                    )

            },


            "profitability": {

                "current_profit":
                    self.company.net_profit,

                "forecast_profit":
                    round(
                        self.forecast_profit
                    ),

                "profit_growth":
                    self.growth_rate(
                        self.company.net_profit,
                        self.forecast_profit
                    ),

                "net_margin":
                    round(
                        (
                            self.company.net_profit /
                            self.company.sales
                        ) * 100,
                        2
                    )
                    if self.company.sales
                    else 0

            },


            "balance_sheet": {

                "assets":
                    self.company.assets,

                "equity":
                    self.company.equity,

                "liabilities":
                    (
                        self.company.assets -
                        self.company.equity
                    ),

                "status":
                    self.balance_status(),

                "debt_equity":
                    self.debt_to_equity()

            },


            "profit_quality":
                self.profit_quality,


            "valuation":
                self.valuation

        }