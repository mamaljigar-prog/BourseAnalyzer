class FinancialMapper:


    def __init__(self, cells):

        self.cells = cells



    def normalize(self, text):

        if not text:
            return ""

        replacements = {
            "ي":"ی",
            "ى":"ی",
            "ك":"ک",
            "‌":" ",
            "\u200f":"",
            "\u200c":" "
        }

        for a,b in replacements.items():
            text = text.replace(a,b)

        return text.strip()



    def find_best_row(self, patterns):

        best_row = None
        best_score = 0


        for cell in self.cells:


            value = self.normalize(
                str(cell.get("value",""))
            )


            score = 0


            for pattern,weight in patterns:

                if pattern in value:

                    score += weight



            if score > best_score:

                best_score = score
                best_row = cell.get("rowCode")



        return best_row




    def extract_value(self,row):

        if row is None:
            return None


        for cell in self.cells:

            if cell.get("rowCode") == row:


                value = cell.get("value")


                if isinstance(value,(int,float)):
                    return value


                try:
                    return int(
                        str(value).replace(",","")
                    )

                except:
                    continue


        return None




    def map_financials(self):


        rules = {


            "sales":[
                ("درآمدهای عملیاتی",10),
                ("درآمدهاي عملياتي",10),
                ("درآمد",3),
                ("عملیاتی",3)
            ],



            "gross_profit":[
                ("سود(زیان) ناخالص",10),
                ("سود(زیان) ناخالص",10),
                ("ناخالص",5)
            ],



            "operating_profit":[
                ("سود(زیان) عملیاتی",10),
                ("سود(زیان) عملياتى",10),
                ("عملیاتی",5)
            ],



            "net_profit":[
                ("سود(زیان) خالص عملیات در حال تداوم",15),
                ("سود(زیان) خالص",10),
                ("سود (زیان) خالص",10),
                ("خالص",3)
            ]

        }



        result={}


        for name,patterns in rules.items():

            row = self.find_best_row(patterns)

            result[name] = self.extract_value(row)



        return result