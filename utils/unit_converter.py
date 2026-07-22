# utils/unit_converter.py


class UnitConverter:
    """
    تبدیل واحدهای مالی پروژه BourseAnalyzer

    قوانین:
    1- داده های کدال معمولاً هزار ریال هستند.
    2- خروجی تحلیل ارزش گذاری تومان است.
    3- تبدیل واحد فقط از این کلاس انجام می شود.
    """


    def __init__(self):
        pass



    def rial_thousand_to_toman(
        self,
        value
    ):
        """
        هزار ریال به تومان
        """

        if value is None:
            return 0

        return value * 100



    # نام سازگار با کدهای قبلی پروژه
    def codal_thousand_rial_to_toman(
        self,
        value
    ):
        """
        تبدیل مقدار استخراج شده از کدال
        """

        return self.rial_thousand_to_toman(
            value
        )



    def to_toman(
        self,
        value
    ):

        return self.rial_thousand_to_toman(
            value
        )



    def normalize_market_cap(
        self,
        value,
        unit="toman"
    ):
        """
        استاندارد ارزش بازار
        """

        if value is None:
            return 0


        if unit == "rial_thousand":

            return self.rial_thousand_to_toman(
                value
            )


        return value



if __name__ == "__main__":

    converter = UnitConverter()


    print(
        converter.codal_thousand_rial_to_toman(
            115068905
        )
    )