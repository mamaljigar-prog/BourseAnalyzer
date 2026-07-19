# forecast.py


def forecast_sales(
        current_sales,
        growth_rate
):
    """
    پیش بینی فروش
    """

    return current_sales * (1 + growth_rate)



def forecast_profit(
        forecast_sales,
        net_margin
):
    """
    پیش بینی سود خالص
    """

    return forecast_sales * net_margin



def forward_valuation(
        market_cap,
        forecast_sales,
        forecast_profit
):

    result = {}


    result["PE_Forward"] = round(
        market_cap / forecast_profit,
        2
    )


    result["PS_Forward"] = round(
        market_cap / forecast_sales,
        2
    )


    return result