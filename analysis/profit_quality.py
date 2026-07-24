class ProfitQualityAnalyzer:


    def __init__(
        self,
        operating_profit,
        net_profit,
        non_operating_income
    ):

        self.operating_profit = operating_profit or 0
        self.net_profit = net_profit or 0
        self.non_operating_income = non_operating_income or 0



    def analyze(self):


        if self.net_profit <= 0:

            return {

                "operating_profit_ratio": 0,

                "non_operating_ratio": 0,

                "status":
                    "Negative profit"

            }



        operating_ratio = (
            self.operating_profit
            /
            self.net_profit
        ) * 100



        non_operating_ratio = (
            self.non_operating_income
            /
            self.net_profit
        ) * 100



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
                "Low quality profit - depends on non operating income"
            )



        return {


            "operating_profit_ratio":

                round(
                    operating_ratio,
                    2
                ),



            "non_operating_ratio":

                round(
                    non_operating_ratio,
                    2
                ),



            "status":

                status



        }