from oracle import connection

listx=[]
cursor = connection.cursor()
with open('textfiles/data.txt', 'r') as file:
    for line in file:
        sno, name, city = line.strip().split(',')
        listx.append({'sno':sno,'name': name, 'city': city})

print(listx)



# Insert data into the person table
for record in listx:
    cursor.execute("""
        INSERT INTO person (sno, name, city)
        VALUES (:sno, :name, :city)
    """, record)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()