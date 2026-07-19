def to_billion_toman(value, unit="million_rial"):

    if value is None:
        return 0

    if unit == "million_rial":
        return round(value / 10000, 2)

    if unit == "billion_rial":
        return round(value / 10, 2)

    if unit == "toman":
        return round(value / 1_000_000_000, 2)

    if unit == "billion_toman":
        return round(value, 2)

    return 0



def normalize_financials(
        sales,
        net_profit,
        assets,
        equity
):

    return {

        "sales":
            to_billion_toman(sales),

        "net_profit":
            to_billion_toman(net_profit),

        "assets":
            to_billion_toman(assets),

        "equity":
            to_billion_toman(equity)

    }