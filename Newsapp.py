import requests
import json
import pyttsx3

eng = pyttsx3.init()
query = input("What type of news are you interested in? ")
apikeyy= "3Enter Your Api key:"  
# You can get you apikey from www.newsapi.org
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-07-18&to=2024-07-18&sortBy=popularity&apiKey={apikeyy}"

response = requests.get(url)
news = json.loads(response.text)

print(news)
voices = eng.getProperty('voices')
# 1 use for female, 0 use for male
eng.setProperty('voice', voices[1].id)

# Speed set krny k liye rate ko change kry gy

eng.setProperty('rate', 150)
eng.setProperty('volume', 9.0)


if "articles" in news:
    for article in news["articles"]:
        title = article["title"]
        description = article["description"]
        print(title)
        print(description)
        print("--------------------------------------")
        eng.say(title)
        eng.say(description)
        eng.runAndWait()
else:
    Error=("No articles found. Response may have an error.")
    print(Error)
    eng.say(Error)
    # Print any error message in the response if available
    if "message" in news:
        print(f"Error: {news['message']}")


