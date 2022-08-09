from __future__ import annotations

import sqlite3


class ToDoApp:
    def __init__(self):
        self.connection = sqlite3.connect('todo.db')

    def add_task(self):
        user_input__task_name = input("Enter task name: ").strip()

        if len(user_input__task_name) == 0:
            print("Task name must have at least one character.")
            exit(1)

        if self.find_task(user_input__task_name) is not None:
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

        self.connection.execute(
            "INSERT INTO tasks (name, priority) VALUES (?, ?)",
            (user_input__task_name, user_input__task_priority)
        )

        self.connection.commit()

    def find_task(self, name: str) -> tuple | None:
        return self.connection.execute(
            "SELECT id, name, priority FROM tasks WHERE name = ?",
            (name,)
        ).fetchone()

    def show_tasks(self):
        for row in self.connection.execute("SELECT id, name, priority FROM tasks"):
            print(row)

    def change_priority(self):
        pass

    def delete_task(self):
        pass

    def main_menu(self):
        options = {
            1: ("Show Tasks", self.show_tasks),
            2: ("Add Task", self.add_task),
            3: ("Change Priority", self.change_priority),
            4: ("Delete Task", self.delete_task),
            5: ("Exit", lambda _: exit(0))
        }


if __name__ == '__main__':
    def main():
        ToDoApp().show_tasks()


    main()
