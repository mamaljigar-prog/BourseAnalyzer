import requests

url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"

r = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
)

text = r.text


keywords = [
    "صورت وضعیت مالی",
    "tbl",
    "table",
    "Financial",
    "Report",
    "ajax",
    ".asmx",
    ".ashx",
    "Handler"
]


for k in keywords:

    print(
        k,
        text.find(k)
    )


print("================")


for line in text.splitlines():

    if (
        "ajax" in line
        or
        ".asmx" in line
        or
        ".ashx" in line
        or
        "table" in line
    ):

        print(line[:300])