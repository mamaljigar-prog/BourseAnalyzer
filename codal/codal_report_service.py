import requests

from codal.codal_adapter import CodalAdapter
from codal.report_selector import ReportSelector



class CodalReportService:


    def __init__(self, symbol):

        self.symbol = symbol



    def normalize_url(self, url):

        if not url:

            return None


        if url.startswith("http"):

            return url


        return (
            "https://codal.ir"
            +
            url
        )



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


        report = (
            selector.latest_financial()
        )


        if not report:

            raise ValueError(
                "No valid financial report found"
            )


        report["url"] = self.normalize_url(
            report.get("url")
        )


        return report



    def get_report_url(self):

        report = self.get_latest_financial_report()

        return report.get(
            "url"
        )