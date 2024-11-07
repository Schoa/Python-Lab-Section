def expression(a: float, b = 25.8):
    assert not a < 0 and not b < 0, 'Only non-negative numbers must be provided'

    try:
        Kok_Seng = (2 + a) / b
        return Kok_Seng

    except ZeroDivisionError:
        return -1
    
a, b = map(int, input().split())
result = expression(a, b)
print(f"{result:.2f}")