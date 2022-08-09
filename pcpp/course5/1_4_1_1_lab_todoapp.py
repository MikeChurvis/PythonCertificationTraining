from __future__ import annotations

import sqlite3


def find_task(connection: sqlite3.Connection, name: str) -> tuple | None:
    return connection.execute(
        "SELECT id, name, priority FROM tasks WHERE name = ?",
        (name,)
    ).fetchone()


def show_tasks(connection: sqlite3.Connection):
    for row in connection.execute("SELECT id, name, priority FROM tasks"):
        print(row)


def change_priority(connection: sqlite3.Connection):
    pass


def delete_task(connection: sqlite3.Connection):
    pass


if __name__ == '__main__':
    def main():
        connection = sqlite3.connect('todo.db')

        with connection:
            user_input__task_name = input("Enter task name: ").strip()

            if len(user_input__task_name) == 0:
                print("Task name must have at least one character.")
                exit(1)

            if find_task(connection, user_input__task_name) is not None:
                print("There is already a task with this name.")
                exit(1)

            user_input__task_priority = input("Enter priority: ").strip()

            try:
                user_input__task_priority = int(user_input__task_priority)
                if user_input__task_priority < 1:
                    raise ValueError
            except (TypeError, ValueError):
                print("Task priority must be an integer greater than or equal to 1.")
                exit(1)

            connection.execute(
                "INSERT INTO tasks (name, priority) VALUES (?, ?)",
                (user_input__task_name, user_input__task_priority)
            )

            connection.commit()

            show_tasks(connection)


    main()
