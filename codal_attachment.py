import requests
import re


class CodalAttachment:

    def __init__(self, letter_serial):
        self.letter_serial = letter_serial


    def get_attachments(self):

        url = "https://codal.ir/Reports/Attachment.aspx"

        params = {
            "LetterSerial": self.letter_serial
        }

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=60
        )

        print("Status:", r.status_code)
        print("Type:", r.headers.get("Content-Type"))

        return r.content