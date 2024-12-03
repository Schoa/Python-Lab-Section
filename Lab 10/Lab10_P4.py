def is_special_palindrome(inp_str, diff=0):
    # Helper function to perform the recursive check
    def check_palindrome(left, right):
        nonlocal diff  # Access the outer diff variable

        # Base case: if left index crosses right index
        if left >= right:
            return diff <= 2  # Check if differences are within the limit

        # Compare characters at left and right indices
        if inp_str[left] != inp_str[right]:
            diff += 1  # Increment difference count

        # If differences exceed 2, return False early
        if diff > 2:
            return False

        # Recursive call moving towards the center of the string
        return check_palindrome(left + 1, right - 1)

    # Start recursion with left and right indices
    return check_palindrome(0, len(inp_str) - 1)

# Input
inp_str = str(input())

# Output
print(is_special_palindrome(inp_str, diff=0))