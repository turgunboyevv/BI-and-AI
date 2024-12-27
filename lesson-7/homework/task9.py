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

    def to_csv(self):
        """Return the employee details as a CSV string (for saving in a file)."""
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        """Initialize the manager with the filename."""
        self.filename = filename

    def employee_exists(self, employee_id):
        """Check if an employee with the given ID already exists."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    emp_data = line.strip().split(", ")
                    if emp_data[0] == employee_id:
                        return True
        except FileNotFoundError:
            return False
        return False

    def add_employee(self, employee):
        """Add a new employee to the file."""
        if self.employee_exists(employee.employee_id):
            print(f"Error: Employee with ID {employee.employee_id} already exists.")
            return
        
        try:
            with open(self.filename, "a") as file:
                file.write(employee.to_csv() + "\n")
            print(f"Employee {employee.name} added successfully.")
        except Exception as e:
            print(f"Error while adding employee: {e}")

    def view_all_employees(self, sort_by=None):
        """View all employee records, optionally sorting them by a field (name or salary)."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                if not lines:
                    print("No employees to display.")
                    return

                employees = []
                for line in lines:
                    emp_data = line.strip().split(", ")
                    employees.append(Employee(emp_data[0], emp_data[1], emp_data[2], float(emp_data[3])))

                if sort_by == "salary":
                    employees.sort(key=lambda emp: emp.salary)
                elif sort_by == "name":
                    employees.sort(key=lambda emp: emp.name)

                for emp in employees:
                    print(emp)
        except FileNotFoundError:
            print(f"{self.filename} not found. No employees to display.")
        except Exception as e:
            print(f"Error while reading employees: {e}")

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
        except Exception as e:
            print(f"Error while searching employee: {e}")

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
        except Exception as e:
            print(f"Error while updating employee: {e}")

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
        except Exception as e:
            print(f"Error while deleting employee: {e}")

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
                if self.employee_exists(employee_id):
                    print(f"Error: Employee with ID {employee_id} already exists.")
                    continue
                name = input("Enter Employee Name: ")
                position = input("Enter Employee Position: ")
                while True:
                    try:
                        salary = float(input("Enter Employee Salary: "))
                        break
                    except ValueError:
                        print("Invalid salary input. Please enter a valid number.")
                employee = Employee(employee_id, name, position, salary)
                self.add_employee(employee)

            elif choice == "2":
                sort_option = input("Sort by (name/salary/none): ").strip().lower()
                self.view_all_employees(sort_by=sort_option if sort_option in ["name", "salary"] else None)

            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)

            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new name (Leave blank to keep current): ")
                position = input("Enter new position (Leave blank to keep current): ")
                while True:
                    salary_input = input("Enter new salary (Leave blank to keep current): ")
                    if salary_input == "":
                        salary = None
                        break
                    try:
                        salary = float(salary_input)
                        break
                    except ValueError:
                        print("Invalid salary input. Please enter a valid number.")
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
