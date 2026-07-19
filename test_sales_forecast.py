from forecast.sales_forecast import SalesForecast


sales = 143134988
months = 9
previous_sales = 70072719


forecast = SalesForecast(
    sales,
    months
)


print("==============================")
print("SALES FORECAST")
print("==============================")

print("Current Sales:")
print(sales)

print()

print("Forecast Sales:")
print(
    forecast.forecast()
)

print()

print("Growth vs Same Period Last Year:")
print(
    forecast.growth_vs_previous(previous_sales),
    "%"
)

print("==============================")