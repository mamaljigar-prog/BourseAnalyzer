import requests


BASE_URL = "https://cdn.tsetmc.com/api"


def get_instrument(ins_code):

    url = f"{BASE_URL}/Instrument/GetInstrument/{ins_code}"

    try:

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()


        # نمایش پاسخ برای بررسی
        # print(data)


        instrument = data.get("instrument")


        if not instrument:
            print("اطلاعات شرکت در پاسخ API پیدا نشد")
            print(data)
            return None


        return {

            "symbol": instrument.get("lVal18AFC"),

            "company": instrument.get("lVal30"),

            "shares": int(
                instrument.get("zTitad",0)
            ),

            "market": instrument.get("flowTitle")

        }


    except Exception as e:

        print(
            "خطا در دریافت اطلاعات شرکت:",
            e
        )

        return None




def get_price(ins_code):


    url = f"{BASE_URL}/ClosingPrice/GetClosingPriceInfo/{ins_code}"


    try:


        response = requests.get(
            url,
            timeout=10
        )


        data = response.json()


        # print(data)


        price = data.get(
            "closingPriceInfo"
        )


        if not price:

            print(
                "اطلاعات قیمت در پاسخ API پیدا نشد"
            )

            print(data)

            return None



        return {


            "last_price":

                price.get(
                    "pDrCotVal",
                    0
                ),


            "closing_price":

                price.get(
                    "pClosing",
                    0
                ),


            "volume":

                price.get(
                    "qTotTran5J",
                    0
                )

        }


    except Exception as e:


        print(
            "خطا در دریافت قیمت:",
            e
        )

        return None





if __name__ == "__main__":


    # شپدیس

    ins_code = "20562694899904339"



    info = get_instrument(
        ins_code
    )


    price = get_price(
        ins_code
    )



    print("================")



    if info:

        print(
            "نماد:",
            info["symbol"]
        )

        print(
            "شرکت:",
            info["company"]
        )

        print(
            "تعداد سهام:",
            info["shares"]
        )

        print(
            "بازار:",
            info["market"]
        )


    print("----------------")



    if price:


        print(
            "آخرین قیمت:",
            price["last_price"]
        )


        print(
            "قیمت پایانی:",
            price["closing_price"]
        )


        print(
            "حجم:",
            price["volume"]
        )


    print("================")