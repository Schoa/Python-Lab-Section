# Input: Celcius & Fahrenheit
unit = int(input())
unit_1 = input()

# Identify Celcius or Fahrenheit & convert
if unit_1 == "C":
    result = (unit * (9/5)) + 32
else:
    result = (unit - 32) * (5/9)

# Ensure the values are within the specified range
if -1000000000 <= unit <= 1000000000 :
    print(result)
else:
    print("Error: Value too big")