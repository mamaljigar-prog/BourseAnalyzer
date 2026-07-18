from codal_monthly import CodalMonthly



url = "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=QxYX7A2pkntVRzKRJzUFvg%3d%3d&rt=0&let=58&ct=0&ft=-1"



codal = CodalMonthly(url)



codal.show_monthly_sales()