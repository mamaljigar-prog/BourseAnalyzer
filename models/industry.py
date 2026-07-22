class Industry:


    def __init__(
        self,
        name
    ):

        self.name = name

        self.companies = []



    def add_company(
        self,
        company
    ):

        self.companies.append(
            company
        )



    def market_cap_ranking(self):

        ranked = sorted(
            self.companies,
            key=lambda x: x.market_cap,
            reverse=True
        )


        result = []


        for index, company in enumerate(
            ranked,
            start=1
        ):

            result.append(
                {
                    "rank": index,
                    "symbol": company.symbol,
                    "name": company.name,
                    "market_cap": company.market_cap
                }
            )


        return result