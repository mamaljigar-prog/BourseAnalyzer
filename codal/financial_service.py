# codal/financial_service.py

from codal.codal_adapter import CodalAdapter
from codal.report_selector import ReportSelector
from codal.codal_profit_loss_parser import CodalProfitLossParser
from codal.financial_mapper import FinancialMapper
from codal.balance_sheet_parser import BalanceSheetParser

from financial.financial_statement import FinancialStatement


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
                "error": "گزارش صورت مالی پیدا نشد"
            }


        print("================")
        print("LATEST REPORT")
        print(
            latest_financial["title"]
        )


        url = self.build_url(
            latest_financial
        )


        # -------------------------
        # سود و زیان
        # -------------------------

        profit_parser = CodalProfitLossParser(
            url
        )


        sheets = profit_parser.extract_sheets()


        cells = []


        print()
        print("AVAILABLE SHEETS:")


        for sheet in sheets:

            title = sheet.get(
                "title_Fa",
                ""
            )

            print(title)


            if (
                "سود" in title
                or
                "عملکرد" in title
                or
                "صورت‌های مالی" in title
            ):

                for table in sheet.get(
                    "tables",
                    []
                ):

                    cells.extend(
                        table.get(
                            "cells",
                            []
                        )
                    )


        if not cells:

            return {
                "error": "سلول مالی پیدا نشد"
            }


        mapper = FinancialMapper(
            cells
        )


        financial_data = mapper.map_financials()



        statement = FinancialStatement(
            financial_data
        )



        # -------------------------
        # ترازنامه
        # -------------------------

        balance_data = {

            "assets": 0,
            "equity": 0,
            "liabilities": 0

        }


        try:

            balance_parser = BalanceSheetParser(
                url
            )


            balance_data = balance_parser.get_balance_data()


        except Exception as e:

            print(
                "Balance Error:",
                e
            )



        statement.assets = balance_data.get(
            "assets",
            0
        )


        statement.equity = balance_data.get(
            "equity",
            0
        )


        statement.liabilities = balance_data.get(
            "liabilities",
            0
        )



        return {

            "report": latest_financial,

            "statement": statement

        }



if __name__ == "__main__":


    service = FinancialService(
        "فزر"
    )


    result = service.get_financial_data()



    print("================")


    if "error" in result:

        print(
            result["error"]
        )

    else:

        print(
            result["report"]
        )

        print("================")

        print(
            result["statement"].to_dict()
        )