from oracle import connection
# Create a cursor object
cursor = connection.cursor()

# Create the PERSON table
create_table_query = """
CREATE TABLE PERSON (
    SNO NUMBER PRIMARY KEY,
    NAME VARCHAR2(50),
    CITY VARCHAR2(50)
)
"""

# Execute the query
cursor.execute(create_table_query)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()