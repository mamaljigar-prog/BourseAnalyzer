class MonthlyAnalyzer:

    def __init__(self, sales_data):
        self.sales_data = sales_data


    def total_sales(self):
        total = 0

        for item in self.sales_data:
            try:
                total += float(item["amount"])
            except:
                pass

        return total


    def product_growth(self):

        result = []

        total = self.total_sales()

        for item in self.sales_data:

            try:
                amount = float(item["amount"])
            except:
                amount = 0

            share = 0

            if total > 0:
                share = amount / total * 100

            result.append({
                "name": item["name"],
                "amount": amount,
                "share": round(share,2)
            })

        return result


    def report(self):

        print("================")
        print("تحلیل فروش ماهانه")
        print("================")

        total = self.total_sales()

        print(
            f"جمع فروش: {total:,.0f} میلیون ریال"
        )

        print("----------------")

        for x in self.product_growth():

            if x["amount"] > 0:

                print(
                    f'{x["name"]} | '
                    f'{x["amount"]:,.0f} میلیون ریال | '
                    f'سهم فروش: {x["share"]}%'
                )