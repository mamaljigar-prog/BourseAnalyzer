from codal.codal_adapter import CodalAdapter
from codal.report_selector import ReportSelector
from codal.codal_profit_loss_parser import CodalProfitLossParser
from codal.financial_mapper import FinancialMapper
from codal.balance_sheet_parser import BalanceSheetParser
from codal.sheet_loader import CodalSheetLoader
from codal.sheet_selector import SheetSelector

from financial.financial_statement_assembler import FinancialStatementAssembler


class FinancialService:


    def __init__(self, symbol):

        self.symbol = symbol



    def build_url(self, report):

        return (
            "https://codal.ir"
            +
            report["url"]
        )



    def get_financial_data(self):

        adapter = CodalAdapter(
            self.symbol
        )


        financial_reports = adapter.find_financial_reports()

        monthly_reports = adapter.find_monthly_reports()



        selector = ReportSelector(
            financial_reports,
            monthly_reports
        )



        latest_financial = selector.latest_complete_financial()



        if not latest_financial:

            return {
                "error": "گزارش مالی پیدا نشد"
            }



        print("================")
        print("LATEST REPORT")
        print(
            latest_financial["title"]
        )



        url = self.build_url(
            latest_financial
        )



        sheets = CodalSheetLoader(
            url
        ).get_sheet_options()



        selected_sheets = SheetSelector(
            sheets
        ).report()



        income_sheet = selected_sheets.get(
            "income_statement"
        )


        balance_sheet = selected_sheets.get(
            "balance_sheet"
        )



        if not income_sheet:

            return {
                "error": "شیت سود و زیان پیدا نشد"
            }



        # -------------------------
        # سود و زیان
        # -------------------------

        profit_parser = CodalProfitLossParser(
            income_sheet["url"]
        )


        cells = profit_parser.get_cells()



        mapper = FinancialMapper(
            cells
        )


        profit_data = mapper.map_financials()



        # -------------------------
        # ترازنامه
        # -------------------------

        balance_data = {

            "assets": 0,
            "equity": 0,
            "liabilities": 0

        }



        if balance_sheet:

            try:

                balance_parser = BalanceSheetParser(
                    balance_sheet["url"]
                )


                balance_data = balance_parser.get_balance_data()


            except Exception as e:

                print(
                    "Balance Error:",
                    e
                )



        # -------------------------
        # ترکیب نهایی
        # -------------------------

        statement = FinancialStatementAssembler(
            profit_data,
            balance_data
        ).build()



        return {

            "report": latest_financial,

            "statement": statement

        }



if __name__ == "__main__":


    service = FinancialService(
        "خراسان"
    )


    result = service.get_financial_data()



    print("================")



    if "error" in result:

        print(
            result["error"]
        )

    else:

        print(
            result["statement"].to_dict()
        )