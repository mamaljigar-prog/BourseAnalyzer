from financial.financial_statement import FinancialStatement


class FinancialStatementAssembler:

    def __init__(
        self,
        profit_data=None,
        balance_data=None
    ):

        self.profit_data = profit_data or {}
        self.balance_data = balance_data or {}


    def build(self):

        statement_data = {}


        # Profit & Loss data
        if isinstance(self.profit_data, dict):

            statement_data.update(
                self.profit_data
            )


        # Balance Sheet data
        if isinstance(self.balance_data, dict):

            statement_data.update(
                self.balance_data
            )


        return FinancialStatement(
            statement_data
        )