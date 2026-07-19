import requests
import re
from urllib.parse import urljoin


class CodalPDF:

    def __init__(self, url):
        self.url = url

        self.session = requests.Session()

        self.headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }


    def download(self):

        r = self.session.get(
            self.url,
            headers=self.headers,
            timeout=60
        )

        print("Status:", r.status_code)
        print(
            "Content-Type:",
            r.headers.get("Content-Type")
        )

        content = r.content


        # PDF واقعی
        if content.startswith(b"%PDF"):

            print("PDF واقعی پیدا شد")

            with open(
                "codal_report.pdf",
                "wb"
            ) as f:
                f.write(content)

            return "codal_report.pdf"



        # HTML گزارش
        print("صفحه HTML دریافت شد")

        html = content.decode(
            "utf-8",
            errors="ignore"
        )


        # پیدا کردن لینک های احتمالی فایل
        patterns = [
            r'href="([^"]+\.pdf[^"]*)"',
            r'href="([^"]+Attachment[^"]*)"',
            r'src="([^"]+\.pdf[^"]*)"'
        ]


        links = []


        for p in patterns:

            result = re.findall(
                p,
                html,
                flags=re.I
            )

            links.extend(result)


        print(
            "لینک احتمالی:",
            links
        )


        if links:

            pdf_url = urljoin(
                self.url,
                links[0]
            )

            print(
                "دانلود:",
                pdf_url
            )


            pdf = self.session.get(
                pdf_url,
                headers=self.headers,
                timeout=60
            )


            print(
                pdf.headers.get(
                    "Content-Type"
                )
            )


            if pdf.content.startswith(b"%PDF"):

                with open(
                    "codal_report.pdf",
                    "wb"
                ) as f:
                    f.write(pdf.content)

                print(
                    "PDF ذخیره شد"
                )

                return "codal_report.pdf"



        # ذخیره HTML برای بررسی
        with open(
            "codal_debug_report.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(html)


        print(
            "PDF پیدا نشد - HTML ذخیره شد"
        )

        return None