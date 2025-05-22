#Exercise83: bs4 Module
# we want to parse the html code and scrape down all the h2's

#bs4 Module
#This module called BeautifulSoup which is used for web scraping in python
# You need to first pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com")
print(response.text)

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

#finding all the headings and printing them
for heading in soup.find_all("h2"):
    print(heading.text)

