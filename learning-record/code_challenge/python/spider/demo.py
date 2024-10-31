import requests
from bs4 import BeautifulSoup

# crawling logic... 
url = "https://reactnative.dev/docs/environment-setup"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.select_one("title").text
print(title)
