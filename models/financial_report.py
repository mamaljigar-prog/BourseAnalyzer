"""Canonical financial report model.

This module defines the canonical container for financial statement data.
Source adapters and parsers should produce this model rather than becoming
dependencies of the model itself.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .financial_line_item import FinancialLineItem


@dataclass(frozen=True)
class FinancialReport:
    """Canonical financial report containing normalized statement data."""

    symbol: str
    period: Optional[str] = None
    duration_months: Optional[int] = None
    report_type: Optional[str] = None
    source: Optional[str] = None

    income_statement: Dict[str, FinancialLineItem] = field(default_factory=dict)
    balance_sheet: Dict[str, FinancialLineItem] = field(default_factory=dict)
    cash_flow: Dict[str, FinancialLineItem] = field(default_factory=dict)

    provenance: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("symbol must be a non-empty string")

        if self.duration_months is not None:
            if self.duration_months <= 0:
                raise ValueError("duration_months must be greater than zero")

        self._validate_statement(
            self.income_statement,
            "income_statement",
        )
        self._validate_statement(
            self.balance_sheet,
            "balance_sheet",
        )
        self._validate_statement(
            self.cash_flow,
            "cash_flow",
        )

    @staticmethod
    def _validate_statement(
        statement: Dict[str, FinancialLineItem],
        statement_name: str,
    ) -> None:
        if not isinstance(statement, dict):
            raise TypeError(f"{statement_name} must be a dictionary")

        for concept, item in statement.items():
            if not isinstance(concept, str) or not concept.strip():
                raise ValueError(
                    f"{statement_name} contains an invalid concept key"
                )

            if not isinstance(item, FinancialLineItem):
                raise TypeError(
                    f"{statement_name}[{concept!r}] must be a "
                    "FinancialLineItem"
                )