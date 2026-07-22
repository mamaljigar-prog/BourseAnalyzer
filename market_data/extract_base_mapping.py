import requests
import re


js_url = "https://www.tsetmc.com/main.9d60e7997e683da143f0.js"


text = requests.get(
    js_url,
    headers={"User-Agent":"Mozilla/5.0"},
    timeout=20
).text


patterns = [
    r'Instrument.{0,100}"https://[^"]+',
    r'Instrument.{0,100}https?://[^"]+',
    r'const [A-Za-z0-9_]+=\([^)]*\)=>"https://[^"]+"',
]


for p in patterns:
    print("\nPATTERN:", p)

    result = re.findall(p,text)

    for x in result[:20]:
        print(x)