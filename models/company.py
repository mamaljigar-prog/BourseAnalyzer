class Company:


    def __init__(
        self,
        name,
        symbol,
        sales,
        operating_profit,
        net_profit,
        assets,
        equity,
        market_cap,
        non_operating_income=0,
        industry="",
        period_months=12,

        # Historical financial data
        previous_sales=0,
        previous_gross_profit=0,
        previous_operating_profit=0,
        previous_net_profit=0,
        previous_non_operating_income=0,

        annual_previous_sales=0,
        annual_previous_gross_profit=0,
        annual_previous_operating_profit=0,
        annual_previous_net_profit=0,
        annual_previous_non_operating_income=0
    ):


        self.name = name

        self.symbol = symbol

        self.industry = industry


        # =========================
        # Current Financial Data
        # =========================

        self.sales = sales

        self.operating_profit = operating_profit

        self.net_profit = net_profit

        self.non_operating_income = (
            non_operating_income
        )


        # =========================
        # Previous Comparable Period
        # =========================

        self.previous_sales = previous_sales

        self.previous_gross_profit = (
            previous_gross_profit
        )

        self.previous_operating_profit = (
            previous_operating_profit
        )

        self.previous_net_profit = (
            previous_net_profit
        )

        self.previous_non_operating_income = (
            previous_non_operating_income
        )


        # =========================
        # Previous Full Year
        #
        # Used only for:
        # - comparison
        # - growth analysis
        # - quality checks
        # =========================

        self.annual_previous_sales = (
            annual_previous_sales
        )

        self.annual_previous_gross_profit = (
            annual_previous_gross_profit
        )

        self.annual_previous_operating_profit = (
            annual_previous_operating_profit
        )

        self.annual_previous_net_profit = (
            annual_previous_net_profit
        )

        self.annual_previous_non_operating_income = (
            annual_previous_non_operating_income
        )


        # =========================
        # Balance Sheet Data
        # =========================

        self.assets = assets

        self.equity = equity


        # =========================
        # Market Data
        # =========================

        self.market_cap = market_cap


        # =========================
        # Report Period
        # =========================

        self.period_months = period_months