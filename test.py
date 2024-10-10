def calculate_area(length, width):
    # Assert that length is a positive integer
    assert length > 0, "Length must be positive."
    
    # Assert that width is a positive integer
    assert width > 0, "Width must be positive."
    
    # Calculate and return the area of the rectangle
    area = length * width
    return area

# Example usage:
try:
    print(calculate_area(5, 10))  # Output: 50
    print(calculate_area(-5, 10)) # This will raise an assertion error
except AssertionError as e:
    print(e)

try:
    print(calculate_area(5, 0))   # This will also raise an assertion error
except AssertionError as e:
    print(e)