from company import Company
from valuation.valuation_model import calculate_valuation


def main():

    print("==============================")
    print("Bourse Analyzer")
    print("==============================")


    company = Company(
        symbol="خراسان",
        name="پتروشیمی خراسان",
        sales=143134988,
        net_profit=65862967,
        assets=50000000,
        equity=30000000
    )


    months_passed = 9

    forecast_sales = (
        company.sales / months_passed
    ) * 12


    margin = (
        company.net_profit /
        company.sales
    ) * 100


    forecast_profit = (
        forecast_sales *
        margin /
        100
    )


    market_cap = 252959.31


    sales_billion = forecast_sales / 10000
    profit_billion = forecast_profit / 10000


    # اصلاح واحد ترازنامه
    equity_billion = company.equity / 10000
    assets_billion = company.assets / 10000


    dividend_billion = profit_billion * 0.7


    result = calculate_valuation(
        market_cap,
        sales_billion,
        profit_billion,
        equity_billion,
        assets_billion,
        dividend_billion
    )


    print()
    print("==============================")
    print("VALUATION REPORT")
    print("==============================")


    print("Symbol:", company.symbol)
    print("------------------------------")

    print("Market Value:", market_cap)
    print("Forecast Sales:", round(sales_billion,2))
    print("Forecast Profit:", round(profit_billion,2))

    print("------------------------------")

    print("P/E Forward:", result["PE"])
    print("P/S Forward:", result["PS"])
    print("P/B:", result["PB"])
    print("P/A:", result["PA"])
    print("P/D Forward:", result["PD"])

    print("==============================")


if __name__ == "__main__":
    main()