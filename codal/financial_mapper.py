from codal.financial_concept_mapper import FinancialConceptMapper


class FinancialMapper:


    def __init__(self, cells):

        self.cells = cells

        self.concept_mapper = FinancialConceptMapper()



    def extract_value(self, row_code):


        if row_code is None:

            return 0



        print(
            "DEBUG EXTRACT ROW:",
            row_code
        )


        found = False



        for cell in self.cells:


            if cell.get("rowCode") == row_code:


                found = True


                print(
                    "CELL:",
                    cell
                )


                column = cell.get(
                    "columnCode"
                )


                # ستون اصلی گزارش معمولا 2 است
                # ولی بعضی گزارش‌ها ممکن است متفاوت باشند

                if column in [2, 3, 4]:


                    value = cell.get(
                        "value"
                    )


                    if value is None:

                        continue



                    value = (

                        str(value)

                        .replace(",", "")

                        .replace("(", "-")

                        .replace(")", "")

                        .replace(" ", "")

                    )


                    try:

                        return int(
                            float(value)
                        )


                    except:


                        continue




        if not found:

            print(
                "ROW NOT FOUND:",
                row_code
            )


        return 0





    def map_financials(self):


        concepts = self.concept_mapper.map_income_statement(

            self.cells

        )



        print()

        print(
            "DEBUG MAPPED CONCEPTS"
        )

        print(
            concepts
        )

        print()



        result = {}



        for key, row_code in concepts.items():


            result[key] = self.extract_value(

                row_code

            )



        return result