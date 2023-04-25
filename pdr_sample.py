# https://www.econdb.com/api/series/

import pandas_datareader.data as web

from data_sources import econdb_labels

fields = econdb_labels.get('fields')
countries = econdb_labels.get('countries')

for _, f in fields.items(): 
    for _, c in countries.items():
        ticker = f'{f}{c}'
        
        data = web.DataReader(f'ticker={ticker}', 'econdb')
        print(data.head())
        print(data.index)
        # print(data.info())