from core.analyzer_engine import AnalyzerEngine
from core.analyzer_request import AnalyzerRequest



def main():


    print("==============================")
    print("Bourse Analyzer")
    print("==============================")


    request = AnalyzerRequest(

        symbol="خراسان"

    )


    engine = AnalyzerEngine(

        request.symbol

    )


    result = engine.run()


    print(

        result["report"]

    )



if __name__ == "__main__":

    main()