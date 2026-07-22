# market_data/market_cap_provider.py


class MarketCapProvider:
    """
    تامین کننده اطلاعات ارزش بازار

    قوانین پروژه:
    1- ارزش بازار از منبع بازار گرفته می شود.
    2- P/E سایت TSETMC استفاده نمی شود.
    3- فقط ارزش بازار و قیمت برای محاسبات استفاده می شوند.
    4- واحد خروجی استاندارد = تومان.
    """


    def __init__(self):

        pass



    def normalize_market_cap(
        self,
        market_cap,
        unit="toman"
    ):
        """
        استانداردسازی ارزش بازار

        فعلا ورودی تستی:
        تومان

        بعداً به TSETMC متصل می شود.
        """

        if market_cap is None:
            return 0


        return market_cap



    def get_market_data(
        self,
        symbol,
        market_cap
    ):
        """
        خروجی استاندارد اطلاعات بازار
        """

        return {

            "symbol": symbol,

            "market_cap":
                self.normalize_market_cap(
                    market_cap
                )

        }



if __name__ == "__main__":


    provider = MarketCapProvider()


    data = provider.get_market_data(

        symbol="TEST",

        market_cap=87350000000

    )


    print(data)