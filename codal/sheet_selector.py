class SheetSelector:


    def __init__(self, sheets):

        self.sheets = sheets or []



    def normalize(self, text):

        if not text:

            return ""

        return (
            str(text)
            .replace("\u200c", "")
            .replace("\u200e", "")
            .replace("\u200f", "")
            .replace("ي", "ی")
            .replace("ك", "ک")
            .strip()
        )



    def find_sheet(
        self,
        keywords
    ):

        for sheet in self.sheets:

            title = self.normalize(
                sheet.get(
                    "title_Fa",
                    ""
                )
            )


            for keyword in keywords:

                if keyword in title:

                    return sheet


        return None



    def find_income_statement(self):

        return self.find_sheet(

            [
                "صورت سود",
                "سود و زیان",
                "صورت سود و زیان"
            ]

        )



    def find_balance_sheet(self):

        return self.find_sheet(

            [
                "صورت وضعیت مالی",
                "ترازنامه"
            ]

        )



    def report(self):

        income = self.find_income_statement()

        balance = self.find_balance_sheet()


        return {

            "income_statement": income,

            "balance_sheet": balance

        }