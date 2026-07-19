import requests
from bs4 import BeautifulSoup


class CodalSheetParser:

    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }


    def get_sheets(self):

        r = requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )

        r.encoding = "utf-8"

        soup = BeautifulSoup(
            r.text,
            "html.parser"
        )


        select = soup.find(
            "select",
            id="ddlTable"
        )


        result = []


        if select:

            for option in select.find_all("option"):

                result.append(
                    {
                        "sheet_id": option.get("value"),
                        "title": option.get_text(
                            strip=True
                        )
                    }
                )


        return result



if __name__ == "__main__":

    url = input(
        "لینک مادر کدال: "
    )


    parser = CodalSheetParser(url)


    print("\nSheet ها:")
    print("----------------")


    for item in parser.get_sheets():

        print(
            item["sheet_id"],
            "-->",
            item["title"]
        )