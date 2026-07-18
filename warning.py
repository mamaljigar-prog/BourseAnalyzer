class WarningAnalyzer:


    def __init__(
        self,
        reported_profit,
        normalized_profit,
        non_recurring_income,
        pe_forward,
        pe_normalized
    ):

        self.reported_profit = reported_profit
        self.normalized_profit = normalized_profit
        self.non_recurring_income = non_recurring_income
        self.pe_forward = pe_forward
        self.pe_normalized = pe_normalized



    def analyze(self):

        warnings = []



        # سهم سود غیرتکرارشونده

        if self.reported_profit > 0:

            non_recurring_percent = (

                self.non_recurring_income
                /
                self.reported_profit

            ) * 100


            if non_recurring_percent > 10:

                warnings.append(

                    f"⚠ {round(non_recurring_percent,1)}٪ سود از محل غیرتکرارشونده است"

                )



        # اختلاف سود گزارش شده و نرمال

        if self.normalized_profit < self.reported_profit * 0.8:

            warnings.append(

                "⚠ بخش قابل توجهی از سود گزارش شده قابل اتکا نیست"

            )



        # P/E واقعی

        if self.pe_normalized > self.pe_forward * 1.2:

            warnings.append(

                "⚠ P/E نرمال‌شده بالاتر از P/E ظاهری است"

            )



        return warnings



    def show(self):

        print("------------------------------")
        print("هشدارهای تحلیلی")
        print("------------------------------")


        warnings = self.analyze()



        if len(warnings) == 0:

            print(
                "✅ هشدار مهمی مشاهده نشد"
            )


        else:

            for warning in warnings:

                print(warning)