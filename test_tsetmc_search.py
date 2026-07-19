import requests

url = "https://cdn.tsetmc.com/api/Instrument/GetInstrumentSearch/خراسان"

r = requests.get(url, timeout=10)

print(r.json())