from bs4 import BeautifulSoup
import pandas as pd
# import requests
# import csv

# import sys
# print(sys.version)

# url = 'https://www.alabamapublichealth.gov/infectiousdiseases/2019-coronavirus.html'
# source = requests.get(url).text
# soup = BeautifulSoup(source, 'lxml')


with open('Sample_ADPH.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
tbl_1 = soup.find_all('table')[0]
# print(tbl_1.prettify())

new_table = pd.DataFrame()


row_marker = 0
for row in tbl_1.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.iat[row_marker, column_marker] = column.get_text()
        column_marker += 1
new_table


# for row in tbl_1.find_all('tr'):
#     column_marker = 0
#     columns = row.find_all('td')
#     for column in columns:
#         new_table.iat[row_marker, column_marker] = column.get_text()
#         column_marker += 1
#
# new_table

# %%

# table_match = soup.find(
#     'table', class_="table dt-responsive table-responsive-sm display data-grid-table-covid-19 nowrap covid-table table-covid dataTable no-footer")


# table_head = soup.find('thead').th.text
#
# for entry in soup.find_all('tr', role='row'):
#     rowheader_1 = entry.th.text
#     print(rowheader_1)
#
# print(table_match.prettify())
#
# print(table_head)
