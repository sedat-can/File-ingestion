import datetime
import csv
import gzip

from dask import dataframe as dd
df = dd.read_csv("C:\\Users\\elifh\\OneDrive\\Masaüstü\\lu\\adult.data",delimiter= ',')

# Write csv in gz format in pipe separated text file (|)
df.to_csv('adult.csv.gz',
          sep='|',
          header=True,
          index=False,
          quoting=csv.QUOTE_ALL,
          compression='gzip',
          quotechar='"',
          doublequote=True,
          line_terminator='\n')
