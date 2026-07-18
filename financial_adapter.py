from financial import FinancialReport



def convert_codal_to_financial(codal_data):


    report = FinancialReport(

        period=codal_data["period"],

        months=12,

        sales=codal_data["sales"],

        operating_profit=codal_data["operating_profit"],

        net_profit=codal_data["net_profit"],

        non_operating_income=codal_data["non_operating_income"]

    )


    return report