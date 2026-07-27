from codal.codal_profit_loss_parser import CodalProfitLossParser


class FinancialAdapter:

    def __init__(self, url):

        self.url = url


    def report(self):

        parser = CodalProfitLossParser(
            self.url
        )

        data = parser.get_financial_data()


        current = self.build_period(
            data,
            "current_period"
        )

        previous = self.build_period(
            data,
            "comparable_period"
        )

        annual = self.build_period(
            data,
            "annual"
        )


        period_months = self.calculate_period_months(
            current
        )


        return {

            # =========================
            # Canonical financial periods
            # =========================

            "current":
                current,

            "previous":
                previous,

            "annual":
                annual,


            # =========================
            # Comparable analysis layer
            # =========================

            "comparison": {

                "current":
                    current,

                "previous":
                    previous

            },


            # =========================
            # Compatibility layer
            # AnalyzerEngine consumes these
            # =========================

            "sales":
                current.get(
                    "sales",
                    0
                ),


            "gross_profit":
                current.get(
                    "gross_profit",
                    0
                ),


            "operating_profit":
                current.get(
                    "operating_profit",
                    0
                ),


            "non_operating_income":
                current.get(
                    "non_operating_income",
                    0
                ),


            "net_profit":
                current.get(
                    "net_profit",
                    0
                ),


            "report_period_end":
                current.get(
                    "report_period_end"
                ),


            "fiscal_year_end":
                current.get(
                    "fiscal_year_end"
                ),


            "period_months":
                period_months,


            "duration_months":
                period_months,


            "period_type":
                self.classify_period(
                    period_months
                )

        }



    def build_period(
        self,
        data,
        period_key
    ):

        result = {}


        concepts = [

            "sales",

            "gross_profit",

            "operating_profit",

            "non_operating_income",

            "net_profit"

        ]


        for concept in concepts:

            concept_data = data.get(
                concept,
                {}
            )

            period = concept_data.get(
                period_key,
                {}
            )


            result[concept] = self.extract_value(
                period
            )


            if concept == "sales":

                result["report_period_end"] = (
                    period.get(
                        "report_period_end"
                    )
                )

                result["fiscal_year_end"] = (
                    period.get(
                        "fiscal_year_end"
                    )
                )


        return result



    def extract_value(
        self,
        period
    ):

        if not period:

            return 0


        value = period.get(
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

            return 0



    def calculate_period_months(
        self,
        current
    ):

        period_end = current.get(
            "report_period_end"
        )


        if not period_end:

            return None


        try:

            parts = str(
                period_end
            ).split("/")


            return int(
                parts[1]
            )


        except Exception:

            return None



    def classify_period(
        self,
        months
    ):

        if months is None:

            return None


        if months <= 3:

            return "3M"


        if months <= 6:

            return "6M"


        if months <= 9:

            return "9M"


        return "12M"