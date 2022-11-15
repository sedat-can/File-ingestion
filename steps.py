import testutility as util
import pandas as pd

import csv
import pandas
import yaml


config_data = util.read_config_file("file.yaml")

a= config_data
print(a)
file_type = config_data['file_type']
source_file = config_data['file_name']


df = pd.read_csv(source_file,config_data['inbound_delimiter'])
print(df)
util.col_header_val(df,config_data)
print("columns of files are:" ,df.columns)
print("columns of YAML are:" ,config_data['columns'])

if util.col_header_val(df,config_data)==0:
    print("validation failed")
    
else:
    print("col validation passed")


print("fddddddddddddddddddddddddddddddddddd")