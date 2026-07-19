import json


def annualize(value, months):
    """
    تبدیل عملکرد دوره به پیش بینی سالانه
    """

    if months == 12:
        return value

    return value * 12 / months



def forecast_profit(data):

    sales = data["sales"]
    net_profit = data["net_profit"]
    months = data["months"]

    # تبدیل به سالانه
    forecast_sales = annualize(sales, months)

    # حاشیه سود واقعی همان دوره
    net_margin = net_profit / sales

    # پیش بینی سود خالص
    forecast_net_profit = forecast_sales * net_margin


    return {

        "months": months,

        "forecast_sales": round(forecast_sales),

        "net_margin_percent":
            round(net_margin * 100, 2),

        "forecast_net_profit":
            round(forecast_net_profit)

    }



with open(
    "codal_data.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)



result = forecast_profit(data)


print("===================")
print("FORECAST REPORT")
print("===================")

print(
    "Report Period:",
    result["months"],
    "Months"
)

print()

print(
    "Forecast Sales:",
    result["forecast_sales"]
)

print()

print(
    "Net Margin %:",
    result["net_margin_percent"]
)

print()

print(
    "Forecast Net Profit:",
    result["forecast_net_profit"]
)