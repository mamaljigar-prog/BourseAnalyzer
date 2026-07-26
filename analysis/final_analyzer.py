class FinalAnalyzer:

    def __init__(
        self,
        company,
        forecast_sales,
        forecast_profit,
        profit_quality,
        valuation,
        period_type=None,
        duration_months=None,
        annualization_factor=None
    ):

        self.company = company

        self.forecast_sales = forecast_sales

        self.forecast_profit = forecast_profit

        self.profit_quality = profit_quality

        self.valuation = valuation

        self.period_type = period_type

        self.duration_months = duration_months

        self.annualization_factor = (
            annualization_factor
        )


    def growth_rate(
        self,
        current,
        forecast
    ):

        # Forecast سالانه‌شده، رشد قابل مقایسه
        # با دوره جاری نیست.
        #
        # بنابراین این متد دیگر برای محاسبه
        # رشد Current -> Forecast استفاده نمی‌شود.

        return None


    def debt_to_equity(self):

        if self.company.equity == 0:

            return 0

        liabilities = (

            self.company.assets

            -

            self.company.equity

        )

        return round(

            liabilities /

            self.company.equity,

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

            "company":
                self.company.name,

            "symbol":
                self.company.symbol,


            "performance": {

                "current_sales":
                    self.company.sales,

                "forecast_sales":
                    round(
                        self.forecast_sales
                    ),

                # رشد قابل مقایسه هنوز
                # از دوره مشابه سال قبل
                # استخراج نشده است.

                "sales_growth":
                    None,

                "sales_growth_status":
                    "Comparable period data not available"

            },


            "profitability": {

                "current_profit":
                    self.company.net_profit,

                "forecast_profit":
                    round(
                        self.forecast_profit
                    ),

                # رشد قابل مقایسه هنوز
                # از دوره مشابه سال قبل
                # استخراج نشده است.

                "profit_growth":
                    None,

                "profit_growth_status":
                    "Comparable period data not available",

                "net_margin":
                    round(

                        (

                            self.company.net_profit

                            /

                            self.company.sales

                        )

                        *

                        100,

                        2

                    )

                    if self.company.sales

                    else 0

            },


            "financial_period": {

                "period_type":
                    self.period_type,

                "duration_months":
                    self.duration_months,

                "annualization_factor":
                    self.annualization_factor

            },


            "balance_sheet": {

                "assets":
                    self.company.assets,

                "equity":
                    self.company.equity,

                "liabilities":
                    (

                        self.company.assets

                        -

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