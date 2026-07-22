from models.company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData
from tsetmc.symbol_resolver import SymbolResolver

from codal.codal_report_service import CodalReportService
from codal.financial_adapter import FinancialAdapter
from codal.balance_sheet_parser import BalanceSheetParser

from valuation.valuation_model import calculate_valuation

from analysis.profit_quality import ProfitQualityAnalyzer
from analysis.final_analyzer import FinalAnalyzer
from analysis.report_generator import ReportGenerator



class AnalyzerEngine:


    def __init__(
        self,
        symbol,
        company_name
    ):

        self.symbol = symbol
        self.company_name = company_name



    def build_sheet_url(
        self,
        base_url,
        sheet_id
    ):

        separator = (
            "&"
            if "?" in base_url
            else "?"
        )

        return (
            base_url +
            separator +
            f"sheetId={sheet_id}"
        )



    def run(self):


        # -------------------------
        # Resolve Symbol
        # -------------------------

        resolver = SymbolResolver()


        ins_code = resolver.find_ins_code(
            self.symbol
        )


        if not ins_code:

            raise ValueError(
                "Instrument code not found"
            )



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
        # Codal Report Selection
        # -------------------------

        codal_service = CodalReportService(
            self.symbol
        )


        codal_url = codal_service.get_report_url()



        # -------------------------
        # Financial Data
        # -------------------------

        income_url = self.build_sheet_url(
            codal_url,
            1
        )


        financial = FinancialAdapter(
            income_url
        )


        data = financial.report()



        # -------------------------
        # Balance Sheet
        # -------------------------

        balance_url = self.build_sheet_url(
            codal_url,
            0
        )


        balance_parser = BalanceSheetParser(
            balance_url
        )


        balance = balance_parser.get_balance_data()



        assets = balance.get(
            "assets",
            0
        )


        equity = balance.get(
            "equity",
            0
        )


        liabilities = balance.get(
            "liabilities",
            0
        )



        # -------------------------
        # Company Object
        # -------------------------

        company = Company(

            name=self.company_name,

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
        # Analysis
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



        final = FinalAnalyzer(

            company,

            forecast_sales,

            forecast_profit,

            profit_quality,

            valuation

        ).generate()



        report = ReportGenerator().generate(

            company,

            forecast_sales,

            forecast_profit,

            profit_quality,

            valuation,

            liabilities,

            (
                "Healthy"
                if balance.get(
                    "balanced",
                    False
                )
                else
                "Warning"
            )

        )


        return {

            "company": company,

            "analysis": final,

            "report": report

        }