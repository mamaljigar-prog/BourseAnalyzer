# analysis/company_classifier.py


class CompanyClassifier:
    """
    تشخیص نوع ساختار شرکت

    خروجی:
    production
    holding
    subsidiary_based
    bank
    insurance
    unknown
    """

    def __init__(
        self,
        financial_data,
        company_name=""
    ):

        self.data = financial_data or {}
        self.company_name = company_name



    def normalize(self, value):

        if value is None:
            return ""

        return str(value).lower()



    def ratio(
        self,
        a,
        b
    ):

        if not b:
            return 0

        return a / b



    def classify(self):

        reasons = []

        name = self.normalize(
            self.company_name
        )


        sales = self.data.get(
            "sales",
            0
        )

        operating_profit = self.data.get(
            "operating_profit",
            0
        )

        net_profit = self.data.get(
            "net_profit",
            0
        )

        non_operating_income = self.data.get(
            "non_operating_income",
            0
        )

        assets = self.data.get(
            "assets",
            0
        )

        equity = self.data.get(
            "equity",
            0
        )

        liabilities = self.data.get(
            "liabilities",
            0
        )

        investment_assets = self.data.get(
            "investment_assets",
            0
        )



        # -------------------------
        # Bank
        # -------------------------

        bank_words = [
            "بانک",
            "وبملت",
            "وتجارت",
            "وبصادر",
            "ونوین",
            "وپاسار"
        ]


        if any(
            word in name
            for word in bank_words
        ):

            return {
                "type": "bank",
                "confidence": "high",
                "reason": [
                    "bank name pattern detected"
                ]
            }



        # -------------------------
        # Insurance
        # -------------------------

        insurance_words = [
            "بیمه",
            "اتکایی",
            "نوین",
            "البرز",
            "پارسیان"
        ]


        if any(
            word in name
            for word in insurance_words
        ):

            return {
                "type": "insurance",
                "confidence": "high",
                "reason": [
                    "insurance name pattern detected"
                ]
            }



        # -------------------------
        # Holding Detection
        # -------------------------

        non_operating_ratio = self.ratio(
            non_operating_income,
            net_profit
        )


        investment_ratio = self.ratio(
            investment_assets,
            assets
        )


        if non_operating_ratio > 0.5:

            reasons.append(
                "high non operating income"
            )


        if investment_ratio > 0.3:

            reasons.append(
                "high investment assets"
            )


        if reasons:

            return {
                "type": "holding",
                "confidence": "medium",
                "reason": reasons
            }



        # -------------------------
        # Subsidiary Based
        # -------------------------

        consolidated_difference = self.data.get(
            "consolidated_difference",
            0
        )


        if consolidated_difference:

            return {
                "type": "subsidiary_based",
                "confidence": "medium",
                "reason": [
                    "difference between standalone and consolidated data"
                ]
            }



        # -------------------------
        # Production
        # -------------------------

        if (
            sales > 0
            and
            operating_profit > 0
        ):

            return {
                "type": "production",
                "confidence": "medium",
                "reason": [
                    "sales detected",
                    "operating profit detected"
                ]
            }



        return {
            "type": "unknown",
            "confidence": "low",
            "reason": [
                "insufficient financial pattern"
            ]
        }



if __name__ == "__main__":


    classifier = CompanyClassifier(

        {
            "sales": 100000,
            "operating_profit": 30000,
            "net_profit": 25000,
            "non_operating_income": 2000
        },

        "پتروشیمی خراسان"

    )


    print(
        classifier.classify()
    )