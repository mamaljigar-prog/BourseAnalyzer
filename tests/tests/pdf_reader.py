import requests
from pathlib import Path


class CodalPDF:

    def __init__(self, url):
        self.url = url


    def download(self):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(
            self.url,
            headers=headers,
            timeout=60
        )

        print("Status:", r.status_code)

        Path("annual_report.pdf").write_bytes(
            r.content
        )

        print(
            "PDF ذخیره شد:",
            len(r.content),
            "bytes"
        )