# Name:  Sarah Kam
# Peers:  N/A
# References:  N/A

def merge(lst1: list, lst2: list) -> list:      # merges two sorted list into 1 sorted list, O(n)
    idx1 = 0
    idx2 = 0
    merged = []
    while idx1 < len(lst1) and idx2 < len(lst2):    # there are still things left to compare
        if lst1[idx1] <= lst2[idx2]:
            merged.append(lst1[idx1])
            idx1 += 1
        else:
            merged.append(lst2[idx2])
            idx2 += 1
    #assert idx1 == len(lst1) or idx2 == len(lst2)   # either of these must be true
    return merged + lst1[idx1:] + lst2[idx2:]


def mergeSort(lst: list) -> list:       # sorts list by splitting in half and sorting recursively, O(logn)
    if len(lst) < 2:    # base case
        return lst
    else:
        mid = len(lst) // 2     # integer division - rounds down
        left_sorted = mergeSort(lst[:mid])
        right_sorted = mergeSort(lst[mid:])
        return merge(left_sorted, right_sorted)

def union(lst1, lst2):
    # Put all of the entries into one list and sort it all
    # This makes checking the final list for repeats a lot easier
    union = mergeSort(lst1 + lst2)

    current = union[-1]     # last elt of union
    i = len(union)-2        # iterate from second from last to beginning
    while i >= 0:
        if union[i] == current:
            union.pop(i)
        else:
            current = union[i]
        i -= 1
    
    return union

def rec_union(lst1, lst2):
    if lst1[0] not in lst2:
        lst2.append(lst1[0])
    if len(lst1) > 1:
        lst2 = rec_union(lst1[1:], lst2)
    return lst2


def sorted_union(lst1,lst2):
    idx1 = 0
    idx2 = 0
    union = []
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] == lst2[idx2]:
            union.append(lst1[idx1])    # add one copy of it
            idx1 +=1      # move past this repeat
            idx2 +=1
        elif lst1[idx1] < lst2[idx2]:
            union.append(lst1[idx1])
            idx1 += 1
        elif lst1[idx1] > lst2[idx2]:
            union.append(lst2[idx2])
            idx2 += 1
    return union + lst1[idx1:] + lst2[idx2:]


list1 = [0,1,2,92,10,4,8,3]
list2 = [5,2,8,92,10,3]
print(union(list1, list2))
print(rec_union( list1, list2 ))

sorted_list1 = mergeSort(list1)
sorted_list2 = mergeSort(list2)
print(sorted_union(sorted_list1, sorted_list2))