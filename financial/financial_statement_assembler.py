from financial.financial_statement import FinancialStatement


class FinancialStatementAssembler:

    def __init__(self, profit_data=None, balance_data=None):

        self.profit_data = profit_data or {}
        self.balance_data = balance_data or {}


    def build(self):

        data = {}

        data.update(
            self.profit_data
        )

        data.update(
            self.balance_data
        )

        return FinancialStatement(
            data
        )