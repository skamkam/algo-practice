# Name:  Sarah Kam
# Peers:  N/A
# References:  N/A
import time
import random

# INCLUDE TEST CASES TO SUCCEED *AND* FAIL

### DO NOT EDIT ###
def new_array(size: int):
    L = [0] * size
    return L
### END ###

def random_array(size: int):    # for testing; creates given size arr of rand nums from 0-99
    L = new_array(size)
    for i in range(size):
        L[i] = random.randint(0, 100)
    return L

# Problem 1(a): SWAP (COPY)
def swapcopy(arr, pos1, pos2):      # this is O(n) because have to copy the whole array
    copyarr = new_array(len(arr))   # create new array the size of old arr
    for i in range(len(arr)):
        if i == pos1:
            copyarr[i] = arr[pos2]
        elif i == pos2:
            copyarr[i] = arr[pos1]
        else:
            copyarr[i] = arr[i]
    return copyarr

# Problem 1(b): SWAP (IN PLACE)
def swapinplace(arr, pos1, pos2):   # this is O(1)
    temp = arr[pos1]
    arr[pos1] = arr[pos2]     # perform the swaps
    arr[pos2] = temp
    return arr

# Problem 2: SUM OF FIRST n INTEGERS
def gaussiansum(n):     # O(1)
    return n * (n-1) / 2

def sumfirstnnums(n):   # O(n)
    ans = 0
    for i in range(n+1):
        ans += i
    return ans

#Problem 3: SUM OF ARRAY OF NUMBERS
def sumarray(a):
    ans = 0
    for n in a:
        ans += n
    return ans

# Problem 4: MAX VALUE OF ARRAY OF NUMBERS
def maxarray(a):
    max = a[0]
    for n in a:
        if n > max:
            max = n
    return max

# Problem 5: POSITION OF MIN VALUE OF ARRAY OF NUMBERS
def minpos(a):
    min_pos = 0
    for i in range(len(a)):
        if a[i] < a[min_pos]:
            min_pos = i
    return min_pos

# Problem 6(a): SORT EVEN AND ODD NUMBERS (ARRAY)
def evenoddarr(a):
    even = [0] * len(a)
    odd = [0] * len(a)
    even_ptr = 0
    odd_ptr = 0
    for val in a:
        if val % 2 == 0:    # even
            even[even_ptr] = val
            even_ptr += 1
        else:               # odd
            odd[odd_ptr] = val
            odd_ptr += 1
    
    final_even = [0] * even_ptr     # counts # even nums via even_ptr
    for i in range(even_ptr):
        final_even[i] = even[i]     # copy the even number over to final_even
    
    final_odd = [0] * odd_ptr       # counts # odd nums via odd_ptr
    for i in range(odd_ptr):
        final_odd[i] = odd[i]
    
    return final_even, final_odd

# Problem 6(b): SORT EVEN AND ODD NUMBERS (LIST)
def evenoddlist(a):
    even = []
    odd = []
    for val in a:
        if val % 2 == 0:    # even
            even.append(val)
        else:
            odd.append(val)
    return even, odd

# Problem 7: MERGE TWO ARRAYS
def mergearr(a, b):
    size_a = len(a)
    size_b = len(b)
    final_size = size_a + size_b
    arr = [0] * final_size
    for i in range(size_a):
        arr[i] = a[i]
    for i in range(size_b):
        arr[i + size_a] = b[i]      # fill in the remaining spaces in arr w/ b's values
    return arr

# Problem 8: FIND A NUMBER
def findnum(arr, x):
    for val in arr:
        if val == x:
            return True
    return False


# Problem 9: INSERT
def insert(arr, x):
    n = len(arr)
    ans = [0] * (n + 1)
    # ans[i] = [arr[i] for i in arr] i think this syntax only works for lists & we're faking an arr
    for i in range(n):
        ans[i] = arr[i]
    ans[-1] = x
    return ans

# MAIN

def main():
    # Creates the first n numbers in the Fibonacci sequence.
    n = 10      # Try for numbers up to 100000. 
    start_time_create = time.time()    # Get start Time.
    M = new_array(n)
    M[0] = 1
    M[1] = 1
    for j in range(2, len(M)):
        M[j] = M[j-1] + M[j-2]
    end_time_create = time.time()      # Get end Time.   
    print("%s seconds to create %d number of the Fibonacci sequence" % ((end_time_create - start_time_create),n))    
    

    randlist = random_array(100)
    print(swapcopy(randlist, 2, 4))
    print(swapinplace(randlist, 2,4))

    print(minpos([10,20,4,3,5,10]))

    print(evenoddarr([0, 1,2,3,4,5,6,7,99,98,99,100]))
    print(evenoddlist([0, 1,2,3,4,5,6,7,99,98,99,100]))

    print(mergearr([0,1,2,3],[4,3,4,3,5,6]))

    print(insert([0,1,2,3,5,8], 13))

    
   
    

if __name__ == "__main__":    
    main()