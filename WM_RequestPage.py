from bs4 import BeautifulSoup
import pandas as pd
import requests

# import csv


site = 'https://www.alabamapublichealth.gov/infectiousdiseases/2019-coronavirus.html'

request1 = requests.get(site)
type(request1)
soup = BeautifulSoup(request1.text, 'html5lib')
type(soup)
prettysoup = soup.prettify()
print(prettysoup)
type(prettysoup)

# count = 0


dfs = pd.read_html(site, header=0)
# for df in dfs:
#     print(df)
#     count += 1
# print(count)
# type(dfs)
print(dfs[0])

data1_df = dfs[0]
print(type(data1_df))
print(data1_df)

# %%
