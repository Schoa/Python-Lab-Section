def process_employee_hours(employee_data):
    # List to store employees who worked more than 40 hours
    qualified_employees = []

    for data in employee_data:
        # Split the input data into parts
        parts = data.split()
        name = parts[0]
        hours = list(map(int, parts[1:]))  # Convert hours to integers
        
        # Calculate total hours worked
        total_hours = sum(hours)

        # Check if total hours is greater than 40
        if total_hours > 40:
            qualified_employees.append((name, total_hours))

    # Sort employees by total hours (descending) and by name (ascending)
    qualified_employees.sort(key=lambda x: (-x[1], x[0]))

    return qualified_employees

# Input
n = int(input())
employee_data = []

for _ in range(n):
    employee_data.append(input())

# Output
print(process_employee_hours(employee_data))