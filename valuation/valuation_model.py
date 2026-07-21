def calculate_valuation(
    market_cap,
    forecast_sales,
    forecast_profit,
    equity,
    assets,
    dividend
):
    equity_billion_toman = equity / 10000 if equity else 0
    assets_billion_toman = assets / 10000 if assets else 0

    result = {}

    result["PE"] = (
        round(market_cap / forecast_profit, 2)
        if forecast_profit
        else 0
    )

    result["PS"] = (
        round(market_cap / forecast_sales, 2)
        if forecast_sales
        else 0
    )

    result["PB"] = (
        round(market_cap / equity_billion_toman, 2)
        if equity_billion_toman
        else 0
    )

    result["PA"] = (
        round(market_cap / assets_billion_toman, 2)
        if assets_billion_toman
        else 0
    )

    result["PD"] = (
        round(market_cap / dividend, 2)
        if dividend
        else 0
    )

    return result
