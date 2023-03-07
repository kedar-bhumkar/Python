from simple_salesforce import Salesforce
import Constants as Q


# create a Salesforce object
sf = Salesforce(username=Q.SF_USERNAME, password=Q.SF_PASSWORD,security_token='T5RzzYt6abvDe0vzF87JohrzR')

def insertRecords(df):
    # map the DataFrame column names to the corresponding Salesforce field names
    field_mapping = {
                    'Member first name': 'Member_FirstName__c',
                    'Member Last name' :  'Member_LastName__c',
                    'Qualitative status': 'Lab_result_status__c',
                    'HICN': 'HICN__c'
                    }

    # create a list of dictionaries containing the data to be inserted into Salesforce
    records = df[['Member first name','Member Last name','Qualitative status','HICN']].rename(columns=field_mapping).to_dict(orient='records')
    print ('records = ', records)
    sf.Lab__c.create(records)
