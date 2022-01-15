from bs4 import BeautifulSoup
import requests


# with open("website.html", "r") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# all_select = soup.select(".heading")
# print(all_select[0].getText())

# # Scraping a live website

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts= []
article_links = []

articles = soup.find_all(name="a", class_="titlelink")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

article_upvotes= [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

