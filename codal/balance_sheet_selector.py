class SheetSelector:

    def __init__(self, sheets):
        self.sheets = sheets or []


    def normalize(self, text):

        if not text:
            return ""

        text = str(text)

        replacements = {
            "\u200c": "",
            "\u200e": "",
            "\u200f": "",
            "ÙŠ": "ی",
            "Ù‰": "ی",
            "Ùƒ": "ک",
            "ÛŒ": "ی",
            "Ú©": "ک",
        }

        for a, b in replacements.items():
            text = text.replace(a, b)

        return text.strip()



    def get_title(self, sheet):

        return self.normalize(
            sheet.get("title_Fa")
            or
            sheet.get("title")
            or
            sheet.get("name")
            or
            ""
        )



    def find_sheet(self, keywords):

        for sheet in self.sheets:

            title = self.get_title(sheet)

            for keyword in keywords:

                if keyword in title:

                    return sheet

        return None



    def find_income_statement(self):

        return self.find_sheet(
            [
                "صورت سود و زیان",
                "سود و زیان",
                "صورت سود"
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