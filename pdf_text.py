from pypdf import PdfReader


class PDFText:

    def __init__(self, file):
        self.file = file


    def extract(self):

        reader = PdfReader(
            self.file
        )

        print(
            "تعداد صفحات:",
            len(reader.pages)
        )

        text = ""

        for i, page in enumerate(reader.pages):

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"


        with open(
            "annual_text.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)


        print(
            "متن استخراج شد:",
            len(text),
            "کاراکتر"
        )

        return text