import pygetwindow
import os
from bs4 import BeautifulSoup as bs4
import requests

url = "Not found"
brave_title = "Not found"
split_title = "Not found"
for title in pygetwindow.getAllTitles():
    if "brave" in title.lower():
        brave_title = title
        split_title = title.split(" ")
        for item in split_title:
            if "https" in item:
                url = item
        
        

if "https" in url:
    html = requests.get(url).text
    soup = bs4(html, "html.parser")
    print(soup)
    print("")
    print(url)
else:
    print(f"url not valid Url: \"{url}\" \nTitle: \"{brave_title}\" \nsplit title: \"{split_title}\"")
    os._exit(0)