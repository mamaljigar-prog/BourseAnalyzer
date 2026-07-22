from codal.financial_mapper import FinancialConceptMapper


class FinancialDataAdapter:


    def __init__(self):

        self.mapper = FinancialConceptMapper()



    def get_latest_two(self, values):

        if not values:

            return {
                "current": 0,
                "previous": 0,
                "current_date": None,
                "previous_date": None
            }


        valid = []


        for item in values:

            value = item.get(
                "value",
                0
            )

            if value != 0:

                valid.append(
                    item
                )


        if not valid:

            return {
                "current": 0,
                "previous": 0,
                "current_date": None,
                "previous_date": None
            }



        current = valid[0]


        previous = (
            valid[1]
            if len(valid) > 1
            else None
        )


        return {

            "current":
                current.get(
                    "value",
                    0
                ),

            "previous":
                previous.get(
                    "value",
                    0
                )
                if previous
                else 0,


            "current_date":
                current.get(
                    "year"
                ),


            "previous_date":
                previous.get(
                    "year"
                )
                if previous
                else None

        }



    def adapt_income_statement(
        self,
        raw_data
    ):


        return {


            "sales":
                self.get_latest_two(
                    raw_data.get(
                        "sales",
                        []
                    )
                ),



            "gross_profit":
                self.get_latest_two(
                    raw_data.get(
                        "gross_profit",
                        []
                    )
                ),



            "operating_profit":
                self.get_latest_two(
                    raw_data.get(
                        "operating_profit",
                        []
                    )
                ),



            "net_profit":
                self.get_latest_two(
                    raw_data.get(
                        "net_profit",
                        []
                    )
                ),



            "non_operating_income":
                self.get_latest_two(
                    raw_data.get(
                        "non_operating_income",
                        []
                    )
                )

        }