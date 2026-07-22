import requests
import re


class CodalSheetLoader:


    def __init__(self, url):

        self.url = url

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }



    def build_sheet_url(self, sheet_id):

        if "sheetId=" in self.url:

            base = self.url.split(
                "sheetId="
            )[0]

            return (
                base +
                f"sheetId={sheet_id}"
            )


        separator = (
            "&"
            if "?" in self.url
            else "?"
        )


        return (
            self.url +
            separator +
            f"sheetId={sheet_id}"
        )



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


        pattern = (
            r'<option[^>]*value="([^"]+)"'
            r'[^>]*>([^<]+)'
        )


        matches = re.findall(
            pattern,
            section
        )


        result = []


        for value, title in matches:

            result.append(
                {
                    "id": value,
                    "title": title.strip(),
                    "url": self.build_sheet_url(value)
                }
            )


        return result