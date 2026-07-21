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
    # CODAL BASE URL
    # ==========================

    codal_base_url = (
        "https://codal.ir/Reports/Decision.aspx?"
        "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"
        "&rt=0"
        "&let=6"
        "&ct=0"
        "&ft=-1"
    )

    # ==========================
    # INCOME STATEMENT
    # ==========================

    income_url = build_sheet_url(
        codal_base_url,
        1
    )

    financial = FinancialAdapter(
        income_url
    )

    data = financial.report()

    # ==========================
    # BALANCE SHEET
    # ==========================

    balance_url = build_sheet_url(
        codal_base_url,
        0
    )

    balance_parser = BalanceSheetParser(
        balance_url
    )

    balance_data = (
        balance_parser.get_balance_data()
    )

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

    # ==========================
    # COMPANY
    # ==========================

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

    # ==========================
    # BALANCE SHEET REPORT
    # ==========================

    print()

    print("==============================")
    print("BALANCE SHEET REPORT")
    print("==============================")

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
        "Equity + Liabilities:",
        balance_total
    )

    print(
        "Balanced:",
        balanced
    )

    # ==========================
    # FORECAST
    # ==========================

    months_passed = 9

    if months_passed <= 0:

        raise ValueError(
            "months_passed must be greater than zero"
        )

    forecast_sales = (
        company.sales /
        months_passed
    ) * 12

    if company.sales != 0:

        margin = (
            company.net_profit /
            company.sales
        )

    else:

        margin = 0

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
        round(
            forecast_sales
        )
    )

    print(
        "Current Profit:",
        company.net_profit
    )

    print(
        "Forecast Profit:",
        round(
            forecast_profit
        )
    )

    # ==========================
    # VALUATION
    # ==========================

    sales_billion = (
        forecast_sales /
        10000
    )

    profit_billion = (
        forecast_profit /
        10000
    )

    dividend = 11570

    result = calculate_valuation(
        market_cap=company.market_cap,
        forecast_sales=sales_billion,
        forecast_profit=profit_billion,
        equity=company.equity,
        assets=company.assets,
        dividend=dividend
    )

    # ==========================
    # VALUATION REPORT
    # ==========================

    print()

    print("==============================")
    print("VALUATION REPORT")
    print("==============================")

    print(
        "Market Cap:",
        company.market_cap
    )

    print(
        "Assets:",
        company.assets
    )

    print(
        "Equity:",
        company.equity
    )

    print(
        "Liabilities:",
        liabilities
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


if __name__ == "__main__":

    main()