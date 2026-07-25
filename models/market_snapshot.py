"""Canonical market snapshot model.

This module contains market observations only. Company identity belongs to
CompanyIdentity, while financial statement data belongs to FinancialReport.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class MarketSnapshot:
    """Point-in-time market data for a listed company."""

    symbol: str
    ins_code: Optional[str] = None
    price: Optional[float] = None
    market_cap: Optional[float] = None
    timestamp: Optional[datetime] = None
    source: Optional[str] = None

    def __post_init__(self) -> None:
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("symbol must be a non-empty string")

        if self.price is not None and self.price < 0:
            raise ValueError("price cannot be negative")

        if self.market_cap is not None and self.market_cap < 0:
            raise ValueError("market_cap cannot be negative")