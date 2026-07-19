import requests


url = "https://excel.codal.ir/service/Excel/GetAll/OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d/0"


headers = {
    "User-Agent": "Mozilla/5.0"
}


r = requests.get(
    url,
    headers=headers,
    timeout=60
)


print("Status:", r.status_code)
print("Content-Type:", r.headers.get("Content-Type"))
print("Length:", len(r.content))


print("\nاولین 100 بایت:")
print(r.content[:100])


with open("codal_output.bin","wb") as f:
    f.write(r.content)


print("\nفایل ذخیره شد: codal_output.bin")