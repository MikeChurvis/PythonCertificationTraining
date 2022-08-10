from __future__ import annotations

import sqlite3
from typing import Callable


class ToDoApp:
    def __init__(self):
        self.connection = sqlite3.connect('todo.db')

    def add_task(self):
        print('--- ADD TASK ---')

        user_input__task_name = input("Enter task name: ").strip()

        if len(user_input__task_name) == 0:
            print("[ERROR] Task name must have at least one character.")
            return

        if self.find_task(name=user_input__task_name) is not None:
            print("[ERROR] There is already a task with this name.")
            return

        user_input__task_priority = input("Enter priority: ").strip()

        try:
            user_input__task_priority = int(user_input__task_priority)
            if user_input__task_priority < 1:
                raise ValueError
        except (TypeError, ValueError):
            print("[ERROR] Task priority must be an integer greater than or equal to 1.")
            return

        self.connection.execute(
            "INSERT INTO tasks (name, priority) VALUES (?, ?)",
            (user_input__task_name, user_input__task_priority)
        )

        self.connection.commit()

        print("[SUCCESS] Task added.")

    def find_task(self, *, task_id: int = None, name: str = None) -> tuple | None:
        where_statement_parts = []
        where_args = []

        if name is not None:
            where_statement_parts.append("name = ?")
            where_args.append(name)

        if task_id is not None:
            where_statement_parts.append("id = ?")
            where_args.append(task_id)

        where_statement = " AND ".join(where_statement_parts)
        where_statement = "WHERE " + where_statement

        return self.connection.execute(
            "SELECT id, name, priority FROM tasks " + where_statement,
            where_args
        ).fetchone()

    def show_tasks(self):
        print('--- TASKS ---')
        for row in self.connection.execute("SELECT id, name, priority FROM tasks"):
            print(row)

    def change_priority(self):
        print('--- CHANGE PRIORITY ---')
        self.show_tasks()

        task_id = input("Enter the ID of one of the tasks shown above: ").strip()

        try:
            task_id = int(task_id)
        except TypeError:
            print('[ERROR] Task ID must be an integer.')
            return

        if self.find_task(task_id=task_id) is None:
            print('[ERROR] No task exists with that ID.')
            return

        task_priority = input("Enter new priority (>=1): ").strip()

        try:
            task_priority = int(task_priority)
        except TypeError:
            print('[ERROR] Task priority must be an integer.')

        if task_priority < 1:
            print('[ERROR] Task priority must be at least 1.')

        self.connection.execute("UPDATE tasks SET priority = ? WHERE id = ?", (task_priority, task_id))
        self.connection.commit()

        print('[SUCCESS] Task priority changed.')

    def delete_task(self):
        print('--- DELETE TASK ---')
        self.show_tasks()

        task_id = input('Enter the ID of one of the tasks above: ').strip()

        try:
            task_id = int(task_id)
        except TypeError:
            print('[ERROR] Task ID must be an integer.')
            return

        if self.find_task(task_id=task_id) is None:
            print('[ERROR] No task exists with that ID.')
            return

        user_cancelled_delete = input(
            'Are you sure you want to delete this task? This cannot be undone [Y/n]: '
        ).strip().lower() not in ['', 'y']

        if user_cancelled_delete:
            print('[CANCELLED] No tasks were deleted.')
            return

        self.connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.connection.commit()

        print('[SUCCESS] The selected task has been deleted.')

    def main_menu(self) -> Callable[[], None]:
        options = {
            "1": ("Show Tasks", self.show_tasks),
            "2": ("Add Task", self.add_task),
            "3": ("Change Priority", self.change_priority),
            "4": ("Delete Task", self.delete_task),
            "5": ("Exit", lambda: exit(0))
        }

        # Start an input capture loop.
        while True:
            print("================")
            for option_key, option_data in options.items():
                print(f"{option_key}. {option_data[0]}")

            user_choice = input("Choose an option [1..5]: ").strip()

            if user_choice not in options:
                print("Invalid choice.")
                continue

            return options[user_choice][1]


if __name__ == '__main__':
    def main():
        app = ToDoApp()

        while True:
            selected_action = app.main_menu()
            selected_action()


    main()
