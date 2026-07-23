from valuation.valuation_model import calculate_valuation


class ValuationEngine:
    """
    موتور ارزشگذاری

    قوانین:
    - P/E از TSETMC استفاده نمی‌شود.
    - P/E = Market Cap / Forecast Profit
    - ارزش هدف = سود پیش‌بینی شده × PE پایه
    - PE پایه پیش‌فرض = 7
    """


    def __init__(
        self,
        company=None,
        forecast=None,
        strategy=None,
        base_pe=7
    ):

        self.company = company
        self.forecast = forecast or {}
        self.strategy = strategy or {}
        self.base_pe = base_pe



    def calculate_forward_pe(
        self,
        market_cap,
        forecast_profit
    ):

        if forecast_profit <= 0:
            return None

        return round(
            market_cap / forecast_profit,
            2
        )



    def calculate_forward_ps(
        self,
        market_cap,
        forecast_sales
    ):

        if forecast_sales <= 0:
            return None

        return round(
            market_cap / forecast_sales,
            2
        )



    def target_market_cap(
        self,
        forecast_profit
    ):

        return (
            forecast_profit *
            self.base_pe
        )



    def upside(
        self,
        target,
        current
    ):

        if current <= 0:
            return None

        return round(
            (
                target-current
            )
            /
            current
            *
            100,
            2
        )



    def production_valuation(self):


        forecast_profit = (
            self.forecast["forecast_profit"]
            /
            10000
        )


        forecast_sales = (
            self.forecast["forecast_sales"]
            /
            10000
        )


        result = calculate_valuation(

            market_cap=self.company.market_cap,

            forecast_sales=forecast_sales,

            forecast_profit=forecast_profit,

            equity=self.company.equity,

            assets=self.company.assets,

            dividend=11570

        )


        target = self.target_market_cap(
            forecast_profit
        )


        result.update({

            "target_market_cap_pe7":
                target,

            "upside_percent":
                self.upside(
                    target,
                    self.company.market_cap
                )

        })


        return result



    def run(self):


        company_type = self.strategy.get(
            "type",
            "production"
        )


        if company_type == "production":

            return self.production_valuation()


        return self.production_valuation()