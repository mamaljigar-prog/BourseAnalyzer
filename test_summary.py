from codal_monthly import CodalMonthly
import json

url = "لینک واقعی کدال"

codal = CodalMonthly(url)

data = codal.get_sales_summary()

print("================")
print("خلاصه فروش")
print("================")

print(json.dumps(data, ensure_ascii=False, indent=4))

with open("sales_summary.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)