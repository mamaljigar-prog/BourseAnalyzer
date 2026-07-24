class ForecastEngine:


    def __init__(
        self,
        company,
        strategy,
        period_months=12
    ):

        self.company = company
        self.strategy = strategy

        self.period_months = (
            period_months
            if period_months and period_months > 0
            else 12
        )



    def sales_margin_forecast(self):

        months = self.period_months


        # ==========================================
        # Annualization
        #
        # Reports are cumulative from start of
        # financial year.
        #
        # Example:
        # 3 months  -> x4
        # 6 months  -> x2
        # 9 months  -> x1.33
        # 12 months -> x1
        # ==========================================

        annual_factor = 12 / months


        current_sales = getattr(
            self.company,
            "sales",
            0
        )


        forecast_sales = (

            current_sales *

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

                    current_sales -

                    previous_sales

                )

                /

                previous_sales

            ) * 100



        # ==========================================
        # Current profit normalization
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


        if isinstance(
            non_operating_income,
            dict
        ):

            non_operating_income = non_operating_income.get(
                "current",
                0
            )


        normalized_profit = current_profit


        if non_operating_income > 0:

            normalized_profit = (

                current_profit -

                non_operating_income

            )



        # ==========================================
        # Current margin
        # ==========================================

        current_margin = 0


        if current_sales > 0:

            current_margin = (

                normalized_profit /

                current_sales

            )



        # ==========================================
        # Previous annual margin
        #
        # Used only as quality control.
        # Not mandatory.
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



        # ==========================================
        # Profit margin selection
        #
        # Current period is the main signal.
        # Historical annual margin prevents
        # temporary abnormal profitability.
        # ==========================================

        if (
            historical_margin > 0
            and
            current_margin > 0
        ):

            margin = (

                current_margin * 0.7

                +

                historical_margin * 0.3

            )


        elif current_margin > 0:

            margin = current_margin


        else:

            margin = historical_margin



        # ==========================================
        # Forecast profit
        # ==========================================

        forecast_profit = (

            forecast_sales *

            margin

        )



        profit_growth = 0


        if normalized_profit != 0:

            profit_growth = (

                (

                    forecast_profit -

                    normalized_profit

                )

                /

                abs(normalized_profit)

            ) * 100



        return {


            "current_sales":

                current_sales,


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

                "period_based_sales_margin",


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