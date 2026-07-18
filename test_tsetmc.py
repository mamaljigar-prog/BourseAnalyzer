from tsetmc_adapter import TsetmcAdapter



stock = TsetmcAdapter(

    "شپدیس"

)



data = stock.get_stock_data()



print("----------------")

print("نماد:", data["symbol"])

print("شرکت:", data["company"])

print("تعداد سهام:", data["shares"])

print("قیمت پایانی:", data["closing_price"])

print("ارزش بازار:", data["market_value"])

print("----------------")