# Input: length, width
length = int(input())
width = int(input())

# Calculator
def calculate_area(length, width):
    """
    length >= 0
    width >=

    Rectangle area = legth * width
    """

    # assert length, and width is positive
    assert length > 0, "Length must be positive."
    
    assert width > 0, "Width must be positive."

    # Calculate and return the area of the rectangle
    area = length * width
    return area

# Print
print("Area: ", calculate_area(length, width))