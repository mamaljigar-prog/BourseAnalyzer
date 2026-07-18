class IncomeAnalysis:


    def __init__(
        self,
        operating_income,
        recurring_income,
        non_recurring_income
    ):

        self.operating_income = operating_income
        self.recurring_income = recurring_income
        self.non_recurring_income = non_recurring_income



    def total_income(self):

        return (
            self.operating_income
            +
            self.recurring_income
            +
            self.non_recurring_income
        )



    def quality_score(self):

        total = self.total_income()


        if total == 0:
            return 0


        non_recurring_ratio = (
            self.non_recurring_income / total
        ) * 100


        recurring_ratio = (
            self.recurring_income / total
        ) * 100



        score = 10



        # جریمه درآمد غیرتکرارشونده

        if non_recurring_ratio > 30:

            score -= 4

        elif non_recurring_ratio > 15:

            score -= 2



        # امتیاز برای درآمد تکرارشونده

        if recurring_ratio > 20:

            score += 1



        if score > 10:
            score = 10


        return score



    def show(self):

        print("------------------------")
        print("تحلیل ساختار درآمد")
        print("------------------------")


        print(
            "درآمد عملیاتی:",
            self.operating_income
        )


        print(
            "درآمد غیرعملیاتی تکرارشونده:",
            self.recurring_income
        )


        print(
            "درآمد غیرعملیاتی غیرتکرارشونده:",
            self.non_recurring_income
        )


        print("------------------------")


        print(
            "کیفیت درآمد:",
            self.quality_score(),
            "از 10"
        )



        if self.quality_score() >= 8:

            print(
                "✅ ساختار درآمد مناسب"
            )

        elif self.quality_score() >= 5:

            print(
                "🟡 نیازمند بررسی"
            )

        else:

            print(
                "🔴 وابستگی بالا به درآمد غیرتکرارشونده"
            )