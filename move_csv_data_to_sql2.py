import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv (r'C:\Repositories\data-internships\output.csv')   
df = pd.DataFrame(data, columns= ['NAME','POP','HISP', 'state'])

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0}; Server=rtmarketanalysis.database.windows.net; Database=rt-prod-demographics; UID=rtadmin; PWD=f3NGPDLBhK6eqJ4Sxbvxd6UG7XxQC5gs;')
cursor=conn.cursor() 



# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO [census].[population_metrics] (category ,population  ,race_code ,state_code)
                VALUES (?,?,?,?)
                ''',
                str(row.NAME), 
                str(row.POP),
                str(row.HISP), 
                str(row.state)
                )
conn.commit()