from market_data.tsetmc_client import TsetmcClient



def calculate_market_value(shares, closing_price):
    """
    ارزش بازار به میلیارد تومان

    shares:
        تعداد سهام شرکت

    closing_price:
        قیمت پایانی به ریال
    """

    market_value = (
        shares * closing_price
    ) / 10_000_000_000


    return market_value




if __name__ == "__main__":


    client = TsetmcClient()


    # شپنا
    ins_code = "7745894403636165"


    data = client.get_market_snapshot(
        ins_code
    )


    value = calculate_market_value(
        data["shares"],
        data["closing_price"]
    )


    print({

        "symbol":
            data["symbol"],


        "name":
            data["name"],


        "shares":
            data["shares"],


        "closing_price":
            data["closing_price"],


        "market_value_billion_toman":
            round(value, 2)

    })