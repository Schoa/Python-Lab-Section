# Input
numbers = list(map(int, input().split()))

def find_min_max(numbers):
    # Find minimum
    minVal = numbers[0]

    for n in numbers:
        if n < minVal:
            minVal = n

    # Find maximum
    maxVal = numbers[0]

    for i in numbers:
        if i > maxVal:
            maxVal = i

    return minVal, maxVal

def count_frequency(numbers):
    a, b = find_min_max(numbers)

    freqList = [0] * (b - a + 1) # Empty frequency counting list 

    for num in numbers:
        freqList[num - a] += 1

    return freqList

def counting_sort(numbers):
    # Finding the maximum element of input_array.
    M = b

    # Initializing count_array with 0
    count_array = [0] * (M + 1)

    # Mapping each element of input_array as an index of count_array
    for num in numbers:
        count_array[num] += 1

    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    # Creating output_array from count_array
    output_array = [0] * len(numbers)

    for i in range(len(numbers) - 1, -1, -1):
        output_array[count_array[numbers[i]] - 1] = numbers[i]
        count_array[numbers[i]] -= 1

    return output_array

# Out put
a, b = find_min_max(numbers)
print(a, b)
print(count_frequency(numbers))
print(counting_sort(numbers))