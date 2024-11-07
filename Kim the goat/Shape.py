import math

def calculate_triangle(a: float, b: float, c: float):
    s = (a + b + c)/2
    
    Perimeter_triangle = a + b + c
    Area_triangle = math.sqrt(s*(s - a) * (s - b) * (s - c))

    return Perimeter_triangle, Area_triangle

def calculate_rectangle(a: float, b: float):
    Perimeter_rectangle = 2 * (a + b)
    Area_rectangle = a * b

    return Perimeter_rectangle, Area_rectangle

def calculate_circle(r: float, pi: float):
    Perimeter_circle = 2 * pi * r
    Area_circle = pi * (r ** 2)

    return Perimeter_circle, Area_circle

pi = 3.14
Kok_Seng = input()

if Kok_Seng == "Triangle":
    a, b, c = map(float, input().split())
    print(*calculate_triangle(a, b ,c))

elif Kok_Seng == "Circle":
    r = float(input())
    print(*calculate_circle(r, pi))

elif Kok_Seng == "Rectangle":
    a, b = map(float, input().split())
    print(*calculate_rectangle(a, b))
    
else:
    print("You dumb! You're not Kok-Seng Wong")