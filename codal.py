class CodalReport:


    def __init__(
        self,
        symbol,
        period,
        sales,
        operating_profit,
        net_profit,
        non_operating_income
    ):

        self.symbol = symbol
        self.period = period
        self.sales = sales
        self.operating_profit = operating_profit
        self.net_profit = net_profit
        self.non_operating_income = non_operating_income



    def get_data(self):

        return {

            "symbol": self.symbol,

            "period": self.period,

            "sales": self.sales,

            "operating_profit": self.operating_profit,

            "net_profit": self.net_profit,

            "non_operating_income": self.non_operating_income

        }



    def show(self):

        print("------------------------")
        print("گزارش مالی کدال")
        print("------------------------")


        print(
            "نماد:",
            self.symbol
        )


        print(
            "دوره:",
            self.period
        )


        print(
            "فروش:",
            self.sales,
            "میلیارد تومان"
        )


        print(
            "سود عملیاتی:",
            self.operating_profit,
            "میلیارد تومان"
        )


        print(
            "سود خالص:",
            self.net_profit,
            "میلیارد تومان"
        )


        print(
            "درآمد غیرعملیاتی:",
            self.non_operating_income,
            "میلیارد تومان"
        )