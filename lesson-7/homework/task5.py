class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

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
                    self.employees[employee_id] = Employee(employee_id, name, position, float(salary))
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

def load_employees(self):
    try:
        with open(self.filename, "r") as file:
            for line in file:
                emp_data = line.strip().split(", ")
                employee_id, name, position, salary = emp_data
                self.employees[employee_id] = Employee(employee_id, name, position, float(salary))
    except FileNotFoundError:
        print(f"{self.filename} not found. Starting with an empty employee list.")

def save_employees(self):
    with open(self.filename, "w") as file:
        for employee in self.employees.values():
            file.write(f"{employee.employee_id}, {employee.name}, {employee.position}, {employee.salary}\n")

def add_employee(self, employee):
    if employee.employee_id in self.employees:
        print(f"Employee with ID {employee.employee_id} already exists.")
    else:
        self.employees[employee.employee_id] = employee
        self.save_employees()
        print(f"Employee {employee.name} added successfully.")

def view_all_employees(self):
    if not self.employees:
        print("No employees to display.")
    else:
        for emp in self.employees.values():
            print(emp)

def search_employee(self, employee_id):
    employee = self.employees.get(employee_id)
    if employee:
        print(employee)
    else:
        print(f"Employee with ID {employee_id} not found.")

def update_employee(self, employee_id, name=None, position=None, salary=None):
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
    if employee_id in self.employees:
        del self.employees[employee_id]
        self.save_employees()
        print(f"Employee with ID {employee_id} deleted successfully.")
    else:
        print(f"Employee with ID {employee_id} not found.")

# Create an instance of EmployeeManager
manager = EmployeeManager()

# Add employees
employee1 = Employee("E001", "John Doe", "Software Engineer", 70000)
employee2 = Employee("E002", "Jane Smith", "Data Analyst", 65000)

manager.add_employee(employee1)
manager.add_employee(employee2)

# View all employees
manager.view_all_employees()

# Search for an employee
manager.search_employee("E001")

# Update an employee's details
manager.update_employee("E001", name="Johnathan Doe", salary=75000)

# Delete an employee
manager.delete_employee("E002")

# View all employees after deletion
manager.view_all_employees()

