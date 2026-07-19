import requests
from bs4 import BeautifulSoup
from io import BytesIO
import pandas as pd


class CodalExcel:


    def __init__(self, letter_url):

        self.url = letter_url



    def download_excel(self):

        session = requests.Session()


        headers = {
            "User-Agent": "Mozilla/5.0"
        }


        r = session.get(
            self.url,
            headers=headers,
            timeout=60
        )


        print(
            "GET:",
            r.status_code
        )


        soup = BeautifulSoup(
            r.text,
            "html.parser"
        )


        data = {}


        for inp in soup.find_all("input"):

            name = inp.get("name")

            value = inp.get(
                "value",
                ""
            )


            if name:

                data[name] = value



        data["ctl00$ibtnExport"] = "Export To Excel"



        response = session.post(

            self.url,

            data=data,

            headers=headers,

            timeout=60

        )


        print(
            "POST:",
            response.status_code
        )


        print(
            "TYPE:",
            response.headers.get(
                "Content-Type"
            )
        )


        return BytesIO(
            response.content
        )





if __name__ == "__main__":


    url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1&sheetId=1"


    excel = CodalExcel(
        url
    )


    file = excel.download_excel()


    try:

        xls = pd.ExcelFile(
            file
        )


        print("================")

        print(
            "Sheet ها:"
        )

        for s in xls.sheet_names:

            print(
                s
            )


    except Exception as e:

        print(
            "خطا در خواندن اکسل:",
            e
        )