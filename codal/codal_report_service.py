from codal.codal_adapter import CodalAdapter
from codal.report_selector import ReportSelector


class CodalReportService:


    def __init__(self, symbol):

        self.symbol = symbol



    def get_latest_financial_report(self):

        adapter = CodalAdapter(
            self.symbol
        )


        financial_reports = (
            adapter.find_financial_reports()
        )


        monthly_reports = (
            adapter.find_monthly_reports()
        )


        selector = ReportSelector(

            financial_reports,

            monthly_reports

        )


        report = selector.latest_financial()


        if report is None:

            raise ValueError(
                "No valid financial report found"
            )


        return report



    def get_report_url(self):

        report = (
            self.get_latest_financial_report()
        )


        url = report.get(
            "url"
        )


        if not url:

            raise ValueError(
                "Financial report URL not found"
            )


        if not url.startswith(
            "http"
        ):

            url = (
                "https://codal.ir"
                +
                url
            )


        return url



if __name__ == "__main__":


    service = CodalReportService(
        "خراسان"
    )


    report = service.get_latest_financial_report()


    print(
        report
    )


    print(
        service.get_report_url()
    )