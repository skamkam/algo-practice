# Grokking Algorithms Ch 3 Recursion practice
# 9/27/23 in-class practice (fibonacci and iterative fibonacci)
# 9/29/23 in-class practice (permutations of a string, parenthesis matching)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):   # starting at 1, 2, 3, 5, ... prints the nth fib number
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def iter_fibonacci(n):  # starting at 1, 2, 3, 5, prints the nth fib num
    a, b = 1, 1
    for i in range(1,n):
        temp = a+b
        b = a
        a = temp
    return a

def string_permutation(str):
    perms = []
    for ch in str:
        pass
    


def parenthesis_match(str):
    count = 0
    left_paren = ord("(")
    right_paren = ord(")")
    for ch in str:
        letnum = ord(ch)
        if letnum == left_paren:
            count += 1
        elif letnum == right_paren and count > 0:       # checking for stuff like ")))"
            count -= 1
        elif letnum == right_paren and count <= 0:
            return False
        else:
            continue
    if count == 0:      # all the ( were canceled out by )
        return True
    return False




print(parenthesis_match("(x+1-(y-1)"))

print(factorial(5))
print(fibonacci(5))
print(iter_fibonacci(5))
print(string_permutation("abc"))

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