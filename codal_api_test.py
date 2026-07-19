import requests


url = "https://search.codal.ir/api/search/v2/q"


params = {

    "PageNumber": 1,

    "Length": 10,

    "Symbol": "خراسان",

    "Category": 1,

    "TracingNo": "",

    "Publisher": "",

    "Audited": -1,

    "NotAudited": -1

}


headers = {

    "User-Agent":
    "Mozilla/5.0",

    "Accept":
    "application/json"

}


r = requests.get(

    url,

    params=params,

    headers=headers,

    timeout=30

)


print(
    r.url
)


print(
    r.status_code
)


print(
    r.text[:1000]
)