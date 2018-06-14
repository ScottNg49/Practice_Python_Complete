#decoding a webpage using requests, beautifulsoup
#print(soup.get_text)

import requests
from bs4 import BeautifulSoup

def main():
    print([line.string.strip() for line in BeautifulSoup(requests.get("https://www.nytimes.com/").text,"html.parser").findAll("h2", {"class":"story-heading"}) if line.string != None])

main()
