from financial.financial_statement_assembler import FinancialStatementAssembler


class FinancialService:

    def build_statement(self, profit_data=None, balance_data=None):

        assembler = FinancialStatementAssembler(
            profit_data,
            balance_data
        )

        return assembler.build()