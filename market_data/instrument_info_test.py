import requests
import json


BASE_URL = "https://cdn.tsetmc.com"


def get_instrument_info(ins_code):

    url = (
        BASE_URL +
        "/api/Instrument/GetInstrumentInfo/" +
        str(ins_code)
    )

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.tsetmc.com/"
        },
        timeout=15
    )

    result = {
        "url": url,
        "status_code": response.status_code,
        "content_type": response.headers.get(
            "Content-Type"
        ),
        "length": len(response.text)
    }

    try:
        result["json"] = response.json()

    except Exception:

        result["raw"] = response.text[:500]


    return result



if __name__ == "__main__":

    ins_code = "7745894403636165"

    data = get_instrument_info(ins_code)

    print(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        )
    )