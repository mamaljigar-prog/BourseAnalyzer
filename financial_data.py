# financial_data.py

from codal_financial_parser import CodalFinancialParser


def get_financial_data():

    parser = CodalFinancialParser()

    data = parser.parse()

    return data



if __name__ == "__main__":

    data = get_financial_data()

    print("================")
    print("اطلاعات مالی استاندارد")
    print("================")

    for k, v in data.items():
        print(k, ":", v)