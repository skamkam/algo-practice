# Grokking Algorithms Ch 3 Recursion practice

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):   # starting at 1, 2, 3, 5, ... prints the nth fib number
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(factorial(5))
print(fibonacci(7))

