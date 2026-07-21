from models.company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData

from codal.financial_adapter import FinancialAdapter

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


    closing = api.get_closing_price(
        ins_code
    )


    info = api.get_instrument_info(
        ins_code
    )


    market = MarketData(
        closing,
        info
    )


    live = market.report()



    # ==========================
    # CODAL DATA
    # ==========================

    codal_url = (
        "https://codal.ir/Reports/Decision.aspx?"
        "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"
        "&rt=0&let=6&ct=0&ft=-1&sheetId=1"
    )


    financial = FinancialAdapter(
        codal_url
    )


    data = financial.report()



    # ==========================
    # COMPANY
    # ==========================

    company = Company(

        name="پتروشیمی خراسان",

        symbol=live["symbol"],

        sales=data["sales"],

        operating_profit=data["operating_profit"],

        net_profit=data["net_profit"],

        assets=50000000,

        equity=30000000,

        market_cap=live["market_cap"]

    )



    # ==========================
    # FORECAST
    # ==========================


    months_passed = 9


    forecast_sales = (
        company.sales /
        months_passed
    ) * 12



    margin = (
        company.net_profit /
        company.sales
    )


    forecast_profit = (
        forecast_sales *
        margin
    )



    print()

    print("==============================")
    print("FORECAST REPORT")
    print("==============================")


    print(
        "Company:",
        company.name
    )


    print(
        "Symbol:",
        company.symbol
    )


    print(
        "Current Sales:",
        company.sales
    )


    print(
        "Forecast Sales:",
        round(forecast_sales)
    )


    print(
        "Current Profit:",
        company.net_profit
    )


    print(
        "Forecast Profit:",
        round(forecast_profit)
    )



    # ==========================
    # VALUATION
    # ==========================


    sales_billion = forecast_sales / 10000

    profit_billion = forecast_profit / 10000


    dividend = 11570



    result = calculate_valuation(

        market_cap=company.market_cap,

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
        "Market Cap:",
        company.market_cap
    )


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