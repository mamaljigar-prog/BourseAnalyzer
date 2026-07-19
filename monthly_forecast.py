# monthly_forecast.py

def forecast_from_monthly(data):
    """
    پیش بینی فروش سالانه بر اساس فروش ماه های سپری شده
    """

    months_passed = data["months_passed"]
    sales_so_far = data["sales_so_far"]

    if months_passed == 0:
        return 0

    average_monthly_sales = sales_so_far / months_passed

    forecast_sales = average_monthly_sales * 12

    return round(forecast_sales)


# --------------------------
# تست اولیه
# --------------------------

if __name__ == "__main__":

    data = {
        "months_passed": 6,
        "sales_so_far": 75000000
    }

    result = forecast_from_monthly(data)

    print("===================")
    print("MONTHLY FORECAST")
    print("===================")

    print("Sales Forecast:", result)