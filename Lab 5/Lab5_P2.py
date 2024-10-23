# Sorter
def Kok_Seng(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        smallest = num1
        if num2 <= num3:
            middle = num2
            largest = num3
        else:
            middle = num3
            largest = num2
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
        if num1 <= num3:
            middle = num1
            largest = num3
        else:
            middle = num3
            largest = num1
    else:  # num3 is the smallest
        smallest = num3
        if num1 <= num2:
            middle = num1
            largest = num2
        else:
            middle = num2
            largest = num1
            
    return smallest, middle, largest

# Input
num1, num2, num3 = map(int, input().split())

# Print result
Wong = Kok_Seng(num1, num2, num3)
print(Wong[0], Wong[1], Wong[2])