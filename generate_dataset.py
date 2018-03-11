#Compiles all the analytic data from the CHR dataset

import pandas as pd
from pprint import pprint
import os
import re

def generate_dataset():
    os.chdir(os.getcwd() + '/CHR/')
    files = os.listdir(os.getcwd())
    li = []
    for f in files:
        print(f)
        year = ''.join([i for i in f if i in '1234567890'])
        x = pd.read_csv(f , header=0 , error_bad_lines=False)
        pprint(x.columns.values)
        x.columns = map(str.lower , x.columns)
        x['year'] = int(year)
        li.append(x)
        res = pd.concat(li)
        print(type(res))
    return res

if __name__ == "__main__":
    data = generate_dataset()
    data.to_csv('final_dataset.csv')
    print(data.head())
