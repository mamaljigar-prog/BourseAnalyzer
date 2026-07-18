class StockReport:


    def __init__(self, data):

        self.data = data



    def show(self):

        print("========================")
        print("گزارش تحلیل سهم")
        print("========================")


        print("نماد:", self.data["symbol"])

        print("------------------------")


        print(
            "ارزش بازار:",
            round(self.data["market_value"]),
            "میلیارد تومان"
        )


        print(
            "فروش برآوردی:",
            self.data["sales"],
            "میلیارد تومان"
        )


        print(
            "سود خالص برآوردی:",
            self.data["profit"],
            "میلیارد تومان"
        )


        print("------------------------")


        print(
            "P/E Forward:",
            round(self.data["pe"],2)
        )


        print(
            "P/S Forward:",
            round(self.data["ps"],2)
        )


        print(
            "P/B:",
            round(self.data["pb"],2)
        )


        print(
            "P/A:",
            round(self.data["pa"],2)
        )


        print("------------------------")


        print(
            "ارزش آینده با PE=7:",
            round(self.data["future_value"]),
            "میلیارد تومان"
        )


        print(
            "پتانسیل تغییر:",
            round(self.data["upside"],2),
            "%"
        )


        print("========================")