from codal.financial_service import FinancialService


if __name__ == "__main__":

    service = FinancialService()

    result = service.get_financial_data(
        "شپنا"
    )

    print(result)