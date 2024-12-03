def permute(nums):
    """
    Generate all permutations of the given list of numbers.
    """
    def backtrack(start=0):
        # Base case: if we've reached the end of the array
        if start == len(nums):
            result.append(nums[:])  # Append a copy of the current permutation
            return
        
        for i in range(start, len(nums)):
            # Swap the current element with the start element
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)  # Recurse on the next index
            # Backtrack: swap back to restore the original array
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack()  # Start generating permutations
    return result

# Input
nums = list(map(int, input().split()))

# Sort the numbers to ensure permutations are generated in sorted order
nums.sort()

# Generate permutations
permutations = permute(nums)

# Sort permutations to ensure they are printed in lexicographical order
permutations.sort()

# Print each permutation in the required format
for perm in permutations:
    print(" ".join(map(str, perm)))