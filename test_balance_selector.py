from codal.codal_adapter import CodalAdapter
from codal.balance_sheet_selector import BalanceSheetSelector


a = CodalAdapter("خراسان")

reports = a.find_financial_reports()


selector = BalanceSheetSelector(reports)


result = selector.select()


print("================")
print(result)