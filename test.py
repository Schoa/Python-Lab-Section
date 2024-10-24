def find_median(numbers):
    # Sort the list first
    numbers.sort()
    n = len(numbers)
    
    # Calculate the median
    if n % 2 == 1:
        # If odd, return the middle element
        median = numbers[n // 2]
    else:
        # If even, return the average of the two middle elements
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    
    return median

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Call the function and print the result formatted to one decimal place
median_value = find_median(numbers)
print(f"{median_value:.1f}")