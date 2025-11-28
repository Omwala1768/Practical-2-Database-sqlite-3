import sqlite3 as om

connection = om.connect("WaterPark.db")
park = connection.cursor()

park.execute("INSERT INTO waterpark VALUES('Om Wala', 18, 123456, 'om@gmail.com')")
print("Data inserted successfully!")

park.execute("SELECT * FROM waterpark")
park.fetchone()
print("Select statement applied successfully!")

for data in park:
    print("~"*10)
    print("Name : ",data[0])
    print("Age : ",data[1])
    print("Contact : ",data[2])
    print("Email : ",data[3])

connection.commit()
connection.close()
