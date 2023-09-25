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
def swapcopy(arr, pos1, pos2):
    n = len(arr)
    copyarr = new_array(n)
    if n == 0 or pos1 >= n or pos2 >= n or pos1 < 0 or pos2 < 0:  # empty arr or bad position inputs
        for i in range(n):
            copyarr[i] = arr[i]
    else:       # inputs good, makes a copy with swaps
        for i in range(n):
            if i == pos1:
                copyarr[i] = arr[pos2]
            elif i == pos2:
                copyarr[i] = arr[pos1]
            else:
                copyarr[i] = arr[i]
    return copyarr

# Problem 1(b): SWAP (IN PLACE)
def swapinplace(arr, pos1, pos2):   # this is O(1)
    n = len(arr)
    if n == 0 or pos1 >= n or pos2 >= n or pos1 < -n or pos2 < -n:  # empty arr or bad position inputs
        return arr      # if bad input just return the same arr with no swaps
    temp = arr[pos1]
    arr[pos1] = arr[pos2]     # perform the swaps
    arr[pos2] = temp
    return arr

# Problem 2: SUM OF FIRST n INTEGERS
def gaussiansum(n):     # O(1)
    if n < 0 or type(n) != int:           # if the input is negative, no first n nums
        return None
    return n * (n+1) // 2   # it will always be even bc one of n or n-1 must be even

def sumfirstnnums(n):   # O(n)
    if n < 0 or type(n) != int:           # if the input is negative, no first n nums
        return None

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
    if len(a) == 0:     # if empty array, no max
        return None

    max = a[0]
    for n in a:
        if n > max:
            max = n
    return max

# Problem 5: POSITION OF MIN VALUE OF ARRAY OF NUMBERS
def minpos(a):
    if len(a) == 0:     # if the array is size 0
        return None

    min_pos = 0
    for i in range(len(a)):
        if a[i] < a[min_pos]:
            min_pos = i
    return min_pos

# Problem 6(a): SORT EVEN AND ODD NUMBERS (ARRAY)
def evenoddarr(a):
    even = new_array(a)
    odd = new_array(a)
    even_ptr = 0
    odd_ptr = 0
    for val in a:
        if val % 2 == 0:    # even
            even[even_ptr] = val
            even_ptr += 1
        elif val % 2 == 1:  # odd
            odd[odd_ptr] = val
            odd_ptr += 1
    
    final_even = new_array(even_ptr)     # counts # even nums via even_ptr
    for i in range(even_ptr):
        final_even[i] = even[i]     # copy the even number over to final_even
    
    final_odd = new_array(odd_ptr)       # counts # odd nums via odd_ptr
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
        elif val % 2 == 1:  # odd
            odd.append(val)
    return even, odd

# Problem 7: MERGE TWO ARRAYS
def mergearr(a, b):
    size_a = len(a)
    size_b = len(b)
    final_size = size_a + size_b
    arr = new_array(final_size)
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
    ans = new_array(n + 1)
    # ans[i] = [arr[i] for i in arr] i think this syntax only works for lists & we're faking an arr
    for i in range(n):
        ans[i] = arr[i]
    ans[-1] = x
    return ans

# MAIN

