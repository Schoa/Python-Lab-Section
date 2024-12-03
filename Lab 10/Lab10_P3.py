def sum_of_digits(num, position=0):
    # Convert to positive if the number is negative
    num = abs(num)
    
    # Base case: if num is 0, return 0
    if num == 0:
        return 0
    
    # Get the last digit
    lastDigit = num % 10

    # Check if the current position is even
    if position % 2 == 0:
        # Add last_digit to the sum and continue recursion with the rest of the number
        return lastDigit + sum_of_digits(num // 10, position + 1)
    else: # Skip
        return sum_of_digits(num // 10, position + 1)
    
# Input
num = int(input())

# Output
print(sum_of_digits(num, position=0))