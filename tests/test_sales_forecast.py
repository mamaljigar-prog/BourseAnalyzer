from forecast.sales_forecast import SalesForecast


sales = 143134988
months = 9


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

print("Months Passed:")
print(months)

print()

print("Monthly Average:")
print(
    forecast.monthly_average()
)

print()

print("Forecast Year Sales:")
print(
    forecast.forecast()
)

print()

print("Growth Report:")

print(
    forecast.growth_report(
        previous_month=12000000,
        last_year_same_month=9000000
    )
)

print("==============================")