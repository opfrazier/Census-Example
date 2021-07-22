
import requests
import pandas as pd
import numpy as np
baseURI = "https://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625"
r = requests.get(baseURI)
# return r.json()
# x = r.json()
print(r.text)
col_names = ["EST","LANLABEL","NAME","LAN","state"]
df = pd.DataFrame(columns=col_names, data=r.json()[1:])
# Fix data types
print(df.head())
df.to_csv(r'C:\Repositories\data-internships\language.csv', index=False)
# df