class ProfitQuality:


    def __init__(
        self,
        operating_profit,
        recurring_income,
        non_recurring_income,
        reported_profit=None
    ):

        self.operating_profit = operating_profit
        self.recurring_income = recurring_income
        self.non_recurring_income = non_recurring_income
        self.reported_profit = reported_profit



    def normalized_profit(self):

        # اگر سود خالص گزارش شده داریم،
        # سود غیرتکرارشونده را از آن حذف می‌کنیم

        if self.reported_profit is not None:

            return (
                self.reported_profit
                -
                self.non_recurring_income
            )


        # حالت پشتیبان

        total_profit = (
            self.operating_profit
            +
            self.recurring_income
            +
            self.non_recurring_income
        )


        return (
            total_profit
            -
            self.non_recurring_income
        )



    def score(self):

        total_profit = (

            self.operating_profit
            +
            self.recurring_income
            +
            self.non_recurring_income

        )


        if total_profit == 0:

            return 0



        score = 10



        non_recurring_ratio = (

            self.non_recurring_income
            /
            total_profit

        ) * 100



        # سهم سود غیرتکرارشونده

        if non_recurring_ratio > 30:

            score -= 4


        elif non_recurring_ratio > 10:

            score -= 2



        normalized_ratio = (

            self.normalized_profit()
            /
            total_profit

        ) * 100



        if normalized_ratio < 90:

            score -= 2



        return max(score,0)





class QualityHistory:


    def __init__(self):

        self.periods = []



    def add_period(
        self,
        period,
        recurring_income,
        non_recurring_income
    ):

        self.periods.append({

            "period": period,

            "recurring": recurring_income,

            "non_recurring": non_recurring_income

        })



    def analyze(self):

        print("------------------------")
        print("روند درآمد غیرعملیاتی")
        print("------------------------")


        repeat_count = 0



        for item in self.periods:


            print(

                item["period"],
                ":",
                item["recurring"],
                "تکرارشونده |",
                item["non_recurring"],
                "غیرتکرارشونده"

            )


            if item["recurring"] > 0:

                repeat_count += 1



        if repeat_count >= 3:

            print(
                "⚠ درآمد غیرعملیاتی چند دوره تکرار شده"
            )

        else:

            print(
                "✅ درآمد غیرعملیاتی تکرار قابل توجه ندارد"
            )