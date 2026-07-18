class QualityHistory:


    def __init__(self):

        self.data = []



    def add_period(
        self,
        period,
        operating_profit,
        recurring_non_operating,
        non_recurring_income
    ):

        self.data.append({

            "period": period,

            "operating_profit": operating_profit,

            "recurring_non_operating": recurring_non_operating,

            "non_recurring_income": non_recurring_income

        })



    def analyze(self):

        print("------------------------")
        print("روند درآمد غیرعملیاتی")
        print("------------------------")


        count = 0


        for item in self.data:

            print(
                item["period"],
                ":",
                item["recurring_non_operating"],
                "تکرارشونده |",
                item["non_recurring_income"],
                "غیرتکرارشونده"
            )


            if item["recurring_non_operating"] > 0:

                count += 1



        print("------------------------")


        if count >= 3:

            print(
                "⚠ درآمد غیرعملیاتی در چند دوره تکرار شده است"
            )

            print(
                "بررسی ماهیت درآمد ضروری است"
            )


        else:

            print(
                "✅ وابستگی چنددوره‌ای مشاهده نشد"
            )