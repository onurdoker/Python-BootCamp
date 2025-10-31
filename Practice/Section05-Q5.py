"""
Create a TO-DO list. In the created task list, ask the user for task, manage the task list, check the status of tasks, and end the program after
thanking the user when all tasks are completed.
"""


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"name": task, "completed": False})
        print("Your task is added successfully!.")

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
        else:
            print("Your TODO List")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else " Not Completed"
                print(f"{i+1}. {task['name']} - {status}")

    def complete_task(self, task_number):
        try:
            if 0 <= task_number < len(self.tasks):
                self.tasks[task_number]["completed"] = True
                print("Task marked as completed")
            else:
                print("Invalid task number, please enter a valid task number.")
        except IndexError:
            print("Please enter a valid task number.")


def main():
    todo_list = TodoList()

    while True:
        action = input(
            "\nPlease choose one of the following options: \n'ADD' to add a new task,\n'COMPLETE' to mark a task as done, \n'SHOW' to see all tasks, \n'QUIT' to exit the program.\n"
        ).lower()

        if action == "add":
            name = input("Please enter a new task name: ")
            todo_list.add_task(name)
        elif action == "complete":
            todo_list.show_tasks()

            try:
                task_number = (
                    int(input("Please enter the number of tasks to mark as done: ")) - 1
                )
                todo_list.complete_task(task_number)
            except ValueError:
                print("Please enter a valid task number.")

        elif action == "show":
            todo_list.show_tasks()

        elif action == "quit":
            print("Thank you!")
            break
        else:
            print("Invalid command, please enter a valid command.")


if __name__ == "__main__":
    main()
