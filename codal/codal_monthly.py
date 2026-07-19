import requests
import re


class CodalMonthly:

    def __init__(self, url):
        self.url = url


    def get_html(self):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(
            self.url,
            headers=headers,
            timeout=60
        )

        print("Status:", r.status_code)

        r.encoding = "utf-8"

        return r.text



    def extract_cells(self):

        html = self.get_html()

        pattern = r'"address":"(.*?)".*?"value":"(.*?)"'

        data = re.findall(
            pattern,
            html,
            re.S
        )

        cells = []

        for address,value in data:

            cells.append(
                {
                    "address":address,
                    "value":value
                }
            )

        print(
            "تعداد سلول پیدا شده:",
            len(cells)
        )

        return cells



    def get_table(self):

        cells = self.extract_cells()

        table = {}

        for c in cells:

            addr = c["address"]

            value = c["value"]

            m = re.match(
                r"([A-Z]+)(\d+)",
                addr
            )

            if m:

                col = m.group(1)
                row = m.group(2)


                if row not in table:
                    table[row] = {}


                table[row][col] = value


        return table



    def show_monthly_sales(self):

        table = self.get_table()


        print("================")
        print("گزارش فروش ماهانه")
        print("================")


        products = {

            "5":"اوره مصرفي در واحد ملامين",
            "6":"اوره صنعتي",
            "7":"کريستال ملامين",
            "8":"آمونياک",
            "9":"اوره حمايتي",
            "13":"آمونياک داخلي",
            "12":"ملامين داخلي",
            "17":"اوره صادراتي",
            "18":"آمونياک صادراتي",
            "19":"کريستال ملامين صادراتي"

        }



        for row,name in products.items():


            data = table.get(row,{})


            sale = data.get("O","")
            price = data.get("P","")
            amount = data.get("Q","")


            if amount and amount!="0":

                print(
                    f"{name} | "
                    f"فروش: {sale} تن | "
                    f"نرخ: {price} | "
                    f"مبلغ: {amount} میلیون ریال"
                )



        print("----------------")

        total = table.get("29",{})


        print(
            "جمع کل فروش:",
            total.get("Q",""),
            "میلیون ریال"
        )