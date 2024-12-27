class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        """Initialize a task."""
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        """Return a string representation of the task (for displaying)."""
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_csv(self):
        """Return the task as a CSV string for saving to file."""
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date or ''}, {self.status}"

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        """Initialize the task manager with a filename."""
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the file."""
        tasks = []
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    task_data = line.strip().split(", ")
                    if task_data:
                        task = Task(task_data[0], task_data[1], task_data[2], task_data[3], task_data[4])
                        tasks.append(task)
        except FileNotFoundError:
            pass  # File does not exist, return empty list
        return tasks

    def save_tasks(self):
        """Save tasks to a file."""
        try:
            with open(self.filename, "w") as file:
                for task in self.tasks:
                    file.write(task.to_csv() + "\n")
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, task):
        """Add a new task."""
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        """View all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        """Update a task's details using the task ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                if title: task.title = title
                if description: task.description = description
                if due_date: task.due_date = due_date
                if status: task.status = status
                print(f"Task {task_id} updated successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task by its task ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    def filter_tasks(self, status):
        """Filter tasks by status (Pending, In Progress, Completed)."""
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered_tasks:
            print(f"No tasks found with status {status}.")
        else:
            for task in filtered_tasks:
                print(task)

def display_menu():
    task_manager = TaskManager()

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD, optional): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")

            task = Task(task_id, title, description, due_date, status)
            task_manager.add_task(task)

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (Leave blank to keep current): ")
            description = input("Enter new Description (Leave blank to keep current): ")
            due_date = input("Enter new Due Date (Leave blank to keep current): ")
            status = input("Enter new Status (Leave blank to keep current): ")
            task_manager.update_task(task_id, title, description, due_date, status)

        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            task_manager.delete_task(task_id)

        elif choice == "5":
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            task_manager.filter_tasks(status)

        elif choice == "6":
            task_manager.save_tasks()

        elif choice == "7":
            task_manager.load_tasks()

        elif choice == "8":
            print("Exiting the application...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    display_menu()

#Welcome to the To-Do Application!
#1. Add a new task
#2. View all tasks
#3. Update a task
#4. Delete a task
#5. Filter tasks by status
#6. Save tasks
#7. Load tasks
#8. Exit

#Enter your choice: 1
#Enter Task ID: 101
#Enter Title: Finish Homework
#Enter Description: Complete math and science homework.
#Enter Due Date (YYYY-MM-DD, optional
