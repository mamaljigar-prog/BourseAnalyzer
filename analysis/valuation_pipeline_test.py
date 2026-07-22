# analysis/valuation_pipeline_test.py


from codal.codal_profit_loss_parser import CodalProfitLossParser
from codal.financial_data_adapter import FinancialDataAdapter

from analysis.normalized_profit import NormalizedProfitCalculator

from valuation.valuation_engine import ValuationEngine

from market_data.market_cap_provider import MarketCapProvider

from utils.unit_converter import UnitConverter



url = (
    "https://codal.ir/Reports/Decision.aspx?"
    "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"
    "&rt=0&let=6&ct=0&ft=-1&sheetId=1"
)



parser = CodalProfitLossParser(url)

raw_data = parser.get_financial_data()



adapter = FinancialDataAdapter()

financial_data = adapter.adapt_income_statement(
    raw_data
)



normalizer = NormalizedProfitCalculator()

normalized_profit = normalizer.calculate(
    financial_data
)



market_provider = MarketCapProvider()


market_data = market_provider.get_market_data(

    symbol="TEST",

    market_cap=87350000000

)



converter = UnitConverter()



forecast_profit = converter.to_toman(
    normalized_profit["normalized_profit"]
)


forecast_sales = converter.to_toman(
    financial_data["sales"]["current"]
)



engine = ValuationEngine()


valuation = engine.analyze(

    market_cap=market_data["market_cap"],

    forecast_profit=forecast_profit,

    forecast_sales=forecast_sales

)



print("\nFinancial Data")
print(financial_data)


print("\nNormalized Profit")
print(normalized_profit)


print("\nMarket Data")
print(market_data)


print("\nValuation")
print(valuation)