import math

def solve_quadratic(a, b, c):
    if a == 0:
        return "Error: Not a quadratic equation (a cannot be zero)"
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "Error: No real solutions"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Solutions: {root1}, {root2}"

try:
    # Input from the user
    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))
    
    # Solve the quadratic equation
    result = solve_quadratic(a, b, c)

except ValueError:
    # Handle invalid input that cannot be converted to an integer
    print("Error: Please enter valid integers for coefficients a, b, and c.")

finally:
    # This block runs regardless of whether an exception occurred or not
    print(result if 'result' in locals() else "No result to display.")
    print("Attempted to solve the equation.")