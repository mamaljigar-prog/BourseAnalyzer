class FullReport:


    def __init__(
        self,
        stock_data,
        profit_quality_score,
        normalized_profit,
        fundamental_score
    ):

        self.stock_data = stock_data
        self.profit_quality_score = profit_quality_score
        self.normalized_profit = normalized_profit
        self.fundamental_score = fundamental_score



    def show(self):

        print("==============================")
        print("گزارش جامع تحلیل سهم")
        print("==============================")


        print(
            "نماد:",
            self.stock_data["symbol"]
        )


        print("------------------------------")


        print(
            "ارزش بازار:",
            round(self.stock_data["market_value"]),
            "میلیارد تومان"
        )


        print(
            "فروش برآوردی:",
            self.stock_data["sales"],
            "میلیارد تومان"
        )


        print(
            "سود خالص گزارش شده:",
            self.stock_data["profit"],
            "میلیارد تومان"
        )


        print(
            "سود نرمال شده:",
            self.normalized_profit,
            "میلیارد تومان"
        )



        if self.normalized_profit < self.stock_data["profit"] * 0.8:

            print(
                "⚠ هشدار: بخش قابل توجهی از سود گزارش شده قابل اتکا نیست"
            )


        print("------------------------------")


        print(
            "P/E Forward:",
            round(self.stock_data["pe"],2)
        )


        print(
            "P/S Forward:",
            round(self.stock_data["ps"],2)
        )


        print(
            "P/B:",
            round(self.stock_data["pb"],2)
        )


        print(
            "P/A:",
            round(self.stock_data["pa"],2)
        )



        if self.normalized_profit > 0:

            normalized_pe = (
                self.stock_data["market_value"]
                /
                self.normalized_profit
            )


            print(
                "P/E بر اساس سود نرمال شده:",
                round(normalized_pe,2)
            )



        print("------------------------------")


        print(
            "کیفیت سود:",
            self.profit_quality_score,
            "از 10"
        )


        print(
            "امتیاز بنیادی:",
            self.fundamental_score,
            "از 100"
        )


        print("==============================")