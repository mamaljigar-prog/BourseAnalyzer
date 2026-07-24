class FinancialConceptMapper:


    def normalize(self, text):

        if text is None:
            return ""


        text = str(text)


        replacements = {

            "ي": "ی",
            "ى": "ی",
            "ئ": "ی",

            "ك": "ک",

            "ۀ": "ه",
            "ة": "ه",

            "‌": "",
            " ": "",

            "\u200f": "",
            "\u200e": "",

            "(": "",
            ")": "",

            "ـ": "",
            "-": "",

            "زيان": "زیان",
            "عمليات": "عملیات",
            "عملياتى": "عملیاتی"

        }


        for a, b in replacements.items():

            text = text.replace(
                a,
                b
            )


        return text.lower()



    def get_rows(self, cells):

        rows = {}


        for cell in cells:


            if cell.get("columnCode") != 1:

                continue


            row_code = cell.get(
                "rowCode"
            )


            title = cell.get(
                "value",
                ""
            )


            if row_code:

                rows[row_code] = self.normalize(
                    title
                )


        return rows



    def score_match(
        self,
        title,
        include_words,
        exclude_words=None
    ):


        if exclude_words is None:

            exclude_words = []


        score = 0


        for word in include_words:


            word = self.normalize(
                word
            )


            if word in title:

                score += 10

            else:

                return -1



        for word in exclude_words:


            word = self.normalize(
                word
            )


            if word in title:

                score -= 20



        return score



    def find_best_match(
        self,
        rows,
        include_words,
        exclude_words=None
    ):


        best_code = None
        best_score = -1


        for code, title in rows.items():


            score = self.score_match(
                title,
                include_words,
                exclude_words
            )


            if score > best_score:

                best_score = score
                best_code = code



        return best_code



    def map_income_statement(self, cells):


        rows = self.get_rows(
            cells
        )


        result = {

            "sales": None,

            "gross_profit": None,

            "operating_profit": None,

            "net_profit": None,

            "non_operating_income": None

        }



        result["sales"] = self.find_best_match(

            rows,

            [
                "درآمد",
                "عملیاتی"
            ],

            [
                "هزینه",
                "هرسهم",
                "تغییرات"
            ]

        )



        result["gross_profit"] = self.find_best_match(

            rows,

            [
                "سود",
                "ناخالص"
            ],

            [
                "هرسهم"
            ]

        )



        result["operating_profit"] = self.find_best_match(

            rows,

            [
                "سود",
                "عملیاتی"
            ],

            [
                "خالص",
                "ناخالص",
                "هرسهم",
                "پایه",
                "مالیات"
            ]

        )



        result["net_profit"] = self.find_best_match(

            rows,

            [
                "سود",
                "خالص"
            ],

            [
                "ناخالص",
                "عملیاتی",
                "هرسهم",
                "پایه",
                "قبل"
            ]

        )



        result["non_operating_income"] = self.find_best_match(

            rows,

            [
                "غیرعملیاتی"
            ],

            [
                "هرسهم"
            ]

        )


        return result