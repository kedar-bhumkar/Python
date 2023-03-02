from sqlalchemy import create_engine, text
import Constants as Q
import pandas as pd



mydb = create_engine('mysql+mysqlconnector://root:root@localhost:3306/CRM')



def getData(query):
    print('query=', query)
    df = pd.read_sql(text(query), mydb.connect())
    # Fetch all rows from the result set    
    return  df

def close():
    mydb.connect().close()

def getEngine():
    return mydb
