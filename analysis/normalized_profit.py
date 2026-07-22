# analysis/normalized_profit.py


class NormalizedProfitCalculator:
    """
    محاسبه سود نرمال شده

    قوانین پروژه:
    1- سود عملیاتی بعد از مالیات مبنا است.
    2- درآمدهای غیرتکرارشونده حذف می شوند.
    3- درآمد غیرعملیاتی فقط در صورت تکرار لحاظ می شود.
    """

    def __init__(self, tax_rate=0.25):

        self.tax_rate = tax_rate



    def calculate_operating_after_tax(
        self,
        operating_profit
    ):

        return operating_profit * (
            1 - self.tax_rate
        )



    def calculate(
        self,
        financial_data
    ):


        operating_profit = (
            financial_data["operating_profit"]["current"]
        )


        recurring_non_operating = 0


        if "non_operating_income" in financial_data:

            non_operating = financial_data[
                "non_operating_income"
            ]

            if isinstance(non_operating, dict):

                recurring_non_operating = (
                    non_operating.get("current", 0)
                )



        operating_after_tax = (
            self.calculate_operating_after_tax(
                operating_profit
            )
        )



        normalized_profit = (
            operating_after_tax
            +
            recurring_non_operating
        )



        return {

            "operating_profit":
                operating_profit,

            "operating_after_tax":
                operating_after_tax,

            "recurring_non_operating":
                recurring_non_operating,

            "normalized_profit":
                normalized_profit

        }



if __name__ == "__main__":

    sample = {

        "operating_profit": {
            "current": 75110367
        },

        "non_operating_income": {
            "current": 0
        }

    }


    calc = NormalizedProfitCalculator()

    print(
        calc.calculate(sample)
    )