import requests


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"


t = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text


pos = t.find("صورت وضعیت مالی")


print("POSITION:", pos)

print("================")

print(
    t[pos-1000:pos+3000]
)