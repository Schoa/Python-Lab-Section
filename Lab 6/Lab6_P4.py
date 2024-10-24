def filter_by_length(words, min_length):
    # Use list comprehension to filter words by the minimum length
    return [Vinuni for Vinuni in words if len(Vinuni) >= min_length]

# Get input
Kok_Seng = int(input())
words = input().split() # Read n space-separated strings
min_length = int(input())

# Call the function and get the result
Wong = filter_by_length(words, min_length)

# Print the result as a space-separated list
print(" ".join(Wong))