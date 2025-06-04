# Exercise 97 : A News API is a powerful tool that allows developers to
#  access and retrieve news articles, headlines, and other related content
#  from various sources such as newspapers, magazines, blogs, and websites.
#  These APIs provide a convenient way to integrate news data into applications
#  and websites, enabling developers to display up-to-date news content to users.

import requests

import json

query = input("What type of news are you interested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-04&sortBy=publishedAt&apiKey=fdd707383cfc4960a04898b38d56d1e8"

response= requests.get(url)
news = json.loads(response.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------")
