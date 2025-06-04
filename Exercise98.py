# Exercise 98 : News api


import requests

def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "fdd707383cfc4960a04898b38d56d1e8"
    }

# how to generate api key:  Go to NewsAPI.org and sign up for a free account.
# Your new API key will be displayed. Copy this key for use in your code.

    url =  "https://newsapi.org/v1/articles"
    res = requests.get(url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
    
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
        print(i + 1, results[i])

if __name__ == '__main__':
    NewsFromBBC()


