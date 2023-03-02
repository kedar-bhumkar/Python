
import Constants as Q
import MySQLDAO as DB
import FileWriterMux as FW
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

def processOrders():
    try:
        mydb, rows = DB.getData(Q.ORDERS_QUERY) 
        df = pd.DataFrame(rows)
        print('df',df)
        for t in Q.TESTS:                    
         
            df_test = df[df[5].str.contains(t)]
            print('df_test',df_test)
            df_test.loc[:,5] = t
            print('df_test ' + t, df_test)
            FW.generateFile(Q.FILENAME+'_' + t+ '_DDMMYYYY.csv', df_test.values.tolist())        
        
    except:
        print('Exception.......')
    finally:
        mydb.close()
processOrders()
