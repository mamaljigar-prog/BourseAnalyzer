from codal_financial import CodalFinancial


reports = []


# اینجا فعلا همان خروجی API قبلی را داخل لیست قرار بده


c = CodalFinancial(reports)


report = c.find_financial_report()


if report:

    excel = c.download_excel(
        report["ExcelUrl"]
    )


    if excel:

        df = c.parse_income_statement(excel)

        print(df)