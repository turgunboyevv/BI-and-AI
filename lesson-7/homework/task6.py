class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        self.employees = {}
        self.load_employees()

    def load_employees(self):
        """Load employees from the file into the dictionary."""
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    emp_data = line.strip().split(", ")
                    employee_id, name, position, salary = emp_data
                    self.employees[employee_id] = (employee_id, name, position, float(salary))
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty employee list.")
        
    def save_employees(self):
        """Save the employee records to the file."""
        with open(self.filename, "w") as file:
            for employee in self.employees.values():
                file.write(f"{employee.employee_id}, {employee.name}, {employee.position}, {employee.salary}\n")

    def add_employee(self, employee):
        """Add a new employee record."""
        if employee.employee_id in self.employees:
            print(f"Employee with ID {employee.employee_id} already exists.")
        else:
            self.employees[employee.employee_id] = employee
            self.save_employees()
            print(f"Employee {employee.name} added successfully.")

    def view_all_employees(self):
        """View all employee records."""
        if not self.employees:
            print("No employees to display.")
        else:
            for emp in self.employees.values():
                print(emp)

    def search_employee(self, employee_id):
        """Search for an employee by ID."""
        employee = self.employees.get(employee_id)
        if employee:
            print(employee)
        else:
            print(f"Employee with ID {employee_id} not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        """Update an employee's information."""
        employee = self.employees.get(employee_id)
        if employee:
            if name:
                employee.name = name
            if position:
                employee.position = position
            if salary is not None:
                employee.salary = salary
            self.save_employees()
            print(f"Employee {employee_id} updated successfully.")
        else:
            print(f"Employee with ID {employee_id} not found.")

    def delete_employee(self, employee_id):
        """Delete an employee record."""
        if employee_id in self.employees:
            del self.employees[employee_id]
            self.save_employees()
            print(f"Employee with ID {employee_id} deleted successfully.")
        else:
            print(f"Employee with ID {employee_id} not found.")
    
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
                employee = employee(employee_id, name, position, salary)
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
            employee = employee(employee_id, name, position, salary)
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
manager.display_menu()  # Call the display_menu method to start the menu system
