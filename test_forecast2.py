from forecast import *


current_sales = 143134988

growth = 0.25

sales = forecast_sales(
    current_sales,
    growth
)


margin = 0.46


profit = forecast_profit(
    sales,
    margin
)


print("================")
print("فروش پیش بینی:", sales)
print("سود پیش بینی:", profit)

print(
    "حاشیه سود:",
    calculate_margin(profit,sales)*100,
    "%"
)