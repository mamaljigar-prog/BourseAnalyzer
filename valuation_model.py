# valuation_model.py

from financial_data import get_financial_data
from tsetmc_data import get_tsetmc_data


def calculate_valuation(
        market_cap,
        sales,
        net_profit,
        assets,
        equity
):

    # تبدیل ریال به میلیارد تومان
    market_cap_toman = market_cap / 10_000_000_000

    sales_billion = sales / 10_000
    profit_billion = net_profit / 10_000
    assets_billion = assets / 10_000
    equity_billion = equity / 10_000


    result = {}


    result["market_cap"] = market_cap_toman

    result["sales"] = sales_billion

    result["net_profit"] = profit_billion


    # نسبت ها

    result["PE"] = round(
        market_cap_toman / profit_billion,
        2
    )


    result["PS"] = round(
        market_cap_toman / sales_billion,
        2
    )


    result["PB"] = round(
        market_cap_toman / equity_billion,
        2
    )


    result["PA"] = round(
        market_cap_toman / assets_billion,
        2
    )


    # سودآوری

    result["net_margin"] = round(
        (net_profit / sales) * 100,
        2
    )


    result["ROA"] = round(
        (net_profit / assets) * 100,
        2
    )


    result["ROE"] = round(
        (net_profit / equity) * 100,
        2
    )


    return result




def main():


    # کد خراسان
    ins_code = "43552974795606067"


    market = get_tsetmc_data(
        ins_code
    )


    financial = get_financial_data()



    result = calculate_valuation(

        market["market_cap"],

        financial["sales"],

        financial["net_profit"],

        financial["assets"],

        financial["equity"]

    )



    print("======================")
    print("تحلیل ارزش گذاری")
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
        result["market_cap"],
        "میلیارد تومان"
    )


    print("----------------------")


    print(
        "فروش:",
        result["sales"],
        "میلیارد تومان"
    )


    print(
        "سود خالص:",
        result["net_profit"],
        "میلیارد تومان"
    )


    print("----------------------")


    print(
        "P/E :",
        result["PE"]
    )

    print(
        "P/S :",
        result["PS"]
    )

    print(
        "P/B :",
        result["PB"]
    )

    print(
        "P/A :",
        result["PA"]
    )


    print("----------------------")


    print(
        "حاشیه سود:",
        result["net_margin"],
        "%"
    )


    print(
        "ROA:",
        result["ROA"],
        "%"
    )


    print(
        "ROE:",
        result["ROE"],
        "%"
    )



if __name__ == "__main__":
    main()