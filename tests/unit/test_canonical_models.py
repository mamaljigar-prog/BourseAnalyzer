"""Contract tests for canonical domain models."""

from datetime import datetime, timezone

import pytest

from models.company_identity import CompanyIdentity
from models.financial_line_item import FinancialLineItem
from models.financial_report import FinancialReport
from models.market_snapshot import MarketSnapshot


def test_company_identity_contract() -> None:
    identity = CompanyIdentity(
        symbol="درهآور",
        name="داروسازی آوه سینا",
        ins_code="123",
        industry="دارویی",
    )

    assert identity.symbol == "درهآور"
    assert identity.name == "داروسازی آوه سینا"
    assert identity.ins_code == "123"
    assert identity.industry == "دارویی"


def test_company_identity_requires_symbol() -> None:
    with pytest.raises(ValueError):
        CompanyIdentity(symbol="")


def test_market_snapshot_contract() -> None:
    timestamp = datetime(2026, 7, 25, 12, 0, tzinfo=timezone.utc)

    snapshot = MarketSnapshot(
        symbol="درهآور",
        price=12500.0,
        market_cap=500000.0,
        ins_code="123",
        timestamp=timestamp,
        source="TSETMC",
    )

    assert snapshot.symbol == "درهآور"
    assert snapshot.price == 12500.0
    assert snapshot.market_cap == 500000.0
    assert snapshot.ins_code == "123"
    assert snapshot.timestamp == timestamp
    assert snapshot.source == "TSETMC"


def test_market_snapshot_rejects_negative_values() -> None:
    with pytest.raises(ValueError):
        MarketSnapshot(symbol="درهآور", price=-1)

    with pytest.raises(ValueError):
        MarketSnapshot(symbol="درهآور", market_cap=-1)


def test_financial_line_item_contract() -> None:
    item = FinancialLineItem(
        concept="revenue",
        value=1000000.0,
        unit="rial",
        period="9M",
        original_label="درآمدهای عملیاتی",
        normalized_label="operating_revenue",
        source="Codal",
        source_sheet="صورت سود و زیان",
        row_reference="R3",
        confidence=0.95,
    )

    assert item.concept == "revenue"
    assert item.value == 1000000.0
    assert item.unit == "rial"
    assert item.period == "9M"
    assert item.original_label == "درآمدهای عملیاتی"
    assert item.normalized_label == "operating_revenue"
    assert item.source == "Codal"
    assert item.source_sheet == "صورت سود و زیان"
    assert item.row_reference == "R3"
    assert item.confidence == 0.95


def test_financial_line_item_rejects_invalid_confidence() -> None:
    with pytest.raises(ValueError):
        FinancialLineItem(concept="revenue", value=1, confidence=-0.1)

    with pytest.raises(ValueError):
        FinancialLineItem(concept="revenue", value=1, confidence=1.1)


def test_financial_report_contract() -> None:
    revenue = FinancialLineItem(
        concept="revenue",
        value=1000000.0,
        unit="rial",
        period="9M",
        source="Codal",
    )

    report = FinancialReport(
        symbol="درهآور",
        report_type="interim",
        period="9M",
        fiscal_year=1404,
        income_statement={"revenue": revenue},
        balance_sheet={},
        cash_flow={},
        provenance={"source": "Codal"},
    )

    assert report.symbol == "درهآور"
    assert report.report_type == "interim"
    assert report.period == "9M"
    assert report.fiscal_year == 1404
    assert report.income_statement["revenue"] is revenue
    assert report.balance_sheet == {}
    assert report.cash_flow == {}
    assert report.provenance["source"] == "Codal"


def test_canonical_models_are_immutable() -> None:
    identity = CompanyIdentity(symbol="درهآور")
    snapshot = MarketSnapshot(symbol="درهآور")
    item = FinancialLineItem(concept="revenue", value=1)
    report = FinancialReport(symbol="درهآور")

    with pytest.raises(Exception):
        identity.symbol = "X"

    with pytest.raises(Exception):
        snapshot.price = 1

    with pytest.raises(Exception):
        item.value = 2

    with pytest.raises(Exception):
        report.symbol = "X"