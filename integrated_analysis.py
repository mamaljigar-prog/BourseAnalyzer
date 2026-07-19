# integrated_analysis.py

from company_data import company

from forecast import (
    forecast_sales,
    forecast_profit
)


symbol = company["symbol"]


sales = company["sales"]

profit = company["profit"]


margin = profit / sales


growth_rate = 0.25


forecast_sales_value = forecast_sales(
    sales,
    growth_rate
)


forecast_profit_value = forecast_profit(
    forecast_sales_value,
    margin
)


market_cap = company["market_cap"] / 10


sales_toman = forecast_sales_value * 1000000 / 10

profit_toman = forecast_profit_value * 1000000 / 10


assets = company["assets"] * 1000000 / 10

equity = company["equity"] * 1000000 / 10



print("======================")
print("تحلیل نهایی", symbol)
print("======================")


print(
    "ارزش بازار:",
    round(market_cap/1e9,2),
    "میلیارد تومان"
)


print("----------------------")


print(
    "فروش پیش بینی:",
    round(sales_toman/1e9,2),
    "میلیارد تومان"
)


print(
    "سود پیش بینی:",
    round(profit_toman/1e9,2),
    "میلیارد تومان"
)


print("----------------------")


print(
    "P/E Forward:",
    round(market_cap/profit_toman,2)
)


print(
    "P/S Forward:",
    round(market_cap/sales_toman,2)
)


print(
    "P/B:",
    round(market_cap/equity,2)
)


print(
    "P/A:",
    round(market_cap/assets,2)
)


print("----------------------")


print(
    "حاشیه سود:",
    round(margin*100,2),
    "%"
)


print("======================")