import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from pdf_reader import CodalPDF


url = input(
    "لینک گزارش کدال: "
)


pdf = CodalPDF(url)

pdf.download()