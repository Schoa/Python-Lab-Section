# import Math to get square root
import math

# get Input
A = list(map(float, input().split()))
B = list(map(float, input().split()))

# calculate the distance
def calc_dist(A, B):
    """
    Calculate the distance between two points in 2D space.
        dist(A,B)= √((xA − xB)^2 + (yA − yB)^2)
    """
    xA, yA = A
    xB, yB = B
    dist = math.sqrt((xA - xB) ** 2 + (yA - yB) ** 2)
    return dist

# Output: Print the distance with 2 decimal places
dist = calc_dist(A, B)
print(f"{dist:.2f}")