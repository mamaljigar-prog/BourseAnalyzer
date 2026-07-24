from models.company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData
from tsetmc.symbol_resolver import SymbolResolver

from codal.codal_report_service import CodalReportService
from codal.sheet_loader import CodalSheetLoader
from codal.sheet_selector import SheetSelector
from codal.financial_adapter import FinancialAdapter
from codal.balance_sheet_parser import BalanceSheetParser
from codal.report_period_detector import ReportPeriodDetector

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

        # =========================================================
        # Symbol Resolver
        # =========================================================

        resolver = SymbolResolver()

        ins_code = resolver.find_ins_code(
            self.symbol
        )

        if not ins_code:

            raise ValueError(
                "Symbol not found"
            )

        # =========================================================
        # Market Data
        # =========================================================

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

        # =========================================================
        # Codal Report
        # =========================================================

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

        # =========================================================
        # Report Period Detection
        # =========================================================

        report_title = codal_report.get(
            "title",
            ""
        )

        period_detector = ReportPeriodDetector(
            report_title
        )

        period_info = (
            period_detector.detect()
        )

        period_months = period_info.get(
            "months"
        )

        # اگر ReportPeriodDetector نتوانست دوره را تشخیص دهد،
        # FinancialAdapter بعداً دوره را از ستون‌های صورت سود و زیان
        # تشخیص خواهد داد.
        #
        # این مقدار فقط fallback موقت است.

        if not period_months or period_months <= 0:

            period_months = 12

        # =========================================================
        # Sheets
        # =========================================================

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

        # =========================================================
        # Financial Data
        #
        # FinancialAdapter is the boundary between the raw
        # Codal parser and the analysis engine.
        #
        # CodalProfitLossParser
        #       ↓
        # data["semantic"]
        #
        # FinancialAdapter
        #       ↓
        # data["current"]
        # data["previous"]
        # data["annual"]
        #
        # AnalyzerEngine must consume the normalized structure.
        # =========================================================

        financial = FinancialAdapter(
            income_sheet["url"],
            period_months=period_months
        )

        data = financial.report()

        # =========================================================
        # Normalized Financial Data
        # =========================================================

        current_data = data.get(
            "current",
            {}
        )

        previous_data = data.get(
            "previous",
            {}
        )

        annual_data = data.get(
            "annual",
            {}
        )

        # =========================================================
        # Current Financial Values
        # =========================================================

        sales = current_data.get(
            "sales",
            0
        )

        gross_profit = current_data.get(
            "gross_profit",
            0
        )

        operating_profit = current_data.get(
            "operating_profit",
            0
        )

        non_operating_income = current_data.get(
            "non_operating_income",
            0
        )

        net_profit = current_data.get(
            "net_profit",
            0
        )

        # =========================================================
        # Previous Comparable Values
        #
        # These values are preserved for growth analysis,
        # comparison and financial quality checks.
        # =========================================================

        previous_sales = previous_data.get(
            "sales",
            0
        )

        previous_gross_profit = previous_data.get(
            "gross_profit",
            0
        )

        previous_operating_profit = previous_data.get(
            "operating_profit",
            0
        )

        previous_non_operating_income = previous_data.get(
            "non_operating_income",
            0
        )

        previous_net_profit = previous_data.get(
            "net_profit",
            0
        )

        # =========================================================
        # Annual Previous Full Year Values
        #
        # These values are not used as the primary current
        # analysis period.
        #
        # They are preserved for future historical comparison,
        # growth analysis and quality checks.
        # =========================================================

        annual_sales = annual_data.get(
            "sales",
            0
        )

        annual_gross_profit = annual_data.get(
            "gross_profit",
            0
        )

        annual_operating_profit = annual_data.get(
            "operating_profit",
            0
        )

        annual_non_operating_income = annual_data.get(
            "non_operating_income",
            0
        )

        annual_net_profit = annual_data.get(
            "net_profit",
            0
        )

        # =========================================================
        # Use FinancialAdapter Period
        #
        # FinancialAdapter has direct access to the financial
        # statement columns and can detect the actual cumulative
        # reporting period.
        #
        # Therefore, when available, its detected period takes
        # priority over the report-title detector.
        # =========================================================

        adapter_period_months = data.get(
            "period_months"
        )

        if (
            adapter_period_months
            and
            adapter_period_months > 0
        ):

            period_months = (
                adapter_period_months
            )

        # =========================================================
        # Debug Financial Values
        # =========================================================

        print()

        print(
            "DEBUG ENGINE FINANCIAL VALUES"
        )

        print(
            "------------------------------"
        )

        print(
            "Period Months:",
            period_months
        )

        print(
            "Current Sales:",
            sales
        )

        print(
            "Previous Comparable Sales:",
            previous_sales
        )

        print(
            "Annual Previous Sales:",
            annual_sales
        )

        print(
            "Current Gross Profit:",
            gross_profit
        )

        print(
            "Current Operating Profit:",
            operating_profit
        )

        print(
            "Current Non Operating Income:",
            non_operating_income
        )

        print(
            "Current Net Profit:",
            net_profit
        )

        print(
            "------------------------------"
        )

        # =========================================================
        # Balance Sheet
        # =========================================================

        balance_parser = BalanceSheetParser(
            balance_sheet["url"]
        )

        balance = (
            balance_parser
            .get_balance_data()
        )

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

        # =========================================================
        # Company Object
        # =========================================================

        company = Company(

            name=company_name,

            symbol=self.symbol,

            sales=sales,

            operating_profit=operating_profit,

            net_profit=net_profit,

            assets=assets,

            equity=equity,

            market_cap=live[
                "market_cap"
            ],

            non_operating_income=(
                non_operating_income
            )

        )

        # =========================================================
        # Company Classification
        # =========================================================

        company_structure = CompanyClassifier(

            {

                "sales":
                    company.sales,

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

        # =========================================================
        # Strategy
        # =========================================================

        analysis_strategy = AnalysisStrategy(

            company_structure

        ).get_strategy()

        # =========================================================
        # Forecast
        # =========================================================

        forecast = ForecastEngine(

            company,

            analysis_strategy,

            period_months=period_months

        ).run()

        # =========================================================
        # Profit Quality
        # =========================================================

        profit_quality = ProfitQualityAnalyzer(

            company.operating_profit,

            company.net_profit,

            company.non_operating_income

        ).analyze()

        # =========================================================
        # Valuation
        # =========================================================

        valuation = ValuationEngine(

            company,

            forecast,

            analysis_strategy

        ).run()

        # =========================================================
        # Final Analysis
        # =========================================================

        final = FinalAnalyzer(

            company,

            forecast[
                "forecast_sales"
            ],

            forecast[
                "forecast_profit"
            ],

            profit_quality,

            valuation

        ).generate()

        # =========================================================
        # Report
        # =========================================================

        report = ReportGenerator().generate(

            company,

            forecast[
                "forecast_sales"
            ],

            forecast[
                "forecast_profit"
            ],

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

            company_structure=(
                company_structure
            ),

            analysis_strategy=(
                analysis_strategy
            )

        )

        # =========================================================
        # Return Result
        # =========================================================

        return {

            "company":
                company,

            "analysis":
                final,

            "report":
                report,

            "company_structure":
                company_structure,

            "analysis_strategy":
                analysis_strategy,

            "forecast":
                forecast,

            "valuation":
                valuation,

            "period_info":
                period_info,

            "period_months":
                period_months,

            # =====================================================
            # Historical Financial Data
            #
            # These values are returned for future growth,
            # comparison and quality analysis.
            # =====================================================

            "financial_data": {

                "current": {

                    "sales":
                        sales,

                    "gross_profit":
                        gross_profit,

                    "operating_profit":
                        operating_profit,

                    "non_operating_income":
                        non_operating_income,

                    "net_profit":
                        net_profit

                },

                "previous_comparable": {

                    "sales":
                        previous_sales,

                    "gross_profit":
                        previous_gross_profit,

                    "operating_profit":
                        previous_operating_profit,

                    "non_operating_income":
                        previous_non_operating_income,

                    "net_profit":
                        previous_net_profit

                },

                "annual_previous": {

                    "sales":
                        annual_sales,

                    "gross_profit":
                        annual_gross_profit,

                    "operating_profit":
                        annual_operating_profit,

                    "non_operating_income":
                        annual_non_operating_income,

                    "net_profit":
                        annual_net_profit

                }

            }

        }