from tsetmc_data import get_market_data
from forecast import forecast_sales, forecast_profit
from valuation_model import calculate_valuation


# کد خراسان
INS_CODE = "43552974795606067"


# داده کدال فعلی
CURRENT_SALES = 143134988
CURRENT_PROFIT = 65862967

# فرض رشد فروش
SALES_GROWTH = 0.25


def main():


    market = get_market_data(INS_CODE)


    if not market:
        print("خطا در دریافت TSETMC")
        return



    forecast_sales_value = forecast_sales(
        CURRENT_SALES,
        SALES_GROWTH
    )


    margin = CURRENT_PROFIT / CURRENT_SALES


    forecast_profit_value = forecast_profit(
        forecast_sales_value,
        margin
    )


    result = calculate_valuation(

        market_cap =
            market["market_cap"],

        forecast_sales =
            forecast_sales_value,

        forecast_profit =
            forecast_profit_value,

        equity =
            95688722,

        assets =
            156582933

    )


    print("======================")
    print("تحلیل نهایی")
    print("======================")

    print(
        "نماد:",
        market["symbol"]
    )

    print(
        "ارزش بازار:",
        round(
            market["market_cap"]/10000000000,
            2
        ),
        "میلیارد تومان"
    )


    print("----------------------")

    print(
        "فروش پیش بینی:",
        round(
            forecast_sales_value/10000,
            2
        ),
        "میلیارد تومان"
    )


    print(
        "سود پیش بینی:",
        round(
            forecast_profit_value/10000,
            2
        ),
        "میلیارد تومان"
    )


    print("----------------------")


    for k,v in result.items():

        print(
            k,
            ":",
            v
        )



if __name__ == "__main__":

    main()