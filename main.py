from company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData

from valuation.valuation_model import calculate_valuation


def main():

    print("==============================")
    print("Bourse Analyzer")
    print("==============================")


    # ==========================
    # TSETMC LIVE
    # ==========================

    ins_code = "43552974795606067"

    api = TSETMCAdapter()

    closing = api.get_closing_price(ins_code)

    info = api.get_instrument_info(ins_code)

    market = MarketData(
        closing,
        info
    )

    live = market.report()


    # ==========================
    # COMPANY
    # ==========================

    company = Company(

        symbol=live["symbol"],

        name="پتروشیمی خراسان",

        sales=143134988,

        net_profit=65862967,

        assets=50000000,

        equity=30000000

    )


    # ==========================
    # FORECAST CURRENT YEAR
    # ==========================

    months_passed = 9


    forecast_sales = (
        company.sales /
        months_passed
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


    print()

    print("==============================")
    print("FORECAST REPORT")
    print("==============================")


    print("Company:", company.name)

    print("Symbol:", company.symbol)

    print("------------------------------")


    print(
        "Current Sales:",
        company.sales
    )


    print(
        "Forecast Sales:",
        round(forecast_sales)
    )


    print(
        "Current Net Profit:",
        company.net_profit
    )


    print(
        "Forecast Net Profit:",
        round(forecast_profit,2)
    )


    print("------------------------------")


    print(
        "Net Margin:",
        round(margin,2),
        "%"
    )


    print("==============================")


    # ==========================
    # VALUATION
    # ==========================


    market_cap = live["market_cap"]


    sales_billion = forecast_sales / 10000

    profit_billion = forecast_profit / 10000


    # سود نقدی فعلا دستی
    dividend = 11570



    result = calculate_valuation(

        market_cap=market_cap,

        forecast_sales=sales_billion,

        forecast_profit=profit_billion,

        equity=company.equity,

        assets=company.assets,

        dividend=dividend

    )


    print()

    print("==============================")
    print("VALUATION REPORT")
    print("==============================")


    print(
        "Symbol:",
        company.symbol
    )


    print("------------------------------")


    print(
        "Market Value:",
        market_cap
    )


    print(
        "Forecast Sales:",
        round(sales_billion,2)
    )


    print(
        "Forecast Profit:",
        round(profit_billion,2)
    )


    print("------------------------------")


    print(
        "P/E Forward:",
        result["PE"]
    )


    print(
        "P/S Forward:",
        result["PS"]
    )


    print(
        "P/B:",
        result["PB"]
    )


    print(
        "P/A:",
        result["PA"]
    )


    print(
        "P/D Forward:",
        result["PD"]
    )


    print("==============================")


if __name__ == "__main__":

    main()