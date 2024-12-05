class Rectangle:
    def __init__(self, length, width):
        self.length = length # Initialize Length
        self.width = width # Initialize Width

    def area(self):
        """Calculating Area of Rectangle"""
        return self.length * self.width
    
    def perimeter(self):
        """Calculating Perimeter of Rectangle"""
        return (self.width + self.length) * 2
    
    def __str__(self):
         """Return a string representation of the rectangle."""
         return f"Rectangle(length={self.length}, width={self.width})"
    
    def __eq__(self, other):
        """Check if two Rectangle is equal"""
        return self.area() == other.area()
    
    def __lt__(self, other):
        """Check if Rectangle_1 is smaller than Rectangle_2"""
        return self.area() < other.area()
    
# Read input for the first rectangle
length1, width1 = map(int, input().split())
rect1 = Rectangle(length1, width1)

# Read input for the second rectangle
length2, width2 = map(int, input().split())
rect2 = Rectangle(length2, width2)

# Output properties of both rectangles
print(rect1)
print(rect2)

# Output area of the first rectangle
print(rect1.area())

# Output perimeter of the second rectangle
print(rect2.perimeter())

# Compare rectangles and output result
if rect1 > rect2:
    print("bigger")
elif rect1 < rect2:
    print("smaller")
else:
    print("equal")