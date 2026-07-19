# codal_financial_parser.py


class CodalFinancialParser:


    def __init__(self):

        pass



    def parse(self):


        data = {


            # فروش دوره جاری
            "sales": 143134988,


            # فروش دوره مشابه سال قبل
            # فعلا تستی - بعداً از اکسل کدال استخراج می‌شود
            "previous_sales": 120000000,



            "operating_profit": 75110367,


            "net_profit": 65862967,


            "assets": 156582933,


            "equity": 95688722,


            "cash_flow": 38332725


        }


        return data




if __name__ == "__main__":


    parser = CodalFinancialParser()


    result = parser.parse()


    print("================")
    print("دریافت اطلاعات کدال")
    print("================")


    for k, v in result.items():

        print(
            k,
            ":",
            v
        )