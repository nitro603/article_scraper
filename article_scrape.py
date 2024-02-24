import requests
from bs4 import BeautifulSoup

# 1. get output from title_scrape (use demo output first)
# 2. create a function that takes the title/politics string as input and outputs it as a website link
# 3. create a function that takes the link as input and outputs the contents as a string
# 4. Create a function that takes the string as input and uploads to a database.
# 5. Set up post get api calls

def make_link(input):
    
    #https://www.w3schools.com/python/python_ref_string.asp //string methods
    return input
    
def scrape(link):
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
        
        
print(make_link("1. Continued Israeli airstrikes flatten parts of Rafah amid slow progress for Gaza cease-fire - World"))