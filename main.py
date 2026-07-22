from models.company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData

from codal.financial_adapter import FinancialAdapter
from codal.balance_sheet_parser import BalanceSheetParser

from valuation.valuation_model import calculate_valuation

from analysis.profit_quality import ProfitQualityAnalyzer
from analysis.final_analyzer import FinalAnalyzer
from analysis.report_generator import ReportGenerator



def build_sheet_url(base_url, sheet_id):

    if "sheetId=" in base_url:

        before = base_url.split(
            "sheetId="
        )[0]

        return before + f"sheetId={sheet_id}"


    separator = "&" if "?" in base_url else "?"

    return (
        base_url +
        separator +
        f"sheetId={sheet_id}"
    )



def main():


    print("==============================")
    print("Bourse Analyzer")
    print("==============================")


    ins_code = "43552974795606067"



    # -------------------------
    # Market Data
    # -------------------------

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



    # -------------------------
    # Codal Data
    # -------------------------

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



    # -------------------------
    # Balance Sheet
    # -------------------------

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


    balance_status = (

        "Healthy"

        if balance_data.get(
            "balanced",
            False
        )

        else

        "Warning"

    )



    # -------------------------
    # Company Object
    # -------------------------

    company = Company(

        name="پتروشیمی خراسان",

        symbol=live["symbol"],

        sales=data["sales"],

        operating_profit=data["operating_profit"],

        net_profit=data["net_profit"],

        assets=assets,

        equity=equity,

        market_cap=live["market_cap"],

        non_operating_income=data.get(
            "non_operating_income",
            0
        )

    )



    # -------------------------
    # Forecast
    # -------------------------

    months_passed = 9


    forecast_sales = (

        company.sales /
        months_passed

    ) * 12



    margin = (

        company.net_profit /
        company.sales

        if company.sales

        else 0

    )


    forecast_profit = (

        forecast_sales *
        margin

    )



    # -------------------------
    # Analysis Modules
    # -------------------------

    profit_quality = ProfitQualityAnalyzer(

        company.operating_profit,

        company.net_profit,

        company.non_operating_income

    ).analyze()



    valuation = calculate_valuation(

        market_cap=company.market_cap,

        forecast_sales=forecast_sales / 10000,

        forecast_profit=forecast_profit / 10000,

        equity=company.equity,

        assets=company.assets,

        dividend=11570

    )



    final_analysis = FinalAnalyzer(

        company,

        forecast_sales,

        forecast_profit,

        profit_quality,

        valuation

    ).generate()



    # -------------------------
    # Final Report
    # -------------------------

    report = ReportGenerator().generate(

        company,

        forecast_sales,

        forecast_profit,

        profit_quality,

        valuation,

        liabilities,

        balance_status

    )


    print(report)



if __name__ == "__main__":

    main()