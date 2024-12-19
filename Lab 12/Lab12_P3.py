class Employee:
    def __init__(self, employee_id, name):
        self.__employee_id = employee_id
        self.__name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def get_employee_info(self):
        return f"Employee ID: {self.__employee_id}, Name: {self.__name}"


class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


n = int(input())  # Read number of employees
employees = []

for _ in range(n):
    data = input().split()
    
    if len(data) == 3:  # Full-time employee
        employee_id = data[0]
        name = data[1]
        monthly_salary = float(data[2])
        employee = FullTimeEmployee(employee_id, name, monthly_salary)
    
    elif len(data) == 4:  # Part-time employee
        employee_id = data[0]
        name = data[1]
        hourly_rate = float(data[2])
        hours_worked = float(data[3])
        employee = PartTimeEmployee(employee_id, name, hourly_rate, hours_worked)
    
    employees.append(employee)

for emp in employees:
    salary = emp.calculate_salary()
    print(f"{emp.get_employee_info()}, Salary: {salary:.1f}")