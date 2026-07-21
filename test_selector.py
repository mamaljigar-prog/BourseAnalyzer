from codal.codal_adapter import CodalAdapter
from codal.report_selector import ReportSelector


adapter = CodalAdapter("خراسان")


financial = adapter.find_financial_reports()

monthly = adapter.find_monthly_reports()


selector = ReportSelector(
    financial,
    monthly
)


print("================")
print("LATEST FINANCIAL")
print("================")

print(
    selector.latest_financial()
)


print("================")
print("LATEST MONTHLY")
print("================")

print(
    selector.latest_monthly()
)


print("================")
print(
    selector.summary()
)