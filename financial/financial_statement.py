class FinancialStatement:


    def __init__(self, data=None):

        if data is None:

            data = {}


        self.revenue = data.get(
            "sales"
        )


        self.gross_profit = data.get(
            "gross_profit"
        )


        self.operating_profit = data.get(
            "operating_profit"
        )


        self.net_profit = data.get(
            "net_profit"
        )


        self.non_operating_income = data.get(
            "non_operating_income"
        )


        # مراحل بعدی پروژه

        self.assets = None

        self.liabilities = None

        self.equity = None

        self.operating_cash_flow = None



    def to_dict(self):

        return {

            "revenue":
                self.revenue,

            "gross_profit":
                self.gross_profit,

            "operating_profit":
                self.operating_profit,

            "net_profit":
                self.net_profit,

            "non_operating_income":
                self.non_operating_income,

            "assets":
                self.assets,

            "liabilities":
                self.liabilities,

            "equity":
                self.equity,

            "operating_cash_flow":
                self.operating_cash_flow

        }



    def is_valid(self):

        required_values = [

            self.revenue,

            self.net_profit

        ]


        for value in required_values:

            if value is None:

                return False


        return True