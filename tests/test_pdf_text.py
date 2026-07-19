import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from pdf_text import PDFText


pdf = PDFText(
    "annual_report.pdf"
)

pdf.extract()