from codal import CodalReport
from financial_adapter import convert_codal_to_financial

from quality import ProfitQuality, QualityHistory
from fundamental import FundamentalScore

from analyzer import StockAnalyzer
from full_report import FullReport

from warning import WarningAnalyzer

from tsetmc_adapter import TsetmcAdapter



# =========================
# 1) گزارش مالی کدال
# =========================

codal = CodalReport(

    symbol="شپدیس",

    period="1404 سالانه",

    fiscal_end_date="1406/04/01",

    sales=100000,

    operating_profit=35000,

    net_profit=30000,

    non_operating_income=7000,

    assets=93000,

    equity=50000,

    cash_flow=25000

)


codal_data = codal.get_data()



# =========================
# 2) تبدیل به FinancialReport
# =========================

current = convert_codal_to_financial(
    codal_data
)



previous = convert_codal_to_financial({

    "period": "1403 سالانه",

    "fiscal_end_date": "1405/04/01",

    "months": 12,

    "sales": 80000,

    "operating_profit": 28000,

    "net_profit": 22000,

    "non_operating_income": 3000,

    "assets": 90000,

    "equity": 48000,

    "cash_flow": 20000

})



# =========================
# 3) کیفیت سود
# =========================

quality = ProfitQuality(

    operating_profit=current.operating_profit,

    recurring_income=2000,

    non_recurring_income=current.non_operating_income,

    reported_profit=current.net_profit

)


quality_score = quality.score()


normalized_profit = quality.normalized_profit()



# =========================
# 4) تاریخچه درآمد غیرعملیاتی
# =========================

history = QualityHistory()


history.add_period(

    "1402",

    1000,

    0

)


history.add_period(

    "1403",

    1500,

    500

)


history.add_period(

    "1404",

    2000,

    700

)


history.analyze()



# =========================
# 5) اطلاعات بازار TSETMC
# =========================

tsetmc = TsetmcAdapter(

    "20562694899904339"

)


market_data = tsetmc.get_stock_data()



if not market_data:

    raise Exception(
        "خطا در دریافت اطلاعات بازار"
    )



# =========================
# 6) ارزش گذاری
# =========================

stock = StockAnalyzer(

    symbol=market_data["symbol"],

    price=market_data["closing_price"],

    shares=market_data["shares"],

    sales_forecast=current.sales,

    profit_forecast=current.net_profit,

    assets=current.assets,

    equity=current.equity

)


stock_data = stock.get_report_data()



# استفاده از ارزش بازار واقعی TSETMC

stock_data["market_value"] = market_data["market_value"]



# =========================
# 7) P/E نرمال شده
# =========================

pe_normalized = (

    stock_data["market_value"]

    /

    normalized_profit

)



# =========================
# 8) امتیاز بنیادی
# =========================

fundamental = FundamentalScore(

    current,

    previous,

    quality_score,

    pe_normalized,

    stock_data["pe"]

)


fundamental_score = fundamental.calculate()



# =========================
# 9) هشدارهای تحلیلی
# =========================

warning = WarningAnalyzer(

    reported_profit=current.net_profit,

    normalized_profit=normalized_profit,

    non_recurring_income=current.non_operating_income,

    pe_forward=stock_data["pe"],

    pe_normalized=pe_normalized

)


warning.show()



# =========================
# 10) گزارش نهایی
# =========================

report = FullReport(

    stock_data,

    quality_score,

    normalized_profit,

    fundamental_score,

    current

)


report.show()