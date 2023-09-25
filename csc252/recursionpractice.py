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

"""
9/25/23 notes
1) make a pile of boxes to look through -> while the pile isn't empty -> grab a box
-> 2) if find a box, add it to the pile of boxes
-> 3) if find a key, done
Then go back to the pile (step 1)

1) go through every item in the box
-> 2) if find a box... -> go back to step 1
-> 3) if find a key, done

Downside of recursion: hard to keep track of what boxes have been opened so far!
"""