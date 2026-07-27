import pytest

from models.company_identity import CompanyIdentity
from models.market_snapshot import MarketSnapshot
from tsetmc.tsetmc_adapter import TSETMCAdapter


def test_tsetmc_canonical_market_data_live():

    adapter = TSETMCAdapter()

    symbol = "خراسان"

    from tsetmc.symbol_resolver import SymbolResolver

    resolver = SymbolResolver()

    ins_code = resolver.find_ins_code(
        symbol
    )

    if not ins_code:
        pytest.skip(
            f"TSETMC instrument not found for symbol: {symbol}"
        )

    data = adapter.get_canonical_market_data(
        ins_code
    )

    identity = data["identity"]

    market = data["market"]

    assert isinstance(
        identity,
        CompanyIdentity
    )

    assert isinstance(
        market,
        MarketSnapshot
    )

    assert identity.symbol == symbol

    assert identity.ins_code == str(
        ins_code
    )

    assert market.symbol == symbol

    assert market.ins_code == str(
        ins_code
    )

    assert market.source == "TSETMC"

    assert market.timestamp is not None

    assert market.price is not None

    assert market.price >= 0

    assert market.market_cap is not None

    assert market.market_cap >= 0