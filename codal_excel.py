import requests
from bs4 import BeautifulSoup


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


        soup = BeautifulSoup(
            r.text,
            "html.parser"
        )


        data = {}

        for inp in soup.find_all("input"):

            name = inp.get("name")

            value = inp.get("value","")


            if name:

                data[name] = value


        data["ctl00$ibtnExport"] = "Export To Excel"


        response = session.post(
            self.url,
            data=data,
            headers=headers,
            timeout=60
        )


        print(response.status_code)
        print(response.headers.get("Content-Type"))


        return response.content