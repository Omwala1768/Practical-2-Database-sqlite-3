import sqlite3
connection = sqlite3.connect("student.db")

print("Om Wala F122")
print(connection.total_changes)
