import time

# Sequential
def fibonacci_sequential(n):
    """
    F(0) = 0,F(1) = 1,and F(n) = F(n−1) + F(n−2), for n>1
    """
    # Base case
    if n == 0:
        return 0
    elif n ==1:
        return 1
    
    # To store the curr Fibonacci number
    curr = 1

    # To store the previous Fibonacci numbers
    prev = 0

    # Loop to calculate Fibonacci numbers from 2 to n
    for i in range(2, n + 1):
        # Calculate the nth Fibonacci number
        prev, curr = curr, prev + curr
    return curr

# Recursive
def fibonacci_recursive(n):
    """
    F(0) = 0,F(1) = 1,and F(n) = F(n−1) + F(n−2), for n>1
    """
    # Base case
    if n <= 1:
        return n
    
    # Recursive case: sum of the two preceding Fibonacci numbers
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Input
n = int(input())

# Output
start_time = time.perf_counter ()
print("Sequential:", fibonacci_sequential(n))
end_time = time.perf_counter ()
print( f" Execution Time ( Sequential ) : { end_time - start_time :.8f}seconds")

start_time = time.perf_counter ()
print("Recursive:", fibonacci_recursive(n))
end_time = time.perf_counter ()
print( f" Execution Time ( Recursive ) : { end_time - start_time:.8f}seconds")