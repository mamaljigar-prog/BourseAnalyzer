from codal.codal_profit_loss_parser import CodalProfitLossParser


class FinancialAdapter:


    def __init__(self, url):

        self.url = url



    def report(self):

        parser = CodalProfitLossParser(
            self.url
        )


        data = parser.get_financial_data()



        sales = self.extract_value(
            data.get(
                "sales",
                []
            )
        )


        gross_profit = self.extract_value(
            data.get(
                "gross_profit",
                []
            )
        )


        operating_profit = self.extract_value(
            data.get(
                "operating_profit",
                []
            )
        )


        non_operating_income = self.extract_value(
            data.get(
                "non_operating_income",
                []
            )
        )


        net_profit = self.extract_value(
            data.get(
                "net_profit",
                []
            )
        )


        # اگر سود عملیاتی مستقیم در گزارش نبود
        # تخمین محافظه کارانه از سود خالص و غیرعملیاتی

        if operating_profit == 0 and net_profit > 0:

            operating_profit = (
                net_profit -
                non_operating_income
            )



        return {

            "sales":
                sales,


            "gross_profit":
                gross_profit,


            "operating_profit":
                operating_profit,


            "non_operating_income":
                non_operating_income,


            "net_profit":
                net_profit

        }




    def extract_value(
        self,
        rows
    ):


        if not rows:

            return 0



        for row in rows:


            address = row.get(
                "address",
                ""
            )


            if address.startswith(
                "B"
            ):


                value = row.get(
                    "value",
                    0
                )


                try:

                    return int(
                        value
                    )

                except (
                    ValueError,
                    TypeError
                ):

                    pass



        for row in rows:


            value = row.get(
                "value",
                0
            )


            try:

                return int(
                    value
                )


            except (
                ValueError,
                TypeError
            ):

                continue



        return 0