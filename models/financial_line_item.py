"""Canonical financial line item model.

A FinancialLineItem represents one normalized financial value while
preserving its source, period, unit, and mapping confidence.
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class FinancialLineItem:
    """A single canonical financial data point with provenance."""

    concept: str
    value: float
    unit: str
    period: Optional[str] = None
    original_label: Optional[str] = None
    normalized_label: Optional[str] = None
    source: Optional[str] = None
    source_sheet: Optional[str] = None
    row_reference: Optional[str] = None
    confidence: Optional[float] = None

    def __post_init__(self) -> None:
        if not isinstance(self.concept, str) or not self.concept.strip():
            raise ValueError("concept must be a non-empty string")

        if not isinstance(self.unit, str) or not self.unit.strip():
            raise ValueError("unit must be a non-empty string")

        if self.confidence is not None:
            if not 0.0 <= self.confidence <= 1.0:
                raise ValueError("confidence must be between 0.0 and 1.0")