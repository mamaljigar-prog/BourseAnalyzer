# financial_model.py

def percent(a, b):
    if b == 0 or b is None:
        return None
    return round((a / b) * 100, 2)


def analyze(data):
    
    sales = data.get("درآمدهاي عملياتي")
    net_profit = data.get("سود(زيان) خالص")
    assets = data.get("جمع دارايي‌ها")
    equity = data.get("جمع حقوق مالکانه")
    debt = data.get("جمع بدهي‌ها")
    operating_profit = data.get("سود(زيان) عملياتى")
    cash_operation = data.get(
        "جريان ‌خالص ‌ورود‌ (خروج) ‌نقد حاصل از فعاليت‌هاي ‌عملياتي"
    )


    print("\n======================")
    print("تحلیل مالی شرکت")
    print("======================")

    print(f"فروش عملیاتی: {sales}")
    print(f"سود عملیاتی: {operating_profit}")
    print(f"سود خالص: {net_profit}")

    print("----------------------")

    if sales:
        print(
            "حاشیه سود خالص:",
            percent(net_profit, sales),
            "%"
        )

    if assets:
        print(
            "ROA:",
            percent(net_profit, assets),
            "%"
        )

    if equity:
        print(
            "ROE:",
            percent(net_profit, equity),
            "%"
        )

    print("----------------------")

    print("دارایی‌ها:", assets)
    print("حقوق مالکانه:", equity)
    print("بدهی:", debt)

    print("----------------------")

    print(
        "جریان نقد عملیاتی:",
        cash_operation
    )