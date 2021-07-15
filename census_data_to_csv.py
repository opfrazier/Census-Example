
import requests   

import pandas as pd
import numpy as np
    
baseURI = "https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state:*"
r = requests.get(baseURI)
#return r.json()
#x = r.json() 
print(r.text) 

col_names = ["NAME","POP","HISP","state"]


df = pd.DataFrame(columns=col_names, data=r.json()[1:]) 

# Fix data types


print(df.head())


df.to_csv(r'C:\Repositories\data-internships\output.csv', index=False) 
# df
