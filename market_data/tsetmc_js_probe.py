import requests
import re


url = "https://www.tsetmc.com"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=10
)


print("STATUS:", r.status_code)


scripts = re.findall(
    r'<script[^>]+src="([^"]+)"',
    r.text
)


print("\nSCRIPTS:")

for s in scripts:
    print(s)