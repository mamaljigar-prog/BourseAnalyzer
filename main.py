import sys

from core.analyzer_engine import AnalyzerEngine
from core.analyzer_request import AnalyzerRequest


def main():

    print("==============================")
    print("Bourse Analyzer")
    print("==============================")

    if len(sys.argv) < 2:
        print("Usage: python main.py <symbol>")
        return

    symbol = sys.argv[1].strip()

    if not symbol:
        print("Symbol cannot be empty")
        return

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