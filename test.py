def counting_sort(numbers):
    """Sorts an array using the Counting Sort algorithm."""
    # Step 1: Find maximum value
    max_val = max(numbers)

    # Step 2: Initialize count array
    count = [0] * (max_val + 1)

    # Step 3: Count occurrences of each value
    for num in numbers:
        count[num] += 1

    # Step 4: Modify count array to store cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build output array
    output = [0] * len(numbers)
    for num in reversed(numbers):  # To maintain stability
        output[count[num] - 1] = num
        count[num] -= 1

    # Step 6: Copy sorted elements back to original array (if needed)
    for i in range(len(numbers)):
        numbers[i] = output[i]

# Example usage
if __name__ == "__main__":
    unsorted_numbers = [4, 2, -3, 8, 3, -7, 1]
    print("Original array:", unsorted_numbers)
    counting_sort(unsorted_numbers)
    print("Sorted array:", unsorted_numbers)
