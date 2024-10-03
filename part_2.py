# Input: Celcius & Fahrenheit
unit = float(input())
unit_1 = input()

# Identify Celcius or Fahrenheit & convert
def convert(unit):
    if unit_1 == "C":
        result = (unit * (9/5)) + 32
    else:
        result = (unit - 32) * (5/9)
    return result

# Print result & format
result = convert(unit)
print("{result:.2f}".format(result = result))