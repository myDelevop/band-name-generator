from bs4 import BeautifulSoup

with open("1_website.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

all_paragraphs = soup.find_all(name="p")
print(all_paragraphs)  # and so on...

# get only the text of an anchor tag
for a_tag in all_anchor_tags:
    print(a_tag.text)

# get only the link of an anchor tag
for a_tag in all_anchor_tags:
    print(a_tag.get("href"))

# get tag h1 with a specific id
name_heading = soup.find(name="h1", id="name")
print(name_heading)

# get tag h3 with a class populated
name_heading = soup.find(name="h3", class_="heading")
print(name_heading)
print(name_heading.name)
print(name_heading.text)
print(name_heading.get("class"))

# we can use CSS selectors to navigate big websites
company_url = soup.select_one(selector="p a")  # it selects the anchor inside a paragraph
print(company_url)

name = soup.select_one(selector="#name")  # CSS Selector by id
print(name)

headings = soup.select(selector=".heading")  # CSS Selector by class
print(headings)

