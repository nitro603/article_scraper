import requests
from bs4 import BeautifulSoup

url = "https://www.pbs.org/newshour/politics/trumps-2024-trials-where-they-stand-and-what-to-expect"  # Replace with a specific article URL

response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.select('h1.title')  # Replace with appropriate selectors
article_contents = soup.select('div.article-body')  # Adjust based on page structure
print(article_contents)

for title, content in zip(titles, article_contents):
    print(title.text.strip())
    print(content.text.strip())