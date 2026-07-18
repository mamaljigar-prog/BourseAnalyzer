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
        non_operating_income=0,
        assets=0,
        equity=0,
        cash_flow=0
    ):

        self.period = period
        self.months = months

        self.sales = sales

        self.operating_profit = operating_profit

        self.net_profit = net_profit

        self.non_operating_income = non_operating_income

        self.assets = assets

        self.equity = equity

        self.cash_flow = cash_flow



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



    def debt_free_value(self):

        return self.assets - self.equity



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

            return 0



        previous = self.reports[-2]

        current = self.reports[-1]


        score = 0



        sales_growth = self.change_percent(
            current.sales,
            previous.sales
        )


        if sales_growth > 0:
            score += 2



        operating_growth = self.change_percent(
            current.operating_profit,
            previous.operating_profit
        )


        if operating_growth > 0:
            score += 2



        profit_growth = self.change_percent(
            current.net_profit,
            previous.net_profit
        )


        if profit_growth > 0:
            score += 2



        if current.net_margin() > previous.net_margin():

            score += 2



        if current.non_operating_ratio() < 0.3:

            score += 2



        return score