class SalesForecast:

    def __init__(self, sales, months_passed):
        self.sales = sales
        self.months_passed = months_passed


    def forecast(self):
        if self.months_passed == 0:
            return 0

        return round(
            self.sales * 12 / self.months_passed
        )


    def growth_vs_previous(self, previous_sales):
        if previous_sales == 0:
            return 0

        return round(
            ((self.sales - previous_sales) / previous_sales) * 100,
            2
        )