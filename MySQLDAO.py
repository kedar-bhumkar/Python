import mysql.connector
import Constants as Q

def getData(query):
  
    # Connect to MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="CRM"
    )

    # Prepare a cursor object
    mycursor = mydb.cursor()  
    # Execute a SELECT statement to get all rows from 'Order' table
    mycursor.execute(Q.ORDERS_QUERY)
    # Fetch all rows from the result set    
    return  mydb, mycursor.fetchall()