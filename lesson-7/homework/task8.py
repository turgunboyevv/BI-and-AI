class Employee:
    def __init__(self, employee_id, name, position, salary):
        """Initialize the employee with their details."""
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        """Return a string representation of the employee."""
        return f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        """Initialize the manager with the filename."""
        self.filename = filename

    def add_employee(self, employee):
        """Add a new employee to the file."""
        with open(self.filename, "a") as file:
            file.write(f"{employee.employee_id}, {employee.name}, {employee.position}, {employee.salary}\n")
        print(f"Employee {employee.name} added successfully.")

    def view_all_employees(self):
        """View all employee records stored in the file."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                if lines:
                    for line in lines:
                        print(line.strip())
                else:
                    print("No employees to display.")
        except FileNotFoundError:
            print(f"{self.filename} not found. No employees to display.")

    def search_employee(self, employee_id):
        """Search for an employee by their employee ID."""
        found = False
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    emp_data = line.strip().split(", ")
                    if emp_data[0] == employee_id:
                        print(f"Employee found: {line.strip()}")
                        found = True
                        break
                if not found:
                    print(f"Employee with ID {employee_id} not found.")
        except FileNotFoundError:
            print(f"{self.filename} not found. Cannot search for employee.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        """Update the details of an employee by their employee ID."""
        found = False
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            with open(self.filename, "w") as file:
                for line in lines:
                    emp_data = line.strip().split(", ")
                    if emp_data[0] == employee_id:
                        if name:
                            emp_data[1] = name
                        if position:
                            emp_data[2] = position
                        if salary is not None:
                            emp_data[3] = str(salary)
                        file.write(", ".join(emp_data) + "\n")
                        print(f"Employee {employee_id} updated successfully.")
                        found = True
                    else:
                        file.write(line)

            if not found:
                print(f"Employee with ID {employee_id} not found.")
        except FileNotFoundError:
            print(f"{self.filename} not found. Cannot update employee.")

    def delete_employee(self, employee_id):
        """Delete an employee from the file using their employee ID."""
        found = False
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            with open(self.filename, "w") as file:
                for line in lines:
                    emp_data = line.strip().split(", ")
                    if emp_data[0] == employee_id:
                        print(f"Employee {employee_id} deleted successfully.")
                        found = True
                    else:
                        file.write(line)

            if not found:
                print(f"Employee with ID {employee_id} not found.")
        except FileNotFoundError:
            print(f"{self.filename} not found. Cannot delete employee.")

    def display_menu(self):
        """Display the menu and handle user input."""
        while True:
            print("\nMenu:")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")

            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Employee Name: ")
                position = input("Enter Employee Position: ")
                salary = float(input("Enter Employee Salary: "))
                employee = Employee(employee_id, name, position, salary)
                self.add_employee(employee)

            elif choice == "2":
                self.view_all_employees()

            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)

            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new name (Leave blank to keep current): ")
                position = input("Enter new position (Leave blank to keep current): ")
                salary_input = input("Enter new salary (Leave blank to keep current): ")
                salary = float(salary_input) if salary_input else None
                self.update_employee(employee_id, name if name else None, position if position else None, salary)

            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please select a number between 1 and 6.")

manager = EmployeeManager()  # Create an instance of EmployeeManager
manager.display_menu()  # Start the menu system to interact with employee records

#E001, John Doe, Software Engineer, 70000
#E002, Jane Smith, Data Analyst, 65000
#E003, Robert Brown, HR Manager, 75000
