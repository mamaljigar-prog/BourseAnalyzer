import requests
from datetime import datetime, timezone

from models.company_identity import CompanyIdentity
from models.market_snapshot import MarketSnapshot


class TSETMCAdapter:
    """
    Adapter for retrieving raw market data from TSETMC.

    Responsibilities:
    - Resolve instrument information from an ins_code.
    - Retrieve closing price information.
    - Convert raw TSETMC responses into canonical domain models.
    """

    def __init__(self):

        self.base_url = (
            "https://cdn.tsetmc.com/api"
        )

        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

        self.session = requests.Session()

        self.session.headers.update(
            self.headers
        )

    # =========================================================
    # HTTP
    # =========================================================

    def request_json(
        self,
        url
    ):
        """
        Execute a GET request and return JSON response.
        """

        response = self.session.get(
            url,
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    # =========================================================
    # Raw TSETMC API
    # =========================================================

    def get_closing_price(
        self,
        ins_code
    ):
        """
        Retrieve raw closing price data.
        """

        url = (
            f"{self.base_url}/ClosingPrice/"
            f"GetClosingPriceInfo/{ins_code}"
        )

        return self.request_json(
            url
        )

    # =========================================================

    def get_instrument_info(
        self,
        ins_code
    ):
        """
        Retrieve raw instrument information.
        """

        url = (
            f"{self.base_url}/Instrument/"
            f"GetInstrumentInfo/{ins_code}"
        )

        return self.request_json(
            url
        )

    # =========================================================
    # Raw Data Extraction
    # =========================================================

    @staticmethod
    def _extract_instrument(
        info
    ):
        """
        Extract instrumentInfo from TSETMC response.
        """

        if not isinstance(
            info,
            dict
        ):
            return {}

        data = info.get(
            "instrumentInfo",
            info
        )

        if not isinstance(
            data,
            dict
        ):
            return {}

        return data

    # =========================================================

    @staticmethod
    def _extract_closing(
        closing
    ):
        """
        Extract closingPriceInfo from TSETMC response.
        """

        if not isinstance(
            closing,
            dict
        ):
            return {}

        data = closing.get(
            "closingPriceInfo",
            closing
        )

        if not isinstance(
            data,
            dict
        ):
            return {}

        return data

    # =========================================================
    # Company Identity
    # =========================================================

    def get_company_identity(
        self,
        ins_code,
        info
    ):
        """
        Convert TSETMC instrument data into canonical
        CompanyIdentity model.
        """

        data = self._extract_instrument(
            info
        )

        symbol = (
            data.get(
                "lVal18AFC"
            )
            or
            data.get(
                "symbol"
            )
        )

        if not symbol:

            raise ValueError(
                "TSETMC instrument data does not contain a symbol"
            )

        name = (
            data.get(
                "lVal30"
            )
            or
            symbol
        )

        if isinstance(
            name,
            str
        ):
            name = name.strip()

        industry = None

        sector = data.get(
            "sector"
        )

        if isinstance(
            sector,
            dict
        ):
            industry = (
                sector.get(
                    "lSecVal"
                )
            )

        return CompanyIdentity(

            symbol=symbol,

            name=name,

            ins_code=str(
                ins_code
            ),

            industry=industry

        )

    # =========================================================
    # Market Snapshot
    # =========================================================

    def get_market_snapshot(
        self,
        ins_code,
        info=None,
        closing=None
    ):
        """
        Convert TSETMC market data into canonical
        MarketSnapshot model.

        Market cap unit:
            billion toman

        TSETMC price:
            rial

        TSETMC shares:
            number of shares
        """

        if info is None:

            info = self.get_instrument_info(
                ins_code
            )

        if closing is None:

            closing = self.get_closing_price(
                ins_code
            )

        instrument = self._extract_instrument(
            info
        )

        closing_data = self._extract_closing(
            closing
        )

        symbol = (
            instrument.get(
                "lVal18AFC"
            )
            or
            instrument.get(
                "symbol"
            )
        )

        if not symbol:

            raise ValueError(
                "TSETMC instrument data does not contain a symbol"
            )

        price = closing_data.get(
            "pDrCotVal"
        )

        if price is None:

            price = closing_data.get(
                "pClosing"
            )

        shares = instrument.get(
            "zTitad"
        )

        market_cap = None

        if (
            price is not None
            and
            shares is not None
        ):

            try:

                price = float(
                    price
                )

                shares = float(
                    shares
                )

                market_cap = (

                    price
                    *
                    shares

                ) / (

                    10
                    *
                    1_000_000_000

                )

            except (
                TypeError,
                ValueError
            ):

                market_cap = None

        return MarketSnapshot(

            symbol=symbol,

            ins_code=str(
                ins_code
            ),

            price=price,

            market_cap=(
                round(
                    market_cap,
                    2
                )
                if market_cap is not None
                else None
            ),

            timestamp=datetime.now(
                timezone.utc
            ),

            source="TSETMC"

        )

    # =========================================================
    # Canonical Market Context
    # =========================================================

    def get_canonical_market_data(
        self,
        ins_code
    ):
        """
        Retrieve TSETMC data and return canonical models.

        Returns:
            {
                "identity": CompanyIdentity,
                "market": MarketSnapshot
            }
        """

        info = self.get_instrument_info(
            ins_code
        )

        closing = self.get_closing_price(
            ins_code
        )

        identity = self.get_company_identity(

            ins_code=ins_code,

            info=info

        )

        market = self.get_market_snapshot(

            ins_code=ins_code,

            info=info,

            closing=closing

        )

        return {

            "identity":
                identity,

            "market":
                market

        }

    # =========================================================
    # Backward Compatibility
    # =========================================================

    def get_company_name(
        self,
        info
    ):
        """
        Backward-compatible helper.

        New code should use get_company_identity().
        """

        data = self._extract_instrument(
            info
        )

        name = data.get(
            "lVal30"
        )

        if name:

            return name.strip()

        return data.get(
            "lVal18AFC"
        )


if __name__ == "__main__":

    adapter = TSETMCAdapter()

    # Example:
    # ins_code = "7745894403636165"
    #
    # data = adapter.get_canonical_market_data(
    #     ins_code
    # )
    #
    # print(data["identity"])
    # print(data["market"])