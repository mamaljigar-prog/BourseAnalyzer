import json

with open("codal_data.json", "w", encoding="utf-8") as f:
    json.dump({
        "sales": sales,
        "operating_profit": operating_profit,
        "net_profit": net_profit,
        "assets": assets,
        "equity": equity
    }, f, ensure_ascii=False, indent=4)

print("CODAL DATA SAVED")