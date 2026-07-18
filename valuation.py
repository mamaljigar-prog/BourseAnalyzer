def market_cap_toman(price_rial, shares):
    """
    ارزش بازار به میلیارد تومان

    قیمت TSETMC به ریال است
    """

    market_cap_rial = price_rial * shares

    market_cap_toman = market_cap_rial / 10

    market_cap_billion = market_cap_toman / 1_000_000_000

    return market_cap_billion



def forward_profit(sales_billion_toman, net_margin):
    """
    سود خالص پیش بینی شده
    فروش × حاشیه سود خالص
    """

    return sales_billion_toman * net_margin



def forward_pe(market_cap_billion, profit_billion):
    """
    P/E Forward
    """

    return market_cap_billion / profit_billion



def forward_ps(market_cap_billion, sales_billion):
    """
    P/S Forward
    """

    return market_cap_billion / sales_billion



def future_value_by_pe(profit_billion, pe=7):
    """
    ارزش بازار آینده با PE مبنا
    """

    return profit_billion * pe