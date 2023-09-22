"""
09/13/2023 in-class exercise
Binary search
"""

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + high // 2   # integer division rounds down
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:   # guess was smaller than item
            low = mid + 1       # set the new lower bound to mid+1
        elif arr[mid] > item:   # guess was larger than item
            high = mid - 1      # set the new upper bound to mid-1
    return None

myList = [1, 5, 7, 9]
print(binary_search(myList, 3))