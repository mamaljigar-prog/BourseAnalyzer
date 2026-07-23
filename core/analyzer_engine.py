from models.company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData
from tsetmc.symbol_resolver import SymbolResolver

from codal.codal_report_service import CodalReportService
from codal.sheet_loader import CodalSheetLoader
from codal.sheet_selector import SheetSelector
from codal.financial_adapter import FinancialAdapter
from codal.balance_sheet_parser import BalanceSheetParser

from analysis.company_classifier import CompanyClassifier
from analysis.analysis_strategy import AnalysisStrategy
from analysis.profit_quality import ProfitQualityAnalyzer
from analysis.final_analyzer import FinalAnalyzer
from analysis.report_generator import ReportGenerator

from forecast.forecast_engine import ForecastEngine
from valuation.valuation_engine import ValuationEngine



class AnalyzerEngine:


    def __init__(self, symbol):

        self.symbol = symbol



    def run(self):


        # =========================
        # Symbol Resolver
        # =========================

        resolver = SymbolResolver()

        ins_code = resolver.find_ins_code(
            self.symbol
        )


        if not ins_code:

            raise ValueError(
                "Symbol not found"
            )



        # =========================
        # Market Data
        # =========================

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


        company_name = (
            api.get_company_name(info)
            or
            self.symbol
        )



        # =========================
        # Codal Report
        # =========================

        codal_service = CodalReportService(
            self.symbol
        )


        codal_report = (
            codal_service
            .get_latest_financial_report()
        )


        if not codal_report:

            raise ValueError(
                "No financial report selected"
            )


        report_url = codal_report.get(
            "url"
        )


        if not report_url:

            raise ValueError(
                "Report URL not found"
            )



        # =========================
        # Sheets
        # =========================

        loader = CodalSheetLoader(
            report_url
        )


        sheets = loader.get_sheet_options()


        selected = SheetSelector(
            sheets
        ).report()



        income_sheet = selected.get(
            "income_statement"
        )


        balance_sheet = selected.get(
            "balance_sheet"
        )



        if not income_sheet:

            raise ValueError(
                "Income statement sheet not found"
            )


        if not balance_sheet:

            raise ValueError(
                "Balance sheet sheet not found"
            )



        # =========================
        # Financial Data
        # =========================

        financial = FinancialAdapter(

            income_sheet["url"]

        )


        data = financial.report()



        # =========================
        # Balance Sheet
        # =========================

        balance_parser = BalanceSheetParser(

            balance_sheet["url"]

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



        # =========================
        # Company Object
        # =========================

        company = Company(

            name=company_name,

            symbol=self.symbol,

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



        # =========================
        # Company Classification
        # =========================

        company_structure = CompanyClassifier(

            {

                "sales": company.sales,

                "operating_profit":
                    company.operating_profit,

                "net_profit":
                    company.net_profit,

                "non_operating_income":
                    company.non_operating_income,

                "assets":
                    company.assets,

                "equity":
                    company.equity,

                "liabilities":
                    liabilities

            },

            company.name

        ).classify()



        # =========================
        # Strategy
        # =========================

        analysis_strategy = AnalysisStrategy(

            company_structure

        ).get_strategy()



        # =========================
        # Forecast
        # =========================

        forecast = ForecastEngine(

            company,

            analysis_strategy

        ).run()



        # =========================
        # Profit Quality
        # =========================

        profit_quality = ProfitQualityAnalyzer(

            company.operating_profit,

            company.net_profit,

            company.non_operating_income

        ).analyze()



        # =========================
        # Valuation
        # =========================

        valuation = ValuationEngine(

            company,

            forecast,

            analysis_strategy

        ).run()



        # =========================
        # Final Analysis
        # =========================

        final = FinalAnalyzer(

            company,

            forecast["forecast_sales"],

            forecast["forecast_profit"],

            profit_quality,

            valuation

        ).generate()



        # =========================
        # Report
        # =========================

        report = ReportGenerator().generate(

            company,

            forecast["forecast_sales"],

            forecast["forecast_profit"],

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

            ),

            company_structure=company_structure,

            analysis_strategy=analysis_strategy

        )



        return {

            "company": company,

            "analysis": final,

            "report": report,

            "company_structure":
                company_structure,

            "analysis_strategy":
                analysis_strategy,

            "forecast":
                forecast,

            "valuation":
                valuation

        }