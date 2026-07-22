import requests
import json
from urllib.parse import quote


BASE = "https://cdn.tsetmc.com"


def search_symbol(symbol):

    url = (
        BASE +
        "/api/Instrument/GetInstrumentSearch/" +
        quote(symbol)
    )

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.tsetmc.com/"
        },
        timeout=10
    )

    print("STATUS:", r.status_code)
    print("TYPE:", r.headers.get("Content-Type"))
    print("LENGTH:", len(r.text))

    print("\nRAW:")
    print(r.text[:1000])


if __name__ == "__main__":

    search_symbol("شپنا")