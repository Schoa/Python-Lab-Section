def Wong(numbers):
    # Calculate the sum of the elements
    total_sum = sum(numbers)
    
    # Find the minimum value in the list
    min_value = min(numbers)
    
    # Find the maximum value in the list
    max_value = max(numbers)
    
    # Reverse the list
    reversed_list = numbers[::-1]
    
    # Print the results
    print(total_sum)
    print(min_value)
    print(max_value)
    print(*reversed_list)

# Get input
Kok_Seng = int(input())
numbers = list(map(int, input().split()))

# Call the function with the input list
Wong(numbers)