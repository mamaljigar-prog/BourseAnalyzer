from financial import FinancialReport



def convert_codal_to_financial(codal_data):


    report = FinancialReport(

        period=codal_data["period"],

        months=codal_data.get(
            "months",
            12
        ),


        fiscal_end_date=codal_data.get(
            "fiscal_end_date",
            None
        ),


        sales=codal_data["sales"],


        operating_profit=codal_data["operating_profit"],


        net_profit=codal_data["net_profit"],


        non_operating_income=codal_data.get(
            "non_operating_income",
            0
        ),


        assets=codal_data.get(
            "assets",
            0
        ),


        equity=codal_data.get(
            "equity",
            0
        ),


        cash_flow=codal_data.get(
            "cash_flow",
            0
        )

    )


    return report