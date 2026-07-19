from models.company import Company


company = Company(
    name="پتروشیمی خراسان",
    symbol="خراسان",

    sales=143134988,
    operating_profit=75110367,
    net_profit=65862967,

    assets=156582933,
    equity=95688722,

    market_cap=87350000
)


company.show()