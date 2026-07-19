# main_analysis.py

from codal_parser import read_codal
from valuation import calculate_valuation



print("==============================")
print("      BOURSE ANALYZER")
print("==============================")


# دریافت اطلاعات کدال

financial = read_codal()


print("\n===== Financial Data =====")

for key, value in financial.items():

    print(
        key,
        ":",
        value
    )



# فعلا ارزش بازار نمونه است
# مرحله بعد از TSETMC می‌گیریم

market_cap = 8735


# تبدیل ریال کدال به میلیارد تومان
# کدال اعداد را میلیون ریال می‌دهد
# 10 میلیون ریال = 1 میلیون تومان

sales = financial["sales"] / 10

profit = financial["net_profit"] / 10

assets = financial["assets"] / 10

equity = financial["equity"] / 10



# محاسبه ارزش‌گذاری

valuation = calculate_valuation(

    market_cap,

    sales,

    profit,

    assets,

    equity

)



print("\n===== VALUATION =====")


for key, value in valuation.items():

    if value is not None:

        print(
            key,
            ":",
            round(value,2)
        )

    else:

        print(
            key,
            ": None"
        )