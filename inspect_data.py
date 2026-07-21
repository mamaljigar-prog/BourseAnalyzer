from bs4 import BeautifulSoup


html = open("sheet0.html", encoding="utf-8").read()

soup = BeautifulSoup(html, "html.parser")


for tag in soup.find_all():
    text = tag.get_text(" ", strip=True)

    if "جمع دارایی" in text or "حقوق مالکانه" in text or "سرمایه" in text:
        print("TAG:", tag.name)
        print("ID:", tag.get("id"))
        print("CLASS:", tag.get("class"))
        print(text[:1000])
        print("================")