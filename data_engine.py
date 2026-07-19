from tsetmc_data import get_market_data


def load_company(ins_code):

    market = get_market_data(ins_code)


    if not market:
        print("خطا در دریافت اطلاعات بازار")
        return None


    company = {

        "symbol":
            market["symbol"],


        "company":
            market["company"],


        "shares":
            market["shares"],


        "price":
            market["price"],


        "market_cap":
            market["market_cap"],

    }


    return company



if __name__ == "__main__":


    data = load_company(
        "43552974795606067"
    )


    print("================")

    print(
        "نماد:",
        data["symbol"]
    )


    print(
        "شرکت:",
        data["company"]
    )


    print(
        "ارزش بازار:",
        data["market_cap"]
    )

    print("================")