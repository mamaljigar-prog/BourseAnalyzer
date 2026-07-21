import requests
import re


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"


html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text


start = html.find("<select name=\"ctl00$ddlTable\"")

end = html.find("</select>", start)


part = html[start:end]


print(part[:1000])