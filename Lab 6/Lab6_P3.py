def enumerate_positive(numbers):
    # Create a 2D array for storing index and positive number pairs
    Wong = []

    # Iterate over the list with index
    for index, value in enumerate(numbers):
        if value > 0: # Check if the number is positive
            Wong.append([index, value]) # Append the index and value as a list
    
    return Wong

# Get input
Kok_Seng = int(input())
numbers = list(map(int, input().split()))

#Print result
Vinuni = enumerate_positive(numbers)
print(Vinuni)