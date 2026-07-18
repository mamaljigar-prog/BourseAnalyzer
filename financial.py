class FinancialReport:
    """
    گزارش مالی یک دوره
    واحد: میلیارد تومان
    """

    def __init__(
        self,
        period,
        months,
        sales,
        operating_profit,
        net_profit,
        non_operating_income=0
    ):

        self.period = period
        self.months = months
        self.sales = sales
        self.operating_profit = operating_profit
        self.net_profit = net_profit
        self.non_operating_income = non_operating_income


    def net_margin(self):

        if self.sales == 0:
            return 0

        return self.net_profit / self.sales



    def operating_margin(self):

        if self.sales == 0:
            return 0

        return self.operating_profit / self.sales



    def non_operating_ratio(self):

        if self.net_profit == 0:
            return 0

        return self.non_operating_income / self.net_profit



class FinancialHistory:


    def __init__(self):

        self.reports = []



    def add_report(self, report):

        self.reports.append(report)



    def change_percent(self, current, previous):

        if previous == 0:
            return 0

        return ((current - previous) / previous) * 100




    def fundamental_score(self):

        if len(self.reports) < 2:

            print("گزارش کافی نیست")
            return



        previous = self.reports[-2]
        current = self.reports[-1]


        score = 0



        # رشد فروش

        sales_growth = self.change_percent(
            current.sales,
            previous.sales
        )


        if sales_growth > 0:
            score += 2



        # رشد سود عملیاتی

        operating_growth = self.change_percent(
            current.operating_profit,
            previous.operating_profit
        )


        if operating_growth > 0:
            score += 2



        # رشد سود خالص

        profit_growth = self.change_percent(
            current.net_profit,
            previous.net_profit
        )


        if profit_growth > 0:
            score += 2



        # بهبود حاشیه سود

        if current.net_margin() > previous.net_margin():

            score += 2



        # کیفیت سود

        if current.non_operating_ratio() < 0.3:

            score += 2



        print("----------------")
        print("امتیاز بنیادی:", score, "از 10")


        if score >= 8:

            print("🟢 وضعیت بنیادی مناسب")


        elif score >= 5:

            print("🟡 نیازمند بررسی")


        else:

            print("🔴 وضعیت بنیادی ضعیف")