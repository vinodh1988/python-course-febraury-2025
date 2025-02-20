from oracle import connection


cursor = connection.cursor()
with open('textfiles/data.txt', 'r') as file:
    for line in file:
        sno, name, city = line.strip().split(',')
        print(sno,name,city)
        cursor.execute("""INSERT INTO person (sno, name, city) VALUES (:1, :2, :3)
         """,(sno,name,city))
        print("Values inserted successfully")


connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()