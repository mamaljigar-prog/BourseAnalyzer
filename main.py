from models.company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData

from codal.financial_adapter import FinancialAdapter
from codal.balance_sheet_parser import BalanceSheetParser

from valuation.valuation_model import calculate_valuation


def build_sheet_url(base_url, sheet_id):

    if "sheetId=" in base_url:
        before = base_url.split("sheetId=")[0]
        return before + f"sheetId={sheet_id}"

    separator = "&" if "?" in base_url else "?"

    return base_url + separator + f"sheetId={sheet_id}"


def main():

    print("==============================")
    print("Bourse Analyzer")
    print("==============================")

    ins_code = "43552974795606067"

    api = TSETMCAdapter()

    closing = api.get_closing_price(ins_code)

    info = api.get_instrument_info(ins_code)

    market = MarketData(
        closing,
        info
    )

    live = market.report()


    codal_base_url = (
        "https://codal.ir/Reports/Decision.aspx?"
        "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"
        "&rt=0"
        "&let=6"
        "&ct=0"
        "&ft=-1"
    )


    income_url = build_sheet_url(
        codal_base_url,
        1
    )

    financial = FinancialAdapter(
        income_url
    )

    data = financial.report()


    balance_url = build_sheet_url(
        codal_base_url,
        0
    )

    balance_parser = BalanceSheetParser(
        balance_url
    )

    balance_data = balance_parser.get_balance_data()


    assets = balance_data.get(
        "assets",
        0
    )

    equity = balance_data.get(
        "equity",
        0
    )

    liabilities = balance_data.get(
        "liabilities",
        0
    )

    balance_total = balance_data.get(
        "total",
        0
    )

    balanced = balance_data.get(
        "balanced",
        False
    )


    company = Company(

        name="پتروشیمی خراسان",

        symbol=live["symbol"],

        sales=data["sales"],

        operating_profit=data["operating_profit"],

        net_profit=data["net_profit"],

        assets=assets,

        equity=equity,

        market_cap=live["market_cap"]

    )


    months_passed = 9


    forecast_sales = (
        company.sales /
        months_passed
    ) * 12


    margin = (

        company.net_profit /
        company.sales

    ) if company.sales else 0


    forecast_profit = (

        forecast_sales *
        margin

    )


    sales_growth = (

        (
            forecast_sales -
            company.sales
        )
        /
        company.sales

    ) if company.sales else 0


    profit_growth = (

        (
            forecast_profit -
            company.net_profit
        )
        /
        company.net_profit

    ) if company.net_profit else 0



    debt_to_equity = (

        liabilities /
        equity

    ) if equity else 0



    sales_billion = forecast_sales / 10000

    profit_billion = forecast_profit / 10000


    dividend = 11570


    valuation = calculate_valuation(

        market_cap=company.market_cap,

        forecast_sales=sales_billion,

        forecast_profit=profit_billion,

        equity=company.equity,

        assets=company.assets,

        dividend=dividend

    )


    print()

    print("==============================")
    print("FINAL ANALYSIS REPORT")
    print("==============================")


    print(
        "Company:",
        company.name
    )

    print(
        "Symbol:",
        company.symbol
    )


    print()

    print("PERFORMANCE")

    print(
        "Current Sales:",
        company.sales
    )

    print(
        "Forecast Sales:",
        round(forecast_sales)
    )

    print(
        "Sales Growth:",
        round(
            sales_growth * 100,
            2
        ),
        "%"
    )


    print()

    print("PROFITABILITY")


    print(
        "Current Profit:",
        company.net_profit
    )


    print(
        "Forecast Profit:",
        round(forecast_profit)
    )


    print(
        "Profit Growth:",
        round(
            profit_growth * 100,
            2
        ),
        "%"
    )


    print(
        "Net Margin:",
        round(
            margin * 100,
            2
        ),
        "%"
    )


    print()

    print("BALANCE SHEET")


    print(
        "Assets:",
        assets
    )


    print(
        "Equity:",
        equity
    )


    print(
        "Liabilities:",
        liabilities
    )


    print(
        "Balance Status:",
        "Healthy"
        if balanced
        else "Warning"
    )


    print(
        "Debt / Equity:",
        round(
            debt_to_equity,
            2
        )
    )


    print()

    print("VALUATION")


    print(
        "Market Cap:",
        company.market_cap
    )


    print(
        "P/E Forward:",
        valuation["PE"]
    )


    print(
        "P/S Forward:",
        valuation["PS"]
    )


    print(
        "P/B:",
        valuation["PB"]
    )


    print(
        "P/A:",
        valuation["PA"]
    )


    print(
        "P/D Forward:",
        valuation["PD"]
    )


    print()

    print("ANALYST SUMMARY")


    if balanced:

        print(
            "- Balance sheet status: OK"
        )

    else:

        print(
            "- Balance sheet needs review"
        )


    if margin > 0.3:

        print(
            "- High profitability margin"
        )


    if valuation["PE"] < 7:

        print(
            "- Forward P/E is below base market PE"
        )


if __name__ == "__main__":

    main()