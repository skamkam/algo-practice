# Sarah Kam
# Grokking Algorithms Ch 4 Exercises
# 9/29/23

def sum(arr):       # Write out the code for the earlier sum function.
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

def count_items(arr):       # Write a recursive function to count the number of items in a list.
    if len(arr) == 1:
        return 1
    elif len(arr) == 0:
        return 0
    else:
        return 1 + count_items(arr[1:])

def findmax(arr):       # Find the maximum number in a list.
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 0:
        return None
    else:
        compare = findmax(arr[1:])
        if arr[0] > compare:
            return arr[0]
        else:
            return compare




myList = []
#print(sum(myList))
#print(count_items(myList))
print(findmax(myList))
