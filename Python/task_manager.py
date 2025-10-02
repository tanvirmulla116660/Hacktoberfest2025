class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.counter = 0

    def add_task(self, title):
        self.counter += 1
        task = Task(self.counter, title)
        self.tasks[task.id] = task
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks.values():
                print(task)

    def update_task(self, task_id, new_title):
        task = self.tasks.get(task_id)
        if task:
            task.title = new_title
            print(f"Task updated: {task}")
        else:
            print("Task not found!")

    def complete_task(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            task.mark_completed()
            print(f"Task marked completed: {task}")
        else:
            print("Task not found!")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task deleted.")
        else:
            print("Task not found!")


def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Mark Task Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new title: ")
                manager.update_task(task_id, new_title)
            except ValueError:
                print("Invalid input!")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Invalid input!")
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid input!")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()
