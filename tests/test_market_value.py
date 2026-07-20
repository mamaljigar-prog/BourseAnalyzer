from tsetmc.tsetmc_adapter import TSETMCAdapter
from tsetmc.tsetmc_market import MarketData


def main():

    ins_code = "43552974795606067"

    api = TSETMCAdapter()

    closing = api.get_closing_price(ins_code)

    info = api.get_instrument_info(ins_code)

    market = MarketData(
        closing,
        info
    )

    print("==============================")
    print("MARKET DATA")
    print("==============================")

    print(market.report())


if __name__ == "__main__":
    main()