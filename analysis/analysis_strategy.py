class AnalysisStrategy:


    def __init__(
        self,
        company_structure
    ):

        self.company_structure = (
            company_structure or {}
        )

        self.company_type = (
            self.company_structure.get(
                "type",
                "unknown"
            )
        )



    def get_strategy(self):

        if self.company_type == "production":

            return {

                "type": "production",

                "forecast": "sales_margin",

                "valuation": [
                    "PE",
                    "PS",
                    "PB",
                    "PA",
                    "PD"
                ],

                "metrics": [

                    "sales_growth",

                    "profit_growth",

                    "net_margin"

                ]

            }



        if self.company_type == "holding":

            return {

                "type": "holding",

                "forecast": "holding_based",

                "valuation": [

                    "NAV",

                    "PB"

                ],

                "metrics": [

                    "investment_assets",

                    "subsidiary_value"

                ]

            }



        if self.company_type == "bank":

            return {

                "type": "bank",

                "forecast": "banking_based",

                "valuation": [

                    "PB"

                ],

                "metrics": [

                    "loan_quality",

                    "capital_adequacy"

                ]

            }



        if self.company_type == "insurance":

            return {

                "type": "insurance",

                "forecast": "insurance_based",

                "valuation": [

                    "PB",

                    "PE"

                ],

                "metrics": [

                    "premium_growth",

                    "profit_margin"

                ]

            }



        if self.company_type == "subsidiary_based":

            return {

                "type": "subsidiary_based",

                "forecast": "consolidated_based",

                "valuation": [

                    "PE",

                    "PB"

                ],

                "metrics": [

                    "subsidiary_performance"

                ]

            }



        return {

            "type": "unknown",

            "forecast": "generic",

            "valuation": [

                "PE"

            ],

            "metrics": []

        }



if __name__ == "__main__":


    strategy = AnalysisStrategy(

        {

            "type": "production"

        }

    )


    print(
        strategy.get_strategy()
    )