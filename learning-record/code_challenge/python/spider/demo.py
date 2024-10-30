import requests
from bs4 import BeautifulSoup

# crawling logic... 
response = requests.get("https://www.zenrows.com/blog/web-crawler-python")
soup = BeautifulSoup(response.content, "html.parser")
title = soup.select_one("title").text
print(title)
