#!/usr/bin/env python3
def print_fibonacci(length):
    fibonacci_sequence = []
    a, b = 0, 1
    
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    print(fibonacci_sequence)

print_fibonacci(0)  # Output: []
print_fibonacci(1)  # Output: [0]
print_fibonacci(9)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]

