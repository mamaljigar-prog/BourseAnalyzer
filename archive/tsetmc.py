import requests


BASE_URL = "https://cdn.tsetmc.com/api"


def get_instrument(ins_code):

    url = f"{BASE_URL}/Instrument/GetInstrument/{ins_code}"

    response = requests.get(url, timeout=10)

    data = response.json()

    instrument = data.get("instrument")

    if not instrument:
        return None

    return {
        "symbol": instrument.get("lVal18AFC"),
        "company": instrument.get("lVal30"),
        "shares": int(instrument.get("zTitad",0)),
        "market": instrument.get("flowTitle")
    }



def get_price(ins_code):

    url = f"{BASE_URL}/ClosingPrice/GetClosingPriceInfo/{ins_code}"

    response = requests.get(url, timeout=10)

    data = response.json()

    price = data.get("closingPriceInfo")

    if not price:
        return None

    return {
        "last_price": int(price.get("pDrCotVal",0)),
        "closing_price": int(price.get("pClosing",0)),
        "volume": int(price.get("qTotTran5J",0))
    }



def calculate_market_cap(shares, price):

    return shares * price



if __name__ == "__main__":


    # خراسان
    ins_code = "43552974795606067"


    info = get_instrument(ins_code)

    price = get_price(ins_code)



    print("======================")

    if info:

        print("نماد :", info["symbol"])
        print("شرکت :", info["company"])
        print("تعداد سهام :", info["shares"])
        print("بازار :", info["market"])



    print("----------------------")


    if price:

        print("آخرین قیمت :", price["last_price"])
        print("قیمت پایانی :", price["closing_price"])


    print("----------------------")


    if info and price:

        market_cap = calculate_market_cap(
            info["shares"],
            price["last_price"]
        )


        print(
            "ارزش بازار :",
            market_cap
        )


    print("======================")