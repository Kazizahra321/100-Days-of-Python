import requests
#The Python Requests module is an HTTP library that
# allows you to  send HTTP requests in Python code
# and makes it possible to interact with APIs and web services.

#Send a get request to Google's home page
response = requests.get("https://www.google.com")
print(response.text) 
#print the reponse


#post request
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : 'Zahra',
    "body" : 'bhai',
    "userId" : 12,
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

response = requests.post(url, headers, json=data)

print(response.text)

