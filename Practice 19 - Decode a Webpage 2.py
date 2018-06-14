#Date 07/20/17
#Practice Python #19
#Decode a Webpage Part 2
#decoding a webpage using requests, beautifulsoup
#Clean up the article title and put the article text on page  

import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html,"html.parser")
    for line in soup.findAll('p'):
        if line.string != None: print(line.string.strip())

if __name__ == "__main__":
    main()
