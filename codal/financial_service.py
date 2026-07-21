from codal.codal_adapter import CodalAdapter
from codal.report_selector import ReportSelector
from codal.codal_profit_loss_parser import CodalProfitLossParser
from codal.financial_mapper import FinancialMapper



class FinancialService:


    def __init__(self, symbol):

        self.symbol = symbol



    def get_financial_data(self):


        # ==========================
        # 1- دریافت گزارش‌های کدال
        # ==========================

        adapter = CodalAdapter(
            self.symbol
        )


        financial_reports = adapter.find_financial_reports()

        monthly_reports = adapter.find_monthly_reports()



        # ==========================
        # 2- انتخاب جدیدترین گزارش
        # ==========================

        selector = ReportSelector(

            financial_reports,

            monthly_reports

        )


        latest_financial = selector.latest_financial()



        if not latest_financial:

            return {

                "error":
                "گزارش مالی پیدا نشد"

            }



        print("================")
        print("LATEST REPORT")
        print(latest_financial["title"])



        # ==========================
        # 3- ساخت URL کامل
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
        # 5- مپ هوشمند ردیف‌ها
        # ==========================

        mapper = FinancialMapper(
            cells
        )


        financial_data = mapper.map_financials()



        return {


            "report":

            latest_financial,


            "data":

            financial_data


        }





if __name__ == "__main__":



    service = FinancialService(
        "خراسان"
    )


    result = service.get_financial_data()



    print("================")

    print(result)