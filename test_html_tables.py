import pandas as pd


url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=OOObOOOaNGDL045HqC0wNGueH5Hw%3d%3d&rt=0&let=6&ct=0&ft=-1"


tables = pd.read_html(url)


print("TABLE COUNT:", len(tables))


for i, t in enumerate(tables):

    print("================")
    print("TABLE", i)
    print(t.head(5))