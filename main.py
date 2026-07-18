from codal import CodalReport
from financial_adapter import convert_codal_to_financial

from quality import ProfitQuality, QualityHistory
from fundamental import FundamentalScore

from analyzer import StockAnalyzer
from full_report import FullReport

from warning import WarningAnalyzer



# =========================
# 1) دریافت گزارش کدال
# =========================

codal = CodalReport(

    symbol="شپدیس",

    period="1404 سالانه",

    sales=100000,

    operating_profit=35000,

    net_profit=30000,

    non_operating_income=7000

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

    "sales": 80000,

    "operating_profit": 28000,

    "net_profit": 22000,

    "non_operating_income": 3000

})



# =========================
# 3) تحلیل کیفیت سود
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
# 5) اطلاعات بازار
# =========================

stock = StockAnalyzer(

    symbol="شپدیس",

    price=11310,

    shares=233572772000,

    sales_forecast=current.sales,

    profit_forecast=current.net_profit,

    assets=200000,

    equity=120000

)


stock_data = stock.get_report_data()



# =========================
# 6) P/E نرمال شده
# =========================

pe_normalized = (

    stock_data["market_value"]

    /

    normalized_profit

)



# =========================
# 7) امتیاز بنیادی
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
# 8) هشدارهای تحلیلی
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
# 9) گزارش نهایی
# =========================

report = FullReport(

    stock_data,

    quality_score,

    normalized_profit,

    fundamental_score

)


report.show()