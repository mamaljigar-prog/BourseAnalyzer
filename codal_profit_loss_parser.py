import requests
import json


class CodalProfitLossParser:


    def __init__(self, url):

        self.url = url

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }



    def extract_sheets(self):

        r = requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )


        text = r.text


        start = text.find(
            '"sheets":'
        )


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




    def get_sales(self):


        sheets = self.extract_sheets()


        for sheet in sheets:


            if sheet.get(
                "title_Fa"
            ) == "صورت سود و زیان":


                cells = sheet["tables"][0]["cells"]


                sales_row = None


                for cell in cells:

                    if cell.get(
                        "value"
                    ) == "درآمدهاي عملياتي":


                        sales_row = cell.get(
                            "rowCode"
                        )

                        break



                result = []


                for cell in cells:


                    if cell.get(
                        "rowCode"
                    ) == sales_row:


                        result.append(
                            {
                                "address": cell.get("address"),
                                "value": cell.get("value"),
                                "year": cell.get("yearEndToDate"),
                                "period": cell.get("periodEndToDate")
                            }
                        )



                return result



        return None





if __name__ == "__main__":


    url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=1"


    parser = CodalProfitLossParser(
        url
    )


    data = parser.get_sales()


    print("================")

    print(data)