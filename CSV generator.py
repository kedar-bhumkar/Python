import mysql.connector
import csv
import Constants as Q

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
rows = mycursor.fetchall()

# Define the name for the CSV file
filename = "Order.csv"

# Open the file in write mode
with open(filename, 'w') as csvfile:

  # Create a CSV writer object
  csvwriter = csv.writer(csvfile, delimiter=',')

  # Write the column headers to the CSV file
  csvwriter.writerow(['Order Id', 'Order Date', 'Status', 'LOINC Code', 'Barcode', 'Test Type', 'Vendor', 'PCP Name', 'HICN', 'Date of Birth'])

  # Write the rows to the CSV file
  for row in rows:
      csvwriter.writerow(row)

# Close the file
csvfile.close()

# Close the database connection
mydb.close()
