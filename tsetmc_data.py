# tsetmc_data.py

import requests


BASE_URL = "https://cdn.tsetmc.com/api"


def get_tsetmc_data(ins_code):

    result = {}

    try:

        # اطلاعات شرکت
        url = f"{BASE_URL}/Instrument/GetInstrument/{ins_code}"

        r = requests.get(
            url,
            timeout=10
        )

        data = r.json()

        instrument = data.get("instrument")


        if instrument:

            result["symbol"] = instrument.get("lVal18AFC")
            result["company"] = instrument.get("lVal30")
            result["shares"] = int(
                instrument.get("zTitad",0)
            )

        else:

            return None



        # قیمت

        url = f"{BASE_URL}/ClosingPrice/GetClosingPriceInfo/{ins_code}"


        r = requests.get(
            url,
            timeout=10
        )


        data = r.json()


        price = data.get(
            "closingPriceInfo"
        )


        if price:

            last_price = int(
                price.get("pDrCotVal",0)
            )

            result["price"] = last_price


            result["market_cap"] = (
                result["shares"]
                *
                last_price
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