from urllib.request import urlopen
import pandas as pd
import datetime

url = 'https://www.contextures.com/xlSampleData01.html'
df = pd.read_html(url)



print(df)
df2 = df[0]
df2.set_index(1)
new_header = df2.iloc[0] #grab the first row for the header
df2 = df2[1:] #take the data less the header row
df2.columns = new_header
df3 = df2[['OrderDate', 'Region', 'Rep', 'Item', 'Units', 'UnitCost', 'Total']]

df3['OrderDate'] = pd.to_datetime(df3['OrderDate'])
df3['UnitCost'] = pd.to_numeric(df3['UnitCost'])
df3['Total'] = pd.to_numeric(df3['Total'])

print(df3)

df3.to_excel("scrapping.xlsx", sheet_name='Scraping', engine='xlsxwriter', index=False)