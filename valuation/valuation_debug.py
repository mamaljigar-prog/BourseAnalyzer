class ValuationDebug:

    @staticmethod
    def print_inputs(
        company,
        forecast,
        market_cap,
        forecast_profit,
        forecast_sales,
        assets,
        equity,
        profit_toman,
        sales_toman,
        assets_toman,
        equity_toman
    ):

        print("\n")
        print("==============================")
        print("DEBUG VALUATION INPUTS")
        print("==============================")

        print("\nCOMPANY")
        print("------------------------------")
        print(
            "Symbol:",
            getattr(company, "symbol", "")
        )

        print(
            "Name:",
            getattr(company, "name", "")
        )


        print("\nRAW VALUES")
        print("------------------------------")

        print(
            "Market Cap:",
            market_cap
        )

        print(
            "Forecast Profit RAW:",
            forecast_profit
        )

        print(
            "Forecast Sales RAW:",
            forecast_sales
        )

        print(
            "Assets RAW:",
            assets
        )

        print(
            "Equity RAW:",
            equity
        )


        print("\nCONVERTED BILLION TOMAN")
        print("------------------------------")

        print(
            "Profit:",
            profit_toman
        )

        print(
            "Sales:",
            sales_toman
        )

        print(
            "Assets:",
            assets_toman
        )

        print(
            "Equity:",
            equity_toman
        )


        print("\nCALCULATED MULTIPLES")
        print("------------------------------")


        if profit_toman:
            print(
                "PE:",
                round(
                    market_cap / profit_toman,
                    2
                )
            )


        if sales_toman:
            print(
                "PS:",
                round(
                    market_cap / sales_toman,
                    2
                )
            )


        if equity_toman:
            print(
                "PB:",
                round(
                    market_cap / equity_toman,
                    2
                )
            )


        if assets_toman:
            print(
                "PA:",
                round(
                    market_cap / assets_toman,
                    2
                )
            )


        print("==============================")