from random import randint
from time import time

def generateArray(n):
    arr = [randint(0,100) for i in range(n)]
    return arr

def quicksort(arr):
    if len(arr) < 2:    # base case
        return arr
    else:               # recursive case  
        pivot = arr[0]      # choose the first elt as pivot
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def main():
    starttime = time()
    arr = generateArray(1000)
    # Randomize the array/list before passing it into quicksort
    sorted_arr = quicksort(arr)
    print("elapsed time: " + str(time() - starttime))

if __name__ == "__main__":
    main()