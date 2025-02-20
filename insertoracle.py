from oracle import connection
# Read values for the department table from the user
department_name = input("Enter department name: ")
location = input("Enter location: ")

# Insert values into the orgdepartment table
cursor = connection.cursor()
cursor.execute("""
    INSERT INTO orgdepartment (department_name, location)
    VALUES (:1, :2)
""", (department_name, location))
connection.commit()
print("Values inserted successfully")

# Close the cursor and connection
cursor.close()
connection.close()