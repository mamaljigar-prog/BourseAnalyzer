class MonthlyAnalyzer:


    def __init__(self, monthly_data):
        self.data = monthly_data



    def total_sales(self):

        total = 0

        for item in self.data:

            total += float(
                item.get("amount",0)
            )

        return total



    def product_share(self):

        total = self.total_sales()

        result = []


        for item in self.data:

            amount = float(
                item.get("amount",0)
            )

            share = 0

            if total:
                share = amount / total * 100


            result.append(
                {
                    "product":item["name"],
                    "amount":amount,
                    "share":round(share,2)
                }
            )


        return result



    def print_report(self):


        print("====================")
        print("تحلیل فروش ماهانه")
        print("====================")


        total = self.total_sales()


        print(
            "کل فروش:",
            total,
            "میلیون ریال"
        )


        print("--------------------")


        for x in self.product_share():

            print(
                x["product"],
                "|",
                x["amount"],
                "میلیون ریال",
                "| سهم:",
                x["share"],
                "%"
            )