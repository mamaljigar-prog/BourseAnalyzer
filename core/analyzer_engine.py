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

from valuation.valuation_model import calculate_valuation

from analysis.profit_quality import ProfitQualityAnalyzer
from analysis.final_analyzer import FinalAnalyzer
from analysis.report_generator import ReportGenerator


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



        codal_service = CodalReportService(
            self.symbol
        )


        codal_report = codal_service.get_latest_financial_report()


        if not codal_report:

            raise ValueError(
                "No financial report selected"
            )



        report_period = ReportPeriodDetector(

            codal_report.get(
                "title",
                ""
            )

        ).detect()



        report_url = codal_report.get(
            "url"
        )


        if not report_url:

            raise ValueError(
                "Report URL not found"
            )



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



        financial = FinancialAdapter(

            income_sheet.get(
                "url"
            )

        )


        data = financial.report()



        balance_parser = BalanceSheetParser(

            balance_sheet.get(
                "url"
            )

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
        # Forecast Logic
        # =========================
        # قانون تحلیل:
        # گزارش میان دوره‌ای -> Annualize
        # گزارش سالانه -> همان مقدار واقعی


        months_passed = report_period.get(
            "months",
            12
        )


        if months_passed < 12:


            forecast_sales = (

                company.sales /

                months_passed

            ) * 12


        else:


            forecast_sales = company.sales



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

            ),

            report_period

        )



        return {

            "company": company,

            "analysis": final,

            "report": report

        }