
import Constants as Q
import MySQLDAO as DB
import FileWriterMux as FW

def processOrders():
    try:
        mydb, rows = DB.getData(Q.ORDERS_QUERY)       
        FW.generateFile(Q.FILENAME, rows)        
    except:
        print('Exception.......')
    finally:
        mydb.close()
processOrders()
