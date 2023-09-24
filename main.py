import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-09-15&sortBy=publishedAt&apiKey" \
      f"=Your_Api_Key"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")
