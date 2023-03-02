import csv

def generateFile(filename, df_test):
    print(filename)
    #print (rows) 
    # Open the file in write mode
    with open(filename, 'w') as csvfile:

        # Create a CSV writer object
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the column headers to the CSV file
        csvwriter.writerow(df_test.columns);   
        # Write the rows to the CSV file
        for row in df_test.values.tolist():
            csvwriter.writerow(row)
    csvfile.close()