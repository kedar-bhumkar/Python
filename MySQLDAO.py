import mysql.connector
import Constants as Q
import pandas as pd

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="CRM"
)


def getData(query):
    print('query=', query)
    df = pd.read_sql(query, mydb)
    # Fetch all rows from the result set    
    return  df

def close():
    mydb.close()

def getEngine():
    return mydb