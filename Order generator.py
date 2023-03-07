
import Constants as Q
import DBEngine as DB

#import FileWriterMux as FW
import FileManager as FW
import pandas as pd
import datetime
pd.options.mode.chained_assignment = None  # default='warn'

def processOrders():
    try:
        #get data from PODS
        df_pods = DB.getData(Q.ORDERS_QUERY) 
        print('df_pods',df_pods)

        #extract the IMS_ID 
        imsIds = df_pods['IMS_ID']
        print('imsIds',imsIds)
        
        #get HICN from IMDB
        hicn_query = Q.IMDB_QUERY.format(",".join([str(ims_id) for ims_id in imsIds]))
        print('hicn_query', hicn_query)
        #df_hicns = pd.read_sql(hicn_query, mydb)
        df_hicns = DB.getData(hicn_query)
        print('df_hicns', df_hicns)
        print('df_hicns[IMS_ID]' , df_hicns['IMS_ID'])

        #Join HICN to data from PODS
        df_all = df_pods.join(df_hicns.set_index('IMS_ID'), on='IMS_ID')     
        print('df_all_cols = ',df_all.columns)
        print('df_all = ',df_all)

        #datetime for the day
        dt = datetime.date.today().strftime('%d-%m-%Y')

        #Generate unique file for each test
        for t in Q.TESTS:                   
     
            df_test = df_all[df_all['Test Type'].str.contains(t)]
            print('df_test',df_test)
            df_test.loc[:,'Test Type'] = t
            print('df_test ' + t, df_test)

            #add the data to the ORDER DB_cache
            DB.writeData(df_test, Q.ORDER_DB_CACHE)
            

            #Remove 'NAN' HICN rows  
            FW.generateFile(Q.FILENAME + '_' + t + '_' +  dt + '.csv', df_test.dropna(subset=['HICN']))        
        
    except Exception as e: 
        print(e)
    finally:
        DB.close()
processOrders()
