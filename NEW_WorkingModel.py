from bs4 import BeautifulSoup
import pandas as pd
import requests
# import urllib.request
# import csv

# import sys
# print(sys.version)

# url = 'https://www.alabamapublichealth.gov/infectiousdiseases/2019-coronavirus.html'
# source = requests.get(url).text
# source = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(source, 'lxml')
count = 0
dfs = pd.read_html('Sample_ADPH.html', header=0)
# for df in dfs:
#     print(df)
#     count += 1
# print(count)
# type(dfs)
# print(dfs[0])

data1_df = dfs[0]

print(data1_df)
