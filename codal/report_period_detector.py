import re


class ReportPeriodDetector:


    def __init__(self, title):

        self.title = title or ""



    def normalize(self):

        text = self.title

        replacements = {

            "\u200c": "",

            "ÙŠ": "ÛŒ",

            "Ùƒ": "Ú©",

        }


        for a, b in replacements.items():

            text = text.replace(a, b)


        return text



    def detect_months(self):

        text = self.normalize()



        rules = [

            (
                [
                    "سه ماهه",
                    "3 ماهه",
                    "Ø³Ù‡ Ù…Ø§Ù‡Ù‡",
                    "3 Ù…Ø§Ù‡Ù‡"
                ],
                3
            ),

            (
                [
                    "شش ماهه",
                    "6 ماهه",
                    "Ø´Ø´ Ù…Ø§Ù‡Ù‡",
                    "6 Ù…Ø§Ù‡Ù‡"
                ],
                6
            ),

            (
                [
                    "نه ماهه",
                    "9 ماهه",
                    "Ù†Ù‡ Ù…Ø§Ù‡Ù‡",
                    "9 Ù…Ø§Ù‡Ù‡"
                ],
                9
            ),

            (
                [
                    "دوازده ماهه",
                    "12 ماهه",
                    "Ø¯ÙˆØ§Ø²Ø¯Ù‡ Ù…Ø§Ù‡Ù‡",
                    "12 Ù…Ø§Ù‡Ù‡"
                ],
                12
            )

        ]



        for keywords, months in rules:

            for keyword in keywords:

                if keyword in text:

                    return months



        return 12



    def detect_type(self):

        months = self.detect_months()


        if months == 12:

            return "Annual actual report"


        return "Annualized estimate"



    def detect(self):

        months = self.detect_months()


        return {

            "months": months,

            "period": f"{months} months",

            "forecast_method": (

                "Annual actual report"

                if months == 12

                else

                "Annualized estimate (×12/{})".format(months)

            )

        }