# tsetmc_data.py

import requests


BASE_URL = "https://cdn.tsetmc.com/api"



def get_tsetmc_data(ins_code):

    result = {}

    try:

        # اطلاعات شرکت
        url = f"{BASE_URL}/Instrument/GetInstrument/{ins_code}"

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        instrument = data.get("instrument")


        if not instrument:
            return None


        result["symbol"] = instrument.get(
            "lVal18AFC"
        )

        result["company"] = instrument.get(
            "lVal30"
        )


        result["shares"] = int(
            instrument.get(
                "zTitad",
                0
            )
        )



        # قیمت پایانی

        url = (
            f"{BASE_URL}/ClosingPrice/"
            f"GetClosingPriceInfo/{ins_code}"
        )


        response = requests.get(
            url,
            timeout=10
        )


        data = response.json()


        closing = data.get(
            "closingPriceInfo"
        )


        if not closing:
            return None



        price = int(
            closing.get(
                "pDrCotVal",
                0
            )
        )


        result["price"] = price



        # ارزش بازار
        # تبدیل ریال به میلیارد تومان

        result["market_cap"] = round(
            (
                result["shares"]
                *
                price
            )
            /
            10_000_000_000,
            2
        )



        return result



    except Exception as e:

        print(
            "خطا در TSETMC:",
            e
        )

        return None




if __name__ == "__main__":


    data = get_tsetmc_data(
        "20562694899904339"
    )


    print(data)