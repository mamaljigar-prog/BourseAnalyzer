class BalanceSheetSelector:


    def __init__(self, reports):

        self.reports = reports



    def select(self):


        candidates = []


        for report in self.reports:


            title = report.get(
                "title",
                ""
            )


            # حذف گزارش‌های توضیحی
            if "توضیحات" in title:
                continue


            # اولویت با سالانه حسابرسی شده
            if (
                "سال مالی" in title
                and
                "حسابرسی شده" in title
            ):

                return report



            candidates.append(report)



        # اگر سالانه نبود، اولین گزارش کامل
        if candidates:

            return candidates[0]



        return None