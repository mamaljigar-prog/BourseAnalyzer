import re



class ReportPeriodDetector:


    def __init__(self, title):

        self.title = title or ""



    def detect_months(self):

        text = self.title.replace(
            "\u200c",
            ""
        )



        rules = [

            (
                [
                    "سه ماهه",
                    "3 ماهه"
                ],
                3
            ),

            (
                [
                    "شش ماهه",
                    "6 ماهه"
                ],
                6
            ),

            (
                [
                    "نه ماهه",
                    "9 ماهه"
                ],
                9
            ),

            (
                [
                    "دوازده ماهه",
                    "12 ماهه"
                ],
                12
            )

        ]



        for keywords, months in rules:

            for keyword in keywords:

                if keyword in text:

                    return months



        # گزارش‌های سالانه معمولاً عبارت مشخص ماه ندارند

        return 12