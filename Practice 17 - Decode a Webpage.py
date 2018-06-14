#Date 07/19/17
#Practice Python #17 - Decode a Webpage Part 1
#Decoding a webpage using requests, beautifulsoup
#Find all the article titles on www.nytimes.com and output them

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    r_html = r.text
    print(r_html)

    soup = BeautifulSoup(r_html,"html.parser")
    for line in soup.findAll("h2", {"class":"story-heading"}):
        if line.string != None: print(line.string.strip())

if __name__ == "__main__":
    main()
