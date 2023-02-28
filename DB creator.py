import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

# Prepare a cursor object
mycursor = mydb.cursor()

# Execute a CREATE DATABASE statement to create 'CRM' database
mycursor.execute("CREATE DATABASE CRM")

# Switch to 'CRM' database
mycursor.execute("USE CRM")

# Execute a CREATE TABLE statement to create 'Order' table
mycursor.execute("CREATE TABLE `Order` ( \
                  `Order Id` INT NOT NULL AUTO_INCREMENT, \
                  `Order Date` DATE NOT NULL, \
                  `Status` VARCHAR(50), \
                  `LOINC Code` VARCHAR(50), \
                  `Barcode` VARCHAR(50), \
                  `Test Type` VARCHAR(50), \
                  `Vendor` VARCHAR(50), \
                  `PCP Name` VARCHAR(50), \
                  `HICN` VARCHAR(50), \
                  `Date of Birth` DATE, \
                  PRIMARY KEY (`Order Id`) \
                  )")

# Close the database connection
mydb.close()

print("Done....")
