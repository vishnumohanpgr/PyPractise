"""
A program where we good test out our connection credential for any database implementation.
"""
import mysql.connector

# Passing the credentials & creating the connection object.
dbconnect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password.123',
    database='world',
    )

# Defining the cursor object.
dbcur = dbconnect.cursor()

# Executing a query
dbcur.execute('SELECT Name FROM world.city;')
temp = dbcur.fetchall()

print(temp)
