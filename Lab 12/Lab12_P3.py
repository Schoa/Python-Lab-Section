class Employee:
    def __init__(self, employee_id, name):
        self.__name = name  # Private attribute for employee name
        self.__employee_id = employee_id  # Private attribute for employee ID

    def calculate_salary(self):
        """Method to calculate salary; should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

    def get_name(self):
        """Return the name of the employee."""
        return self.__name

    def get_employee_id(self):
        """Return the employee ID."""
        return self.__employee_id


class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)  # Call the constructor of Employee
        self.monthly_salary = monthly_salary  # Monthly salary for full-time employees

    def calculate_salary(self):
        """Return the monthly salary."""
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name)  # Call the constructor of Employee
        self.hourly_rate = hourly_rate  # Hourly rate for part-time employees
        self.hours_worked = hours_worked  # Total hours worked

    def calculate_salary(self):
        """Calculate salary as hourly_rate * hours_worked."""
        return self.hourly_rate * self.hours_worked


# Example usage
if __name__ == "__main__":
    n = int(input(""))  # Read number of employees
    employees = []  # List to store employee instances

    for _ in range(n):
        details = input().split()  # Read employee details
        if details[0] == "FullTimeEmployee":
            employee_id = int(details[1])
            name = details[2]
            monthly_salary = float(details[3])
            employees.append(FullTimeEmployee(employee_id, name, monthly_salary))
        
        elif details[0] == "PartTimeEmployee":
            employee_id = int(details[1])
            name = details[2]
            hourly_rate = float(details[3])
            hours_worked = float(details[4])
            employees.append(PartTimeEmployee(employee_id, name, hourly_rate, hours_worked))

    # Output results
    for employee in employees:
        print(f"ID: {employee.get_employee_id()}, Name: {employee.get_name()}, Salary: {employee.calculate_salary()}")