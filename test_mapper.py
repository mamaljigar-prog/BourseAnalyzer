from codal.codal_profit_loss_parser import CodalProfitLossParser
from codal.financial_mapper import FinancialMapper


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=1"


parser = CodalProfitLossParser(url)


sheets = parser.extract_sheets()


cells = []


for sheet in sheets:

    if sheet.get("title_Fa") == "صورت سود و زیان":

        cells = sheet["tables"][0]["cells"]

        break


mapper = FinancialMapper(cells)


result = mapper.map_financials()


print("================")
print(result)