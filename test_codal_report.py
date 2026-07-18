import requests
from bs4 import BeautifulSoup


url = "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=QxYX7A2pkntVRzKRJzUFvg%3d%3d&rt=0&let=58&ct=0&ft=-1"


headers = {
    "User-Agent": "Mozilla/5.0"
}


try:

    r = requests.get(
        url,
        headers=headers,
        timeout=60
    )


    print("Status:", r.status_code)

    print("----------------")
    print("بررسی HTML")
    print("----------------")


    html = r.text


    print(
        "طول صفحه:",
        len(html)
    )


    print(
        "ctl00:",
        html.find("ctl00")
    )


    print(
        "Table:",
        html.find("Table")
    )


    print(
        "فروش:",
        html.find("فروش")
    )


    print(
        "محصول:",
        html.find("محصول")
    )


    print(
        "مقدار:",
        html.find("مقدار")
    )


    print("----------------")
    print("متن های مرتبط")
    print("----------------")


    soup = BeautifulSoup(
        html,
        "html.parser"
    )


    text = soup.get_text(
        "\n"
    )


    keywords = [
        "فروش",
        "محصول",
        "مقدار",
        "تولید",
        "نرخ"
    ]


    for line in text.splitlines():

        line = line.strip()

        if line:

            for key in keywords:

                if key in line:

                    print(line)
                    break



except Exception as e:

    print(
        "خطا:",
        e
    )