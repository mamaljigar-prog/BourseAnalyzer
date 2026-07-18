class CodalReport:


    def __init__(
        self,
        symbol,
        period,
        sales,
        operating_profit,
        net_profit,
        non_operating_income=0,
        assets=0,
        equity=0,
        cash_flow=0
    ):

        self.symbol = symbol

        self.period = period

        self.sales = sales

        self.operating_profit = operating_profit

        self.net_profit = net_profit

        self.non_operating_income = non_operating_income

        self.assets = assets

        self.equity = equity

        self.cash_flow = cash_flow



    def get_data(self):

        return {


            "symbol": self.symbol,

            "period": self.period,


            "sales": self.sales,

            "operating_profit": self.operating_profit,

            "net_profit": self.net_profit,


            "non_operating_income": self.non_operating_income,


            "assets": self.assets,

            "equity": self.equity,

            "cash_flow": self.cash_flow

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


        print(
            "دارایی:",
            self.assets,
            "میلیارد تومان"
        )


        print(
            "حقوق صاحبان سهام:",
            self.equity,
            "میلیارد تومان"
        )


        print(
            "جریان نقدی:",
            self.cash_flow,
            "میلیارد تومان"
        )