from models.company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData
from tsetmc.symbol_resolver import SymbolResolver

from codal.codal_report_service import CodalReportService
from codal.sheet_loader import CodalSheetLoader
from codal.sheet_selector import SheetSelector
from codal.codal_profit_loss_parser import CodalProfitLossParser
from codal.financial_mapper import FinancialMapper
from codal.financial_adapter import FinancialAdapter
from codal.balance_sheet_parser import BalanceSheetParser

from valuation.valuation_model import calculate_valuation

from analysis.profit_quality import ProfitQualityAnalyzer
from analysis.final_analyzer import FinalAnalyzer
from analysis.report_generator import ReportGenerator


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
        # Codal Report Selection
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
        # Sheet Selection
        # =========================

        loader = CodalSheetLoader(
            report_url
        )

        sheets = loader.get_sheet_options()

        selector = SheetSelector(
            sheets
        )

        selected = selector.report()

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

        income_url = income_sheet.get(
            "url"
        )

        balance_url = balance_sheet.get(
            "url"
        )

        if not income_url:

            raise ValueError(
                "Income statement URL not found"
            )

        if not balance_url:

            raise ValueError(
                "Balance sheet URL not found"
            )

        # =========================
        # Canonical Financial Layer
        # =========================

        financial = FinancialAdapter(
            income_url
        )

        financial_report = (
            financial.report()
        )

        sales = financial_report.get(
            "sales",
            0
        )

        operating_profit = (
            financial_report.get(
                "operating_profit",
                0
            )
        )

        net_profit = (
            financial_report.get(
                "net_profit",
                0
            )
        )

        non_operating_income = (
            financial_report.get(
                "non_operating_income",
                0
            )
        )

        report_period_end = (
            financial_report.get(
                "report_period_end"
            )
        )

        fiscal_year_end = (
            financial_report.get(
                "fiscal_year_end"
            )
        )

        duration_months = (
            financial_report.get(
                "duration_months"
            )
        )

        period_type = (
            financial_report.get(
                "period_type"
            )
        )

        # =========================
        # Balance Sheet
        # =========================

        balance_parser = BalanceSheetParser(
            balance_url
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

        # =========================
        # Company Domain Model
        # =========================

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

        # =========================
        # Financial Period Validation
        # =========================

        if duration_months is None:

            raise ValueError(

                "Financial period duration "
                "could not be determined from "
                "Codal report metadata"

            )

        if period_type is None:

            raise ValueError(

                "Financial period type "
                "could not be determined"

            )

        # =========================
        # Forecast
        # =========================

        # Forecast is an annualized estimate.
        #
        # IMPORTANT:
        # Forecast must NOT be treated as
        # comparable growth against the
        # current reporting period.
        #
        # 3M  -> 12 / 3  = 4.0
        # 6M  -> 12 / 6  = 2.0
        # 9M  -> 12 / 9  = 1.3333
        # 12M -> 12 / 12 = 1.0

        annualization_factor = (

            12 /

            duration_months

        )

        forecast_sales = (

            company.sales

            *

            annualization_factor

        )

        margin = (

            company.net_profit /

            company.sales

            if company.sales

            else 0

        )

        forecast_profit = (

            forecast_sales

            *

            margin

        )

        # =========================
        # Profit Quality
        # =========================

        profit_quality = (

            ProfitQualityAnalyzer(

                company.operating_profit,

                company.net_profit,

                company.non_operating_income

            ).analyze()

        )

        # =========================
        # Valuation
        # =========================

        valuation = calculate_valuation(

            market_cap=company.market_cap,

            forecast_sales=(

                forecast_sales /

                10000

            ),

            forecast_profit=(

                forecast_profit /

                10000

            ),

            equity=company.equity,

            assets=company.assets,

            dividend=11570

        )

        # =========================
        # Final Analysis
        # =========================

        final = FinalAnalyzer(

            company,

            forecast_sales,

            forecast_profit,

            profit_quality,

            valuation,

            period_type=period_type,

            duration_months=duration_months,

            annualization_factor=(
                annualization_factor
            )

        ).generate()

        # =========================
        # Report
        # =========================

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

            ),

            report_period={

                "period":
                    report_period_end,

                "fiscal_year_end":
                    fiscal_year_end,

                "duration_months":
                    duration_months,

                "period_type":
                    period_type,

                "annualization_factor":
                    annualization_factor,

                "forecast_method":
                    (
                        "Annualized from "
                        f"{period_type} current period"
                    ),

                "growth_method":
                    (
                        "Comparable-period growth "
                        "not available yet"
                    )

            }

        )

        return {

            "company":
                company,

            "analysis":
                final,

            "report":
                report,

            "financial_period": {

                "report_period_end":
                    report_period_end,

                "fiscal_year_end":
                    fiscal_year_end,

                "duration_months":
                    duration_months,

                "period_type":
                    period_type,

                "annualization_factor":
                    annualization_factor

            }

        }