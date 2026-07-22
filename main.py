from analysis.analyzer_engine import AnalyzerEngine



def main():


    print("==============================")
    print("Bourse Analyzer")
    print("==============================")


    ins_code = "43552974795606067"


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