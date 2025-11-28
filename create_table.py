import sqlite3 as om

connection = om.connect("WaterPark.db")
park = connection.cursor()
park.execute("CREATE TABLE waterpark(Name varchar(30), Age int, Contact int, Email varchar(50))")
print("Waterpark Table Created Successfully!")

connection.commit()
connection.close()
