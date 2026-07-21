class FinancialData:

    def __init__(
        self,
        symbol,
        report_title,
        sales,
        gross_profit,
        operating_profit,
        net_profit
    ):

        self.symbol = symbol
        self.report_title = report_title

        self.sales = sales
        self.gross_profit = gross_profit
        self.operating_profit = operating_profit
        self.net_profit = net_profit



    def to_dict(self):

        return {

            "symbol": self.symbol,

            "report_title": self.report_title,

            "sales": self.sales,

            "gross_profit": self.gross_profit,

            "operating_profit": self.operating_profit,

            "net_profit": self.net_profit

        }