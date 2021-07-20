import requests

import pandas as pd
import numpy as np

baseURI = "https://api.census.gov/data/timeseries/healthins/sahie"
r = requests.get(baseURI)
# return r.json()
# x = r.json()
print(r.text)

col_names = ["NAME", "NIC_PT", "NUI_PT", "IPRCAT", "AGECAT", "YEAR", "SEXCAT", "RACECAT"]

df = pd.DataFrame(columns=col_names, data=r.json()[1:])

# Fix data types


print(df.head())

df.to_csv(r'C:\Repositories\data-internships\output_health_insurance.csv', index=False)
# df