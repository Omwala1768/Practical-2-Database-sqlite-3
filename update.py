import sqlite3 as om

connection = om.connect("WaterPark.db")
park = connection.cursor()

park.execute("UPDATE waterpark SET Age=21 WHERE Name='Sahil Yadav'")
print("Update statement applied successfully!")

park.execute("SELECT * from waterpark")
output = park.fetchall()
for data in output:
    print("~"*10)
    print ("Name", data[0])
    print("Age: ", data [1])
    print("Contact: ", data [2])
    print("Email", data[3])

connection.commit()
connection.close()
