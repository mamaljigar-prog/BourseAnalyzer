from bs4 import BeautifulSoup


html = open("sheet0.html", encoding="utf-8").read()

soup = BeautifulSoup(html, "html.parser")


grids = soup.find_all(class_=lambda x: x and "Grid" in x)

print("GRID COUNT:", len(grids))


for i,g in enumerate(grids):
    print("==========")
    print("GRID", i)
    print(g.name)
    print(g.get_text(" ", strip=True)[:500])