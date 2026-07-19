import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from codal_financial import CodalFinancialAdapter


x = CodalFinancialAdapter("خراسان")

x.read_excel()