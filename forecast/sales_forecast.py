class SalesForecast:

    def __init__(self, sales, months_passed):
        self.sales = sales
        self.months_passed = months_passed


    def forecast_year_sales(self):
        if self.months_passed == 0:
            return 0

        return round(
            (self.sales / self.months_passed) * 12
        )


    def monthly_average(self):
        if self.months_passed == 0:
            return 0

        return round(
            self.sales / self.months_passed
        )


    def growth_vs_previous_month(self, previous_month_sales):

        if previous_month_sales == 0:
            return 0

        return round(
            ((self.monthly_average() - previous_month_sales)
            / previous_month_sales) * 100,
            2
        )


    def report(self):

        return {
            "current_sales": self.sales,
            "months_passed": self.months_passed,
            "forecast_sales": self.forecast_year_sales(),
            "monthly_average": self.monthly_average()
        }