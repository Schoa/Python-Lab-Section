# Input
numbers = list(map(int, input().split()))

def find_min_max(numbers):
    """
    Bubble Sort Algorithm Implementation:
        Range of the array is from 0 to n-i-1
        Swap the elements if the element found is greater than the adjacent element
    """

    n = len(numbers)

    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):            
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    minVal = numbers[0]
    maxVal = numbers[-1]

    return minVal, maxVal

def count_frequency(numbers):
    a, b = find_min_max(numbers)

    freqList = [0] * (b - a + 1) # Empty frequency counting list 

    for num in numbers:
        freqList[num - a] += 1

    return freqList

def counting_sort(numbers):
    """
    Bubble Sort Algorithm Implementation:
        Range of the array is from 0 to n-i-1
        Swap the elements if the element found is greater than the adjacent element
    """

    n = len(numbers)

    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):            
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(numbers)

# Out put
a, b = find_min_max(numbers)
print(a, b)
print(count_frequency(numbers))
counting_sort(numbers)