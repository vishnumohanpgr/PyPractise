"""
A program where we go to test out our connection credential for any database implementation.
"""
import mysql.connector
import pandas as pd

# Passing the credentials & creating the connection object.
dbconnect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password.123',
    database='world',
    )

# Defining the cursor object.
dbcur = dbconnect.cursor()
"""
# Read from database without column names
dbcur.execute('SELECT DISTINCT ct.Name AS City, cl.Language, cl.Percentage, '
              'cn.Name AS Country, cn.Continent, cn.Population * cl.Percentage * 0.01 AS Speakers, cn.Population '
              'FROM world.country cn RIGHT JOIN world.city ct ON ct.CountryCode=cn.Code '
              'LEFT JOIN world.countrylanguage cl USING(CountryCode) '
              'ORDER BY ct.Name;')
df_original = pd.DataFrame(dbcur.fetchall())
"""

# Read from SQL with column names
df_original = pd.read_sql('SELECT DISTINCT * '
                          'FROM world.country cn RIGHT JOIN world.city ct ON ct.CountryCode=cn.Code '
                          'LEFT JOIN world.countrylanguage cl USING(CountryCode) '
                          'ORDER BY ct.Name;', dbconnect)

# Describes the dataframe
# print(df_original.describe())
print(df_original.columns)

# Prints out the first 5 rows
print(df_original.head(5))

# Prints out the row at the index i
i = 126
print(df_original.iloc[0])

# Return the data as a csv file
#df_original.to_csv('full_world_data.csv', index=False, header=True)

dbconnect.commit()
dbconnect.close()
