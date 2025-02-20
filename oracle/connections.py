import oracledb

# Define your connection string
connection_string = (
   "hr/hr@localhost:1521/XEPDB1"
)

# Connect to the database
connection = oracledb.connect(connection_string)