from tsetmc import get_instrument, get_price


class TsetmcAdapter:

    def __init__(self, ins_code):
        self.ins_code = ins_code


    def format_money(self, value):

        # value بر حسب میلیارد تومان است
        if value >= 1000:

            return f"{value:,.0f} میلیارد تومان"

        return f"{value:,.0f} میلیارد تومان"



    def get_stock_data(self):

        info = get_instrument(self.ins_code)

        price = get_price(self.ins_code)


        if not info or not price:
            return None



        # TSETMC:
        # قیمت به ریال است
        # خروجی پروژه: میلیارد تومان

        market_value = (

            info["shares"]

            *

            price["closing_price"]

        ) / 10 / 1_000_000_000



        return {


            "symbol": info["symbol"],

            "company": info["company"],

            "shares": info["shares"],

            "market": info["market"],


            "last_price": price["last_price"],

            "closing_price": price["closing_price"],

            "volume": price["volume"],


            # میلیارد تومان

            "market_value": market_value,


            "market_value_text": self.format_money(
                market_value
            )

        }