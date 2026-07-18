class StockAlerts:


    def __init__(self, data):

        self.data = data



    def check(self):

        print("------------------------")
        print("هشدارهای تحلیلی")
        print("------------------------")


        warning = False



        # بررسی P/B

        if self.data["pb"] > 3:

            print(
                "⚠ P/B بالا است؛ بررسی تجدید ارزیابی دارایی‌ها"
            )

            warning = True



        # بررسی P/A

        if self.data["pa"] > 2:

            print(
                "⚠ P/A بالا است؛ ارزش بازار نسبت به دارایی‌ها زیاد است"
            )

            warning = True



        # بررسی P/E

        if self.data["pe"] > 10:

            print(
                "⚠ P/E Forward بالاتر از محدوده معمول"
            )

            warning = True



        if not warning:

            print(
                "✅ هشدار مهمی مشاهده نشد"
            )