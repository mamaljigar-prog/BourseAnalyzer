# main.py

# -*- coding: utf-8 -*-

import sys

from core.analyzer_engine import AnalyzerEngine
from core.analyzer_request import AnalyzerRequest



def main():

    print("==============================")
    print("Bourse Analyzer")
    print("==============================")


    symbol = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "خراسان"
    )


    request = AnalyzerRequest(
        symbol=symbol
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