import requests


def get_instrument(ins_code):
    url = f"https://cdn.tsetmc.com/api/Instrument/GetInstrument/{ins_code}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        instrument = data["instrument"]

        return {
            "symbol": instrument["lVal18AFC"],
            "company": instrument["lVal30"],
            "shares": instrument["zTitad"],
            "market": instrument["flowTitle"]
        }

    except Exception as e:
        print("خطا در دریافت اطلاعات شرکت:", e)
        return None



def get_price(ins_code):
    url = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{ins_code}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        price = data["closingPriceInfo"]

        return {
            "last_price": price["pDrCotVal"],
            "closing_price": price["pClosing"],
            "volume": price["qTotTran5J"]
        }

    except Exception as e:
        print("خطا در دریافت قیمت:", e)
        return None



if __name__ == "__main__":

    # شپدیس
    ins_code = "20562694899904339"

    info = get_instrument(ins_code)
    price = get_price(ins_code)

    if info and price:

        print("----------------------")
        print("نماد:", info["symbol"])
        print("شرکت:", info["company"])
        print("تعداد سهام:", info["shares"])
        print("بازار:", info["market"])

        print("----------------------")
        print("آخرین قیمت:", price["last_price"])
        print("قیمت پایانی:", price["closing_price"])
        print("حجم معاملات:", price["volume"])

        market_value = price["closing_price"] * info["shares"]

        print("----------------------")
        print("ارزش بازار:", market_value)