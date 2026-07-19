# forecast.py


def forecast_sales(current_sales, growth_rate):

    return round(
        current_sales * (1 + growth_rate)
    )



def forecast_profit(forecast_sales, net_margin):

    return round(
        forecast_sales * net_margin
    )



def forward_ratios(
        market_cap,
        forecast_sales,
        forecast_profit
):

    result = {}


    if forecast_profit > 0:

        result["P/E Forward"] = round(
            market_cap / forecast_profit,
            2
        )


    if forecast_sales > 0:

        result["P/S Forward"] = round(
            market_cap / forecast_sales,
            2
        )


    return result