#Day-15 on python
''' Hi :), this is Day-15 in Python.
Congratulations for reaching Day-15.
In this day you are completing a project with files and classes.
'''

# Project: task manager with file storage

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                tasks = [line.strip() for line in file if line.strip()]
            return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def show_tasks(self):
        print("--- Task List ---")
        if not self.tasks:
            print("There are no saved tasks.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        print("-------------------")


def run_app():
    manager = TaskManager("tasks.txt")

    while True:
        print("\nTask menu:")
        print("1. Show tasks")
        print("2. Add task")
        print("0. Exit")
        option = input("Select an option: ")

        if option == "1":
            manager.show_tasks()
        elif option == "2":
            task = input("Write the task: ")
            manager.add_task(task)
        elif option == "0":
            print("Saving and exiting. See you later.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    run_app()
