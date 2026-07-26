class FinancialConceptMapper:


    def normalize(self, text):

        if text is None:
            return ""

        text = str(text)

        replacements = {

            "ي": "ی",
            "ى": "ی",
            "ك": "ک",

            "ۀ": "ه",

            "‌": "",
            "\u200f": "",
            "\u200e": "",

            "(": "",
            ")": "",

            "ـ": "",

            " ": "",

            "‌": ""

        }


        for a, b in replacements.items():
            text = text.replace(a, b)


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

            normalized = self.normalize(
                word
            )


            if normalized in title:

                score += 10

            else:

                return -1



        for word in exclude_words:

            normalized = self.normalize(
                word
            )


            if normalized in title:

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



    def map_income_statement(
        self,
        cells
    ):


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



        # درآمد عملیاتی

        result["sales"] = self.find_best_match(

            rows,

            [
                "درآمد",
                "عملیاتی"
            ],

            [
                "هزینه",
                "هرسهم"
            ]

        )



        # سود ناخالص

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



        # سود عملیاتی
        # الگوی واقعی Codal:
        # سود(زیان) عملیاتى

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

                "قبل",

                "مالیات"

            ]

        )


        if result["operating_profit"] is None:


            result["operating_profit"] = self.find_best_match(

                rows,

                [
                    "سود",
                    "زیان",
                    "عملیاتی"
                ]

            )



        # سود خالص

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

                "قبل",

                "مالیات"

            ]

        )



        # درآمد غیرعملیاتی

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