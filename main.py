from tsetmc.symbol_resolver import SymbolResolver
from analysis.analyzer_engine import AnalyzerEngine



def main():

    print("==============================")
    print("Bourse Analyzer")
    print("==============================")


    symbol = "خراسان"


    resolver = SymbolResolver()


    ins_code = resolver.find_ins_code(
        symbol
    )


    if not ins_code:

        print(
            "Symbol not found"
        )

        return



    company_name = (
        "پتروشیمی خراسان"
    )


    codal_url = (

        "https://codal.ir/Reports/Decision.aspx?"

        "LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d"

        "&rt=0"

        "&let=6"

        "&ct=0"

        "&ft=-1"

    )



    engine = AnalyzerEngine(

        ins_code,

        company_name,

        codal_url

    )


    result = engine.run()


    print(
        result["report"]
    )



if __name__ == "__main__":

    main()