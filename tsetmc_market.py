import requests
import re


def get_market_data(inscode):

    url = "http://www.tsetmc.com/Loader.aspx"

    params = {
        "ParTree": "151311",
        "i": inscode
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=15
    )

    print("Status:", r.status_code)

    html = r.text

    print("Length:", len(html))

    # نمایش اطلاعات مهم
    patterns = {
        "EPS": r"EstimatedEPS='(.*?)'",
        "SectorPE": r"SectorPE='(.*?)'",
        "CSecVal": r"CSecVal='(.*?)'",
    }

    result = {}

    for name, pattern in patterns.items():
        x = re.search(pattern, html)

        if x:
            result[name] = x.group(1)
        else:
            result[name] = None


    # دریافت دیتای لحظه ای
    csec = result["CSecVal"]

    if csec:

        data_url = "http://www.tsetmc.com/tsev2/data/instinfodata.aspx"

        data = requests.get(
            data_url,
            params={
                "i": inscode,
                "c": csec
            },
            headers=headers,
            timeout=15
        ).text

        result["raw"] = data


    return result



if __name__ == "__main__":

    inscode = "43552974795606067"

    data = get_market_data(inscode)

    print("================")
    print(data)