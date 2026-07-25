"""Canonical company identity model.

This module intentionally contains identity metadata only.
Financial and market observations belong to FinancialReport
and MarketSnapshot.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CompanyIdentity:
    """Stable identity information for a listed company."""

    symbol: str
    name: Optional[str] = None
    ins_code: Optional[str] = None
    industry: Optional[str] = None

    def __post_init__(self) -> None:
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("symbol must be a non-empty string")