from main import build_financial_data

data = build_financial_data("خراسان")

print("==============================")
print("FINANCIAL DATA DEBUG")
print("==============================")

print("Company:", data.company_name)
print("Symbol:", data.symbol)

print("Current Sales:", data.current_sales)
print("Forecast Sales:", data.forecast_sales)

print("Current Profit:", data.current_profit)
print("Forecast Profit:", data.forecast_profit)

print("Total Assets:", data.total_assets)
print("Total Equity:", data.total_equity)

print("Market Cap:", data.market_cap)

print("==============================")