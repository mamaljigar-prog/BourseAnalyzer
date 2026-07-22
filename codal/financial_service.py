from codal.codal_adapter import CodalAdapter
from codal.report_selector import ReportSelector
from codal.codal_profit_loss_parser import CodalProfitLossParser
from codal.financial_mapper import FinancialMapper
from codal.balance_sheet_parser import BalanceSheetParser

from financial.financial_statement import FinancialStatement



class FinancialService:


    def __init__(self, symbol):

        self.symbol = symbol



    def get_financial_data(self):


        # ==========================
        # 1- دریافت گزارش‌ها
        # ==========================

        adapter = CodalAdapter(
            self.symbol
        )


        financial_reports = adapter.find_financial_reports()

        monthly_reports = adapter.find_monthly_reports()



        # ==========================
        # 2- انتخاب گزارش مناسب
        # ==========================

        selector = ReportSelector(

            financial_reports,

            monthly_reports

        )


        latest_financial = selector.latest_complete_financial()



        if not latest_financial:


            return {

                "error":
                "گزارش صورت مالی کامل پیدا نشد"

            }



        print("================")

        print(
            "LATEST REPORT"
        )

        print(
            latest_financial["title"]
        )



        # ==========================
        # 3- ساخت URL
        # ==========================

        url = (

            "https://codal.ir"

            +

            latest_financial["url"]

        )



        # ==========================
        # 4- استخراج شیت‌ها
        # ==========================

        parser = CodalProfitLossParser(

            url

        )


        sheets = parser.extract_sheets()



        print()

        print(
            "AVAILABLE SHEETS:"
        )


        for sheet in sheets:

            print(

                sheet.get(
                    "title_Fa",
                    ""
                )

            )



        cells = []



        for sheet in sheets:


            title = sheet.get(

                "title_Fa",

                ""

            )


            if (

                "سود" in title

                or

                "عملکرد" in title

                or

                "صورت‌های مالی" in title

                or

                "صورت های مالی" in title

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

                "error":

                "سلول مالی پیدا نشد"

            }



        # ==========================
        # 5- مپ سود و زیان
        # ==========================

        mapper = FinancialMapper(

            cells

        )


        financial_data = mapper.map_financials()



        # ==========================
        # 6- ساخت مدل مالی
        # ==========================

        statement = FinancialStatement(

            financial_data

        )



        # ==========================
        # 7- استخراج ترازنامه
        # ==========================

        balance_parser = BalanceSheetParser(

            url

        )


        balance_data = balance_parser.get_balance_data()



        statement.assets = balance_data.get(

            "assets"

        )


        statement.equity = balance_data.get(

            "equity"

        )


        statement.liabilities = balance_data.get(

            "liabilities"

        )



        return {


            "report":

            latest_financial,


            "statement":

            statement


        }





if __name__ == "__main__":


    service = FinancialService(

        "فزر"

    )


    result = service.get_financial_data()



    print("================")



    if "error" in result:


        print(

            "ERROR:",

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