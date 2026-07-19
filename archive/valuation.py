# valuation.py

def calculate_valuation(
        market_cap,
        forecast_sales,
        forecast_profit,
        assets,
        equity
):

    result = {}


    # P/E Forward
    if forecast_profit:
        result["P/E Forward"] = (
            market_cap / forecast_profit
        )
    else:
        result["P/E Forward"] = None



    # P/S Forward
    if forecast_sales:
        result["P/S Forward"] = (
            market_cap / forecast_sales
        )
    else:
        result["P/S Forward"] = None



    # P/A
    if assets:
        result["P/A"] = (
            market_cap / assets
        )
    else:
        result["P/A"] = None



    # P/B
    if equity:
        result["P/B"] = (
            market_cap / equity
        )
    else:
        result["P/B"] = None



    # حاشیه سود خالص
    if forecast_sales:
        result["Net Margin %"] = (
            forecast_profit /
            forecast_sales * 100
        )
    else:
        result["Net Margin %"] = None


    return result



# تست اولیه
if __name__ == "__main__":


    # نمونه بنیرو (اعداد میلیارد تومان)

    market_cap = 8735

    forecast_sales = 6824

    forecast_profit = 2399

    assets = 10900

    equity = 6800



    data = calculate_valuation(
        market_cap,
        forecast_sales,
        forecast_profit,
        assets,
        equity
    )


    print("===================")
    print("VALUATION REPORT")
    print("===================")


    for key, value in data.items():

        if value is not None:
            print(
                key,
                ":",
                round(value,2)
            )

        else:
            print(
                key,
                ": اطلاعات کافی نیست"
            )