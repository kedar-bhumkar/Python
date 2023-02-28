import csv

file1 = 'Order-02162023.csv'
file2 = 'Order-02172023.csv'
delta_file = 'Delta-Orders.csv'

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(delta_file, 'w', newline='') as f_out:
    reader1 = csv.DictReader(f1)
    reader2 = csv.DictReader(f2)
    writer = csv.DictWriter(f_out, fieldnames=reader1.fieldnames)
    writer.writeheader()
    
    data1 = {row['Barcode']: row for row in reader1 if row['Status']=='Pending'}
    data2 = {row for row in reader2}
    keys = ['Barcode', 'Date of Birth']
    print (data2)
    
    #print (data1)
    #for barcode in data1:
    #    if barcode not in data2:
    #        writer.writerow(data1[barcode])
       
    #for barcode in data2:
    #    if barcode not in data1:
    #        writer.writerow(data2[barcode])