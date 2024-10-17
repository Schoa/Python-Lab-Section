#  Leap year checker
def Kok_Seng(year):
    """
    A year is a leap year if it is divisible by 4, 
    but years divisible by 100 are not leap years 
    unless they are also divisible by 400
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("True")
    else:
        print("False")

# Input
year = int(input())

# Print
Kok_Seng(year)