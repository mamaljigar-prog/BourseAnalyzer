import requests

url = "https://codal.ir/Reports/Attachment.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw=="


t = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text


for key in [
    "xlsx",
    "xls",
    "zip",
    "Attachment",
    "Download",
    "File"
]:

    print(key, t.find(key))


print("================")
print(t[:2000])