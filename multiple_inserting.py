import sqlite3 as om

connection = om.connect("WaterPark.db")
park = connection.cursor()

park.execute("INSERT INTO waterpark VALUES ('Om Wala', 18, 123456, 'om@gmail.com')")
park.execute("INSERT INTO waterpark VALUES ('Krishna Yadav', 18,734567, 'krishna@gmail.com')")
park.execute("INSERT INTO waterpark VALUES ('Sahil Yadav', 19,245384,'sahil@gmail.com')")
print("Data inserted successfully!")

park.execute ("SELECT * FROM waterpark")
print("Select statement applied successfully!")

output = park.fetchall()
for data in output:
    print("~"*10)
    print("Name: ",data[0])
    print("Age: ",data [1])
    print("Contact: ",data [2])
    print("Email: ",data [3])

connection.commit()
connection.close()
