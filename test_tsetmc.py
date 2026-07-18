from tsetmc_adapter import TsetmcAdapter


ins_code = "20562694899904339"


adapter = TsetmcAdapter(ins_code)


data = adapter.get_stock_data()


if data:

    print("----------------")
    print("نماد:", data["symbol"])
    print("شرکت:", data["company"])
    print("تعداد سهام:", data["shares"])
    print("قیمت پایانی:", data["closing_price"])

    print(
        "ارزش بازار:",
        data["market_value_text"]
    )

    print("----------------")

else:

    print("خطا در دریافت اطلاعات")