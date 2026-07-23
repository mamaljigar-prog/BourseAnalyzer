class ForecastEngine:


    def __init__(
        self,
        company,
        strategy
    ):

        self.company = company
        self.strategy = strategy



    def sales_margin_forecast(self):

        months_passed = 9


        forecast_sales = (

            self.company.sales /

            months_passed

        ) * 12



        margin = (

            self.company.net_profit /

            self.company.sales

            if self.company.sales

            else 0

        )


        forecast_profit = (

            forecast_sales *

            margin

        )


        return {

            "forecast_sales": forecast_sales,

            "forecast_profit": forecast_profit,

            "method": "sales_margin"

        }



    def run(self):


        forecast_method = self.strategy.get(
            "forecast",
            "sales_margin"
        )



        if forecast_method == "sales_margin":

            return self.sales_margin_forecast()



        return self.sales_margin_forecast()