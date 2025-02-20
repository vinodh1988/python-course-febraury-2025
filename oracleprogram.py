from oracle import connection

#from oracle.connections import connection

# Create a new table
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE orgdepartment (
        department_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
        department_name VARCHAR2(50) NOT NULL,
        location VARCHAR2(50),
        PRIMARY KEY (department_id)
    )
""")
print("Table created successfully")

# Close the cursor and connection
cursor.close()
connection.close()

