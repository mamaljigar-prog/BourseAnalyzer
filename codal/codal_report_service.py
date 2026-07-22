from codal.codal_adapter import CodalAdapter
from codal.report_selector import ReportSelector


class CodalReportService:


    def __init__(
        self,
        symbol
    ):

        self.symbol = symbol

        self.base_url = (
            "https://codal.ir"
        )



    def get_latest_financial_report(self):


        adapter = CodalAdapter(

            self.symbol

        )


        financial_reports = adapter.find_financial_reports()


        monthly_reports = adapter.find_monthly_reports()



        selector = ReportSelector(

            financial_reports,

            monthly_reports

        )



        report = selector.latest_financial()



        if not report:

            raise ValueError(
                "No valid financial report found"
            )



        return report



    def get_report_url(self):


        report = self.get_latest_financial_report()



        url = report.get(

            "url"

        )



        if not url:

            raise ValueError(

                "Invalid report url"

            )



        if url.startswith(
            "http"
        ):

            return url



        return (

            self.base_url +

            url

        )



    def get_sheets(
        self,
        url
    ):


        import requests
        import json



        response = requests.get(

            url,

            headers={

                "User-Agent":

                "Mozilla/5.0"

            },

            timeout=30

        )


        response.raise_for_status()



        text = response.text



        marker = '"sheets":'



        start = text.find(

            marker

        )



        if start == -1:

            raise ValueError(

                "Sheets not found"

            )



        start += len(marker)



        while (

            start < len(text)

            and

            text[start] != "["

        ):

            start += 1



        depth = 0

        end = None



        for index in range(

            start,

            len(text)

        ):


            if text[index] == "[":

                depth += 1



            elif text[index] == "]":

                depth -= 1



            if depth == 0:


                end = index + 1

                break



        if end is None:

            raise ValueError(

                "Invalid sheets json"

            )



        return json.loads(

            text[start:end]

        )



    def select_sheets(
        self,
        url
    ):


        from codal.sheet_selector import SheetSelector



        sheets = self.get_sheets(

            url

        )


        selector = SheetSelector(

            sheets

        )


        return selector.report()