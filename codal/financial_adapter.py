from codal.codal_profit_loss_parser import CodalProfitLossParser


class FinancialAdapter:

    def __init__(self, url):

        self.url = url

    def report(self):

        parser = CodalProfitLossParser(
            self.url
        )

        data = parser.get_financial_data()

        result = {

            "sales":
                self.extract_value(
                    data["sales"]
                ),

            "gross_profit":
                self.extract_value(
                    data["gross_profit"]
                ),

            "operating_profit":
                self.extract_value(
                    data["operating_profit"]
                ),

            "net_profit":
                self.extract_value(
                    data["net_profit"]
                )

        }

        return result

    def extract_value(self, rows):

        for row in rows:

            if row["address"].startswith("B"):

                try:

                    return int(
                        row["value"]
                    )

                except (ValueError, TypeError):

                    return 0

        return 0