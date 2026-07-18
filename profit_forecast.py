class ProfitForecast:


    def __init__(
        self,
        yearly_sales,
        net_margin
    ):

        self.yearly_sales = yearly_sales
        self.net_margin = net_margin



    def calculate_profit(self):

        profit = (
            self.yearly_sales *
            self.net_margin /
            100
        )

        return round(
            profit,
            2
        )



    def report(self):

        profit = self.calculate_profit()


        print("----------------------")
        print("پیش بینی سود")
        print("----------------------")


        print(
            "فروش سالانه:",
            self.yearly_sales,
            "میلیارد تومان"
        )


        print(
            "حاشیه سود خالص:",
            self.net_margin,
            "%"
        )


        print(
            "سود پیش بینی شده:",
            profit,
            "میلیارد تومان"
        )