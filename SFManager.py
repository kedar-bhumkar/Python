from simple_salesforce import Salesforce
import Constants as Q
import requests, json

# create a Salesforce object
sf = Salesforce(username=Q.SF_USERNAME, password=Q.SF_PASSWORD,security_token='T5RzzYt6abvDe0vzF87JohrzR')
instance_url = 'https://' +sf.sf_instance
access_token = sf.session_id
print ('sf session id  =', sf.session_id, 'sf instance url = ', sf.sf_instance)

def insertRecords(df):
    # map the DataFrame column names to the corresponding Salesforce field names
    field_mapping = {
                    'Member first name': 'Member_FirstName__c',
                    'Member Last name' :  'Member_LastName__c',
                    'Qualitative status': 'Lab_result_status__c',
                    'HICN': 'HICN__c'
                    }

  

    # create a list of dictionaries containing the data to be inserted into Salesforce
    df_renamed = df[['Member first name','Member Last name','Qualitative status','HICN']].rename(columns=field_mapping)
    print ('df_renamed = ', df_renamed)

  
    records = df_renamed.to_dict(orient='records')
    print ('records = ', records)
    # Convert dataframe to JSON format
 
    attributes_json = {"type": "Lab__c", "referenceId": "ref1"}
    # Loop through the records and add the "attributes" field
    for record in records:
       record['attributes'] = attributes_json
       #print ('record', record)

 
    json_records = json.dumps({'records': records})
    print('json_records', json_records)
    


    
 


    #sf.Lab__c.create(records)
    call = sf_api_call('/services/data/v55.0/composite/tree/Lab__c', method="post", data=json_records)




def sf_api_call(action, parameters = {}, method = 'get', data = {}):
    """
    Helper function to make calls to Salesforce REST API.
    Parameters: action (the URL), URL params, method (get, post or patch), data for POST/PATCH.
    """
    headers = {
        'Content-type': 'application/json',
        'Accept-Encoding': 'gzip',
        'Authorization': 'Bearer %s' % access_token
    }
    if method == 'get':
        r = requests.request(method, instance_url+action, headers=headers, params=parameters, timeout=30)
    elif method in ['post', 'patch']:
        r = requests.request(method, instance_url+action, headers=headers, json=data, params=parameters, timeout=10)
    else:
        # other methods not implemented in this example
        raise ValueError('Method should be get or post or patch.')
    print('Debug: API %s call: %s' % (method, r.url) )
    if r.status_code < 300:
        if method=='patch':
            return None
        else:
            return r.json()
    else:
        raise Exception('API error when calling %s : %s' % (r.url, r.content))

