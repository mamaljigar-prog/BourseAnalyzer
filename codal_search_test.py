import requests


url = "https://codal.ir/Reports/Decision.aspx"


params = {

    "Symbol": "خراسان"

}


r = requests.get(

    url,

    params=params,

    headers={
        "User-Agent":"Mozilla/5.0"
    },

    timeout=30

)


print(
    r.status_code
)


print(
    r.url
)


print(
    r.text[:500]
)