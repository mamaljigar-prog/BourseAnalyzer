class ForecastEngine:


    def __init__(
        self,
        company,
        strategy,
        period_months=12
    ):

        self.company = company
        self.strategy = strategy
        self.period_months = period_months



    def sales_margin_forecast(self):


        months = self.period_months


        if months <= 0:

            months = 12



        # Annualization factor
        annual_factor = 12 / months



        # Current period annualized sales
        annualized_sales = (

            self.company.sales *

            annual_factor

        )



        # Previous comparable period
        previous_sales = getattr(
            self.company,
            "previous_sales",
            0
        )



        previous_profit = getattr(
            self.company,
            "previous_profit",
            0
        )



        # Growth adjustment
        sales_growth = 0

        if previous_sales:

            sales_growth = (

                (self.company.sales - previous_sales)

                /

                previous_sales

                *

                100

            )



        # Use realistic growth instead of raw x4 growth
        if sales_growth > 0:

            forecast_sales = (

                annualized_sales *

                (1 + sales_growth / 100)

            )

        else:

            forecast_sales = annualized_sales



        # Net margin
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



        profit_growth = 0


        if self.company.net_profit:

            profit_growth = (

                (forecast_profit - self.company.net_profit)

                /

                self.company.net_profit

                *

                100

            )



        return {


            "current_sales":

                self.company.sales,


            "current_profit":

                self.company.net_profit,


            "forecast_sales":

                int(forecast_sales),


            "forecast_profit":

                int(forecast_profit),


            "sales_growth":

                round(
                    sales_growth,
                    2
                ),


            "profit_growth":

                round(
                    profit_growth,
                    2
                ),


            "net_margin":

                round(
                    margin * 100,
                    2
                ),


            "method":

                "sales_margin_growth_adjusted",


            "period_months":

                months

        }



    def run(self):


        method = self.strategy.get(

            "forecast",

            "sales_margin"

        )



        if method == "sales_margin":

            return self.sales_margin_forecast()



        return self.sales_margin_forecast()