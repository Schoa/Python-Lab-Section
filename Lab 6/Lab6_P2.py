# Calculate the median of the elements
def find_median(numbers):
    # Sort
    numbers.sort()
    Kok_Seng = len(numbers)

    if Kok_Seng % 2 == 1:
        # If odd, return the middle element
        median = numbers[Kok_Seng // 2]
    else:
        # If even, return the average of the two middle elements
        median = (numbers[Kok_Seng // 2 - 1] + numbers[Kok_Seng // 2]) / 2

    return median

# Get input
Kok_Seng = int(input())
numbers = list(map(int, input().split()))

# Print Medainr5
Wong = find_median(numbers)
print(f"{Wong:.1f}")