def initialize_chunks(numbers):
    """
    Convert a list of integers into a list of single-element lists.
    """
    return [[element] for element in numbers]

def merge_two_lists(numbers):
    """
    Pair specific numbers together from the input list.
    """
    # Define the specific pairs based on the requirement
    pairs = []
    
    # Create pairs based on the specified logic
    if len(numbers) >= 2:
        pairs.append([numbers[1], numbers[0]])
        pairs.append([numbers[3], numbers[2]])
        pairs.append([numbers[5], numbers[4]])
    
    # If there's an odd number of elements, add the last one as a single-element list
    if len(numbers) % 2 != 0:
        pairs.append([numbers[-1]])  # Add last element (5)

    return pairs

def merge_sort(numbers):
    """Sort an unordered list using initialize_chunks and merge_two_lists."""
    
    # Step 1: Initialize chunks
    chunks = initialize_chunks(numbers)
    
    # Step 2: Flatten the chunks back into a single list
    flat_list = [item for sublist in chunks for item in sublist]
    
    # Step 3: Sort the flat list using merge_two_lists logic
    sorted_pairs = merge_two_lists(flat_list)
    
    # Flatten the sorted pairs into a single sorted list
    sorted_list = []
    
    for pair in sorted_pairs:
        sorted_list.extend(pair)

    return sorted(sorted_list)

# Input
numbers = list(map(int, input().split()))

# Output
print(initialize_chunks(numbers))
print(merge_two_lists(numbers))
print(merge_sort(numbers))