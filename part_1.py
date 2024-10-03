# Function to calculate area and perimeter of the rectangle
def rectangle_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Input: length and width of the rectangle
input_length_width = input()
length, width = map(
    int, input_length_width.split()
)

# Ensure the values are within the specified range
if 1 <= length <= 100000 and 1 <= width <= 100000:
    area, perimeter = rectangle_area_and_perimeter(length, width)
    print(area, perimeter)
else:
    print("Error: Value too big")