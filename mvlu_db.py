import sqlite3

connection = sqlite3.connect("mvlu.db")

print("Om Wala F122")
print(connection.total_changes)

cursor = connection.cursor()
cursor.execute("CREATE TABLE CSstudents (Roll_no int, Name varchar(30), Email_id varchar(50), Contact int, Course varchar(40))")
cursor.execute("INSERT INTO CSstudents VALUES (1, 'Om Wala', 'om@gmail.com', 12345, 'Computer Science')")
cursor.execute("INSERT INTO CSstudents VALUES (2, 'Shreyash Kadam', 'kadam@gmail.com', 23456, 'Computer Science')")

print("data inserted successfully")
connection.commit()

rows = cursor.execute("select Roll_no, Name, Course from CSstudents").fetchall()
print (rows)
