import requests
import json


query = input("What type of news you want to read: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-07-31&sortBy=publishedAt&apiKey=e7ab2d03552b4a8586755be94a5a0a93"
r= requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------")