from financial.financial_statement_assembler import FinancialStatementAssembler


class FinancialService:

    def __init__(self):
        pass


    def build_statement(
        self,
        profit_data=None,
        balance_data=None
    ):

        assembler = FinancialStatementAssembler(
            profit_data=profit_data,
            balance_data=balance_data
        )

        return assembler.build()