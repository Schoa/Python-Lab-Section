def divide(a, b):
    return a / b

try:
    # Input
    a = int(input())
    b = int(input())

    # Perform the division
    result = divide(a, b)

except ZeroDivisionError:
    # Division by zero
    print("Error: Division by zero is not allowed.")

else:
    # No Error
    print("Result:", result)
  
finally:
    # Runs regardless of whether an Error occurred or not
    print("Execution complete.")