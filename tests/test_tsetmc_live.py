from tsetmc.tsetmc_adapter import TSETMCAdapter


def main():

    adapter = TSETMCAdapter()

    ins_code = "43552974795606067"

    print("==============================")
    print("TSETMC TEST")
    print("==============================")


    price = adapter.get_closing_price(ins_code)

    print("CLOSING PRICE")
    print(price)


    print("------------------------------")


    info = adapter.get_instrument_info(ins_code)

    print("INSTRUMENT INFO")
    print(info)



if __name__ == "__main__":
    main()