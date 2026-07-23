from models.company import Company

from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData

from codal.financial_adapter import FinancialAdapter
from codal.balance_sheet_parser import BalanceSheetParser
from codal.sheet_loader import CodalSheetLoader
from codal.sheet_selector import SheetSelector

from financial.balance_sheet_mapper import BalanceSheetMapper

from valuation.valuation_model import calculate_valuation

from analysis.profit_quality import ProfitQualityAnalyzer
from analysis.final_analyzer import FinalAnalyzer
from analysis.report_generator import ReportGenerator
from analysis.company_classifier import CompanyClassifier
from analysis.analysis_strategy import AnalysisStrategy



class AnalyzerEngine:


    def __init__(
        self,
        ins_code,
        company_name,
        codal_url
    ):

        self.ins_code = ins_code
        self.company_name = company_name
        self.codal_url = codal_url



    def build_sheet_url(
        self,
        base_url,
        sheet_id
    ):

        if "sheetId=" in base_url:

            before = base_url.split(
                "sheetId="
            )[0]

            return before + f"sheetId={sheet_id}"


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


        api = TSETMCAdapter()


        closing = api.get_closing_price(
            self.ins_code
        )


        info = api.get_instrument_info(
            self.ins_code
        )


        market = MarketData(
            closing,
            info
        )


        live = market.report()



        income_url = self.build_sheet_url(
            self.codal_url,
            1
        )


        financial = FinancialAdapter(
            income_url
        )


        data = financial.report()



        balance_url = self.build_sheet_url(
            self.codal_url,
            0
        )


        sheets = CodalSheetLoader(
            balance_url
        ).get_sheet_options()


        balance_sheet = SheetSelector(
            sheets
        ).report()["balance_sheet"]



        balance_parser = BalanceSheetParser(
            balance_sheet["url"]
        )


        sheet = balance_parser.find_balance_sheet(
            balance_parser.extract_sheets()
        )


        cells = balance_parser.get_balance_table(
            sheet
        )["cells"]


        balance_data = BalanceSheetMapper(
            cells
        ).map()


        balance = balance_data.to_dict()


        balance["balanced"] = (

            balance["assets"]
            ==
            balance["liabilities"]
            +
            balance["equity"]
            +
            balance.get(
                "non_controlling_interest",
                0
            )

        )


        assets = balance["assets"]
        equity = balance["equity"]
        liabilities = balance["liabilities"]



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



        company_structure = CompanyClassifier(

            {

                "sales": company.sales,

                "operating_profit": company.operating_profit,

                "net_profit": company.net_profit,

                "non_operating_income": company.non_operating_income,

                "assets": company.assets,

                "equity": company.equity,

                "liabilities": liabilities

            },

            company.name

        ).classify()



        analysis_strategy = AnalysisStrategy(

            company_structure

        ).get_strategy()



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
                if balance["balanced"]
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

            "company_structure": company_structure,

            "analysis_strategy": analysis_strategy

        }