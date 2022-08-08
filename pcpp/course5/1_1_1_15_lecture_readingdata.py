import sqlite3

connection = sqlite3.connect('todo.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM tasks')

row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)

connection.close()
