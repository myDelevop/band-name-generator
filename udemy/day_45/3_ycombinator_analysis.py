import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.text
    link = article_tag.find("a").get("href")
    article_texts.append(text)
    article_links.append(link)

article_up_votes = [int(score.text.split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_up_votes)
print("")

maximum = article_up_votes[0]
for i in range(1, len(article_up_votes)):
    if article_up_votes[i] > maximum:
        maximum = article_up_votes[i]
index = article_up_votes.index(maximum)

print(article_texts[index])
print(article_links[index])
print(article_up_votes[index])
