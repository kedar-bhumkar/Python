import csv

def generateFile(filename, rows):
    #print(filename)
    #print (rows) 
    # Open the file in write mode
    with open(filename, 'w') as csvfile:

        # Create a CSV writer object
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the column headers to the CSV file
        csvwriter.writerow(['Order Id', 'Order Date', 'Status', 'LOINC Code', 'Barcode', 'Test Type', 'Vendor', 'PCP Name', 'HICN', 'Date of Birth'])

        # Write the rows to the CSV file
        for row in rows:
            csvwriter.writerow(row)
    csvfile.close()