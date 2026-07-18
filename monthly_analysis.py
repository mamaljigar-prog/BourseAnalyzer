class MonthlyAnalyzer:


    def __init__(self, data):
        self.data = data



    def total_sales(self):

        total = 0

        for item in self.data:

            try:
                total += float(item["amount"])
            except:
                pass

        return total



    def sales_share(self):

        total = self.total_sales()

        result = []

        for item in self.data:

            try:
                amount=float(item["amount"])
            except:
                amount=0


            share=0

            if total:
                share=(amount/total)*100


            result.append({

                "name":item["name"],
                "amount":amount,
                "share":round(share,2)

            })


        return result



    def report(self):

        print("===================")
        print("تحلیل فروش ماهانه")
        print("===================")


        print(
            "کل فروش:",
            self.total_sales(),
            "میلیون ریال"
        )


        print("-------------------")


        for x in self.sales_share():

            if x["amount"]>0:

                print(
                    f'{x["name"]} | '
                    f'{x["amount"]} '
                    f'میلیون ریال | '
                    f'سهم: {x["share"]}%'
                )