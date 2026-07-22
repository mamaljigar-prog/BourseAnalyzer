import requests
import json


BASE_URL = "https://cdn.tsetmc.com"


def get_closing_price(ins_code):

    url = (
        BASE_URL +
        "/api/ClosingPrice/GetClosingPriceInfo/" +
        str(ins_code)
    )

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.tsetmc.com/"
        },
        timeout=15
    )

    result = {
        "url": url,
        "status_code": r.status_code,
        "content_type": r.headers.get(
            "Content-Type"
        ),
        "length": len(r.text)
    }

    try:
        result["json"] = r.json()
    except:
        result["raw"] = r.text[:500]

    return result


if __name__ == "__main__":

    print(
        json.dumps(
            get_closing_price(
                "7745894403636165"
            ),
            ensure_ascii=False,
            indent=2
        )
    )