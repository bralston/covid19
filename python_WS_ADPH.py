#  python project to create a web scraper
#  will pull data from ADPH site for daily by county counts in Alabama
#  of positive tested, deaths recorded, and cases resolved


#  url for ADPH

#  filename for storing data

#

from bs4 import BeautifulSoup
import requests
# import lxml

# file_path = '/Users/Jeff/github/COVID19WebScraper/covid19/Sample_ADPH.html'

with open('Sample_ADPH.html') as html_file:
    soup = BeautifulSoup(html_file, "lxml")

print(soup)
