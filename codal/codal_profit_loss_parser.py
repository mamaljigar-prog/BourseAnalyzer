import requests
import json


class CodalProfitLossParser:


    def __init__(self, url):

        self.url = url

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }



    def extract_sheets(self):

        response = requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )

        text = response.text


        start = text.find('"sheets":')

        if start == -1:
            raise Exception("Sheets پیدا نشد")


        start += len('"sheets":')


        while text[start] != '[':
            start += 1


        count = 0


        for i in range(start, len(text)):

            if text[i] == '[':
                count += 1

            elif text[i] == ']':
                count -= 1


            if count == 0:

                end = i + 1
                break


        return json.loads(
            text[start:end]
        )



    def find_sheet(self, title):

        sheets = self.extract_sheets()


        for sheet in sheets:

            if sheet.get("title_Fa") == title:

                return sheet


        return None



    def find_row_value(self, cells, keyword):


        row_code = None


        for cell in cells:

            value = cell.get("value")


            if value and keyword in str(value):

                row_code = cell.get("rowCode")
                break



        if not row_code:

            return None



        result = []


        for cell in cells:

            if cell.get("rowCode") == row_code:

                result.append({

                    "address": cell.get("address"),

                    "value": self.clean_number(
                        cell.get("value")
                    ),

                    "year": cell.get("yearEndToDate"),

                    "period": cell.get("periodEndToDate")

                })


        return result



    def clean_number(self,value):

        try:

            return int(value)

        except:

            return value



    def get_financial_data(self):


        sheet = self.find_sheet(
            "صورت سود و زیان"
        )


        if not sheet:

            return None



        cells = sheet["tables"][0]["cells"]



        data = {


            "sales":
                self.find_row_value(
                    cells,
                    "درآمدهاي عملياتي"
                ),


            "gross_profit":
                self.find_row_value(
                    cells,
                    "سود(زيان) ناخالص"
                ),


            "operating_profit":
                self.find_row_value(
                    cells,
                    "سود(زيان) عملياتى"
                ),


            "net_profit":
                self.find_row_value(
                    cells,
                    "سود(زيان) خالص"
                )

        }



        return data




if __name__ == "__main__":


    url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=1"


    parser = CodalProfitLossParser(url)


    result = parser.get_financial_data()


    print("================")

    print(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=4
        )
    )