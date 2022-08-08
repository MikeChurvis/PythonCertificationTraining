import sqlite3

query__create_table = '''CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            priority INTEGER NOT NULL
                    );'''

q = '''CREATE TABLE IF NOT EXISTS tasks (
)'''

query__insert_into_tasks = "INSERT INTO TASKS (name, priority) VALUES (?, ?)"

tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]

connection = sqlite3.connect('todo.db')
cursor = connection.cursor()

cursor.execute(query__create_table)
# cursor.execute(query__insert_into_tasks, ("My first task", 2))
cursor.executemany(query__insert_into_tasks, tasks)

connection.commit()
connection.close()
