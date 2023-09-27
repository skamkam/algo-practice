
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

print(mergeSort([3,9,6,0,4,8,0,1,2,7,5]))

