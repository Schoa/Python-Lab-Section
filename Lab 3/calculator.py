from math_operations import add, subtract, multiply, divide, power, integer_divide

def main():
    # Input: Two numbers
    num1, num2 = map(float, input().split())
    
    # Input: Operator
    operator = input()

    # Perform operation based on operator
    try:
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '**':
            result = power(num1, num2)
        elif operator == '//':
            result = integer_divide(num1, num2)
        else:
            print("Invalid operator!")
            return
        
        # Output result formatted to 2 decimal places
        print(f"{result:.2f}")
    
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()