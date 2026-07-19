from codal_monthly import CodalMonthly

url = input("لینک گزارش کدال را وارد کن: ")

codal = CodalMonthly(url)

codal.show_monthly_sales()