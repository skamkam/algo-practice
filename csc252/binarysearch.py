"""
09/13/2023 in-class exercise
Binary search

09/27/2023 in-class exercise
Recursive binary search
"""

def iterBinSearch(arr, item):   # iterative
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2   # integer division rounds down
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:   # guess was smaller than item
            low = mid + 1       # set the new lower bound to mid+1
        elif arr[mid] > item:   # guess was larger than item
            high = mid - 1      # set the new upper bound to mid-1
    return None

def recBinSearch(arr, item): # recursive
    mid = len(arr) // 2
    guess = arr[mid]

    if guess == item:       # if the mid item is exactly it, return mid
        return mid
    elif len(arr) == 1:
        return None
    elif guess > item:      # bottom half of list - indexing isn't affected
        return recBinSearch(arr[:mid], item)
    else:
        found = recBinSearch(arr[mid+1:], item)
        if found != None:
            return found + mid + 1      # top half of list - have to add back the index
        else:
            return None


myList = [1, 5, 7, 9]
print(iterBinSearch(myList, 5))
print(recBinSearch(myList, 5))