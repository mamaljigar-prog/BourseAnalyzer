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



        annual_factor = 12 / months



        annualized_sales = (

            self.company.sales *

            annual_factor

        )



        previous_sales = getattr(

            self.company,

            "previous_sales",

            0

        )



        sales_growth = 0



        if previous_sales:


            sales_growth = (

                (self.company.sales - previous_sales)

                /

                previous_sales

                *

                100

            )



        if sales_growth > 0:


            forecast_sales = (

                annualized_sales *

                (1 + sales_growth / 100)

            )


        else:


            forecast_sales = annualized_sales




        # ==========================================
        # Normalized Profit
        #
        # Base:
        # Current Net Profit
        #
        # Rule:
        # Positive non-operating income is removed
        # because it may be non-recurring.
        #
        # Negative non-operating income is kept
        # because it represents real cost pressure.
        # ==========================================


        net_profit = getattr(

            self.company,

            "net_profit",

            0

        )


        non_operating_income = getattr(

            self.company,

            "non_operating_income",

            0

        )



        if isinstance(

            non_operating_income,

            dict

        ):

            non_operating_income = (

                non_operating_income.get(

                    "current",

                    0

                )

            )



        normalized_profit = net_profit



        if non_operating_income > 0:


            normalized_profit = (

                net_profit -

                non_operating_income

            )



        margin = (

            normalized_profit /

            self.company.sales

            if self.company.sales

            else 0

        )



        forecast_profit = (

            forecast_sales *

            margin

        )



        profit_growth = 0



        if normalized_profit:


            profit_growth = (

                (forecast_profit - normalized_profit)

                /

                normalized_profit

                *

                100

            )



        return {


            "current_sales":

                self.company.sales,



            "current_profit":

                normalized_profit,



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

                "normalized_net_profit",



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