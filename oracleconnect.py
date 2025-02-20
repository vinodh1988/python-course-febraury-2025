import oracledb

# Define your connection string
connection_string = (
   "hr/hr@localhost:1521/XEPDB1"
)

# Connect to the database
connection = oracledb.connect(connection_string)

# Now you can perform database operations
cursor = connection.cursor()
cursor.execute("SELECT * FROM employees")
for row in cursor:
    print(row)

# Close the connection
cursor.close()
connection.close()