def main():
    starttime = time.time()

    # Test arrays
    n10 = random_array(10)
    n100 = random_array(100)
    n1000 = random_array(1000)
    #print(n10)
    #print(n100)
    #print(n1000)

    # NOTE: Did not include failure cases where bad input (non-arrays, non-ints, etc)
    #       would have caused a program bug. I am assuming inputs are the correct type
    #       even if they aren't inputs that make sense in context of the problem.

    # Testing Problem 1(a): Swap (copy)
    test1a = False
    if test1a == True:
        print(swapcopy(n1000, 0, 1))     # Success
        print(swapcopy(n100, 0, 1))      # Success
        print(swapcopy(n10, 0, -9))      # Failure - returns copy of n10 (neg index not supported for swapcopy)
        print(swapcopy(n100, 100, 101))  # Failure - returns copy of n100 (positions out of range)
        print(swapcopy(n10, 0, 0))       # Success
        print(swapcopy([], 0, 1))        # Failure - returns None (bad position input)

    # Testing Problem 1(b): Swap (in place)
    test1b = False
    if test1b == True:
        print(swapinplace(n1000, 0, 1))     # Success
        print(swapinplace(n100, 0, 1))      # Success
        print(swapinplace(n10, 0, -9))      # Success - uses negative indexing
        print(swapinplace(n100, 99, -101))  # Failure - returns unchanged arr (positions out of range)
        print(swapinplace(n10, 0, 0))       # Success
        print(swapinplace([], 0, 1))        # Failure - returns unchanged arr

    # Testing Problem 2: Sum first n numbers
    test2 = False
    if test2 == True:
        print(gaussiansum(10))      # Success
        print(gaussiansum(100))     # Success
        print(gaussiansum(1000))    # Success
        print(gaussiansum(0))       # Success
        print(gaussiansum(-10))     # Failure - returns None bc first n integers is negative
        print(gaussiansum(0.5))     # Failure - returns None bc first n numbers doesn't make sense w/ non-integers

        print(sumfirstnnums(10))    # Success
        print(sumfirstnnums(100))   # Success
        print(sumfirstnnums(1000))  # Success
        print(sumfirstnnums(0))     # Success
        print(sumfirstnnums(-10))   # Failure - None
        print(sumfirstnnums(0.5))   # Failure - None

    # Testing Problem 3: Sum of array of numbers
    test3 = False
    if test3 == True:
        print(sumarray(n10))        # Success (checked with online calculator)
        print(sumarray(n100))       # Success (checked with online calculator)
        print(sumarray(n1000))      # Success (checked with online calculator)
        print(sumarray([-1, 1, -2, 2]))  # Success
        print(sumarray([-1, -3, -7, -99]))   # Success
        print(sumarray([0.5, 1.3, 9.02]))   # Success
        print(sumarray([]))         # Success - sum is 0
        # Failure state would be trying to add non-numbers, would throw error

    # Testing Problem 4: Max value of array of numbers
    test4 = False
    if test4 == True:
        print(maxarray(n10))        # Success - checked with online calculator
        print(maxarray(n100))       # Success - checked with online calculator
        print(maxarray(n1000))      # Success - checked with online calculator
        print(maxarray([-1,-2,-3,-4,-5]))   # Success
        print(maxarray([0,0,0,0]))          # Success
        print(maxarray([0.5,1.3,9.02]))     # Success
        print(maxarray([]))         # Success - returns None

    # Testing Problem 5: Position of min value of array of numbers
    test5 = False
    if test5 == True:
        # Note: minpos returns the first occurrence of a minimum value
        print(minpos(n10))              # Success - eyeballed
        print(minpos(n100))             # Success - eyeballed
        print(minpos(n1000))            # Success - eyeballed
        print(minpos([]))               # Success - returns None
        print(minpos([-1,-2,-3,-4]))    # Success
        print(minpos([0,0,0]))          # Success - returns 0 (first pos)
        print(minpos([0.5,0.4,0.3]))    # Success

    # Testing Problem 6(a): Sort even and odd numbers (array)
    test6a = False
    if test6a == True:
        print(evenoddarr(n10))              # Success - eyeballed
        print(evenoddarr(n100))             # Success - eyeballed
        print(evenoddarr(n1000))            # Success - eyeballed
        print(evenoddarr([0,2,4]))          # Success - creates an empty list for odd
        print(evenoddarr([]))               # Success - creates 2 empty lists
        print(evenoddarr([-1,-2,-3,-4]))    # Success
        print(evenoddarr([0.1,0.2,0.3]))    # Success - none of these decimals are even or odd so 2 empty lists
    
    # Testing Problem 6(b): Sort even and odd numbers (list)
    test6b = False
    if test6b == True:
        print(evenoddlist(n10))              # Success - eyeballed
        print(evenoddlist(n100))             # Success - eyeballed
        print(evenoddlist(n1000))            # Success - eyeballed
        print(evenoddlist([0,2,4]))          # Success - creates an empty list for odd
        print(evenoddlist([]))               # Success - creates 2 empty lists
        print(evenoddlist([-1,-2,-3,-4]))    # Success
        print(evenoddlist([0.1,0.2,0.3]))    # Success - none of these decimals are even or odd so 2 empty lists
    
    # Testing Problem 7: Merge two arrays
    test7 = False
    if test7 == True:
        n5 = random_array(5)
        print(str(n5) + "\n")
        print(mergearr(n10,n5))         # Success
        print(mergearr(n100,n5))        # Success
        print(mergearr(n1000,n5))       # Success
        print(mergearr([1,2,3],[]))     # Success
        print(mergearr([],[1,2,3]))     # Success
        print(mergearr([],[]))          # Success
        print(mergearr([0.1,0.2,0.3],[1,2,3]))  # Success
        print(mergearr(["a", "b", "c"], [1,2,3]))   # Success but only bc this is Python lol
        # Failures would result from bad input (need two arrays)

    # Testing Problem 8: Find a number
    test8 = False
    if test8 == True:
        print(findnum(n10, 0))          # Success - eyeballed
        print(findnum(n100, 0))         # Success
        print(findnum(n1000, 0))        # Success
        print(findnum(n10, 100))        # Success - was not found
        print(findnum([], 0))           # Success - was not found
        print(findnum([1,2,3], 0.5))    # Success - was not found
        print(findnum([0.1,0.1], 0.1))  # Success

    # Testing Problem 9: Insert a number into an unsorted array
    test9 = False
    if test9 == True:
        print(insert(n10, 1000))        # Success
        print(insert(n100, 1000))       # Success
        print(insert(n1000, 1000))      # Success
        print(insert([], 1000))         # Success
        print(insert([0,0], 0))         # Success
        print(insert([-1.5,-2], 0.5))   # Success

    print("Tests completed in " + str(time.time() - starttime) + " seconds.")



if __name__ == "__main__":    
    main()