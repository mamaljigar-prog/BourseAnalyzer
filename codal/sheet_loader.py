import requests
import re


class CodalSheetLoader:

    def __init__(self, url):

        self.url = url

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }


    def get_sheet_options(self):

        r = requests.get(
            self.url,
            headers=self.headers,
            timeout=60
        )

        html = r.text


        start = html.find(
            '<select name="ctl00$ddlTable"'
        )

        end = html.find(
            "</select>",
            start
        )


        section = html[start:end]


        pattern = r'<option[^>]*value="([^"]+)"[^>]*>([^<]+)'


        matches = re.findall(
            pattern,
            section
        )


        result = []


        for value, title in matches:

            result.append(
                {
                    "id": value,
                    "title": title.strip()
                }
            )


        return result



if __name__ == "__main__":


    url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"


    loader = CodalSheetLoader(url)


    for item in loader.get_sheet_options():

        print(item)