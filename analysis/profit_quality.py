class ProfitQualityAnalyzer:


    def __init__(
        self,
        operating_profit,
        net_profit,
        non_operating_income
    ):

        self.operating_profit = operating_profit
        self.net_profit = net_profit
        self.non_operating_income = non_operating_income



    def operating_profit_ratio(self):

        if self.net_profit <= 0:
            return 0

        return round(
            (
                self.operating_profit /
                self.net_profit
            ) * 100,
            2
        )



    def non_operating_ratio(self):

        if self.net_profit <= 0:
            return 0

        return round(
            (
                self.non_operating_income /
                self.net_profit
            ) * 100,
            2
        )



    def analyze(self):

        operating_ratio = (
            self.operating_profit_ratio()
        )

        non_operating_ratio = (
            self.non_operating_ratio()
        )


        if non_operating_ratio < 10:

            status = (
                "High quality profit"
            )

        elif non_operating_ratio < 30:

            status = (
                "Acceptable profit quality"
            )

        else:

            status = (
                "Warning: profit depends on non-operating income"
            )


        return {

            "operating_profit_ratio":
                operating_ratio,

            "non_operating_ratio":
                non_operating_ratio,

            "status":
                status

        }