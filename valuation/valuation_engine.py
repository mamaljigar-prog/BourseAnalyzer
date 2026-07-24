from typing import Any, Dict


class ValuationEngine:
    """
    Main valuation engine.

    Calculates:
        PE Forward
        PS Forward
        PB
        PA
        PD

    Includes valuation debug output:
        - Market Cap
        - Forecast Profit
        - Forecast Sales
        - Assets
        - Equity
        - Converted values
        - Final calculation inputs
    """


    def __init__(
        self,
        company: Any,
        forecast: Dict[str, Any],
        analysis_strategy: Any = None,
        base_pe: float = 7
    ):

        self.company = company
        self.forecast = forecast
        self.analysis_strategy = analysis_strategy
        self.base_pe = base_pe



    def _to_billion_toman(self, value):

        """
        Convert million rial to billion toman.

        1 billion toman = 10,000 million rial
        """

        if value is None:
            return 0

        try:
            return float(value) / 10000

        except Exception:

            return 0



    def _safe_divide(self, a, b):

        if b in (0, None):

            return 0

        try:

            return round(
                float(a) / float(b),
                2
            )

        except Exception:

            return 0



    def _debug_valuation_inputs(
        self,
        market_cap,
        forecast_profit,
        forecast_sales,
        assets,
        equity,
        forecast_profit_toman,
        forecast_sales_toman,
        assets_toman,
        equity_toman
    ):


        print()

        print("==============================")
        print("DEBUG VALUATION INPUTS")
        print("==============================")


        print(
            f"Market Cap: {market_cap}"
        )


        print(
            f"Forecast Profit Raw: {forecast_profit}"
        )


        print(
            f"Forecast Sales Raw: {forecast_sales}"
        )


        print(
            f"Assets Raw: {assets}"
        )


        print(
            f"Equity Raw: {equity}"
        )


        print("------------------------------")


        print(
            f"Forecast Profit Billion Toman: {forecast_profit_toman}"
        )


        print(
            f"Forecast Sales Billion Toman: {forecast_sales_toman}"
        )


        print(
            f"Assets Billion Toman: {assets_toman}"
        )


        print(
            f"Equity Billion Toman: {equity_toman}"
        )


        print("------------------------------")


        print(
            "PE = Market Cap / Forecast Profit"
        )


        print(
            "PB = Market Cap / Equity"
        )


        print(
            "PA = Market Cap / Assets"
        )


        print("==============================")

        print()



    def run(self):


        market_cap = float(

            getattr(
                self.company,
                "market_cap",
                0
            )
            or 0

        )



        forecast_profit = self.forecast.get(

            "forecast_profit",

            getattr(
                self.company,
                "net_profit",
                0
            )

        )



        forecast_sales = self.forecast.get(

            "forecast_sales",

            getattr(
                self.company,
                "sales",
                0
            )

        )



        assets = getattr(

            self.company,

            "assets",

            0

        )



        equity = getattr(

            self.company,

            "equity",

            0

        )



        forecast_profit_toman = self._to_billion_toman(

            forecast_profit

        )


        forecast_sales_toman = self._to_billion_toman(

            forecast_sales

        )


        assets_toman = self._to_billion_toman(

            assets

        )


        equity_toman = self._to_billion_toman(

            equity

        )



        self._debug_valuation_inputs(

            market_cap,

            forecast_profit,

            forecast_sales,

            assets,

            equity,

            forecast_profit_toman,

            forecast_sales_toman,

            assets_toman,

            equity_toman

        )



        pe = self._safe_divide(

            market_cap,

            forecast_profit_toman

        )



        ps = self._safe_divide(

            market_cap,

            forecast_sales_toman

        )



        pb = self._safe_divide(

            market_cap,

            equity_toman

        )



        pa = self._safe_divide(

            market_cap,

            assets_toman

        )



        pd = 0



        if forecast_profit_toman:

            target_market_cap = (

                forecast_profit_toman *

                self.base_pe

            )

        else:

            target_market_cap = 0



        upside = 0


        if market_cap:

            upside = round(

                (

                    (

                        target_market_cap -

                        market_cap

                    )

                    /

                    market_cap

                )

                *

                100,

                2

            )



        return {


            "PE": pe,

            "PS": ps,

            "PB": pb,

            "PA": pa,

            "PD": pd,


            "target_market_cap":

                round(

                    target_market_cap,

                    2

                ),


            "upside":

                upside,


            "forward_profit":

                round(

                    forecast_profit_toman,

                    2

                ),


            "forward_sales":

                round(

                    forecast_sales_toman,

                    2

                )

        }