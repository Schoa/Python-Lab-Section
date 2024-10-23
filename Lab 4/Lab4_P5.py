import math

def solve_quadratic(a, b, c):
    try:
        if a == 0:
            # Handle linear case
            if b == 0:
                return "Error: No solution"  # Both a and b are zero
            else:
                solution = -c / b
                return f"Linear equation, solution: {solution}"
        
        # Calculate discriminant for quadratic case
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return "Error: No real solutions"
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"Solutions: {root1}, {root2}"
    
    except ZeroDivisionError:
        return "Error: Division by zero occurred"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
    finally:
        print("Attempted to solve the equation.")

# Input from the user
a = int(input())
b = int(input())
c = int(input())
    
# Call the function and print the result
result = solve_quadratic(a, b, c)
print(result)