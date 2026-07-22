from core.analyzer_engine import AnalyzerEngine



def main():

    print("==============================")
    print("Bourse Analyzer")
    print("==============================")


    engine = AnalyzerEngine(

        symbol="خراسان",

        company_name="پتروشیمی خراسان"

    )


    result = engine.run()


    print(
        result["report"]
    )



if __name__ == "__main__":

    main()