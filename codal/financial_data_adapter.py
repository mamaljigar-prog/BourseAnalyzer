"""Financial data normalization layer for Codal data."""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional

from codal.financial_adapter import FinancialAdapter


class FinancialDataAdapter:
    """Normalize raw Codal financial data before canonical conversion."""

    def __init__(
        self,
        symbol: Optional[str] = None,
        *,
        period: Optional[str] = None,
        duration_months: Optional[int] = None,
        report_type: Optional[str] = None,
        source: str = "Codal",
        source_sheet: Optional[str] = None,
    ) -> None:
        self.symbol = symbol
        self.period = period
        self.duration_months = duration_months
        self.report_type = report_type
        self.source = source
        self.source_sheet = source_sheet

    @staticmethod
    def _safe_float(value: Any) -> Optional[float]:
        if value is None:
            return None

        if isinstance(value, bool):
            return None

        if isinstance(value, (int, float)):
            return float(value)

        text = str(value).strip()

        if not text:
            return None

        replacements = {
            "۰": "0",
            "۱": "1",
            "۲": "2",
            "۳": "3",
            "۴": "4",
            "۵": "5",
            "۶": "6",
            "۷": "7",
            "۸": "8",
            "۹": "9",
            "٬": "",
            ",": "",
            "(": "-",
            ")": "",
            "−": "-",
            "٫": ".",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        try:
            return float(text)
        except (TypeError, ValueError):
            return None

    @classmethod
    def _normalize_item(
        cls,
        item: Any,
    ) -> Optional[Dict[str, Any]]:
        if item is None:
            return None

        if isinstance(item, Mapping):
            value = cls._safe_float(
                item.get("value")
            )

            if value is None:
                return None

            return {
                "value": value,
                "year": (
                    item.get("year")
                    or item.get("yearEndToDate")
                ),
                "period": (
                    item.get("period")
                    or item.get("periodEndToDate")
                ),
            }

        value = cls._safe_float(item)

        if value is None:
            return None

        return {
            "value": value,
            "year": None,
            "period": None,
        }

    @classmethod
    def _normalize_values(
        cls,
        values: Any,
    ) -> list[Dict[str, Any]]:
        if values is None:
            return []

        if isinstance(values, Mapping):
            item = cls._normalize_item(values)

            return (
                [item]
                if item is not None
                else []
            )

        if isinstance(values, (list, tuple)):
            result = []

            for value in values:
                item = cls._normalize_item(
                    value
                )

                if item is not None:
                    result.append(item)

            return result

        item = cls._normalize_item(values)

        return (
            [item]
            if item is not None
            else []
        )

    @staticmethod
    def _sort_values(
        values: list[Dict[str, Any]],
    ) -> list[Dict[str, Any]]:
        """Keep source order unless explicit comparable dates exist."""

        if len(values) <= 1:
            return values

        # Do not blindly sort Persian/date strings.
        # Codal parsers commonly return newest value first.
        return values

    def get_latest_two(
        self,
        values: Any,
    ) -> Dict[str, Any]:
        """Return current and previous usable financial values."""

        normalized = self._normalize_values(
            values
        )

        normalized = self._sort_values(
            normalized
        )

        if not normalized:
            return {
                "current": 0,
                "previous": 0,
                "current_date": None,
                "previous_date": None,
            }

        current = normalized[0]

        previous = (
            normalized[1]
            if len(normalized) > 1
            else None
        )

        return {
            "current": current.get(
                "value",
                0,
            ),
            "previous": (
                previous.get(
                    "value",
                    0,
                )
                if previous
                else 0
            ),
            "current_date": (
                current.get("period")
                or current.get("year")
            ),
            "previous_date": (
                (
                    previous.get("period")
                    or previous.get("year")
                )
                if previous
                else None
            ),
        }

    def adapt_income_statement(
        self,
        raw_data: Mapping[str, Any],
    ) -> Dict[str, Dict[str, Any]]:
        """Normalize income statement data into latest/previous values."""

        if not isinstance(raw_data, Mapping):
            raise TypeError(
                "raw_data must be a mapping"
            )

        return {
            "sales": self.get_latest_two(
                raw_data.get(
                    "sales",
                    [],
                )
            ),
            "gross_profit": self.get_latest_two(
                raw_data.get(
                    "gross_profit",
                    [],
                )
            ),
            "operating_profit": self.get_latest_two(
                raw_data.get(
                    "operating_profit",
                    [],
                )
            ),
            "net_profit": self.get_latest_two(
                raw_data.get(
                    "net_profit",
                    [],
                )
            ),
            "non_operating_income": self.get_latest_two(
                raw_data.get(
                    "non_operating_income",
                    [],
                )
            ),
        }

    def _canonical_raw_data(
        self,
        raw_data: Mapping[str, Any],
    ) -> Dict[str, Any]:
        """Convert latest/previous wrappers into canonical adapter input."""

        adapted = self.adapt_income_statement(
            raw_data
        )

        result: Dict[str, Any] = {}

        for concept, values in adapted.items():
            result[concept] = {
                "value": values.get(
                    "current",
                    0,
                ),
                "period": values.get(
                    "current_date"
                ),
            }

        return result

    def build_report(
        self,
        raw_data: Mapping[str, Any],
        *,
        balance_sheet: Optional[
            Mapping[str, Any]
        ] = None,
        cash_flow: Optional[
            Mapping[str, Any]
        ] = None,
    ):
        """Build a canonical FinancialReport."""

        if not self.symbol:
            raise ValueError(
                "symbol is required to build FinancialReport"
            )

        adapter = FinancialAdapter(
            self.symbol,
            period=self.period,
            duration_months=self.duration_months,
            report_type=self.report_type,
            source=self.source,
            source_sheet=self.source_sheet,
        )

        canonical_raw_data = self._canonical_raw_data(
            raw_data
        )

        return adapter.build_report(
            canonical_raw_data,
            balance_sheet=balance_sheet,
            cash_flow=cash_flow,
        )

    def report(
        self,
        raw_data: Mapping[str, Any],
        *,
        balance_sheet: Optional[
            Mapping[str, Any]
        ] = None,
        cash_flow: Optional[
            Mapping[str, Any]
        ] = None,
    ):
        """Backward-compatible alias for build_report."""

        return self.build_report(
            raw_data,
            balance_sheet=balance_sheet,
            cash_flow=cash_flow,
        )