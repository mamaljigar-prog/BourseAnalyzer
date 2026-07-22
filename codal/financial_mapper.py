from codal.financial_concept_mapper import FinancialConceptMapper


class FinancialMapper:


    def __init__(self, cells):

        self.cells = cells

        self.concept_mapper = FinancialConceptMapper()



    def extract_value(self, row_code):

        if row_code is None:
            return None


        for cell in self.cells:

            if (
                cell.get("columnCode") == 2
                and cell.get("rowCode") == row_code
            ):

                value = cell.get("value")

                if value:

                    value = (
                        str(value)
                        .replace(",", "")
                        .replace("(", "-")
                        .replace(")", "")
                    )

                    try:
                        return float(value)

                    except:

                        return value


        return None



    def map_financials(self):


        concepts = self.concept_mapper.map_income_statement(
            self.cells
        )


        result = {}


        for key, row_code in concepts.items():

            result[key] = self.extract_value(
                row_code
            )


        return result