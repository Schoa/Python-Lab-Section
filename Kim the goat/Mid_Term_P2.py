n = int(input())
# Prime checker
def prime_checker(n):
    Counter = 0
    if n > 1:
        for i in (1, n):
            if n % i == 0:
                Counter += 1
        
        if Counter > 1:
            return False
        else:
            return True
    else:
        return False

print(prime_checker(n))

def find_divisors(n):
    div = []

    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)

    return div
print(find_divisors(n))

def power_divisors(n):
    