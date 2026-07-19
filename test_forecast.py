from forecast import *


sales = 143134988

margin = 65862967 / sales


future_sales = forecast_sales(
    sales,
    0.25
)


future_profit = forecast_profit(
    future_sales,
    margin
)


ratios = forward_ratios(
    8735000,
    future_sales,
    future_profit
)


print("فروش پیش بینی:", future_sales)
print("سود پیش بینی:", future_profit)

for k,v in ratios.items():
    print(k,":",v)