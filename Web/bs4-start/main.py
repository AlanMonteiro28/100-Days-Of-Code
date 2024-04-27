from bs4 import BeautifulSoup
import requests

r = requests.get("https://news.ycombinator.com/")
yc_web_page = r.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_upvotes = article_upvotes[0]
index_highest_upvotes = 0

for n in range(1, len(article_upvotes)):
    if article_upvotes[n] > highest_upvotes:
        highest_upvotes = article_upvotes[n]
        index_highest_upvotes = n

print(article_texts[index_highest_upvotes])
print(article_links[index_highest_upvotes])
print(article_upvotes[index_highest_upvotes])



# with open("website.html", "r", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# name = soup.select_one("#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)
