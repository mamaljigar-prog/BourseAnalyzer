class ValuationEngine:


    def __init__(
        self,
        company,
        forecast,
        strategy
    ):

        self.company = company
        self.forecast = forecast
        self.strategy = strategy



    def run(self):

        market_cap = self.company.market_cap


        forecast_profit = self.forecast.get(
            "forecast_profit",
            0
        )


        forecast_sales = self.forecast.get(
            "forecast_sales",
            0
        )


        print()
        print("DEBUG VALUATION")
        print("------------------------------")
        print("Market Cap:", market_cap)
        print("Forecast Profit:", forecast_profit)
        print("Forecast Sales:", forecast_sales)
        print("Assets:", self.company.assets)
        print("Equity:", self.company.equity)
        print("------------------------------")



        pe_forward = 0

        if forecast_profit:

            pe_forward = (
                market_cap /
                forecast_profit
            )



        ps_forward = 0

        if forecast_sales:

            ps_forward = (
                market_cap /
                forecast_sales
            )



        pb = 0

        if self.company.equity:

            pb = (
                market_cap /
                self.company.equity
            )



        pa = 0

        if self.company.assets:

            pa = (
                market_cap /
                self.company.assets
            )



        pd_forward = 0

        if forecast_profit:

            pd_forward = (
                market_cap /
                forecast_profit
            )



        return {


            "market_cap":
                market_cap,


            "forecast_profit":
                forecast_profit,


            "forecast_sales":
                forecast_sales,


            "pe_forward":
                round(pe_forward,2),


            "ps_forward":
                round(ps_forward,2),


            "pb":
                round(pb,2),


            "pa":
                round(pa,2),


            "pd_forward":
                round(pd_forward,2)

        }