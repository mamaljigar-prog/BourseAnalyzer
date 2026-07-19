# integrated_report.py


from tsetmc_data import get_tsetmc_data

from financial_data import get_financial_data

from valuation_model import calculate_valuation

from forecast import (
    forecast_sales,
    forecast_profit,
    forward_valuation
)

from growth_model import sales_growth




def main():


    # خراسان

    ins_code = "43552974795606067"



    # اطلاعات بازار

    market = get_tsetmc_data(
        ins_code
    )



    # اطلاعات مالی

    financial = get_financial_data()



    # ارزش گذاری فعلی

    valuation = calculate_valuation(

        market["market_cap"],

        financial["sales"],

        financial["net_profit"],

        financial["assets"],

        financial["equity"]

    )



    # ======================
    # محاسبه رشد فروش
    # ======================


    growth_percent = sales_growth(

        financial["sales"],

        financial["previous_sales"]

    )


    growth_rate = growth_percent / 100



    # حاشیه سود

    net_margin = (

        financial["net_profit"]

        /

        financial["sales"]

    )



    # ======================
    # Forecast
    # ======================


    forecast_sales_value = forecast_sales(

        financial["sales"],

        growth_rate

    )



    forecast_profit_value = forecast_profit(

        forecast_sales_value,

        net_margin

    )



    # تبدیل به میلیارد تومان

    forward = forward_valuation(

        valuation["market_cap"],

        forecast_sales_value / 10000,

        forecast_profit_value / 10000

    )



    # ======================
    # گزارش
    # ======================


    print("======================")

    print("گزارش نهایی خراسان")

    print("======================")



    print(
        "نماد:",
        market["symbol"]
    )


    print(
        "شرکت:",
        market["company"]
    )


    print("----------------------")



    print(
        "ارزش بازار:",
        round(
            valuation["market_cap"],
            2
        ),
        "میلیارد تومان"
    )


    print("----------------------")



    print(
        "فروش فعلی:",
        round(
            financial["sales"] / 10000,
            2
        ),
        "میلیارد تومان"
    )



    print(
        "فروش سال قبل:",
        round(
            financial["previous_sales"] / 10000,
            2
        ),
        "میلیارد تومان"
    )



    print(
        "رشد فروش:",
        growth_percent,
        "%"
    )



    print(
        "فروش پیش بینی:",
        round(
            forecast_sales_value / 10000,
            2
        ),
        "میلیارد تومان"
    )



    print(
        "سود پیش بینی:",
        round(
            forecast_profit_value / 10000,
            2
        ),
        "میلیارد تومان"
    )



    print("----------------------")



    print(
        "P/E Forward:",
        forward["PE_Forward"]
    )


    print(
        "P/S Forward:",
        forward["PS_Forward"]
    )



    print(
        "P/B:",
        valuation["PB"]
    )



    print(
        "P/A:",
        valuation["PA"]
    )



    print("----------------------")



    print(
        "حاشیه سود:",
        valuation["net_margin"],
        "%"
    )


    print(
        "ROA:",
        valuation["ROA"],
        "%"
    )


    print(
        "ROE:",
        valuation["ROE"],
        "%"
    )



    print("======================")




if __name__ == "__main__":

    main()