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



        # ==========================================
        # Annualized sales
        # ==========================================

        annual_factor = 12 / months


        forecast_sales = (

            self.company.sales *

            annual_factor

        )



        # ==========================================
        # Sales growth
        # ==========================================

        previous_sales = getattr(

            self.company,

            "previous_sales",

            0

        )


        sales_growth = 0


        if previous_sales > 0:


            sales_growth = (

                (

                    self.company.sales -

                    previous_sales

                )

                /

                previous_sales

            ) * 100



        # ==========================================
        # Profit normalization
        # ==========================================

        current_profit = getattr(

            self.company,

            "net_profit",

            0

        )


        non_operating_income = getattr(

            self.company,

            "non_operating_income",

            0

        )


        if isinstance(non_operating_income, dict):

            non_operating_income = non_operating_income.get(

                "current",

                0

            )


        normalized_current_profit = current_profit


        if non_operating_income > 0:

            normalized_current_profit = (

                current_profit -

                non_operating_income

            )



        # ==========================================
        # Historical annual profit margin
        #
        # Prevents short-term quarter margins
        # from inflating forecast valuation
        # ==========================================

        annual_sales = getattr(

            self.company,

            "annual_previous_sales",

            0

        )


        annual_profit = getattr(

            self.company,

            "annual_previous_net_profit",

            0

        )


        annual_non_operating = getattr(

            self.company,

            "annual_previous_non_operating_income",

            0

        )


        if annual_non_operating > 0:

            annual_profit = (

                annual_profit -

                annual_non_operating

            )



        historical_margin = 0


        if annual_sales > 0:

            historical_margin = (

                annual_profit /

                annual_sales

            )



        current_margin = 0


        if self.company.sales > 0:

            current_margin = (

                normalized_current_profit /

                self.company.sales

            )



        # ==========================================
        # Conservative blended margin
        #
        # Current quarter has higher weight,
        # but previous annual performance limits
        # temporary spikes.
        # ==========================================

        if historical_margin > 0 and current_margin > 0:

            margin = (

                (current_margin * 0.35) +

                (historical_margin * 0.65)

            )

        elif historical_margin > 0:

            margin = historical_margin

        else:

            margin = current_margin



        forecast_profit = (

            forecast_sales *

            margin

        )



        profit_growth = 0


        if normalized_current_profit != 0:


            profit_growth = (

                (

                    forecast_profit -

                    normalized_current_profit

                )

                /

                normalized_current_profit

            ) * 100



        return {


            "current_sales":

                self.company.sales,


            "current_profit":

                normalized_current_profit,


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

                "historical_adjusted_sales_margin",


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