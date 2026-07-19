# codal_parser.py

import pandas as pd


def clean_number(x):

    if pd.isna(x):
        return None

    x = str(x)

    x = x.translate(
        str.maketrans(
            "۰۱۲۳۴۵۶۷۸۹",
            "0123456789"
        )
    )

    x = x.replace(",", "")

    if "(" in x and ")" in x:
        x = x.replace("(", "")
        x = x.replace(")", "")

        try:
            return -int(x)
        except:
            return None

    try:
        return int(x)

    except:
        return None



def find_value(df, keyword):

    col = df.iloc[:,0].astype(str)

    exact = df[
        col.str.strip() == keyword
    ]

    if len(exact):
        return clean_number(
            exact.iloc[0,1]
        )


    result = df[
        col.str.contains(
            keyword,
            regex=False,
            na=False
        )
    ]


    if len(result):
        return clean_number(
            result.iloc[0,1]
        )


    return None



def read_codal(file="codal_output.bin"):


    tables = pd.read_html(file)


    # صورت سود و زیان

    income = tables[0]


    revenue = find_value(
        income,
        "درآمدهاي عملياتي"
    )


    operating_profit = find_value(
        income,
        "سود(زيان) عملياتى"
    )


    net_profit = find_value(
        income,
        "سود(زيان) خالص"
    )



    # ترازنامه

    balance = tables[4]


    assets = find_value(
        balance,
        "جمع دارايي‌ها"
    )


    equity = find_value(
        balance,
        "جمع حقوق مالکانه"
    )



    return {

        "sales": revenue,

        "operating_profit": operating_profit,

        "net_profit": net_profit,

        "assets": assets,

        "equity": equity

    }



# تست مستقل

if __name__ == "__main__":


    data = read_codal()


    print("===================")
    print("CODAL DATA")
    print("===================")


    for k,v in data.items():

        print(
            k,
            ":",
            v
        )