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
            or self.symbol
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


        period_info = ReportPeriodDetector(
            codal_report.get(
                "title",
                ""
            )
        ).detect()


        period_months = period_info.get(
            "months",
            12
        )


        if not period_months:
            period_months = 12



        # =========================
        # Sheets
        # =========================

        sheets = CodalSheetLoader(
            report_url
        ).get_sheet_options()


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
                "Income statement not found"
            )



        # =========================
        # Financial Adapter
        # =========================

        financial = FinancialAdapter(
            income_sheet["url"],
            period_months=period_months
        )


        data = financial.report()


        current = data.get(
            "current",
            {}
        )

        previous = data.get(
            "previous",
            {}
        )

        annual = data.get(
            "annual",
            {}
        )


        adapter_period = data.get(
            "period_months"
        )


        if adapter_period:
            period_months = adapter_period



        sales = current.get(
            "sales",
            0
        )

        operating_profit = current.get(
            "operating_profit",
            0
        )

        net_profit = current.get(
            "net_profit",
            0
        )

        non_operating_income = current.get(
            "non_operating_income",
            0
        )



        # =========================
        # Balance Sheet
        # =========================

        assets = 0
        equity = 0
        liabilities = 0


        if balance_sheet:

            balance = BalanceSheetParser(
                balance_sheet["url"]
            ).get_balance_data()


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
        # Company
        # =========================

        company = Company(

            name=company_name,

            symbol=self.symbol,

            sales=sales,

            operating_profit=operating_profit,

            net_profit=net_profit,

            assets=assets,

            equity=equity,

            market_cap=live.get(
                "market_cap",
                0
            ),

            non_operating_income=non_operating_income,

            period_months=period_months,


            previous_sales=previous.get(
                "sales",
                0
            ),

            previous_gross_profit=previous.get(
                "gross_profit",
                0
            ),

            previous_operating_profit=previous.get(
                "operating_profit",
                0
            ),

            previous_net_profit=previous.get(
                "net_profit",
                0
            ),

            previous_non_operating_income=previous.get(
                "non_operating_income",
                0
            ),


            annual_previous_sales=annual.get(
                "sales",
                0
            ),

            annual_previous_gross_profit=annual.get(
                "gross_profit",
                0
            ),

            annual_previous_operating_profit=annual.get(
                "operating_profit",
                0
            ),

            annual_previous_net_profit=annual.get(
                "net_profit",
                0
            ),

            annual_previous_non_operating_income=annual.get(
                "non_operating_income",
                0
            )

        )



        # =========================
        # Classification
        # =========================

        structure = CompanyClassifier(

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



        strategy = AnalysisStrategy(
            structure
        ).get_strategy()



        # =========================
        # Forecast
        # =========================

        forecast = ForecastEngine(

            company,

            strategy,

            period_months

        ).run()



        # =========================
        # Profit Quality
        # =========================

        quality = ProfitQualityAnalyzer(

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

            strategy

        ).run()



        # =========================
        # Final
        # =========================

        final = FinalAnalyzer(

            company,

            forecast["forecast_sales"],

            forecast["forecast_profit"],

            quality,

            valuation

        ).generate()



        report = ReportGenerator().generate(

            company,

            forecast["forecast_sales"],

            forecast["forecast_profit"],

            quality,

            valuation,

            liabilities,

            (
                "Healthy"
                if assets + liabilities - equity == assets
                else "Warning"
            ),

            company_structure=structure,

            analysis_strategy=strategy

        )


        return {

            "company": company,

            "analysis": final,

            "report": report,

            "company_structure": structure,

            "analysis_strategy": strategy,

            "forecast": forecast,

            "valuation": valuation,

            "period_info": period_info,

            "period_months": period_months

        }