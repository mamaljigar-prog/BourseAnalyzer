# financial/balance_sheet_mapper.py

from dataclasses import dataclass


@dataclass
class BalanceSheetData:

    assets: int = 0
    liabilities: int = 0
    equity: int = 0
    non_controlling_interest: int = 0

    def to_dict(self):

        return {
            "assets": self.assets,
            "liabilities": self.liabilities,
            "equity": self.equity,
            "non_controlling_interest": self.non_controlling_interest,
        }



class BalanceSheetMapper:


    def __init__(self, cells):

        self.cells = cells



    def normalize_text(self, value):

        if value is None:
            return ""

        text = str(value)

        replacements = {
            "\u200c": "",
            "\u200f": "",
            "\u200e": "",
            "ي": "ی",
            "ى": "ی",
            "ك": "ک",
        }

        for old, new in replacements.items():

            text = text.replace(
                old,
                new
            )

        return text.strip()



    def normalize_number(self, value):

        if value is None:

            return 0


        text = (
            str(value)
            .replace(",", "")
            .strip()
        )


        if text in (
            "",
            "-",
            "None"
        ):

            return 0


        try:

            return int(float(text))


        except Exception:

            return 0



    def get_value_by_address(self, address):

        for cell in self.cells:

            if cell.get("address") == address:

                return self.normalize_number(
                    cell.get("value")
                )

        return 0



    def get_value_by_row(self, row):

        return self.get_value_by_address(
            f"B{row}"
        )



    def find_rows(self):

        rows = {}

        for cell in self.cells:

            if cell.get("columnCode") != 1:

                continue


            text = self.normalize_text(
                cell.get("value")
            )


            address = cell.get(
                "address",
                ""
            )


            if not address.startswith("A"):

                continue


            row = int(
                address[1:]
            )


            # جمع دارایی ها

            if (
                "جمع" in text
                and "دارایی" in text
                and "بدهی" not in text
            ):

                rows["assets"] = row



            # حقوق مالکانه واقعی
            # نه جمع حقوق مالکانه و بدهی ها

            elif (
                "جمع" in text
                and "حقوق مالکانه" in text
                and "بدهی" not in text
            ):

                rows["equity"] = row



            # بدهی ها

            elif (
                "جمع" in text
                and "بدهی" in text
                and "مالکانه" not in text
            ):

                rows["liabilities"] = row



            # منافع غیرکنترلی

            elif (
                "منافع" in text
                and "غیرکنترل" in text
            ):

                rows["non_controlling_interest"] = row



        return rows



    def map(self):

        result = BalanceSheetData()


        rows = self.find_rows()



        if "assets" in rows:

            result.assets = self.get_value_by_row(
                rows["assets"]
            )


        if "equity" in rows:

            result.equity = self.get_value_by_row(
                rows["equity"]
            )


        if "liabilities" in rows:

            result.liabilities = self.get_value_by_row(
                rows["liabilities"]
            )


        if "non_controlling_interest" in rows:

            result.non_controlling_interest = self.get_value_by_row(
                rows["non_controlling_interest"]
            )



        # fallback برای گزارش‌های متفاوت کدال

        if result.assets == 0:

            result.assets = self.get_value_by_address(
                "B24"
            )


        if result.liabilities == 0:

            result.liabilities = self.get_value_by_address(
                "B59"
            )


        if result.equity == 0:

            result.equity = self.get_value_by_address(
                "B35"
            )



        if result.non_controlling_interest == 0:

            result.non_controlling_interest = self.get_value_by_address(
                "B40"
            )



        # اگر گزارش تلفیقی باشد:
        # equity + NCI باید سمت حقوق مالکانه را تشکیل دهد

        total_right_side = (
            result.equity
            +
            result.non_controlling_interest
            +
            result.liabilities
        )


        # کنترل تراز

        if (
            result.assets != total_right_side
            and result.non_controlling_interest > 0
        ):

            # در بعضی گزارش‌های تلفیقی
            # جمع حقوق مالکانه شامل NCI است
            result.equity = (
                result.assets
                -
                result.liabilities
                -
                result.non_controlling_interest
            )


        return result