from codal.codal_profit_loss_parser import CodalProfitLossParser


class FinancialAdapter:

    def __init__(self, url, period_months=None):

        self.url = url
        self.period_months = period_months

    # =========================================================
    # MAIN REPORT
    # =========================================================

    def report(self):

        parser = CodalProfitLossParser(
            self.url
        )

        data = parser.get_financial_data()

        # =====================================================
        # PERIOD MONTHS
        # =====================================================

        detected_period_months = (
            self.detect_period_months(
                parser
            )
        )

        if (
            detected_period_months
            and
            detected_period_months > 0
        ):

            self.period_months = (
                detected_period_months
            )

        elif (
            self.period_months is not None
            and
            self.period_months > 0
        ):

            self.period_months = (
                self.period_months
            )

        else:

            self.period_months = 12

        # =====================================================
        # EXTRACT SEMANTIC DATA
        # =====================================================

        semantic = data.get(
            "semantic",
            {}
        )

        sales = self.build_concept_data(
            semantic.get(
                "sales",
                {}
            )
        )

        gross_profit = self.build_concept_data(
            semantic.get(
                "gross_profit",
                {}
            )
        )

        operating_profit = self.build_concept_data(
            semantic.get(
                "operating_profit",
                {}
            )
        )

        non_operating_income = self.build_concept_data(
            semantic.get(
                "non_operating_income",
                {}
            )
        )

        net_profit = self.build_concept_data(
            semantic.get(
                "net_profit",
                {}
            )
        )

        # =====================================================
        # STRUCTURED RESULT
        # =====================================================

        current = {

            "sales":
                sales["current"],

            "gross_profit":
                gross_profit["current"],

            "operating_profit":
                operating_profit["current"],

            "non_operating_income":
                non_operating_income[
                    "current"
                ],

            "net_profit":
                net_profit["current"]

        }

        previous = {

            "sales":
                sales["previous"],

            "gross_profit":
                gross_profit["previous"],

            "operating_profit":
                operating_profit[
                    "previous"
                ],

            "non_operating_income":
                non_operating_income[
                    "previous"
                ],

            "net_profit":
                net_profit["previous"]

        }

        annual = {

            "sales":
                sales["annual"],

            "gross_profit":
                gross_profit["annual"],

            "operating_profit":
                operating_profit[
                    "annual"
                ],

            "non_operating_income":
                non_operating_income[
                    "annual"
                ],

            "net_profit":
                net_profit["annual"]

        }

        result = {

            "current":
                current,

            "previous":
                previous,

            "annual":
                annual,

            "period_months":
                self.period_months

        }

        # =====================================================
        # DEBUG
        # =====================================================

        self.debug_report(
            result
        )

        return result

    # =========================================================
    # BUILD CONCEPT DATA
    # =========================================================

    def build_concept_data(
        self,
        semantic
    ):

        if not semantic:

            return {

                "current": 0,

                "previous": 0,

                "annual": 0,

                "change": 0

            }

        return {

            "current":
                self.safe_int(
                    semantic.get(
                        "current",
                        0
                    )
                ),

            "previous":
                self.safe_int(
                    semantic.get(
                        "previous",
                        0
                    )
                ),

            "annual":
                self.safe_int(
                    semantic.get(
                        "annual",
                        0
                    )
                ),

            "change":
                self.safe_int(
                    semantic.get(
                        "change",
                        0
                    )
                )

        }

    # =========================================================
    # PERIOD DETECTION
    # =========================================================

    def detect_period_months(
        self,
        parser
    ):

        try:

            cells = parser.get_cells()

            mapping = (
                parser.detect_column_mapping(
                    cells
                )
            )

        except Exception:

            return None

        current_dates = []

        for column_code, info in mapping.items():

            if not isinstance(
                info,
                dict
            ):

                continue

            role = info.get(
                "role"
            )

            if role != "current":

                continue

            date = info.get(
                "date"
            )

            if not date:

                continue

            current_dates.append(
                date
            )

        if not current_dates:

            return None

        # =====================================================
        # CURRENT REPORT DATE
        # =====================================================

        current_date = max(
            current_dates
        )

        year = current_date[0]
        month = current_date[1]
        day = current_date[2]

        # =====================================================
        # PERIOD MONTH ESTIMATION
        #
        # Codal reports are normally cumulative from the
        # beginning of the financial year.
        #
        # Example:
        #
        # 1405/03/31 -> 3 months
        # 1405/06/31 -> 6 months
        # 1405/09/30 -> 9 months
        # 1405/12/29 -> 12 months
        #
        # This is intentionally based on the report month.
        # ForecastEngine will perform annualization later.
        # =====================================================

        if month in (
            1,
            2,
            3
        ):

            period_months = 3

        elif month in (
            4,
            5,
            6
        ):

            period_months = 6

        elif month in (
            7,
            8,
            9
        ):

            period_months = 9

        elif month in (
            10,
            11,
            12
        ):

            period_months = 12

        else:

            period_months = None

        print()

        print(
            "DETECTED PERIOD MONTHS:",
            period_months
        )

        print(
            "CURRENT REPORT DATE:",
            f"{year}/{month:02d}/{day:02d}"
        )

        print()

        return period_months

    # =========================================================
    # DEBUG REPORT
    # =========================================================

    def debug_report(
        self,
        result
    ):

        current = result.get(
            "current",
            {}
        )

        previous = result.get(
            "previous",
            {}
        )

        annual = result.get(
            "annual",
            {}
        )

        print()

        print(
            "DEBUG FINANCIAL ADAPTER"
        )

        print(
            "----------------------"
        )

        print(
            "Period Months:",
            result.get(
                "period_months"
            )
        )

        print()

        print(
            "Current:"
        )

        print(
            "Sales:",
            current.get(
                "sales",
                0
            )
        )

        print(
            "Gross Profit:",
            current.get(
                "gross_profit",
                0
            )
        )

        print(
            "Operating Profit:",
            current.get(
                "operating_profit",
                0
            )
        )

        print(
            "Non Operating:",
            current.get(
                "non_operating_income",
                0
            )
        )

        print(
            "Net Profit:",
            current.get(
                "net_profit",
                0
            )
        )

        print()

        print(
            "Previous:"
        )

        print(
            "Sales:",
            previous.get(
                "sales",
                0
            )
        )

        print(
            "Gross Profit:",
            previous.get(
                "gross_profit",
                0
            )
        )

        print(
            "Operating Profit:",
            previous.get(
                "operating_profit",
                0
            )
        )

        print(
            "Non Operating:",
            previous.get(
                "non_operating_income",
                0
            )
        )

        print(
            "Net Profit:",
            previous.get(
                "net_profit",
                0
            )
        )

        print()

        print(
            "Annual:"
        )

        print(
            "Sales:",
            annual.get(
                "sales",
                0
            )
        )

        print(
            "Gross Profit:",
            annual.get(
                "gross_profit",
                0
            )
        )

        print(
            "Operating Profit:",
            annual.get(
                "operating_profit",
                0
            )
        )

        print(
            "Non Operating:",
            annual.get(
                "non_operating_income",
                0
            )
        )

        print(
            "Net Profit:",
            annual.get(
                "net_profit",
                0
            )
        )

        print(
            "----------------------"
        )

        print()

    # =========================================================
    # SAFE INTEGER
    # =========================================================

    def safe_int(
        self,
        value
    ):

        try:

            if value is None:

                return 0

            return int(
                float(
                    value
                )
            )

        except (
            ValueError,
            TypeError
        ):

            return 0