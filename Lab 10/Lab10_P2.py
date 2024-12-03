import time

# Sequential
def  print_pattern_sequential(n):
    print("Sequential:")
    for i in range(1, n + 1):
        print("*" * i)

# Recursive
def print_pattern_recursive(n, row=1):
    if row > n:
        return  # Base case: stop when row exceeds n
    print('*' * row)  # Print stars for the current row
    print_pattern_recursive(n, row + 1)  # Recursive call for the next row

# Input
n = int(input())

# Output
start_time = time.perf_counter ()
print_pattern_sequential(n)
end_time = time.perf_counter ()
print( f" Execution Time ( Sequential ) : { end_time - start_time :.8f}seconds")

start_time = time.perf_counter ()
print("Recursive:")
print_pattern_recursive(n, row=1)
end_time = time.perf_counter ()
print( f" Execution Time ( Recursive ) : { end_time - start_time:.8f}seconds")