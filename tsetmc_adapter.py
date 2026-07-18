from tsetmc import get_instrument, get_price


class TsetmcAdapter:

    def __init__(self, ins_code):
        self.ins_code = ins_code


    def format_money(self, value):

        # تومان به همت (هزار میلیارد تومان)
        hamat = value / 1_000_000_000_000

        if hamat >= 1000:
            return f"{hamat/1000:.1f} تریلیون تومان"

        return f"{hamat:,.0f} همت"


    def get_stock_data(self):

        info = get_instrument(self.ins_code)
        price = get_price(self.ins_code)


        if not info or not price:
            return None


        # قیمت TSETMC ریال است
        # تبدیل ارزش بازار به تومان

        market_value = (
            info["shares"]
            *
            price["closing_price"]
        ) / 10


        return {

            "symbol": info["symbol"],

            "company": info["company"],

            "shares": info["shares"],

            "market": info["market"],

            "last_price": price["last_price"],

            "closing_price": price["closing_price"],

            "volume": price["volume"],

            "market_value": market_value,

            "market_value_text": self.format_money(
                market_value
            )
        }