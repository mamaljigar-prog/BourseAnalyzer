# valuation/valuation_engine.py


class ValuationEngine:
    """
    موتور ارزش گذاری

    قوانین پروژه:

    1- P/E از TSETMC استفاده نمی شود.
    2- P/E فقط از Market Cap / Forecast Profit محاسبه می شود.
    3- سود ورودی باید قبلاً نرمال شده باشد.
    4- واحد ورودی ها تومان است.
    """


    def __init__(self, base_pe=7):

        self.base_pe = base_pe



    def calculate_forward_pe(
        self,
        market_cap,
        forecast_profit
    ):

        if forecast_profit <= 0:
            return None

        return market_cap / forecast_profit



    def calculate_forward_ps(
        self,
        market_cap,
        forecast_sales
    ):

        if forecast_sales <= 0:
            return None

        return market_cap / forecast_sales



    def calculate_target_market_cap(
        self,
        forecast_profit
    ):

        return forecast_profit * self.base_pe



    def calculate_upside(
        self,
        target_market_cap,
        current_market_cap
    ):

        if current_market_cap <= 0:
            return None

        return (
            target_market_cap - current_market_cap
        ) / current_market_cap



    def analyze(
        self,
        market_cap,
        forecast_profit,
        forecast_sales
    ):


        forward_pe = self.calculate_forward_pe(

            market_cap,

            forecast_profit

        )


        forward_ps = self.calculate_forward_ps(

            market_cap,

            forecast_sales

        )


        target_market_cap = (
            self.calculate_target_market_cap(
                forecast_profit
            )
        )


        upside = self.calculate_upside(

            target_market_cap,

            market_cap

        )


        return {

            "market_cap": market_cap,

            "forecast_profit": forecast_profit,

            "forecast_sales": forecast_sales,

            "forward_pe": forward_pe,

            "forward_ps": forward_ps,

            "target_market_cap_pe7": target_market_cap,

            "upside": upside

        }



if __name__ == "__main__":


    engine = ValuationEngine()


    print(
        engine.analyze(

            market_cap=87350000000,

            forecast_profit=5633277525,

            forecast_sales=14313498800

        )
    )