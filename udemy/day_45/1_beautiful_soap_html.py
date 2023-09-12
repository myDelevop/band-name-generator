from bs4 import BeautifulSoup

with open("1_website.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

contents = soup.prettify()
print(contents)
print("****** HTML ABOVE *********\n\n")

# Prints the first <a> Tag, the first <li> Tag and so on...
# Next lesson we'll see how to obtain all lists, paragraphs etc...
print(soup.title)
print(soup.title.string)
print(soup.a)
print(soup.li)
print(soup.p)
